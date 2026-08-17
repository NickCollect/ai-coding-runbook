---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-TW
fetched_at: 2026-08-17T02:36:57.835417+00:00
title: "\u512a\u5148\u9806\u5e8f\u63a8\u65b7 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 優先順序推斷

說明：瞭解如何透過 Interactions API 中的「優先」推論層級，縮短延遲時間

Gemini Priority API 是進階推論層級，專為需要低延遲和最高可靠性的重要業務工作負載設計，價格較高。系統會優先處理 Priority 層級的流量，再處理 Standard API 和 Flex 層級的流量。

您可以在 Interactions API 端點使用優先順序推論功能。

## 如何使用優先檔案區

如要使用「優先」層級，請將要求中的 `service_tier` 欄位設為 `priority`。如未填寫此欄位，則預設級別為標準。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## 優先推論的運作方式

優先順序推論會將要求轉送至高重要性的運算佇列，為面向使用者的應用程式提供可預測的快速效能。主要機制是將超過動態限制的流量，從伺服器端順暢降級為標準處理程序，確保應用程式穩定性，而非讓要求失敗。

| 功能 | 優先順序 | 標準 | Flex | 批次 |
| --- | --- | --- | --- | --- |
| **定價** | 比 Standard 方案多 75% 至 100% | 原價 | 50% 折扣 | 50% 折扣 |
| **延遲** | 秒 | 秒至分鐘 | 分鐘 (目標：1 到 15 分鐘) | 長達 24 小時 |
| **穩定性** | 高 (不會脫落) | 高 / 中高 | 盡可能提供最佳服務 (可卸載) | 高 (處理量) |
| **介面** | 同步 | 同步 | 同步 | 非同步 |

### 主要優點

- **低延遲**：專為互動式 AI 工具設計，可直接與使用者互動，並在幾秒內回應。
- **高可靠性**：流量會以最高重要性處理，且嚴格來說不可捨棄。
- **正常降級**：如果流量尖峰超過動態限制，系統會自動將流量降級為標準層級，以利處理，避免服務中斷。
- **低摩擦**：使用與標準和 Flex 層級相同的同步 `create` 方法。

### 用途

優先處理非常適合用於效能和可靠性至關重要的重要業務工作流程。

- **互動式 AI 應用程式**：客戶服務聊天機器人和副手，使用者會支付額外費用，並期望獲得快速且一致的回覆。
- **即時決策引擎**：需要高度可靠的低延遲結果的系統，例如即時票證分類或詐欺偵測。
- **進階客戶功能**：開發人員需要為付費客戶確保更高的服務等級目標 (SLO)。

### 頻率限制

即使優先取用量會計入[整體互動式流量速率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)，仍有自己的速率限制。Priority 推論的預設速率限制為**模型 / 層級的標準速率限制的 0.3 倍**

### 優雅降級邏輯

如果因壅塞而超出優先順序限制，系統會**自動且正常**將溢出的要求降級為標準處理，而不是因 503 或 429 錯誤而失敗。降級的要求會以標準費率計費，而非優先級進階費率。

### 客戶責任

- **回應監控**：開發人員應監控 API 回應中的 `x-gemini-service-tier`
  標頭，偵測要求是否經常降級為 `standard`。
- **重試**：用戶端必須為標準錯誤 (例如 `DEADLINE_EXCEEDED`) 實作重試邏輯/指數輪詢。

## 定價

優先推論的價格比[標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw) 高出 75% 至 100%，並以每詞元計費。

## 支援的模型

下列模型支援優先推論：

| 模型 | 優先順序推斷 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |

## 後續步驟

- [彈性推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)，降低成本。
- [權杖](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw)：瞭解權杖。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
