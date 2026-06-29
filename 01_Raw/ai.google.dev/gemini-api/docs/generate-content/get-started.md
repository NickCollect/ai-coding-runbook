---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar
fetched_at: 2026-06-29T05:32:16.544581+00:00
title: "\u0627\u0644\u0628\u062f\u0621 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البدء

سيساعدك هذا الدليل في بدء استخدام واجهة برمجة التطبيقات القديمة **generateContent**. بالنسبة إلى المشاريع والتطبيقات الجديدة، ننصحك بشدة باستخدام **واجهة برمجة التطبيقات Interactions API** الجديدة بدلاً من ذلك، لأنّها توفّر واجهة مبسطة لسير العمل المستند إلى الوكلاء وأحدث النماذج.

يوضّح لك دليل البدء السريع هذا كيفية تثبيت
[المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar) وإجراء طلبك الأول، وبث الردود، وإنشاء محادثات مترابطة، واستخدام الأدوات باستخدام طريقة `generateContent` العادية.

## قبل البدء

لاستخدام Gemini API، يجب أن يكون لديك مفتاح واجهة برمجة تطبيقات للمصادقة على طلباتك وفرض حدود الأمان وتتبُّع الاستخدام في حسابك.

يمكنك إنشاء واحد مجانًا في AI Studio للبدء:

[إنشاء مفتاح لواجهة Gemini API](https://aistudio.google.com/apikey?hl=ar)

## تثبيت حزمة تطوير البرامج (SDK) من Google GenAI

### Python

باستخدام [Python 3.9 أو إصدار أحدث](https://www.python.org/downloads/)، ثبِّت حزمة
[`google-genai`](https://pypi.org/project/google-genai/)
باستخدام
[أمر pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) التالي:

```
pip install -q -U google-genai
```

### JavaScript

باستخدام [Node.js الإصدار 18 أو إصدار أحدث](https://nodejs.org/en/download/package-manager)،
ثبِّت
[حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي في TypeScript وJavaScript](https://www.npmjs.com/package/@google/genai)
باستخدام
[أمر npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) التالي:

```
npm install @google/genai
```

## إنشاء نص

استخدِم طريقة `models.generate_content` من أجل
[إنشاء ردّ نصي](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar).

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

### REST

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

تُرجع النماذج تلقائيًا ردًا بعد اكتمال عملية الإنشاء بأكملها. للحصول على تجربة أسرع وأكثر تفاعلية، يمكنك
[بث أجزاء الرد](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#stream) أثناء إنشائها.

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

### REST

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

## محادثات مترابطة

بالنسبة إلى المحادثات المترابطة، توفّر حِزم تطوير البرامج أداة مساعدة `chats` ذات حالة لإنشاء [تجربة محادثة مترابطة](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#chat) تدير سجلّ المحادثات تلقائيًا.

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

### REST

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
للوصول إلى محتوى الويب في الوقت الفعلي. يقرّر النموذج تلقائيًا متى يجب البحث، وينفّذ طلبات البحث، ويصوغ ردًا.

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

### REST

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

تتيح Gemini API أيضًا استخدام أدوات مضمّنة أخرى:

- **[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)**:
  تتيح هذه الميزة للنموذج كتابة رموز Python البرمجية وتشغيلها لحلّ المسائل الرياضية المعقّدة.
- **[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)**: يتيح لك
  تحديد أساس الردود في عناوين URL محدّدة لصفحات الويب تقدّمها.
- **[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)**: تتيح لك هذه الميزة تحميل الملفات وتحديد مصدر الردود من محتواها باستخدام البحث الدلالي.
- **[خرائط Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)**: تتيح لك
  تحديد أساس الردود استنادًا إلى بيانات الموقع الجغرافي والبحث عن أماكن واتجاهات وخرائط.
- **[استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar)**: تتيح هذه الميزة للنموذج التفاعل مع شاشة ولوحة مفاتيح وفأرة افتراضية على الكمبيوتر لتنفيذ المهام.

## استدعاء الدوال المخصّصة

استخدِم **[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)** لربط النماذج بأدواتك وواجهات برمجة التطبيقات المخصّصة. يحدّد النموذج الوقت المناسب لاستدعاء الدالة، ويعرض `functionCall` في الردّ ليتمكّن تطبيقك من تنفيذها.

يعرّف هذا المثال دالة وهمية لدرجة الحرارة ويتحقّق مما إذا كان النموذج يريد استدعاءها.

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

### REST

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

بعد أن بدأت استخدام واجهة Gemini API، يمكنك الاطّلاع على الأدلة التالية لإنشاء تطبيقات أكثر تقدّمًا:

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar)
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)
- [فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar)
- [التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar)
- [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
- [تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)
- [السياق الطويل](https://ai.google.dev/gemini-api/docs/long-context?hl=ar)
- [عمليات التضمين](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-24 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
