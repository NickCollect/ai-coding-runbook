---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=zh-TW
fetched_at: 2026-09-14T05:50:32.547118+00:00
title: "\u7db2\u5740\u80cc\u666f\u8cc7\u8a0a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 網址背景資訊

網址背景資訊工具可讓您以網址形式，為模型提供額外背景資訊。在要求中加入網址後，模型就會存取這些網頁的內容 (只要網址類型未列於[限制一節](#limitations))，藉此提供更完善的回覆。

網址脈絡工具適用於下列工作：

- **擷取資料**：從多個網址擷取特定資訊，例如價格、名稱或重要發現。
- **比較文件**：分析多份報表、文章或 PDF，找出差異並追蹤趨勢。
- **統整及建立內容**：整合多個來源網址的資訊，生成準確的摘要、網誌文章或報告。
- **分析程式碼和文件**：指向 GitHub 存放區或技術文件，即可說明程式碼、生成設定說明或回答問題。

以下範例說明如何比較不同網站的兩道食譜。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## 運作方式

網址內容工具採用兩步驟的擷取程序，兼顧速度、成本和最新資料存取權。提供網址後，這項工具會先嘗試從內部索引快取擷取內容。這可做為經過高度最佳化的快取。如果網址未編入索引 (例如網頁剛發布)，工具會自動改為擷取實際網頁。這項工具會直接存取網址，即時擷取內容。

## 與其他工具搭配使用

您可以將網址內容工具與其他工具結合，建立功能更強大的工作流程。

[Gemini 3 模型](#supported-models)支援結合內建工具 (例如網址背景資訊) 和自訂工具 (函式呼叫)。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)」頁面。

### 以搜尋結果為基準

同時啟用網址背景資訊和 [以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-tw)後，模型就能使用搜尋功能在網路上尋找相關資訊，然後使用網址背景資訊工具深入瞭解找到的網頁。這種做法非常適合需要廣泛搜尋，並深入分析特定網頁的提示。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## 瞭解回覆內容

模型使用網址背景資訊工具時，文字回覆會在文字內容區塊中加入行內 `url_citation` 註解。每則註解都會將回覆文字的片段 (透過 `start_index` 和 `end_index`) 連結至衍生來源網址。這是應用程式中顯示引文的主要方式，請參閱[上方的主要範例](#get-started)，瞭解如何擷取引文。

回應中也會納入 `url_context_result` 步驟，其中含有每個網址擷取嘗試的中繼資料 (狀態、擷取的網址)。這項功能主要用於偵錯。

### 安全檢查

系統會對網址執行內容審查檢查，確認網址符合安全標準。如果網址未通過這項檢查，對應的 `url_context_result` 步驟會顯示 `status` `"unsafe"`。

### 符記數量

系統會將從提示中指定網址擷取的內容，計為輸入權杖的一部分。您可以在互動的 `usage` 物件中查看詞元數。範例如下：

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

每個權杖的價格取決於使用的模型，詳情請參閱[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)頁面。

## 支援的模型

| 模型 | 網址背景資訊 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |

## 最佳做法

- **提供具體網址**：為獲得最佳結果，請提供您希望模型分析的內容的直接網址。模型只會從您提供的網址擷取內容，不會從巢狀連結擷取任何內容。
- **檢查存取權**：確認提供的網址不會導向需要登入或位於付費牆後的網頁。
- **使用完整網址**：請提供完整網址，包括通訊協定 (例如 https://www.google.com，而不是只有 google.com)。

## 限制

- 要求限制：這項工具每次最多可處理 20 個網址。
- 網址內容大小：從單一網址擷取的內容大小上限為 34 MB。
- 公開存取：網址必須可在網路上公開存取。
  系統不支援本機主機位址 (例如 localhost、127.0.0.1)、私人網路和通道服務 (例如 ngrok、pinggy)。
- 僅限 Gemini API：網址背景資訊僅適用於 Gemini API，不適用於 Gemini Enterprise Agent Platform。

### 支援及不支援的內容類型

這項工具可從下列內容類型的網址中擷取內容：

- 文字 (text/html、application/json、text/plain、text/xml、text/css、text/javascript、text/csv、text/rtf)
- 圖片 (image/png、image/jpeg、image/bmp、image/webp)
- PDF (application/pdf)

系統「不」支援下列內容類型：

- 付費牆內容
- YouTube 影片 (請參閱[影片理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw#youtube)，瞭解如何處理 YouTube 網址)
- Google Workspace 檔案，例如 Google 文件或試算表
- 影片和音訊檔案

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-12 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-12 (世界標準時間)。"],[],[]]
