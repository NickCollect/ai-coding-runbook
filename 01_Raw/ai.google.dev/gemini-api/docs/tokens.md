---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=ar
fetched_at: 2026-08-03T04:27:45.391831+00:00
title: "\u0641\u0647\u0645 \u0627\u0644\u0631\u0645\u0648\u0632 \u0627\u0644\u0645\u0645\u064a\u0651\u0632\u0629 \u0648\u0639\u062f\u0651\u0647\u0627 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الرموز المميّزة وعدّها

تعالج Gemini ونماذج الذكاء الاصطناعي التوليدي الأخرى المدخلات والمخرجات بمستوى تفصيلي يُعرف باسم *الرمز المميز*.

**في نماذج Gemini، يعادل الرمز المميز الواحد حوالي 4 أحرف.
يساوي 100 رمز مميز حوالي 60 إلى 80 كلمة إنجليزية.**

## لمحة عن الرموز المميزة

يمكن أن تكون الرموز المميزة أحرفًا مفردة مثل `z` أو كلمات كاملة مثل `cat`. يتم تقسيم الكلمات الطويلة إلى عدة رموز مميزة. تُعرف مجموعة جميع الرموز المميزة التي يستخدمها النموذج باسم المفردات، وتُعرف عملية تقسيم النص إلى رموز مميزة باسم *التقسيم إلى رموز مميزة*.

عند تفعيل الفوترة، يتم تحديد [تكلفة طلب البيانات من Gemini API](https://ai.google.dev/pricing?hl=ar) جزئيًا من خلال عدد الرموز المميزة للإدخال والإخراج، لذا قد يكون من المفيد معرفة كيفية عدّ الرموز المميزة.

## عدد الرموز المميّزة

يتم تحويل جميع البيانات المدخلة إلى واجهة Gemini API والناتجة عنها إلى رموز مميزة، بما في ذلك النصوص وملفات الصور وغيرها من الوسائط غير النصية.

يمكنك احتساب الرموز المميزة بالطرق التالية:

- **استدعاء الدالة `count_tokens` مع إدخال الطلب** تعرض هذه الدالة إجمالي عدد الرموز المميزة *في الإدخال فقط*. يجب إجراء هذه المكالمة قبل إرسال أي بيانات
  للتحقّق من حجم طلباتك.
- **استخدِم `usage` في ردّك على التفاعل.** تعرض هذه السمة عدد الرموز المميزة للإدخال (`total_input_tokens`) والإخراج (`total_output_tokens`) والتفكير (`total_thought_tokens`) والمحتوى المخزّن مؤقتًا (`total_cached_tokens`) واستخدام الأدوات (`total_tool_use_tokens`) والإجمالي (`total_tokens`).

### احتساب الرموز المميّزة للنص

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.6-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### عدّ الرموز المميّزة في المحادثات المترابطة

احتساب الرموز المميزة في سجلّ المحادثات باستخدام `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### احتساب الرموز المميّزة المتعددة الوسائط

يتم تحويل جميع البيانات المُدخلة إلى Gemini API إلى رموز مميزة، بما في ذلك الصور والفيديوهات والمحتوى الصوتي.
في ما يلي النقاط الرئيسية حول عملية الترميز:

- **الصور**: يتم احتساب الصور التي يبلغ حجمها 384 بكسل أو أقل في كلا البُعدين على أنّها 258 رمزًا مميزًا. يتم تقسيم الصور الأكبر حجمًا إلى مربّعات بحجم 768x768 بكسل، ويتم احتساب كل مربّع على أنّه 258 رمزًا مميزًا.
- **الفيديو**: 263 رمزًا مميزًا في الثانية
- **الصوت**: 32 رمزًا مميزًا في الثانية

#### رموز الصور المميزة

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.6-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**مثال على البيانات المضمّنة:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### رموز الفيديو المميّزة

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### الرموز الصوتية

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### احتساب الرموز المميزة لتعليمات النظام

يتم احتساب تعليمات النظام كجزء من الرموز المميزة للإدخال:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### رموز مميّزة لأداة الاحتساب

يتم أيضًا احتساب الأدوات (الدوال، وتنفيذ التعليمات البرمجية، و"بحث Google"):

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## قدرة الاستيعاب

لكل نموذج من نماذج Gemini حدّ أقصى لعدد الرموز المميزة التي يمكنه معالجتها. تحدّد نافذة السياق الحدّ الأقصى المسموح به لعدد الرموز المميزة في كل من الطلب والرد.

### الحصول على حجم قدرة الاستيعاب آليًا

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.6-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.6-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

يمكنك الاطّلاع على أحجام قدرة الاستيعاب في صفحة [النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

## الخطوات التالية

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar): الأساسيات
- [التخزين المؤقت](https://ai.google.dev/gemini-api/docs/caching?hl=ar): خفض التكاليف باستخدام التخزين المؤقت
- [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar): التعرّف على التكاليف

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
