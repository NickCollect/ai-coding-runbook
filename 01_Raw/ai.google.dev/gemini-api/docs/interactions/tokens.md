---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ar
fetched_at: 2026-05-18T05:12:40.904367+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الرموز المميّزة وعدّها

تعالج نماذج Gemini ونماذج الذكاء الاصطناعي التوليدي الأخرى الإدخالات والإخراجات بدقة تُعرف باسم *الرمز المميّز*.

**بالنسبة إلى نماذج Gemini، يعادل الرمز المميّز 4 أحرف تقريبًا.
ويعادل 100 رمز مميّز من 60 إلى 80 كلمة باللغة الإنجليزية تقريبًا.**

## لمحة عن الرموز المميّزة

يمكن أن تكون الرموز المميّزة أحرفًا مفردة، مثل `z`، أو كلمات كاملة، مثل `cat`. ويتم تقسيم الكلمات الطويلة إلى عدة رموز مميّزة. تُعرف مجموعة جميع الرموز المميّزة التي يستخدمها النموذج باسم المفردات، وتُعرف عملية تقسيم النص إلى رموز مميّزة باسم *الترميز*.

عند تفعيل الفوترة، يتم تحديد [تكلفة طلب البيانات من Gemini API](https://ai.google.dev/pricing?hl=ar) جزئيًا حسب عدد الرموز المميّزة للإدخال والإخراج، لذا قد يكون من المفيد معرفة كيفية
عدّ الرموز المميّزة.

## عدّ الرموز المميّزة

يتم ترميز جميع الإدخالات والإخراجات من Gemini API، بما في ذلك النصوص وملفات الصور والوسائط الأخرى غير النصية.

يمكنك عدّ الرموز المميّزة بالطرق التالية:

- **استدعاء `count_tokens` مع إدخال الطلب** تعرض هذه الدالة إجمالي عدد الرموز المميّزة في *الإدخال فقط*. يمكنك إجراء هذا الاستدعاء قبل إرسال الإدخال للتحقّق من حجم طلباتك.
- **استخدام `usage` في استجابة التفاعل.** تعرض هذه الدالة أعداد الرموز المميّزة للإدخال (`total_input_tokens`) والإخراج (`total_output_tokens`) والتفكير (`total_thought_tokens`) والمحتوى المخزّن مؤقتًا (`total_cached_tokens`) واستخدام الأدوات (`total_tool_use_tokens`) والإجمالي (`total_tokens`).

### عدّ الرموز المميّزة للنص

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### عدّ الرموز المميّزة للمحادثات المتعددة الأدوار

يمكنك عدّ الرموز المميّزة في سجلّ المحادثات باستخدام `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### عدّ الرموز المميّزة المتعددة الوسائط

يتم ترميز جميع الإدخالات إلى Gemini API، بما في ذلك الصور والفيديوهات والمحتوى الصوتي.
في ما يلي نقاط أساسية حول الترميز:

- **الصور**: يتم احتساب 258 رمزًا مميّزًا للصور التي يبلغ حجمها ‎384 × 384 بكسل أو أقل في كلا البُعدَين. ويتم تقسيم الصور الأكبر حجمًا إلى مربّعات بحجم ‎768 × 768 بكسل، ويتم احتساب 258 رمزًا مميّزًا لكل مربّع.
- **الفيديوهات**: 263 رمزًا مميّزًا في الثانية
- **المحتوى الصوتي**: 32 رمزًا مميّزًا في الثانية

#### الرموز المميّزة للصور

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
    model="gemini-3-flash-preview",
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

#### الرموز المميّزة للفيديوهات

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
    model="gemini-3-flash-preview",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### الرموز المميّزة للمحتوى الصوتي

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### عدّ الرموز المميّزة لتعليمات النظام

يتم عدّ تعليمات النظام كجزء من الرموز المميّزة للإدخال:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### عدّ الرموز المميّزة للأدوات

يتم أيضًا عدّ الأدوات (الدوال وتنفيذ التعليمات البرمجية و"بحث Google"):

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
    model="gemini-3-flash-preview",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## قدرة الاستيعاب

لكل نموذج من نماذج Gemini عدد أقصى من الرموز المميّزة التي يمكنه معالجتها. وتحدّد قدرة الاستيعاب الحدّ المجمّع للرموز المميّزة للإدخال والإخراج.

### الحصول على حجم قدرة الاستيعاب آليًا

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3-flash-preview")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3-flash-preview" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

يمكنك الاطّلاع على أحجام قدرة الاستيعاب في صفحة [النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

## الخطوات التالية

- [إنشاء النص](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar): أساسيات الإنشاء
- [التخزين المؤقت](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=ar): خفض التكاليف باستخدام التخزين المؤقت
- [التسعير](https://ai.google.dev/gemini-api/docs/pricing?hl=ar): التعرّف على التكاليف

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
