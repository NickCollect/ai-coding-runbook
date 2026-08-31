---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=zh-TW
fetched_at: 2026-08-31T06:32:58.953491+00:00
title: "Gemini Robotics ER 2 \u4e32\u6d41 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini Robotics ER 2 串流

Gemini Robotics ER 2 Streaming 是適用於機器人的視覺語言模型 (VLM)，可透過 Live API 即時串流文字。可接受文字、圖片、影片和音訊輸入內容，並支援雙向串流和函式呼叫。

[在 Google AI Studio 中試用](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=zh-tw)

## 說明文件

如要全面瞭解功能，請前往 [Live API for robotics](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw) 頁面。

## gemini-robotics-er-2-streaming-preview

### Gemini Robotics ER 2 預先發布版

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | `gemini-robotics-er-2-preview` |
| save支援的資料類型 | **輸入裝置**  文字、圖片、影片、音訊  **輸出內容**  文字 |
| token\_auto 代幣限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw) | **輸入權杖限制**  131,072  **輸出詞元限制**  65,536 |
| handyman功能 | **[生成音訊](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)**  不支援  **[快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)**  支援  **[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)**  支援  **[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)**  支援  **[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)**  支援  **[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)**  支援  **[利用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)**  支援  **[圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)**  不支援  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw)**  不支援  **[以搜尋為基準](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)**  支援  **[結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)**  支援  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)**  支援  **[網址內容](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)**  支援 |
| speed用量方案 | **[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)**  支援  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)**  不支援  **[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)**  不支援 |
| 123 個版本 | 詳閱[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#model-versions)。  - 預覽：`gemini-robotics-er-2-preview` |
| calendar\_month最新更新 | 2026 年 7 月 |
| id\_card模型資訊卡 | [模型資訊卡](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=zh-tw) |

### Gemini Robotics ER 2 Streaming Preview

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | `gemini-robotics-er-2-streaming-preview` |
| save支援的資料類型 | **輸入裝置**  文字、圖片、影片、音訊  **輸出內容**  文字 |
| token\_auto 代幣限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw) | **輸入權杖限制**  131,072  **輸出詞元限制**  65,536 |
| handyman功能 | **[生成音訊](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)**  不支援  **[快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)**  不支援  **[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)**  不支援  **[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)**  不支援  **[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)**  不支援  **[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)**  支援  **[利用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)**  不支援  **[圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)**  不支援  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw)**  支援  **[以搜尋為基準](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)**  支援  **[結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)**  不支援  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)**  支援  **[網址內容](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)**  不支援 |
| speed用量方案 | **[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)**  不支援  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)**  不支援  **[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)**  不支援 |
| 123 個版本 | 詳閱[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#model-versions)。  - 預覽：`gemini-robotics-er-2-streaming-preview` |
| calendar\_month最新更新 | 2026 年 7 月 |
| id\_card模型資訊卡 | [模型資訊卡](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=zh-tw) |

### Gemini Robotics ER 1.6 預先發布版

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | `gemini-robotics-er-1.6-preview` |
| save支援的資料類型 | **輸入裝置**  文字、圖片、影片、音訊  **輸出內容**  文字 |
| token\_auto 代幣限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw) | **輸入權杖限制**  131,072  **輸出詞元限制**  65,536 |
| handyman功能 | **[生成音訊](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)**  不支援  **[快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)**  支援  **[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)**  支援  **[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)**  支援  **[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)**  支援  **[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)**  支援  **[利用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)**  支援  **[圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)**  不支援  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw)**  不支援  **[以搜尋為基準](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)**  支援  **[結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)**  支援  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)**  支援  **[網址內容](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)**  支援 |
| speed用量方案 | **[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)**  支援  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)**  不支援  **[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)**  不支援 |
| 123 個版本 | 詳閱[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#model-versions)。  - 預覽：`gemini-robotics-er-1.6-preview` |
| calendar\_month最新更新 | 2025 年 12 月 |
| cognition\_2知識截點 | 2025 年 1 月 |

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-08-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-08-19 (世界標準時間)。"],[],[]]
