---
source_url: https://ai.google.dev/gemini-api/docs/migrate?hl=th
fetched_at: 2026-06-08T05:39:21.889405+00:00
title: "\u0e22\u0e49\u0e32\u0e22\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e1b\u0e22\u0e31\u0e07 Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ย้ายข้อมูลไปยัง Google GenAI SDK

เราได้เปิดตัวชุดไลบรารีใหม่ที่เรียกว่า [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=th) ตั้งแต่การเปิดตัว Gemini 2.0 ในช่วงปลายปี 2024
ซึ่งมีประสบการณ์การใช้งานที่ดียิ่งขึ้นสำหรับนักพัฒนาแอปผ่าน
สถาปัตยกรรมไคลเอ็นต์ที่[อัปเดต](https://ai.google.dev/gemini-api/docs/migrate?hl=th#client) และ
[ช่วยลดความซับซ้อนในการเปลี่ยนผ่าน](https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=th)ระหว่างเวิร์กโฟลว์ของนักพัฒนาแอป
และองค์กร

[ตอนนี้ Google GenAI SDK พร้อมให้บริการแก่ผู้ใช้ทั่วไป (GA) ในทุกแพลตฟอร์มที่รองรับ](https://ai.google.dev/gemini-api/docs/libraries?hl=th#new-libraries) หากคุณใช้[ไลบรารีเดิม](https://ai.google.dev/gemini-api/docs/libraries?hl=th#previous-sdks)ของเรา เราขอแนะนำอย่างยิ่งให้
ย้ายข้อมูล

คู่มือนี้มีตัวอย่างโค้ดที่ย้ายข้อมูลแล้วทั้งก่อนและหลังเพื่อช่วยให้คุณเริ่มต้นใช้งานได้

## การติดตั้ง

**ก่อน**

### Python

```
pip install -U -q "google-generativeai"
```

### JavaScript

```
npm install @google/generative-ai
```

### Go

```
go get github.com/google/generative-ai-go
```

**หลัง**

### Python

```
pip install -U -q "google-genai"
```

### JavaScript

```
npm install @google/genai
```

### Go

```
go get google.golang.org/genai
```

## การเข้าถึง API

SDK เก่าจะจัดการไคลเอ็นต์ API เบื้องหลังโดยปริยายโดยใช้วิธีการเฉพาะกิจต่างๆ ซึ่งทำให้จัดการไคลเอ็นต์และข้อมูลเข้าสู่ระบบได้ยาก
ตอนนี้คุณโต้ตอบผ่านออบเจ็กต์ `Client` ส่วนกลาง ออบเจ็กต์ `Client` นี้ทำหน้าที่เป็นจุดแรกเข้าเดียวสำหรับบริการ API ต่างๆ (เช่น `models`, `chats`, `files`, `tunings`) ซึ่งส่งเสริมความสอดคล้องและลดความซับซ้อนในการจัดการข้อมูลเข้าสู่ระบบและการกำหนดค่าในการเรียก API ต่างๆ

**ก่อน (การเข้าถึง API ที่รวมศูนย์น้อยกว่า)**

### Python

SDK เก่าไม่ได้ใช้ออบเจ็กต์ไคลเอ็นต์ระดับบนสุดอย่างชัดเจนสำหรับการเรียก API ส่วนใหญ่ คุณจะต้องสร้างอินสแตนซ์และโต้ตอบกับออบเจ็กต์ `GenerativeModel` โดยตรง

```
import google.generativeai as genai

# Directly create and use model objects
model = genai.GenerativeModel('gemini-3.5-flash')
response = model.generate_content(...)
chat = model.start_chat(...)
```

### JavaScript

แม้ว่า `GoogleGenerativeAI` จะเป็นจุดศูนย์กลางสำหรับโมเดลและการแชท แต่ฟังก์ชันการทำงานอื่นๆ เช่น การจัดการไฟล์และการจัดการแคช มักจะต้องนำเข้าและสร้างอินสแตนซ์ของคลาสไคลเอ็นต์ที่แยกกันโดยสิ้นเชิง

```
import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager, GoogleAICacheManager } from "@google/generative-ai/server"; // For files/caching

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");
const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");

// Get a model instance, then call methods on it
const model = genAI.getGenerativeModel({ model: "gemini-3.5-flash" });
const result = await model.generateContent(...);
const chat = model.startChat(...);

// Call methods on separate client objects for other services
const uploadedFile = await fileManager.uploadFile(...);
const cache = await cacheManager.create(...);
```

### Go

ฟังก์ชัน `genai.NewClient` สร้างไคลเอ็นต์ แต่โดยทั่วไปแล้วการดำเนินการกับโมเดล Generative จะเรียกใช้ในอินสแตนซ์ `GenerativeModel` ที่แยกกันซึ่งได้จากไคลเอ็นต์นี้ คุณอาจเข้าถึงบริการอื่นๆ ผ่านแพ็กเกจหรือรูปแบบที่แตกต่างกัน

```
import (
      "github.com/google/generative-ai-go/genai"
      "github.com/google/generative-ai-go/genai/fileman" // For files
      "google.golang.org/api/option"
)

client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
fileClient, err := fileman.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))

// Get a model instance, then call methods on it
model := client.GenerativeModel("gemini-3.5-flash")
resp, err := model.GenerateContent(...)
cs := model.StartChat()

// Call methods on separate client objects for other services
uploadedFile, err := fileClient.UploadFile(...)
```

**หลัง (ออบเจ็กต์ไคลเอ็นต์ที่รวมศูนย์)**

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

## การตรวจสอบสิทธิ์

ทั้งไลบรารีเดิมและไลบรารีใหม่จะตรวจสอบสิทธิ์โดยใช้คีย์ API คุณสามารถ
[สร้าง](https://aistudio.google.com/app/apikey?hl=th)คีย์ API ใน Google AI
Studio ได้

**ก่อน**

### Python

SDK เก่าจะจัดการออบเจ็กต์ไคลเอ็นต์ API โดยปริยาย

```
import google.generativeai as genai

genai.configure(api_key=...)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
```

### Go

นำเข้าไลบรารีของ Google ดังนี้

```
import (
      "github.com/google/generative-ai-go/genai"
      "google.golang.org/api/option"
)
```

สร้างไคลเอ็นต์ดังนี้

```
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
```

**หลัง**

### Python

เมื่อใช้ Google GenAI SDK คุณจะต้องสร้างไคลเอ็นต์ API ก่อน ซึ่งจะใช้ในการเรียก API
SDK ใหม่จะดึงคีย์ API จากตัวแปรสภาพแวดล้อม `GEMINI_API_KEY` หากคุณไม่ได้ส่งคีย์ไปยังไคลเอ็นต์

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

### Go

นำเข้าไลบรารี GenAI ดังนี้

```
import "google.golang.org/genai"
```

สร้างไคลเอ็นต์ดังนี้

```
client, err := genai.NewClient(ctx, &genai.ClientConfig{
        Backend:  genai.BackendGeminiAPI,
})
```

## สร้างเนื้อหา

### ข้อความ

**ก่อน**

### Python

ก่อนหน้านี้ไม่มีออบเจ็กต์ไคลเอ็นต์ คุณเข้าถึง API ผ่านออบเจ็กต์ `GenerativeModel` โดยตรง

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.5-flash')
response = model.generate_content(
    'Tell me a story in 300 words'
)
print(response.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-3.5-flash" });
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

model := client.GenerativeModel("gemini-3.5-flash")
resp, err := model.GenerateContent(ctx, genai.Text("Tell me a story in 300 words."))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response parts
```

**หลัง**

### Python

Google GenAI SDK ใหม่ให้สิทธิ์เข้าถึงเมธอด API ทั้งหมดผ่านออบเจ็กต์ `Client` ยกเว้นกรณีพิเศษที่เก็บสถานะ (`chat` และ `session` ของ Live API) ฟังก์ชันเหล่านี้ทั้งหมดเป็นฟังก์ชันที่ไม่เก็บสถานะ ออบเจ็กต์ที่แสดงผลจะเป็นคลาส `pydantic` เพื่อความสะดวกและสม่ำเสมอ

```
from google import genai
client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me a story in 300 words."), nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### รูปภาพ

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.5-flash')
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
const model = genAI.getGenerativeModel({ model: "gemini-3.5-flash" });

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

model := client.GenerativeModel("gemini-3.5-flash")

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

**หลัง**

### Python

SDK ใหม่มีฟีเจอร์อำนวยความสะดวกมากมายเช่นเดียวกับ SDK เดิม เช่น ระบบจะแปลงออบเจ็กต์ `PIL.Image` โดยอัตโนมัติ

```
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### สตรีมมิง

**ก่อน**

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
const model = genAI.getGenerativeModel({ model: "gemini-3.5-flash" });

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

model := client.GenerativeModel("gemini-3.5-flash")
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

**หลัง**

### Python

```
from google import genai

client = genai.Client()

for chunk in client.models.generate_content_stream(
  model='gemini-3.5-flash',
  contents='Tell me a story in 300 words.'
):
    print(chunk.text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContentStream({
  model: "gemini-3.5-flash",
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
    "gemini-3.5-flash",
    genai.Text("Write a story about a magic backpack."),
    nil,
) {
    if err != nil {
        log.Fatal(err)
    }
    fmt.Print(result.Candidates[0].Content.Parts[0].Text)
}
```

## การกำหนดค่า

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
  'gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

model := client.GenerativeModel("gemini-3.5-flash")
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

**หลัง**

### Python

สำหรับเมธอดทั้งหมดใน SDK ใหม่ ระบบจะระบุอาร์กิวเมนต์ที่จำเป็นเป็นอาร์กิวเมนต์คีย์เวิร์ด และระบุอินพุตที่ไม่บังคับทั้งหมดในอาร์กิวเมนต์ `config` คุณระบุอาร์กิวเมนต์การกำหนดค่าเป็นพจนานุกรม Python หรือคลาส `Config` ในเนมสเปซ `google.genai.types` ก็ได้ คำจำกัดความทั้งหมดในโมดูล `types` จะเป็นคลาส `pydantic` เพื่อความสะดวกและสม่ำเสมอ

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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
    "gemini-3.5-flash",
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

## การตั้งค่าความปลอดภัย

สร้างการตอบกลับด้วยการตั้งค่าความปลอดภัยดังนี้

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.5-flash')
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
  model: "gemini-3.5-flash",
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

**หลัง**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

## Async

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.5-flash')
response = model.generate_content_async(
    'tell me a story in 100 words'
)
```

**หลัง**

### Python

หากต้องการใช้ SDK ใหม่กับ `asyncio` จะมีการติดตั้งใช้งาน `async`
แยกกันสำหรับทุกเมธอดภายใต้ `client.aio`

```
from google import genai

client = genai.Client()

response = await client.aio.models.generate_content(
    model='gemini-3.5-flash',
    contents='Tell me a story in 300 words.'
)
```

## แชท

เริ่มแชทและส่งข้อความไปยังโมเดลดังนี้

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.5-flash')
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
const model = genAI.getGenerativeModel({ model: "gemini-3.5-flash" });
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

model := client.GenerativeModel("gemini-3.5-flash")
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

**หลัง**

### Python

```
from google import genai

client = genai.Client()

chat = client.chats.create(model='gemini-3.5-flash')

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
  model: "gemini-3.5-flash",
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

chat, err := client.Chats.Create(ctx, "gemini-3.5-flash", nil, nil)
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

## การเรียกใช้ฟังก์ชัน

**ก่อน**

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
    model_name="gemini-3.5-flash",
    tools=[get_current_weather]
)

response = model.generate_content("What is the weather in San Francisco?")
function_call = response.candidates[0].parts[0].function_call
```

**หลัง**

### Python

ใน SDK ใหม่ การเรียกใช้ฟังก์ชันอัตโนมัติจะเป็นค่าเริ่มต้น ซึ่งคุณจะปิดใช้ได้ดังนี้

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
  model='gemini-3.5-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather],
      automatic_function_calling={'disable': True},
  ),
)

function_call = response.candidates[0].content.parts[0].function_call
```

### การเรียกใช้ฟังก์ชันอัตโนมัติ

**ก่อน**

### Python

SDK เก่ารองรับการเรียกใช้ฟังก์ชันอัตโนมัติในการแชทเท่านั้น ใน SDK ใหม่ ลักษณะการทำงานนี้จะเป็นค่าเริ่มต้นใน `generate_content`

```
import google.generativeai as genai

def get_current_weather(city: str) -> str:
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-3.5-flash",
    tools=[get_current_weather]
)

chat = model.start_chat(
    enable_automatic_function_calling=True)
result = chat.send_message("What is the weather in San Francisco?")
```

**หลัง**

### Python

```
from google import genai
from google.genai import types
client = genai.Client()

def get_current_weather(city: str) -> str:
    return "23C"

response = client.models.generate_content(
  model='gemini-3.5-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather]
  ),
)
```

## การดำเนินการกับโค้ด

การดำเนินการกับโค้ดเป็นเครื่องมือที่ช่วยให้โมเดลสร้างโค้ด Python เรียกใช้โค้ด และแสดงผลลัพธ์

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
  tools: [{ codeExecution: {} }],
});

const result = await model.generateContent(
  "What is the sum of the first 50 prime numbers? " +
    "Generate and run code for the calculation, and make sure you get " +
    "all 50.",
);

console.log(result.response.text());
```

**หลัง**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

## การเชื่อมต่อแหล่งข้อมูลของ Search

`GoogleSearch` (Gemini>=2.0) และ `GoogleSearchRetrieval` (Gemini < 2.0) เป็น
เครื่องมือที่ช่วยให้โมเดลดึงข้อมูลเว็บสาธารณะเพื่อเชื่อมต่อแหล่งข้อมูล ซึ่งขับเคลื่อนโดย
Google

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.5-flash')
response = model.generate_content(
    contents="what is the Google stock price?",
    tools='google_search_retrieval'
)
```

**หลัง**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash',
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

## การตอบสนองของ JSON

สร้างคำตอบในรูปแบบ JSON ดังนี้

**ก่อน**

### Python

เมื่อระบุ `response_schema` และตั้งค่า
`response_mime_type="application/json"` ผู้ใช้จะจำกัดให้โมเดล
สร้างการตอบกลับ `JSON` ตามโครงสร้างที่กำหนดได้

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

model = genai.GenerativeModel(model_name="gemini-3.5-flash")
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
  model: "gemini-3.5-flash",
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

**หลัง**

### Python

SDK ใหม่ใช้คลาส `pydantic` เพื่อระบุสคีมา (แม้ว่าคุณจะส่ง `genai.types.Schema` หรือ `dict` ที่เทียบเท่ากันได้) SDK จะแยกวิเคราะห์ JSON ที่แสดงผลและแสดงผลลัพธ์ใน `response.parsed` หากทำได้ หากคุณระบุคลาส `pydantic` เป็นสคีมา SDK จะแปลง `JSON` นั้นเป็นอินสแตนซ์ของคลาส

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
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

## ไฟล์

### อัปโหลด

อัปโหลดไฟล์ดังนี้

**ก่อน**

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

model = genai.GenerativeModel('gemini-3.5-flash')
response = model.generate_content([
    'Can you summarize this file:',
    my_file
])
print(response.text)
```

**หลัง**

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
    model='gemini-3.5-flash',
    contents=[
        'Can you summarize this file:',
        my_file
    ]
)
print(response.text)
```

### แสดงรายการและรับ

แสดงรายการไฟล์ที่อัปโหลดและรับไฟล์ที่อัปโหลดด้วยชื่อไฟล์ดังนี้

**ก่อน**

### Python

```
import google.generativeai as genai

for file in genai.list_files():
  print(file.name)

file = genai.get_file(name=file.name)
```

**หลัง**

### Python

```
from google import genai
client = genai.Client()

for file in client.files.list():
    print(file.name)

file = client.files.get(name=file.name)
```

### ลบ

ลบไฟล์ดังนี้

**ก่อน**

### Python

```
import pathlib
import google.generativeai as genai

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = genai.upload_file(path='dummy.txt')

file = genai.delete_file(name=dummy_file.name)
```

**หลัง**

### Python

```
import pathlib
from google import genai

client = genai.Client()

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = client.files.upload(file='dummy.txt')

response = client.files.delete(name=dummy_file.name)
```

## การแคชบริบท

การแคชบริบทช่วยให้ผู้ใช้ส่งเนื้อหาไปยังโมเดลได้ครั้งเดียว แคชโทเค็นอินพุต แล้วอ้างอิงโทเค็นที่แคชไว้ในการเรียกครั้งต่อๆ ไปเพื่อลดค่าใช้จ่าย

**ก่อน**

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
    model="gemini-3.5-flash",
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
  model: "models/gemini-3.5-flash",
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

**หลัง**

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
model='gemini-3.5-flash'
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
const modelName = "gemini-3.5-flash";

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

## นับโทเค็น

นับจำนวนโทเค็นในคำขอดังนี้

**ก่อน**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.5-flash')
response = model.count_tokens(
    'The quick brown fox jumps over the lazy dog.')
```

### JavaScript

```
 import { GoogleGenerativeAI } from "@google/generative-ai";

 const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
 const model = genAI.getGenerativeModel({
   model: "gemini-3.5-flash",
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

**หลัง**

### Python

```
from google import genai

client = genai.Client()

response = client.models.count_tokens(
    model='gemini-3.5-flash',
    contents='The quick brown fox jumps over the lazy dog.',
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const prompt = "The quick brown fox jumps over the lazy dog.";
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
```

## สร้างรูปภาพ

สร้างรูปภาพดังนี้

**ก่อน**

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

**หลัง**

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

## ฝังเนื้อหา

สร้างการฝังเนื้อหาดังนี้

**ก่อน**

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

**หลัง**

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

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-01 UTC"],[],[]]
