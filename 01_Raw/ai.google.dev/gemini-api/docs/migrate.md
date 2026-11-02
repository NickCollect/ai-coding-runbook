---
source_url: https://ai.google.dev/gemini-api/docs/migrate?hl=ru
fetched_at: 2026-11-02T07:23:28.552380+00:00
title: "\u041f\u0435\u0440\u0435\u0445\u043e\u0434 \u043d\u0430 Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Переход на Google GenAI SDK

В конце 2024 года мы выпустили Gemini 2.0 и представили новый набор библиотек – [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ru). Она предлагает разработчикам улучшенный опыт благодаря [обновленной клиентской архитектуре](https://ai.google.dev/gemini-api/docs/migrate?hl=ru#client) и [упрощает переход](https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=ru) между рабочими процессами разработчика и предприятия.

Google GenAI SDK теперь [общедоступен](https://ai.google.dev/gemini-api/docs/libraries?hl=ru#new-libraries) на всех поддерживаемых платформах. Если вы используете одну из наших [устаревших библиотек](https://ai.google.dev/gemini-api/docs/libraries?hl=ru#previous-sdks), мы настоятельно рекомендуем перейти на новую.

В этом руководстве приведены примеры кода до и после переноса, которые помогут вам начать работу.

## Установка

**До**

### Python

```
pip install -U -q "google-generativeai"
```

### JavaScript

```
npm install @google/generative-ai
```

### Проложить маршрут

```
go get github.com/google/generative-ai-go
```

### Java

```
<dependency>
    <groupId>com.google.ai.client.generativeai</groupId>
    <artifactId>generativeai</artifactId>
    <version>0.9.0</version>
</dependency>
```

**После**

### Python

```
pip install -U -q "google-genai"
```

### JavaScript

```
npm install @google/genai
```

### Проложить маршрут

```
go get google.golang.org/genai
```

### Java

```
<dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.67.0</version>
</dependency>
```

## Доступ через API

В старом SDK API-клиент обрабатывался неявно с помощью различных специальных методов. Это усложняло управление клиентом и учетными данными.
Теперь вы взаимодействуете с центральным объектом `Client`. Объект `Client` выступает в качестве единой точки входа для различных сервисов API (например, `models`, `chats`, `files`, `tunings`), обеспечивая согласованность и упрощая управление учетными данными и управление конфигурацией при разных вызовах API.

**Раньше (менее централизованный доступ к API)**

### Python

В старом SDK для большинства вызовов API не использовался объект клиента верхнего уровня. Вы будете напрямую создавать экземпляры объектов `GenerativeModel` и взаимодействовать с ними.

```
import google.generativeai as genai

# Directly create and use model objects
model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(...)
chat = model.start_chat(...)
```

### JavaScript

Хотя `GoogleGenerativeAI` был центральной точкой для моделей и чата, другие функции, такие как управление файлами и кешем, часто требовали импорта и создания экземпляров совершенно отдельных клиентских классов.

```
import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager, GoogleAICacheManager } from "@google/generative-ai/server"; // For files/caching

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");
const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");

// Get a model instance, then call methods on it
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });
const result = await model.generateContent(...);
const chat = model.startChat(...);

// Call methods on separate client objects for other services
const uploadedFile = await fileManager.uploadFile(...);
const cache = await cacheManager.create(...);
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

// Previously, model operations were called on separate model instances
Client client = new Client();
GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "Tell me a story.", null);
Chat chat = client.chats.create("gemini-3.8-flash");
```

### Проложить маршрут

Функция `genai.NewClient` создала клиента, но операции с генеративной моделью обычно вызывались в отдельном экземпляре `GenerativeModel`, полученном от этого клиента. Другие сервисы могли быть доступны через другие пакеты или шаблоны.

```
import (
      "github.com/google/generative-ai-go/genai"
      "github.com/google/generative-ai-go/genai/fileman" // For files
      "google.golang.org/api/option"
)

client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
fileClient, err := fileman.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))

// Get a model instance, then call methods on it
model := client.GenerativeModel("gemini-3.8-flash")
resp, err := model.GenerateContent(...)
cs := model.StartChat()

// Call methods on separate client objects for other services
uploadedFile, err := fileClient.UploadFile(...)
```

**После (централизованный объект клиента)**

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

### JavaScript

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

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.CachedContent;
import com.google.genai.types.CreateCachedContentConfig;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentResponse;

// Create a single client object
Client client = new Client();

// Access API methods through services on the client object
GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "Tell me a story.", null);
Chat chat = client.chats.create("gemini-3.8-flash");
File uploadedFile = client.files.upload("sample.txt", null);
CachedContent cache =
    client.caches.create("gemini-3.8-flash", CreateCachedContentConfig.builder().build());
```

### Проложить маршрут

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

## Аутентификация

Для аутентификации в старых и новых библиотеках используются ключи API. [Создать](https://aistudio.google.com/apikey?hl=ru) ключ API можно в Google AI Studio.

**До**

### Python

В старой версии SDK объект API-клиента обрабатывался неявно.

```
import google.generativeai as genai

genai.configure(api_key=...)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
```

### Java

```
import com.google.genai.Client;

// Passing the API key explicitly to the client builder
Client client = Client.builder().apiKey("GEMINI_API_KEY").build();
```

### Проложить маршрут

Импортируйте библиотеки Google:

```
import (
      "github.com/google/generative-ai-go/genai"
      "google.golang.org/api/option"
)
```

Создайте клиента:

```
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
```

**После**

### Python

При использовании Google GenAI SDK сначала создается API-клиент, который затем используется для вызова API.
Если вы не передадите ключ API клиенту, новый SDK возьмет его из переменных среды `GEMINI_API_KEY`.

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

```
from google import genai

client = genai.Client() # Set the API key using the GEMINI_API_KEY env var.
                        # Alternatively, you could set the API key explicitly:
                        # client = genai.Client(api_key="YOUR_API_KEY")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({apiKey: "GEMINI_API_KEY"});
```

### Java

```
import com.google.genai.Client;

// The client automatically picks up the GEMINI_API_KEY environment variable,
// or you can pass it explicitly via Client.builder().apiKey("GEMINI_API_KEY").build()
Client client = new Client();
```

### Проложить маршрут

Импортируйте библиотеку GenAI:

```
import "google.golang.org/genai"
```

Создайте клиента:

```
client, err := genai.NewClient(ctx, &genai.ClientConfig{
        Backend:  genai.BackendGeminiAPI,
})
```

## Генерация контента

### Текст

**До**

### Python

Раньше объектов клиента не было, и доступ к API осуществлялся напрямую через объекты `GenerativeModel`.

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(
    'Tell me a story in 300 words'
)
print(response.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });
const prompt = "Tell me a story in 300 words";

const result = await model.generateContent(prompt);
console.log(result.response.text());
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "Tell me a story in 300 words";

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", prompt, null);
System.out.println(response.text());
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
resp, err := model.GenerateContent(ctx, genai.Text("Tell me a story in 300 words."))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response parts
```

**После**

### Python

Новый Google GenAI SDK предоставляет доступ ко всем методам API через объект `Client`. За исключением нескольких особых случаев с сохранением состояния (`chat` и live-api `session`s), все это функции без сохранения состояния. Для удобства и единообразия возвращаемые объекты относятся к классам `pydantic`.

```
from google import genai
client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Tell me a story in 300 words.'
)
print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me a story in 300 words.",
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Tell me a story in 300 words.", null);
System.out.println(response.text());
```

### Проложить маршрут

```
ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me a story in 300 words."), nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### Изображение

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content([
    'Tell me a story based on this image',
    Image.open(image_path)
])
print(response.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("path/to/organ.jpg"));
Part imagePart = Part.fromBytes(imageBytes, "image/jpeg");

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        Content.fromParts(Part.fromText("Tell me a story based on this image"), imagePart),
        null);
System.out.println(response.text());
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")

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

**После**

### Python

В новом SDK есть многие удобные функции. Например, объекты `PIL.Image` преобразуются автоматически.

```
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=[
        'Tell me a story based on this image',
        Image.open(image_path)
    ]
)
print(response.text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const organ = await ai.files.upload({
  file: "path/to/organ.jpg",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    createUserContent([
      "Tell me a story based on this image",
      createPartFromUri(organ.uri, organ.mimeType)
    ]),
  ],
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

Client client = new Client();

File organ = client.files.upload("path/to/organ.jpg", null);

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        Content.fromParts(
            Part.fromText("Tell me a story based on this image"),
            Part.fromUri(organ.uri().orElse(""), organ.mimeType().orElse("image/jpeg"))),
        null);
System.out.println(response.text());
```

### Проложить маршрут

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

result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### Потоковая передача

**До**

### Python

```
import google.generativeai as genai

response = model.generate_content(
    "Write a cute story about cats.",
    stream=True)
for chunk in response:
    print(chunk.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });

const prompt = "Write a story about a magic backpack.";

const result = await model.generateContentStream(prompt);

// Print text as it comes in.
for await (const chunk of result.stream) {
  const chunkText = chunk.text();
  process.stdout.write(chunkText);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "Write a story about a magic backpack.";

try (ResponseStream<GenerateContentResponse> stream =
    client.models.generateContentStream("gemini-3.8-flash", prompt, null)) {
  for (GenerateContentResponse chunk : stream) {
    System.out.print(chunk.text());
  }
}
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
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

**После**

### Python

```
from google import genai

client = genai.Client()

for chunk in client.models.generate_content_stream(
  model='gemini-3.8-flash',
  contents='Tell me a story in 300 words.'
):
    print(chunk.text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContentStream({
  model: "gemini-3.8-flash",
  contents: "Write a story about a magic backpack.",
});
let text = "";
for await (const chunk of response) {
  console.log(chunk.text);
  text += chunk.text;
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

try (ResponseStream<GenerateContentResponse> response =
    client.models.generateContentStream(
        "gemini-3.8-flash", "Tell me a story in 300 words.", null)) {
  for (GenerateContentResponse chunk : response) {
    System.out.println(chunk.text());
  }
}
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

for result, err := range client.Models.GenerateContentStream(
    ctx,
    "gemini-3.8-flash",
    genai.Text("Write a story about a magic backpack."),
    nil,
) {
    if err != nil {
        log.Fatal(err)
    }
    fmt.Print(result.Candidates[0].Content.Parts[0].Text)
}
```

## Конфигурация

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
  'gemini-3.8-flash',
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

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .systemInstruction(
            Content.fromParts(Part.fromText("you are a story teller for kids under 5 years old")))
        .maxOutputTokens(400)
        .topK(2.0f)
        .topP(0.5f)
        .temperature(0.5f)
        .responseMimeType("application/json")
        .stopSequences(Arrays.asList("\n"))
        .build();

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "tell me a story in 100 words", config);
System.out.println(response.text());
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
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

**После**

### Python

Для всех методов в новом SDK обязательные аргументы предоставляются в виде аргументов ключевых слов. Все необязательные входные данные указываются в аргументе `config`. Аргументы конфигурации можно задавать в виде словарей Python или классов `Config` в пространстве имен `google.genai.types`. Для удобства и единообразия все определения в модуле `types` являются классами `pydantic`.

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-3.8-flash',
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

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .candidateCount(1)
        .stopSequences(Arrays.asList("x"))
        .maxOutputTokens(20)
        .temperature(1.0f)
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Tell me a story about a magic backpack.", config);
System.out.println(response.text());
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx,
    "gemini-3.8-flash",
    genai.Text("Tell me about New York"),
    &genai.GenerateContentConfig{
        Temperature:      genai.Ptr[float32](0.5),
        TopP:             genai.Ptr[float32](0.5),
        TopK:             genai.Ptr[float32](2.0),
        ResponseMIMEType: "application/json",
        StopSequences:    []string{"Yankees"},
        CandidateCount:   2,
        Seed:             genai.Ptr[int32](42),
        MaxOutputTokens:  128,
        PresencePenalty:  genai.Ptr[float32](0.5),
        FrequencyPenalty: genai.Ptr[float32](0.5),
    },
)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing response
```

## Настройки безопасности

Сгенерируйте ответ с настройками безопасности:

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(
    'say something bad',
    safety_settings={
        'HATE': 'BLOCK_ONLY_HIGH',
        'HARASSMENT': 'BLOCK_ONLY_HIGH',
  }
)
```

### JavaScript

```
import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(
            Arrays.asList(
                SafetySetting.builder()
                    .category(HarmCategory.Known.HARM_CATEGORY_HARASSMENT)
                    .threshold(HarmBlockThreshold.Known.BLOCK_LOW_AND_ABOVE)
                    .build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "say something bad", config);
System.out.println(response.text());
```

**После**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-3.8-flash',
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

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const unsafePrompt =
  "I support Martians Soccer Club and I think " +
  "Jupiterians Football Club sucks! Write an ironic phrase telling " +
  "them how I feel about them.";

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(
            Arrays.asList(
                SafetySetting.builder()
                    .category(HarmCategory.Known.HARM_CATEGORY_HATE_SPEECH)
                    .threshold(HarmBlockThreshold.Known.BLOCK_ONLY_HIGH)
                    .build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "say something bad", config);
System.out.println("Finish reason: " + response.finishReason());
```

## Асинхр.

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content_async(
    'tell me a story in 100 words'
)
```

**После**

### Python

Чтобы использовать новый SDK с `asyncio`, для каждого метода в `client.aio` есть отдельная реализация `async`.

```
from google import genai

client = genai.Client()

response = await client.aio.models.generate_content(
    model='gemini-3.8-flash',
    contents='Tell me a story in 300 words.'
)
```

## Чат

Начните чат и отправьте сообщение модели:

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
chat = model.start_chat()

response = chat.send_message(
    "Tell me a story in 100 words")
response = chat.send_message(
    "What happened after that?")
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });
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

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
Chat chat = client.chats.create("gemini-3.8-flash");

GenerateContentResponse response1 = chat.sendMessage("Tell me a story in 100 words");
System.out.println(response1.text());

GenerateContentResponse response2 = chat.sendMessage("What happened after that?");
System.out.println(response2.text());
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
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

**После**

### Python

```
from google import genai

client = genai.Client()

chat = client.chats.create(model='gemini-3.8-flash')

response = chat.send_message(
    message='Tell me a story in 100 words')
response = chat.send_message(
    message='What happened after that?')
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const chat = ai.chats.create({
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
Chat chat = client.chats.create("gemini-3.8-flash");

GenerateContentResponse response1 = chat.sendMessage("I have 2 dogs in my house.");
System.out.println("Chat response 1: " + response1.text());

GenerateContentResponse response2 = chat.sendMessage("How many paws are in my house?");
System.out.println("Chat response 2: " + response2.text());
```

### Проложить маршрут

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

chat, err := client.Chats.Create(ctx, "gemini-3.8-flash", nil, nil)
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

## Вызов функций

**До**

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
    model_name="gemini-3.8-flash",
    tools=[get_current_weather]
)

response = model.generate_content("What is the weather in San Francisco?")
function_call = response.candidates[0].parts[0].function_call
```

**После**

### Python

В новом SDK автоматический вызов функций включен по умолчанию. Здесь вы можете отключить его.

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
  model='gemini-3.8-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather],
      automatic_function_calling={'disable': True},
  ),
)

function_call = response.candidates[0].content.parts[0].function_call
```

### Автоматический вызов функций

**До**

### Python

Старая версия SDK поддерживает только автоматический вызов функций в чате. В новом SDK это режим работы по умолчанию в `generate_content`.

```
import google.generativeai as genai

def get_current_weather(city: str) -> str:
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    tools=[get_current_weather]
)

chat = model.start_chat(
    enable_automatic_function_calling=True)
result = chat.send_message("What is the weather in San Francisco?")
```

**После**

### Python

```
from google import genai
from google.genai import types
client = genai.Client()

def get_current_weather(city: str) -> str:
    return "23C"

response = client.models.generate_content(
  model='gemini-3.8-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather]
  ),
)
```

## Выполнение кода

Выполнение кода – это инструмент, который позволяет модели генерировать код Python, запускать его и возвращать результат.

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    tools="code_execution"
)

result = model.generate_content(
  "What is the sum of the first 50 prime numbers? Generate and run code for "
  "the calculation, and make sure you get all 50.")
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-3.8-flash",
  tools: [{ codeExecution: {} }],
});

const result = await model.generateContent(
  "What is the sum of the first 50 prime numbers? " +
    "Generate and run code for the calculation, and make sure you get " +
    "all 50.",
);

console.log(result.response.text());
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Tool;
import com.google.genai.types.ToolCodeExecution;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .tools(
            Arrays.asList(
                Tool.builder().codeExecution(ToolCodeExecution.builder().build()).build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "What is the sum of the first 50 prime numbers? Generate and run code for "
            + "the calculation, and make sure you get all 50.",
        config);
System.out.println(response.text());
```

**После**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='What is the sum of the first 50 prime numbers? Generate and run '
            'code for the calculation, and make sure you get all 50.',
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    ),
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;
import com.google.genai.types.ToolCodeExecution;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .tools(
            Arrays.asList(
                Tool.builder().codeExecution(ToolCodeExecution.builder().build()).build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Write and execute code that calculates the sum of the first 50 prime numbers. "
            + "Ensure that only the executable code and its resulting output are generated.",
        config);

if (response.parts() != null) {
  for (Part part : response.parts()) {
    System.out.println(part);
  }
}
System.out.println(response.text());
```

## Находите информацию из надежных источников

`GoogleSearch` (Gemini 2.0 и более поздние версии) и `GoogleSearchRetrieval` (Gemini до версии 2.0) – это инструменты, которые позволяют модели получать общедоступные веб-данные для обоснования. Они работают на основе технологий Google.

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(
    contents="what is the Google stock price?",
    tools='google_search_retrieval'
)
```

**После**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
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

## Ответ JSON

Генерировать ответы в формате JSON.

**До**

### Python

Указав `response_schema` и задав `response_mime_type="application/json"`, пользователи могут ограничить модель, чтобы она создавала ответ `JSON` в соответствии с заданной структурой.

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

model = genai.GenerativeModel(model_name="gemini-3.8-flash")
result = model.generate_content(
    "Give me information of the United States",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema = CountryInfo
    ),
)
```

### JavaScript

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
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

Schema schema =
    Schema.builder()
        .description("List of recipes")
        .type(Type.Known.ARRAY)
        .items(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(
                    Map.of(
                        "recipeName",
                        Schema.builder()
                            .type(Type.Known.STRING)
                            .description("Name of the recipe")
                            .build()))
                .required(Arrays.asList("recipeName"))
                .build())
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .responseMimeType("application/json")
        .responseSchema(schema)
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "List a few popular cookie recipes.", config);
System.out.println(response.text());
```

**После**

### Python

Новый SDK использует классы `pydantic` для предоставления схемы (хотя вы можете передать `genai.types.Schema` или эквивалентный класс `dict`). Если это возможно, SDK будет анализировать возвращенный JSON и возвращать результат в `response.parsed`. Если вы указали класс `pydantic` в качестве схемы, SDK преобразует `JSON` в экземпляр класса.

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
    model='gemini-3.8-flash',
    contents='Give me information of the United States.',
    config={
        'response_mime_type': 'application/json',
        'response_schema': CountryInfo,
    },
)

response.parsed
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

Schema schema =
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(
                    Map.of(
                        "recipeName", Schema.builder().type(Type.Known.STRING).build(),
                        "ingredients",
                            Schema.builder()
                                .type(Type.Known.ARRAY)
                                .items(Schema.builder().type(Type.Known.STRING).build())
                                .build()))
                .required(Arrays.asList("recipeName", "ingredients"))
                .build())
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .responseMimeType("application/json")
        .responseSchema(schema)
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "List a few popular cookie recipes.", config);
System.out.println(response.text());
```

## Файлы

### Загрузить

Загрузка файла:

**До**

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

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content([
    'Can you summarize this file:',
    my_file
])
print(response.text)
```

**После**

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
    model='gemini-3.8-flash',
    contents=[
        'Can you summarize this file:',
        my_file
    ]
)
print(response.text)
```

### List и Get

Чтобы получить список загруженных файлов и загруженный файл с определенным названием, выполните следующие действия:

**До**

### Python

```
import google.generativeai as genai

for file in genai.list_files():
  print(file.name)

file = genai.get_file(name=file.name)
```

**После**

### Python

```
from google import genai
client = genai.Client()

for file in client.files.list():
    print(file.name)

file = client.files.get(name=file.name)
```

### Удалить

Как удалить файл

**До**

### Python

```
import pathlib
import google.generativeai as genai

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = genai.upload_file(path='dummy.txt')

file = genai.delete_file(name=dummy_file.name)
```

**После**

### Python

```
import pathlib
from google import genai

client = genai.Client()

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = client.files.upload(file='dummy.txt')

response = client.files.delete(name=dummy_file.name)
```

## Кеширование контекста

Кеширование контекста позволяет пользователю передать контент модели один раз, кешировать входные токены, а затем ссылаться на кешированные токены в последующих вызовах, чтобы снизить стоимость.

**До**

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
    model="gemini-3.8-flash",
    system_instruction="You are an expert at analyzing transcripts.",
    contents=[document],
)

# Generate response
apollo_model = genai.GenerativeModel.from_cached_content(
    cached_content=apollo_cache
)
response = apollo_model.generate_content("Find a lighthearted moment from this transcript")
```

### JavaScript

```
import { GoogleAICacheManager, GoogleAIFileManager } from "@google/generative-ai/server";
import { GoogleGenerativeAI } from "@google/generative-ai";

const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");

const uploadResult = await fileManager.uploadFile("path/to/a11.txt", {
  mimeType: "text/plain",
});

const cacheResult = await cacheManager.create({
  model: "models/gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CachedContent;
import com.google.genai.types.Content;
import com.google.genai.types.CreateCachedContentConfig;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

File uploadResult = client.files.upload("path/to/a11.txt", null);

CachedContent cacheResult =
    client.caches.create(
        "gemini-3.8-flash",
        CreateCachedContentConfig.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromUri(
                            uploadResult.uri().orElse(""),
                            uploadResult.mimeType().orElse("text/plain")))))
            .systemInstruction(
                Content.fromParts(Part.fromText("You are an expert at analyzing transcripts.")))
            .build());

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Please summarize this transcript.",
        GenerateContentConfig.builder().cachedContent(cacheResult.name().orElse("")).build());
System.out.println(response.text());
```

**После**

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
model='gemini-3.8-flash'
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

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-3.8-flash";

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CachedContent;
import com.google.genai.types.Content;
import com.google.genai.types.CreateCachedContentConfig;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

File document = client.files.upload("a11.txt", null);
String modelName = "gemini-3.8-flash";

CachedContent cache =
    client.caches.create(
        modelName,
        CreateCachedContentConfig.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromUri(
                            document.uri().orElse(""), document.mimeType().orElse("text/plain")))))
            .systemInstruction(
                Content.fromParts(Part.fromText("You are an expert analyzing transcripts.")))
            .build());

GenerateContentResponse response =
    client.models.generateContent(
        modelName,
        "Find a lighthearted moment from this transcript",
        GenerateContentConfig.builder().cachedContent(cache.name().orElse("")).build());
System.out.println(response.text());
```

## Подсчет токенов

Подсчет количества токенов в запросе.

**До**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.count_tokens(
    'The quick brown fox jumps over the lazy dog.')
```

### JavaScript

```
 import { GoogleGenerativeAI } from "@google/generative-ai";

 const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
 const model = genAI.getGenerativeModel({
   model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

CountTokensResponse countResult = client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println(countResult.totalTokens().orElse(0));

GenerateContentResponse generateResult =
    client.models.generateContent("gemini-3.8-flash", prompt, null);
System.out.println(generateResult.usageMetadata());
```

**После**

### Python

```
from google import genai

client = genai.Client()

response = client.models.count_tokens(
    model='gemini-3.8-flash',
    contents='The quick brown fox jumps over the lazy dog.',
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const prompt = "The quick brown fox jumps over the lazy dog.";
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
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

CountTokensResponse countTokensResponse =
    client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println(countTokensResponse.totalTokens().orElse(0));

GenerateContentResponse generateResponse =
    client.models.generateContent("gemini-3.8-flash", prompt, null);
System.out.println(generateResponse.usageMetadata());
```

## Сгенерировать изображения

Генерировать изображения

**До**

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

**После**

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

## Встраивание контента

Создавать встраивания контента.

**До**

### Python

```
import google.generativeai as genai

response = genai.embed_content(
  model='models/gemini-embedding-001',
  content='Hello world'
)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-embedding-001",
});

const result = await model.embedContent("Hello world!");

console.log(result.embedding);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-001", "Hello world!", null);
System.out.println(response.embeddings());
```

**После**

### Python

```
from google import genai

client = genai.Client()

response = client.models.embed_content(
  model='gemini-embedding-001',
  contents='Hello world',
)
```

### JavaScript

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();
String text = "Hello World!";

EmbedContentResponse result =
    client.models.embedContent(
        "gemini-embedding-001",
        text,
        EmbedContentConfig.builder().outputDimensionality(10).build());
System.out.println(result.embeddings());
```

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-15 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-15 UTC."],[],[]]
