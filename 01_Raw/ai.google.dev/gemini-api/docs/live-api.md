---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=zh-TW
fetched_at: 2026-07-20T04:43:39.601843+00:00
title: "Gemini Live API \u7e3d\u89bd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini Live API 總覽

透過 Live API，您可以與 Gemini 展開低延遲的即時語音和視覺互動。這項服務可處理連續的音訊、圖片和文字，並立即以擬真語音回應，為使用者打造自然的對話體驗。

![Live API 總覽](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=zh-tw)

[在 Google AI Studio 中試用 Live APImic](https://aistudio.google.com/live?hl=zh-tw)
[從 GitHub 複製範例應用程式code](https://github.com/google-gemini/gemini-live-api-examples)
[使用程式碼編寫代理程式技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-tw)

## 用途

Live API 可用於為各種產業建構即時語音代理程式，包括：

- **電子商務和零售：**提供個人化建議的購物助理，以及解決顧客問題的支援代理。
- **遊戲：**互動式非玩家角色 (NPC)、遊戲內輔助助理，以及遊戲內容的即時翻譯。
- **新一代介面：**在機器人、智慧眼鏡和車輛中，提供支援語音和視訊的體驗。
- **醫療保健：**為病患提供支援和教育資訊的健康夥伴。
- **金融服務：**AI 顧問提供財富管理和投資建議。
- **教育：**AI 導師和學習夥伴，提供個人化指導和意見回饋。
- **翻譯和本地化：**即時翻譯口語對話，延遲時間短，可順暢進行多語言溝通。

## 主要功能與特色

Live API 提供完整的功能，可建構強大的語音代理程式：

- [**支援多種語言**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw#supported-languages)：
  支援 70 種語言。
- [**插話**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw#interruptions)：
  使用者隨時可以打斷模型，進行回應式互動。
- [**使用工具**](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-tw)：
  整合函式呼叫和 Google 搜尋等工具，進行動態互動。
- [**音訊轉錄稿**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw#audio-transcription)：
  提供使用者輸入內容和模型輸出內容的文字轉錄稿。
- [**主動式語音**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw#proactive-audio)：
  可控制模型的回覆時間和情境。
- [**情感對話**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw#affective-dialog)：
  根據使用者輸入內容的措辭調整回覆風格和語氣。
- [**即時翻譯**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=zh-tw)：
  即時翻譯語音內容，支援超過 70 種語言。

## 技術規格

下表列出 Live API 的技術規格：

| 類別 | 詳細資料 |
| --- | --- |
| 輸入模態 | 音訊 (原始 16 位元 PCM 音訊，16 kHz，小端序)、圖片 (JPEG <= 1 FPS)、文字 |
| 輸出模態 | 音訊 (原始 16 位元 PCM 音訊，24 kHz，小端序) |
| 通訊協定 | 具狀態的 WebSocket 連線 (WSS) |

## 選擇導入方式

整合 Live API 時，您需要選擇下列其中一種實作方式：

- **伺服器對伺服器**：後端會使用 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) 連線至 Live API。一般來說，用戶端會將串流資料 (音訊、影片、文字) 傳送至伺服器，然後伺服器會將資料轉送至 Live API。
- **用戶端到伺服器**：前端程式碼會使用 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) 直接連線至 Live API 來串流資料，略過後端。

## 開始使用

選取與開發環境相符的指南：

伺服器對伺服器

### [GenAI SDK 教學課程](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-tw)

使用 GenAI SDK 連線至 Gemini Live API，透過 Python 後端建構即時多模態應用程式。

用戶端對伺服器

### [WebSocket 教學課程](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=zh-tw)

使用 WebSockets 連線至 Gemini Live API，透過 JavaScript 前端和臨時權杖建構即時多模態應用程式。

Agent Development Kit

### [ADK 教學課程](https://google.github.io/adk-docs/streaming/)

建立代理程式，並使用 Agent Development Kit (ADK) 串流功能啟用語音和視訊通訊。

## 與合作夥伴整合

如要簡化即時音訊和視訊應用程式的開發作業，您可以透過 WebRTC 或 WebSocket 使用支援 Gemini Live API 的第三方整合服務。

[LiveKit

搭配 LiveKit Agents 使用 Gemini Live API。](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

使用 Gemini Live 和 Pipecat 建立即時 AI 聊天機器人。](https://docs.pipecat.ai/guides/features/gemini-live)
[Software Mansion 的 Fishjam

使用 Fishjam 建立即時影像和音訊串流應用程式。](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Stream 的 Vision Agents

使用 Vision Agents 建構即時語音和視訊 AI 應用程式。](https://visionagents.ai/integrations/gemini)
[Voximplant

使用 Voximplant 將撥入和撥出電話連線至 Live API。](https://voximplant.com/products/gemini-client)
[Agora

使用 Agora 建構即時對話式 AI 應用程式。](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

使用 Firebase AI Logic 開始使用 Gemini Live API。](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-12 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-12 (世界標準時間)。"],[],[]]
