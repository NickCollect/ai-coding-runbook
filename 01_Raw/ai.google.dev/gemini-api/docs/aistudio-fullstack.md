---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-TW
fetched_at: 2026-08-24T02:24:10.892317+00:00
title: "\u5728 Google AI Studio \u4e2d\u958b\u767c\u5168\u7aef\u61c9\u7528\u7a0b\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

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

### Gemini API 金鑰

建立使用 Gemini API 的新應用程式時，AI Studio 會自動將 `GEMINI_API_KEY` 設定為伺服器端密鑰，不需要手動設定。您可以在「設定」中的「密鑰」面板查看這項金鑰。應用程式的 Gemini API 呼叫是透過這個金鑰，從伺服器端程式碼發出，因此絕不會在瀏覽器中公開。

### 第三方 API 金鑰

如要使用其他服務，請手動新增 API 金鑰：

- **第三方 API**：連結至 Stripe、SendGrid 或自訂 REST API 等服務。
- **資料庫**：連線至外部資料庫 (例如透過 Supabase、Firebase 或 MongoDB Atlas)，在工作階段結束後保留資料。

建構實際應用程式時，您通常需要連線至第三方服務 (例如 Twilio、Slack 或資料庫)，而這些服務需要 API 金鑰。您可以按照下列步驟手動新增金鑰：

1. **新增密鑰**：前往 Google AI Studio 的「設定」選單，然後找到「密鑰」專區。
2. **儲存金鑰**：在此新增 API 金鑰或密碼權杖。
3. **在程式碼中存取**：代理程式可以編寫伺服器端程式碼，安全地存取這些密鑰 (通常是透過環境變數)，確保密鑰絕不會暴露給用戶端瀏覽器。

如有需要，當需要新密鑰或在專案的環境變數中偵測到新金鑰時，服務專員也會在對話中顯示資訊卡，提示您新增金鑰。

### 整合 Firebase 資料庫和驗證功能

現在，您只要透過 [Firebase 整合](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=zh-tw)，就能在 Google AI Studio 中輕鬆為應用程式新增資料庫或驗證功能。Antigravity Agent 可以自動佈建及設定下列服務：

- **Firestore 資料庫**：彈性且可擴充的 NoSQL 雲端資料庫，可儲存及同步處理用戶端與伺服器端開發的資料。
- **Firebase 驗證**：讓使用者透過「使用 Google 帳戶登入」流程，安全地登入應用程式。

只要要求代理程式「在我的應用程式中新增資料庫」或「設定 Google 登入」，
代理程式就會為您處理必要的設定和程式碼產生作業。

Firebase 提供免費方案，您也可以視需求升級至付費帳戶，享有更多配額或使用付費功能。

## Google Workspace API

Google AI Studio 可讓您建構連結至 Google Workspace API 的應用程式，讓使用者在應用程式中處理實際資料，例如電子郵件、試算表、文件、日曆活動等。您不必再設定 Google Cloud 雲端專案、設定 OAuth 或手動管理 API。

### 運作方式

您可以透過兩種方式新增 Workspace 整合：

- **在對話面板中描述**：只要在底部的對話面板中告訴代理程式所需內容，例如「建立費用追蹤工具，將收據記錄到我的 Google 試算表」或「建立摘要顯示未讀取 Gmail 郵件的資訊主頁」。
- **從整合面板選取**：在「建構」模式的右側邊欄中開啟「整合」面板，然後啟用要連結的 Workspace 應用程式。

新增 Workspace 應用程式時，AI Studio 會自動執行下列操作：

1. 為應用程式設定必要的 Google API。
2. 產生呼叫 API 的伺服器端程式碼。
3. 新增安全的「使用 Google 帳戶登入」流程，讓應用程式的終端使用者授權存取自己的資料。

### 支援的應用程式

可用的 Google Workspace 應用程式如下：

| 應用程式 | 可建構的內容 |
| --- | --- |
| Google 日曆 | 讀取、建立及管理活動和日曆 |
| Google Chat | 讀取及參與對話和群組聊天室 |
| Google 文件 | 建立、讀取、更新及設定文件格式 |
| Google 雲端硬碟 | 整理、搜尋及管理檔案和資料夾 |
| Google 表單 | 建立問卷調查、更新問題及擷取回覆 |
| Gmail | 讀取、傳送及管理電子郵件內容 |
| Google Keep | 管理記事、清單和附件 |
| Google Meet | 安排及管理視訊通話 |
| 聯絡人 | 同步及管理聯絡人 |
| Google 試算表 | 讀取、寫入及格式化試算表資料 |
| Google 簡報 | 建立及修改簡報 |
| Google Tasks | 建立、管理及整理工作 |

### 驗證和權限

身為建構者，您不需要設定 OAuth 用戶端、管理憑證或設定 Google Cloud 專案。AI Studio 會為您處理所有這些事項。

整合 Workspace API 的應用程式會使用「使用 Google 帳戶登入」驗證使用者身分。使用者開啟應用程式時，系統會提示他們登入並授予應用程式所需的特定權限 (例如日曆的唯讀存取權，或是編輯試算表的權限)。應用程式只會存取使用者的資料。每位使用者都會授權存取自己的帳戶。

### 提示詞範例

以下提供幾個構想，協助您開始使用 Workspace 整合功能：

- *「建立一個應用程式，讀取我的 Google 日曆，並在 Gmail 中為每場會議草擬準備電子郵件。」*
- 「建立工具，將 Google 文件內容生成 5 張投影片的摘要簡報，並匯入 Google 簡報。」
- *「製作費用追蹤工具，讓我上傳收據，Gemini 擷取詳細資料，並在 Google 試算表中記錄新資料列。」*

### 設定 OAuth

密鑰管理的主要用途之一是設定 OAuth，以便連線至其他網站或應用程式。如果提示包含連線至需要 OAuth 驗證的第三方應用程式的操作說明，智慧助理會提供該應用程式的 OAuth 設定說明。這些操作說明會提供設定 OAuth 應用程式所需的必要回呼網址。您也可以在「設定」面板的「整合」下方找到回呼網址。

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

- **Gemini API 呼叫**：系統會自動將 `GEMINI_API_KEY` 設定為伺服器端密鑰。使用這個金鑰，從伺服器端程式碼呼叫 Gemini API。您可以在「密鑰」面板中查看。
- **密鑰安全性**：請務必使用 Secret Manager 管理機密金鑰。
  請勿在檔案中以硬式編碼方式加入這些金鑰。
- **關注點分離**：將 UI 邏輯保留在用戶端框架 (React/Angular)，並將商業邏輯/資料處理保留在伺服器端。
- **錯誤處理**：確保伺服器端程式碼能妥善處理外部 API 呼叫的錯誤，避免應用程式當機。

## 後續步驟

- [在 Google AI Studio 中建構應用程式](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-tw)
- [從 Google AI Studio 部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-tw)
- [應用程式庫](https://aistudio.google.com/apps?source=showcase&hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-08-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-08-19 (世界標準時間)。"],[],[]]
