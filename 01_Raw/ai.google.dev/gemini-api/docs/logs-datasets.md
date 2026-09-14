---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-TW
fetched_at: 2026-09-14T05:41:04.489499+00:00
title: "\u8a18\u9304\u548c\u8cc7\u6599\u96c6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 記錄和資料集

本指南說明如何透過 Google AI Studio 資訊主頁查看 Gemini API 使用記錄，進一步瞭解模型行為，以及使用者與應用程式的互動方式。您可以使用記錄功能觀察及偵錯，並*視需要與 Google 分享使用意見回饋，協助改善 Gemini 的開發人員用途*。[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-tw)

系統支援所有 `GenerateContent`、`BatchGenerateContent`、`StreamGenerateContent` API 呼叫，以及 [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw) API 呼叫 (不含受管理代理程式)。包括透過 [OpenAI 相容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)端點發出的呼叫。

## 設定專案記錄

根據預設，API 會儲存所有互動物件 (`store=true`)，以簡化伺服器端狀態管理功能的使用。相較之下，Generate Content API 預設不會儲存要求，且必須從 AI Studio 啟用每個要求或專案層級的儲存功能。

在 Google [AI Studio](https://aistudio.google.com/logs?hl=zh-tw) 中，您可以為所有專案或特定專案啟用或停用記錄功能，並隨時透過「記錄和資料集」頁面中的「設定」面板變更這些偏好設定。您可以分別為 `generateContent` API 和[互動](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw) API 開啟或關閉記錄功能，藉此變更專案的預設儲存行為。

### 要求層級記錄

不同 API 的儲存和記錄行為有所不同：

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw)：**預設會儲存要求 (`store=true`)，簡化伺服器端狀態管理。
- **生成 Content API (`generateContent`)：**預設不會儲存要求 (`store=false`)。

以下說明如何設定 `store` 屬性：

**`generateContent` API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## 在 AI Studio 中查看專案記錄

1. 前往 [AI Studio](https://aistudio.google.com/logs?hl=zh-tw) 的「記錄」頁面。
2. 從下拉式選單中選取專案。
3. 如果存在記錄，表格會以逆時序顯示 Interactions API 的記錄。
4. 如要觀察 Generate Content API 的專案記錄，請先在[設定面板](#configure-logging)中啟用這項功能。

按一下項目即可預覽酬載。您可以檢查 Gemini 的完整提示和回覆，以及先前對話的脈絡。如果是 **Interactions API** 要求，記錄也會包含 `previous_interaction_id` 的直接連結。

## 設定專案儲存空間保留期限

記錄會在預設保留期限 (55 天) 過後失效，並標示為待刪除 (除非[儲存至資料集](#create)，否則不會失效)。您可以將專案記錄的保留期限設為最多 7、14、28 或 55 天。

## 建立及共用資料集

您可以將記錄檔儲存至資料集，以便更有效率地整理及匯出記錄檔。

- 在「記錄」頁面中，找出頂端的篩選列，然後選取要篩選的屬性。
- 在篩選後的檢視畫面中，使用核取方塊選取所有或個別記錄。
- 按一下清單頂端的「建立資料集」按鈕。
- 為新資料集命名，並視需要新增說明。
- 您會看到剛才建立的資料集，其中包含精選的記錄集。
- 將資料集匯出為 CSV、JSONL 檔案或 Google 試算表，以供進一步分析。

資料集可協助您處理多種用途。

- **策劃挑戰集：**針對您希望 AI 改進的領域，推動未來的改善措施。
- **策劃樣本集：**例如，從實際使用情況中取得樣本，以便透過其他模型生成回應，或是收集極端案例，以便在部署前進行例行檢查。
- **評估集：**這類資料集代表重要功能的實際使用情況，可用於比較其他模型或系統指令疊代版本。

您可以選擇將資料集提供給 Google 做為示範範例，協助我們進行 Gemini 研究與開發。

## 限制

目前系統不支援記錄下列項目：

- Imagen 和 Veo 模型
- Gemini 嵌入模型
- Gemini Robotics 模型
- 含有影片、GIF 或 PDF 的輸入內容
- Gemini API 中的公開預先發布版代理

## 後續步驟

- **使用工作階段記錄設計原型：**使用 [AI Studio Build](https://aistudio.google.com/apps?hl=zh-tw) 直覺式程式開發應用程式，並新增 API 金鑰，啟用 AI 功能的 Gemini API 記錄。
- **使用 Gemini Batch API 重新執行記錄：**使用資料集進行回應取樣，並透過 [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb) 重新執行記錄，評估模型或應用程式邏輯。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-12 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-12 (世界標準時間)。"],[],[]]
