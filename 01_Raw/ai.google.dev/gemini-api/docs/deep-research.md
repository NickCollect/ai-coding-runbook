---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=ja
fetched_at: 2026-05-05T13:17:55.133719+00:00
title: "Gemini Deep Research \u30a8\u30fc\u30b8\u30a7\u30f3\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

- [ホーム](https://ai.google.dev/gemini-api/docs/ホーム)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/ドキュメント)

フィードバックを送信

# Gemini Deep Research エージェント

Gemini Deep Research エージェントは、複数ステップの調査タスクを自律的に計画、実行、合成します。Gemini を搭載し、複雑な情報環境をナビゲートして、詳細な引用付きレポートを作成します。新しい機能により、エージェントと共同で計画を立てたり、MCP サーバーを使用して外部ツールに接続したり、グラフなどの可視化を含めたり、ドキュメントを直接入力として提供したりできます。

リサーチのタスクでは、反復的な検索と読み取りが行われ、完了までに数分かかることがあります。エージェントを非同期で実行し、結果をポーリングするか、更新をストリーミングするには、バックグラウンド実行（`background=true` を設定）を使用する必要があります。詳しくは、[長時間実行タスクの処理](https://ai.google.dev/gemini-api/docs/長時間実行タスクの処理)をご覧ください。

次の例は、バックグラウンドでリサーチ タスクを開始し、結果をポーリングする方法を示しています。

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.outputs[-1].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.outputs[result.outputs.length - 1].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## サポート対象のバージョン

Deep Research エージェントには次の 2 つのバージョンがあります。

- **Deep Research**（`deep-research-preview-04-2026`）: スピードと効率性を重視して設計されており、クライアント UI にストリーミングで戻すのに最適です。
- **Deep Research Max**（`deep-research-max-preview-04-2026`）: コンテキストの自動収集と統合の包括性を最大化します。

## 共同計画

共同プランニングでは、エージェントが作業を開始する前に調査の方向性を制御できます。有効にすると、エージェントはすぐに実行するのではなく、提案されたリサーチプランを返します。その後、マルチターン インタラクションを通じてプランを確認、変更、承認できます。

### ステップ 1: プランをリクエストする

最初のインタラクションで `collaborative_planning=True` を設定します。エージェントは、完全なレポートではなくリサーチプランを返します。

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.outputs[-1].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### ステップ 2: プランを調整する（省略可）

`previous_interaction_id` を使用して会話を続け、計画を繰り返し処理します。`collaborative_planning=True` を押したままにすると、プランニング モードが維持されます。

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.outputs[-1].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### ステップ 3: 承認して実行する

`collaborative_planning=False` を設定（または省略）して、プランを承認し、リサーチを開始します。

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.outputs[-1].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Visualization

`visualization` が `"auto"` に設定されている場合、エージェントは調査結果をサポートするグラフなどの視覚要素を生成できます。生成された画像はレスポンス出力に含まれ、`image` デルタとしてストリーミングされます。最適な結果を得るには、クエリでビジュアルを明示的にリクエストします（例: 「経時的な傾向を示すグラフを含めてください」、「マーケット シェアを比較するグラフィックを生成してください」）。`visualization` を `"auto"` に設定すると、この機能が有効になりますが、エージェントはプロンプトで要求された場合にのみビジュアルを生成します。

### Python

```
import base64
from IPython.display import Image, display

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for output in result.outputs:
    if output.type == "text":
        print(output.text)
    elif output.type == "image" and output.data:
        image_bytes = base64.b64decode(output.data)
        print(f"Received image: {len(image_bytes)} bytes")
        # To display in a Jupyter notebook:
        # from IPython.display import display, Image
        # display(Image(data=image_bytes))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const output of result.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    } else if (output.type === 'image' && output.data) {
        console.log(`[Image Output: ${output.data.substring(0, 20)}...]`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## サポートされているツール

Deep Research は、複数の組み込みツールと外部ツールをサポートしています。デフォルトでは（`tools` パラメータが指定されていない場合）、エージェントは Google 検索、URL コンテキスト、コード実行にアクセスできます。エージェントの機能を制限または拡張するツールを明示的に指定できます。

| ツール | Type 値 | 説明 |
| --- | --- | --- |
| Google 検索 | `google_search` | 公開ウェブを検索します。デフォルトで有効。 |
| URL コンテキスト | `url_context` | ウェブページの内容を読み取って要約します。デフォルトで有効。 |
| コードを実行する | `code_execution` | コードを実行して、計算とデータ分析を行います。デフォルトで有効。 |
| MCP サーバー | `mcp_server` | 外部ツールにアクセスするために、リモート MCP サーバーに接続します。 |
| ファイル検索 | `file_search` | アップロードしたドキュメント コーパスを検索します。 |

### Google 検索

Google 検索のみをツールとして明示的に有効にします。

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### URL コンテキスト

エージェントに特定のウェブページを読み取って要約する権限を付与します。

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### コードを実行する

エージェントが計算とデータ分析のためにコードを実行できるようにします。

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Calculate the 50th Fibonacci number.",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### MCP サーバー

ツールの構成でサーバーの `name` と `url` を指定します。認証情報を受け渡し、エージェントが呼び出すことができるツールを制限することもできます。

| フィールド | 型 | 必須 / 省略可 | 説明 |
| --- | --- | --- | --- |
| `type` | `string` | はい | `"mcp_server"` を指定します。 |
| `name` | `string` | いいえ | MCP サーバーの表示名。 |
| `url` | `string` | いいえ | MCP サーバー エンドポイントの完全な URL。 |
| `headers` | `object` | いいえ | サーバーへのすべてのリクエストとともに HTTP ヘッダーとして送信される Key-Value ペア（認証トークンなど）。 |
| `allowed_tools` | `array` | いいえ | エージェントが呼び出すことができるサーバーのツールを制限します。 |

#### 基本的な使用方法

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### ファイル検索

[ファイル検索](https://ai.google.dev/gemini-api/docs/ファイル検索)ツールを使用して、エージェントが自分のデータにアクセスできるようにします。

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## 操作性と書式設定

プロンプトで特定の形式の指示を指定することで、エージェントの出力を制御できます。これにより、レポートを特定のセクションとサブセクションに構成したり、データテーブルを含めたり、さまざまなユーザー（「技術者向け」、「経営幹部向け」、「カジュアル」など）に合わせてトーンを調整したりできます。

入力テキストで目的の出力形式を明示的に定義します。

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## マルチモーダル入力

Deep Research は、画像やドキュメント（PDF）などのマルチモーダル入力をサポートしているため、エージェントは視覚コンテンツを分析し、提供された入力によってコンテキスト化されたウェブベースの調査を実施できます。

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.outputs[-1].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.outputs[result.outputs.length - 1].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### ドキュメントの理解

ドキュメントをマルチモーダル入力として直接渡します。エージェントは、提供されたドキュメントを分析し、その内容に基づいて調査を行います。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## 長時間実行タスクの処理

Deep Research は、計画、検索、読解、執筆を含む複数ステップのプロセスです。通常、このサイクルは同期 API 呼び出しの標準のタイムアウト上限を超えます。

`background=True` を使用するには、エージェントが必要です。API は、部分的な `Interaction` オブジェクトをすぐに返します。`id` プロパティを使用すると、ポーリング用のインタラクションを取得できます。インタラクションの状態が `in_progress` から `completed` または `failed` に移行します。

### ストリーミング

Deep Research は、思考の要約、テキスト出力、生成された画像など、調査の進捗状況に関するリアルタイムの更新情報を受信するためのストリーミングをサポートしています。`stream=True` と `background=True` を設定する必要があります。

中間推論ステップ（思考）と進行状況の更新を受け取るには、`agent_config` で `thinking_summaries` を `"auto"` に設定して、**思考の要約**を有効にする必要があります。これがないと、ストリームは最終結果のみを提供する可能性があります。

#### ストリーム イベントのタイプ

| イベントの種類 | デルタタイプ | 説明 |
| --- | --- | --- |
| `content.delta` | `thought_summary` | エージェントからの中間推論ステップ。 |
| `content.delta` | `text` | 最終的なテキスト出力の一部。 |
| `content.delta` | `image` | 生成された画像（base64 エンコード）。 |

次の例では、調査タスクを開始し、自動再接続でストリームを処理します。`interaction_id` と `last_event_id` を追跡し、接続が切断された場合（600 秒のタイムアウト後など）に、中断したところから再開できるようにします。

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for chunk in stream:
        if chunk.event_type == "interaction.start":
            interaction_id = chunk.interaction.id
        if chunk.event_id:
            last_event_id = chunk.event_id
        if chunk.event_type == "content.delta":
            if chunk.delta.type == "text":
                print(chunk.delta.text, end="", flush=True)
            elif chunk.delta.type == "thought_summary":
                print(f"Thought: {chunk.delta.content.text}", flush=True)
        elif chunk.event_type in ("interaction.complete", "error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const chunk of stream) {
        if (chunk.event_type === 'interaction.start') {
            interactionId = chunk.interaction.id;
        }
        if (chunk.event_id) lastEventId = chunk.event_id;
        if (chunk.event_type === 'content.delta') {
            if (chunk.delta.type === 'text') {
                process.stdout.write(chunk.delta.text);
            } else if (chunk.delta.type === 'thought_summary') {
                console.log(`Thought: ${chunk.delta.content.text}`);
            }
        } else if (['interaction.complete', 'error'].includes(chunk.event_type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## フォローアップの質問とやり取り

エージェントが最終レポートを返した後に会話を続けるには、`previous_interaction_id` を使用します。これにより、タスク全体を再開することなく、調査の特定のセクションについて説明、要約、詳細を求めることができます。

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Gemini Deep Research エージェントを使用する場合

Deep Research は単なるモデルではなく、**エージェント**です。低レイテンシのチャットではなく、「アナリスト イン ア ボックス」のアプローチを必要とするワークロードに最適です。

| 機能 | 標準の Gemini モデル | Gemini Deep Research エージェント |
| --- | --- | --- |
| **レイテンシ** | 秒 | 分（非同期/バックグラウンド） |
| **プロセス** | 生成 -> 出力 | 計画 -> 検索 -> 読み取り -> 反復 -> 出力 |
| **出力** | 会話テキスト、コード、短い要約 | 詳細なレポート、長文の分析、比較表 |
| **最適な用途** | Chatbot、抽出、クリエイティブ ライティング | 市場分析、デュー デリジェンス、文献レビュー、競合状況の把握 |

## エージェントの構成

Deep Research は、`agent_config` パラメータを使用して動作を制御します。次のフィールドを含む辞書として渡します。

| フィールド | タイプ | デフォルト | 説明 |
| --- | --- | --- | --- |
| `type` | `string` | 必須 | `"deep-research"` を指定します。 |
| `thinking_summaries` | `string` | `"none"` | ストリーミング中に中間推論ステップを受け取る場合は、`"auto"` に設定します。無効にするには、`"none"` に設定します。 |
| `visualization` | `string` | `"auto"` | エージェントが生成したグラフと画像を有効にするには、`"auto"` に設定します。無効にするには、`"off"` に設定します。 |
| `collaborative_planning` | `boolean` | `false` | `true` に設定すると、調査開始前に複数ターンのプランのレビューが有効になります。 |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## リリース情報と料金

Gemini Deep Research Agent には、Google AI Studio の Interactions API と Gemini API を使用してアクセスできます。

料金は、基盤となる Gemini モデルとエージェントが使用する特定のツールに基づく[従量課金制モデル](https://ai.google.dev/gemini-api/docs/従量課金制モデル)に従います。リクエストが 1 つの出力につながる標準的なチャット リクエストとは異なり、Deep Research タスクはエージェント ワークフローです。1 つのリクエストで、計画、検索、読み取り、推論の自律ループがトリガーされます。

### 推定費用

費用は、必要な調査の深さによって異なります。エージェントは、プロンプトに回答するために必要な読み取りと検索の量を自律的に決定します。

- **Deep Research**（`deep-research-preview-04-2026`）: 中程度の分析を必要とする一般的なクエリの場合、エージェントは通常、約 80 個の検索クエリ、約 25 万個の入力トークン（約 50 ～ 70% がキャッシュに保存）、約 6 万個の出力トークンを使用します。
  - **合計（推定）:** タスクあたり$1.00 ～$3.00
- **Deep Research Max**（`deep-research-max-preview-04-2026`）: 競合他社の状況の詳細な分析や広範なデュー デリジェンスを行う場合、エージェントは最大で約 160 件の検索クエリ、約 90 万個の入力トークン（約 50 ～ 70% がキャッシュに保存）、約 8 万個の出力トークンを使用する可能性があります。
  - **合計（推定）:** タスクあたり$3.00 ～$7.00

## 安全上の考慮事項

エージェントにウェブとプライベート ファイルへのアクセス権を付与する場合は、安全性のリスクを慎重に検討する必要があります。

- **ファイルを使用したプロンプト インジェクション:** エージェントは、ユーザーが提供したファイルの内容を読み取ります。アップロードされたドキュメント（PDF、テキスト ファイル）が信頼できるソースからのものであることを確認します。悪意のあるファイルには、エージェントの出力を操作するように設計された隠しテキストが含まれている可能性があります。
- **ウェブ コンテンツのリスク:** エージェントが公開ウェブを検索します。堅牢なセーフティ フィルタを実装していますが、エージェントが悪意のあるウェブページに遭遇して処理するリスクがあります。回答で提供された `citations` を確認して、ソースを検証することをおすすめします。
- **データ流出:** エージェントに機密性の高い内部データの要約を依頼する際に、エージェントにウェブの閲覧も許可している場合は注意が必要です。

## ベスト プラクティス

- **不明な場合のプロンプト:** データが欠落している場合の処理方法をエージェントに指示します。たとえば、プロンプトに「2025 年の具体的な数値が利用できない場合は、推定ではなく、予測または利用不可であることを明示的に記載してください」と追加します。
- **コンテキストを提供する:** 入力プロンプトで背景情報や制約を直接指定して、エージェントの調査をグラウンディングします。
- **共同プランニングを使用する:** 複雑なクエリの場合は、共同プランニングを有効にして、実行前にリサーチプランを確認して調整します。
- **マルチモーダル入力:** Deep Research エージェントはマルチモーダル入力をサポートしています。コストが増加し、コンテキスト ウィンドウのオーバーフローのリスクが高まるため、慎重に使用してください。

## 制限事項

- **ベータ版のステータス**: Interactions API は公開ベータ版です。機能とスキーマは変更される可能性があります。
- **カスタムツール:** 現在、カスタムの関数呼び出しツールを提供することはできませんが、Deep Research エージェントでリモート MCP（Model Context Protocol）サーバーを使用できます。
- **構造化出力:** Deep Research エージェントは現在、構造化出力をサポートしていません。
- **最大調査時間:** Deep Research エージェントの最大調査時間は 60 分です。ほとんどのタスクは 20 分以内に完了します。
- **ストアの要件:** `background=True` を使用したエージェントの実行には `store=True` が必要です。
- **Google 検索:** [Google 検索](https://ai.google.dev/gemini-api/docs/Google 検索)はデフォルトで有効になっており、グラウンディングされた検索結果には[特定の制限](https://ai.google.dev/gemini-api/docs/特定の制限)が適用されます。

## 次のステップ

- [操作用 API](https://ai.google.dev/gemini-api/docs/操作用 API) の詳細をご確認ください。
- [Gemini API クックブックの Deep Research](https://ai.google.dev/gemini-api/docs/Gemini API クックブックの Deep Research) を試す。
- [ファイル検索](https://ai.google.dev/gemini-api/docs/ファイル検索)ツールを使用して独自のデータを使用する方法について説明します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://ai.google.dev/gemini-api/docs/クリエイティブ・コモンズの表示 4.0 ライセンス)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://ai.google.dev/gemini-api/docs/Apache 2.0 ライセンス)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://ai.google.dev/gemini-api/docs/Google Developers サイトのポリシー)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください
