---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-TW
fetched_at: 2026-05-05T20:47:47.695421+00:00
title: "\u5728 Google AI Studio \u4e2d\u958b\u767c\u5168\u7aef\u61c9\u7528\u7a0b\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 在 Google AI Studio 中開發全端應用程式

Google AI Studio 現在支援全端開發，可讓您建構的應用程式不只是用戶端原型。透過伺服器端執行階段，您可以管理密鑰、連線至外部 API，以及建構即時多人遊戲體驗。

## 伺服器端執行階段

Google AI Studio 應用程式現在可以包含伺服器端元件 (Node.js)。這種做法有以下幾個優點：

- **執行伺服器端邏輯**：執行不應向用戶端公開的程式碼。
- **存取 npm 套件**：[Antigravity Agent](https://antigravity.google/docs/agent?hl=zh-tw) 可以安裝及使用 npm 生態系統中的大量套件。
- **處理密鑰**：安全地使用 API 金鑰和憑證。

### 使用 npm 套件

您不需要手動執行 `npm install`，只要要求 Agent 新增需要套件的功能，Agent 就會處理安裝和匯入作業。

**範例**：>「使用 `axios` 從外部 API 擷取資料。」

## 安全地管理密鑰

有了伺服器端程式碼和密鑰管理功能，您現在可以建構與世界互動的應用程式。

- **第三方 API**：連結至 Stripe、SendGrid 或自訂 REST API 等服務。
- **資料庫**：連線至外部資料庫 (例如透過 Supabase、Firebase 或 MongoDB Atlas)，在工作階段結束後保留資料。

建構實際應用程式時，您通常需要連線至第三方服務 (例如 Twilio、Slack 或資料庫)，這些服務需要 API 金鑰。您可以按照下列步驟手動新增金鑰：

1. **新增密鑰**：前往 Google AI Studio 的「設定」選單，然後找到「密鑰」專區。
2. **儲存金鑰**：在此新增 API 金鑰或密碼權杖。
3. **在程式碼中存取**：代理程式可以編寫伺服器端程式碼，安全地存取這些密鑰 (通常是透過環境變數)，確保密鑰絕不會暴露給用戶端瀏覽器。

如有需要，當需要新的 Secret 或在專案的環境變數中偵測到新的金鑰時，代理程式也會在對話中顯示資訊卡，提示您新增金鑰。

### 整合 Firebase 資料庫和驗證功能

現在透過 [Firebase 整合](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=zh-tw)，您可以在 Google AI Studio 中輕鬆為應用程式新增資料庫或驗證功能。Antigravity Agent 可以自動佈建及設定下列服務：

- **Firestore 資料庫**：彈性且可擴充的 NoSQL 雲端資料庫，可儲存及同步處理用戶端與伺服器端開發的資料。
- **Firebase 驗證**：讓使用者透過「使用 Google 帳戶登入」流程，安全地登入應用程式。

只要要求代理程式「在我的應用程式中新增資料庫」或「設定 Google 登入」，
代理程式就會為您處理必要的設定和程式碼產生作業。

Firebase 提供免費方案，您也可以視需求升級至付費帳戶，享有更多配額或使用付費功能。

### 設定 OAuth

密鑰管理的主要用途之一，是設定 OAuth 來連線至其他網站或應用程式。如果提示包含連線至需要 OAuth 驗證的第三方應用程式的操作說明，智慧助理會提供該應用程式的 OAuth 設定說明。這些操作說明會提供設定 OAuth 應用程式所需的必要回呼網址。您也可以在「設定」面板的「整合」下方找到回呼網址。

## 打造多人遊戲體驗

全堆疊執行階段可啟用即時協作功能。

- **即時狀態**：你可以要求 Agent 建構「即時通訊」、「協作白板」或「多人遊戲」等功能。
- **同步工作階段**：伺服器會管理狀態，讓多位使用者即時與同一個應用程式例項互動。

**範例提示**：「將這個遊戲設為多人遊戲，讓玩家可以看到彼此的游標。」

### 測試多人遊戲應用程式的訣竅

部署應用程式前，您可以透過兩種方式測試多人遊戲模式。

1. 在多個分頁中，以 Google AI Studio 建構模式開啟應用程式。在「建構」模式下開發時，應用程式會位於開發容器中。在多個分頁中開啟應用程式，即可模擬多位玩家使用應用程式。
2. 使用右上方的「分享」選單與他人共用應用程式。
   然後使用「分享」選單「整合」分頁中的「共用網址」，與您共用應用程式的玩家一起使用應用程式。

## 最佳做法

- **密鑰安全性**：請務必使用 Secret Manager 管理機密金鑰。
  請勿在檔案中以硬式編碼方式加入這些金鑰。
- **關注點分離**：將 UI 邏輯保留在用戶端框架 (React/Angular)，並將商業邏輯/資料處理保留在伺服器端。
- **錯誤處理**：確保伺服器端程式碼能妥善處理外部 API 呼叫的錯誤，避免應用程式當機。

## 後續步驟

- [在 Google AI Studio 中建構應用程式](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-tw)
- [應用程式庫](https://aistudio.google.com/apps?source=showcase&hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-04-29 (世界標準時間)。"],[],[]]
