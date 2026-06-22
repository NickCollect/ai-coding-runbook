---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=zh-TW
fetched_at: 2026-06-22T06:25:21.270511+00:00
title: "\u6392\u89e3 Google AI Studio \u554f\u984c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 排解 Google AI Studio 問題

本頁提供 Google AI Studio 的疑難排解建議，協助您解決問題。

## 瞭解 403 存取受限錯誤

如果看到「403 Access Restricted」錯誤，表示您使用 Google AI Studio 的方式違反《[服務條款](https://ai.google.dev/terms?hl=zh-tw)》。常見原因之一是您不在[支援的區域](https://ai.google.dev/available_regions?hl=zh-tw)。

## 解決 Google AI Studio 中的「沒有內容」回應

如果內容因任何原因遭到封鎖，Google AI Studio 會顯示「沒有內容」warning訊息。如要查看更多詳細資料，請將指標懸停在「沒有內容」上，然後按一下「安全」圖示 warning。

如果回覆因[安全設定](https://ai.google.dev/docs/safety_setting?hl=zh-tw)而遭到封鎖，且您已考量用途的[安全風險](https://ai.google.dev/docs/safety_guidance?hl=zh-tw)，可以修改[安全設定](https://ai.google.dev/docs/safety_setting?hl=zh-tw#safety_settings_in_makersuite)，影響系統傳回的回覆。

如果回覆遭到封鎖，但不是因為安全設定，則查詢或回覆可能違反[服務條款](https://ai.google.dev/terms?hl=zh-tw)，或是不支援。

## 查看權杖用量和限制

開啟提示後，畫面底部的「文字預覽」按鈕會顯示提示內容目前使用的權杖，以及所用模型的權杖上限。

## AI Studio 的 Google Cloud IAM 權限

Google Cloud 雲端專案成員必須具備特定 Identity and Access Management (IAM) 權限，才能在 Google AI Studio 中執行動作。如要進一步瞭解這些身分，請參閱「[IAM 主體總覽](https://cloud.google.com/iam/docs/principals?hl=zh-tw)」。

在相關聯的 Google Cloud 雲端專案中，具有「編輯者」或「擁有者」角色的使用者，有權查看資訊主頁及管理 Gemini API 金鑰。具備「檢視者」角色的使用者可以查看資訊主頁和 API 金鑰，但無法建立、更新或刪除這些項目。

如要進行更精細的控制，請參閱下表，瞭解各項 AI Studio 功能所需的特定權限。如需授予這些權限的操作說明，請參閱 Google Cloud 說明文件中的「[授予、變更及撤銷資源的存取權](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=zh-tw)」。

| AI Studio 功能 | 必要 IAM 權限 | 額外規定 |
| --- | --- | --- |
| **搜尋專案** (匯入專案) | `resourcemanager.projects.get` |  |
| **重新命名專案** | `resourcemanager.projects.update` |  |
| **顯示配額層級** | 不適用 |  |
| **建立 API 金鑰** | 具備「搜尋專案」權限，且：  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **列出 API 金鑰** | 具備「搜尋專案」權限，且：  `apikeys.keys.list` `serviceusage.services.get` | Google Cloud 雲端專案必須啟用 [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=zh-tw)。 |
| **重新命名 API 金鑰** | `apikeys.keys.update` |  |
| **刪除 API 金鑰** | `apikeys.keys.delete` |  |
| **用量資訊主頁** | 具備「搜尋專案」權限，且：  `monitoring.timeSeries.list` |  |
| **速率限制資訊主頁** | 擁有「使用情況資訊主頁」權限，且：  `cloudquotas.quotas.get` |  |
| **支出 (帳單上限)** | `billing.resourceCosts.get` (查看支出) `billing.resourcebudgets.read` (查看上限) `billing.resourcebudgets.write` (設定上限) |  |
| **帳單資訊主頁** | `billing.accounts.get` |  |

### 其他存取權檢查

除了 Google Cloud IAM 權限，AI Studio 也會執行安全性和法規遵循檢查。如未符合下列條件，您可能會在 AI Studio 介面或 API 回應中遇到 `PERMISSION_DENIED` 或存取限制錯誤：

- **安全檢查：**您的要求必須通過自動安全檢查。
- **服務條款：**您必須接受《Google 服務條款》和《生成式 AI 附加服務條款》。
- **支援的區域：**你必須位於[支援的區域](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-tw)。
- **信任與安全：**Google Cloud 雲端專案不得因濫用行為而遭到檢舉。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-29 (世界標準時間)。"],[],[]]
