---
source_url: https://ai.google.dev/gemini-api/docs/google-ai-plans?hl=zh-TW
fetched_at: 2026-08-31T06:37:12.196755+00:00
title: "Google AI \u65b9\u6848 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Google AI 方案

在 AI Studio 中使用 Google AI 訂閱方案。

與免費方案相比，Google AI Pro 和 Ultra 訂閱方案提供更高的模型存取權，以及更高的頻率限制，方便您在 AI Studio 中進行原型設計和開發。

如要註冊 Google AI 方案，請直接在 Google AI Studio 中按一下左側導覽選單的「升級」按鈕，即可升級。你也可以前往 [Google AI 方案頁面](https://one.google.com/about/google-ai-plans/?hl=zh-tw)註冊。

## 總覽

訂閱 Google AI Pro 和 Ultra，開發人員就能在 Google AI Studio Playground 中使用付費模型，並享有更高的頻率限制，還能使用[建構模式](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-tw)中的程式碼助理等功能，以直覺式程式碼開發。訂閱者可獲得比免費方案更高的每日配額，在 [Playground](https://aistudio.google.com/prompts/new_chat?hl=zh-tw) 和 [Build](https://aistudio.google.com/apps?hl=zh-tw) 介面中使用。系統會使用重設機制而非滾動時間視窗來強制執行每日限制，確保您在透過 Cloud Billing 轉移至實際工作環境規模的開發作業前，能享有順暢的開發體驗。

| 方案 | AI Studio 使用情況 | 模型存取權和福利 |
| --- | --- | --- |
| **免費** | 適中配額 | 基本限制和存取權，可選擇升級以取得更多權限。 |
| **AI Pro** | 提高配額 | 使用 Gemini Pro、Nano Banana 和 Lyria 等進階模型。 |
| **AI Ultra** | 最高配額 | 享有原型設計、開發和進階前沿模型的最高用量。 |

## Gemini API 使用量

在 AI Studio 中用盡每日基本訂閱配額後，您可以繼續使用 Gemini API 金鑰和已啟用 Cloud Billing 的 Gemini API，直接依要求付費。
您可以在 [AI Studio 資訊主頁](https://aistudio.google.com/projects?hl=zh-tw)中，查看專案和 API 金鑰的 Gemini API 用量。

如果訂閱者有 Google Cloud Platform (GCP) 專案並啟用 Cloud Billing，即可透過 [Google Developer Program](https://developers.google.com/program?hl=zh-tw) 取得每月 Cloud 抵免額，用於 Cloud 服務 (包括 Gemini API)。預付和後付的使用量和帳單結算方式維持不變。如果使用者採用預付帳單，AI Studio 必須有大於 $0 的付費餘額，才能啟用宣傳抵免額。系統會先套用符合資格的 Google Cloud 抵免額 (如有)。[瞭解詳情](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#billing-plans)。

整合 Google AI 訂閱方案可降低門檻，方便您進行進階實驗和開發。不過，如要大規模部署正式版，建議使用 Google Cloud 專案、[Google Cloud 入門級](https://cloud.google.com/blog/topics/developers-practitioners/the-starter-tier-for-google-ai-studio-explained?hl=zh-tw) 和 Gemini API 金鑰。

## 限制和相容性

- **僅限 AI Studio UI：**開發人員使用 Google AI 方案的福利，僅適用於 Google AI Studio 網頁介面。直接使用 Gemini API (例如使用 API 金鑰或外部應用程式) 時，系統會另外計費及管理。不過，你可以在其他 Google 產品中使用訂閱方案 (請參閱「[Google AI 方案](https://one.google.com/about/google-ai-plans/?hl=zh-tw)」)。
- **與 API 計費不同：**AI Studio 的 Google AI 方案與 [Gemini API 用量層級](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)不同，後者涵蓋開發和正式環境的 API 用量。
- **Google One 抵免額：** [Google One AI 點數](https://support.google.com/googleone/answer/16287445?hl=zh-tw)是獨立的點數系統，AI Studio 不支援這類點數，且這類點數與 Google Cloud 抵免額不重疊。
- **代理程式存取權：**Google AI 方案不含 AI Studio 內的代理程式 (Deep Research 和 Antigravity 預覽版) 存取權，如要存取，必須使用[付費 API 金鑰](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#setup-billing)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-08-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-08-19 (世界標準時間)。"],[],[]]
