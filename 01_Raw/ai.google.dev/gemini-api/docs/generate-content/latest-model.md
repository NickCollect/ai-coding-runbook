---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=zh-TW
fetched_at: 2026-10-26T06:01:13.156486+00:00
title: "Gemini 4 Argon \u65b0\u529f\u80fd \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

提供意見

# Gemini 4 Argon 新功能

Gemini 4 Argon (`gemini-4-argon`) 是 Google 最新、最強大的模型，能花更多時間推論困難問題，在複雜的程式設計、代理、數學和科學任務中，提供更優質的結果。Gemini 4 Argon 可透過 Gemini API 和 Google AI Studio 使用。

Gemini 4 Argon 支援統一的 100 萬輸入/輸出詞元限制、長解碼 (最多 100 萬詞元)，以及可調整的思考等級 (`low`、`medium`、`high`)。

[experiment

前往 AI Studio 試用

使用 Gemini 4 Argon 和 AI Studio，從零開始建構應用程式。](https://aistudio.google.com/apps?model=gemini-4-argon&hl=zh-tw)
[smart\_toy

應用程式庫

使用 Gemini 4 Argon 建構的應用程式，並加以改造。](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=zh-tw)
[rocket\_launch

開始使用

使用啟動提示詞，開始體驗 Gemini 4 Argon。](https://aistudio.google.com/learn/gemini-4-argon?hl=zh-tw)

本指南將說明 Gemini 4 Argon 的新功能、API 異動、程式碼範例和遷移指南。

## 新增模型

| 模型 | 模型 ID | 預設思考程度 | 定價 | 說明 |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | 2026 年 11 月 30 日前，可享新用戶優惠價：每 100 萬個輸入詞元 $2 美元，每 100 萬個輸出詞元 $10 美元 (之後為每 100 萬個輸入詞元 $4 美元，每 100 萬個輸出詞元 $20 美元)。詳情請參閱[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。 | Google 最強大的模型，專為解決最困難的問題而生，能深入精準地處理實際的軟體工程和知識工作。 |

## 快速入門導覽課程

請參考下列範例，使用建議的預設 `thinking_level` (`medium`) 和 64K 輸出詞元限制，向 `gemini-4-argon` 傳送要求：

### Python

```
pip install -U "google-genai>=2.30.1"
```

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
    config=types.GenerateContentConfig(
        max_output_tokens=65536,
        thinking_config=types.ThinkingConfig(thinking_level="medium"),
    ),
)

print(response.text)
```

### JavaScript

```
npm install "@google/genai@>=2.29.1"
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-4-argon",
  contents: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
  config: {
    maxOutputTokens: 65536,
    thinkingConfig: {
      thinkingLevel: "medium",
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."}]
    }],
    "generationConfig": {
      "maxOutputTokens": 65536,
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Gemini 4 Argon 新功能

- **輸入和輸出詞元合計上限為 100 萬個：**輸入、思考和輸出詞元共用 100 萬個詞元的窗口，非串流呼叫的單次要求上限為 3.2 萬個詞元，串流呼叫的單次串流上限為 6.4 萬個詞元。
- **解碼長度最多 100 萬個詞元：**模型可生成超過每個要求上限的內容，最多可達 100 萬個詞元減去輸入內容。系統預設會繼續使用最新的 Google GenAI SDK。
- **代理式影片解讀 (正式發布)：** [代理式影片解讀](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-tw#agentic-video-understanding)功能現已正式發布。
- **支援 Gemini Managed Agents：**Gemini Managed Agents 的 [Antigravity 代理程式](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw)現已支援 Gemini 4 Argon。

詳情請參閱 [Gemini 4 Argon 模型頁面](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-tw)。如需定價詳細資料，請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-4-argon)。

## 大型輸出內容和長解碼

如果任務需要深度推論，Gemini 4 Argon 會花較長時間思考，並更努力解決複雜的數學、科學和程式設計問題，一次就能生成結果。

- **輸入和輸出詞元數量上限統一為 100 萬：**Argon 最多可使用 100 萬個詞元 (扣除輸入詞元)，用於思考和輸出。
- **思考詞元會計入 `max_output_tokens`：**處理困難工作時，模型會使用更多 `max_output_tokens` 預算，以提供更優質的答案。使用 `thinking_level` 控制權杖用量。
- **單一要求上限 (串流 64K / 非串流 32K)：**單一串流要求最多可傳回 65,536 個詞元。單一非串流要求最多可傳回 32,768 個詞元，低於 Gemini 3.x 的 65,536 個。REST 呼叫也預設採用這些上限。

最新版 Google GenAI SDK 預設會執行長解碼。請使用 Python `google-genai` 2.30.1 以上版本，或 JavaScript `@google/genai` 2.29.1 以上版本。

在這些版本中，`automatic_continuation` 預設為 `True`，因此您不需要設定。如果將 `max_output_tokens` 設為高於單次要求上限，`generate_content` 和 `generate_content_stream` 會自動透過後續要求接續回覆，直到模型完成或達到 `max_output_tokens`，並傳回合併的回覆。

```
response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a complete, rigorous proof of the prime number theorem.",
    config=types.GenerateContentConfig(
        max_output_tokens=262144,
        thinking_config=types.ThinkingConfig(thinking_level="high"),
        automatic_continuation=True,  # Default.
    ),
)
```

如要自行執行迴圈，請設定 `automatic_continuation=False`。如果呼叫 REST 或使用舊版 SDK，要求會在達到單次要求上限時停止。如要瞭解 REST 迴圈、第三方架構、詞元計數，以及何時使用長解碼，請參閱[長解碼指南](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=zh-tw)。

### 設定輸出詞元限制

`max_output_tokens` 會設定生成內容的思考和輸出詞元總數，包括所有接續要求。請將這個值設得夠高，以免思考過程導致回覆過短。請將這個值設得夠低，這樣一來，當硬提示用完所有預算時，就能限制支出。

請先參考下列指引：

- **標準工作：**保留預設值。
- **現有應用程式的限制低於 32K：**將 `max_output_tokens` 提高至 32,768。如要使用較少權杖，請調低 `thinking_level`。
- **先前使用超過 32,000 個詞元的任務：**將 `max_output_tokens` 設為 65,536。
- **複雜推論和程式設計：**將 `max_output_tokens` 設為 131,072 或 262,144，最高可設為 1,048,576 減去輸入詞元。

如果要求用盡所有 `max_output_tokens`，就會傳回 `finish_reason: "MAX_TOKENS"`，並包含 `continuation_token`。你可以繼續或重新開始。

- **從檢查點繼續：**傳送原始要求，並附上最新的 `continuation_token` 和較高的 `max_output_tokens`。如未引發 `max_output_tokens`，要求會傳回 `400 INVALID_ARGUMENT`。
- **重新開始：**傳送原始要求，並提高 `max_output_tokens`，不使用 `continuation_token`。

### 瞭解思考程度

[思考等級](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=zh-tw)是 Gemini 4 Argon 的主要控制項，可調整品質、延遲時間和詞元用量：

| 思考程度 | 詞元用量 | 使用時機 |
| --- | --- | --- |
| `low` | 詞元最少，延遲時間最短 | 簡單且預算有限的工作。也適合用於需要稍微動腦的分析和寫作工作。處理困難工作時，品質可能會下降。 |
| `medium` (預設) | 平衡 | 建議用於大多數工作，包括複雜的程式碼和代理用途。 |
| `high` | 詞元最多，第一個詞元生成速度最慢 | 複雜推理、困難的數學和科學問題，以及最難的程式碼或代理工作。適合搭配長解碼，產生長輸出內容。 |

請在三個層級都以較高的 `max_output_tokens` 執行評估，以免答案因限制而中斷。然後選擇符合品質標準的最低 `thinking_level`。

## 遷移工作檢查清單

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### 遷移至 gemini-4-argon

- **更新模型 ID：**將模型字串變更為 `gemini-4-argon`。
- **明確設定 `max_output_tokens`：**串流和 SDK 呼叫的預設值為 64K，非串流 REST 呼叫的預設值為 32K。
- **提高低於 32K 的上限：**將任何低於 32K 的上限提高至至少 32,768。使用 `thinking_level` 減少權杖用量。
- **為長時間解碼做好準備：**如果工作超過單次要求上限，請使用最新版 SDK 或新增 `continuation_token` 迴圈。
- **將 `thinking_budget` 替換為 `thinking_level`：** `thinking_budget` 仍可運作，並對應至最接近的 `thinking_level`，但會傳回警告。在 `low`、`medium` 和 `high` 測試工作負載。
- **停止使用明確脈絡快取：**Gemini 4 Argon 不支援明確快取 (`cachedContents`/`caches.create`)，並會傳回錯誤。移除在 `GenerateContentConfig` 中建立或傳遞 `cached_content` 的呼叫。如果提示詞元數至少為 4,096 個，系統預設會啟用[隱含快取](https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=zh-tw)，並在快取命中時，將快取輸入詞元的費用折扣 95%。
- **移除已淘汰的參數：**從要求中移除 `temperature`、`top_p`、`top_k` 和 `candidate_count`。如果提供，系統會忽略取樣參數。
- **增加用戶端逾時值：**將 HTTP 用戶端逾時值設為每次呼叫至少 20 分鐘。
- **保留思考簽章：**在多輪和函式呼叫要求中，傳遞完整的對話記錄，包括[思考簽章](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=zh-tw#signatures)。

## 定價

2026 年 11 月 30 日前，Gemini 4 Argon 享有新用戶優惠：

- **輸入詞元：**每 100 萬個詞元 $2.00 美元 (2026 年 12 月 1 日起為 $4.00 美元)
  - **快取輸入詞元：**隱含快取功能會將快取輸入內容的費用折扣 95%，降至每 100 萬個詞元 $0.10 美元 (2026 年 12 月 1 日起為 $0.20 美元)。
- **輸出詞元 (含思考詞元)：**每 100 萬個詞元 $10.00 美元 (2026 年 12 月 1 日起為 $20.00 美元)

免費方案不支援 Gemini 4 Argon。如要查看完整的定價級別，請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-4-argon)。

## 其他模型

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8?hl=zh-tw)
- [Gemini 3.6 Flash 和 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=zh-tw)
- [查看所有車型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)

## 後續步驟

- 如要瞭解完整的串流、重新連線和詞元計數模式，請參閱[長解碼開發人員指南](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=zh-tw)。
- 如要瞭解思考等級和思考摘要的運作方式，請參閱[思考指南](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=zh-tw)。
- 在 [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw) 測試 Gemini 4 Argon。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-16 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-16 (世界標準時間)。"],[],[]]
