---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=ar
fetched_at: 2026-06-22T06:27:24.613883+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الرموز المميزة وعدّها

تعالج نماذج الذكاء الاصطناعي التوليدي، مثل Gemini، المدخلات والمخرجات بدقة
تُعرف باسم *الرمز المميز*.

**في نماذج Gemini، يعادل الرمز المميز الواحد حوالي 4 أحرف، ويعادل 100 رمز مميز حوالي 60 إلى 80 كلمة باللغة الإنجليزية.**

## لمحة عن الرموز المميزة

يمكن أن تكون الرموز المميّزة أحرفًا مفردة مثل `z` أو كلمات كاملة مثل `cat`، ويتم تقسيم الكلمات الطويلة إلى عدة رموز مميّزة. وتُعرف مجموعة كل الرموز المميّزة التي يستخدمها النموذج باسم المفردات، وتُعرف عملية تقسيم النص إلى رموز مميّزة باسم *التقطيع إلى رموز مميّزة*.

عند تفعيل الفوترة، يتم تحديد [تكلفة طلب البيانات من Gemini API](https://ai.google.dev/pricing?hl=ar) جزئيًا من خلال عدد الرموز المميزة للإدخال والإخراج، لذا قد يكون من المفيد معرفة كيفية عدّ الرموز المميزة.

يمكنك تجربة احتساب الرموز المميزة في Colab.

|  |  |  |
| --- | --- | --- |
| [عرض على ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) | [تجربة ورقة ملاحظات Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=ar) | [عرض ورقة الملاحظات على GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=ar) |

## عدد الرموز المميزة

يتم تحويل جميع البيانات المدخلة إلى Gemini API والناتجة عنها إلى رموز مميزة، بما في ذلك النصوص وملفات الصور وغيرها من الوسائط غير النصية.

يمكنك احتساب الرموز المميزة بالطرق التالية:

- **استدعِ الدالة [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=ar) مع إدخال الطلب.**  
   تعرض هذه الدالة إجمالي عدد الرموز المميزة في *الإدخال فقط*. يمكنك إجراء هذه المكالمة قبل إرسال الإدخال إلى النموذج للتحقّق من حجم طلباتك.
- **استخدِم السمة `usage_metadata` في العنصر `response` بعد استدعاء `generate_content`.**  
   تعرض هذه السمة إجمالي عدد الرموز المميزة في *كلّ من الإدخال والإخراج*: `total_token_count`.  
   وتعرض أيضًا عدد الرموز المميزة للإدخال والإخراج بشكل منفصل: `prompt_token_count` (رموز الإدخال) و`candidates_token_count` (رموز الإخراج).

  إذا كنت تستخدم [نموذجًا
  للتفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar)، سيتم عرض الرموز المميزة المستخدَمة أثناء عملية التفكير في `thoughts_token_count`. وفي حال استخدام
  [التخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/caching?hl=ar)، سيكون عدد الرموز المميزة المخزّنة مؤقتًا في `cached_content_token_count`.

### احتساب الرموز المميّزة للنص

إذا طلبت `count_tokens` باستخدام إدخال نصي فقط، ستعرض عدد الرموز المميزة للنص *في الإدخال فقط* (`total_tokens`). يمكنك إجراء هذا الطلب قبل طلب `generate_content` للتحقّق من حجم طلباتك.

هناك خيار آخر وهو الاتصال بـ `generate_content` ثم استخدام السمة `usage_metadata`
في الكائن `response` للحصول على ما يلي:

- عدد الرموز المميزة المنفصلة للإدخال (`prompt_token_count`) والمحتوى المخزّن مؤقتًا (`cached_content_token_count`) والإخراج (`candidates_token_count`)
- عدد الرموز المميّزة لعملية التفكير (`thoughts_token_count`)
- إجمالي عدد الرموز المميّزة في *كل من الطلب والرد*
  (`total_token_count`)

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

### احتساب الرموز المميزة للمحادثات المتعددة الجولات

إذا طلبت من `count_tokens` عرض سجلّ المحادثة، سيعرض إجمالي عدد الرموز المميزة للنص من كل دور في المحادثة (`total_tokens`).

هناك خيار آخر وهو الاتصال بـ `send_message` ثم استخدام السمة `usage_metadata`
في الكائن `response` للحصول على ما يلي:

- عدد الرموز المميزة المنفصلة للإدخال (`prompt_token_count`) والمحتوى المخزّن مؤقتًا (`cached_content_token_count`) والإخراج (`candidates_token_count`)
- عدد الرموز المميّزة لعملية التفكير (`thoughts_token_count`)
- إجمالي عدد الرموز المميّزة في *كل من الطلب والرد*
  (`total_token_count`)

لمعرفة حجم الدور التالي في المحادثة، عليك إلحاقه بالسجلّ عند طلب `count_tokens`.

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

### احتساب الرموز المميّزة المتعددة الوسائط

يتم تحويل جميع المدخلات إلى رموز مميزة في Gemini API، بما في ذلك النصوص وملفات الصور وغيرها من الوسائط غير النصية. في ما يلي النقاط الرئيسية العالية المستوى حول تحويل الإدخال المتعدّد الوسائط إلى رموز مميزة أثناء معالجته من خلال Gemini API:

- يتم احتساب مدخلات الصور التي يقل فيها كلا البُعدين عن 384 بكسل أو يساويهما على أنّها 258 رمزًا مميزًا. يتم اقتصاص الصور الأكبر حجمًا في أحد البُعدَين أو كليهما وتغيير حجمها حسب الحاجة إلى مربّعات بحجم 768 × 768 بكسل، ويتم احتساب كل مربّع على أنّه 258 رمزًا مميزًا.
- يتم تحويل ملفات الفيديو والصوت إلى رموز مميزة بالأسعار الثابتة التالية:
  الفيديو: 263 رمزًا مميزًا في الثانية، والصوت: 32 رمزًا مميزًا في الثانية.

#### درجات دقة الوسائط

تتيح [نماذج Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-3) التحكّم بشكل دقيق في معالجة الصور المتعددة الوسائط باستخدام المَعلمة `media_resolution`. وتحدّد المَعلمة `media_resolution` **الحد الأقصى لعدد الرموز المميزة المخصّصة لكل صورة إدخال أو إطار فيديو.** وتؤدي الدقة الأعلى إلى تحسين قدرة النموذج على قراءة النصوص الدقيقة أو تحديد التفاصيل الصغيرة، ولكنها تزيد من استخدام الرموز المميزة ووقت الاستجابة.

لمزيد من التفاصيل حول المَعلمة وكيفية تأثيرها في احتساب الرموز المميّزة، راجِع دليل [دقة الوسائط](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ar).

#### ملفات الصور

إذا طلبت `count_tokens` باستخدام نص وصورة كمدخلات، سيعرض عدد الرموز المميزة المجمّعة للنص والصورة *في المدخلات فقط* (`total_tokens`). يمكنك إجراء هذا الطلب قبل طلب `generate_content` للتحقّق من حجم طلباتك. يمكنك أيضًا استدعاء `count_tokens` بشكل اختياري على النص والملف بشكل منفصل.

هناك خيار آخر وهو الاتصال بـ `generate_content` ثم استخدام السمة `usage_metadata`
في الكائن `response` للحصول على ما يلي:

- عدد الرموز المميزة المنفصلة للإدخال (`prompt_token_count`) والمحتوى المخزّن مؤقتًا (`cached_content_token_count`) والإخراج (`candidates_token_count`)
- عدد الرموز المميّزة لعملية التفكير (`thoughts_token_count`)
- إجمالي عدد الرموز المميّزة في *كل من الطلب والرد*
  (`total_token_count`)

مثال يستخدم صورة تم تحميلها من File API:

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

مثال يقدّم الصورة كبيانات مضمّنة:

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

#### ملفات الفيديو أو الصوت

يتم تحويل الصوت والفيديو إلى رموز مميزة بالأسعار الثابتة التالية:

- الفيديو: 263 رمزًا مميزًا في الثانية
- الصوت: 32 رمزًا مميزًا في الثانية

إذا اتصلت بـ `count_tokens` باستخدام إدخال نصي وفيديو/صوتي، سيعرض لك
عدد الرموز المميزة المجمّع للنص وملف الفيديو/الصوت *في الإدخال فقط*
(`total_tokens`). يمكنك إجراء هذا الاتصال قبل الاتصال بـ `generate_content`
للتحقّق من حجم طلباتك. يمكنك أيضًا الاتصال بـ `count_tokens` بشكل اختياري
على النص والملف بشكل منفصل.

هناك خيار آخر وهو الاتصال بـ `generate_content` ثم استخدام السمة `usage_metadata`
في الكائن `response` للحصول على ما يلي:

- عدد الرموز المميزة المنفصلة للإدخال (`prompt_token_count`) والمحتوى المخزّن مؤقتًا (`cached_content_token_count`) والإخراج (`candidates_token_count`)
- عدد الرموز المميّزة لعملية التفكير (`thoughts_token_count`)
- إجمالي عدد الرموز المميّزة في *كلّ من الطلب والرد*
  (`total_token_count`)

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

### عدّ الرموز المميّزة للأفكار

عند تفعيل ميزة "التفكير"، يكون سعر الردّ هو مجموع الرموز المميزة للناتج والرموز المميزة للتفكير. يمكنك استرداد إجمالي عدد الرموز المميزة التي تم إنشاؤها من الحقل `thoughtsTokenCount` (أو ما يعادله في حزمة تطوير البرامج (SDK)).

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

تنشئ نماذج التفكير أفكارًا كاملة لتحسين جودة الردّ النهائي، ثم تعرض [ملخّصات](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#summaries) لتقديم نظرة ثاقبة على عملية التفكير. وبالتالي، تستند الأسعار في واجهة برمجة التطبيقات إلى الرموز المميزة للأفكار الكاملة التي ينشئها النموذج لإنشاء ملخّص، حتى لو كانت واجهة برمجة التطبيقات تعرض الملخّص فقط.

يمكنك الاطّلاع على مزيد من المعلومات حول كيفية ضبط مدة التفكير في دليل [مدة تفكير Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).

## قدرات الاستيعاب

تتضمّن النماذج المتاحة من خلال Gemini API قدرات استيعاب يتم قياسها بالرموز المميّزة. تحدّد قدرة الاستيعاب حجم الإدخال الذي يمكنك تقديمه وحجم الإخراج الذي يمكن للنموذج إنشاؤه. يمكنك تحديد حجم قدرة الاستيعاب من خلال استدعاء نقطة النهاية [`models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=ar) أو الرجوع إلى [مستندات النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

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

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
