---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=zh-TW
fetched_at: 2026-08-03T04:31:19.573372+00:00
title: "\u4f7f\u7528\u4e2d API \u7684\u6700\u4f73\u505a\u6cd5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用中 API 的最佳做法

本指南將介紹最佳做法，協助您充分運用 Live API。如需常見用途的總覽和程式碼範例，請參閱「[開始使用 Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw)」頁面。

## 設計清楚的系統指令

如要充分發揮 Live API 的效能，建議您先明確定義一組系統指令 (SI)，依序定義代理程式角色、對話規則和防護措施。

為獲得最佳結果，請將每個代理程式分別歸入不同的 SI。

1. **指定代理程式角色：**詳細說明代理程式的名稱、角色和任何偏好特徵。如要指定口音，請務必同時指定偏好的輸出語言 (例如，為英文使用者指定英國口音)。
2. **指定對話規則：**請按照您希望模型遵循的順序，區分對話的一次性元素和對話迴圈。例如：

   - **一次性元素：**收集顧客詳細資料一次 (例如姓名、地點、會員卡號)。
   - **對話迴圈：**使用者可以討論建議、價格、退貨和運送事宜，並可能想從一個主題轉到另一個主題。讓模型知道只要使用者願意，就可以持續進行這類對話。
3. **在流程中以不同句子指定工具呼叫：**舉例來說，如果收集顧客詳細資料的一次性步驟需要叫用 `get_user_info` 函式，您可以說：「第一個步驟是收集使用者資訊。*首先，請使用者提供姓名、地點和會員卡號碼。然後使用這些詳細資料叫用 `get_user_info`。*
4. **新增任何必要的防護措施：**提供任何一般對話防護措施，避免模型做出您不希望的行為。您可以提供具體範例，說明如果發生 *x*，您希望模型執行 *y*。如果模型仍未達到您偏好的精確度，請使用「unmistakably」一詞引導模型提高精確度。

## 精確定義工具

使用 Live API 時，請明確定義工具。
請務必告訴 Gemini 應在何種情況下呼叫工具。詳情請參閱範例部分中的「[工具定義](#tool-definitions-example)」。

## 撰寫有效的提示

- **使用明確的提示：**在提示中提供模型應執行的動作和不應執行的動作範例，並盡量一次只為一個角色或職務提供提示。建議您改用提示鏈結，而非冗長的多頁提示。模型最適合處理單一函式呼叫的工作。
- **提供起始指令和資訊：**Live API 會先等待使用者輸入內容，再做出回應。如要讓 Live API 啟動對話，請加入提示，要求該 API 向使用者問候或開始對話。加入使用者資訊，讓 Live API 個人化問候語。

## 指定語言

如要讓 Live API 串聯 `gemini-live-2.5-flash` 達到最佳效能，請確保 API 的 `language_code` 與使用者說的語言相符。

如果希望模型以非英文回覆，請在系統指令中加入下列內容：

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## 串流

實作即時音訊時，請遵循下列最佳做法：

- **區塊大小和延遲時間**：以 20 毫秒到 40 毫秒的區塊傳送音訊。
- **中斷處理**：如果使用者在模型回覆時說話，伺服器會傳送含有 `"interrupted": true` 的 `server_content` 訊息。您必須立即捨棄用戶端音訊緩衝區，避免代理程式繼續與使用者交談。

## 管理資訊脈絡

如果工作階段較長，請使用 `ContextWindowCompressionConfig`，因為原生音訊符記會快速累積 (每秒音訊約 25 個符記)。

## 用戶端緩衝

請勿在傳送前大幅緩衝輸入音訊 (例如 1 秒)。傳送小區塊 (20 毫秒 - 100 毫秒)，盡量縮短延遲時間。

## 重新取樣

請確保用戶端應用程式會在傳輸前，將麥克風輸入內容 (通常為 44.1 kHz 或 48 kHz) 重新取樣為 16 kHz。

## 工作階段管理

請按照下列指南處理工作階段生命週期，確保使用者體驗穩定可靠：

- **啟用脈絡窗口壓縮功能：**音訊權杖的累積速度約為每秒 25 個權杖。如果沒有壓縮，純音訊工作階段最多只能進行 15 分鐘，音訊和視訊工作階段則為 2 分鐘。啟用[內容視窗壓縮](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-tw#context-window-compression)，即可將工作階段延長至無限時長。
- **實作工作階段續傳：**伺服器可能會定期重設 WebSocket 連線。使用[工作階段續傳](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-tw#session-resumption)功能，即可順暢地重新連線，不會遺失背景資訊。保留 `SessionResumptionUpdate` 訊息的最新續傳權杖，並在重新連線時將其做為控制代碼傳遞。工作階段終止後，續傳權杖的有效期限為 2 小時。
- **處理 GoAway 訊息：**伺服器會在終止連線前傳送 [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-tw#goaway-message) 訊息。請監聽這則訊息，並使用 `timeLeft` 欄位妥善結束或重新連線，以免連線中斷。
- **處理 generationComplete 信號：**使用 [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-tw#generation-complete-message) 訊息瞭解模型何時完成生成回覆，以便應用程式更新 UI 或繼續執行下一個動作。

如要瞭解實作方式，請參閱「[工作階段管理](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-tw)」。

## 範例

這個範例結合了最佳做法和[系統指令設計指南](#system-instruction-guidelines)，引導模型以職涯教練的身分提供建議。

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### 工具定義

這個 JSON 會定義職業教練範例中呼叫的相關函式。
定義函式時，請加入函式名稱、說明、參數和叫用條件，以獲得最佳結果。

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## 價格與計費

Gemini Live API 會嚴格按照權杖用量計費。由於 Live API 會維持持續的 WebSocket 工作階段，因此計費方式會根據有效內容視窗，採用複合式模型。

### 工作階段脈絡窗口 (複合成本)

API 會根據工作階段情境視窗中的所有符記，按輪次收費。「回合」是指使用者輸入內容和模型相應的回覆。

- **累積：**內容視窗包含目前回合的新詞元，以及先前回合累積的所有詞元。
- **重新計費：**系統會重新處理先前的權杖，並在每個新回合中計費，最多可達您設定的內容視窗大小。隨著工作階段時間拉長，系統會重新處理對話記錄，因此每回合的費用會增加。

### 音訊權杖和轉錄稿

Live API 本身就是多模態模型，這項功能會以原始音訊權杖的形式保留對話記錄，以保留聲學細微差異和語氣。

- **音訊費用：**API 會在每個回合中，以標準音訊輸入費率計算累積的原生音訊權杖費用。
- **轉錄附加費用：**啟用語音轉錄功能 (`inputAudioTranscription` 或 `outputAudioTranscription`) 後，除了標準音訊權杖費用外，API 還會按照文字權杖輸出費率，針對轉錄產生的所有文字權杖收費。

### 使用背景資訊限制管理費用

如要避免長時間工作階段的費用無上限成長，請使用 `contextWindowCompression` 設定內容視窗大小。

設定壓縮觸發條件 (例如 25,000 個權杖) 和滑動視窗 (例如 8,000 個權杖) 後，API 會在達到門檻時自動清除較舊的權杖。接著，API 只會針對保留的記錄加上任何新詞元，收取後續回合的費用。

### 主動式音訊模式

啟用主動式音訊模式後，只要 Live API 處於接聽狀態，系統就會持續收取輸入權杖費用，但只會在 API 回應時收取輸出權杖費用。

- **Gemini 3.1 注意事項：**`gemini-3.1-flash-live-preview` 不支援主動式音訊模式。採用這種模式時，只有在主動串流輸入內容時，系統才會收取音訊費用。

如需詳細定價資訊，請參閱 [Gemini API 定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-01 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-01 (世界標準時間)。"],[],[]]
