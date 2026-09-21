---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-TW
fetched_at: 2026-09-21T05:51:08.155026+00:00
title: "\u63d0\u793a\u8a2d\u8a08\u7b56\u7565 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 提示設計策略

*提示設計*是指建立提示或自然語言要求的程序，目的是讓語言模型提供準確、高品質的回覆。

本頁面將介紹基本概念、策略和最佳做法，協助您開始設計提示，充分發揮 Gemini AI 模型的效用。

## 主題專屬提示指南

想瞭解更多具體的提示策略嗎？歡迎參閱其他提示詞指南，瞭解如何：

- [使用媒體檔案提示](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw#prompt-guide)
- [圖像生成提示](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw#prompt-guide)
- [提示生成影片](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#prompt-guide)

如要查看其他提示範例，請前往[提示範例庫](https://ai.google.dev/gemini-api/prompts?hl=zh-tw)，以互動方式瞭解本指南中分享的許多概念。

## 清楚明確的指令

如要有效率地自訂模型行為，請提供清楚明確的指令。指令可以是問題、逐步完成的任務，也可以是複雜的指令，例如繪製使用者體驗和思維模式。

### 輸入

輸入內容是提示中必須提供的文字，模型會根據這些文字生成回覆。輸入內容可以是模型回答的問題 (問題型輸入內容)、模型執行的工作 (工作型輸入內容)、模型操作的實體 (實體型輸入內容)，或是模型補完或繼續編寫的不完整輸入內容 (補完型輸入內容)。

| **輸入類型** | **提示** | **生成內容** |
| --- | --- | --- |
| Question | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| 工作 | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| 實體 | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### 部分輸入完成

生成式語言模型就像進階的自動完成工具，當您提供部分內容，模型就能補足其餘的部分，或提供模型認為是該內容的延續部分做為回覆。如果提供範例或脈絡資訊，模型就會將這些資訊納入考量。

以下範例提供含有指令和實體輸入內容的提示：

|  |
| --- |
| **提示：**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **回覆：**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

雖然模型已按照提示執行，但以自然語言撰寫指令有時可能很困難，而且模型會根據自己的解讀執行指令。舉例來說，餐廳菜單可能包含許多項目。如要縮減 JSON 回應的大小，您可能想省略未訂購的項目。在這種情況下，您可以提供範例和回覆前置字串，讓模型完成後續內容：

|  |
| --- |
| **提示：**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **回覆：**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

請注意，輸出內容中不包含「起司漢堡」，因為這不是訂單的一部分。

雖然您可以使用提示指定簡單 JSON 回覆物件的格式，但我們建議您使用 Gemini API 的[結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)功能，為回覆指定更複雜的 JSON 結構定義。

### 限制

指定讀取提示或生成回覆的任何限制。您可以告知模型該做什麼和不該做什麼。舉例來說，您可以在提示中指定摘要長度限制：

|  |
| --- |
| **提示：**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **回覆：**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### 回覆格式

你可以下指令，指定回覆格式。舉例來說，你可以要求回覆內容採用表格、項目符號清單、電梯簡報、關鍵字、句子或段落格式。下列系統指令會要求模型以對話口吻回覆：

|  |
| --- |
| **系統指令**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **提示**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **回覆：**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### 使用完成策略設定回覆格式

[完成策略](#completion)也有助於設定回覆格式。
以下範例會提示模型建立文章大綱：

|  |
| --- |
| **提示：**    ``` Create an outline for an essay about hummingbirds. ```  **回覆：**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

提示未指定大綱格式，因此模型為您選擇了格式。如要讓模型以特定格式傳回大綱，可以加入代表大綱開頭的文字，讓模型根據您啟動的模式完成大綱。

|  |
| --- |
| **提示：**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **回覆：**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## 零樣本提示與少量樣本提示

您可以在提示中加入範例，說明正確答案的樣貌。模型會嘗試從範例中找出模式和關係，並在生成回覆時套用這些模式和關係。含有少量範例的提示稱為「少量樣本」提示，而未提供範例的提示則稱為「零樣本」提示。Few-shot 提示通常用於控管模型回覆的格式、措辭、範圍或一般模式。使用具體且多樣化的示例協助模型縮小範圍，生成更準確的結果。

建議您一律在提示中加入少量樣本範例。如果提示沒有少量樣本，效果可能較差。事實上，如果範例已清楚說明手邊的工作，您可以從提示中移除指令。

下列零樣本提示會要求模型選擇最佳說明。

|  |
| --- |
| **提示：**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **回覆：**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

如果您的用途需要模型產生簡潔的回覆，可以在提示中加入偏好簡潔回覆的範例。

以下提示提供兩個範例，說明偏好較短的說明。在回覆中，您可以看到範例引導模型選擇較短的說明 (`Explanation2`)，而非像先前一樣選擇較長的說明 (`Explanation1`)。

|  |
| --- |
| **提示：**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **回覆：**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### 最佳範例數量

Gemini 等模型通常可以從幾個範例中找出模式，但您可能需要嘗試在提示中提供不同數量的範例，才能獲得最佳結果。但如果提供太多範例，模型可能會開始[過度配適](https://developers.google.com/machine-learning/glossary?hl=zh-tw#overfitting)範例的回覆。

### 格式一致

請確保少量樣本的結構和格式相同，以免回應的格式不符預期。在提示中加入少量樣本的主要目標之一，是向模型展示回覆格式。因此，請務必確保所有範例的格式一致，特別是 XML 標記、空白字元、換行符號和範例分隔符號。

## 新增情境

您可以在提示中加入模型解決問題所需的指示和資訊，而非假設模型包含所有必要資訊。這類脈絡資訊可協助模型瞭解限制，以及您要求模型執行的詳細內容。

以下範例要求模型提供路由器疑難排解指南：

|  |
| --- |
| **提示：**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **回覆：**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

回覆內容看起來是通用的疑難排解資訊，與路由器或 LED 指示燈的狀態無關。

如要自訂特定路由器的回覆，可以在提示中加入路由器的疑難排解指南，做為模型提供回覆時的參考情境。

|  |
| --- |
| **提示：**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **回覆：**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## 將提示拆解為多個部分

如果應用情境需要複雜提示，您可以將提示拆解成簡單的組成部分，協助模型管理這類複雜性。

1. **將指令細分成多個提示：**不要在一個提示中加入多個指令，而是為每個指令建立一個提示。您可以根據使用者的輸入內容，選擇要處理的提示。
2. **串連提示：**如要處理涉及多個連續步驟的複雜工作，請將每個步驟變成一個提示，並將提示串連在一起。在這個提示的連續鏈結中，序列中一個提示的輸出內容會成為下一個提示的輸入內容。序列中最後一個提示的輸出內容就是最終輸出內容。
3. **匯總回應：**匯總是指您想對資料的不同部分執行不同的平行工作，並匯總結果以產生最終輸出內容。舉例來說，您可以指示模型對資料的第一部分執行一項作業，對其餘資料執行另一項作業，然後彙整結果。

## 嘗試各種模型參數

您傳送至模型的每個呼叫都含有參數值，用來控制模型生成回覆的方式，參數值不同，生成的結果也可能會不同。實驗不同參數值，取得最適合工作目標的結果。不同模型可用的參數不盡相同。最常見的參數如下：

1. **輸出詞元數量上限：**指定回覆中可生成的詞元數量上限。一個符記約為四個字元，100 個符記約為 60 到 80 個字。
2. **溫度：**溫度參數會決定選取詞元時的隨機程度。生成回覆時會使用溫度參數進行取樣，這發生在套用 `topP` 和 `topK` 時。如果您想藉由提示生成更具確定性、較不具開放性的回覆，建議調低溫度參數。另一方面，如果溫度參數較高，則可能產生較多元或有創意的結果。溫度為 0 代表具有確定性，即模型一律會選取可能性最高的回覆。
3. **`topK`：**`topK` 參數會影響模型選取輸出詞元的方式。如果 `topK` 設為 1，代表所選詞元是模型詞彙表所有詞元中可能性最高者 (也稱為「貪婪解碼」)。如果 `topK` 設為 3，則代表模型會依據溫度參數，從可能性最高的 3 個詞元中選取下一個詞元。在每個符記選取步驟中，模型會對機率最高的「Top-K」`topK`符記取樣，接著進一步根據 `topP` 篩選詞元，最後依 temperature 選出最終詞元。
4. **`topP`：**`topP` 參數會影響模型選取輸出詞元的方式。模型會按照可能性最高到最低的順序選取詞元，直到所選詞元的可能性總和等於 `topP` 值。舉例來說，假設詞元 A、B 和 C 的可能性分別為 0.3、0.2 和 0.1，而 `topP` 值為 0.5，模型會依據 temperature 選擇 A 或 B 做為下一個詞元，並排除 C。預設 `topP` 值為 0.95。
5. **`stop_sequences`：**設定停止序列，告知模型停止生成內容。停止序列可以是任何字元序列。請盡量避免使用可能會出現在生成內容中的字元序列。

## 反覆修正提示詞的策略

有時需要經過幾次疊代，才能獲得想要的提示設計，並持續獲得所需的回應。本節提供一些指引，說明在疊代提示時可以嘗試哪些做法：

1. **使用不同措辭：**即使提示的意義相同，使用不同字詞或措辭，模型通常也會產生不同的回覆。如果提示未產生預期結果，請嘗試重新措辭。

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **改用類似工作：**如果模型無法按照工作指令執行，請嘗試提供類似工作的指令，以達到相同結果。

   這個提示會指示模型使用預先定義的類別，將書籍分類：

   |  |
   | --- |
   | **提示：**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **回覆：**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   答案正確，但模型未遵守選項範圍。您也希望模型只回覆其中一個選項，而不是完整的句子。在這種情況下，您可以將指令改寫為選擇題，並要求模型選擇選項。

   |  |
   | --- |
   | **提示：**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **回覆：**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **變更提示內容的順序：**提示中的內容順序有時會影響回覆結果，因此不妨嘗試變更內容順序，看看回覆會有什麼變化。

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## 備用回覆

如果提示或回覆觸發安全篩選器，模型就會傳回備用回覆。例如：「我只能提供語言模型服務，無法協助處理這項要求。」

如果模型提供備用回覆，請嘗試調高溫度參數。

## 建立基準和執行程式碼

在可能產生不正確回覆的情況下，Gemini 會使用工具避免出現幻覺。

[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)可讓 Gemini 模型取得即時網路內容。如果模型可能需要瞭解冷門或近期事實，請務必啟用這項功能。

Gemini 的[執行程式碼工具](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)可讓模型生成及執行 Python 程式碼，因此模型需要執行任何算術、計數或計算時，都應啟用這項工具。

## Gemini 3

[Gemini 3 模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-3)專為進階推論和指令遵循而設計。提示詞越直接、結構越完整，且清楚定義工作和任何限制，模型的回覆效果就越好。為獲得最佳 Gemini 3 結果，建議採取下列做法：

### 核心提示原則

- **明確且直接：**清楚簡潔地說明目標。避免使用不必要的語言或過於強烈的說服性語言。
- **使用一致的結構：**使用明確的分隔符號分隔提示的不同部分。XML 樣式的標記 (例如 `<context>`、`<task>`) 或 Markdown 標題都很有效。選擇一種格式，並在單一提示中保持一致。
- **定義參數：**明確說明任何模稜兩可的字詞或參數。
- **控制輸出內容的詳細程度：**Gemini 3 模型預設會提供直接且有效率的答案。如需更自然流暢或詳細的回覆，請在指令中明確要求。
- **一致處理多模態輸入內容：**使用文字、圖片、音訊或影片時，請將這些內容視為同類輸入內容。請確保說明清楚提及各個模式。
- **優先提供重要指令：**將必要的行為限制、角色定義 (角色) 和輸出格式要求放在系統指令中，或使用者提示的開頭。
- **長篇脈絡資料的結構：**提供大量脈絡資料 (例如文件、程式碼) 時，請先提供所有脈絡資料。將具體指示或問題放在提示的*最後*。
- **錨定情境：**在大量資料後，使用清楚的轉場片語來連結情境和查詢，例如「根據上述資訊...」。

### Gemini 3 Flash 策略

- **當天準確度：**在系統指令中加入下列子句，協助模型注意當天是 2026 年：

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **知識截點準確率：**在系統指令中加入下列子句，讓模型瞭解知識截點：

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **建立基準成效：**在系統指令中加入下列子句 (視需要編輯)，提升模型根據所提供脈絡資訊建立回覆基準的能力：

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### 提升推論和規劃能力

Gemini 2.5 和 3 系列模型會自動生成內部「思考」文字，以提升推論效能。因此，模型通常不需要在回覆內容中列出大綱、規劃或詳細說明推論步驟。對於需要大量推論的問題，簡單的要求 (例如「請先仔細思考再回答」) 就能提升效能，但會耗用額外的思考詞元。

詳情請參閱 [Gemini 思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)說明文件。

### 結構化提示範例

使用標記或 Markdown 有助於模型區分指令、情境和工作。

**XML 範例：**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Markdown 範例：**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### 結合最佳做法的範本範例

這個範本涵蓋 Gemini 3 提示的核心原則。請務必根據特定用途進行疊代和修改。

**系統操作說明：**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**使用者提示：**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## 代理工作流程

對於深入的代理工作流程，通常需要特定指令來控管模型如何推論、規劃及執行工作。雖然 Gemini 的一般效能很強大，但複雜的代理通常需要您在運算成本 (延遲時間和詞元) 與任務準確率之間取得平衡。

為代理程式設計提示時，請考量以下可引導代理程式的行為面向：

### 推論與策略

模型採取行動前思考和規劃的方式設定。

- **邏輯分解：**定義模型必須分析限制、先決條件和作業順序的詳盡程度。
- **問題診斷**：控管找出原因時的分析深度，以及模型使用溯因推論的程度。決定模型應接受最明顯的答案，還是探索複雜且可能性較低的解釋。
- **資訊詳盡程度：**分析所有可用政策和文件，與優先考量效率和速度之間的取捨。

### 執行和可靠性

代理程式自主運作和處理障礙的設定。

- **適應性：**模型對新資料的反應。決定是否應嚴格遵守初始計畫，或在觀察結果與假設相矛盾時立即調整。
- **持續性和復原：**模型嘗試自行修正錯誤的程度。高持續性可提高成功率，但代幣成本或迴圈風險也會隨之增加。
- **風險評估：**評估後果的邏輯。明確區分低風險的探索性動作 (讀取) 和高風險的狀態變更 (寫入)。

### 互動和輸出

代理程式與使用者通訊及格式化結果的方式設定。

- **模糊不清和權限處理：**定義模型何時可進行假設，以及何時必須暫停執行，要求使用者提供說明或權限。
- **詳細程度：**控制工具呼叫時產生的文字量。這項設定會決定模型是否向使用者說明其動作，或是在執行期間保持沉默。
- **精確度和完整度：**輸出內容的必要精確度。指定模型是否必須解決所有極端情況並提供確切數字，或可接受概略估算。

### 系統指令範本

以下系統指令範例已由研究人員評估，可提升代理程式基準的效能，模型必須遵守複雜的規則手冊並與使用者互動。這會促使代理成為強大的推理和規劃者，在上述各個層面強制執行特定行為，並要求模型在採取任何行動前主動規劃。

您可以根據特定用途限制調整這個範本。

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## 後續步驟

- 現在您已深入瞭解提示設計，不妨使用 [Google AI Studio](http://aistudio.google.com?hl=zh-tw) 撰寫自己的提示。
- 如要瞭解多模態提示，請參閱「[使用媒體檔案撰寫提示](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw#prompt-guide)」。
- 如要瞭解圖片提示詞，請參閱 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw#prompt-guide) 提示詞指南。
- 如要瞭解影片提示詞，請參閱 [Veo 提示詞指南](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#prompt-guide)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-18 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-18 (世界標準時間)。"],[],[]]
