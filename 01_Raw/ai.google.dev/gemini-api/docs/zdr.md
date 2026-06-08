---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=zh-TW
fetched_at: 2026-06-08T05:35:23.481384+00:00
title: "Gemini Developer API \u4e0d\u6703\u4fdd\u7559\u4efb\u4f55\u8cc7\u6599 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini Developer API 不會保留任何資料

本頁面將詳細說明 Gemini 開發人員 API 中一般所謂的「零資料保留」。

## 訓練限制

如《[Gemini API 服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw)》所述，使用付費服務時，Google 不會將您的提示 (包括相關聯的系統指令、快取內容和檔案，例如圖片、影片或文件) 或回覆用於改善產品。如要瞭解付費服務的定義，請參閱[這篇文章](https://ai.google.dev/gemini-api/terms?hl=zh-tw#paid-services)。

## 保留顧客資料和實現零資料保留

在下列情況和條件下，客戶資料通常只會保留一段時間。如要達成零資料保留目標，客戶必須在下列各個領域採取特定行動或避免使用特定功能：

- **記錄提示以監控濫用情形**：如《[Gemini API 附加服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw)》所述，對於付費服務，Google 會記錄提示和回覆一段時間，僅用於偵測是否違反《[使用限制政策](https://policies.google.com/terms/generative-ai/use-policy?hl=zh-tw)》。當您對特定專案的 ZDR 要求獲得核准後，系統會先清除所有使用者內容 (提示和回覆) 和可識別的中繼資料 (例如 IP 位址和 Google 帳戶 ID)，再進行記錄。產生的記錄會標示為已清除，且不含任何可識別的使用者資料，確保與 Gemini Enterprise Agent Platform Zero Data Retention 相同。
- **以 Google 搜尋強化事實基礎**：如《[Gemini API 附加服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw#grounding-with-google-search)》所述，Google 會將提示、背景資訊和生成的輸出內容儲存三十 (30) 天，用於建立回覆依據和搜尋建議。這類儲存資訊可用於偵錯及測試支援基礎的系統。**使用「以 Google 搜尋強化事實基礎」功能時，無法停用這類資訊的儲存功能。**
- **利用 Google 地圖建立基準**：如《[Gemini API 附加服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw)》所述，Google 會將提示詞、背景資訊和生成的輸出內容儲存三十 (30) 天，以便建立以 Google 地圖為依據的結果。這類儲存的資訊僅供可靠性工程使用，例如在發生服務問題時進行偵錯。**如果使用「利用 Google 地圖建立基準」，就無法停用這項資訊的儲存功能。**
- **Interactions API**：Interactions API 可管理對話的有效狀態，以啟用多輪對話。**根據預設，Interactions API 會啟用狀態儲存功能**。如要確保零資料足跡，您必須在 API 要求中明確將 `store` 參數設為 `false`，選擇不保留預設狀態。
- **即時 API**：這個有狀態的 API 會儲存對話狀態，以便即時重新連線。如要達到零資料保留，請**不要設定 SessionResumptionConfig**。如果生成工作階段控制代碼，對話狀態 (包括文字、音訊和影片) 最多會保留 24 小時。
- **File API Storage**：使用者可透過 File API 上傳大型資產。檔案會以靜態形式儲存，直到使用者刪除或檔案過期為止。
  File API 的使用與 ZDR 記錄無關；使用者必須手動刪除檔案，才能確保資料足跡為零。
- **明確的內容快取**：使用者可使用 `cached_content` 欄位，手動快取大型資料集 (例如長篇影片或文件庫)。雖然這些要求的記錄會遵循 ZDR 捨棄政策，但快取內容本身會以使用者定義的 `ttl` 或 `expire_time` 儲存。如要達到絕對零資料足跡，請勿使用 cached\_content 功能。
- **隱含記憶體內快取**：根據預設，Gemini 模型會將資料快取在記憶體內，以減少開發人員的延遲時間和成本。這項資料嚴格來說是儲存在 RAM 中 (而非靜態)，且會以專案層級隔離，並設有 24 小時的 TTL。**這不會違反零資料保留政策。**

## 後續步驟

- 瞭解[生成式 AI 使用限制政策](https://policies.google.com/terms/generative-ai/use-policy?hl=zh-tw)。
- 詳閱《[Gemini API 附加服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw)》。
- 如需企業級自助式 ZDR 控制選項，請參閱 [Gemini Enterprise Agent Platform 零資料保留指南](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-28 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-28 (世界標準時間)。"],[],[]]
