---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=zh-TW
fetched_at: 2026-11-02T07:22:57.904418+00:00
title: "\u77ad\u89e3\u53ca\u8a08\u7b97\u7b26\u8a18 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

提供意見

# 瞭解及計算符記

Gemini 和其他生成式 AI 模型會以稱為「詞元」的細微程度處理輸入和輸出內容。

**Gemini 模型的 1 個詞元約等於 4 個字元。100 個符記約等於 60 到 80 個英文字。**

## 關於權杖

詞元可以是單一字元 (例如 `z`)，也可以是完整字詞 (例如 `cat`)。長字詞會拆分為多個詞元。模型使用的所有符記組合稱為詞彙，而將文字分割成符記的程序稱為*符記化*。

啟用計費功能後，[Gemini API 呼叫費用](https://ai.google.dev/pricing?hl=zh-tw)會部分取決於輸入和輸出權杖數量，因此瞭解如何計算權杖數量會很有幫助。

您可以在 Colab 中試用計算符記。

|  |  |  |
| --- | --- | --- |
| [在 ai.google.dev 上查看](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw) | [試用 Colab 筆記本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=zh-tw) | [在 GitHub 中查看筆記本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=zh-tw) |

## 計算詞元數

Gemini API 的所有輸入和輸出內容都會經過權杖化，包括文字、圖片檔和其他非文字模態。

計算權杖的方式如下：

- **使用要求輸入內容呼叫 [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=zh-tw)。**  
  ：這會傳回*僅輸入內容*中的權杖總數。您可以在將輸入內容傳送至模型前，先呼叫這個方法，檢查要求的大小。
- **呼叫 `generate_content` 後，請在 `response` 物件上使用 `usage_metadata` 屬性。**  
  ：這會傳回*輸入和輸出*的權杖總數：`total_token_count`。  
  此外，這項要求也會分別傳回輸入和輸出內容的詞元數：`prompt_token_count` (輸入詞元) 和 `candidates_token_count` (輸出詞元)。

  如果使用[思考型模型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)，思考過程中使用的詞元會傳回 `thoughts_token_count`。如果使用[脈絡快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)，快取的詞元數會顯示在 `cached_content_token_count`。

### 計算文字詞元數

如果呼叫 `count_tokens` 時只輸入文字，系統只會傳回*輸入內容* (`total_tokens`) 的文字詞元數。您可以在呼叫 `generate_content` 之前執行這項呼叫，檢查要求的大小。

另一個選項是呼叫 `generate_content`，然後使用 `response` 物件的 `usage_metadata` 屬性取得下列項目：

- 輸入 (`prompt_token_count`)、快取內容 (`cached_content_token_count`) 和輸出 (`candidates_token_count`) 的個別權杖數
- 思考過程的權杖數 (`thoughts_token_count`)
- *輸入和輸出*的詞元總數 (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=prompt
)

print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

// Convert prompt to a slice of *genai.Content using the helper.
contents := []*genai.Content{
  genai.NewContentFromText(prompt, genai.RoleUser),
}
countResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
    ```
```

### 計算多輪 (對話) 詞元

如果使用對話記錄呼叫 `count_tokens`，系統會傳回對話中每個角色 (`total_tokens`) 的文字總詞元數。

另一個選項是呼叫 `send_message`，然後使用 `response` 物件上的 `usage_metadata` 屬性，取得下列資訊：

- 輸入 (`prompt_token_count`)、快取內容 (`cached_content_token_count`) 和輸出 (`candidates_token_count`) 的個別詞元數
- 思考過程的權杖數 (`thoughts_token_count`)
- *輸入和輸出*的詞元總數 (`total_token_count`)

如要瞭解下一個對話回合的大小，您需要在呼叫 `count_tokens` 時將其附加至記錄。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.8-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=chat.get_history()
    )
)

response = chat.send_message(
    message="In one sentence, explain how a computer works to a young child."
)
print(response.usage_metadata)

extra = types.UserContent(
    parts=[
        types.Part(
            text="What is the meaning of life?",
        )
    ]
)
history = [*chat.get_history(), extra]
print(client.models.count_tokens(model="gemini-3.8-flash", contents=history))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    { role: "user", parts: [{ text: "Hi my name is Bob" }] },
    { role: "model", parts: [{ text: "Hi Bob!" }] },
  ];
  const chat = ai.chats.create({
    model: "gemini-3.8-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: chat.getHistory(),
  });
  console.log(countTokensResponse.totalTokens);

  const chatResponse = await chat.sendMessage({
    message: "In one sentence, explain how a computer works to a young child.",
  });
  console.log(chatResponse.usageMetadata);

  const extraMessage = {
    role: "user",
    parts: [{ text: "What is the meaning of life?" }],
  };
  const combinedHistory = [...chat.getHistory(), extraMessage];
  const combinedCountTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: combinedHistory,
  });
  console.log(
    "Combined history token count:",
    combinedCountTokensResponse.totalTokens,
  );
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

history := []*genai.Content{
  {Role: genai.RoleUser, Parts: []*genai.Part({Text: "Hi my name is Bob"})},
  {Role: genai.RoleModel, Parts: []*genai.Part({Text: "Hi Bob!"})},
}
chat, err := client.Chats.Create(ctx, "gemini-3.8-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", chat.History(false), nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(firstTokenResp.TotalTokens)

resp, err := chat.SendMessage(ctx, genai.NewPartFromText("In one sentence, explain how a computer works to a young child."))
if err != nil {
  log.Fatal(err)
}
fmt.Printf("%#v\n", resp.UsageMetadata)

extra := genai.NewContentFromText("What is the meaning of life?", genai.RoleUser)
hist := chat.History(false)
hist = append(hist, extra)

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### 計算多模態權杖

Gemini API 的所有輸入內容都會經過權杖化，包括文字、圖片檔和其他非文字模態。請注意以下關於 Gemini API 處理多模態輸入內容時，權杖化的重要重點：

- 如果輸入圖片的兩個維度均 <=384 像素，則會計為 258 個權杖。如果圖片有一邊或兩邊超過這個尺寸，系統會視需要裁剪及縮放成 768x768 像素的圖塊，每個圖塊計為 258 個詞元。
- 影片和音訊檔案會按照下列固定費率轉換為詞元：影片每秒 263 個詞元，音訊每秒 32 個詞元。這個費率適用於靜態處理 (預設)。如果是代理處理，詞元用量會有所不同。請參閱[依處理模式劃分的影片權杖用量](#video-token-usage)。

#### 媒體解析度

[Gemini 3 模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-3)透過 `media_resolution` 參數，提供多模態視覺處理的精細控制功能。`media_resolution` 參數會決定每個輸入圖片或影片影格分配的權杖數量上限。解析度越高，模型就越能辨識細小文字或細節，但會增加詞元用量和延遲時間。

如要進一步瞭解這項參數，以及該參數對詞元計算的影響，請參閱[媒體解析度](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=zh-tw)指南。

#### 圖片檔

如果使用文字和圖片輸入內容呼叫 `count_tokens`，系統會傳回*輸入內容中*文字和圖片的合併詞元數 (`total_tokens`)。您可以在呼叫 `generate_content` 之前執行這項呼叫，檢查要求的大小。您也可以選擇分別對文字和檔案呼叫 `count_tokens`。

另一個選項是呼叫 `generate_content`，然後使用 `response` 物件上的 `usage_metadata` 屬性，取得下列資訊：

- 輸入 (`prompt_token_count`)、快取內容 (`cached_content_token_count`) 和輸出 (`candidates_token_count`) 的個別權杖數
- 思考過程的權杖數 (`thoughts_token_count`)
- *輸入和輸出*的詞元總數 (`total_token_count`)

使用 File API 上傳圖片的範例：

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";

async function main() {
  const organ = await ai.files.upload({
    file: path.join(media, "organ.jpg"),
    config: { mimeType: "image/jpeg" },
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx, 
  filepath.Join(getMedia(), "organ.jpg"), 
  &genai.UploadFileConfig{
    MIMEType : "image/jpeg",
  },
)
if err != nil {
  log.Fatal(err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

以內嵌資料形式提供圖片的範例：

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";
const imageBuffer = fs.readFileSync(path.join(media, "organ.jpg"));

const imageBase64 = imageBuffer.toString("base64");

const contents = createUserContent([
  prompt,
  createPartFromBase64(imageBase64, "image/jpeg"),
]);

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: contents,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

imageBytes, err := os.ReadFile("organ.jpg")
if err != nil {
    log.Fatalf("Failed to read image file: %v", err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  {
        InlineData: &genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imageBytes,
        },
  },
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### 影片或音訊檔案

音訊和視訊會分別以以下固定費率轉換為權杖：

- 影片：每秒 263 個詞元
- 音訊：每秒 32 個權杖

如果您使用文字和影片/音訊輸入內容呼叫 `count_tokens`，系統會傳回*輸入內容中*文字和影片/音訊檔案的合併權杖計數 (`total_tokens`)。您可以在呼叫 `generate_content` 之前進行這項呼叫，檢查要求大小。您也可以視需要分別對文字和檔案呼叫 `count_tokens`。

另一個選項是呼叫 `generate_content`，然後使用 `response` 物件的 `usage_metadata` 屬性取得下列項目：

- 輸入 (`prompt_token_count`)、快取內容 (`cached_content_token_count`) 和輸出 (`candidates_token_count`) 的個別權杖數
- 思考過程的詞元數 (`thoughts_token_count`)
- *輸入和輸出*中的詞元總數 (`total_token_count`)。

### Python

```
from google import genai
import time

client = genai.Client()
prompt = "Tell me about this video"
your_file = client.files.upload(file=media / "Big_Buck_Bunny.mp4")

while not your_file.state or your_file.state.name != "ACTIVE":
    print("Processing video...")
    print("File state:", your_file.state)
    time.sleep(5)
    your_file = client.files.get(name=your_file.name)

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this video";

async function main() {
  let videoFile = await ai.files.upload({
    file: path.join(media, "Big_Buck_Bunny.mp4"),
    config: { mimeType: "video/mp4" },
  });

  while (!videoFile.state || videoFile.state.toString() !== "ACTIVE") {
    console.log("Processing video...");
    console.log("File state: ", videoFile.state);
    await sleep(5000);
    videoFile = await ai.files.get({ name: videoFile.name });
  }

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx,
  filepath.Join(getMedia(), "Big_Buck_Bunny.mp4"),
  &genai.UploadFileConfig{
    MIMEType : "video/mp4",
  },
)
if err != nil {
  log.Fatal(err)
}

for file.State == genai.FileStateUnspecified || file.State != genai.FileStateActive {
  fmt.Println("Processing video...")
  fmt.Println("File state:", file.State)
  time.Sleep(5 * time.Second)

  file, err = client.Files.Get(ctx, file.Name, nil)
  if err != nil {
    log.Fatal(err)
  }
}

parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this video"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### 各處理模式的影片權杖用量

影片的權杖用量取決於處理模式：

| **處理模式** | **詞元計算** | **常見用途** |
| --- | --- | --- |
| **靜態** (預設) | 預設為每秒約 100 個詞元 (低解析度)，或每秒約 300 個詞元 (高解析度)。所有影格皆以每秒 1 影格的速度取樣。 | 可預測，與影片長度成正比。 |
| **代理功能** | 視內容複雜度而定。模型只會載入回答提示所需的部分，例如轉錄稿、影格和/或音訊。 | 長篇內容最多可減少 88% 的詞元。 |

如果採用代理處理，1 小時的講座在靜態模式下會使用約 108 萬個詞元，但實際使用量可能約為 10.8 萬個詞元，具體取決於提示和內容。

如要查看要求的實際權杖用量，請使用回應中的 `usage_metadata` 欄位。在 `UsageMetadata` 中，代理影片權杖會透過下列欄位回報：

- **初始提示** (影片參考資料 + 使用者提示)：`prompt_token_count`
- **導覽思維**：`thoughts_token_count`
- **依需求載入轉錄稿、影格和音訊**：`tool_use_prompt_token_count`
- **最終答案**：`candidates_token_count`

### 計算思考詞元數

開啟思考功能後，回覆的價格會是輸出詞元和思考詞元的總和。您可以從 `thoughtsTokenCount` 欄位 (或 SDK 對等欄位) 擷取生成的思考詞元總數。

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

思考模型會生成完整的想法，藉此提升最終回覆的品質，然後輸出[摘要](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw#summaries)，深入瞭解思考過程。因此，即使 API 只輸出摘要，API 仍會根據模型生成摘要時產生的完整思考詞元計費。

如要進一步瞭解如何設定思考功能，請參閱「[Gemini 思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)」指南。

## 脈絡窗口

Gemini API 提供的模型，其脈絡窗口是以詞元為單位。脈絡窗口定義了您可以提供的輸入量，以及模型可以生成的輸出量。如要判斷脈絡窗口的大小，可以呼叫 [`models.get` 端點](https://ai.google.dev/api/rest/v1/models/get?hl=zh-tw)，或查看[模型說明文件](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)。

- **Gemini 4 模型 (`gemini-4-argon`)：**輸入、思考和輸出詞元共用 100 萬個詞元的脈絡窗口 (`1,048,576` 個詞元)。單一要求的輸出詞元上限為 `65,536` 個 (串流，`streamGenerateContent`) 和 `32,768` 個 (非串流，`generateContent`)，您也可以使用[長解碼](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=zh-tw)生成最多 `1,048,576` 個詞元。如果輸入的詞元加上 `max_output_tokens` 超過 1,048,576 個詞元，API 會自動將輸出上限設為脈絡窗口的剩餘空間 (`1,048,576` 減去輸入的詞元)。
- **Gemini 3 和 2.5 模型：**使用不同的輸入 (`1,048,576` 權杖) 和輸出 (`65,536` 權杖) 預算。

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.8-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.8-flash'});
  console.log(modelInfo.inputTokenLimit);
  console.log(modelInfo.outputTokenLimit);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
  log.Fatal(err)
}
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.8-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-13 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-13 (世界標準時間)。"],[],[]]
