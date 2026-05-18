---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-TW
fetched_at: 2026-05-18T05:14:55.209278+00:00
title: "\u5728 Google AI Studio \u4e2d\u5efa\u69cb\u61c9\u7528\u7a0b\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 在 Google AI Studio 中建構應用程式

本頁面說明如何使用 Google AI Studio 快速建構 (或「隨意編碼」) 及部署應用程式，測試 Gemini 的最新功能，例如 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) 和 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw)。Google AI Studio 現在支援**全端執行階段**，讓您透過自然語言提示，建構具備伺服器端邏輯、安全密鑰管理和 npm 套件支援的強大應用程式。

## 開始使用

在 Google AI Studio 的[建構模式](https://aistudio.google.com/apps?hl=zh-tw)中，開始直覺式程式開發。您可以透過下列幾種方式開始建構：

- **先輸入提示**：在「建構」模式中，使用輸入框輸入要建構的內容說明。選取「AI 晶片」，在提示中加入圖片生成或 Google 地圖資料等特定功能。你甚至可以按語音轉文字按鈕，說出想聽的內容。
- **「好手氣」按鈕**：如果需要靈感，請使用「好手氣」按鈕，Gemini 就會生成含有專案構想的提示，協助你開始創作。
- **從範本庫重新混音專案**：從[應用程式範本庫](https://aistudio.google.com/apps?source=showcase&hl=zh-tw)開啟專案，然後選取「複製應用程式」。

執行提示詞後，系統會生成必要的程式碼和檔案，並在右側顯示應用程式的即時預覽畫面。

## 系統會建立什麼內容？

執行提示時，AI Studio 會建立完整的應用程式。根據預設，這項工具會建立全端環境，其中可能包含：

- **用戶端**：網頁前端 (預設為 React)。
- **伺服器端**：Node.js 執行階段，可進行安全的 API 呼叫、資料庫連線，以及使用 npm 套件。

選取右側預覽窗格中的「程式碼」分頁，即可查看產生的程式碼。**Antigravity Agent** 會智慧管理堆疊中的多個檔案，確保變更正確傳播。

### The Antigravity Agent

**Antigravity Agent** 是 [Google Antigravity](https://antigravity.google?hl=zh-tw) 的主要 AI 功能，現在代理程式架構的核心元件已支援 Google AI Studio 的建構模式體驗。不只是產生簡單的程式碼，還能維護整個專案的環境、管理多個檔案，以及瞭解複雜的指令，建構穩健的全端應用程式。

主要功能如下所示：

- **脈絡感知**：保留先前提示和檔案狀態的脈絡。
- **多檔案管理**：處理多個檔案之間的依附元件。
- **驗證執行**：驗證程式碼更新，減少產生錯覺。

## 全端功能

Google AI Studio 充分發揮現代網路生態系統的強大功能，讓您不僅能建構用戶端原型，還能：

- **伺服器端執行階段和 npm**：使用 npm 套件的龐大程式庫。代理程式會自動識別並安裝應用程式所需的套件 (例如資料視覺化或 API 用戶端的特定程式庫)。您也可以視需要要求特定套件。
- **密鑰管理**：在「設定」選單中安全地儲存 API 金鑰和密鑰。這些值可在伺服器端程式碼中存取，避免在用戶端曝光。
- **多人遊戲**：直接在 AI Studio 中建構即時協作體驗。伺服器端執行階段會管理使用者互動所需的狀態和連線。
- **Firebase 整合**：自動佈建及設定 Firebase，包括 Firestore 資料庫 (持續性資料儲存空間) 和 Firebase 驗證 (登入流程，特別是「使用 Google 帳戶登入」)。代理程式會處理整個設定程序，甚至在應用程式中編寫這些服務的程式碼。

[進一步瞭解如何開發全端應用程式](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-tw)

## 繼續建構

Google AI Studio 為應用程式生成初始程式碼後，您可以繼續調整：

### 在 Google AI Studio 中建構內容

- **使用 Gemini 進行反覆運算**：在**建構模式**中使用對話面板，要求 Gemini 進行修改、新增功能或變更樣式。
- **直接編輯程式碼**：開啟預覽面板中的「程式碼」分頁，即可即時編輯。

### 在外部開發

如要使用更進階的工作流程，可以匯出程式碼，並在偏好的環境中作業：

- **在本機下載及開發**：將產生的程式碼匯出為 **ZIP 檔案**，然後匯入程式碼編輯器。
- **推送至 GitHub**：將程式碼推送至 **GitHub 存放區**，與現有的開發和部署程序整合。

## 主要功能與特色

Google AI Studio 提供多項功能，讓建構過程直覺且視覺化：

- **建立及反覆改良全端應用程式**：只要提供提示，即可建立全端應用程式，並透過對話或**註解模式**反覆改良。使用註解模式，醒目顯示應用程式 UI 的任何部分，並說明您想要的變更。
- **分享及部署應用程式**：您可以與他人分享創作內容，進行協作或展示作品。分享時，API 呼叫會計入使用限制。使用付費模型可能需要支付費用。應用程式準備就緒後，即可部署至 Cloud Run。
- **應用程式庫**：應用程式庫提供專案構想的視覺化程式庫。
  你可以瀏覽 Gemini 的功能、即時預覽應用程式，以及重新混音應用程式，打造專屬版本。

## 部署或封存應用程式

應用程式準備就緒後，即可部署：

- **Cloud Run**：將應用程式部署為可擴充的服務。
  系統可能會根據用量收取 [Google Cloud Run](https://cloud.google.com/run?hl=zh-tw) 費用。如要進一步瞭解部署作業，請參閱「[從 Google AI Studio 部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-tw)」。
- **GitHub**：將專案匯出至 GitHub 存放區。

## 限制

本節列出 Google AI Studio 建構模式目前的限制。

### API 金鑰管理

建立使用 Gemini API 的新應用程式時，AI Studio 會自動將 Gemini API 金鑰設定為應用程式伺服器端環境中的密鑰。您可以在「密鑰」面板中查看及管理這個金鑰。

- **自動設定**：系統會為你設定 `GEMINI_API_KEY`，無須手動設定即可開始建構。
- **僅限伺服器端**：API 金鑰會注入伺服器端執行階段，且絕不會納入用戶端程式碼。
- **現有應用程式**：如果是 2026 年 5 月 14 日前建構的應用程式，下次修改應用程式的 Gemini 功能時，代理程式會自動將 Gemini API 整合升級為建議的伺服器端方法。

### 在 Google AI Studio 以外的環境中部署

- **Cloud Run**：從 AI Studio 部署至 Cloud Run 時，API 金鑰會安全地納入伺服器端環境。部署的應用程式會使用您的 API 金鑰，為所有使用者呼叫 Gemini API。
- **下載 ZIP 檔案**：如果將應用程式下載為 ZIP 檔案，以便在其他位置運作執行，則必須在代管環境中設定 `GEMINI_API_KEY` 環境變數。由於應用程式的 Gemini API 呼叫是透過伺服器端程式碼發出，因此金鑰不會向使用者公開。

### 分享應用程式時發生錯誤

如果您分享應用程式，而使用者透過共用網址存取時遇到 **403 存取受限**錯誤，可能是因為下列其中一個原因：

- **瀏覽器擴充功能**：隱私權擴充功能 (例如 Privacy Badger) 可能會封鎖應用程式。請停用擴充功能，避免發生錯誤。
- **建構問題**：目前的程式碼可能存在問題。提示代理程式「修正目前程式碼的所有建構問題」，然後重新分享網址。

## 常見問題

### 什麼是「在 AI Studio 中建構」？

AI Studio Build 平台可協助您從簡單的提示詞開始，使用 Gemini 建構可供正式發布的 AI 輔助應用程式。只要透過提示描述想建構的內容，Gemini 就會為您生成應用程式。您也可以瀏覽我們的資源庫，瞭解 Gemini API 的功能，並重新混音應用程式，打造專屬版本。

### Build 如何處理我的 Gemini API 金鑰？

建立使用 Gemini API 的應用程式時，AI Studio 會自動將 Gemini API 金鑰設為伺服器端密鑰。應用程式的 Gemini API 呼叫是透過這個金鑰，從伺服器端程式碼發出，因此絕不會在瀏覽器中公開。您可以在「設定」的「祕密」面板中查看 API 金鑰。

### 分享應用程式時，我的 API 金鑰是否會曝光？

不會。API 金鑰會儲存為伺服器端密碼，絕不會納入用戶端程式碼。分享應用程式後，其他使用者可以存取，但無法查看您的 API 金鑰。

與他人共用應用程式時，API 呼叫會計入用量限制。使用付費模型可能需要支付費用。如果應用程式可能會產生費用，AI Studio 會在設定期間和分享前提醒您。

### 哪些人可以看到我的應用程式？

應用程式預設為私人。您可以與其他使用者共用應用程式，讓他們使用。與您共用應用程式的使用者可以查看程式碼，並視需要複製程式碼。如果您共用應用程式時授予編輯權限，其他使用者就能編輯應用程式的程式碼。

### 我可以在 AI Studio 以外執行應用程式嗎？

可以。您可以從 AI Studio 將應用程式部署至 [Cloud Run](https://cloud.google.com/run?hl=zh-tw)，這樣應用程式就會取得公開網址，且 API 金鑰已在伺服器端環境中安全設定。您也可以將應用程式下載為 ZIP 檔案，並在其他位置代管，但必須在代管環境中設定 `GEMINI_API_KEY` 環境變數。由於 Gemini API 呼叫是透過伺服器端程式碼發出，金鑰會保持安全。

如要進一步瞭解部署選項，請參閱「[從 Google AI Studio 部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-tw)」。

### 我可以使用自己的工具在本機開發應用程式，然後在這裡分享嗎？

目前尚未提供這項功能。我們很期待日後能支援更多應用程式的用途。如有任何具體想法，歡迎提供意見回饋。

### 如何搭配應用程式使用資料庫或其他儲存空間？

AI Studio 應用程式是在 Cloud Run 容器中執行的標準應用程式。只要沒有防火牆禁止從動態 IP 範圍存取，您可以使用任何可透過網路連線的儲存空間解決方案。

我們正努力在日後新增儲存空間的直接支援，屆時您將可直接在 AI Studio 中設定。

### 如何存取麥克風、網路攝影機和其他 Navigator API？

為確保觀眾瞭解應用程式使用網路攝影機或其他裝置的情況，應用程式必須先取得額外確認，才能存取這些 [Navigator API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator)。應用程式建立者可以在應用程式的 `metadata.json` 檔案中新增這些權限要求。例如：

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

`requestFramePermissions` 支援的值是標準[政策控管功能](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md)的子集。

### 如何搭配應用程式使用 GitHub？

透過 AI Studio 的 GitHub 整合功能，您可以為工作建立存放區，並提交最新變更。我們目前不支援提取遠端變更。

### 我可以將應用程式的編輯權授予其他使用者嗎？

目前尚未支援，但很快就會推出。

### 為什麼我的應用程式因違反政策而遭到標記？

我們有自動審查應用程式的系統，確保應用程式符合政策規定。如果我們發現應用程式違反政策，就會從 AI Studio 移除。違反政策的行為包括但不限於：

- 含有惡意軟體、網路釣魚或冒用他人身分內容的應用程式
- 應用程式顯示或散布違反兒少性虐待圖像政策的內容
- 顯示或散布違反騷擾政策內容的應用程式
- 顯示或散布違反仇恨言論政策內容的應用程式
- 應用程式顯示或散布違反人口販運政策的內容
- 顯示或散布違反情色露骨內容政策的內容
- 應用程式顯示或散布違反暴力和血腥內容政策的內容
- 應用程式顯示或散布違反有害或危險內容政策的內容

如果應用程式遭檢舉違反政策，但您認為這是誤判，可以提出申訴。如果屢次違反政策，我們可能會終止您對 AI Studio 的存取權。

### 身為應用程式開發人員，我有哪些責任？

提醒您，身為應用程式擁有者，您有責任確保應用程式的行為和處理的所有資料符合規定。包括：

- **遵守法律和第三方權利：**確保應用程式遵守所有適用法律和法規，且未侵犯他人權利，包括智慧財產權和隱私權。
- **內容監控：**應用程式使用的其他服務可能適用附加條款。舉例來說，適用於 Firestore 的《[Google Cloud 服務條款](https://cloud.google.com/terms?hl=zh-tw)》規定，代管第三方內容的客戶必須發布政策，定義禁止的內容 (例如非法內容)，並監控是否有這類非法內容。
- **安全實作：**實作必要的防護措施和審核工具，防止應用程式遭到濫用。

請注意《服務條款》中的[使用限制](https://ai.google.dev/gemini-api/terms?hl=zh-tw#use-restrictions)。

### AI Studio 應用程式庫中的應用程式適用哪些條款？

使用 AI Studio 應用程式庫中的應用程式時，須遵守《[Gemini API 附加服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw)》，除非另有說明。

## 後續步驟

- [開發全端應用程式](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-tw)
- 請參閱[應用程式庫](https://aistudio.google.com/apps?source=showcase&hl=zh-tw)中的範例。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-17 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-17 (世界標準時間)。"],[],[]]
