---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=ja
fetched_at: 2026-06-22T06:32:41.846940+00:00
title: "Gemini \u3068 LlamaIndex \u3092\u4f7f\u7528\u3057\u305f\u30ea\u30b5\u30fc\u30c1 \u30a8\u30fc\u30b8\u30a7\u30f3\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini と LlamaIndex を使用したリサーチ エージェント

LlamaIndex は、データに接続された LLM を使用してナレッジ エージェントを構築するためのフレームワークです。この例では、リサーチ エージェント用のマルチエージェント ワークフローを構築する方法を示します。LlamaIndex では、[`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
はエージェント システムとマルチエージェント システムの構成要素です。

Gemini API キーが必要です。キーがない場合は、Google AI Studio で
[取得できます](https://aistudio.google.com/apikey?hl=ja)。
まず、必要な LlamaIndex ライブラリをすべてインストールします。LlamaIndex は、内部で `google-genai` パッケージを使用します。

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## LlamaIndex で Gemini を設定する

LlamaIndex エージェントのエンジンは、推論とテキスト処理を処理する LLM です。この例では、Gemini 3 Flash を使用します。API キーを環境変数として[設定してください
。](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## ビルドツール

エージェントはツールを使用して、ウェブの検索や情報の保存など、外部の世界とやり取りします。[LlamaIndex のツール](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
は、通常の Python 関数にすることも、既存の `ToolSpecs` からインポートすることもできます。
Gemini には、Google 検索を使用するための組み込みツールが用意されています。ここでは、このツールを使用します。

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3.5-flash",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

検索が必要なクエリを使用して、LLM インスタンスをテストします。このガイドでは、実行中のイベント ループ（`python -m asyncio` や Google Colab など）を想定しています。

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

リサーチ エージェントは、Python 関数をツールとして使用します。このタスクを実行するシステムを構築する方法はたくさんあります。この例では、次のものを使用します。

1. `search_web` は、Gemini と Google 検索を使用して、指定されたトピックに関する情報をウェブで検索します。
2. `record_notes` は、ウェブで見つかった調査結果を状態に保存して、他のツールで使用できるようにします。
3. `write_report` は、`ResearchAgent` が見つけた情報を使用してレポートを作成します。
4. `review_report` はレポートを確認し、フィードバックを提供します。

`Context` クラスは、エージェントとツールの間で状態を渡します。各エージェントは、システムの現在の状態にアクセスできます。

```
from llama_index.core.workflow import Context

async def search_web(ctx: Context, query: str) -> str:
    """Useful for searching the web about a specific query or topic"""
    response = await llm_with_search.acomplete(f"""Please research given this query or topic,
    and return the result\n<query_or_topic>{query}</query_or_topic>""")
    return response

async def record_notes(ctx: Context, notes: str, notes_title: str) -> str:
    """Useful for recording notes on a given topic."""
    current_state = await ctx.store.get("state")
    if "research_notes" not in current_state:
        current_state["research_notes"] = {}
    current_state["research_notes"][notes_title] = notes
    await ctx.store.set("state", current_state)
    return "Notes recorded."

async def write_report(ctx: Context, report_content: str) -> str:
    """Useful for writing a report on a given topic."""
    current_state = await ctx.store.get("state")
    current_state["report_content"] = report_content
    await ctx.store.set("state", current_state)
    return "Report written."

async def review_report(ctx: Context, review: str) -> str:
    """Useful for reviewing a report and providing feedback."""
    current_state = await ctx.store.get("state")
    current_state["review"] = review
    await ctx.store.set("state", current_state)
    return "Report reviewed."
```

## マルチエージェント アシスタントを構築する

マルチエージェント システムを構築するには、エージェントとそのインタラクションを定義します。
システムには 3 つのエージェントがあります。

1. `ResearchAgent` は、指定されたトピックに関する情報をウェブで検索します。
2. `WriteAgent` は、`ResearchAgent` が見つけた情報を使用してレポートを作成します。
3. `ReviewAgent` はレポートを確認し、フィードバックを提供します。

この例では、`AgentWorkflow` クラスを使用して、これらのエージェントを順番に実行するマルチエージェント システムを作成します。各エージェントは、実行する内容を指示する `system_prompt` を受け取り、他のエージェントとの連携方法を提案します。

必要に応じて、`can_handoff_to` を使用して、マルチエージェント システムが通信できる他のエージェントを指定できます（指定しない場合、システムは独自に判断しようとします）。

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)
from llama_index.core.agent.workflow import FunctionAgent, ReActAgent

research_agent = FunctionAgent(
    name="ResearchAgent",
    description="Useful for searching the web for information on a given topic and recording notes on the topic.",
    system_prompt=(
        "You are the ResearchAgent that can search the web for information on a given topic and record notes on the topic. "
        "Once notes are recorded and you are satisfied, you should hand off control to the WriteAgent to write a report on the topic."
    ),
    llm=llm,
    tools=[search_web, record_notes],
    can_handoff_to=["WriteAgent"],
)

write_agent = FunctionAgent(
    name="WriteAgent",
    description="Useful for writing a report on a given topic.",
    system_prompt=(
        "You are the WriteAgent that can write a report on a given topic. "
        "Your report should be in a markdown format. The content should be grounded in the research notes. "
        "Once the report is written, you should get feedback at least once from the ReviewAgent."
    ),
    llm=llm,
    tools=[write_report],
    can_handoff_to=["ReviewAgent", "ResearchAgent"],
)

review_agent = FunctionAgent(
    name="ReviewAgent",
    description="Useful for reviewing a report and providing feedback.",
    system_prompt=(
        "You are the ReviewAgent that can review a report and provide feedback. "
        "Your feedback should either approve the current report or request changes for the WriteAgent to implement."
    ),
    llm=llm,
    tools=[review_report],
    can_handoff_to=["ResearchAgent","WriteAgent"],
)
```

エージェントが定義されたので、`AgentWorkflow` を作成して実行できます。

```
from llama_index.core.agent.workflow import AgentWorkflow

agent_workflow = AgentWorkflow(
    agents=[research_agent, write_agent, review_agent],
    root_agent=research_agent.name,
    initial_state={
        "research_notes": {},
        "report_content": "Not written yet.",
        "review": "Review required.",
    },
)
```

ワークフローの実行中に、イベント、ツール呼び出し、更新をコンソールにストリーミングできます。

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)

research_topic = """Write me a report on the history of the web.
Briefly describe the history of the world wide web, including
the development of the internet and the development of the web,
including 21st century developments"""

handler = agent_workflow.run(
    user_msg=research_topic
)

current_agent = None
current_tool_calls = ""
async for event in handler.stream_events():
    if (
        hasattr(event, "current_agent_name")
        and event.current_agent_name != current_agent
    ):
        current_agent = event.current_agent_name
        print(f"\n{'='*50}")
        print(f"🤖 Agent: {current_agent}")
        print(f"{'='*50}\n")
    elif isinstance(event, AgentOutput):
        if event.response.content:
            print("📤 Output:", event.response.content)
        if event.tool_calls:
            print(
                "🛠️  Planning to use tools:",
                [call.tool_name for call in event.tool_calls],
            )
    elif isinstance(event, ToolCallResult):
        print(f"🔧 Tool Result ({event.tool_name}):")
        print(f"  Arguments: {event.tool_kwargs}")
        print(f"  Output: {event.tool_output}")
    elif isinstance(event, ToolCall):
        print(f"🔨 Calling Tool: {event.tool_name}")
        print(f"  With arguments: {event.tool_kwargs}")
```

ワークフローが完了したら、レポートの最終出力と、レビュー エージェントからの最終レビューの状態を出力できます。

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## カスタム ワークフローでさらに活用する

`AgentWorkflow` は、マルチエージェント システムを始めるのに最適な方法です。ただし、より詳細な制御が必要な場合はどうすればよいでしょうか。 ワークフローを最初から構築できます。独自のワークフローを構築する理由としては、次のようなものがあります。

- **プロセスをより詳細に制御する**: エージェントがたどる正確なパスを決定できます。これには、ループの作成、特定の時点での意思決定、エージェントが異なるタスクを並行して実行することが含まれます。
- **複雑なデータを使用する**: プレーン テキストを超えて、カスタム ワークフローでは、入力と出力に JSON オブジェクトやカスタム クラスなど、より構造化されたデータを使用できます。
- **さまざまなメディアを扱う**: テキストだけでなく、画像、音声、動画も理解して処理できるエージェントを構築します。
- **よりスマートな計画**: エージェントが作業を開始する前に
  詳細な計画を作成するワークフローを設計できます。これは、複数のステップを必要とする複雑なタスクに便利です。
- **自己修正を有効にする**: 自分の作業を確認できるエージェントを作成します。出力が十分でない場合、エージェントは結果が完璧になるまで改善を繰り返します。

LlamaIndex Workflows の詳細については、[LlamaIndex Workflows
ドキュメント](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-10 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-10 UTC。"],[],[]]
