---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ar
fetched_at: 2026-05-18T05:07:05.692225+00:00
title: "\u0646\u0642\u0644 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0625\u0644\u0649 Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# نقل البيانات إلى Interactions API

يساعدك هذا الدليل في نقل البيانات من `generateContent` API إلى Interactions API.

‫Interactions API هي الواجهة العادية للتصميم باستخدام Gemini. وهي محسّنة لسير عمل الوكلاء وإدارة الحالة من جهة الخادم والمحادثات المعقّدة المتعدّدة الوسائط والمتعدّدة الجولات، مع مواصلة الدعم الكامل للطلبات البسيطة من جولة واحدة بدون حالة. على الرغم من أنّ `generateContent` لا تزال مدعومة بالكامل، ننصح باستخدام Interactions API لجميع عمليات التطوير الجديدة.

### لماذا يجب نقل البيانات؟

توفّر Interactions API طريقة أكثر تنظيمًا وفعالية للتصميم باستخدام Gemini:

- **إدارة السجلّ من جهة الخادم**: تبسيط تدفقات المحادثات المتعدّدة الجولات من خلال `previous_interaction_id` يُفعِّل الخادم الحالة تلقائيًا (`store=true`)، ولكن يمكنكم تفعيل السلوك بدون حالة من خلال ضبط `store=false`.
- **خطوات التنفيذ القابلة للمراقبة**: تسهّل الخطوات المكتوبة تصحيح الأخطاء في التدفقات المعقّدة وعرض واجهة المستخدم للأحداث الوسيطة (مثل الأفكار أو مربّعات البحث).
- **مصمّمة لسير عمل الوكلاء**: دعم أصلي لاستخدام الأدوات المتعدّدة الخطوات والتنسيق وتدفقات الاستنتاج المعقّدة من خلال خطوات التنفيذ المكتوبة
- **المهام الطويلة والمهام في الخلفية**: تتيح نقل العمليات التي تستغرق وقتًا طويلاً، مثل Deep Think وDeep Research، إلى عمليات الخلفية باستخدام `background=true`

## الإدخال/الإخراج الأساسي

يوضّح هذا القسم كيفية نقل طلب بسيط لإنشاء نص.

### قبل (`generateContent`)

‫`generateContent` API هي واجهة برمجة تطبيقات بدون حالة وتعرض الردّ مباشرةً. يغلّف بنية الردّ الناتج في قائمة `candidates`، يحتوي كل منها على `content` مع قائمة `parts` لتحليلها.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me a joke."
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "Tell me a joke.",
});
console.log(response.text);
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a joke."
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Why did the chicken cross the road? To get to the other side!"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 4,
    "candidatesTokenCount": 12,
    "totalTokenCount": 16
  }
}
```

### بعد (‫Interactions API)

تعرض Interactions API مورد تفاعل مخزّنًا مع مخطط زمني `steps`. بدلاً من الانتقال بين المرشّحين والأجزاء، افحصوا صفيف `steps` للعثور على نوع الناتج المطلوب.

### Python

```
from google import genai

client = genai.Client()

# The input can be a simple string shorthand
interaction = client.interactions.create(
    model="gemini-3-flash-preview", input="Tell me a joke."
)

# Inspect the steps manually
for step in interaction.steps:
    if step.type == "model_output":
        print(step.content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a joke.'
});

// Manual inspection
const modelStep = interaction.steps.find(s => s.type === 'model_output');
console.log(modelStep.content[0].text);
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a joke."
}'

# Response
{
  "id": "int_123",
  "status": "completed",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Tell me a joke."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

## محادثات متعدّدة الجولات

تخزِّن Interactions API التفاعلات تلقائيًا، ما يتيح إدارة الحالة من جهة الخادم للمحادثات المتعدّدة الجولات.

### قبل (`generateContent`)

في `generateContent`، يجب إدارة سجلّ المحادثات يدويًا باستخدام صفيف `contents` أو أداة مساعدة للدردشة من جهة العميل.

### Python

**استخدام أداة مساعدة للدردشة (الخيار الذي ننصح به)**

```
from google import genai

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash")
response1 = chat.send_message("Hi, my name is Phil.")
print(response1.text)

response2 = chat.send_message("What is my name?")
print(response2.text)
```

**إدارة السجلّ يدويًا**

```
from google import genai
from google.genai import types

client = genai.Client()

# The second turn requires sending the entire history
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user", parts=[types.Part.from_text("Hi, my name is Phil.")]
        ),
        types.Content(
            role="model",
            parts=[types.Part.from_text("Hi Phil, how can I help you?")],
        ),
        types.Content(
            role="user", parts=[types.Part.from_text("What is my name?")]
        ),
    ],
)
print(response.text)
```

### JavaScript

**استخدام أداة مساعدة للدردشة (الخيار الذي ننصح به)**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const chat = client.chats.create({ model: 'gemini-2.5-flash' });
let response = await chat.sendMessage({ message: 'Hi, my name is Phil.' });
console.log(response.text);

response = await chat.sendMessage({ message: 'What is my name?' });
console.log(response.text);
```

**إدارة السجلّ يدويًا**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// The second turn requires sending the entire history
const response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [
        { role: 'user', parts: [{ text: 'Hi, my name is Phil.' }] },
        { role: 'model', parts: [{ text: 'Hi Phil, how can I help you?' }] },
        { role: 'user', parts: [{ text: 'What is my name?' }] }
    ]
});
console.log(response.text);
```

### راحة

```
# Request (the second turn requires sending the entire history)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [
        {"role": "user", "parts": [{"text": "Hi, my name is Phil."}]},
        {"role": "model", "parts": [{"text": "Hi Phil, how can I help you?"}]},
        {"role": "user", "parts": [{"text": "What is my name?"}]}
    ]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Your name is Phil."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### بعد (‫Interactions API)

تُدير Interactions API الحالة على الخادم. يمكنكم مواصلة المحادثة من خلال الإشارة إلى `previous_interaction_id`.

### Python

```
from google import genai

client = genai.Client()

# First turn
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview", input="Hi, my name is Phil."
)
print(interaction1.steps[-1].content[0].text)

# Second turn (passing previous_interaction_id)
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction1.id,
    input="What is my name?",
)
print(interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// First turn
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Hi, my name is Phil.'
});
console.log(interaction.steps.at(-1).content[0].text);

// Second turn
interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction.id,
    input: 'What is my name?'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### راحة

```
# First Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Hi, my name is Phil."
}'

# Second Request (using ID from first response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "int_123",
    "input": "What is my name?"
}'

# Response to Second Request
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Hi, my name is Phil." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Hello Phil! How can I help you today?" }]
    },
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "What is my name?" }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Your name is Phil." }]
    }
  ]
}
```

## إدخالات متعددة الوسائط

تتيح كلتا واجهتَي برمجة التطبيقات إدخالات متعددة الوسائط (نصوص وصور وفيديوهات وما إلى ذلك).

### قبل (`generateContent`)

في `generateContent`، يتم تمرير قائمة `parts` ضمن صفيف `contents`. يعرض الردّ الناتج في `parts` من المرشّح الأول.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Describe this image.",
    ],
)
print(response.text)
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [
            {
                "inlineData": {
                    "mimeType": "image/jpeg",
                    "data": "..."
                }
            },
            {
                "text": "Describe this image."
            }
        ]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "This is a picture of a beautiful sunset."
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### بعد (‫Interactions API)

في Interactions API، يتم تمرير صفيف إلى حقل `input`. يمكنكم استرداد محتوى الناتج من خلال العثور على خطوة `model_output` في المخطط الزمني.

### Python

```
from google import genai

client = genai.Client()

# Assuming you have an image file
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_bytes,
        },
        {"type": "text", "text": "Describe this image."},
    ],
)
for step in interaction.steps:
    if step.type == "model_output":
        print(step.content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        {
            type: 'image',
            mime_type: 'image/jpeg',
            data: imageBytes
        },
        {
            type: 'text',
            text: 'Describe this image.'
        }
    ]
});
for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        console.log(step.content[0].text);
    }
}
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "..."
        },
        {
            "type": "text",
            "text": "Describe this image."
        }
    ]
}'

# Response
{
  "id": "int_multimodal",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "..."
        },
        {
          "type": "text",
          "text": "Describe this image."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "This is a picture of a beautiful sunset over the mountains."
        }
      ]
    }
  ]
}
```

## ناتج منظَّم

لجعل النموذج يعرض JSON يطابق مخططًا معيّنًا، يجب ضبط تنسيق الردّ.

### قبل (`generateContent`)

في `generateContent`، يتم ضبط تنسيق الناتج باستخدام حقل `response_format` المضمّن داخل عنصر `generationConfig`.

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me a recipe for chocolate chip cookies.",
    config=types.GenerateContentConfig(
        response_format=[
            {
                "type": "text",
                "mime_type": "application/json",
                "schema": Recipe,
            }
        ]
    ),
)
print(response.text)
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Give me a recipe for chocolate chip cookies."
        }]
    }],
    "generationConfig": {
        "responseFormat": [
            {
                "type": "text",
                "mimeType": "application/json",
                "schema": {
                    "type": "OBJECT",
                    "properties": {
                        "recipe_name": { "type": "STRING" },
                        "ingredients": {
                            "type": "ARRAY",
                            "items": { "type": "STRING" }
                        }
                    },
                    "required": ["recipe_name", "ingredients"]
                }
            }
        ]
    }
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### بعد (‫Interactions API)

في Interactions API، تنتقل عناصر التحكّم في تنسيق الناتج إلى صفيف `response_format` على المستوى الأعلى.

### Python

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Give me a recipe for chocolate chip cookies.",
    response_format=[
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": Recipe,
        }
    ],
)

for step in interaction.steps:
    if step.type == "model_output":
        print(step.content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Give me a recipe for chocolate chip cookies.',
    response_format: [
        {
            type: 'text',
            mime_type: 'application/json',
            schema: {
                type: 'object',
                properties: {
                    recipe_name: { type: 'string' },
                    ingredients: {
                        type: 'array',
                        items: { type: 'string' }
                    }
                },
                required: ['recipe_name', 'ingredients']
            }
        }
    ]
});
for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        console.log(step.content[0].text);
    }
}
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Give me a recipe for chocolate chip cookies.",
    "response_format": [
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": {
                "type": "OBJECT",
                "properties": {
                    "recipe_name": { "type": "STRING" },
                    "ingredients": {
                        "type": "ARRAY",
                        "items": { "type": "STRING" }
                    }
                },
                "required": ["recipe_name", "ingredients"]
            }
        }
    ]
}'

# Response
{
  "id": "int_structured",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Give me a recipe for chocolate chip cookies." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
        }
      ]
    }
  ]
}
```

## إنشاء محتوى متعدد الوسائط

عند إنشاء محتوى بتنسيقات أخرى غير النص (مثل الصور أو الصوت)، يكمن الاختلاف الأساسي في كيفية تنظيم الردّ للوسائط التي تم إنشاؤها.

### قبل (`generateContent`)

في `generateContent`، يعرض الردّ الوسائط التي تم إنشاؤها مباشرةً في `parts` من المرشّح، عادةً كبيانات base64 في `inlineData`.

```
# Response structure concept
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Here is your generated image:"
          },
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "...base64..."
            }
          }
        ]
      }
    }
  ]
}
```

### بعد (‫Interactions API)

في Interactions API، تظهر الوسائط التي تم إنشاؤها كعناصر مميّزة ضمن صفيف `content` لخطوة `model_output` في المخطط الزمني، ما يحافظ على التدفق الزمني للتفاعل.

```
# Response structure concept
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Here is your generated image:"
        },
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "...base64..." // Or a reference URL in future
        }
      ]
    }
  ]
}
```

يضمن ذلك أن يكون تحليل الردّ متسقًا مع طريقة التعامل مع الإدخالات والنواتج النصية، إذ يمثّل كل عنصر خطوة في المخطط الزمني.

## أدوات من جهة الخادم

تتيح Gemini أدوات مضمّنة من جهة الخادم، مثل ميزة تحديد مصدر المعلومات الخاصة بـ "بحث Google". ويكمن الاختلاف الأساسي في كيفية تمثيل الردّ لتنفيذ الأداة.

### قبل (`generateContent`)

في `generateContent`، تكون الأدوات من جهة الخادم غير واضحة إلى حد كبير. يمكنكم تفعيل الأداة والحصول على إجابة نهائية باستخدام عنصر `groundingMetadata` منفصل. الأهم من ذلك أنّ الاقتباسات ليست مضمّنة، إذ تستخدم `groundingSupports` مؤشرات الأحرف لربط أجزاء النص بمصادر الويب في `groundingChunks`.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}]
    ),
)

# Access search entry point (widget) and citations
metadata = response.candidates[0].grounding_metadata
if metadata.search_entry_point:
    print(f"Search Entry Point: {metadata.search_entry_point.rendered_content}")

for support in metadata.grounding_supports:
    print(f"Citation: {support.segment.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: 'Who won Euro 2024?',
    config: {
        tools: [{ google_search: {} }]
    }
});

const metadata = response.candidates[0].groundingMetadata;
if (metadata.searchEntryPoint) {
    console.log(`Search Entry Point: ${metadata.searchEntryPoint.renderedContent}`);
}
for (const support of metadata.groundingSupports) {
    console.log(`Citation: ${support.segment.text}`);
}
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Who won Euro 2024?"
        }]
    }],
    "tools": [{
        "googleSearchRetrieval": {}
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

### بعد (‫Interactions API)

في Interactions API، توفّر الأدوات من جهة الخادم شفافية كاملة للمخطط الزمني. تسجِّل واجهة برمجة التطبيقات الطلب والنتيجة كـ `steps` تنفيذ مميّزة (`google_search_call` و`google_search_result`)، ما يكشف عن البيانات التي استردّها النموذج بالضبط.

علاوةً على ذلك، تعرض واجهة برمجة التطبيقات الاقتباسات **مضمّنة**. بدلاً من ربط المؤشرات من عنصر بيانات وصفية منفصل، يحتوي عنصر النص ضمن خطوة `model_output` على صفيف `annotations` خاص به يرتبط مباشرةً بالمصدر.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won Euro 2024?",
    tools=[{"type": "google_search"}],
)

for step in interaction.steps:
    if step.type == "google_search_result":
        print(f"Search Suggestions: {step.search_suggestions}")
    elif step.type == "model_output":
        print(f"Answer: {step.content[0].text}")
        if step.content[0].annotations:
            for anno in step.content[0].annotations:
                print(f"Citation: {anno.title} ({anno.uri})")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Who won Euro 2024?',
    tools: [{ type: 'google_search' }]
});

for (const step of interaction.steps) {
    if (step.type === 'google_search_result') {
        console.log(`Search Suggestions: ${step.search_suggestions}`);
    } else if (step.type === 'model_output') {
        console.log(`Answer: ${step.content[0].text}`);
        if (step.content[0].annotations) {
            for (const anno of step.content[0].annotations) {
                console.log(`Citation: ${anno.title} (${anno.uri})`);
            }
        }
    }
}
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won Euro 2024?",
    "tools": [{"type": "google_search"}]
}'

# Response (showing grounding)
{
  "id": "int_grounded",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Who won Euro 2024?" }]
    },
    {
      "type": "google_search_call",
      "status": "done",
      "content": [{ "type": "text", "text": "UEFA Euro 2024 winner" }]
    },
    {
      "type": "google_search_result",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024..." 
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1.",
          "annotations": [
            {
              "start_index": 0,
              "end_index": 42,
              "uri": "https://vertexaisearch...",
              "title": "aljazeera.com"
            }
          ]
        }
      ]
    }
  ]
}
```

## استدعاء الدالة

تغيّرت أيضًا بنية استدعاءات الدوال ونتائجها لتناسب مخطط الخطوات.

### قبل (`generateContent`)

في `generateContent`، يعرض الردّ استدعاءات الدوال ضمن المرشّحين.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Step 1: Send prompt with tools
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

# Assume model returned function_call
function_call = response.candidates[0].content.parts[0].function_call
print(f"Requested tool: {function_call.name}")

# Step 2: Execute local function and send result back
result = "52°F and rain"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="What's the weather in Boston?")
            ],
        ),
        response.candidates[0].content,  # Model turn with function call
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result},
                )
            ],
        ),
    ],
    config=types.GenerateContentConfig(tools=[weather_tool]),
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// Step 1: Send prompt with tools
let response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

const functionCall = response.candidates[0].content.parts[0].functionCall;
console.log(`Requested tool: ${functionCall.name}`);

// Step 2: Execute local function and send result back
const result = "52°F and rain";

response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [
        { role: 'user', parts: [{ text: "What's the weather in Boston?" }] },
        response.candidates[0].content, // Model turn
        {
            role: 'user',
            parts: [{
                functionResponse: {
                    name: functionCall.name,
                    response: { result: result }
                }
            }]
        }
    ],
    config: { tools: [weatherTool] }
});
console.log(response.text);
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "What is the weather like in Boston, MA?"
        }]
    }],
    "tools": [{
        "functionDeclarations": [{
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "location": {"type": "STRING"}
                },
                "required": ["location"]
            }
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "functionCall": {
              "name": "get_weather",
              "args": { "location": "Boston, MA" }
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### بعد (‫Interactions API)

أصبحت الآن استدعاءات الأدوات ونتائجها خطوات مميّزة في المخطط الزمني.

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets weather",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the weather in Boston?",
    tools=[weather_tool],
)

# Check if the model requested a tool call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Executing {step.name} for {step.arguments}")

        # Execute your local function here...
        result = "52°F and rain"

        # Submit the result back as a step
        interaction = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            input=[
                {
                    "type": "function_result",
                    "call_id": step.id,
                    "name": step.name,
                    "result": [{"type": "text", "text": result}],
                }
            ],
        )
        # Inspect steps for final response
        for s in interaction.steps:
            if s.type == "model_output":
                print(s.content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get weather for a location",
    parameters: {
        type: "object",
        properties: {
            location: { type: "string" }
        },
        required: ["location"]
    }
};

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What's the weather in Boston?",
    tools: [weatherTool]
});

// Check if the model requested a tool call
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Executing ${step.name} for ${JSON.stringify(step.arguments)}`);

        const result = "52°F and rain";

        // Submit the result back as a step
        const nextInteraction = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            previous_interaction_id: interaction.id,
            input: [
                {
                    type: 'function_result',
                    call_id: step.id,
                    name: step.name,
                    result: [{ type: 'text', text: result }]
                }
            ]
        });

        // Inspect steps for final response
        for (const s of nextInteraction.steps) {
            if (s.type === 'model_output') {
                console.log(s.content[0].text);
            }
        }
    }
}
```

### راحة

```
# Initial Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What's the weather in Boston?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": { "type": "string" }
            },
            "required": ["location"]
        }
    }]
}'

# Response (requires action)
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        { "type": "text", "text": "What's the weather in Boston?" }
      ]
    },
    {
      "type": "function_call",
      "status": "waiting",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}

# Submit Tool Result Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "int_001",
    "input": {
        "type": "function_result",
        "call_id": "fc_1",
        "name": "get_weather",
        "result": [
            { "type": "text", "text": "52°F with rain" }
        ]
    }
}'

# Final Response
{
  "id": "int_002",
  "status": "completed",
  "steps": [
    {
      "type": "function_result",
      "call_id": "fc_1",
      "name": "get_weather",
      "result": [
        { "type": "text", "text": "52°F with rain" }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        { "type": "text", "text": "It's 52°F with rain in Boston." }
      ]
    }
  ]
}
```

## البث

يكمن الاختلاف الرئيسي في البث في أنّ Interactions API تستخدم نقطة النهاية نفسها مع `"stream": true` في نص الطلب، بينما تتطلّب `generateContent` API استدعاء نقطة نهاية مخصّصة (`:streamGenerateContent`).

بالإضافة إلى ذلك، تستخدم أحداث البث الآن أنواعًا متخصّصة لمراقبة دورة حياة التفاعل وتتبُّع خطوات التنفيذ على طول المخطط الزمني.

### قبل (`generateContentStream`)

باستخدام `generateContent`، يتم استهلاك سلسلة من أجزاء الردّ.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-2.5-flash", contents="Tell me a story"
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
const responseStream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash',
    contents: 'Tell me a story',
});
for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
}
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a story"
        }]
    }]
}'

# Response stream
event: content.start
data: {"event_type": "content.start", "index": 0, "content": {"type": "thought"}}
event: content.delta
data: {"event_type": "content.delta", "index": 0, "delta": {"type": "thought_summary", "text": "User wants an explanation."}}
event: content.stop
data: {"event_type": "content.stop", "index": 0}
event: content.start
data: {"event_type": "content.start", "index": 1, "content": {"type": "text"}}
event: content.delta
data: {"event_type": "content.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: content.stop
data: {"event_type": "content.stop", "index": 1}
```

### بعد (‫Interactions API)

في Interactions API، يستخدم البث أحداثًا يتم إرسالها من الخادم (SSE) وأنواعًا متخصّصة من التغييرات الجزئية لتمثيل خطوات التنفيذ أثناء حدوثها.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a story",
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\n--- Stream Finished ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a story',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {
        if (event.delta.type === 'text' && 'text' in event.delta) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n\n--- Stream Finished ---');
    }
}
```

### راحة

# Example SSE stream output
**event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int\_xyz", "status": "created"}}
event: interaction.in\_progress
data: {"type": "interaction.in\_progress", "interaction": {"id": "int\_xyz", "status": "in\_progress"}}
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}
event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "User wants an explanation."}}
event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}}
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "model\_output"}}
event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: step.stop
data: {"type": "step.stop", "index": 1, "status": "done"}}
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int\_xyz", "status": "completed", "usage": {"prompt\_tokens": 10, "completion\_tokens": 5, "total\_tokens": 15}}}**
```

### أدوات البث واستدعاءات الدوال

تغيّرت طريقة عمل الأدوات في البث بشكلٍ كبير من `generateContent` لتوفير تحكّم ورؤية أكثر دقة.

#### قبل (`generateContent`)

باستخدام `generateContent`، كانت استدعاءات الدوال التي يتم بثها تصل كاملةً في جزء واحد. لم يكن بإمكانكم الاطّلاع على الوسيطات التي يتم إنشاؤها في الوقت الفعلي، لذا كان معالج الأحداث يتحقّق ببساطة من وجود عنصر `functionCall` كامل.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

for chunk in stream:
    # Function calls arrived complete — no partial arguments
    if chunk.candidates[0].content.parts[0].function_call:
        fc = chunk.candidates[0].content.parts[0].function_call
        print(f"Call: {fc.name}({fc.args})")
    elif chunk.text:
        print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

for await (const chunk of stream) {
    // Function calls arrived complete — no partial arguments
    const part = chunk.candidates[0].content.parts[0];
    if (part.functionCall) {
        console.log(`Call: ${part.functionCall.name}(${JSON.stringify(part.functionCall.args)})`);
    } else if (part.text) {
        process.stdout.write(part.text);
    }
}
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{"parts": [{"text": "What'\''s the weather in Boston?"}]}],
    "tools": [{"functionDeclarations": [{"name": "get_weather", "parameters": {"type": "OBJECT", "properties": {"location": {"type": "STRING"}}}}]}]
}'

# Response stream — function call arrives complete in one chunk
{"candidates": [{"content": {"parts": [{"functionCall": {"name": "get_weather", "args": {"location": "Boston, MA"}}}]}}]}
```

#### بعد (‫Interactions API)

تبث Interactions API وسيطات استدعاء الدوال حرفًا بحرف كأحداث `arguments`. تظهر دورة حياة الأداة بأكملها، بما في ذلك الفكرة والاستدعاء والنتيجة والناتج، كسلسلة من الخطوات المميّزة.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the weather in Boston?",
    tools=[get_weather_tool],
    stream=True,
)

for event in stream:
    if event.event_type == "step.start":
        if event.step.type == "function_call":
            print(f"Calling: {event.step.name}")
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments":
            print(f"  args: {event.delta.partial_arguments}")
        elif event.delta.type == "text":
            print(event.delta.text, end="")
    elif event.event_type == "interaction.completed":
        print("\n--- Done ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What's the weather in Boston?",
    tools: [getWeatherTool],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.start') {
        if (event.step.type === 'function_call') {
            console.log(`Calling: ${event.step.name}`);
        }
    } else if (event.event_type === 'step.delta') {
        if (event.delta.type === 'arguments') {
            console.log(`  args: ${event.delta.partial_arguments}`);
        } else if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n--- Done ---');
    }
}
```

### راحة

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What'\''s the weather in Boston?",
    "tools": [{"type": "function", "name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}],
    "stream": true
}'

# Response stream
// Interaction created
event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int_xyz", "status": "created"}}

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "The user wants weather data for Boston. I'll call the get_weather tool."}}

event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}

// ── Step 1: Function Call (arguments streamed) ───────
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "function_call", "id": "fc_1", "name": "get_weather"}}

event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "arguments", "partial_arguments": "{\"location\": \"Boston, MA\"}"}}

event: step.stop
data: {"type": "step.stop", "index": 1, "status": "waiting"}

// The interaction pauses — the model needs the tool result before continuing.
event: interaction.requires_action
data: {"type": "interaction.requires_action", "interaction": {"id": "int_xyz", "status": "requires_action"}}

// ── (Client submits the tool result) ──────────────────
// The client calls interactions.create with the function_result as input
// and the previous interaction's ID, then resumes consuming the stream.

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 2: Function Result (echoed back, no deltas) ─
event: step.start
data: {"type": "step.start", "index": 2, "step": {"type": "function_result", "call_id": "fc_1", "name": "get_weather", "result": [{"type": "text", "text": "52°F, rain"}]}}

event: step.stop
data: {"type": "step.stop", "index": 2, "status": "done"}

// ── Step 3: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 3, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 3, "delta": {"type": "thought", "text": "Got weather data. Composing the final response."}}

event: step.stop
data: {"type": "step.stop", "index": 3, "status": "done"}

// ── Step 4: Model Output (text streamed) ─────────────
event: step.start
data: {"type": "step.start", "index": 4, "step": {"type": "model_output"}}

event: step.delta
data: {"type": "step.delta", "index": 4, "delta": {"type": "text", "text": "It's currently 52°F and rainy in Boston."}}

event: step.stop
data: {"type": "step.stop", "index": 4, "status": "done"}

// ── Interaction complete ─────────────────────────────
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 256, "completion_tokens": 128, "total_tokens": 384}}}
```

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-17 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-17 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
