---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=ko
fetched_at: 2026-05-05T19:49:05.356786+00:00
title: "\ud1a0\ud070 \uc774\ud574 \ubc0f \uacc4\uc0b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 토큰 이해 및 계산

Gemini 및 기타 생성형 AI 모델은 *토큰*이라는 세분성으로 입력과 출력을 처리합니다.

**Gemini 모델의 경우 토큰은 약 4자에 해당합니다.
토큰 100개는 영어 단어 약 60~80개에 해당합니다.**

## 토큰 정보

토큰은 단일 문자(예: `z`) 또는 전체 단어(예: `cat`)일 수 있습니다. 긴 단어는 여러 토큰으로 나뉩니다. 모델에서 사용하는 모든 토큰 집합을 어휘라고 하며, 텍스트를 토큰으로 분할하는 프로세스를 *토큰화*라고 합니다.

결제가 사용 설정된 경우 [Gemini API 호출 비용](https://ai.google.dev/pricing?hl=ko)은 입력 및 출력 토큰 수에 따라 결정되므로 토큰 수를 세는 방법을 알아두면 유용합니다.

Colab에서 토큰 수를 세어 볼 수 있습니다.

|  |  |  |
| --- | --- | --- |
| [ai.google.dev에서 보기](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | [Colab 노트북 사용해 보기](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=ko) | [GitHub에서 노트북 보기](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=ko) |

## 토큰 집계

텍스트, 이미지 파일, 기타 비텍스트 모달리티를 비롯한 Gemini API의 모든 입력과 출력은 토큰화됩니다.

다음과 같은 방법으로 토큰을 계산할 수 있습니다.

- **요청의 입력으로 [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=ko)를 호출합니다.**  
   *입력만*의 총 토큰 수를 반환합니다. 모델에 입력을 보내기 전에 이 호출을 실행하여 요청의 크기를 확인할 수 있습니다.
- **`generate_content`를 호출한 후 `response` 객체에서 `usage_metadata` 속성을 사용합니다.**  
   *입력과 출력 모두*의 총 토큰 수를 반환합니다(`total_token_count`).  
   또한 입력 및 출력의 토큰 수를 별도로 반환합니다. `prompt_token_count` (입력 토큰) 및 `candidates_token_count`(출력 토큰)

  [사고 모델](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)을 사용하는 경우 사고 과정에서 사용된 토큰이 `thoughts_token_count`에 반환됩니다. [컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)을 사용하는 경우 캐시된 토큰 수는 `cached_content_token_count`에 표시됩니다.

### 텍스트 토큰 수 계산

텍스트 전용 입력으로 `count_tokens`를 호출하면 *입력만* (`total_tokens`)의 텍스트 토큰 수가 반환됩니다. `generate_content`를 호출하기 전에 이 호출을 실행하여 요청의 크기를 확인할 수 있습니다.

또 다른 방법은 `generate_content`을 호출한 다음 `response` 객체에서 `usage_metadata` 속성을 사용하여 다음을 가져오는 것입니다.

- 입력 (`prompt_token_count`), 캐시된 콘텐츠 (`cached_content_token_count`), 출력(`candidates_token_count`)의 별도 토큰 수
- 사고 과정의 토큰 수 (`thoughts_token_count`)
- *입력과 출력 모두*의 총 토큰 수(`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=prompt
)

print(response.usage_metadata)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
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
countResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
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

### 멀티턴 (채팅) 토큰 수 계산

채팅 기록과 함께 `count_tokens`를 호출하면 채팅의 각 역할 (`total_tokens`)에서 텍스트의 총 토큰 수가 반환됩니다.

또 다른 방법은 `send_message`을 호출한 다음 `response` 객체에서 `usage_metadata` 속성을 사용하여 다음을 가져오는 것입니다.

- 입력 (`prompt_token_count`), 캐시된 콘텐츠 (`cached_content_token_count`), 출력(`candidates_token_count`)의 별도 토큰 수
- 사고 과정의 토큰 수 (`thoughts_token_count`)
- *입력과 출력 모두*의 총 토큰 수(`total_token_count`)

다음 대화 턴의 크기를 파악하려면 `count_tokens`를 호출할 때 기록에 추가해야 합니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3-flash-preview",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3-flash-preview", contents=chat.get_history()
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
print(client.models.count_tokens(model="gemini-3-flash-preview", contents=history))
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    { role: "user", parts: [{ text: "Hi my name is Bob" }] },
    { role: "model", parts: [{ text: "Hi Bob!" }] },
  ];
  const chat = ai.chats.create({
    model: "gemini-3-flash-preview",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
chat, err := client.Chats.Create(ctx, "gemini-3-flash-preview", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", chat.History(false), nil)
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

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### 멀티모달 토큰 수 계산

텍스트, 이미지 파일, 기타 텍스트가 아닌 모달리티를 비롯한 Gemini API의 모든 입력은 토큰화됩니다. Gemini API에서 처리하는 동안 멀티모달 입력의 토큰화에 관한 다음 상위 수준 주요 사항에 유의하세요.

- 두 치수가 모두 384픽셀 이하인 이미지 입력은 258개의 토큰으로 계산됩니다. 한쪽 또는 양쪽 크기가 더 큰 이미지는 필요에 따라 768x768픽셀 타일로 잘리고 크기가 조정되며, 각 타일은 258개의 토큰으로 계산됩니다.
- 동영상 및 오디오 파일은 다음 고정 요율로 토큰으로 변환됩니다. 동영상은 초당 263개 토큰, 오디오는 초당 32개 토큰입니다.

#### 미디어 해상도

[Gemini 3 모델](https://ai.google.dev/gemini-api/docs/models?hl=ko#gemini-3)은 `media_resolution` 파라미터를 통해 멀티모달 비전 처리에 대한 세밀한 제어 기능을 제공합니다. `media_resolution` 파라미터는 **입력 이미지 또는 동영상 프레임당 할당되는 최대 토큰 수**를 결정합니다.
해상도가 높을수록 모델이 작은 텍스트를 읽거나 세부 요소를 식별하는 능력을 향상시키지만, 토큰 사용량과 지연 시간이 증가합니다.

파라미터 및 파라미터가 토큰 계산에 미치는 영향에 대한 자세한 내용은 [미디어 해상도](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ko) 가이드를 참고하세요.

#### 이미지 파일

텍스트와 이미지 입력으로 `count_tokens`를 호출하면 *입력만* (`total_tokens`)에 텍스트와 이미지의 결합된 토큰 수가 반환됩니다. `generate_content`를 호출하기 전에 이 호출을 실행하여 요청의 크기를 확인할 수 있습니다. 선택적으로 텍스트와 파일에서 각각 `count_tokens`을 호출할 수도 있습니다.

또 다른 방법은 `generate_content`을 호출한 다음 `response` 객체에서 `usage_metadata` 속성을 사용하여 다음을 가져오는 것입니다.

- 입력 (`prompt_token_count`), 캐시된 콘텐츠 (`cached_content_token_count`), 출력(`candidates_token_count`)의 별도 토큰 수
- 사고 과정의 토큰 수 (`thoughts_token_count`)
- *입력과 출력 모두*의 총 토큰 수(`total_token_count`)

File API에서 업로드된 이미지를 사용하는 예:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3-flash-preview", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### 자바스크립트

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
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

이미지를 인라인 데이터로 제공하는 예:

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3-flash-preview", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### 자바스크립트

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
    model: "gemini-3-flash-preview",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### 동영상 또는 오디오 파일

오디오와 동영상은 각각 다음 고정된 비율로 토큰으로 변환됩니다.

- 동영상: 초당 토큰 263개
- 오디오: 초당 토큰 32개

텍스트 및 동영상/오디오 입력으로 `count_tokens`를 호출하면 *입력만*(`total_tokens`)에 있는 텍스트와 동영상/오디오 파일의 결합된 토큰 수가 반환됩니다. `generate_content`를 호출하기 전에 이 호출을 실행하여 요청의 크기를 확인할 수 있습니다. 선택적으로 텍스트와 파일에서 `count_tokens`를 별도로 호출할 수도 있습니다.

또 다른 방법은 `generate_content`을 호출한 다음 `response` 객체에서 `usage_metadata` 속성을 사용하여 다음을 가져오는 것입니다.

- 입력 (`prompt_token_count`), 캐시된 콘텐츠 (`cached_content_token_count`), 출력(`candidates_token_count`)의 별도 토큰 수
- 사고 과정의 토큰 수 (`thoughts_token_count`)
- *입력과 출력 모두*의 총 토큰 수(`total_token_count`)입니다.

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
        model="gemini-3-flash-preview", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[prompt, your_file]
)
print(response.usage_metadata)
```

### 자바스크립트

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
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

## 컨텍스트 윈도우

Gemini API를 통해 사용할 수 있는 모델에는 토큰으로 측정되는 컨텍스트 윈도우가 있습니다. 컨텍스트 윈도우는 제공할 수 있는 입력의 양과 모델이 생성할 수 있는 출력의 양을 정의합니다. [`models.get` 엔드포인트](https://ai.google.dev/api/rest/v1/models/get?hl=ko)를 호출하거나 [모델 문서](https://ai.google.dev/gemini-api/docs/models?hl=ko)를 확인하여 컨텍스트 윈도우의 크기를 확인할 수 있습니다.

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3-flash-preview")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3-flash-preview'});
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
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3-flash-preview")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
