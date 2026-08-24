---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=ja
fetched_at: 2026-08-24T02:27:56.753107+00:00
title: "Gemini \u3068 Temporal \u3092\u4f7f\u7528\u3057\u305f\u6c38\u7d9a\u7684\u306a AI \u30a8\u30fc\u30b8\u30a7\u30f3\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini と Temporal を使用した永続的な AI エージェント

このチュートリアルでは、推論に
[Gemini API](https://arxiv.org/abs/2210.03629) を使用し、永続化に [Temporal](https://temporal.io/) を使用する
ReAct スタイルのエージェント ループを構築する手順について説明します。このチュートリアルの完全なソースコードは
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini)で入手できます。

エージェントは、天気予報の検索や IP アドレスのジオロケーションなどのツールを呼び出すことができ、応答に必要な十分な情報が得られるまでループします。

一般的なエージェント デモとの違いは**耐久性** です。すべての LLM 呼び出し、すべてのツール呼び出し、エージェント
ループのすべてのステップは Temporal によって永続化されます。プロセスがクラッシュした場合、ネットワークが切断された場合、API
がタイムアウトした場合、Temporal は自動的に再試行し、最後に完了したステップから再開します。会話履歴が失われることも、ツール呼び出しが誤って繰り返されることもありません。

## アーキテクチャ

このアーキテクチャは次の 3 つの部分で構成されます。

- **ワークフロー:** 実行ロジックをオーケストレートするエージェント ループ。
- **アクティビティ:** Temporal が永続化する個々の作業単位（LLM 呼び出し、ツール呼び出し）。
- **ワーカー:** ワークフローとアクティビティを実行するプロセス。

この例では、これら 3 つの要素をすべて 1 つのファイル（`durable_agent_worker.py`）に配置します。実際の環境では、さまざまなデプロイとスケーラビリティのメリットを得るために、これらを分離します。エージェントにプロンプトを提供するコードは、2 つ目のファイル（`start_workflow.py`）に配置します。

## 前提条件

このガイドを完了するには、次のものが必要です。

- Gemini API キー。[Google AI Studio で無料で作成できます。](https://aistudio.google.com/apikey?hl=ja)
- [Python](https://www.python.org/downloads/) バージョン 3.10 以降。
- ローカル
  開発用サーバーを実行するための [Temporal CLI](https://docs.temporal.io/cli)。

## 設定

始める前に、
[Temporal 開発用サーバー](https://docs.temporal.io/cli#start-dev-server)
がローカルで実行されていることを確認してください。

```
temporal server start-dev
```

次に、必要な依存関係をインストールします。

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Gemini API キーを使用して、プロジェクト ディレクトリに `.env` ファイルを作成します。API キーは
[Google AI Studio](https://aistudio.google.com/apikey?hl=ja)から取得できます。

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## 実装

このチュートリアルの残りの部分では、`durable_agent_worker.py` を上から下まで順に説明し、エージェントを段階的に構築していきます。ファイルを作成して、手順に沿って進めてください。

### インポートとサンドボックスの設定

最初に、事前に定義する必要があるインポートから始めます。`workflow.unsafe.imports_passed_through()`
ブロックは、特定のモジュールを制限なく通過させるように Temporal のワークフロー
サンドボックスに指示します。これは、いくつかのライブラリ（特に `urllib.request.Request` をサブクラス化する
`httpx`）が、サンドボックスでブロックされるパターンを使用しているため必要です。

```
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    import pydantic_core  # noqa: F401
    import annotated_types  # noqa: F401

    import httpx
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
```

### システム指示

次に、エージェントの個性を定義します。システムの指示は、モデルの動作方法を指定します。このエージェントは、ツールが必要ない場合は俳句で応答するように指示されています。

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### ツール定義

次に、エージェントが使用できるツールを定義します。各ツールは、説明的なドキュメント文字列を持つ非同期関数です。パラメータを受け取るツールは、単一の引数として
Pydantic モデルを使用します。これは Temporal
のベストプラクティスであり、時間の経過とともにオプションのフィールドを追加してもアクティビティの署名を安定させることができます。

```
import json

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class GetWeatherAlertsRequest(BaseModel):
    """Request model for getting weather alerts."""

    state: str = Field(description="Two-letter US state code (e.g. CA, NY)")

async def get_weather_alerts(request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        request: The request object containing:
            - state: Two-letter US state code (e.g. CA, NY)
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=5.0)
        response.raise_for_status()
        return json.dumps(response.json())
```

次に、IP アドレスのジオロケーションのツールを定義します。

```
class GetLocationRequest(BaseModel):
    """Request model for getting location info from an IP address."""

    ipaddress: str = Field(description="An IP address")

async def get_ip_address() -> str:
    """Get the public IP address of the current machine."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://icanhazip.com")
        response.raise_for_status()
        return response.text.strip()

async def get_location_info(request: GetLocationRequest) -> str:
    """Get the location information for an IP address including city, state, and country.

    Args:
        request: The request object containing:
            - ipaddress: An IP address to look up
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{request.ipaddress}")
        response.raise_for_status()
        result = response.json()
        return f"{result['city']}, {result['regionName']}, {result['country']}"
```

### ツール レジストリ

次に、ツール名をハンドラ関数にマッピングするレジストリを作成します。
`get_tools()` 関数は、`FunctionDeclaration` オブジェクト
を呼び出し可能オブジェクトから `FunctionDeclaration.from_callable_with_api_option()` を使用して生成します。

```
from typing import Any, Awaitable, Callable

ToolHandler = Callable[..., Awaitable[Any]]

def get_handler(tool_name: str) -> ToolHandler:
    """Get the handler function for a given tool name."""
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    raise ValueError(f"Unknown tool name: {tool_name}")

def get_tools() -> types.Tool:
    """Get the Tool object containing all available function declarations.

    Uses FunctionDeclaration.from_callable_with_api_option() from the Google GenAI SDK
    to generate tool definitions from the handler functions.
    """
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_weather_alerts, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_location_info, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_ip_address, api_option="GEMINI_API"
            ),
        ]
    )
```

### LLM アクティビティ

Gemini API を呼び出すアクティビティを定義します。`GeminiChatRequest` と `GeminiChatResponse`
のデータクラスはコントラクトを定義します。

LLM 呼び出しとツール呼び出しが別々のタスクとして処理されるように、自動関数呼び出しを無効にします。これにより、エージェントの永続性が向上します。Temporal
は永続的に再試行を処理するため、SDK の組み込み再試行（`attempts=1`）も無効にします。

```
import os
from dataclasses import dataclass

from temporalio import activity

@dataclass
class GeminiChatRequest:
    """Request parameters for a Gemini chat completion."""

    model: str
    system_instruction: str
    contents: list[types.Content]
    tools: list[types.Tool]

@dataclass
class GeminiChatResponse:
    """Response from a Gemini chat completion."""

    text: str | None
    function_calls: list[dict[str, Any]]
    raw_parts: list[types.Part]

@activity.defn
async def generate_content(request: GeminiChatRequest) -> GeminiChatResponse:
    """Execute a Gemini chat completion with tool support."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    config = types.GenerateContentConfig(
        system_instruction=request.system_instruction,
        tools=request.tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    response = await client.aio.models.generate_content(
        model=request.model,
        contents=request.contents,
        config=config,
    )

    function_calls = []
    raw_parts = []
    text_parts = []

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            raw_parts.append(part)
            if part.function_call:
                function_calls.append(
                    {
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args) if part.function_call.args else {},
                    }
                )
            elif part.text:
                text_parts.append(part.text)

    text = "".join(text_parts) if text_parts and not function_calls else None

    return GeminiChatResponse(
        text=text,
        function_calls=function_calls,
        raw_parts=raw_parts,
    )
```

### 動的ツール アクティビティ

次に、ツールを実行するアクティビティを定義します。これには Temporal の動的アクティビティ機能を使用します。ツール
ハンドラ（呼び出し可能オブジェクト）は、`get_handler` 関数を使用してツール
レジストリから取得されます。これにより、さまざまなツールとシステム指示を指定するだけで、さまざまなエージェントを定義できます。エージェント
ループを実装するワークフローを変更する必要はありません。

アクティビティはハンドラの署名を調べて、引数を渡す方法を決定します。ハンドラが Pydantic モデルを想定している場合、Gemini が生成するネストされた出力
形式（フラットな `{"state": "CA"}` ではなく `{"request": {"state": "CA"}}` など）を処理します。

```
import inspect
from collections.abc import Sequence

from temporalio.common import RawValue

@activity.defn(dynamic=True)
async def dynamic_tool_activity(args: Sequence[RawValue]) -> dict:
    """Execute a tool dynamically based on the activity name."""
    tool_name = activity.info().activity_type
    tool_args = activity.payload_converter().from_payload(args[0].payload, dict)
    activity.logger.info(f"Running dynamic tool '{tool_name}' with args: {tool_args}")

    handler = get_handler(tool_name)

    if not inspect.iscoroutinefunction(handler):
        raise TypeError("Tool handler must be async (awaitable).")

    sig = inspect.signature(handler)
    params = list(sig.parameters.values())

    if len(params) == 0:
        result = await handler()
    else:
        param = params[0]
        param_name = param.name
        ann = param.annotation

        if isinstance(ann, type) and issubclass(ann, BaseModel):
            nested_args = tool_args.get(param_name, tool_args)
            result = await handler(ann(**nested_args))
        else:
            result = await handler(**tool_args)

    activity.logger.info(f"Tool '{tool_name}' result: {result}")
    return result
```

### エージェント ループ ワークフロー

これで、エージェントの構築を完了するためのすべての要素が揃いました。`AgentWorkflow` クラスは、エージェント
ループを含むワークフローを実装します。このループ内で、LLM はアクティビティを介して呼び出され（永続化されます）、出力が検査されます。LLM
によってツールが選択された場合は、`dynamic_tool_activity` を介して呼び出されます。

このシンプルな ReAct スタイルのエージェントでは、LLM がツールを使用しないことを選択すると、ループは完了とみなされ、最終的な LLM
の結果が返されます。

```
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Agentic loop workflow that uses Gemini for LLM calls and executes tools."""

    @workflow.run
    async def run(self, input: str) -> str:
        contents: list[types.Content] = [
            types.Content(role="user", parts=[types.Part.from_text(text=input)])
        ]

        tools = [get_tools()]

        while True:
            result = await workflow.execute_activity(
                generate_content,
                GeminiChatRequest(
                    model="gemini-3.5-flash",
                    system_instruction=SYSTEM_INSTRUCTIONS,
                    contents=contents,
                    tools=tools,
                ),
                start_to_close_timeout=timedelta(seconds=60),
            )

            if result.function_calls:
                # Sending the complete raw_parts here ensures Gemini 3 thought
                # signatures are propagated correctly.
                contents.append(types.Content(role="model", parts=result.raw_parts))

                for function_call in result.function_calls:
                    tool_result = await self._handle_function_call(function_call)

                    contents.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call["name"],
                                    response={"result": tool_result},
                                )
                            ],
                        )
                    )
            else:
                return result.text
            # Leave this in place. You will un-comment it during a durability
            # test later on.
            # await asyncio.sleep(10)

    async def _handle_function_call(self, function_call: dict) -> str:
        """Execute a tool via dynamic activity and return the result."""
        tool_name = function_call["name"]
        tool_args = function_call.get("args", {})

        result = await workflow.execute_activity(
            tool_name,
            tool_args,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return result
```

エージェント ループは完全に永続化されます。ループを数回繰り返した後にエージェント ワーカーがクラッシュした場合、Temporal
は中断したところから正確に再開します。すでに実行された LLM 呼び出しやツール呼び出しを再度呼び出す必要はありません。

### ワーカーの起動

最後に、すべてを接続します。コードは、単一のプロセスで実行されているように見える方法で必要なビジネス
ロジックを実装しますが、Temporal を使用すると、ワークフローとアクティビティ間の通信が Temporal
によって提供されるメッセージングを介して行われるイベント ドリブン システム（具体的にはイベント ソーシング）になります。

Temporal ワーカーは Temporal
サービスに接続し、ワークフローとアクティビティのタスクのスケジューラとして機能します。ワーカーはワークフローと両方のアクティビティを登録し、タスクのリッスンを開始します。

```
import asyncio
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter
from temporalio.envconfig import ClientConfig
from temporalio.worker import Worker

async def main():
    config = ClientConfig.load_client_connect_config()
    config.setdefault("target_host", "localhost:7233")
    client = await Client.connect(
        **config,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="gemini-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            generate_content,
            dynamic_tool_activity,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
```

## クライアント スクリプト

クライアント スクリプト（`start_workflow.py`）を作成します。クエリを送信して結果を待ちます。エージェント
ワーカーで参照されているのと同じタスクキューに接続します。`start_workflow` スクリプトは、ユーザー
プロンプトを含むワークフロー タスクをそのタスクキューにディスパッチし、エージェントの実行を開始します。

```
import asyncio
import sys
import uuid

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Tell me about recursion"

    result = await client.execute_workflow(
        "AgentWorkflow",
        query,
        id=f"gemini-agent-id-{uuid.uuid4()}",
        task_queue="gemini-agent-python-task-queue",
    )
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## エージェントを実行する

まだの場合は、Temporal 開発用サーバーを起動します。

```
temporal server start-dev
```

新しいターミナル ウィンドウで、エージェント ワーカーを起動します。

```
python -m durable_agent_worker
```

3 つ目のターミナル ウィンドウで、エージェントにクエリを送信します。

```
python -m start_workflow "are there any weather alerts for where I am?"
```

`durable_agent_worker` のターミナルに出力される、エージェント
ループの各イテレーションで発生するアクションを確認します。LLM は、使用可能な一連のツールを呼び出すことで、ユーザー
リクエストを満たすことができます。実行されたステップは、Temporal UI（`http://localhost:8233/namespaces/default/workflows`）で確認できます。

いくつかのプロンプトを試して、エージェントが推論してツールを呼び出すことを確認します。

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

最後のプロンプトではツールは必要ないため、エージェントは `SYSTEM_INSTRUCTIONS` に基づいて俳句で応答します。

## 耐久性をテストする（省略可）

Temporal を基盤に構築することで、エージェントは障害からシームレスに復旧できます。これは、2 つの異なるテストで確認できます。

### ネットワーク停止をシミュレートする

このテストでは、パソコンのインターネット接続を一時的に無効にし、ワークフローを送信して、Temporal
が自動的に再試行するのを確認してから、ネットワークを復元して復旧を確認します。

1. パソコンをインターネットから切断します（Wi-Fi をオフにするなど）。
2. ワークフローを送信します。

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Temporal UI（`http://localhost:8233`）を確認します。LLM アクティビティが失敗し、Temporal がバックグラウンドで再試行を自動的に管理していることがわかります。
4. インターネットに再接続します。
5. 次の自動再試行で Gemini API に正常に到達し、ターミナルに最終結果が出力されます。

### ワーカーのクラッシュから復旧する

このテストでは、実行中にワーカーを強制終了して再起動します。Temporal はワークフロー履歴（イベント
ソーシング）を再生し、最後に完了したアクティビティから再開します。すでに完了した LLM 呼び出しとツール呼び出しは繰り返されません。

1. ワーカーを強制終了する時間を確保するため、`durable_agent_worker.py` を開き、`AgentWorkflow`
   `run` ループ内の `await asyncio.sleep(10)` のコメント化を一時的に解除します。
2. ワーカーを再起動します。

   ```
   python -m durable_agent_worker
   ```
3. 複数のツールをトリガーするクエリを送信します。

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. 完了する前にいつでもワーカー プロセスを強制終了します（ワーカー ターミナルで `Ctrl-C` を押すか、バックグラウンドで実行している場合は `kill %1` を使用します）。
5. ワーカーを再起動します。

   ```
   python -m durable_agent_worker
   ```

Temporal はワークフロー履歴を再生します。すでに完了した LLM 呼び出しとツール呼び出しは**再実行されません**
。結果は履歴（イベントログ）から即座に再生されます。ワークフローは正常に完了します。

## その他のリソース

- [Temporal のドキュメント](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [このチュートリアルのソースコード](https://github.com/temporal-community/durable-react-agent-gemini)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
