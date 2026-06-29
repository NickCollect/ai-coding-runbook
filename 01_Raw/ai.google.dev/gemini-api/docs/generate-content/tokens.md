---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=zh-CN
fetched_at: 2026-06-29T05:34:02.018820+00:00
title: "\u4e86\u89e3\u8bcd\u5143\u5e76\u8ba1\u7b97\u8bcd\u5143\u6570\u91cf \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 了解词元并计算词元数量

Gemini 和其他生成式 AI 模型会以一种称为“token”的粒度处理输入和输出。

**对于 Gemini 模型，一个 token 大致相当于 4 个字符。
100 个 token 大约相当于 60-80 个英文单词。**

## 令牌简介

词元可以是单个字符（例如 `z`），也可以是整个字词（例如 `cat`）。长字词会被拆分为多个 token。模型使用的所有 token 的集合称为词汇，将文本拆分为 token 的过程称为 *token 化*。

启用结算功能后，[对 Gemini API 的调用费用](https://ai.google.dev/pricing?hl=zh-cn)部分取决于输入和输出 token 的数量，因此了解如何计算 token 数量会很有帮助。

您可以在我们的 Colab 中尝试统计令牌。

|  |  |  |
| --- | --- | --- |
| [在 ai.google.dev 上查看](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | [试用 Colab 笔记本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=zh-cn) | [在 GitHub 上查看笔记本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=zh-cn) |

## 统计 token 数量

Gemini API 的所有输入和输出（包括文本、图片文件和其他非文本模态）都会进行分词。

您可以通过以下方式统计令牌数量：

- **使用请求的输入调用 [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=zh-cn)。**  
   这会返回*仅输入*中的令牌总数。您可以在将输入内容发送给模型之前进行此调用，以检查请求的大小。
- **在调用 `generate_content` 后，对 `response` 对象使用 `usage_metadata` 属性。**  
   这会返回*输入和输出*中的令牌总数：`total_token_count`。  
   它还会分别返回输入和输出的 token 数：`prompt_token_count`（输入 token）和 `candidates_token_count`（输出 token）。

  如果您使用的是[思考模型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)，则思考过程中使用的 token 会在 `thoughts_token_count` 中返回。如果您使用的是[上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)，缓存的令牌数量将位于 `cached_content_token_count` 中。

### 统计文本 token

如果您使用仅包含文本的输入调用 `count_tokens`，它会返回*仅包含输入内容* (`total_tokens`) 的文本的 token 数量。您可以在调用 `generate_content` 之前进行此调用，以检查请求的大小。

另一种方法是调用 `generate_content`，然后使用 `response` 对象上的 `usage_metadata` 属性来获取以下信息：

- 输入 (`prompt_token_count`)、缓存内容 (`cached_content_token_count`) 和输出 (`candidates_token_count`) 的单独 token 数
- 思考过程的 token 数 (`thoughts_token_count`)
- *输入和输出*中的 token 总数 (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=prompt
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
    model: "gemini-3.5-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
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
countResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
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

### 统计多轮（聊天）对话的 token 数量

如果您使用聊天记录调用 `count_tokens`，它会返回聊天中每个角色的文本的总 token 数 (`total_tokens`)。

另一种方法是调用 `send_message`，然后使用 `response` 对象上的 `usage_metadata` 属性来获取以下信息：

- 输入 (`prompt_token_count`)、缓存内容 (`cached_content_token_count`) 和输出 (`candidates_token_count`) 的单独 token 数
- 思考过程的 token 数 (`thoughts_token_count`)
- *输入和输出*中的 token 总数 (`total_token_count`)

如需了解下一个对话轮次的大小，您需要在调用 `count_tokens` 时将其附加到历史记录中。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=chat.get_history()
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
print(client.models.count_tokens(model="gemini-3.5-flash", contents=history))
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
    model: "gemini-3.5-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
chat, err := client.Chats.Create(ctx, "gemini-3.5-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", chat.History(false), nil)
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

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### 统计多模态 token

Gemini API 的所有输入内容（包括文本、图片文件和其他非文本模态）都会被分词。请注意以下关于 Gemini API 在处理多模态输入时进行分词的高级关键点：

- 如果图片输入的两个维度均小于或等于 384 像素，则计为 258 个 token。如果图片在某个或两个维度上较大，则会根据需要将其剪裁并缩放为 768x768 像素的图块，每个图块计为 258 个 token。
- 视频和音频文件会按以下固定费率转换为 token：视频为每秒 263 个 token，音频为每秒 32 个 token。

#### 媒体分辨率

[Gemini 3 模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-3)通过 `media_resolution` 参数引入了对多模态视觉处理的精细控制。`media_resolution` 参数用于确定**为每个输入图片或视频帧分配的 token 数量上限**。分辨率越高，模型读取细小文字或识别细微细节的能力就越强，但 token 用量和延迟时间也会增加。

如需详细了解该参数及其对令牌计算的影响，请参阅[媒体分辨率](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=zh-cn)指南。

#### 图片文件

如果您使用文本和图片输入调用 `count_tokens`，它会返回*输入中*文本和图片的组合令牌数量 (`total_tokens`)。您可以在调用 `generate_content` 之前进行此调用，以检查请求的大小。您还可以选择性地分别对文本和文件调用 `count_tokens`。

另一种方法是调用 `generate_content`，然后使用 `response` 对象上的 `usage_metadata` 属性来获取以下信息：

- 输入 (`prompt_token_count`)、缓存内容 (`cached_content_token_count`) 和输出 (`candidates_token_count`) 的单独 token 数
- 思考过程的 token 数 (`thoughts_token_count`)
- *输入和输出*中的 token 总数 (`total_token_count`)

使用 File API 上传的图片的示例：

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

以内嵌数据形式提供图片的示例：

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.5-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### 视频或音频文件

音频和视频会分别按以下固定费率转换为 token：

- 视频：每秒 263 个 token
- 音频：每秒 32 个 token

如果您使用文本和视频/音频输入调用 `count_tokens`，它会返回*输入中*文本和视频/音频文件的总令牌数 (`total_tokens`)。您可以在调用 `generate_content` 之前进行此调用，以检查请求的大小。您还可以选择分别对文本和文件调用 `count_tokens`。

另一种方法是调用 `generate_content`，然后使用 `response` 对象上的 `usage_metadata` 属性来获取以下信息：

- 输入 (`prompt_token_count`)、缓存内容 (`cached_content_token_count`) 和输出 (`candidates_token_count`) 的单独 token 数
- 思考过程的 token 数 (`thoughts_token_count`)
- *输入和输出*中的 token 总数 (`total_token_count`)。

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
        model="gemini-3.5-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_file]
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
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

### 统计思考 token 数

开启思考功能后，回答价格是输出 token 和思考 token 的总和。您可以从 `thoughtsTokenCount` 字段（或 SDK 等效字段）检索生成的思考 token 总数。

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

思考模型会生成完整的想法，以提高最终回答的质量，然后输出[摘要](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#summaries)，以便深入了解思考过程。因此，即使 API 仅输出摘要，也会根据模型为创建摘要而生成的完整思路令牌来确定价格。

如需详细了解如何配置思考，请参阅 [Gemini 思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)指南。

## 上下文窗口

通过 Gemini API 提供的模型具有以 token 衡量的上下文窗口。上下文窗口定义了您可以提供的输入量以及模型可以生成的输出量。您可以通过调用 [`models.get` 端点](https://ai.google.dev/api/rest/v1/models/get?hl=zh-cn)或查看[模型文档](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)来确定上下文窗口的大小。

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.5-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.5-flash'});
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
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.5-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-24。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-24。"],[],[]]
