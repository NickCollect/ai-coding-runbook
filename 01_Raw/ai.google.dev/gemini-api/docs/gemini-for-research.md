---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=zh-TW
fetched_at: 2026-10-12T07:03:16.453845+00:00
title: "\u904b\u7528 Gemini for Research \u52a0\u5feb\u63a2\u7d22\u901f\u5ea6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)

# 運用 Gemini for Research 加快探索速度

[取得 Gemini API 金鑰](https://aistudio.google.com/apikey?hl=zh-tw)

Gemini 模型可用於推進各領域的基礎研究。
以下說明如何使用 Gemini 進行研究：

- **分析及控管模型輸出內容**：如要進一步分析，可以使用 `CitationMetadata` 等工具檢查模型生成的候選回覆。您也可以設定模型生成和輸出選項，例如 `responseSchema`、`topP` 和 `topK`。[瞭解詳情](https://ai.google.dev/api/generate-content?hl=zh-tw)。
- **多模態輸入**：Gemini 可處理圖片、音訊和影片，因此能朝多種令人振奮的研究方向發展。[瞭解詳情](https://ai.google.dev/gemini-api/docs/vision?hl=zh-tw)。
- **長篇對話脈絡功能**：Gemini 3.0 Flash 和 Pro 支援 100 萬個詞元的脈絡窗口。[瞭解詳情](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw)。
- **Grow with Google 成長計畫**：透過 API 和 Google AI Studio 快速存取 Gemini 模型，用於生產用途。如果您需要以 Google Cloud 為基礎的平台，Gemini Enterprise Agent Platform 可提供額外的支援基礎架構。

為支援學術研究並推動尖端研究，Google 透過 [Gemini 學術計畫](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=zh-tw#gemini-academic-program)，為科學家和學術研究人員提供 Gemini API 抵免額。

## 開始使用 Gemini

透過 Gemini API 和 Google AI Studio，您可以開始使用 Google 的最新模型，並將構想化為可擴充的應用程式。

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("How large is the universe?"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("How large is the universe?"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## 精選學術人員

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=zh-tw)

「我們的研究從穩健性和安全性的角度，探討 Gemini 做為視覺語言模型 (VLM) 的功能，以及在各種環境中的代理行為。到目前為止，我們已評估 Gemini 在 VLM 代理程式執行電腦工作時，面對彈出式視窗等干擾的強健程度，並運用 Gemini 分析社群互動、時間事件，以及根據影片輸入內容判斷風險因素。

[Diyi Yang 的網站](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=zh-tw)

「Gemini Pro 和 Flash 具有長脈絡窗口，有助於我們進行 OK-Robot (開放式詞彙行動操作專案)。Gemini 可透過機器人的「記憶體」執行複雜的自然語言查詢和指令，也就是機器人在長時間運作期間所做的先前觀察。我和 Mahi Shafiullah 也使用 Gemini 將工作分解為程式碼，讓機器人可以在現實世界中執行。」

[Lerrel Pinto 的網站](https://www.lerrelpinto.com/)

## Gemini 學術計畫

[支援國家/地區](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-tw)的合格學術研究人員 (例如教職員、行政人員和博士生) 可申請 Gemini API 抵免額和更高的頻率限制，用於研究專案。這項支援可提高科學實驗的處理量，並促進研究進展。

我們特別感興趣的研究領域如下，但我們也歡迎來自不同科學領域的申請：

- **評估和基準**：社群認可的評估方法，可提供真實性、安全性、指令遵循、推論和規劃等領域的強大效能信號。
- **加速科學探索，造福人類**：AI 在跨領域科學研究的潛在應用，包括罕見和被忽略的疾病、實驗生物學、材料科學和永續發展等領域。
- **具體化和互動**：運用大型語言模型，在具體化 AI、環境互動、機器人和人機互動等領域中，探索新穎的互動方式。
- **新興功能**：探索強化推論和規劃所需的新代理能力，以及如何在推論期間擴展功能 (例如使用 Gemini Flash)。
- **多模態互動和理解**：找出多模態基礎模型的差距和機會，以便分析、推論及規劃各種任務。

資格：只有隸屬於有效學術機構或學術研究機構的個人 (教職員、研究人員或同等人員) 才能申請。請注意，Google 可全權決定是否授予及移除 API 存取權和抵免額。我們每月都會審查申請。

### 開始使用 Gemini API 進行研究

[立即申請](https://forms.gle/HMviQstU8PxC5iCt5)

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-24 (世界標準時間)。

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-24 (世界標準時間)。"],[],[]]
