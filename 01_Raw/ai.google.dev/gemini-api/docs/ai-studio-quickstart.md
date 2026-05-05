---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=zh-TW
fetched_at: 2026-05-05T20:06:34.477922+00:00
title: "Google AI Studio \u5feb\u901f\u5165\u9580\u5c0e\u89bd\u8ab2\u7a0b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Google AI Studio 快速入門導覽課程

[Google AI Studio](https://aistudio.google.com/?hl=zh-tw) 可讓您快速試用模型，以及測試不同提示。準備好建構應用程式後，您可以選取「取得程式碼」和偏好的程式設計語言，使用 [Gemini API](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-tw)。

## 提示和設定

Google AI Studio 提供多種提示介面，適用於不同用途。本指南涵蓋**對話提示**，可用於建構對話式體驗。這項提示技巧可進行多輪輸入和回覆，以生成輸出內容。如要瞭解詳情，請參閱[下方的聊天提示範例](#chat_example)。
其他選項包括「即時串流」、「影片生成」等。

AI Studio 也提供「執行設定」面板，可供調整[模型參數](https://ai.google.dev/docs/prompting-strategies?hl=zh-tw#model-parameters)、[安全設定](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-tw)，以及開啟「結構化輸出」、「函式呼叫」、「程式碼執行」和「建立基準」等工具。

## 聊天提示範例：建構自訂聊天應用程式

如果您使用過 [Gemini](https://gemini.google.com/?hl=zh-tw) 等一般用途聊天機器人，應該親身體驗過生成式 AI 模型在開放式對話中的強大功能。雖然這些一般用途聊天機器人很有用，但通常需要針對特定用途進行調整。

舉例來說，您可能想建立客戶服務聊天機器人，但只支援與公司產品相關的對話。你可能想建立的聊天機器人會使用特定語氣或風格說話，例如：愛開玩笑、像詩人一樣押韻，或在回覆中大量使用表情符號。

這個範例說明如何使用 Google AI Studio 建構友善的聊天機器人，並模擬居住在木星衛星歐羅巴的外星人進行對話。

### 步驟 1 - 建立聊天提示

如要建構聊天機器人，您需要提供使用者與聊天機器人互動的範例，引導模型提供您要的回覆。

如何建立聊天提示：

1. 開啟 [Google AI Studio](https://aistudio.google.com/?hl=zh-tw)。左側的選項選單會預先選取「Chat」。
2. 按一下「對話提示」視窗頂端的 assignment 圖示，展開「系統指令」輸入欄位。將下列內容貼到文字輸入欄位：

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

新增系統指令後，即可與模型對話，開始測試應用程式：

1. 在標示為「Type something...」(輸入內容...) 的文字輸入方塊中，輸入使用者可能會提出的問題或觀察結果。例如：

   **使用者：**

   ```
   What's the weather like?
   ```
2. 按一下「執行」按鈕，即可取得聊天機器人的回覆。這項回應可能類似如下：

   **型號：**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### 步驟 2 - 訓練機器人進行更流暢的對話

您只需提供單一指令，就能建立基本的 Europa 外星人聊天機器人。不過，單一指令可能不足以確保模型回覆的一致性和品質。如果沒有更具體的指示，模型回覆天氣問題時往往會長篇大論，甚至會自行發揮。

在系統指令中加入以下內容，自訂聊天機器人的語氣：

1. 發起新的對話提示，或使用相同提示。即時通訊工作階段開始後，系統指令仍可修改。
2. 在「系統指令」部分，將現有的指令變更為下列內容：

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. 重新輸入問題 (`What's the weather like?`)，然後按一下「執行」按鈕。如果沒有發起新對話，回覆可能大致如下：

   **型號：**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

您可以運用這種方式，讓聊天機器人更深入瞭解主題。提出更多問題、編輯答案，並提升聊天機器人的品質。繼續新增或修改指令，並測試這些指令如何改變聊天機器人的行為。

### 步驟 3 - 後續步驟

與其他提示類型類似，當您對提示原型感到滿意時，即可使用「取得程式碼」按鈕開始編碼，或儲存提示以供日後使用及與他人分享。

## 延伸閱讀

- 如要開始編寫程式碼，請參閱 [API 快速入門指南](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-tw)。
- 如要瞭解如何編寫更優質的提示，請參閱[提示設計指南](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-04-29 (世界標準時間)。"],[],[]]
