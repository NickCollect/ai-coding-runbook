---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=zh-TW
fetched_at: 2026-05-18T05:10:45.868430+00:00
title: "\u642d\u914d Gemini API \u4f7f\u7528\u5de5\u5177 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 搭配 Gemini API 使用工具

工具可擴展 Gemini 模型的能力，讓模型在現實世界中採取行動、存取即時資訊，以及執行複雜的運算工作。模型可以使用工具，透過標準要求/回應互動和 [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-tw) 進行即時串流工作階段。

工具是模型可用來回答查詢的特定功能 (例如 Google 搜尋或程式碼執行)。Gemini API 提供一整套全代管內建工具，您也可以使用[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)定義自訂工具。

如要建構多步驟、以目標為導向的系統，請參閱「[代理程式總覽](https://ai.google.dev/gemini-api/docs/agents?hl=zh-tw)」。

## 可用的內建工具

| 工具 | 說明 | 應用實例 |
| --- | --- | --- |
| [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw) | 根據網路上的時事和事實建立回覆基準，減少幻覺。 | \- 回答近期活動相關問題   \- 透過各種來源驗證事實 |
| [Google 地圖](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw) | 建構位置辨識助理，可尋找地點、規劃路線及提供豐富的當地資訊。 | - 規劃包含多個停靠點的旅遊行程   - 根據使用者條件尋找當地商家 |
| [程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw) | 允許模型撰寫及執行 Python 程式碼，準確解決數學問題或處理資料。 | - 解出複雜的數學方程式   - 精確處理及分析文字資料 |
| [網址環境](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw) | 指示模型讀取及分析特定網頁或文件中的內容。 | \- 根據特定網址或文件回答問題   \- 擷取不同網頁的資訊 |
| [電腦使用 (預覽)](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw) | 啟用 Gemini 來查看畫面，並生成與網路瀏覽器 UI 互動的動作 (用戶端執行作業)。 | \- 自動執行重複的網頁工作流程   \- 測試網頁應用程式使用者介面 |
| [檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw) | 為自有文件建立索引並進行搜尋，啟用檢索增強生成 (RAG) 功能。 | - 搜尋技術手冊   - 根據專有資料回答問題 |

如要瞭解特定工具的相關費用，請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#pricing_for_tools)。

## 工具執行的運作方式

模型可在對話期間透過工具要求執行動作。視工具是內建 (由 Google 管理) 還是自訂 (由您管理) 而定，流程會有所不同。

### 內建工具流程

如果是內建工具 (Google 搜尋、Google 地圖、網址內容、檔案搜尋、程式碼執行)，整個程序會在一次 API 呼叫中完成：

1. **你**傳送提示詞：「GOOG 最新股價的平方根是多少？」
2. **Gemini** 判斷需要工具，並在 Google 伺服器上執行這些工具 (例如搜尋股價，然後執行 Python 程式碼來計算平方根)。
3. **Gemini** 會根據工具結果傳回最終答案。

### 自訂工具流程 (函式呼叫)

如果是自訂工具和電腦使用，應用程式會處理執行作業：

1. **你**會連同函式 (工具) 宣告傳送提示。
2. **Gemini** 可能會傳回結構化 JSON，以呼叫特定函式 (例如 `{"name": "get_order_status", "args": {"order_id": "123"}}`)，且一律會附上專屬的 `id`。
3. **您**可以在應用程式或環境中執行函式。
4. 您將函式結果連同函式呼叫的相同 `id` 送回 Gemini。
5. **Gemini** 會根據結果生成最終回覆，或呼叫其他工具。

詳情請參閱[函式呼叫指南](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)。

### 結合內建和自訂工具流程

如果要求結合了內建工具和自訂工具 (函式呼叫)，模型會使用[工具情境循環](https://ai.google.dev/gemini-api/docs/toold-combination?hl=zh-tw)，協調不同環境的執行作業：

1. **您**可以傳送提示，並宣告要啟用的內建工具和自訂函式，然後設定旗標來啟用組合支援功能。
2. **Gemini** 會執行內建工具，並在產生任何用戶端函式呼叫時讓步 (執行順序取決於提示和模型判斷)。並傳回包含下列內容的回應：
   - 確認工具呼叫
   - 工具回應的結果 (如果模型生成兩個平行函式呼叫，這可能會出現在 JSON 之後)
   - 呼叫函式的結構化 JSON
   - 加密的思緒簽章，可保留情境
3. **您**可以在應用程式或環境中執行函式。
4. **你**會傳回 Gemini 回覆的所有部分，以及函式呼叫結果。
5. **Gemini** 會使用所有合併的脈絡資訊生成最終回覆。

請參閱[工具組合指南](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)，瞭解如何啟用內建和自訂工具組合的支援功能，以及內容循環的範例。

## 結構化輸出內容與函式呼叫

Gemini 提供兩種產生結構化輸出的方法。如果模型需要連線至您自己的工具或資料系統，執行中繼步驟，請使用[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)。如果模型最終回應必須嚴格遵守特定結構，例如用於算繪自訂 UI，請使用[結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)。

## 使用工具產生結構化輸出內容

您可以結合[結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)和內建工具，確保模型回覆內容以外部資料或運算結果為基準，但仍嚴格遵守結構定義。

如需程式碼範例，請參閱「[使用工具產生結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=zh-tw#structured_outputs_with_tools)」。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-04-29 (世界標準時間)。"],[],[]]
