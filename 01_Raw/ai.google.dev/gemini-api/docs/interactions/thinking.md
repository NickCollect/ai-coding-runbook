---
source_url: https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ja
fetched_at: 2026-06-08T05:36:57.216930+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini が考えています

[Gemini 3 および 2.5 シリーズのモデル](https://ai.google.dev/gemini-api/docs/models?hl=ja)は、「思考プロセス」を使用して推論と多段階計画の能力を大幅に向上させているため、コーディング、高度な数学、データ分析などの複雑なタスクに非常に効果的です。

思考モデルを使用すると、Gemini は回答する前に内部で推論を行います。Interactions API は、`thought` ステップ（`steps` 配列の関数呼び出し、ユーザー入力、モデル出力とともに時系列で表示される専用ステップ）を介してこの推論を表面化します。

すべての思考ステップには次の 2 つのフィールドが含まれています。

| フィールド | 必須 | 説明 |
| --- | --- | --- |
| `signature` | ✅ はい | モデルの内部推論状態を暗号化した表現。モデルが最小限の推論を行う場合でも、常に存在します。 |
| `summary` | ❌ 不可 | 理由を要約したコンテンツ（テキストや画像など）の配列。[`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=ja) 構成、モデルが十分な推論を実行したかどうか、コンテンツ タイプ（画像潜在空間にテキストの要約がない場合など）によっては、空になることがあります。 |

## 思考とのやり取り

思考モデルとのインタラクションを開始する手順は、他のインタラクション リクエストと同様です。`model` フィールドで、[思考サポート付きのモデル](#thinking-levels)のいずれかを指定します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## 思考の要約

思考の要約は、モデルの内部推論プロセスに関する分析情報を提供します。デフォルトでは、最終出力のみが返されます。`thinking_summaries` を使用して思考の要約を有効にできます。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

次のような場合、思考ブロックには**要約のない署名のみ**が含まれることがあります。

- 単純なリクエスト。モデルが要約を生成するのに十分な推論を行っていない
- `thinking_summaries: "none"`、要約が明示的に無効になっている場合
- 画像などの特定の種類の思考コンテンツには、テキストの要約がない場合があります。

コードでは、`summary` が空または存在しない思考ブロックを常に処理する必要があります。

## 思考を伴うストリーミング

ストリーミングを使用して、生成中に思考の増分要約を受け取ります。思考ブロックは、次の 2 つの異なるデルタタイプでサーバー送信イベント（SSE）を使用して配信されます。

| デルタタイプ | 次を含む | 送信日時 |
| --- | --- | --- |
| `thought_summary` | テキストまたは画像の要約コンテンツ | 増分サマリーを含む 1 つ以上のデルタ |
| `thought_signature` | 暗号署名 | `step.stop` の前の最後の差分処理 |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

ストリーミング レスポンスはサーバー送信イベント（SSE）を使用し、ステップとイベントで構成されます。例:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## 思考の制御

Gemini モデルはデフォルトで動的思考を行い、リクエストの複雑さに基づいて推論の労力を自動的に調整します。この動作は、`thinking_level` パラメータを使用して制御できます。

| モデル | デフォルトの思考 | サポートされているレベル |
| --- | --- | --- |
| gemini-3.1-pro-preview | オン（高） | 低、中、高 |
| gemini-3-flash-preview | オン（高） | 最小、低、中、高 |
| gemini-3-pro-preview | オン（高） | 低、高 |
| gemini-2.5-pro | オン | 低、中、高 |
| gemini-2.5-flash | オン | 低、中、高 |
| gemini-2.5-flash-lite | オフ | 低、中、高 |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## 思考シグネチャ

思考シグネチャは、モデルの内部推論を暗号化したものです。マルチターン インタラクション全体で推論の継続性を維持する必要があります。

Interactions API を使用すると、`generateContent` API よりもはるかに簡単に思考シグネチャを処理できます。

### ステートフル モード（推奨）

デフォルトでは、ステートフル モードで Interactions API を使用すると（`store: true` を設定し、後続のターンで `previous_interaction_id` を渡す）、サーバーはすべての思考ブロックとシグネチャを含む会話の状態を自動的に管理します。このモードでは、署名に関して何もする必要はありません。これらはすべてサーバーサイドで処理されます。

### ステートレス モード

会話の状態を自分で管理し（ステートレス モード）、各リクエストで入力と出力の完全な履歴を渡す場合:

- すべての `thought` ブロックは、モデルから受信したとおりに常に再送信しなければなりません。
- 思考ブロックには、モデルが推論を継続するために必要なシグネチャが含まれているため、履歴から思考ブロックを削除したり変更したりしないでください。
- セッション内でモデルを切り替える場合でも、前のモデルの思考ブロックを再送信する必要があります。バックエンドが互換性を管理します。

## 料金

思考が有効になっている場合、レスポンスの料金は出力トークンと思考トークンの合計です。生成された思考トークンの合計数は、`total_thought_tokens` フィールドから取得できます。

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

思考モデルは、最終的なレスポンスの質を高めるために完全な思考を生成し、思考プロセスに関する分析情報を提供するために[要約](#summaries)を出力します。料金は、API から要約のみが出力される場合でも、モデルが生成する必要がある思考トークンの合計数に基づいて計算されます。

トークンの詳細については、[トークン数のカウント](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ja)をご覧ください。

## ベスト プラクティス

次のガイドラインに沿って、思考モデルを効率的に使用します。

- **推論を確認する**: 思考の要約を分析して、失敗を理解し、プロンプトを改善します。
- **思考予算を制御する**: 長い出力に対してモデルの思考を減らすようにプロンプトを送信し、トークンを節約します。
- **簡単なタスク**: 事実の取得や分類に最小限の思考を使用します（例: 「DeepMind はどこで設立されましたか？」）。
- **中程度のタスク**: 概念の比較や創造的な推論（電気自動車とハイブリッド車の比較など）には、デフォルトの思考を使用します。
- **複雑なタスク**: 高度なコーディング、数学、複数ステップの計画（AIME の数学の問題を解くなど）には、最大思考を使用します。

## 次のステップ

- [テキスト生成](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ja): 基本的なテキスト レスポンス
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ja): ツールに接続する
- [Gemini 3 ガイド](https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=ja): モデル固有の機能

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
