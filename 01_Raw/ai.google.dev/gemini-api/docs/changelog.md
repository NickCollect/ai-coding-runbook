---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=zh-TW
fetched_at: 2026-05-05T20:03:14.215659+00:00
title: "\u7248\u672c\u8cc7\u8a0a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 版本資訊

本頁面說明 Gemini API 的更新內容。

## 2026 年 5 月 5 日

- 更新「檔案搜尋」，支援多模態搜尋。您現在可以使用 `gemini-embedding-2` 模型，以原生方式嵌入及搜尋圖片。基礎中繼資料現在包含 `media_id`，可顯示視覺引用內容，以及 `page_numbers`，可指出資訊來源。詳情請參閱「[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)」指南。

## 2026 年 5 月 4 日

- 在 Gemini API 中推出事件導向的 [Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=zh-tw) 支援，取代 Batch API 和長時間執行的作業輪詢工作流程。

## 2026 年 4 月 30 日

- `gemini-robotics-er-1.5-preview` 模型已[關閉](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)。請改用 [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=zh-tw)。

## 2026 年 4 月 22 日

- 正式發布 `gemini-embedding-2` 做為正式版 (GA)。詳情請參閱「[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw)」頁面。

## 2026 年 4 月 21 日

- 發布新版「Deep Research」代理程式，支援協作規劃、視覺化、MCP 伺服器整合和檔案搜尋：

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=zh-tw)：專為速度和效率而設計，非常適合串流回用戶端 UI。
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=zh-tw)：自動收集及綜合分析背景資訊時，盡可能提供最全面的資訊。

## 2026 年 4 月 15 日

- 推出 [Gemini 3.1 Flash TTS 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=zh-tw)，這是經濟實惠、生動且可控的文字轉語音模型。詳情請參閱 [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw) 說明文件。

## 2026 年 4 月 14 日

- 我們發布了更新版機器人模型 `gemini-robotics-er-1.6-preview`。現在還具備樂器辨識、更強大的空間和物理推論能力等新功能。詳情請參閱 [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-tw) 頁面和[網誌](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=zh-tw)。
- 淘汰公告：`gemini-robotics-er-1.5-preview` 模型將於 2026 年 4 月 30 日太平洋時間上午 9 點[停止服務](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)。

## 2026 年 4 月 2 日

- `gemma-4-26b-a4b-it`和 `gemma-4-31b-it`已發布，可透過 [AI Studio](https://aistudio.google.com?hl=zh-tw) 和 Gemini API 使用，是 [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=zh-tw) 發布計畫的一部分。

## April 1, 2026

- 推出新的 [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw) 和 [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw) 推論層級，提供更多選項，協助您最佳化成本或延遲時間。

## 2026 年 3 月 31 日

- 推出 Veo 3.1 Lite 搶先版 [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=zh-tw)，這是我們最經濟實惠的[影片生成](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw)模型，專為快速疊代及建構大量應用程式而設計。
- `gemini-2.5-flash-lite-preview-09-2025` 模型已關閉。請改用 [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-tw)。

## 2026 年 3 月 26 日

- 最新推出的 [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=zh-tw) 音訊對音訊 (A2A) 模型，專為即時對話和語音優先的 AI 應用程式設計。請參閱 [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw) 文件，瞭解如何開始使用。

## 2026 年 3 月 25 日

- 推出 [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-tw) 音樂生成模型：[`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=zh-tw) (30 秒片段) 和 [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=zh-tw) (完整歌曲)。這兩款模型都能接收文字和圖像輸入內容，並生成高品質的 48 kHz 立體聲音訊。詳情和程式碼範例請參閱「[音樂生成](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-tw)」指南。

## March 23, 2026

- 在 AI Studio 中推出[預付和後付帳單方案](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)。現有帳戶可能會受到影響；詳情請參閱「[帳單](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)」說明文件。

## 2026 年 3 月 18 日

- 推出[內建工具和函式呼叫組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)功能，讓您在單一 API 呼叫中，同時使用 Gemini 的內建工具和自訂函式呼叫工具。
- Gemini 3 模型現已支援[利用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw#supported_models)的服務。

## 2026 年 3 月 16 日

- 推出全新[用量層級](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#about-billing)和[帳單帳戶支出上限](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#tier-spend-caps)，提供更優質的帳單體驗。

## 2026 年 3 月 12 日

- 在 AI Studio 的帳單中導入[專案層級的支出上限](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#project-spend-caps)。

## 2026 年 3 月 10 日

- 發布 `gemini-embedding-2-preview`，這是我們第一個多模態嵌入模型。
  這項模型支援文字、圖片、影片、音訊和 PDF 輸入內容，並將所有模態對應至統一的嵌入空間。詳情請參閱「[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw)」。
- 淘汰公告：`gemini-2.5-flash-lite-preview-09-2025` 模型將於 2026 年 3 月 31 日[停用](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)。

## 2026 年 3 月 9 日

- Gemini 3 Pro 預先發布版模型已[停止服務](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)。`gemini-3-pro-preview` 現在指向 [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw)。

## 2026 年 3 月 3 日

- 推出 Gemini 3.1 Flash-Lite 預先發布版，這是 Gemini 3 系列中的第一個 Flash-Lite 模型。如需規格、特定更新和開發人員指南，請參閱[型號頁面](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-tw)。

## 2026 年 2 月 26 日

- 推出 Nano Banana 2 ([Gemini 3.1 Flash Image 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=zh-tw))，這款高效率模型經過最佳化處理，速度飛快，適合大量使用。
- 淘汰公告：Gemini 3 Pro 預先發布版 (`gemini-3-pro-preview`) 將於 2026 年 3 月 9 日[停止服務](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)。

## 2026 年 2 月 19 日

- 發布 [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw)，這是全新 Gemini 3 系列的最新版本。
- 推出獨立端點 `gemini-3.1-pro-preview-customtools`，可更妥善地優先處理自訂工具，適合同時使用 Bash 和工具建構的使用者。

## 2026 年 2 月 18 日

- 淘汰公告：下列模型將於 2026 年 6 月 1 日[停止服務](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)：

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 2026 年 2 月 17 日

- 下列模型已[關閉](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)：

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 2026 年 1 月 29 日

- 在 `gemini-3-pro-preview` 和 `gemini-3-flash-preview` 推出電腦使用工具。

## 2026 年 1 月 21 日

- 變更 `latest` 別名：

  - `gemini-pro-latest`已切換為 `gemini-3-pro-preview`
  - `gemini-flash-latest`已切換為 `gemini-3-flash-preview`

## 2026 年 1 月 15 日

- 淘汰公告：下列模型將於 2026 年 2 月 17 日[停止服務](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)：

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- `gemini-2.5-flash-image-preview` 模型已關閉。

## 2026 年 1 月 14 日

- `text-embedding-004` 模型已[關機](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)。

## 2026 年 1 月 13 日

- 為 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw) 新增 4K 輸出解析度，並支援所有解析度的直向影片。

## 2026 年 1 月 12 日

- 推出模型生命週期功能。部分模型現在會指定生命週期階段和淘汰時間表。詳情請參閱下列說明文件：

  - [模型階段](https://ai.google.dev/api/generate-content?hl=zh-tw#ModelStatus)

## 2026 年 1 月 8 日

- 支援 Cloud Storage 儲存空間和任何公開與私有 DB 預先簽署的網址，做為 Gemini API 的資料輸入來源。檔案大小上限也從 20MB 提高至 100MB。詳情請參閱[檔案輸入法指南](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-tw)。

## 2025 年 12 月 19 日

- 在 v1beta 中，對 Interactions API 公開預先發布版進行破壞性變更。`total_reasoning_tokens` 欄位已重新命名為 `total_thought_tokens`，以便與思考型模型中的「想法」概念更一致。

## 2025 年 12 月 17 日

- 推出 Gemini 3 Flash 預先發布版 `gemini-3-flash-preview`，以低成本提供媲美大型模型的快速頂尖效能。升級的視覺和空間推論能力，以及代理功能編碼功能。請參閱說明文件，瞭解部分新功能，包括：

  - [多模態函式回應](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#multimodal)
  - [執行程式碼並顯示圖片](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw#images)

## 2025 年 12 月 12 日

- 發布 `gemini-2.5-flash-native-audio-preview-12-2025`，這是 Live API 的全新原生音訊模型。這項更新可提升模型處理複雜工作流程的能力。詳情請參閱 [Live API 指南](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw)和 [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=zh-tw)。

## 2025 年 12 月 11 日

- 推出 Beta 版的 Interactions API。這個 API 提供統一的介面，可與 Gemini 模型和代理程式互動。詳情請參閱[互動 API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw) 指南。
- 推出 Gemini Deep Research 代理 (預先發布版)。這項功能可自主規劃、執行及彙整多步驟研究工作的結果。詳情請參閱「[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw)」指南。

## 2025 年 12 月 10 日

- 推出[文字轉語音模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)的強化功能，包括 Gemini 2.5 Flash TTS 搶先版 (針對低延遲最佳化) 和 Gemini 2.5 Pro TTS 搶先版 (針對品質最佳化)，可提升表現力、精準掌握語速，以及流暢對話。

## 2025 年 12 月 9 日

- 下列 Gemini Live API 模型現已停止服務：
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 2025 年 12 月 5 日

- 2026 年 1 月 5 日起，系統將開始收取 Gemini 3 的「[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)」費用。

## 2025 年 12 月 4 日

- 淘汰公告：`gemini-2.5-flash-image-preview` 模型將於 2026 年 1 月 15 日停用。

## 2025 年 12 月 3 日

- 淘汰公告：`text-embedding-004` 模型將於 2026 年 1 月 14 日停用。

## 2025 年 11 月 20 日

- 發布 Gemini 3 Pro Image 預先發布版 `gemini-3-pro-image-preview`，這是 Nano Banana 模型的下一個疊代版本。詳情請參閱「[圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)」頁面。

## 2025 年 11 月 18 日

- 推出首款 Gemini 3 系列模型 `gemini-3-pro-preview`，這是 Google 最先進的推論和多模態理解模型，具備強大的代理功能和程式設計能力。

  除了智慧和效能方面的改良，Gemini 3 Pro 預先發布版還導入了以下新行為：

  - [媒體解析度](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-tw)
  - [想法簽名](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-tw)
  - [思考程度](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw#thinking-levels)

  請參閱 [Gemini 3 開發人員指南](https://ai.google.dev/gemini-api/docs/gemini-3?hl=zh-tw)，瞭解遷移作業、新功能和規格。

## 2025 年 11 月 11 日

- 淘汰公告：下列模型即將停止服務：

  - 11 月 12 日：

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 11 月 14 日：

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 2025 年 11 月 10 日

- 下列模型已關閉：

  - `imagen-3.0-generate-002`

  請改用 [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=zh-tw#imagen-4)。詳情請參閱 [Gemini 淘汰項目表](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)。

## 2025 年 11 月 6 日

- 推出檔案搜尋 API 公開預覽版，讓開發人員能根據自有資料建立回覆基準。詳情請參閱新的「[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)」頁面。

## 2025 年 11 月 4 日

- [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) 的圖片輸入權杖數從 1290 個減少至 258 個，降低圖片編輯成本。
- 淘汰公告：下列模型即將停止服務：

  - 11 月 18 日：

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 12 月 2 日：

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 12 月 9 日：

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 2025 年 10 月 29 日

- 推出 Gemini API 的全新[記錄和資料集](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-tw)工具。

## 2025 年 10 月 20 日

- 下列 Gemini Live API 模型現已停止服務：

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  請改用 `gemini-2.5-flash-native-audio-preview-09-2025`。
- 淘汰公告：`gemini-2.0-flash-live-001` 和 `gemini-live-2.5-flash-preview` 將於 2025 年 12 月 9 日停用。

## 2025 年 10 月 17 日

- **利用 Google 地圖建立基準**的服務現已正式推出。詳情請參閱「[利用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)」說明文件。

## 2025 年 10 月 15 日

- 推出 [Veo 3.1 和 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#veo-3.1) 模型公開預先發布版，新功能包括：

  - 延長 Veo 製作的影片。
  - 參考最多三張圖片來生成影片。
  - 提供影片的開頭和結尾影格圖片，讓 AI 生成影片。

  這次更新也為 Veo 3 輸出影片新增更多時長選項：4 秒、6 秒和 8 秒。
- 淘汰公告：`veo-3.0-generate-preview` 和 `veo-3.0-fast-generate-preview` 將於 2025 年 11 月 12 日停用。

## 2025 年 10 月 7 日

- 推出 [Gemini 2.5 Computer Use 預先發布版](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)

## 2025 年 10 月 2 日

- 推出 Gemini 2.5 Flash Image 正式版：[使用 Gemini 生成圖片](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)

## September 29, 2025

- 下列 Gemini 1.5 模型現已停止服務：
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 2025 年 9 月 25 日

- 發布 Gemini Robotics-ER 1.5 模型預先發布版。請參閱[機器人技術總覽](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-tw)，瞭解如何將模型用於機器人應用程式。
- 推出下列預先發布版模型：

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  詳情請參閱「[模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)」頁面。

## 2025 年 9 月 23 日

- 發布 `gemini-2.5-flash-native-audio-preview-09-2025`，這是 Live API 的全新原生音訊模型，可改善函式呼叫和語音中斷處理功能。詳情請參閱 [Live API 指南](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw)和 [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-native-audio)。

## 2025 年 9 月 16 日

- 淘汰公告：下列機型將於 2025 年 10 月停用：

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  如要瞭解最新嵌入模型，請參閱「[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw)」頁面。

## 2025 年 9 月 10 日

- 支援[批次 API 中的 Embeddings 模型](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw#batch-embedding)，並在 [OpenAI 相容性程式庫](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw#batch)中新增批次 API，讓您更輕鬆地開始使用批次查詢。

## 2025 年 9 月 9 日

- 推出 Veo 3 和 Veo 3 Fast 正式版，價格更低，並提供新的長寬比、解析度和種子選項。詳情請參閱 [Veo 說明文件](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#model-features)。

## 2025 年 8 月 26 日

- 推出 [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-image-preview)，這是我們最新的原生圖像生成模型。

## 2025 年 8 月 18 日

- [網址背景資訊工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)正式發布，可提供網址做為提示的額外背景資訊。我們將於一週後停止支援搭配 `gemini-2.0-flash` 模型使用網址內容 (實驗版)。

## 2025 年 8 月 14 日

- Imagen 4 Ultra、Standard 和 Fast 模型已正式發布 (GA)。詳情請參閱 [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=zh-tw) 頁面。

## 2025 年 8 月 7 日

- `allow_adult`設定，但目前僅適用於特定地區。詳情請參閱 [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=zh-tw#veo-model-parameters) 頁面。

## 2025 年 7 月 31 日

- 推出 Veo 3 搶先體驗版模型的圖像生成影片功能。
- 發布 Veo 3 Fast 預先發布版模型。
- 如要進一步瞭解 Veo 3，請前往 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw) 頁面。

## 2025 年 7 月 22 日

- 我們已於 `gemini-2.5-flash-lite`推出 Gemini 2.5 模型，這個模型速度快、成本低且效能高。詳情請參閱 [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-lite)。

## 2025 年 7 月 17 日

- 推出 `veo-3.0-generate-preview`，這是 Veo 的最新更新，可生成含音訊的影片。如要進一步瞭解 Veo 3，請前往 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw) 頁面。
- 提高 Imagen 4 Standard 和 Ultra 的速率限制。詳情請參閱「[速率限制](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-tw)」頁面。

## 2025 年 7 月 14 日

- 發布文字嵌入模型穩定版 `gemini-embedding-001`。詳情請參閱「[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw)」。`gemini-embedding-exp-03-07`模型將於 2025 年 8 月 14 日淘汰。

## 2025 年 7 月 7 日

- 推出 Gemini API 批次模式。將要求批次處理並非同步傳送，詳情請參閱「[批次模式](https://ai.google.dev/gemini-api/docs/batch-mode?hl=zh-tw)」。

## 2025 年 6 月 26 日

- 預覽模型 `gemini-2.5-pro-preview-05-06` 和 `gemini-2.5-pro-preview-03-25` 現在會重新導向至最新穩定版 `gemini-2.5-pro`。
- `gemini-2.5-pro-exp-03-25`已關機。

## 2025 年 6 月 24 日

- 發布 Imagen 4 Ultra 和 Standard 預先發布版模型。詳情請參閱「[圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)」頁面。

## 2025 年 6 月 17 日

- 發布 `gemini-2.5-pro` 穩定版，這是 Google 最強大的模型，現在還具備適應性思考能力。詳情請參閱「[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-pro)」和「[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)」一節。`gemini-2.5-pro-preview-05-06`
  將於 2025 年 6 月 26 日重新導向至 `gemini-2.5-pro`。
- 發布第一個穩定版 2.5 Flash 模型「`gemini-2.5-flash`」。詳情請參閱「[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash)」。`gemini-2.5-flash-preview-04-17` 將於 2025 年 7 月 15 日淘汰。
- 推出 `gemini-2.5-flash-lite-preview-06-17`，這款 Gemini 2.5 模型價格低廉，但效能優異。如要瞭解詳情，請參閱 [Gemini 2.5 Flash-Lite 搶先版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-lite)。

## 2025 年 6 月 5 日

- 發布了 `gemini-2.5-pro-preview-06-05`，這是 Google 最強大模型的新版本，現在具備適應性思考能力。詳情請參閱「[Gemini 2.5 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-pro-preview-06-05)」和「[思考型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)」。`gemini-2.5-pro-preview-05-06` 將於 2025 年 6 月 26 日重新導向至 `gemini-2.5-pro`。

## 2025 年 5 月 27 日

- 最後一個可用的微調模型 Gemini 1.5 Flash 001 已停止服務。所有模型都不再支援微調。
  請參閱「[使用 Gemini API 微調](https://ai.google.dev/gemini-api/docs/model-tuning?hl=zh-tw)」。

## 2025 年 5 月 20 日

**API 更新：**

- 推出支援功能，可使用剪輯間隔和可設定的影格率取樣，進行[自訂影片前處理](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw#customize-video-processing)。
- 推出多工具使用功能，支援在同一個 `generateContent` 要求中設定[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)和[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-tw)。
- 在 Live API 中推出[非同步函式呼叫](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-tw#async-function-calling)支援功能。
- 推出實驗性[網址背景資訊工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)，可提供網址做為提示的額外背景資訊。

**模型更新：**

- 發布 `gemini-2.5-flash-preview-05-20`，這是經過最佳化的 Gemini[預先發布版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#model-versions)模型，可提供高性價比和適應性思考能力。詳情請參閱「[Gemini 2.5 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-preview)」和「[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)」。
- 發布 [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-pro-preview-tts) 和 [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-preview-tts) 模型，可[生成語音](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)，支援一或兩名說話者。
- 發布 `lyria-realtime-exp` 模型，可[即時生成音樂](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-tw)。
- 發布 `gemini-2.5-flash-preview-native-audio-dialog` 和 `gemini-2.5-flash-exp-native-audio-thinking-dialog`，以及適用於 Live API 的新 Gemini 模型，支援原生音訊輸出功能。如要瞭解詳情，請參閱 [Live API 指南](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw#native-audio-output)和 [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-native-audio)。
- 發布`gemma-3n-e4b-it`預先發布版，可透過 [AI Studio](https://aistudio.google.com?hl=zh-tw) 和 Gemini API 取得，是 [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=zh-tw) 發布計畫的一部分。

## 2025 年 5 月 7 日

- 發布 `gemini-2.0-flash-preview-image-generation`，這是用於生成和編輯圖像的預覽模型。詳情請參閱「[圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)」和「[Gemini 2.0 Flash 預先發布版圖像生成](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.0-flash-preview-image-generation)」。

## 2025 年 5 月 6 日

- 我們發布了最強大的模型新版本 `gemini-2.5-pro-preview-05-06`，並改善了程式碼和函式呼叫功能。`gemini-2.5-pro-preview-03-25`
  會自動指向新版模型。

## 2025 年 4 月 17 日

- 發布 `gemini-2.5-flash-preview-04-17`，這是經過最佳化的 Gemini[預先發布版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#model-versions)模型，可提供高性價比和適應性思考能力。詳情請參閱「[Gemini 2.5 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-flash-preview)」和「[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)」。

## 2025 年 4 月 16 日

- 推出 [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.0-flash) 的內容快取功能。

## 2025 年 4 月 9 日

**模型更新：**

- 發布 `veo-2.0-generate-001`，這是正式發布的文字和圖像轉影片模型，可生成細緻且充滿藝術感的影片。詳情請參閱 [Veo 說明文件](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw)。
- 發布 `gemini-2.0-flash-live-001`，這是啟用計費功能的 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw) 模型公開預先發布版。

  - **強化工作階段管理和穩定性**

    - **工作階段續傳：**即使網路暫時中斷，工作階段仍會持續運作。這項 API 現在支援伺服器端工作階段狀態儲存 (最多 24 小時)，並提供控點 (session\_resumption) 以重新連線，並從上次中斷的地方繼續。
    - **透過脈絡壓縮延長對話時間：**啟用這項功能後，對話時間將不受限制，使用滑動視窗機制設定內容視窗壓縮，自動管理內容長度，避免因內容限制而突然終止。
    - **正常中斷連線通知：**接收 `GoAway` 伺服器訊息，瞭解連線即將關閉的時間，以便在終止前正常處理。
  - **進一步掌控互動動態**
  - **可設定的語音活動偵測 (VAD)：**選擇靈敏度等級，或完全停用自動 VAD，並使用新的用戶端事件 (`activityStart`、`activityEnd`) 手動控制通話。
  - **可設定的中斷處理方式：**決定使用者輸入內容是否應中斷模型的回覆。
  - **可設定的 Turn 涵蓋範圍：**選擇 API 是要持續處理所有音訊和視訊輸入內容，還是只在偵測到使用者說話時擷取。
  - **可設定的媒體解析度：**選取輸入媒體的解析度，以盡量提高品質或減少權杖用量。
  - **更豐富的輸出內容和功能**
  - **擴充語音和語言選項：**選擇兩種新語音和 30 種新語言，做為音訊輸出內容的語音。現在可以在 `speechConfig` 中設定輸出語言。
  - **文字串流：**逐步接收生成的文字回覆，以便更快向使用者顯示內容。
  - **權杖用量報表：**透過伺服器訊息 `usageMetadata` 欄位中提供的詳細權杖計數，深入瞭解用量，並依模式和提示或回應階段細分。

## 2025 年 4 月 4 日

- 發布 `gemini-2.5-pro-preview-03-25` Gemini 2.5 Pro 公開預先發布版，並啟用帳單功能。您可以在免費方案中繼續使用「`gemini-2.5-pro-exp-03-25`」。

## 2025 年 3 月 25 日

- 發布 `gemini-2.5-pro-exp-03-25`，這是公開的實驗性 Gemini 模型，預設一律開啟思考模式。詳情請參閱「[Gemini 2.5 Pro 實驗版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-2.5-pro-preview-03-25)」。

## 2025 年 3 月 12 日

**模型更新：**

- 推出實驗性 [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw#gemini) 模型，可生成及編輯圖片。
- 已於 `gemma-3-27b-it`發布，可透過 [AI Studio](https://aistudio.google.com?hl=zh-tw) 和 Gemini API 使用，是 [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=zh-tw) 發布計畫的一部分。

**API 更新：**

- 開始支援將 [YouTube 網址](https://ai.google.dev/gemini-api/docs/vision?hl=zh-tw#youtube)做為媒體來源。
- 新增支援內嵌小於 20 MB 的[影片](https://ai.google.dev/gemini-api/docs/vision?hl=zh-tw#inline-video)。

## 2025 年 3 月 11 日

**SDK 更新：**

- 公開預先發布 [Google Gen AI SDK for TypeScript and JavaScript](https://googleapis.github.io/js-genai)。

## 2025 年 3 月 7 日

**模型更新：**

- 發布`gemini-embedding-exp-03-07`以 Gemini 為基礎的[實驗性](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-tw)嵌入模型，並推出公開預先發布版。

## 2025 年 2 月 28 日

**API 更新：**

- [搜尋工具](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-tw)支援`gemini-2.0-pro-exp-02-05`，這是以 Gemini 2.0 Pro 為基礎的實驗模型。

## 2025 年 2 月 25 日

**模型更新：**

- 發布 `gemini-2.0-flash-lite` Gemini 2.0 Flash-Lite 正式版，這款模型經過最佳化，速度快、可擴充性高，且成本效益高。

## 2025 年 2 月 19 日

**AI Studio 更新：**

- 支援[其他地區](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-tw) (科索沃、格陵蘭和法羅群島)。

**API 更新：**

- 支援[其他地區](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-tw) (科索沃、格陵蘭和法羅群島)。

## 2025 年 2 月 18 日

**模型更新：**

- Gemini 1.0 Pro 已停止支援，如需支援的型號清單，請參閱「[Gemini 模型](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw)」。

## 2025 年 2 月 11 日

**API 更新：**

- [OpenAI 程式庫相容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)更新。

## 2025 年 2 月 6 日

**模型更新：**

- 發布 `imagen-3.0-generate-002`，這是 [Gemini API 中的 Imagen 3](https://ai.google.dev/gemini-api/docs/imagen?hl=zh-tw) 正式版。

**SDK 更新：**

- 發布 [Google Gen AI SDK for Java](https://github.com/googleapis/java-genai) 公開預先發布版。

## 2025 年 2 月 5 日

**模型更新：**

- 發布 `gemini-2.0-flash-001`，這是 [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-2.0-flash) 的正式發布版，支援僅輸出文字。
- 發布 Gemini 2.0 Pro 的`gemini-2.0-pro-exp-02-05`[實驗版](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-tw)公開預先發布版。
- 發布實驗性公開搶先版`gemini-2.0-flash-lite-preview-02-05`[模型](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-2.0-flash-lite)，可提高成本效益。

**API 更新：**

- 在程式碼執行中新增[檔案輸入和圖表輸出](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw#input-output)支援。

**SDK 更新：**

- 正式發布 [Google Gen AI SDK for Python](https://googleapis.github.io/python-genai/)。

## 2025 年 1 月 21 日

**模型更新：**

- 發布 `gemini-2.0-flash-thinking-exp-01-21`，這是 [Gemini 2.0 Flash Thinking 模型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)的最新預先發布版。

## 2024 年 12 月 19 日

**模型更新：**

- 發布 Gemini 2.0 Flash 思考型模式，供公開預先發布版。思考模式是測試時的運算模型，可讓您在模型生成回覆時，查看模型的思考過程，並生成推論能力更強的回覆。

  如要進一步瞭解 Gemini 2.0 Flash Thinking 模式，請參閱[總覽頁面](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=zh-tw)。

## 2024 年 12 月 11 日

**模型更新：**

- 發布 [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-2.0-flash) 公開預先發布版。Gemini 2.0 Flash Experimental 的部分功能包括：
  - 速度是 Gemini 1.5 Pro 的兩倍
  - 透過 Live API 進行雙向串流
  - 生成文字、圖片和語音等多模態回覆
  - 使用內建工具，透過多輪推論使用程式碼執行、搜尋、函式呼叫等功能

如要進一步瞭解 Gemini 2.0 Flash，請參閱[總覽頁面](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=zh-tw)。

## 2024 年 11 月 21 日

**模型更新：**

- 推出 `gemini-exp-1121`，這是功能更強大的實驗性 Gemini API 模型。

**模型更新：**

- 更新 `gemini-1.5-flash-latest` 和 `gemini-1.5-flash` 模型別名，使用 `gemini-1.5-flash-002`。
  - 變更為 `top_k` 參數：`gemini-1.5-flash-002` 模型支援介於 1 到 41 (不含) 之間的 `top_k` 值。如果值大於 40，系統會將其變更為 40。

## 2024 年 11 月 14 日

**模型更新：**

- 發布 `gemini-exp-1114`，這是功能強大的實驗性 Gemini API 模型。

## 2024 年 11 月 8 日

**API 更新：**

- 在 OpenAI 程式庫 / REST API 中[新增 Gemini 支援](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)。

## 2024 年 10 月 31 日

**API 更新：**

- 新增[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-tw)的支援。

## 2024 年 10 月 3 日

**模型更新：**

- 發布 `gemini-1.5-flash-8b-001`，這是最小的 Gemini API 模型穩定版。

## 2024 年 9 月 24 日

**模型更新：**

- 正式發布 Gemini 1.5 Pro 和 1.5 Flash 的兩個全新穩定版本，分別於 `gemini-1.5-pro-002`和 `gemini-1.5-flash-002`推出。
- 更新 `gemini-1.5-pro-latest` 模型程式碼，改用 `gemini-1.5-pro-002`，並更新 `gemini-1.5-flash-latest` 模型程式碼，改用 `gemini-1.5-flash-002`。
- 發布 `gemini-1.5-flash-8b-exp-0924` 以取代 `gemini-1.5-flash-8b-exp-0827`。
- 為 Gemini API 和 AI Studio 發布[公民誠信安全篩選器](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-tw#safety-filters)。
- 在 Python 和 NodeJS 中，為 Gemini 1.5 Pro 和 1.5 Flash 新增兩個參數的支援：[`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=zh-tw#FIELDS.frequency_penalty) 和 [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=zh-tw#FIELDS.presence_penalty)。

## 2024 年 9 月 19 日

**AI Studio 更新：**

- 在模型回覆中新增「喜歡」和「不喜歡」按鈕，讓使用者針對回覆品質提供意見。

**API 更新：**

- 新增 Google Cloud 抵免額支援，現在可用於支付 Gemini API 用量。

## 2024 年 9 月 17 日

**AI Studio 更新：**

- 新增「在 Colab 中開啟」按鈕，可將提示和執行提示的程式碼匯出至 Colab 筆記本。這項功能目前不支援使用工具提示 (JSON 模式、函式呼叫或程式碼執行)。

## 2024 年 9 月 13 日

**AI Studio 更新：**

- 新增比較模式支援功能，可比較不同模型和提示的回覆，找出最適合您用途的選項。

## 2024 年 8 月 30 日

**模型更新：**

- Gemini 1.5 Flash 支援[透過模型設定提供 JSON 結構定義](https://ai.google.dev/gemini-api/docs/json-mode?hl=zh-tw#supply-schema-in-config)。

## 2024 年 8 月 27 日

**模型更新：**

- 發布下列[實驗模型](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-tw)：
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 2024 年 8 月 9 日

**API 更新：**

- 新增 [PDF 處理](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)支援。

## 2024 年 8 月 5 日

**模型更新：**

- Gemini 1.5 Flash 支援微調功能。

## 2024 年 8 月 1 日

**模型更新：**

- 推出 `gemini-1.5-pro-exp-0801`，這是 [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-pro) 的全新實驗版本。

## 2024 年 7 月 12 日

**模型更新：**

- Google AI 服務和工具已移除對 Gemini 1.0 Pro Vision 的支援。

## 2024 年 6 月 27 日

**模型更新：**

- 正式發布 Gemini 1.5 Pro，支援 200 萬個詞元的脈絡窗口。

**API 更新：**

- 新增[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)支援功能。

## 2024 年 6 月 18 日

**API 更新：**

- 新增[內容快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)支援功能。

## 2024 年 6 月 12 日

**模型更新：**

- Gemini 1.0 Pro Vision 已淘汰。

## 2024 年 5 月 23 日

**模型更新：**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) 正式發布。
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) 現已正式發布 (GA)。

## 2024 年 5 月 14 日

**API 更新：**

- 推出 Gemini 1.5 Pro 的 200 萬個詞元脈絡窗口 (候補名單)。
- 推出 Gemini 1.0 Pro 的即付即用[帳單](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)，Gemini 1.5 Pro 和 Gemini 1.5 Flash 的帳單也即將推出。
- 即將推出的 Gemini 1.5 Pro 付費級別將提供更高的頻率限制。
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-tw) 新增內建影片支援。
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-tw) 新增純文字支援。
- 新增平行函式呼叫支援，一次傳回多個呼叫。

## 2024 年 5 月 10 日

**模型更新：**

- 發布 [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) 預先發布版。

## 2024 年 4 月 9 日

**模型更新：**

- 發布 [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-pro) (`gemini-1.5-pro-latest`) 預先發布版。
- 推出新的文字嵌入模型 `text-embeddings-004`，支援 768 以下的[彈性嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw#elastic-embedding)大小。

**API 更新：**

- 發布 [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-tw)，可暫時儲存媒體檔案，用於提示。
- 新增支援以文字、圖片和音訊資料提示，也就是*多模態*提示。詳情請參閱「[使用媒體提示](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=zh-tw)」。
- 發布「系統指令」的 Beta 版。
- 新增「函式呼叫模式」，定義函式呼叫的執行行為。
- 新增 `response_mime_type` 設定選項的支援功能，可讓您要求 [JSON 格式](https://ai.google.dev/gemini-api/docs/api-overview?hl=zh-tw#json)的回應。

## 2024 年 3 月 19 日

**模型更新：**

- 新增支援在 Google AI Studio 或使用 Gemini API [微調 Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)。

## 2023 年 12 月 13 日

**模型更新：**

- gemini-pro：適用於多種工作的新文字模型。兼顧功能和效率。
- gemini-pro-vision：適用於各種工作的新型多模態模型。
  兼具功能和效率。
- embedding-001：全新嵌入模型。
- aqa：經過特別調整的新模型，可根據文字段落回答問題，並以這些段落做為生成答案的依據。

詳情請參閱「[Gemini 模型](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw)」。

**API 版本更新：**

- v1：穩定版 API 通道。
- v1beta：Beta 版。這個頻道有部分功能可能仍在開發中。

詳情請參閱[這個 API 版本主題](https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-tw)。

**API 更新：**

- `GenerateContent` 是對話和文字的單一整合式端點。
- 可透過 `StreamGenerateContent` 方法串流播放。
- 多模態功能：圖片是新支援的模態
- Beta 版新功能：
  - [函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)
  - [語意擷取器](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=zh-tw)
  - 附出處的問答 (AQA)
- 更新候選項目數量：Gemini 模型只會傳回 1 個候選項目。
- 不同的安全設定和安全評等類別。詳情請參閱[安全設定](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-tw)。
- 目前尚不支援調整 Gemini 模型 (開發中)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-05 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-05 (世界標準時間)。"],[],[]]
