---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-TW
fetched_at: 2026-09-28T06:16:58.237443+00:00
title: "\u5f9e Google AI Studio \u90e8\u7f72 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 從 Google AI Studio 部署

您可以使用 Google AI Studio，直接從建構模式部署全端應用程式。這可讓您快速從原型轉移至可擴充的受管理正式環境。

## 部署方案

如要從 AI Studio 建構模式部署應用程式，相關規定會因您使用的層級而異：

- [**Google Cloud 基礎方案**](https://docs.cloud.google.com/docs/starter-tier?hl=zh-tw)：
  可讓您發布最多 2 個全端應用程式，不必設定 Google Cloud 專案或帳單帳戶。
- **標準部署**：需要連結至 AI Studio 帳戶的 Google Cloud 專案，且該專案已啟用計費功能。

## 關於入門級別

Google Cloud Starter Tier 提供簡化的途徑，讓您直接從 Google AI Studio 將應用程式部署至 Google Cloud，不必設定完整的 Google Cloud 環境或帳單帳戶。

每次部署 Google AI Studio 都會在 Cloud Run 中建立對應的服務。如果服務是透過 Google AI Studio 的入門方案部署，則適用下列限制：

- 最多可部署兩項服務。
- 您的服務部署在[單一 Cloud Run 區域](https://docs.cloud.google.com/run/docs/locations?hl=zh-tw)。

## 「起步」級別的部署步驟

在「建構」模式中設計應用程式後，請使用 Starter 層級部署應用程式：

1. 按一下右上角的「發布」按鈕。
2. 點選「開始使用」。
3. 按一下「發布應用程式」。

部署完成後，AI Studio 會提供 Cloud Run 網址，您可透過該網址存取上線的應用程式。

## AI Studio 的自訂網址

從 Google AI Studio 發布應用程式時，您可以在 `ai.studio` 下設定自訂的子網域 (例如 `https://your-app-name.ai.studio`)，方便記憶。

Google AI Studio 要求所有專案的子網域不得重複，並以先到先得的方式指派子網域。如果其他專案已使用該名稱，AI Studio 會提示您選擇其他名稱。如果取消發布或刪除應用程式，自訂網址就會釋出，供其他使用者申請。

### 設定自訂網址

如要設定或更新應用程式的自訂網址，請按照下列步驟操作：

1. 在 Google AI Studio 中以「建構」模式開啟應用程式。
2. 按一下右上角的「發布」。
3. 在部署設定中，於「自訂網址」欄位輸入偏好的子網域，或接受系統建議的網址。
4. 按一下「發布應用程式」。

如要將現有的自訂網址轉移至其他應用程式，請先取消發布或刪除已指派該自訂網址的應用程式，然後使用所選子網域發布新應用程式。

### 檢舉商標或著作權問題

自訂子網域必須遵守《[Google 服務條款](https://policies.google.com/terms?hl=zh-tw)》。如果發現自訂網址侵害商標或未經授權使用受著作權保護的名稱，請使用 [Google 法律疑難排解工具](https://support.google.com/legal/troubleshooter/1114905?hl=zh-tw)檢舉。

## 標準部署項目

隨著應用程式不斷演進，您可能需要入門級方案以外的功能，例如更高的配額、更多運算資源，或是入門級方案未提供的其他 Google Cloud 產品。如要解鎖這些功能，您可以將完全代管的入門級專案轉換為標準 Google Cloud 專案。

這樣一來，您就能順暢擴大規模，不會失去進度。請按照步驟[建立 Cloud Billing 帳戶](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=zh-tw#create-new-billing-account)、正式接受標準的 Google Cloud 服務條款，並[升級為標準的 Google Cloud 專案](https://docs.cloud.google.com/docs/starter-tier?hl=zh-tw#upgradee)。詳情請參閱「[付費帳戶設定](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-tw#paid-setup)」。

如要進一步瞭解計費級別，請參閱「[計費](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)」。

## 刪除應用程式

如果不再需要應用程式，可以按照下列指示在 Google AI Studio 中刪除：

1. 在 Google AI Studio 中，前往「應用程式」頁面。
2. 選取左選單中的「應用程式」。
3. 將指標懸停在要刪除的應用程式上。
4. 點選資料列右側的垃圾桶圖示，即可刪除應用程式。

## 後續步驟

- 進一步瞭解 [Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier?hl=zh-tw)。
- 請參閱 [Gemini API 的計費方式](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-10 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-10 (世界標準時間)。"],[],[]]
