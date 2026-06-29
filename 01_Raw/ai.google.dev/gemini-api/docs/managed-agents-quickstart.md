---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja
fetched_at: 2026-06-29T05:41:50.217409+00:00
title: "Managed Agents \u306e\u30af\u30a4\u30c3\u30af\u30b9\u30bf\u30fc\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Managed Agents のクイックスタート

このガイドでは、[Antigravity エージェント](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=ja)を使用して、Gemini API でマネージド エージェントを作成して使用する方法について説明します。最初のエージェント呼び出しを行い、複数ターンの会話を続け、レスポンスをストリーミングし、サンドボックスからファイルをダウンロードして、Antigravity マネージド エージェントを操作します。

## 最初のエージェント インタラクションを実行する

[Interactions API](https://ai.google.dev/gemini-api/docs?hl=ja) を 1 回呼び出すと、Linux サンドボックスがプロビジョニングされ、エージェント ループが実行されて、結果が返されます。次の 3 つのパラメータを定義します。

- 事前定義された汎用マネージド エージェントの現在のバージョンである `agent` を `"antigravity-preview-05-2026",` として渡します。
- `environment="remote"` を定義して、新しいサンドボックス環境をプロビジョニングします。
- エージェントに実行させたい内容を定義して、入力を作成します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

レスポンスは `Interaction` オブジェクトを返します。`interaction.id` と `interaction.environment_id` を保存して、同じサンドボックスで会話を続けます。`interaction.output_text` を使用して、エージェントの最終レスポンスにアクセスします。`interaction.steps` には、エージェントが実行した各ステップ（推論、ツール呼び出し、コード実行）が一覧表示されます。

## 会話を続ける（複数ターン）

API は、次の 2 つの独立した状態ディメンションを追跡します。

- **会話のコンテキスト:** チャット履歴、推論トレース、ツールの使用、`previous_interaction_id` の使用。
- [**環境の状態:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja) ファイル、インストールされているパッケージ、サンドボックスの状態、`environment` の使用。

再開するには、両方をそれぞれの場所に渡します。

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

ターン 1 のファイル（`fibonacci.txt`）はターン 2 でも保持されます。エージェントは会話のコンテキストも保持します。

これらは個別に組み合わせて使用できます。

- **会話をクリアしてファイルを保持する:** `previous_interaction_id` を省略し、`environment` を使用して環境 ID のみを渡して、同じワークスペースで新しい会話を開始します。
- **会話を保持して新しいワークスペースを作成する:** `previous_interaction_id` を渡し、`environment="remote"` を設定して新しいサンドボックスを作成します。

### コンテキストの自動圧縮

長時間にわたる複数ターンの会話では、推論ステップ、ツール呼び出し、大きなファイル コンテンツの未加工の履歴が急速に増加し、コンテキスト空間を大量に消費する可能性があります。トークン上限エラーを防ぎ、エージェントの焦点を維持する（「コンテキストの劣化」を防ぐ）ため、Managed Agents API には、約 135,000 トークンでネイティブ コンテキスト圧縮ステップが用意されています。これは自動処理で、

## レスポンスをストリーミングする

長時間実行されるタスクの場合は、レスポンスをストリーミングして、エージェントの動作をリアルタイムで確認できます。

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

ストリーミングは、ステップの差分（増分テキスト、推論トークン、ツール呼び出しの更新）のイテラブルを返します。レスポンスをストリーミングする方法の詳細については、[ストリーミング ガイド](https://ai.google.dev/gemini-api/docs/streaming?hl=ja)をご覧ください。

## 環境からファイルをダウンロードする

エージェントがサンドボックス内にファイルを作成します。Files API を使用して、直接 HTTP リクエストでダウンロードします（SDK メソッドはまだありません）。

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## マネージド エージェントを保存する

前のステップでは、デフォルトの Antigravity エージェントを使用して、インラインでカスタマイズしました。構成（手順、スキル、環境）を反復処理したら、マネージド エージェントとして保存できます。これにより、構成を繰り返すことなく ID で呼び出すことができます。

エージェントを保存するときに、`base_environment`（ソースから、または既存の環境をフォークして）を定義します。エージェントは、新しいインタラクションごとにこの環境を使用します。

**ソースから:** ソースをインラインで定義するか、GitHub や Cloud Storage などの他のソースから定義します。

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## マネージド エージェントを呼び出す

マネージド エージェントを保存したら、ID で呼び出すことができます。呼び出しごとにベース環境がフォークされるため、実行は常にクリーンな状態から開始されます。

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## 次のステップ

- [Antigravity エージェント](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja): 機能、サポートされているツール、マルチモーダル入力、料金、制限事項。
- [マネージド エージェントの構築](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja): 独自の手順、スキル、データで Antigravity を拡張する。
- [環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja): ソース、ネットワーク、ライフサイクル、リソース上限。
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja): モデルとエージェントの基盤となる API。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
