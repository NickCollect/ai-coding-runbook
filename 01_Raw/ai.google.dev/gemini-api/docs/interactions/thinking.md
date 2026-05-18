---
source_url: https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=zh-TW
fetched_at: 2026-05-18T05:07:09.739550+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini 正在思考

[Gemini 3 和 2.5 系列模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)採用「思考過程」，大幅提升推論和多步驟規劃能力，因此非常適合處理複雜工作，例如程式設計、高等數學和資料分析。

使用思考型模型時，Gemini 會先在內部進行推論，再做出回應。Interactions API 會透過 `thought` 步驟顯示這項推理過程，這些專屬步驟會依時間順序顯示在 `steps` 陣列中，與函式呼叫、使用者輸入內容或模型輸出內容並列。

每個思考步驟都包含兩個欄位：

| 欄位 | 必要 | 說明 |
| --- | --- | --- |
| `signature` | ✅ 是 | 模型內部推論狀態的加密表示法。一律會顯示，即使模型只執行最少的推論作業。 |
| `summary` | ❌ 否 | 總結推論過程的內容陣列 (文字和/或圖片)。視 [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=zh-tw) 設定、模型是否執行足夠的推論，或內容類型而定，可能為空白 (例如，圖像潛在空間可能沒有文字摘要)。 |

## 與思考過程的互動

啟動與思考型模型的互動，與其他互動要求類似。在 `model` 欄位中指定[支援思考輔助功能的模型](#thinking-levels)：

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

您可以串流思考互動，在生成期間接收增量思考摘要和簽章。如需涵蓋事件類型、差異類型和程式碼範例的完整指南，請參閱「[串流互動](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=zh-tw#streaming-with-thinking)」指南。

## 想法摘要

思考摘要可深入瞭解模型的內部推論過程。根據預設，系統只會傳回最終輸出內容。你可以使用 `thinking_summaries` 啟用想法摘要：

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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
# Specifies the API revision to avoid breaking changes when they become default
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

在下列情況下，想法區塊**只能包含簽名，不得有摘要**：

- 簡單要求，模型未充分推理，無法生成摘要
- `thinking_summaries: "none"`，明確停用摘要功能
- 部分想法內容類型 (例如圖片) 可能沒有文字摘要

您的程式碼應一律處理 `summary` 為空或不存在的思考區塊。

## 控制思考

Gemini 模型預設會進行動態思考，根據要求的複雜程度自動調整推論量。您可以使用 `thinking_level` 參數控制這項行為。

| 型號 | 預設思考 | 支援的等級 |
| --- | --- | --- |
| gemini-3.1-pro-preview | 開啟 (高) | 低、中、高 |
| gemini-3-flash-preview | 開啟 (高) | 極低、低、中、高 |
| gemini-3-pro-preview | 開啟 (高) | 低、高 |
| gemini-2.5-pro | 開啟 | 低、中、高 |
| gemini-2.5-flash | 開啟 | 低、中、高 |
| gemini-2.5-flash-lite | 關閉 | 低、中、高 |

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
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

## 思想簽名

想法簽章是模型內部推論過程的加密表示法。他們必須在多輪互動中維持推論連續性。

與 `generateContent` API 相比，Interactions API 可大幅簡化處理思緒簽章的程序。

### 有狀態模式 (建議)

根據預設，在有狀態模式下使用 Interactions API 時 (設定 `store: true` 並在後續回合中傳遞 `previous_interaction_id`)，伺服器會自動管理對話狀態，包括所有想法區塊和簽章。在這個模式下，您不需要對簽章採取任何行動。這些作業完全在伺服器端處理。

### 無狀態模式

如果您自行管理對話狀態 (無狀態模式)，並在每個要求中傳遞完整的輸入和輸出記錄：

- 您**必須**一律重新傳送所有 `thought` 區塊，且內容必須與模型傳送的完全一致。
- **請勿**從記錄中移除或修改思維方塊，因為這些方塊包含模型繼續推論所需的簽章。
- 在工作階段中切換模型時，您仍應重新傳送先前模型的思考區塊。後端會管理相容性。

## 定價

開啟思考功能後，回覆價格為輸出詞元和思考詞元的總和。您可以從 `total_thought_tokens` 欄位取得產生的思考權杖總數。

### Python

```
# This will only work for SDK newer than 2.0.0
# ...
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// ...
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

思考模型會生成完整想法，提升最終回覆的品質，然後輸出[摘要](#summaries)，深入瞭解思考過程。即使 API 只會輸出摘要，但計價依據仍是模型需要產生的完整思考權杖。

如要進一步瞭解權杖，請參閱「[權杖計數](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-tw)」指南。

## 最佳做法

請按照下列指南，有效運用思考模型。

- **檢閱推論**：分析想法摘要，瞭解失敗原因並改善提示。
- **控管思考預算**：提示模型減少思考，以節省詞元。
- **簡單工作**：用於事實擷取或分類，不需經過太多思考 (例如「DeepMind 在哪裡成立？」)。
- **中等難度的工作**：使用預設的思考方式比較概念或進行創意推論 (例如比較電動車和油電混合車)。
- **複雜工作**：運用最高思考力處理進階程式設計、數學或多步驟規劃工作 (例如：解決美國數學邀請賽 (AIME) 的數學問題)。

## 後續步驟

- [生成文字](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw)：基本文字回覆
- [函式呼叫](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw)：連結至工具
- [Gemini 3 指南](https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=zh-tw)：模型專屬功能

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-16 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-16 (世界標準時間)。"],[],[]]
