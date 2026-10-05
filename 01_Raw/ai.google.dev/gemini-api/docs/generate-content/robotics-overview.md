---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=zh-TW
fetched_at: 2026-10-05T06:38:03.548797+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

提供意見

# Gemini Robotics ER

Gemini Robotics ER (具身推論) 模型是視覺語言模型 (VLM)，可讓機器人感知實體世界並與之互動。解讀視覺資料、執行空間和時間推論、規劃多步驟工作，以及調度機器人和工具。

## 模型

Gemini Robotics ER 2 模型是 Gemini Robotics 的最新模型。
這項更新後的推論模型可讓機器人精確瞭解周遭環境。這項技術專門用於具身推論功能，例如代理機器人協調 (例如使用 VLA)、機器人影片理解 (包括進度理解和成功偵測)、儀表讀取、指向和空間推論。

Gemini Robotics ER 2 模型推出兩個模型端點：

- **`gemini-robotics-er-2-preview`**：標準 ER 2 模型。以 Gemini 3.5 Flash 為基礎，改善空間推理、影片片段搜尋、影片進度分類、多機器人協調和多步驟工具使用。
- **`gemini-robotics-er-2-streaming-preview`**：透過 [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw) 進行即時串流時，可獲得最佳體驗。這個模型適用於低延遲的機器人代理程式，可處理連續的音訊和視訊輸入內容。

如果您使用 Gemini Robotics ER 1.6，請在 API 呼叫中將 `model="gemini-robotics-er-1.6-preview"` 替換為 `model="gemini-robotics-er-2-preview"` 或 `model="gemini-robotics-er-2-streaming-preview"`，升級至 Gemini Robotics ER 2。請注意，Gemini Robotics ER 1.6 模型將於 [8 月底](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw#robotics-models)停用。

[在 Google AI Studio 中試用 Gemini Robotics ER 2](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=zh-tw)

## 機器人功能

Gemini Robotics ER 支援多種具身推論功能。
選取功能即可瞭解詳情：

| 功能 | 說明 | 指南 |
| --- | --- | --- |
| 空間推論 | 指向物件、在影片中追蹤物件、使用定界框偵測物件，以及規劃軌跡。 | [空間推論](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=zh-tw) |
| 代理式願景 | 運用圖片處理工具，透過執行程式碼功能提升其他功能。 | [代理願景](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=zh-tw) |
| 工作自動化調度管理 | 結合空間推論和自訂機器人 API，完成長期任務。 | [工作自動化調度管理](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=zh-tw) |
| 串流 (僅限 Gemini Robotics ER 2 串流端點) | 雙向串流功能，可供低延遲的即時機器人代理程式使用函式呼叫。 | [機器人串流](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw) |
| 影片進度 (僅限 Gemini Robotics ER 2) | 從連續影片動態饋給中尋找重要時刻，並分類進度。 | [影片理解](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=zh-tw) |

## 開始使用

以下範例會在圖片中尋找物件，並傳回標準化的 2D 座標和標籤。您可以將這項輸出內容直接傳遞至機器人 API 或 VLA 模型，產生機器人動作。

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

輸出內容會是包含物件的 JSON 陣列，每個物件都有 `point` (標準化 `[y, x]` 座標) 和用於識別物件的 `label`。

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

下圖顯示這些點的範例：

![顯示圖片中物體點的範例](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=zh-tw)

## 運作方式

Gemini Robotics ER 接受圖片、影片或音訊輸入內容，並以自然語言提示。這項功能會識別物件、推論場景脈絡和空間關係，並傳回座標或定界框等結構化輸出內容。

Gemini Robotics ER 也是代理式系統，可將複雜工作分解為子工作，並呼叫機器人函式或執行生成的程式碼來完成這些子工作。舉例來說，「把蘋果放進碗裡」這個動作會分解為「找到蘋果」、「抓住蘋果」和「放置蘋果」等步驟。

如要瞭解 Gemini 如何執行工具呼叫，請參閱「[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=zh-tw#how-it-works)」。

## 安全性

雖然 Gemini Robotics ER 的設計以安全為考量，但您仍有責任確保機器人周圍環境安全無虞。生成式 AI 模型可能會出錯，實體機器人則可能造成損壞。如要瞭解詳情，請前往 [Google DeepMind 機器人安全頁面](https://deepmind.google/models/gemini-robotics/safety?hl=zh-tw)。

## 最佳做法

1. 使用平實的自然語言。請像對人一樣描述機器人要執行的動作。如果某個字詞無法正常運作，請嘗試使用常見的同義字。
2. 最佳化視覺輸入內容。先裁剪或放大圖片中的小型或模糊物件，再傳送圖片。光線和低色彩對比度可能會影響偵測結果。
3. 將複雜任務拆解成多個步驟。請將每個步驟分別傳送至模型，讓模型專注於特定內容，並提高準確率。
4. 針對高精確度工作多次查詢，並計算結果平均值。這種共識做法可減少空間輸出內容的差異。

## 限制

使用 Gemini Robotics ER 進行開發時，請注意下列限制：

- **API 金鑰限制：**Gemini API 不接受來自未受限制 API 金鑰的要求，並會傳回 `403 Forbidden` 錯誤。在 [AI Studio](https://aistudio.google.com/api-keys?hl=zh-tw) 中新增限制，確保 API 金鑰安全無虞。詳情請參閱「[保護未設限的 API 金鑰安全](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#secure-unrestricted-keys)」一文。
- **延遲時間與效能：**複雜的查詢、高解析度輸入內容或高思考程度可能會導致處理時間增加。思考層級請使用中等，在延遲時間和效能之間取得平衡。
- **幻覺：**如同所有大型語言模型，Gemini Robotics ER 模型有時也會產生「幻覺」或提供錯誤資訊，尤其是針對模稜兩可的提示或超出分布範圍的輸入內容。
- **取決於提示品質：**輸出內容品質取決於輸入提示的清晰度。使用具體且結構完整的提示。
- **運算成本：**執行模型 (尤其是使用影片輸入內容或高 `thinking_budget` 時) 會消耗運算資源並產生費用。詳情請參閱「[思考](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=zh-tw)」頁面。
- **輸入類型：**如要瞭解各模式的限制，請參閱下列主題。
  - [圖片輸入內容](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=zh-tw#technical-details-image)
  - [視訊輸入](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-tw#supported-formats)
  - [音訊輸入](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=zh-tw#supported-formats)

## 隱私權聲明

您瞭解本文件提及的機器人模型 (以下簡稱「機器人模型」) 會運用影片和音訊資料，根據您的指示操作及移動硬體。因此，您可能會操作機器人模型，讓模型收集可識別身分者的資料，例如語音、圖像和肖像資料 (「個人資料」)。如果您選擇以會收集個人資料的方式操作機器人模型，您同意不會允許任何可識別身分的人與機器人模型互動或出現在機器人模型周圍區域，除非且直到您已充分通知這些可識別身分的人，並取得他們同意，瞭解 Google 可能會根據 [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=zh-tw) (以下簡稱「條款」) 的 Gemini API 附加服務條款提供及使用他們的個人資料，包括「Google 如何使用您的資料」一節所述。您應確保這類通知允許收集及使用《條款》所述的個人資料，並盡可能運用商業上合理的努力，透過臉部模糊處理等技術，以及在不含可識別身分者的區域操作機器人模型，盡量減少個人資料的收集和散布。

## 定價

如需價格和適用區域的詳細資訊，請參閱[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)頁面。

## 模型端點

### Gemini Robotics ER 2 預先發布版

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | `gemini-robotics-er-2-preview` |
| save支援的資料類型 | **輸入裝置**  文字、圖片、影片、音訊  **輸出內容**  文字 |
| token\_auto 代幣限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw) | **輸入權杖限制**  131,072  **輸出詞元限制**  65,536 |
| handyman功能 | **[生成音訊](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)**  不支援  **[快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)**  支援  **[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)**  支援  **[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)**  支援  **[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)**  支援  **[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)**  支援  **[利用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)**  支援  **[圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)**  不支援  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw)**  不支援  **[以搜尋為基準](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)**  支援  **[結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)**  支援  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)**  支援  **[網址內容](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)**  支援 |
| speed計費方案 | **[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)**  支援  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)**  不支援  **[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)**  不支援 |
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
| speed計費方案 | **[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)**  不支援  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)**  不支援  **[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)**  不支援 |
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
| speed計費方案 | **[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)**  支援  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)**  不支援  **[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)**  不支援 |
| 123 個版本 | 詳閱[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#model-versions)。  - 預覽：`gemini-robotics-er-1.6-preview` |
| calendar\_month最新更新 | 2025 年 12 月 |
| cognition\_2知識截點 | 2025 年 1 月 |

## 後續步驟

- [空間推論](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=zh-tw)：指向、追蹤、定界框、軌跡。
- [代理能力](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=zh-tw)：執行程式碼、讀取儀器、標註圖片。
- [工作流程協調](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=zh-tw)：使用自訂機器人 API 執行長期任務。
- [串流機器人](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw)：即時雙向串流 (僅限 Gemini Robotics ER 2)。
- [影片理解](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=zh-tw)：尋找特定時刻和進度分類 (僅限 Gemini Robotics ER 2)。
- [Google DeepMind 機器人安全](https://deepmind.google/models/gemini-robotics/safety?hl=zh-tw)：模型系列背後的安全研究。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-08 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-08 (世界標準時間)。"],[],[]]
