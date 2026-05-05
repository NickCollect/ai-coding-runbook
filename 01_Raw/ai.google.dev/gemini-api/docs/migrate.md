---
source_url: https://ai.google.dev/gemini-api/docs/migrate?hl=ko
fetched_at: 2026-05-05T13:13:21.132397+00:00
title: "Google GenAI SDK\ub85c \uc774\uc804 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

- [홈](https://ai.google.dev/gemini-api/docs/홈)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [문서](https://ai.google.dev/gemini-api/docs/문서)

의견 보내기

# Google GenAI SDK로 이전

2024년 말에 출시된 Gemini 2.0부터 [Google 생성형 AI SDK](https://ai.google.dev/gemini-api/docs/Google 생성형 AI SDK)라는 새로운 라이브러리 세트가 도입되었습니다. [업데이트된 클라이언트 아키텍처](https://ai.google.dev/gemini-api/docs/업데이트된 클라이언트 아키텍처)를 통해 개발자 환경을 개선하고 개발자와 엔터프라이즈 워크플로 간의 [전환을 간소화](https://ai.google.dev/gemini-api/docs/전환을 간소화)합니다.

이제 지원되는 모든 플랫폼에서 Google GenAI SDK가 [정식 버전 (GA)](https://ai.google.dev/gemini-api/docs/정식 버전 (GA))으로 제공됩니다. Google의 [기존 라이브러리](https://ai.google.dev/gemini-api/docs/기존 라이브러리) 중 하나를 사용하고 있다면 이전하는 것이 좋습니다.

이 가이드에서는 마이그레이션된 코드의 전후 예시를 제공하여 시작하는 데 도움을 드립니다.

## 설치

**전**

### Python

```
pip install -U -q "google-generativeai"
```

### 자바스크립트

```
npm install @google/generative-ai
```

### Go

```
go get github.com/google/generative-ai-go
```

**후**

### Python

```
pip install -U -q "google-genai"
```

### 자바스크립트

```
npm install @google/genai
```

### Go

```
go get google.golang.org/genai
```

## API 액세스

이전 SDK는 다양한 임시 방법을 사용하여 백그라운드에서 API 클라이언트를 암시적으로 처리했습니다. 이로 인해 클라이언트와 사용자 인증 정보를 관리하기가 어려웠습니다.
이제 중앙 `Client` 객체를 통해 상호작용합니다. 이 `Client` 객체는 다양한 API 서비스 (예: `models`, `chats`, `files`, `tunings`)의 단일 진입점 역할을 하여 일관성을 촉진하고 다양한 API 호출 전반에서 사용자 인증 정보 및 구성 관리를 간소화합니다.

**이전 (중앙화되지 않은 API 액세스)**

### Python

이전 SDK는 대부분의 API 호출에 최상위 클라이언트 객체를 명시적으로 사용하지 않았습니다. `GenerativeModel` 객체를 직접 인스턴스화하고 상호작용합니다.

```
import google.generativeai as genai

# Directly create and use model objects
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(...)
chat = model.start_chat(...)
```

### 자바스크립트

`GoogleGenerativeAI`는 모델과 채팅의 중심이었지만 파일 및 캐시 관리와 같은 다른 기능에는 완전히 별도의 클라이언트 클래스를 가져오고 인스턴스화해야 하는 경우가 많았습니다.

```
import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager, GoogleAICacheManager } from "@google/generative-ai/server"; // For files/caching

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");
const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");

// Get a model instance, then call methods on it
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
const result = await model.generateContent(...);
const chat = model.startChat(...);

// Call methods on separate client objects for other services
const uploadedFile = await fileManager.uploadFile(...);
const cache = await cacheManager.create(...);
```

### Go

`genai.NewClient` 함수는 클라이언트를 만들었지만 생성형 모델 작업은 일반적으로 이 클라이언트에서 가져온 별도의 `GenerativeModel` 인스턴스에서 호출되었습니다. 다른 서비스는 별도의 패키지나 패턴을 통해 액세스했을 수 있습니다.

```
import (
      "github.com/google/generative-ai-go/genai"
      "github.com/google/generative-ai-go/genai/fileman" // For files
      "google.golang.org/api/option"
)

client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
fileClient, err := fileman.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))

// Get a model instance, then call methods on it
model := client.GenerativeModel("gemini-2.0-flash")
resp, err := model.GenerateContent(...)
cs := model.StartChat()

// Call methods on separate client objects for other services
uploadedFile, err := fileClient.UploadFile(...)
```

**After (중앙 집중식 클라이언트 객체)**

### Python

```
from google import genai

# Create a single client object
client = genai.Client()

# Access API methods through services on the client object
response = client.models.generate_content(...)
chat = client.chats.create(...)
my_file = client.files.upload(...)
tuning_job = client.tunings.tune(...)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

// Create a single client object
const ai = new GoogleGenAI({apiKey: "GEMINI_API_KEY"});

// Access API methods through services on the client object
const response = await ai.models.generateContent(...);
const chat = ai.chats.create(...);
const uploadedFile = await ai.files.upload(...);
const cache = await ai.caches.create(...);
```

### Go

```
import "google.golang.org/genai"

// Create a single client object
client, err := genai.NewClient(ctx, nil)

// Access API methods through services on the client object
result, err := client.Models.GenerateContent(...)
chat, err := client.Chats.Create(...)
uploadedFile, err := client.Files.Upload(...)
tuningJob, err := client.Tunings.Tune(...)
```

## 인증

기존 라이브러리와 새 라이브러리 모두 API 키를 사용하여 인증합니다. Google AI Studio에서 API 키를 [만들 수](https://ai.google.dev/gemini-api/docs/만들 수) 있습니다.

**전**

### Python

이전 SDK는 API 클라이언트 객체를 암시적으로 처리했습니다.

```
import google.generativeai as genai

genai.configure(api_key=...)
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
```

### Go

Google 라이브러리를 가져옵니다.

```
import (
      "github.com/google/generative-ai-go/genai"
      "google.golang.org/api/option"
)
```

클라이언트를 만듭니다.

```
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
```

**후**

### Python

Google GenAI SDK를 사용하면 먼저 API를 호출하는 데 사용되는 API 클라이언트를 만듭니다.
클라이언트에 API 키를 전달하지 않으면 새 SDK가 `GEMINI_API_KEY` 환경 변수에서 API 키를 가져옵니다.

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

```
from google import genai

client = genai.Client() # Set the API key using the GEMINI_API_KEY env var.
                        # Alternatively, you could set the API key explicitly:
                        # client = genai.Client(api_key="YOUR_API_KEY")
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({apiKey: "GEMINI_API_KEY"});
```

### Go

생성형 AI 라이브러리를 가져옵니다.

```
import "google.golang.org/genai"
```

클라이언트를 만듭니다.

```
client, err := genai.NewClient(ctx, &genai.ClientConfig{
        Backend:  genai.BackendGeminiAPI,
})
```

## 콘텐츠 생성

### 텍스트

**전**

### Python

이전에는 클라이언트 객체가 없었고 `GenerativeModel` 객체를 통해 API에 직접 액세스했습니다.

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(
    'Tell me a story in 300 words'
)
print(response.text)
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });
const prompt = "Tell me a story in 300 words";

const result = await model.generateContent(prompt);
console.log(result.response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
resp, err := model.GenerateContent(ctx, genai.Text("Tell me a story in 300 words."))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response parts
```

**후**

### Python

새 Google GenAI SDK는 `Client` 객체를 통해 모든 API 메서드에 대한 액세스를 제공합니다. 몇 가지 상태 저장 특수 사례 (`chat` 및 라이브 API `session`)를 제외하고는 모두 상태 비저장 함수입니다. 유틸리티와 일관성을 위해 반환되는 객체는 `pydantic` 클래스입니다.

```
from google import genai
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='Tell me a story in 300 words.'
)
print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: "Tell me a story in 300 words.",
});
console.log(response.text);
```

### Go

```
ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx, "gemini-2.0-flash", genai.Text("Tell me a story in 300 words."), nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### 이미지

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content([
    'Tell me a story based on this image',
    Image.open(image_path)
])
print(response.text)
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

function fileToGenerativePart(path, mimeType) {
  return {
    inlineData: {
      data: Buffer.from(fs.readFileSync(path)).toString("base64"),
      mimeType,
    },
  };
}

const prompt = "Tell me a story based on this image";

const imagePart = fileToGenerativePart(
  `path/to/organ.jpg`,
  "image/jpeg",
);

const result = await model.generateContent([prompt, imagePart]);
console.log(result.response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")

imgData, err := os.ReadFile("path/to/organ.jpg")
if err != nil {
    log.Fatal(err)
}

resp, err := model.GenerateContent(ctx,
    genai.Text("Tell me about this instrument"),
    genai.ImageData("jpeg", imgData))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response
```

**후**

### Python

새 SDK에는 동일한 편의 기능이 많이 있습니다. 예를 들어 `PIL.Image` 객체는 자동으로 변환됩니다.

```
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        'Tell me a story based on this image',
        Image.open(image_path)
    ]
)
print(response.text)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const organ = await ai.files.upload({
  file: "path/to/organ.jpg",
});

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: [
    createUserContent([
      "Tell me a story based on this image",
      createPartFromUri(organ.uri, organ.mimeType)
    ]),
  ],
});
console.log(response.text);
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

imgData, err := os.ReadFile("path/to/organ.jpg")
if err != nil {
    log.Fatal(err)
}

parts := []*genai.Part{
    {Text: "Tell me a story based on this image"},
    {InlineData: &genai.Blob{Data: imgData, MIMEType: "image/jpeg"}},
}
contents := []*genai.Content{
    {Parts: parts},
}

result, err := client.Models.GenerateContent(ctx, "gemini-2.0-flash", contents, nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### 스트리밍

**전**

### Python

```
import google.generativeai as genai

response = model.generate_content(
    "Write a cute story about cats.",
    stream=True)
for chunk in response:
    print(chunk.text)
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

const prompt = "Write a story about a magic backpack.";

const result = await model.generateContentStream(prompt);

// Print text as it comes in.
for await (const chunk of result.stream) {
  const chunkText = chunk.text();
  process.stdout.write(chunkText);
}
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
iter := model.GenerateContentStream(ctx, genai.Text("Write a story about a magic backpack."))
for {
    resp, err := iter.Next()
    if err == iterator.Done {
        break
    }
    if err != nil {
        log.Fatal(err)
    }
    printResponse(resp) // utility for printing the response
}
```

**후**

### Python

```
from google import genai

client = genai.Client()

for chunk in client.models.generate_content_stream(
  model='gemini-2.0-flash',
  contents='Tell me a story in 300 words.'
):
    print(chunk.text)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContentStream({
  model: "gemini-2.0-flash",
  contents: "Write a story about a magic backpack.",
});
let text = "";
for await (const chunk of response) {
  console.log(chunk.text);
  text += chunk.text;
}
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

for result, err := range client.Models.GenerateContentStream(
    ctx,
    "gemini-2.0-flash",
    genai.Text("Write a story about a magic backpack."),
    nil,
) {
    if err != nil {
        log.Fatal(err)
    }
    fmt.Print(result.Candidates[0].Content.Parts[0].Text)
}
```

## 구성

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
  'gemini-2.0-flash',
    system_instruction='you are a story teller for kids under 5 years old',
    generation_config=genai.GenerationConfig(
      max_output_tokens=400,
      top_k=2,
      top_p=0.5,
      temperature=0.5,
      response_mime_type='application/json',
      stop_sequences=['\n'],
    )
)
response = model.generate_content('tell me a story in 100 words')
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  generationConfig: {
    candidateCount: 1,
    stopSequences: ["x"],
    maxOutputTokens: 20,
    temperature: 1.0,
  },
});

const result = await model.generateContent(
  "Tell me a story about a magic backpack.",
);
console.log(result.response.text())
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
model.SetTemperature(0.5)
model.SetTopP(0.5)
model.SetTopK(2.0)
model.SetMaxOutputTokens(100)
model.ResponseMIMEType = "application/json"
resp, err := model.GenerateContent(ctx, genai.Text("Tell me about New York"))
if err != nil {
    log.Fatal(err)
}
printResponse(resp) // utility for printing response
```

**후**

### Python

새 SDK의 모든 메서드에서 필수 인수는 키워드 인수로 제공됩니다. 모든 선택적 입력은 `config` 인수에 제공됩니다. 구성 인수는 `google.genai.types` 네임스페이스의 Python 사전 또는 `Config` 클래스로 지정할 수 있습니다. 유틸리티와 균일성을 위해 `types` 모듈 내의 모든 정의는 `pydantic` 클래스입니다.

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='Tell me a story in 100 words.',
  config=types.GenerateContentConfig(
      system_instruction='you are a story teller for kids under 5 years old',
      max_output_tokens= 400,
      top_k= 2,
      top_p= 0.5,
      temperature= 0.5,
      response_mime_type= 'application/json',
      stop_sequences= ['\n'],
      seed=42,
  ),
)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: "Tell me a story about a magic backpack.",
  config: {
    candidateCount: 1,
    stopSequences: ["x"],
    maxOutputTokens: 20,
    temperature: 1.0,
  },
});

console.log(response.text);
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx,
    "gemini-2.0-flash",
    genai.Text("Tell me about New York"),
    &genai.GenerateContentConfig{
        Temperature:      genai.Ptr[float32](https://ai.google.dev/gemini-api/docs/float32),
        TopP:             genai.Ptr[float32](https://ai.google.dev/gemini-api/docs/float32),
        TopK:             genai.Ptr[float32](https://ai.google.dev/gemini-api/docs/float32),
        ResponseMIMEType: "application/json",
        StopSequences:    []string{"Yankees"},
        CandidateCount:   2,
        Seed:             genai.Ptr[int32](https://ai.google.dev/gemini-api/docs/int32),
        MaxOutputTokens:  128,
        PresencePenalty:  genai.Ptr[float32](https://ai.google.dev/gemini-api/docs/float32),
        FrequencyPenalty: genai.Ptr[float32](https://ai.google.dev/gemini-api/docs/float32),
    },
)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing response
```

## 안전 설정

안전 설정으로 대답을 생성합니다.

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(
    'say something bad',
    safety_settings={
        'HATE': 'BLOCK_ONLY_HIGH',
        'HARASSMENT': 'BLOCK_ONLY_HIGH',
  }
)
```

### 자바스크립트

```
import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  safetySettings: [
    {
      category: HarmCategory.HARM_CATEGORY_HARASSMENT,
      threshold: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    },
  ],
});

const unsafePrompt =
  "I support Martians Soccer Club and I think " +
  "Jupiterians Football Club sucks! Write an ironic phrase telling " +
  "them how I feel about them.";

const result = await model.generateContent(unsafePrompt);

try {
  result.response.text();
} catch (e) {
  console.error(e);
  console.log(result.response.candidates[0].safetyRatings);
}
```

**후**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='say something bad',
  config=types.GenerateContentConfig(
      safety_settings= [
          types.SafetySetting(
              category='HARM_CATEGORY_HATE_SPEECH',
              threshold='BLOCK_ONLY_HIGH'
          ),
      ]
  ),
)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const unsafePrompt =
  "I support Martians Soccer Club and I think " +
  "Jupiterians Football Club sucks! Write an ironic phrase telling " +
  "them how I feel about them.";

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: unsafePrompt,
  config: {
    safetySettings: [
      {
        category: "HARM_CATEGORY_HARASSMENT",
        threshold: "BLOCK_ONLY_HIGH",
      },
    ],
  },
});

console.log("Finish reason:", response.candidates[0].finishReason);
console.log("Safety ratings:", response.candidates[0].safetyRatings);
```

## 비동기식

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content_async(
    'tell me a story in 100 words'
)
```

**후**

### Python

`asyncio`와 함께 새 SDK를 사용하려면 `client.aio` 아래의 모든 메서드에 별도의 `async` 구현이 있어야 합니다.

```
from google import genai

client = genai.Client()

response = await client.aio.models.generate_content(
    model='gemini-2.0-flash',
    contents='Tell me a story in 300 words.'
)
```

## 채팅

채팅을 시작하고 모델에 메시지를 보냅니다.

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat()

response = chat.send_message(
    "Tell me a story in 100 words")
response = chat.send_message(
    "What happened after that?")
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });
const chat = model.startChat({
  history: [
    {
      role: "user",
      parts: [{ text: "Hello" }],
    },
    {
      role: "model",
      parts: [{ text: "Great to meet you. What would you like to know?" }],
    },
  ],
});
let result = await chat.sendMessage("I have 2 dogs in my house.");
console.log(result.response.text());
result = await chat.sendMessage("How many paws are in my house?");
console.log(result.response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
cs := model.StartChat()

cs.History = []*genai.Content{
    {
        Parts: []genai.Part{
            genai.Text("Hello, I have 2 dogs in my house."),
        },
        Role: "user",
    },
    {
        Parts: []genai.Part{
            genai.Text("Great to meet you. What would you like to know?"),
        },
        Role: "model",
    },
}

res, err := cs.SendMessage(ctx, genai.Text("How many paws are in my house?"))
if err != nil {
    log.Fatal(err)
}
printResponse(res) // utility for printing the response
```

**후**

### Python

```
from google import genai

client = genai.Client()

chat = client.chats.create(model='gemini-2.0-flash')

response = chat.send_message(
    message='Tell me a story in 100 words')
response = chat.send_message(
    message='What happened after that?')
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const chat = ai.chats.create({
  model: "gemini-2.0-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "Hello" }],
    },
    {
      role: "model",
      parts: [{ text: "Great to meet you. What would you like to know?" }],
    },
  ],
});

const response1 = await chat.sendMessage({
  message: "I have 2 dogs in my house.",
});
console.log("Chat response 1:", response1.text);

const response2 = await chat.sendMessage({
  message: "How many paws are in my house?",
});
console.log("Chat response 2:", response2.text);
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

chat, err := client.Chats.Create(ctx, "gemini-2.0-flash", nil, nil)
if err != nil {
    log.Fatal(err)
}

result, err := chat.SendMessage(ctx, genai.Part{Text: "Hello, I have 2 dogs in my house."})
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result

result, err = chat.SendMessage(ctx, genai.Part{Text: "How many paws are in my house?"})
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

## 함수 호출

**전**

### Python

```
import google.generativeai as genai
from enum import Enum

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools=[get_current_weather]
)

response = model.generate_content("What is the weather in San Francisco?")
function_call = response.candidates[0].parts[0].function_call
```

**후**

### Python

새 SDK에서는 자동 함수 호출이 기본값입니다. 여기에서 사용 중지합니다.

```
from google import genai
from google.genai import types

client = genai.Client()

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather],
      automatic_function_calling={'disable': True},
  ),
)

function_call = response.candidates[0].content.parts[0].function_call
```

### 자동 함수 호출

**전**

### Python

이전 SDK는 채팅에서만 자동 함수 호출을 지원합니다. 새 SDK에서는 `generate_content`의 기본 동작입니다.

```
import google.generativeai as genai

def get_current_weather(city: str) -> str:
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools=[get_current_weather]
)

chat = model.start_chat(
    enable_automatic_function_calling=True)
result = chat.send_message("What is the weather in San Francisco?")
```

**후**

### Python

```
from google import genai
from google.genai import types
client = genai.Client()

def get_current_weather(city: str) -> str:
    return "23C"

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather]
  ),
)
```

## 코드 실행

코드 실행은 모델이 Python 코드를 생성하고 실행하며 결과를 반환할 수 있는 도구입니다.

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools="code_execution"
)

result = model.generate_content(
  "What is the sum of the first 50 prime numbers? Generate and run code for "
  "the calculation, and make sure you get all 50.")
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  tools: [{ codeExecution: {} }],
});

const result = await model.generateContent(
  "What is the sum of the first 50 prime numbers? " +
    "Generate and run code for the calculation, and make sure you get " +
    "all 50.",
);

console.log(result.response.text());
```

**후**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='What is the sum of the first 50 prime numbers? Generate and run '
            'code for the calculation, and make sure you get all 50.',
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    ),
)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: `Write and execute code that calculates the sum of the first 50 prime numbers.
            Ensure that only the executable code and its resulting output are generated.`,
});

// Each part may contain text, executable code, or an execution result.
for (const part of response.candidates[0].content.parts) {
  console.log(part);
  console.log("\n");
}

console.log("-".repeat(80));
// The `.text` accessor concatenates the parts into a markdown-formatted text.
console.log("\n", response.text);
```

## 검색 그라운딩

`GoogleSearch` (Gemini 2.0 이상) 및 `GoogleSearchRetrieval` (Gemini 2.0 미만)은 모델이 그라운딩을 위해 공개 웹 데이터를 검색할 수 있도록 지원하는 도구이며 Google에서 제공합니다.

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(
    contents="what is the Google stock price?",
    tools='google_search_retrieval'
)
```

**후**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='What is the Google stock price?',
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch()
            )
        ]
    )
)
```

## JSON 응답

JSON 형식으로 답변을 생성합니다.

**전**

### Python

`response_schema`를 지정하고 `response_mime_type="application/json"`를 설정하면 사용자가 모델이 지정된 구조에 따라 `JSON` 응답을 생성하도록 제한할 수 있습니다.

```
import google.generativeai as genai
import typing_extensions as typing

class CountryInfo(typing.TypedDict):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
result = model.generate_content(
    "Give me information of the United States",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema = CountryInfo
    ),
)
```

### 자바스크립트

```
import { GoogleGenerativeAI, SchemaType } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");

const schema = {
  description: "List of recipes",
  type: SchemaType.ARRAY,
  items: {
    type: SchemaType.OBJECT,
    properties: {
      recipeName: {
        type: SchemaType.STRING,
        description: "Name of the recipe",
        nullable: false,
      },
    },
    required: ["recipeName"],
  },
};

const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  generationConfig: {
    responseMimeType: "application/json",
    responseSchema: schema,
  },
});

const result = await model.generateContent(
  "List a few popular cookie recipes.",
);
console.log(result.response.text());
```

**후**

### Python

새 SDK는 `pydantic` 클래스를 사용하여 스키마를 제공합니다 (`genai.types.Schema` 또는 이에 상응하는 `dict`를 전달할 수 있음). 가능하면 SDK가 반환된 JSON을 파싱하고 결과를 `response.parsed`로 반환합니다. `pydantic` 클래스를 스키마로 제공한 경우 SDK는 해당 `JSON`을 클래스의 인스턴스로 변환합니다.

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='Give me information of the United States.',
    config={
        'response_mime_type': 'application/json',
        'response_schema': CountryInfo,
    },
)

response.parsed
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: "List a few popular cookie recipes.",
  config: {
    responseMimeType: "application/json",
    responseSchema: {
      type: "array",
      items: {
        type: "object",
        properties: {
          recipeName: { type: "string" },
          ingredients: { type: "array", items: { type: "string" } },
        },
        required: ["recipeName", "ingredients"],
      },
    },
  },
});
console.log(response.text);
```

## 파일

### 업로드

파일 업로드:

**전**

### Python

```
import requests
import pathlib
import google.generativeai as genai

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

file = genai.upload_file(path='a11.txt')

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content([
    'Can you summarize this file:',
    my_file
])
print(response.text)
```

**후**

### Python

```
import requests
import pathlib
from google import genai

client = genai.Client()

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

my_file = client.files.upload(file='a11.txt')

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        'Can you summarize this file:',
        my_file
    ]
)
print(response.text)
```

### 목록 및 가져오기

업로드된 파일을 나열하고 파일 이름으로 업로드된 파일을 가져옵니다.

**전**

### Python

```
import google.generativeai as genai

for file in genai.list_files():
  print(file.name)

file = genai.get_file(name=file.name)
```

**후**

### Python

```
from google import genai
client = genai.Client()

for file in client.files.list():
    print(file.name)

file = client.files.get(name=file.name)
```

### 삭제

파일을 삭제합니다.

**전**

### Python

```
import pathlib
import google.generativeai as genai

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = genai.upload_file(path='dummy.txt')

file = genai.delete_file(name=dummy_file.name)
```

**후**

### Python

```
import pathlib
from google import genai

client = genai.Client()

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = client.files.upload(file='dummy.txt')

response = client.files.delete(name=dummy_file.name)
```

## 컨텍스트 캐싱이

컨텍스트 캐싱을 사용하면 사용자가 콘텐츠를 모델에 한 번 전달하고 입력 토큰을 캐시한 다음 후속 호출에서 캐시된 토큰을 참조하여 비용을 낮출 수 있습니다.

**전**

### Python

```
import requests
import pathlib
import google.generativeai as genai
from google.generativeai import caching

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

# Upload file
document = genai.upload_file(path="a11.txt")

# Create cache
apollo_cache = caching.CachedContent.create(
    model="gemini-2.0-flash-001",
    system_instruction="You are an expert at analyzing transcripts.",
    contents=[document],
)

# Generate response
apollo_model = genai.GenerativeModel.from_cached_content(
    cached_content=apollo_cache
)
response = apollo_model.generate_content("Find a lighthearted moment from this transcript")
```

### 자바스크립트

```
import { GoogleAICacheManager, GoogleAIFileManager } from "@google/generative-ai/server";
import { GoogleGenerativeAI } from "@google/generative-ai";

const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");

const uploadResult = await fileManager.uploadFile("path/to/a11.txt", {
  mimeType: "text/plain",
});

const cacheResult = await cacheManager.create({
  model: "models/gemini-2.0-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: uploadResult.file.uri,
            mimeType: uploadResult.file.mimeType,
          },
        },
      ],
    },
  ],
});

console.log(cacheResult);

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModelFromCachedContent(cacheResult);
const result = await model.generateContent(
  "Please summarize this transcript.",
);
console.log(result.response.text());
```

**후**

### Python

```
import requests
import pathlib
from google import genai
from google.genai import types

client = genai.Client()

# Check which models support caching.
for m in client.models.list():
  for action in m.supported_actions:
    if action == "createCachedContent":
      print(m.name)
      break

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

# Upload file
document = client.files.upload(file='a11.txt')

# Create cache
model='gemini-2.0-flash-001'
apollo_cache = client.caches.create(
      model=model,
      config={
          'contents': [document],
          'system_instruction': 'You are an expert at analyzing transcripts.',
      },
  )

# Generate response
response = client.models.generate_content(
    model=model,
    contents='Find a lighthearted moment from this transcript',
    config=types.GenerateContentConfig(
        cached_content=apollo_cache.name,
    )
)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-2.0-flash";

const contents = [
  createUserContent(createPartFromUri(document.uri, document.mimeType)),
];

const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});
console.log("Cache created:", cache);

const response = await ai.models.generateContent({
  model: modelName,
  contents: "Please summarize this transcript",
  config: { cachedContent: cache.name },
});
console.log("Response text:", response.text);
```

## 토큰 집계

요청의 토큰 수를 계산합니다.

**전**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.count_tokens(
    'The quick brown fox jumps over the lazy dog.')
```

### 자바스크립트

```
 import { GoogleGenerativeAI } from "@google/generative-ai";

 const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
 const model = genAI.getGenerativeModel({
   model: "gemini-2.0-flash",
 });

 // Count tokens in a prompt without calling text generation.
 const countResult = await model.countTokens(
   "The quick brown fox jumps over the lazy dog.",
 );

 console.log(countResult.totalTokens); // 11

 const generateResult = await model.generateContent(
   "The quick brown fox jumps over the lazy dog.",
 );

 // On the response for `generateContent`, use `usageMetadata`
 // to get separate input and output token counts
 // (`promptTokenCount` and `candidatesTokenCount`, respectively),
 // as well as the combined token count (`totalTokenCount`).
 console.log(generateResult.response.usageMetadata);
 // candidatesTokenCount and totalTokenCount depend on response, may vary
 // { promptTokenCount: 11, candidatesTokenCount: 124, totalTokenCount: 135 }
```

**후**

### Python

```
from google import genai

client = genai.Client()

response = client.models.count_tokens(
    model='gemini-2.0-flash',
    contents='The quick brown fox jumps over the lazy dog.',
)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const prompt = "The quick brown fox jumps over the lazy dog.";
const countTokensResponse = await ai.models.countTokens({
  model: "gemini-2.0-flash",
  contents: prompt,
});
console.log(countTokensResponse.totalTokens);

const generateResponse = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: prompt,
});
console.log(generateResponse.usageMetadata);
```

## 이미지 생성

이미지 생성:

**전**

### Python

```
#pip install https://github.com/google-gemini/generative-ai-python@imagen
import google.generativeai as genai

imagen = genai.ImageGenerationModel(
    "imagen-3.0-generate-001")
gen_images = imagen.generate_images(
    prompt="Robot holding a red skateboard",
    number_of_images=1,
    safety_filter_level="block_low_and_above",
    person_generation="allow_adult",
    aspect_ratio="3:4",
)
```

**후**

### Python

```
from google import genai

client = genai.Client()

gen_images = client.models.generate_images(
    model='gemini-2.5-flash-image',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 1,
        safety_filter_level= "BLOCK_LOW_AND_ABOVE",
        person_generation= "ALLOW_ADULT",
        aspect_ratio= "3:4",
    )
)

for n, image in enumerate(gen_images.generated_images):
    pathlib.Path(f'{n}.png').write_bytes(
        image.image.image_bytes)
```

## 콘텐츠 삽입

콘텐츠 임베딩을 생성합니다.

**전**

### Python

```
import google.generativeai as genai

response = genai.embed_content(
  model='models/gemini-embedding-001',
  content='Hello world'
)
```

### 자바스크립트

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-embedding-001",
});

const result = await model.embedContent("Hello world!");

console.log(result.embedding);
```

**후**

### Python

```
from google import genai

client = genai.Client()

response = client.models.embed_content(
  model='gemini-embedding-001',
  contents='Hello world',
)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const text = "Hello World!";
const result = await ai.models.embedContent({
  model: "gemini-embedding-001",
  contents: text,
  config: { outputDimensionality: 10 },
});
console.log(result.embeddings);
```

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0 라이선스)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://ai.google.dev/gemini-api/docs/Apache 2.0 라이선스)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://ai.google.dev/gemini-api/docs/Google Developers 사이트 정책)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?
