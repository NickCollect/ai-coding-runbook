---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ja
fetched_at: 2026-09-07T05:38:13.891864+00:00
title: "Gemini \u306e\u601d\u8003 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini の思考

[Gemini 3 シリーズと 2.5 シリーズのモデル](https://ai.google.dev/gemini-api/docs/models?hl=ja)は、内部の
「思考プロセス」を使用して推論能力と多段階
計画能力を大幅に向上させているため、コーディング、高度な数学、データ分析などの複雑なタスクに非常に効果的です。

このガイドでは、Gemini API を使用して Gemini の思考機能を操作する方法について説明します。

## 思考によるコンテンツの生成

思考モデルでリクエストを開始する手順は、他のコンテンツ生成リクエストと同様です。主な違いは、次の[テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#text-input)の例に示すように、思考をサポートする
[モデル](#supported-models)のいずれかを `model` フィールドで指定することです。

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## 思考の要約

思考の要約は、モデルの生の思考を要約したもので、モデルの内部的な推論プロセスに関する分析情報を提供します。思考レベルと予算は、思考の要約ではなく、モデルの生の思考に適用されます。

思考の要約を有効にするには、リクエスト構成で `includeThoughts` を `true` に設定します。その後、`response` パラメータの `parts` を反復処理し、`thought` ブール値を確認することで、要約にアクセスできます。

次の例は、ストリーミングなしで思考の要約を有効にして取得する方法を示しています。これにより、レスポンスとともに単一の最終的な思考の要約が返されます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

ストリーミングで思考を使用する例を次に示します。これにより、生成中にローリング増分要約が返されます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.8-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## 思考の制御

Gemini モデルはデフォルトで動的な思考を行い、ユーザーのリクエストの複雑さに応じて推論の労力を自動的に調整します。
ただし、特定のレイテンシ制約がある場合や、モデルが通常よりも深い推論を行う必要がある場合は、必要に応じてパラメータを使用して思考動作を制御できます。

### 思考レベル（Gemini 3）

`thinkingLevel` パラメータ（Gemini 3 モデル以降で推奨）を使用すると、推論動作を制御できます。

次の表に、モデルタイプごとの `thinkingLevel` 設定の詳細を示します。

| 思考レベル | Gemini 3.8 &3.7 Flash | Gemini 3.6 &3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 &3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | 説明 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | サポート対象外（エラー） | サポート対象 | サポート対象外 | サポート対象（デフォルト） | サポート対象（デフォルト） | サポート対象 | ほとんどのクエリで「思考なし」の設定と一致します。なお、`minimal` は思考がオフであることを保証するものではありません。複雑なタスクでは、モデルが最小限の推論を行うことがあります。 |
| **`low`** | サポート対象 | サポート対象 | サポート対象 | サポート対象 | サポート対象外 | サポート対象 | レイテンシと費用を最小限に抑えます。 |
| **`medium`** | サポート対象（デフォルト） | サポート対象（デフォルト） | サポート対象 | サポート対象 | サポート対象外 | サポート対象 | ほとんどのタスクでバランスの取れた思考を行います。 |
| **`high`** | サポート対象（動的） | サポート対象（動的） | サポート対象（デフォルト、動的） | サポート対象（動的） | サポート対象（動的） | サポート対象（デフォルト、動的） | 推論の深さを最大化します。モデルが最初の（思考なし）出力トークンに到達するまでに 大幅に時間がかかる場合がありますが、出力はより慎重に推論されます。 |

次の例は、思考レベルを設定する方法を示しています。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Gemini 3.1 Pro では思考を無効にできません。Gemini 3 Flash と Flash-Lite
も、思考の完全オフをサポートしていません。
思考レベルを指定しない場合、Gemini は Gemini 3 モデルの
デフォルトの思考レベル（Gemini 3.1 Pro の場合は `"high"`、Gemini 3.5 Flash の場合は `"medium"` など）を使用します。

Gemini 2.5 シリーズのモデルは `thinkingLevel` をサポートしていません。代わりに `thinkingBudget` を使用してください。

### 思考予算

Gemini 2.5 シリーズで導入された `thinkingBudget` パラメータは、推論に使用する思考トークンの特定の数に関するガイダンスをモデルに提供します。

以下に、モデルタイプごとの `thinkingBudget` 構成の詳細を示します。
`thinkingBudget` を 0 に設定すると、思考を無効にできます。`thinkingBudget` を -1 に設定すると、
**動的な思考** が有効になります。つまり、モデルはリクエストの
複雑さに応じて予算を調整します。

| モデル | デフォルト設定 (思考予算は設定されていません) | 範囲 | 思考を無効にする | 動的な思考を有効にする |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | 動的な思考 | `128`～`32768` | N/A: 思考を無効にできません | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash** | 動的な思考 | `0`～`24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash Preview** | 動的な思考 | `0`～`24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash Lite** | モデルは思考しません | `512`～`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | モデルは思考しません | `512`～`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | 動的な思考 | `0`～`24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash Live Native Audio Preview（2025 年 9 月）** | 動的な思考 | `0`～`24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

プロンプトによっては、モデルがトークン予算を超過または不足する可能性があります。

## 思考シグネチャ

思考シグネチャを手動で管理する必要があります。

Gemini API はステートレスであるため、モデルはすべての API リクエストを独立して処理し、マルチターンのやり取りで前のターンの思考コンテキストにアクセスできません。

マルチターンのやり取りで思考コンテキストを維持できるようにするため、Gemini は思考シグネチャを返します。これは、モデルの内部的な思考プロセスを暗号化したものです。

- **Gemini 2.5 モデル** は、思考が有効になっていて、
  リクエストに [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#thinking)（
  具体的には [関数宣言](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#step-2)）が含まれている場合に、思考シグネチャを返します。
- **Gemini 3 モデル** は、すべてのタイプの [パート](https://ai.google.dev/api/caching?hl=ja#Part) に対して思考シグネチャを返すことがあります。
  常にすべてのシグネチャをそのまま渡すことをおすすめしますが、関数呼び出しシグネチャの場合は必須です。 詳しくは、
  [思考シグネチャ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ja)のページをご覧ください。

関数呼び出しで考慮すべきその他の使用上の制限は次のとおりです。

- シグネチャは、レスポンスの他の部分（関数呼び出しやテキストのパートなど）からモデルによって返されます。
  [その後のやり取りで、](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#step-4)
  すべての部分を含むレスポンス全体をモデルに返します。
- シグネチャを含むパートを連結しないでください。
- シグネチャ付きのパートとシグネチャなしのパートを結合しないでください。

## 料金

思考がオンの場合、レスポンスの料金は出力トークンと思考トークンの合計です。生成された思考トークンの合計数は、`thoughtsTokenCount` フィールドから取得できます。

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

思考モデルは、最終的な
レスポンスの品質を高めるために完全な思考を生成し、思考プロセスに関する
分析情報を提供するために[要約](#summaries)を出力します。そのため、API から出力されるのは要約のみですが、料金はモデルが要約を作成するために生成する必要がある完全な思考トークンに基づきます。

トークンについて詳しくは、[トークン数のカウント](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)
ガイドをご覧ください。

## ベスト プラクティス

このセクションでは、思考モデルを効率的に使用するためのガイダンスを示します。
いつものように、[プロンプトのガイダンスとベスト プラクティス](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)に従うことで、最適な結果が得られます。

### デバッグとステアリング

- **推論を確認する**: 思考モデルから期待どおりのレスポンスが得られない場合は、Gemini の思考の要約を慎重に分析すると役立ちます。タスクをどのように分解して結論に達したかを確認し、その情報を使用して正しい結果に修正できます。
- **推論のガイダンスを提供する**: 特に長い
  出力が必要な場合は、プロンプトでガイダンスを指定して、モデルが使用する[思考量](#set-budget)を制限することをおすすめします。これにより、レスポンス用にトークン出力をより多く予約できます。

### タスクの複雑さ

- **簡単なタスク（思考をオフにできる）:** 事実の取得や分類など、複雑な推論を必要としない簡単なリクエストの場合は、思考は必要ありません。次に例を示します。
  - 「DeepMind はどこで設立されましたか？」
  - 「このメールは会議を依頼するものですか、それとも情報を提供するものですか？」
- **中程度のタスク（デフォルト/一部の思考）:** 多くの一般的なリクエストでは、段階的な処理や深い理解が役立ちます。Gemini は、次のようなタスクで思考機能を柔軟に使用できます。
  - 光合成と成長を比較する。
  - 電気自動車とハイブリッド車を比較対照する。
- **難しいタスク（思考能力を最大限に活用）:** 複雑な数学の問題を解くタスクやコーディング タスクなど、非常に複雑な課題の場合は、高い思考予算を設定することをおすすめします。このようなタスクでは、モデルが推論能力と計画能力を最大限に活用する必要があります。回答を提供するまでに多くの内部ステップが必要になることがよくあります。次に例を示します。
  - AIME 2025 の問題 1 を解く: 17b が 97b の約数となるすべての整数基数 b > 9 の合計を求めます。
  - ユーザー認証を含む、リアルタイムの株式市場データを可視化するウェブ アプリケーションの Python コードを作成します。できるだけ効率的にしてください。

## サポートされているモデル、ツール、機能

思考機能は、3 シリーズと 2.5 シリーズのすべてのモデルでサポートされています。
すべてのモデル機能は、
[モデルの概要](https://ai.google.dev/gemini-api/docs/models?hl=ja)ページで確認できます。

思考モデルは、Gemini のすべてのツールと機能で動作します。これにより、モデルは外部システムとやり取りしたり、コードを実行したり、リアルタイム情報にアクセスしたりして、その結果を推論と最終的なレスポンスに組み込むことができます。

思考モデルでツールを使用する例は、[思考クックブック][Colab]で試すことができます。

## 次のステップ

- 思考の範囲については、[OpenAI 互換性](https://ai.google.dev/gemini-api/docs/openai?hl=ja#thinking)ガイドをご覧ください。

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-04 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-04 UTC。"],[],[]]
