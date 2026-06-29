---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-TW
fetched_at: 2026-06-29T05:32:09.982083+00:00
title: "API \u7248\u672c\u8aaa\u660e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [API 參考資料](https://ai.google.dev/api?hl=zh-tw)

提供意見

# API 版本說明

本文將概略說明 Gemini API 的 `v1` 和 `v1beta` 版本之間的差異。

- **v1**：API 穩定版。穩定版中的功能在主要版本生命週期內完全受支援。如有任何重大變更，系統會建立下一個 API 主要版本，並在一段合理時間後淘汰現有版本。API 導入非破壞性變更時，不必變更主要版本。自 2026 年 6 月起，**Interactions API** 將全面開放使用，並支援 `v1`。
- **v1beta**：這個版本包含正在積極開發的早期功能。`v1beta` 中的功能可能會根據意見回饋進行調整，但您可以在這些功能升級為穩定版之前搶先試用。

| 功能 | v1 | v1beta |
| --- | --- | --- |
| Interactions API |  |  |
| 生成內容 - 僅輸入文字 |  |  |
| 生成內容 - 輸入文字和圖片 |  |  |
| 生成內容 - 文字輸出 |  |  |
| 生成內容 - 多輪對話 (聊天) |  |  |
| 生成內容 - 函式呼叫 |  |  |
| 生成內容 - 串流 |  |  |
| 嵌入內容 - 僅輸入文字 |  |  |
| 生成答案 |  |  |
| 語意檢索器 |  |  |

- - 支援
- - Will never be supported

## 在 SDK 中設定 API 版本

Gemini API SDK 預設為 `v1beta`，但您可以明確指定版本，方法是設定 API 版本，如下列程式碼範例所示：

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works"
  }'
```

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-22 (世界標準時間)。"],[],[]]
