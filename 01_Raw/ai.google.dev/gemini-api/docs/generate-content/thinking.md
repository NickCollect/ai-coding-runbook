---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=zh-TW
fetched_at: 2026-09-28T06:24:49.500391+00:00
title: "Gemini \u601d\u8003 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

提供意見

# Gemini 思考

[Gemini 3 和 2.5 系列模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)採用內部「思考過程」，大幅提升推論和多步驟規劃能力，因此非常適合處理程式設計、高等數學和資料分析等複雜工作。

本指南說明如何使用 Gemini API，運用 Gemini 的思考能力。

## 生成內容時進行思考

使用思考型模型發起要求，與任何其他內容生成要求類似。主要差異在於 `model` 欄位中指定了[支援思考的其中一個模型](#supported-models)，如下列[文字生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw#text-input)範例所示：

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

## 想法重點摘要

想法摘要是模型原始想法的摘要版本，可深入瞭解模型的內部推論過程。請注意，思考程度和預算適用於模型的原始想法，而非想法摘要。

如要啟用想法摘要，請在要求設定中將 `includeThoughts` 設為 `true`。接著，您可以透過 `response` 參數的 `parts` 進行疊代，並檢查 `thought` 布林值，存取摘要。

以下範例說明如何啟用及擷取想法摘要 (不使用串流)，並在回應中傳回單一最終想法摘要：

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

以下是使用串流思考的範例，會在生成期間傳回滾動式增量摘要：

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

## 控制思考

Gemini 模型預設會進行動態思考，根據使用者要求的複雜程度自動調整推論工作量。不過，如果您有特定的延遲限制，或需要模型進行比平常更深入的推論，可以視需要使用參數來控制思考行為。

### 思考程度 (Gemini 3)

建議搭配 Gemini 3 模型和後續版本使用 `thinkingLevel` 參數，藉此控制推論行為。

下表詳細列出各模型類型的 `thinkingLevel` 設定：

| 思考程度 | Gemini 3.8 和 3.7 Flash | Gemini 3.6 和 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 和 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | Gemini Robotics ER 2 | 說明 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | 不支援 (錯誤) | 支援 | 不支援 | 支援 (預設) | 支援 (預設) | 支援 | 支援 | 對於大多數查詢，這項設定與「不思考」相同。請注意，`minimal` 無法保證關閉思考功能，模型可能仍會針對複雜工作進行極少的推理。 |
| **`low`** | 支援 | 支援 | 支援 | 支援 | 不支援 | 支援 | 支援 | 盡量縮短延遲時間並降低成本。 |
| **`medium`** | 支援 (預設) | 支援 (預設) | 支援 | 支援 | 不支援 | 支援 | 支援 | 思考能力均衡，適合處理多數工作。 |
| **`high`** | 支援 (動態) | 支援 (動態) | 支援 (預設、動態) | 支援 (動態) | 支援 (動態) | 支援 (預設、動態) | 支援 (預設、動態) | 盡可能深入推論。模型可能需要較長時間才能輸出第一個 (非思考) 輸出權杖，但輸出內容會經過更仔細的推論。 |

以下範例說明如何設定思考層級。

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

你無法停用 Gemini 3.1 Pro 的思考功能。Gemini 3 Flash 和 Flash-Lite 也不支援完全關閉思考功能。如果未指定思考層級，Gemini 會使用 Gemini 3 模型的預設思考層級 (例如 Gemini 3.1 Pro 為 `"high"`，Gemini 3.5 Flash 為 `"medium"`)。

Gemini 2.5 系列模型不支援 `thinkingLevel`，請改用 `thinkingBudget`。

### 詞元數量上限和 `max_output_tokens`

[`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=zh-tw#v1beta.GenerationConfig) 生成參數會設定回覆可生成的詞元數量上限，包括思考詞元。

設定後，這項參數會做為基礎架構強制執行的硬性截斷，不會改變模型分配思考預算 (`thinking_level`) 的方式。

如果模型在推論時達到這項限制，就會停止生成內容，並傳回截斷或空白的輸出內容 (但仍會針對產生的任何思考詞元計費)。`finish_reason: MAX_TOKENS`如要減少費用或延遲時間，但不想截斷回應，請降低 `thinking_level` (`low` 或 `medium`)，而不是設定較小的 `max_output_tokens`。

### 思考預算

Gemini 2.5 系列推出的 `thinkingBudget` 參數，可引導模型使用特定數量的思考詞元進行推論。

以下是各模型類型的`thinkingBudget`設定詳細資料。
如要停用思考功能，請將 `thinkingBudget` 設為 0。
將 `thinkingBudget` 設為 -1 可開啟**動態思考**，也就是模型會根據要求的複雜度調整預算。

| 模型 | 預設設定 (未設定思考預算) | 範圍 | 停用思考模式 | 開啟動態思考模式 |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | 動態思維 | `128` 至 `32768` | 不適用：無法停用思考模式 | `thinkingBudget = -1` (預設) |
| **2.5 Flash** | 動態思維 | `0` 至 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (預設) |
| **2.5 Flash 預先發布版** | 動態思維 | `0` 至 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (預設) |
| **2.5 Flash Lite** | 模型不會思考 | `512` 至 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite 預先發布版** | 模型不會思考 | `512` 至 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 預先發布版** | 動態思維 | `0` 至 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (預設) |
| **2.5 Flash 即時原生音訊預覽 (2025 年 9 月)** | 動態思維 | `0` 至 `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (預設) |

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

視提示而定，模型可能會超出或未用完權杖預算。

## 想法簽名

Gemini API 是無狀態的，因此模型會獨立處理每個 API 要求，且無法存取多輪互動中先前回合的思考脈絡。

為確保多輪互動的思考脈絡一致，Gemini 會傳回思考簽章，這是模型內部思考過程的加密表示法。

- 啟用思考功能，且要求包含[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#thinking) (具體來說是[函式宣告](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#step-2)) 時，**Gemini 2.5 模型**會傳回思考簽章。
- **Gemini 3 模型**可能會傳回所有類型[部分](https://ai.google.dev/api/caching?hl=zh-tw#Part)的思維簽章。
  建議您一律將所有簽章傳回，但函式呼叫簽章*必須*傳回。詳情請參閱「[Thought Signatures](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-tw)」頁面。

使用函式呼叫時，請注意以下其他用量限制：

- 簽章會與回覆中的其他部分一起從模型傳回，例如函式呼叫或文字部分。[將整個回覆](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#step-4)的所有部分，在後續回合中傳回模型。
- 請勿將簽名檔與郵件內容合併。
- 請勿將有簽名的部分與沒有簽名的部分合併。

## 定價

開啟思考功能後，回覆價格為輸出詞元和思考詞元的總和。您可以從 `thoughtsTokenCount` 欄位取得產生的思考權杖總數。

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

思考模型會生成完整想法，提升最終回覆的品質，然後輸出[摘要](#summaries)，深入瞭解思考過程。因此，即使 API 只會輸出摘要，但計費依據仍是模型生成摘要時所需的所有思考權杖。

如要進一步瞭解權杖，請參閱「[權杖計數](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw)」指南。

## 最佳做法

本節提供一些指引，說明如何有效使用思考模型。一如往常，請按照[提示指南和最佳做法](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw)操作，以獲得最佳結果。

### 偵錯與導向

- **查看推論過程**：如果思考型模型未提供預期回覆，請仔細分析 Gemini 的思考摘要。你可以查看 AI 如何分解工作並得出結論，然後根據這些資訊修正結果。
- **提供推論指引**：如果希望輸出內容特別長，建議在提示詞中提供指引，限制模型[思考量](#set-budget)。這樣一來，就能為回覆保留更多權杖輸出。

### 工作複雜度

- **簡單任務 (可關閉思考)：**對於不需要複雜推論的簡單要求 (例如事實擷取或分類)，不需要思考。例如：
  - 「DeepMind 是在哪裡成立的？」
  - 「這封電子郵件是要求召開會議，還是只是提供資訊？」
- **中等工作 (預設/需要思考)：**許多常見要求需要逐步處理或深入瞭解。Gemini 可彈性運用思考能力處理下列工作：
  - 以光合作用和成長過程做類比。
  - 比較電動車和油電混合車的異同。
- **困難任務 (最高思考能力)：**如要解決複雜的數學問題或程式碼編寫工作等高難度挑戰，建議設定較高的思考預算。這類工作需要模型充分運用推論和規劃能力，通常需要經過許多內部步驟，才能提供答案。例如：
  - 解決 2025 年 AIME 的第 1 題：找出所有大於 9 的整數底數 b，使 17b 為 97b 的因數，並計算這些底數的總和。
  - 編寫 Python 程式碼，建立可顯示即時股市資料的網頁應用程式，包括使用者驗證。盡可能提高效率。

## 支援的模型、工具和功能

所有 3 和 2.5 系列模型都支援思考功能。
如要查看所有模型功能，請前往[模型總覽](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)頁面。

Thinking 模型可搭配 Gemini 的所有工具和功能。模型可藉此與外部系統互動、執行程式碼或存取即時資訊，並將結果納入推理和最終回覆。

如要試用工具和思維模型，請參閱 [思維食譜][Colab]中的範例。

## 後續步驟

- 如需相關資訊，請參閱 [OpenAI 相容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw#thinking)指南。

[Colab]：https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-25 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-25 (世界標準時間)。"],[],[]]
