---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=zh-TW
fetched_at: 2026-08-17T02:27:16.723683+00:00
title: "\u7591\u96e3\u6392\u89e3\u6307\u5357 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 疑難排解指南

本指南可協助您診斷及解決呼叫 Gemini API 時發生的常見問題。您可能會遇到 Gemini API 後端服務或用戶端 SDK 的問題。我們的用戶端 SDK 採用開放原始碼，位於下列存放區：

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

如果遇到 API 金鑰問題，請確認您已按照 [API 金鑰設定指南](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw)正確設定 API 金鑰。

## Gemini API 後端服務錯誤代碼

下表列出您可能會遇到的常見後端錯誤代碼，並說明原因和疑難排解步驟：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP 程式碼** | **狀態** | **說明** | **範例** | **解決方案** |
| 400 | INVALID\_ARGUMENT | 要求主體格式錯誤。 | 要求中有錯別字，或缺少必填欄位。 | 請參閱 [API 參考資料](https://ai.google.dev/api?hl=zh-tw)，瞭解要求格式、範例和支援的版本。如果使用較舊的端點，可能會發生錯誤。 |
| 400 | FAILED\_PRECONDITION | 你所在的國家/地區不支援 Gemini API 免費方案。請在 Google AI Studio 中為專案啟用帳單功能。 | 您在不支援免費層級的區域提出要求，且尚未在 Google AI Studio 中為專案啟用帳單資訊。 | 如要使用 Gemini API，請透過 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-tw) 設定付費方案。 |
| 403 | PERMISSION\_DENIED | 您的 API 金鑰沒有必要權限。 | 您使用的 API 金鑰有誤；您嘗試使用微調模型，但未經過[適當的驗證](https://ai.google.dev/gemini-api/docs/model-tuning?hl=zh-tw)。 | 確認 API 金鑰已設定且具有適當的存取權。請務必完成適當的驗證程序，才能使用微調模型。 |
| 404 | NOT\_FOUND | 找不到要求的資源。 | 系統找不到要求中參照的圖片、音訊或影片檔案。 | 確認要求中的所有[參數都適用於您的 API 版本](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=zh-tw#check-api)。 |
| 429 | RESOURCE\_EXHAUSTED | 您已超過其中一項 API 使用頻率限制 (RPM、TPM、RPD、支出等)。 | 您傳送的要求過多、使用的權杖過多，或是超出帳戶帳單記錄和層級的支出上限。 | 確認您未超出模型的[速率限制](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-tw)。請稍候片刻再重試。降低要求速率或縮減要求大小。如有需要，請[要求提高速率限制](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-tw#request-rate-limit-increase)。 |
| 499 | 已取消 | 作業已取消 (通常由呼叫端取消)。 | API 尚未完成回應，用戶端就已關閉連線。 | 檢查用戶端或網路基礎架構是否過早關閉連線 (例如因用戶端逾時)。 |
| 500 | 內部資源 | Google 發生未預期的錯誤。 | 輸入內容過長。 | 查看 [Gemini API 狀態頁面](https://aistudio.google.com/status?hl=zh-tw)，瞭解是否有任何進行中的事件。縮減輸入內容的脈絡，或暫時改用其他模型 (例如從 Gemini 2.5 Pro 改用 Gemini 2.5 Flash)，看看是否能解決問題。或者稍後再試一次。如果重試後問題仍未解決，請使用 Google AI Studio 的「提供意見」按鈕回報。 |
| 503 | 無法使用 | 該服務可能暫時超載或關閉。 | 這項服務的容量暫時不足。 | 查看 [Gemini API 狀態頁面](https://aistudio.google.com/status?hl=zh-tw)，瞭解是否有任何進行中的事件。暫時切換至其他模型 (例如從 Gemini 2.5 Pro 切換至 Gemini 2.5 Flash)，看看是否能正常運作。或者稍後再試一次。如果重試後問題仍未解決，請使用 Google AI Studio 的「提供意見」按鈕回報。 |
| 504 | DEADLINE\_EXCEEDED | 服務無法在期限內完成處理。 | 提示 (或情境) 過大，無法及時處理。 | 在用戶端要求中設定較大的「逾時」，即可避免這個錯誤。 |

## 重試策略

如果收到錯誤訊息，指出您應重試要求 (例如 `429 RESOURCE_EXHAUSTED` 或 `503 UNAVAILABLE`)，建議您採用指數輪詢策略。也就是說，第一次重試前會等待一小段時間，然後逐漸延長後續重試之間的等待時間。

Gemini API 的官方用戶端 SDK (例如 [Python SDK](https://github.com/googleapis/python-genai)) 預設會包含自動重試邏輯，並採用指數輪詢間隔，處理逾時、網路問題和速率限制等暫時性錯誤 (`429` 和 `5xx` 狀態碼)。舉例來說，Python SDK 會自動重試暫時性錯誤，最多重試四次，初始延遲時間約為 1 秒，最長延遲時間為 60 秒。

如果您直接發出 REST API 要求或自訂重試邏輯，請遵循下列最佳做法，提高要求成功的可能性，並避免服務負載過重：

- **使用指數輪詢：**第一次重試前先等待一小段時間 (例如 1 秒)，然後以指數方式增加延遲時間 (例如 2 秒、4 秒、8 秒)。
- **加入時基誤差：**在延遲時間中加入隨機「時基誤差」，避免所有用戶端在完全相同的時間重試。
- **針對特定錯誤重試：**僅針對暫時性錯誤 (例如 `429`、`408` 或 `5xx`) 重試。請勿針對用戶端錯誤 (例如 `400` 或 `403`) 重試，因為這類錯誤表示 API 金鑰無效或語法錯誤等問題。
- **設定重試次數上限：**定義重試次數上限，避免無限迴圈。

## 檢查 API 呼叫是否有模型參數錯誤

確認模型參數符合下列值：

|  |  |
| --- | --- |
| **模型參數** | **值 (範圍)** |
| 候選人數 | 1 到 8 (整數) |
| 溫度 | 0.0 到 1.0 |
| 輸出詞元數量上限 | 請前往[模型頁面](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw)，瞭解所用模型的詞元數量上限。 |
| TopP | 0.0 到 1.0 |

除了檢查參數值，請務必使用正確的 [API 版本](https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-tw) (例如 `/v1` 或 `/v1beta`)，以及支援所需功能的模型。舉例來說，如果某項功能為 Beta 版，則僅適用於 `/v1beta` API 版本。

## 確認你是否使用正確的機型

確認您使用的是[模型頁面](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw)上列出的支援模型。

## 使用 2.5 模型時延遲時間較長或詞元用量較高

如果使用 2.5 Flash 和 Pro 模型時，發現延遲時間較長或權杖用量較高，可能是因為這些模型**預設啟用思考功能**，以提升品質。如果想加快速度或盡量降低成本，可以調整或停用思考功能。

如需指引和程式碼範例，請參閱[思考頁面](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw#set-budget)。

## 安全問題

如果系統顯示提示遭到封鎖，是因為 API 呼叫中的安全設定，請根據您在 API 呼叫中設定的篩選器檢查提示。

如果看到 `BlockedReason.OTHER`，表示查詢或回覆可能違反《[服務條款](https://ai.google.dev/terms?hl=zh-tw)》或不支援。

## 背誦問題

如果模型因「RECITATION」原因停止生成輸出內容，表示模型輸出內容可能與特定資料相似。如要修正這個問題，請盡量讓提示 / 背景資訊獨一無二，並使用較高的溫度。

## 重複權杖問題

如果看到重複的輸出權杖，請嘗試下列建議，減少或消除這些權杖。

| 說明 | 原因 | 建議的解決方法 |
| --- | --- | --- |
| Markdown 表格中重複的連字號 | 如果資料表內容很長，模型會嘗試建立視覺上對齊的 Markdown 資料表，不過，Markdown 中的對齊方式並非正確算繪的必要條件。 | 在提示中加入指令，為模型提供生成 Markdown 表格的具體規範。請提供符合這些規範的範例。你也可以嘗試調整溫度。如要生成程式碼或 Markdown 表格等結構化輸出內容，高溫 (>= 0.8) 的效果較好。  以下是您可以新增至提示的範例規範，避免發生這種情況：     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Markdown 表格中的重複權杖 | 與重複的連字號類似，這是因為模型嘗試在視覺上對齊表格內容。Markdown 中的對齊方式不影響正確的轉譯結果。 | - 試著在系統提示中加入下列指令：      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - 請嘗試調整溫度。溫度越高 (>= 0.8)，輸出內容就越不會重複。 |
| 結構化輸出內容中重複出現換行符 (`\n`) | 如果模型輸入內容包含 Unicode 或逸出序列 (例如 `\u` 或 `\t`)，可能會導致重複換行。 | - 檢查提示中是否有禁止使用的逸出序列，並以 UTF-8 字元取代。舉例來說，JSON 範例中的 `\u`   逸出序列可能會導致模型在輸出內容中也使用這些序列。 - 指示模型可接受的逸出字元。新增類似這樣的系統指令：      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| 使用結構化輸出內容時重複的文字 | 如果模型輸出內容的欄位順序與定義的結構化結構定義不同，可能會導致文字重複。 | - 請勿在提示中指定欄位順序。 - 將所有輸出欄位設為必填。 |
| 重複呼叫工具 | 如果模型失去先前想法的脈絡，且/或呼叫無法使用的端點，就可能發生這種情況。 | 引導模型在思考過程中維持狀態。 在系統指令結尾新增下列內容：    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| 重複的文字，不屬於結構化輸出內容 | 如果模型無法解決要求，就可能會發生這種情況。 | - 如果開啟思考功能，請避免在指令中明確指示如何思考問題。只要要求最終輸出內容即可。 - 請嘗試將溫度調高至 0.8 以上。 - 新增「簡潔扼要」、「不要重複」或「只提供一次答案」等指令。 |

## 遭封鎖或無法使用的 API 金鑰

本節說明如何檢查 Gemini API 金鑰是否遭到封鎖，以及如何解決這個問題。

### 瞭解金鑰遭到封鎖的原因

我們發現部分 API 金鑰可能遭到公開，為保護您的資料並防止未經授權的存取行為，我們已主動封鎖這些已知的洩漏金鑰，避免存取 Gemini API。

### 確認金鑰是否受影響

如果金鑰外洩，您就無法再透過該金鑰使用 Gemini API。您可以使用 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-tw)，查看是否有任何 API 金鑰遭到封鎖，無法呼叫 Gemini API，並產生新的金鑰。嘗試使用這些金鑰時，也可能會看到下列錯誤訊息：

```
Your API key was reported as leaked. Please use another API key.
```

### 遭封鎖 API 金鑰的動作

請使用 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-tw)，為 Gemini API 整合項目產生新的 API 金鑰。我們強烈建議您檢查 API 金鑰管理做法，確保新金鑰安全無虞，且不會公開。

### 因安全漏洞而產生意外費用

[提交帳單客服案件](https://console.cloud.google.com/support/chat?hl=zh-tw)。
我們的帳單團隊正在處理這項問題，一有最新消息就會盡快通知您。

### Google 針對外洩金鑰採取的安全措施

**如果我的 API 金鑰外洩，Google 會如何協助保護帳戶，避免費用超出預算和遭到濫用？**

- 我們將逐步調整，日後透過 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-tw) 申請新金鑰時，系統預設只會發放 Google AI Studio 專用的 API 金鑰，不會接受其他服務的金鑰。這有助於防止任何非預期的跨金鑰使用情況。
- 我們預設會封鎖遭洩漏並搭配 Gemini API 使用的 API 金鑰，協助您避免費用遭到濫用，以及保護應用程式資料。
- 您可以在 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-tw) 中查看 API 金鑰的狀態。如果我們發現您的 API 金鑰外洩，會主動通知您立即採取行動。

## 提升模型輸出內容品質

如要取得更高品質的模型輸出內容，請嘗試撰寫結構更完整的提示。「[提示工程指南](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw)」頁面介紹了一些基本概念、策略和最佳做法，協助您入門。

## 瞭解權杖限制

詳閱[權杖指南](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw)，進一步瞭解如何計算權杖和權杖限制。

## 已知問題

- 這項 API 僅支援部分語言。如果以不支援的語言提交提示，可能會生成非預期的回覆，甚至遭到封鎖。如需最新資訊，請參閱[支援的語言](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#supported-languages)。

## 回報錯誤

如有任何問題，歡迎前往 [Google AI 開發人員論壇](https://discuss.ai.google.dev?hl=zh-tw)參與討論。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-08 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-08 (世界標準時間)。"],[],[]]
