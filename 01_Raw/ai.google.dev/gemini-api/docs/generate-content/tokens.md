---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=th
fetched_at: 2026-07-20T04:43:22.130079+00:00
title: "\u0e17\u0e4d\u0e32\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e41\u0e25\u0e30\u0e19\u0e31\u0e1a\u0e42\u0e17\u0e40\u0e04\u0e47\u0e19 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ทําความเข้าใจและนับโทเค็น

Gemini และโมเดล Generative AI อื่นๆ จะประมวลผลอินพุตและเอาต์พุตที่ระดับความละเอียดที่เรียกว่า *โทเค็น*

**สำหรับโมเดล Gemini โทเค็นจะเทียบเท่ากับอักขระประมาณ 4 ตัว
โทเค็น 100 รายการจะเท่ากับคำภาษาอังกฤษประมาณ 60-80 คำ**

## เกี่ยวกับโทเค็น

โทเค็นอาจเป็นอักขระเดียว เช่น `z` หรือคำทั้งคำ เช่น `cat` คำยาวจะถูกแบ่งออกเป็นโทเค็นหลายรายการ ชุดโทเค็นทั้งหมดที่โมเดลใช้เรียกว่าคำศัพท์ และกระบวนการแยกข้อความออกเป็นโทเค็นเรียกว่า *การแยกโทเค็น*

เมื่อเปิดใช้การเรียกเก็บเงิน [ต้นทุนของการเรียกใช้ Gemini API](https://ai.google.dev/pricing?hl=th) จะ
พิจารณาจากจำนวนโทเค็นอินพุตและเอาต์พุตเป็นส่วนหนึ่ง ดังนั้นการรู้วิธี
นับโทเค็นจึงอาจเป็นประโยชน์

คุณสามารถลองนับโทเค็นใน Colab ของเราได้

|  |  |  |
| --- | --- | --- |
| [ดูใน ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | [ลองใช้ Colab Notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=th) | [ดู Notebook ใน GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=th) |

## นับโทเค็น

อินพุตและเอาต์พุตทั้งหมดของ Gemini API จะได้รับการแยกโทเค็น ซึ่งรวมถึงข้อความ ไฟล์รูปภาพ และรูปแบบอื่นๆ ที่ไม่ใช่ข้อความ

คุณสามารถนับโทเค็นได้ด้วยวิธีต่อไปนี้

- **เรียกใช้ [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=th) ด้วยอินพุต
  ของคำขอ**  
   ฟังก์ชันนี้จะแสดงผลจำนวนโทเค็นทั้งหมดใน *อินพุตเท่านั้น* คุณสามารถเรียกใช้ฟังก์ชันนี้ก่อนส่งอินพุตไปยังโมเดลเพื่อตรวจสอบขนาดของคำขอ
- **ใช้แอตทริบิวต์ `usage_metadata` ในออบเจ็กต์ `response` หลังจาก
  เรียกใช้ `generate_content`**  
   ฟังก์ชันนี้จะแสดงผลจำนวนโทเค็นทั้งหมดใน
  *ทั้งอินพุตและเอาต์พุต*: `total_token_count`  
   นอกจากนี้ยังแสดงผลจำนวนโทเค็นของอินพุตและเอาต์พุตแยกกันด้วย ได้แก่ `prompt_token_count` (โทเค็นอินพุต) และ `candidates_token_count` (โทเค็นเอาต์พุต)

  หากคุณใช้ [โมเดล
  การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th) ระบบจะแสดงผลโทเค็นที่ใช้ระหว่างกระบวนการคิด
  ใน `thoughts_token_count` และหากคุณใช้
  [การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th) จำนวนโทเค็นที่แคชไว้จะอยู่ใน `cached_content_token_count`

### นับโทเค็นข้อความ

หากคุณเรียกใช้ `count_tokens` ด้วยอินพุตที่เป็นข้อความเท่านั้น ฟังก์ชันนี้จะแสดงผลจำนวนโทเค็นของข้อความใน *อินพุตเท่านั้น* (`total_tokens`) คุณสามารถเรียกใช้ฟังก์ชันนี้ก่อนเรียกใช้ `generate_content` เพื่อตรวจสอบขนาดของคำขอ

อีกตัวเลือกหนึ่งคือการเรียกใช้ `generate_content` แล้วใช้แอตทริบิวต์ `usage_metadata` ในออบเจ็กต์ `response` เพื่อรับข้อมูลต่อไปนี้

- จำนวนโทเค็นแยกกันของอินพุต (`prompt_token_count`) เนื้อหาที่แคชไว้ (`cached_content_token_count`) และเอาต์พุต (`candidates_token_count`)
- จำนวนโทเค็นสำหรับกระบวนการคิด (`thoughts_token_count`)
- จำนวนโทเค็นทั้งหมดใน *ทั้งอินพุตและเอาต์พุต* (`total_token_count`)

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

### นับโทเค็นการสนทนาไปมา (แชท)

หากคุณเรียกใช้ `count_tokens` ด้วยประวัติการแชท ฟังก์ชันนี้จะแสดงผลจำนวนโทเค็นทั้งหมดของข้อความจากแต่ละบทบาทในการแชท (`total_tokens`)

อีกตัวเลือกหนึ่งคือการเรียกใช้ `send_message` แล้วใช้แอตทริบิวต์ `usage_metadata` ในออบเจ็กต์ `response` เพื่อรับข้อมูลต่อไปนี้

- จำนวนโทเค็นแยกกันของอินพุต (`prompt_token_count`) เนื้อหาที่แคชไว้ (`cached_content_token_count`) และเอาต์พุต (`candidates_token_count`)
- จำนวนโทเค็นสำหรับกระบวนการคิด (`thoughts_token_count`)
- จำนวนโทเค็นทั้งหมดใน *ทั้งอินพุตและเอาต์พุต* (`total_token_count`)

หากต้องการทราบว่าการสนทนาครั้งถัดไปจะมีขนาดเท่าใด คุณต้องเพิ่มการสนทนาครั้งถัดไปลงในประวัติเมื่อเรียกใช้ `count_tokens`

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

### นับโทเค็นแบบหลายรูปแบบ

อินพุตทั้งหมดของ Gemini API จะได้รับการแยกโทเค็น ซึ่งรวมถึงข้อความ ไฟล์รูปภาพ และรูปแบบอื่นๆ ที่ไม่ใช่ข้อความ โปรดทราบประเด็นสำคัญระดับสูงต่อไปนี้เกี่ยวกับการแยกโทเค็นของอินพุตแบบหลายรูปแบบระหว่างการประมวลผลโดย Gemini API

- อินพุตรูปภาพที่มีขนาดทั้ง 2 ด้าน <=384 พิกเซลจะนับเป็น 258 โทเค็น รูปภาพที่มีขนาดใหญ่กว่าในด้านใดด้านหนึ่งหรือทั้ง 2 ด้านจะถูกครอบตัดและปรับขนาดตามความจำเป็นให้เป็นไทล์ขนาด 768x768 พิกเซล โดยแต่ละไทล์จะนับเป็น 258 โทเค็น
- ระบบจะแปลงไฟล์วิดีโอและไฟล์เสียงเป็นโทเค็นในอัตราคงที่ต่อไปนี้ วิดีโอที่ 263 โทเค็นต่อวินาที และเสียงที่ 32 โทเค็นต่อวินาที

#### ความละเอียดของสื่อ

[โมเดล Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-3) มีการควบคุมแบบละเอียดในการประมวลผลการมองเห็นแบบ
หลายรูปแบบด้วยพารามิเตอร์ `media_resolution` พารามิเตอร์ `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุดที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ**
ความละเอียดที่สูงขึ้นจะช่วยเพิ่มความสามารถของโมเดลในการอ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง

ดูรายละเอียดเพิ่มเติมเกี่ยวกับพารามิเตอร์และวิธีที่พารามิเตอร์นี้อาจส่งผลต่อการคำนวณโทเค็นได้ที่
คู่มือ[ความละเอียดของสื่อ](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=th)

#### ไฟล์ภาพ

หากคุณเรียกใช้ `count_tokens` ด้วยอินพุตที่เป็นข้อความและรูปภาพ ฟังก์ชันนี้จะแสดงผลจำนวนโทเค็นรวมของข้อความและรูปภาพใน *อินพุตเท่านั้น* (`total_tokens`) คุณสามารถเรียกใช้ฟังก์ชันนี้ก่อนเรียกใช้ `generate_content` เพื่อตรวจสอบขนาดของคำขอ นอกจากนี้ คุณยังเรียกใช้ `count_tokens` กับข้อความและไฟล์แยกกันได้ด้วย

อีกตัวเลือกหนึ่งคือการเรียกใช้ `generate_content` แล้วใช้แอตทริบิวต์ `usage_metadata` ในออบเจ็กต์ `response` เพื่อรับข้อมูลต่อไปนี้

- จำนวนโทเค็นแยกกันของอินพุต (`prompt_token_count`) เนื้อหาที่แคชไว้ (`cached_content_token_count`) และเอาต์พุต (`candidates_token_count`)
- จำนวนโทเค็นสำหรับกระบวนการคิด (`thoughts_token_count`)
- จำนวนโทเค็นทั้งหมดใน *ทั้งอินพุตและเอาต์พุต* (`total_token_count`)

ตัวอย่างที่ใช้รูปภาพที่อัปโหลดจาก File API

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

ตัวอย่างที่แสดงรูปภาพเป็นข้อมูลแบบอินไลน์

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

#### ไฟล์วิดีโอหรือไฟล์เสียง

ระบบจะแปลงเสียงและวิดีโอแต่ละรายการเป็นโทเค็นในอัตราคงที่ต่อไปนี้

- วิดีโอ: 263 โทเค็นต่อวินาที
- เสียง: 32 โทเค็นต่อวินาที

หากคุณเรียกใช้ `count_tokens` ด้วยอินพุตที่เป็นข้อความและวิดีโอ/เสียง ฟังก์ชันนี้จะแสดงผลจำนวนโทเค็นรวมของข้อความและไฟล์วิดีโอ/เสียงใน *อินพุตเท่านั้น* (`total_tokens`) คุณสามารถเรียกใช้ฟังก์ชันนี้ก่อนเรียกใช้ `generate_content` เพื่อตรวจสอบขนาดของคำขอ นอกจากนี้ คุณยังเรียกใช้ `count_tokens` กับข้อความและไฟล์แยกกันได้ด้วย

อีกตัวเลือกหนึ่งคือการเรียกใช้ `generate_content` แล้วใช้แอตทริบิวต์ `usage_metadata` ในออบเจ็กต์ `response` เพื่อรับข้อมูลต่อไปนี้

- จำนวนโทเค็นแยกกันของอินพุต (`prompt_token_count`) เนื้อหาที่แคชไว้ (`cached_content_token_count`) และเอาต์พุต (`candidates_token_count`)
- จำนวนโทเค็นสำหรับกระบวนการคิด (`thoughts_token_count`)
- จำนวนโทเค็นทั้งหมดใน *ทั้งอินพุตและเอาต์พุต* (`total_token_count`)

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

### นับโทเค็นการคิด

เมื่อเปิดใช้การคิด ราคาการตอบกลับจะเป็นผลรวมของโทเค็นเอาต์พุตและโทเค็นการคิด คุณสามารถดึงข้อมูลจำนวนโทเค็นการคิดทั้งหมดที่สร้างขึ้นจากช่อง `thoughtsTokenCount` (หรือเทียบเท่าใน SDK)

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

โมเดลการคิดจะสร้างความคิดทั้งหมดเพื่อปรับปรุงคุณภาพของการตอบกลับสุดท้าย แล้วแสดงผล[ข้อมูลสรุป](https://ai.google.dev/gemini-api/docs/thinking?hl=th#summaries)เพื่อให้ข้อมูลเชิงลึกเกี่ยวกับกระบวนการคิด ดังนั้น API จะกำหนดราคาตามโทเค็นความคิดทั้งหมดที่โมเดลสร้างขึ้นเพื่อสร้างข้อมูลสรุป แม้ว่า API จะแสดงผลข้อมูลสรุปเท่านั้น

ดูข้อมูลเพิ่มเติมเกี่ยวกับวิธีกำหนดค่าการคิดได้ในคู่มือการคิดของ [Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

## หน้าต่างบริบท

โมเดลที่พร้อมใช้งานผ่าน Gemini API มีหน้าต่างบริบทที่วัดเป็นโทเค็น หน้าต่างบริบทจะกำหนดจำนวนอินพุตที่คุณระบุได้และจำนวนเอาต์พุตที่โมเดลสร้างได้ คุณสามารถกำหนดขนาดของ
หน้าต่างบริบทได้โดยการเรียกใช้ปลายทาง [`models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=th)
หรือดูใน[เอกสารประกอบของโมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)

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

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-24 UTC"],[],[]]
