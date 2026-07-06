---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=ja
fetched_at: 2026-07-06T05:19:34.451861+00:00
title: "Gemini \u306e\u601d\u8003 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini の思考

[Gemini 3 シリーズと 2.5 シリーズのモデル](https://ai.google.dev/gemini-api/docs/models?hl=ja)は、
「思考プロセス」を使用して推論とマルチステップ
プランニングの能力を大幅に向上させています。これにより、コーディング、高度な数学、データ分析などの複雑なタスクで非常に効果的です。

思考モデルを使用すると、Gemini はレスポンスを返す前に内部で推論を行います。Interactions API は、この推論を `thought` ステップで表示します。これは、`steps` 配列内の関数呼び出し、ユーザー入力、モデル出力とともに時系列で表示される専用のステップです。

思考ステップには次の 2 つのフィールドがあります。

| フィールド | 必須 | 説明 |
| --- | --- | --- |
| `signature` | ✅ はい | モデルの内部推論状態を暗号化した表現。モデルが最小限の推論を行う場合でも常に存在します。 |
| `summary` | ❌ いいえ | 推論を要約するコンテンツ（テキストや画像）の配列。[`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=ja) 構成、モデルが十分な推論を行ったかどうか、コンテンツ タイプ（画像レイテンシにテキストの要約がない場合など）によって空になることがあります。 |

## 思考とのインタラクション

思考モデルとのインタラクションを開始する手順は、他のインタラクション リクエストと同様です。`model` フィールドで、[思考をサポートするモデル](#thinking-levels)のいずれかを指定します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## 思考の要約

思考の要約は、モデルの内部推論プロセスに関する分析情報を提供します。
デフォルトでは、最終出力のみが返されます。`thinking_summaries` を使用して思考の要約を有効にできます。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

思考ブロックには、次のような場合に**要約のない署名のみ** が含まれることがあります。

- モデルが要約を生成するのに十分な推論を行わなかった簡単なリクエスト
- `thinking_summaries: "none"`: 要約が明示的に無効になっている場合
- 画像など、特定の思考コンテンツ タイプにはテキストの要約がない場合がある

コードでは、`summary` が空または存在しない思考ブロックを常に処理する必要があります。

## 思考を伴うストリーミング

ストリーミングを使用して、生成中に段階的な思考の要約を受け取ります。
思考ブロックは、サーバー送信イベント（SSE）を使用して配信されます。デルタタイプは 2 つあります。

| デルタタイプ | 次を含む | 送信されるタイミング |
| --- | --- | --- |
| `thought_summary` | テキストまたは画像の要約コンテンツ | 段階的な要約を含む 1 つ以上のデルタ |
| `thought_signature` | 暗号署名 | `step.stop` の前の最後のデルタ |

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
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
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
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

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

Gemini モデルはデフォルトで動的思考を行い、リクエストの複雑さに応じて推論の労力を自動的に調整します。この動作は、`thinking_level` パラメータを使用して制御できます。

| モデル | デフォルトの思考 | サポートされているレベル |
| --- | --- | --- |
| gemini-3.1-pro-preview | オン（高） | 低、中、高 |
| gemini-3.1-flash-lite-image | オン（最小） | 最小、高 |
| gemini-3-flash-preview | オン（高） | 最小、低、中、高 |
| gemini-3-pro-preview | オン（高） | 低、高 |
| gemini-3.5-flash | オン（中） | 最小、低、中、高 |
| gemini-2.5-pro | オン | 低、中、高 |
| gemini-2.5-flash | オン | 低、中、高 |
| gemini-2.5-flash-lite | オフ | 低、中、高 |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## 思考シグネチャ

思考シグネチャは、モデルの内部推論を暗号化したものです。マルチターン インタラクションで推論の継続性を維持するために必要です。

Interactions API を使用すると、`generateContent` API よりも思考シグネチャの処理がはるかに簡単になります。

### ステートフル モード（推奨）

デフォルトでは、ステートフル モードで Interactions API を使用する場合（`store: true` を設定し、後続のターンで `previous_interaction_id` を渡す場合）、サーバーはすべての思考ブロックと署名を含む会話の状態を自動的に管理します。このモードでは、署名に関して何もする必要はありません。サーバー側で完全に処理されます。

### ステートレス モード

会話の状態を自分で管理し（ステートレス モード）、各リクエストで入力と出力の完全な履歴を渡す場合:

- モデルから受信したとおりに、すべての `thought` ブロックを常に再送信する**必要があります** 。
- モデルが推論を続行するために必要な署名が含まれているため、履歴から思考ブロックを削除または変更**しないでください** 。
- セッション内でモデルを切り替える場合は、前のモデルの思考ブロックを再送信する必要があります。バックエンドで互換性が管理されます。

## 料金

思考がオンの場合、レスポンスの料金は出力トークンと思考トークンの合計です。生成された思考トークンの合計数は、`total_thought_tokens` フィールドから取得できます。

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

思考モデルは、最終的な
レスポンスの品質を高めるために完全な思考を生成し、思考プロセスに関する
分析情報を提供するために[要約](#summaries)を出力します。料金は、API から出力されるのは要約のみですが、モデルが生成する必要がある完全な思考トークンに基づきます。

トークンの詳細については、[トークンのカウント](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)ガイドをご覧ください。

## ベスト プラクティス

次のガイドラインに沿って、思考モデルを効率的に使用してください。

- **推論を確認する**: 思考の要約を分析して、失敗を把握し、プロンプトを改善します。
- **思考予算を管理する**: 長い出力の場合は、モデルの思考を減らすようにプロンプトを設定して、トークンを節約します。
- **簡単なタスク**: 事実の取得や分類には、最小限または低レベルの思考を使用します（例: 「DeepMind はどこで設立されましたか？」）。
- **中程度のタスク**: 概念の比較や創造的な推論には、デフォルトの思考を使用します（例: 電気自動車とハイブリッド車の比較）。
- **複雑なタスク**: 高度なコーディング、数学、マルチステップ プランニングには、最大限の思考を使用します（例: AIME の数学の問題を解く）。

## 次のステップ

- [テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja): 基本的なテキスト レスポンス
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja): ツールに接続する
- [Gemini 3 ガイド](https://ai.google.dev/gemini-api/docs/gemini-3?hl=ja): モデル固有の機能

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-01 UTC。"],[],[]]
