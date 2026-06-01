---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=ar
fetched_at: 2026-06-01T06:08:18.602939+00:00
title: "\u0627\u0644\u0628\u062f\u0621 \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u062a\u0637\u0628\u064a\u0642\u0627\u062a Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البدء السريع لواجهة برمجة تطبيقات Gemini

يوضّح لك دليل البدء السريع هذا كيفية تثبيت مكتباتنا
 وتقديم أول طلب وعرض الردود تدريجيًا وإنشاء محادثات متعدّدة الجولات واستخدام الأدوات باستخدام الطريقة العادية
`generateContent`.

## قبل البدء

لاستخدام Gemini API، يجب أن يكون لديك مفتاح واجهة برمجة تطبيقات للمصادقة على طلباتك وفرض حدود الأمان وتتبُّع الاستخدام في حسابك.

يمكنك إنشاء مفتاح واجهة برمجة تطبيقات مجانًا على AI Studio للبدء:

[إنشاء مفتاح Gemini API](https://aistudio.google.com/app/apikey?hl=ar)

## تثبيت حزمة Google GenAI SDK

### Python

باستخدام [Python 3.9 أو إصدار أحدث](https://www.python.org/downloads/)، ثبِّت حزمة
[`google-genai` باستخدام](https://pypi.org/project/google-genai/)
أمر
[pip التالي](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

باستخدام [Node.js الإصدار 18 أو إصدار أحدث](https://nodejs.org/en/download/package-manager)،
ثبِّت
[حزمة Google Gen AI SDK لـ TypeScript وJavaScript](https://www.npmjs.com/package/@google/genai)
باستخدام
[أمر npm التالي](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

## إنشاء نص

استخدِم طريقة `models.generate_content` لـ
[إنشاء رد نصي](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### راحة

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## عرض الردود تدريجيًا

لا يعرض النموذج ردًا تلقائيًا إلا بعد اكتمال عملية الإنشاء بأكملها. للحصول على تجربة أسرع وأكثر تفاعلية، يمكنك
[عرض أجزاء الرد](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#stream) تدريجيًا أثناء
إنشائها.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### راحة

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## محادثات متعدّدة الجولات

بالنسبة إلى المحادثات المتعدّدة الجولات، توفّر حزم SDK أداة مساعدة `chats` ذات حالة لـ
إنشاء تجربة محادثة [متعدّدة الجولات](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#chat)
تدير تلقائيًا سجلّ المحادثات.

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### راحة

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## استخدام الأدوات

يمكنك توسيع إمكانات النموذج من خلال
[تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)
للوصول إلى محتوى الويب في الوقت الفعلي. يقرّر النموذج تلقائيًا متى يبحث وينفّذ طلبات البحث ويُنشئ ردًا.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### راحة

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

تتوافق Gemini API أيضًا مع الأدوات المضمّنة الأخرى:

- **[تنفيذ الرمز](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)**:
  يتيح للنموذج كتابة رمز Python وتشغيله لحلّ المسائل الرياضية المعقّدة.
- **[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)**: يتيح لك
  تحديد مصدر الردود في عناوين URL معيّنة لصفحات الويب تقدّمها.
- **[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)**: يتيح لك
  تحميل الملفات وتحديد مصدر الردود في محتواها باستخدام البحث الدلالي.
- **[خرائط Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)**: يتيح لك
  تحديد مصدر الردود في بيانات الموقع الجغرافي والبحث عن الأماكن والاتجاهات و
  الخرائط.
- **[استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar)**: يتيح للنموذج التفاعل مع شاشة الكمبيوتر ولوحة المفاتيح والفأرة الافتراضية لتنفيذ المهام.

## استدعاء الدوال المخصّصة

استخدِم **[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)** لربط
النماذج بأدواتك وواجهات برمجة التطبيقات المخصّصة. يحدّد النموذج متى يستدعي دالتك ويعرض `functionCall` في الرد لتنفيذه في تطبيقك.

يعلن هذا المثال عن دالة وهمية لدرجة الحرارة ويتحقّق مما إذا كان النموذج يريد استدعاءها.

### Python

```
from google import genai
from google.genai import types

weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### راحة

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## الخطوات التالية

بعد أن بدأت استخدام Gemini API، استكشِف الأدلة التالية لإنشاء تطبيقات أكثر تقدّمًا:

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar)
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)
- [فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar)
- [طريقة التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar)
- [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
- [تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)
- [سياق طويل](https://ai.google.dev/gemini-api/docs/long-context?hl=ar)
- [المتجهات الدلالية](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-28 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-28 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
