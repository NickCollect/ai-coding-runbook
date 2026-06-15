---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=zh-TW
fetched_at: 2026-06-15T06:33:22.691554+00:00
title: "Gemini Developer API \u8207 Gemini Enterprise Agent Platform \u7684\u6bd4\u8f03 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini Developer API 與 Gemini Enterprise Agent Platform 的比較

使用 Gemini 開發生成式 AI 解決方案時，Google 提供兩種 API 產品：[Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=zh-tw) 和 [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=zh-tw)。

透過 Gemini Developer API，您就能以最快速度建構、正式推出及擴充 Gemini 輔助應用程式。除非需要特定企業控制項，否則大多數開發人員都應使用 Gemini 開發人員 API。

Gemini Enterprise Agent Platform 提供全方位的企業級功能和服務生態系統，可建構及部署由 Google Cloud Platform 支援的生成式 AI 應用程式。

我們最近簡化了這兩項服務之間的遷移作業。現在可透過統一的 [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw) 存取 Gemini 開發人員 API 和 Gemini Enterprise Agent Platform API。

## 程式碼比較

本頁面會並列比較 Gemini Developer API 和 Gemini Enterprise Agent Platform 的文字生成快速入門導覽程式碼。

### Python

您可以透過 `google-genai` 程式庫存取 Gemini 開發人員 API 和 Gemini Enterprise Agent Platform 服務。如需安裝 `google-genai` 的操作說明，請參閱[程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)頁面。

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript 和 TypeScript

您可以透過 `@google/genai`程式庫存取 Gemini Developer API 和 Gemini Enterprise Agent Platform 服務。如需安裝 `@google/genai` 的操作說明，請參閱[程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)頁面。

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

您可以透過 `google.golang.org/genai`程式庫存取 Gemini Developer API 和 Gemini Enterprise Agent Platform 服務。如需安裝 `google.golang.org/genai` 的操作說明，請參閱[程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)頁面。

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### 其他用途和平台

如要瞭解其他平台和用途，請參閱 [Gemini 開發人員 API 說明文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)和 [Gemini Enterprise Agent Platform 說明文件](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=zh-tw)中的特定用途指南。

## 遷移注意事項

遷移時：

- 您必須使用 Google Cloud 服務帳戶進行驗證。詳情請參閱 [Gemini Enterprise Agent Platform 說明文件](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=zh-tw)。
- 你可以使用現有的 Google Cloud 專案 (與產生 API 金鑰時使用的專案相同)，也可以[建立新的 Google Cloud 專案](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=zh-tw)。
- Gemini Developer API 和 Gemini Enterprise Agent Platform API 支援的區域可能不同。請參閱[支援 Google Cloud 生成式 AI 的區域清單](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=zh-tw)。
- 在 Google AI Studio 中建立的模型必須在 Gemini Enterprise Agent Platform 中重新訓練。

如果不再需要使用 Gemini API 金鑰存取 Gemini Developer API，請遵循安全性最佳做法刪除金鑰。

刪除 API 金鑰的做法如下：

1. 開啟 [Google Cloud API 憑證](https://console.cloud.google.com/apis/credentials?hl=zh-tw)頁面。
2. 找出要刪除的 API 金鑰，然後點選「動作」圖示。
3. 選取「刪除 API 金鑰」。
4. 在「刪除憑證」強制回應中，選取「刪除」。

   刪除 API 金鑰需要幾分鐘的時間才會生效。作業完畢後，凡是使用已刪除 API 金鑰的流量都會遭拒。

## 後續步驟

- 如要進一步瞭解 Gemini Enterprise Agent Platform 的生成式 AI 解決方案，請參閱[這篇文章](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/multimodal/overview?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-19 (世界標準時間)。"],[],[]]
