---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar
fetched_at: 2026-06-22T06:25:45.326134+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u0627\u062f \u0625\u0644\u0649 \"\u062e\u0631\u0627\u0626\u0637 Google\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستناد إلى "خرائط Google"

يتيح استخدام "خرائط Google" كمصدر ربط إمكانات الذكاء الاصطناعي التوليدي في Gemini بالبيانات الغنية والواقعية والحديثة في "خرائط Google". تتيح هذه الميزة للمطوّرين دمج وظائف تستند إلى الموقع الجغرافي في تطبيقاتهم بسهولة. عندما يتضمّن طلب بحث المستخدم سياقًا مرتبطًا ببيانات &quot;خرائط Google&quot;، يستفيد نموذج Gemini من &quot;خرائط Google&quot; لتقديم إجابات دقيقة وحديثة وذات صلة بالموقع الجغرافي المحدّد أو المنطقة العامة التي ذكرها المستخدم.

- **ردود دقيقة ومراعية للموقع الجغرافي:** يمكنك الاستفادة من بيانات &quot;خرائط Google&quot; الشاملة والحديثة للاستعلامات الخاصة بمواقع جغرافية معيّنة.
- **التخصيص المحسّن:** تخصيص الاقتراحات والمعلومات استنادًا إلى المواقع الجغرافية المقدَّمة من المستخدِم

## البدء

يوضّح هذا المثال كيفية دمج ميزة استخدام "خرائط Google" كمصدر في تطبيقك لتقديم ردود دقيقة ومراعية للموقع الجغرافي على طلبات المستخدمين. يطلب الطلب الحصول على اقتراحات محلية مع تحديد موقع جغرافي اختياري للمستخدم، ما يتيح لنموذج Gemini استخدام بيانات &quot;خرائط Google&quot;.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## طريقة عمل ميزة "استخدام خرائط Google كمصدر"

تدمج ميزة استخدام "خرائط Google" كمصدر واجهة Gemini API مع نظام Google Geo البيئي من خلال استخدام Maps API كمصدر للاستناد إلى مصادر خارجية. عندما يتضمّن طلب المستخدم سياقًا جغرافيًا، يمكن لنموذج Gemini استخدام أداة &quot;الاستناد إلى بيانات واقعية&quot; في &quot;خرائط Google&quot;. يمكن للنموذج بعد ذلك إنشاء ردود استنادًا إلى بيانات &quot;خرائط Google&quot; ذات الصلة بالموقع الجغرافي المقدَّم.

تتضمّن العملية عادةً ما يلي:

1. **طلب بحث المستخدم:** يرسل المستخدم طلب بحث إلى تطبيقك، وقد يتضمّن سياقًا جغرافيًا (مثل "مقاهي بالقرب مني" أو "متاحف في سان فرانسيسكو").
2. **استدعاء الأداة:** يستدعي نموذج Gemini أداة Grounding with Google Maps بعد التعرّف على النية الجغرافية. يمكنك اختياريًا تزويد هذه الأداة `latitude` و`longitude` الخاصين بالمستخدم. الأداة هي أداة بحث نصي وتعمل بشكل مشابه للبحث على &quot;خرائط Google&quot;، إذ إنّ طلبات البحث المحلية (&quot;بالقرب مني&quot;) ستستخدم الإحداثيات، بينما من غير المرجّح أن تتأثر طلبات البحث المحدّدة أو غير المحلية بالموقع الجغرافي الواضح.
3. **استرداد البيانات:** تستعلم خدمة استخدام "خرائط Google" كمصدر من "خرائط Google" عن المعلومات ذات الصلة (مثل الأماكن والمراجعات والصور والعناوين وساعات العمل).
4. **الإنشاء المستند إلى مصادر:** يتم استخدام بيانات &quot;خرائط Google&quot; التي تم استرجاعها لإبلاغ ردّ نموذج Gemini، ما يضمن دقة المعلومات ومدى صلتها بالموضوع.
5. **الردّ:** يعرض النموذج ردًا نصيًا يتضمّن اقتباسات من مصادر &quot;خرائط Google&quot;.

## أسباب استخدام ميزة "استخدام "خرائط Google" كمصدر" وحالات استخدامها

يُعدّ استخدام &quot;خرائط Google&quot; كمصدر مثاليًا للتطبيقات التي تتطلّب معلومات دقيقة وحديثة وخاصة بالموقع الجغرافي. تعمل هذه الميزة على تحسين تجربة المستخدم من خلال توفير محتوى ملائم ومخصّص استنادًا إلى قاعدة بيانات &quot;خرائط Google&quot; الشاملة التي تضم أكثر من 250 مليون مكان حول العالم.

عليك استخدام Grounding with Google Maps عندما يحتاج تطبيقك إلى:

- تقديم إجابات كاملة ودقيقة عن الأسئلة الخاصة بمنطقة جغرافية معيّنة
- إنشاء أدوات تخطيط رحلات ومراجع محلية مستندة إلى المحادثات
- اقتراح نقاط الاهتمام استنادًا إلى الموقع الجغرافي وإعدادات المستخدم المفضّلة، مثل المطاعم أو المتاجر
- إنشاء تجارب تستند إلى الموقع الجغرافي للخدمات الاجتماعية أو خدمات البيع بالتجزئة أو توصيل الطعام

يتفوّق استخدام "خرائط Google" كمصدر في حالات الاستخدام التي تكون فيها القرب والبيانات الواقعية الحالية مهمة، مثل العثور على "أفضل مقهى بالقرب مني" أو الحصول على اتجاهات.

## طُرق واجهة برمجة التطبيقات والمَعلمات

يتم عرض ميزة "استخدام "خرائط Google" كمصدر" من خلال Gemini API كأداة ضمن الطريقة [`generateContent`](https://ai.google.dev/api/generate-content?hl=ar). يمكنك تفعيل ميزة استخدام "خرائط Google" كمصدر وضبطها من خلال تضمين عنصر [`googleMaps`](https://ai.google.dev/api/caching?hl=ar#GoogleMaps) في المَعلمة `tools` ضمن طلبك.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

بالإضافة إلى ذلك، تتيح الأداة تمرير الموقع الجغرافي السياقي كـ `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### فهم الردّ المستند إلى معلومات خارجية

عندما يتم إنشاء استجابة ناجحة استنادًا إلى بيانات &quot;خرائط Google&quot;، تتضمّن الاستجابة الحقل [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ar#GroundingMetadata).
هذه البيانات المنظَّمة ضرورية للتحقّق من صحة الادعاءات وإنشاء تجربة اقتباس غنية في تطبيقك، بالإضافة إلى استيفاء متطلبات استخدام الخدمة.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

تعرض Gemini API المعلومات التالية مع
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ar#GroundingMetadata):

- `groundingChunks`: مصفوفة من العناصر التي تحتوي على مصادر `maps` (`uri` و`placeId` و`title`).
- `groundingSupports`: مصفوفة من الأجزاء لربط نص ردّ النموذج بالمستندات المصدر في `groundingChunks`. يربط كل جزء نطاقًا نصيًا (محدّدًا بواسطة `startIndex` و`endIndex`) بعنصر `groundingChunkIndices` واحد أو أكثر. هذا هو المفتاح لإنشاء اقتباسات مضمّنة.

للحصول على مقتطف رمز يوضّح كيفية عرض الاقتباسات المضمّنة في النص، يمكنك الاطّلاع على [المثال](https://ai.google.dev/gemini-api/docs/google-search?hl=ar#attributing_sources_with_inline_citations) في مستندات تحديد المصدر من خلال "بحث Search".

## حالات الاستخدام

يتيح استخدام "خرائط Google" كمصدر مجموعة متنوعة من حالات الاستخدام التي تعتمد على الموقع الجغرافي. توضّح الأمثلة التالية كيف يمكن أن تستفيد الطلبات والمَعلمات المختلفة من استخدام "خرائط Google" كمصدر. قد تختلف المعلومات الواردة في النتائج المستندة إلى بيانات واقعية في &quot;خرائط Google&quot; عن الظروف الفعلية.

### التعامل مع الأسئلة المتعلّقة بمكان معيّن

طرح أسئلة مفصّلة حول مكان معيّن للحصول على إجابات استنادًا إلى مراجعات مستخدمي Google وبيانات &quot;خرائط Google&quot; الأخرى

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### توفير ميزة التخصيص المستندة إلى الموقع الجغرافي

الحصول على اقتراحات مخصّصة حسب الإعدادات المفضّلة للمستخدِم ومنطقة جغرافية معيّنة

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### المساعدة في التخطيط لبرنامج الرحلة

إنشاء خطط لعدة أيام تتضمّن الاتجاهات ومعلومات حول مواقع جغرافية مختلفة، ما يجعلها مثالية لتطبيقات السفر

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## متطلبات استخدام الخدمة

يوضّح هذا القسم متطلبات استخدام خدمة &quot;التأسيس باستخدام خرائط Google&quot;.

### إبلاغ المستخدم بشأن استخدام مصادر "خرائط Google"

مع كل نتيجة مستندة إلى بيانات واقعية في &quot;خرائط Google&quot;، ستتلقّى مصادر في
`groundingChunks` تؤيّد كل ردّ. يتم أيضًا عرض البيانات الوصفية التالية:

- معرّف الموارد المنتظم (URI) للمصدر
- title
- رقم التعريف

عند عرض نتائج من استخدام "خرائط Google" كمصدر، يجب تحديد مصادر "خرائط Google" المرتبطة وإبلاغ المستخدمين بما يلي:

- يجب أن تتبع مصادر &quot;خرائط Google&quot; المحتوى الذي تم إنشاؤه مباشرةً والذي تستند إليه هذه المصادر. يُشار إلى هذا المحتوى الذي يتم إنشاؤه أيضًا باسم "نتيجة مستندة إلى بيانات واقعية" في "خرائط Google".
- يجب أن تكون مصادر "خرائط Google" قابلة للعرض من خلال تفاعل واحد من المستخدم.

### عرض مصادر "خرائط Google" باستخدام روابط "خرائط Google"

بالنسبة إلى كل مصدر في `groundingChunks` و`grounding_chunks.maps.placeAnswerSources.reviewSnippets`، يجب إنشاء معاينة للرابط وفقًا للمتطلبات التالية:

- يجب إسناد كل مصدر إلى &quot;خرائط Google&quot; باتّباع [إرشادات الإسناد](#maps-attribution-guidelines) الخاصة بنص &quot;خرائط Google&quot;.
- عرض عنوان المصدر المقدَّم في الرد
- انقر على `uri` أو `googleMapsUri` من الردّ للانتقال إلى المصدر.

تعرض هذه الصور الحدّ الأدنى من المتطلبات لعرض المصادر وروابط &quot;خرائط Google&quot;.

![طلب مع ردّ يعرض المصادر](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=ar)

يمكنك تصغير عرض المصادر.

![الطلب مع الرد والمصادر مصغّرة](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=ar)

اختياري: تحسين معاينة الرابط من خلال إضافة محتوى إضافي، مثل:

- يتم إدراج [رمز مفضّل لـ "خرائط Google"](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=ar)
  قبل نص بيان المصدر الخاص بـ "خرائط Google".
- تمثّل هذه السمة صورة من عنوان URL المصدر (`og:image`).

لمزيد من المعلومات حول بعض مزوّدي بيانات "خرائط Google" وبنود الترخيص الخاصة بهم، يُرجى الاطّلاع على [الإشعارات القانونية في "خرائط Google" وGoogle Earth](https://www.google.com/help/legalnotices_maps/?hl=ar).

### إرشادات تحديد المصدر باستخدام النصوص في "خرائط Google"

عند الإشارة إلى مصادر &quot;خرائط Google&quot; في النص، اتّبِع الإرشادات التالية:

- يجب عدم تعديل النص في "خرائط Google" بأي شكل من الأشكال:
  - لا تغيِّر الكتابة بالأحرف الكبيرة في "خرائط Google".
  - لا تلتفّ "خرائط Google" على أسطر متعددة.
  - لا تقم بتوطين "خرائط Google" إلى لغة أخرى.
  - منع المتصفّحات من ترجمة &quot;خرائط Google&quot; باستخدام السمة translate=&quot;no&quot; في HTML
- يمكنك تنسيق نص "خرائط Google" كما هو موضّح في الجدول التالي:

| الموقع | النمط |
| --- | --- |
| `Font family` | Roboto تحميل الخط اختياري. |
| `Fallback font family` | أي خط sans serif مستخدَم حاليًا في منتجك أو "Sans-Serif" لاستخدام خط النظام التلقائي |
| `Font style` | عادي |
| `Font weight` | 400 |
| `Font color` | أبيض أو أسود (#1F1F1F) أو رمادي (#5E5E5E) الحفاظ على تباين يسهل الوصول إليه (4.5:1) مع الخلفية |
| `Font size` | - الحد الأدنى لحجم الخط: 12sp - الحدّ الأقصى لحجم الخط: 16 وحدة مستقلة عن الكثافة - لمعرفة المزيد عن وحدات البكسل غير المرتبطة بالمقياس، يمكنك الاطّلاع على وحدات حجم الخط على [موقع "التصميم المتعدد الأبعاد" الإلكتروني](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | عادي |

#### مثال على CSS

تعرض ورقة الأنماط المتتالية (CSS) التالية &quot;خرائط Google&quot; بنمط الطباعة واللون المناسبَين على خلفية بيضاء أو فاتحة.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### رقم تعريف المكان ورقم تعريف المراجعة

تتضمّن بيانات "خرائط Google" رقم تعريف المكان ورقم تعريف المراجعة. يمكنك تخزين بيانات الردود التالية مؤقتًا وتخزينها وتصديرها:

- `placeId`
- `reviewId`

لا تنطبق القيود المفروضة على التخزين المؤقت في "بنود استخدام ميزة استخدام "خرائط Google" كمصدر".

### النشاط والأراضي المحظورة

يتضمن استخدام "خرائط Google" كمصدر قيودًا إضافية على بعض المحتوى والأنشطة للحفاظ على منصة آمنة وموثوقة. بالإضافة إلى قيود الاستخدام الواردة في [البنود](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-maps):

- لن تستخدم استخدام "خرائط Google" كمصدر في الأنشطة عالية الخطورة، بما في ذلك خدمات الاستجابة لحالات الطوارئ.
- لن توزع أو تسوّق تطبيقك الذي يوفّر ميزة Grounding with Google Maps في منطقة محظورة. لمزيد من المعلومات، يُرجى الاطّلاع على [المناطق المحظورة في "منصة خرائط Google"](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=ar).
  قد يتم تعديل قائمة "المناطق المحظورة" من حين لآخر.

## أفضل الممارسات

- **توفير الموقع الجغرافي للمستخدم:** للحصول على الردود الأكثر صلة وتخصيصًا، احرص دائمًا على تضمين `user_location` (خطوط الطول والعرض) في إعدادات `googleMapsGrounding` عندما يكون الموقع الجغرافي للمستخدم معروفًا.
- **إعلام المستخدمين النهائيين:** يجب إعلام المستخدمين النهائيين بوضوح بأنّه يتم استخدام بيانات &quot;خرائط Google&quot; للرد على طلباتهم، خاصةً عند تفعيل الأداة.
- **مراقبة وقت الاستجابة:** بالنسبة إلى التطبيقات الحوارية، تأكَّد من أنّ وقت الاستجابة P95 للردود المستندة إلى بيانات خارجية يظل ضمن الحدود المقبولة للحفاظ على تجربة مستخدم سلسة.
- **إيقاف الميزة عند عدم الحاجة إليها:** يكون استخدام "خرائط Google" كمصدر غير مفعّل تلقائيًا. لا تفعِّلها (`"tools": [{"googleMaps": {}}]`) إلا عندما يكون لطلب البحث سياق جغرافي واضح، وذلك لتحسين الأداء والتكلفة.

## القيود

- **النطاق الجغرافي:** تتوفّر ميزة "الاستناد إلى خرائط Google" على مستوى العالم.
- **الأجهزة المتوافقة:** يمكنك الاطّلاع على قسم [الطُرز المتوافقة](#supported-models).
- **المدخلات والمخرجات بتنسيقات متعدّدة:** لا تتيح ميزة "استخدام "خرائط Google" كمصدر" حاليًا استخدام المدخلات أو المخرجات بتنسيقات متعدّدة غير النص.
- **الحالة التلقائية:** تكون أداة "استخدام خرائط Google كمصدر" غير مفعّلة تلقائيًا.
  يجب تفعيلها صراحةً في طلبات واجهة برمجة التطبيقات.

## الأسعار وحدود الاستخدام

يستند تسعير ميزة "استخدام خرائط Google كمصدر" إلى عدد طلبات البحث. يبلغ السعر الحالي
**25 دولارًا أمريكيًا لكل 1,000 طلب مستند إلى بيانات واقعية**. تتضمّن الطبقة المجانية أيضًا ما يصل إلى 500 طلب في اليوم. لا يتم احتساب الطلب ضمن الحصة إلا عندما يعرض الردّ بنجاح نتيجة واحدة على الأقل من نتائج &quot;خرائط Google&quot; المستندة إلى بيانات واقعية (أي النتائج التي تتضمّن مصدرًا واحدًا على الأقل من &quot;خرائط Google&quot;). إذا تم إرسال طلبات بحث متعددة إلى &quot;خرائط Google&quot; من طلب واحد، سيتم احتسابها كطلب واحد ضمن الحد الأقصى لعدد الطلبات.

للحصول على معلومات مفصّلة عن الأسعار، يُرجى الاطّلاع على [صفحة أسعار Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

تتيح النماذج التالية استخدام "خرائط Google" كمصدر:

| الطراز | استخدام "خرائط Google" كمصدر |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## مجموعات الأدوات المتوافقة

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل Grounding with Google Maps) والأدوات المخصّصة (استدعاء الدوال). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## الخطوات التالية

- جرِّب [كتاب الطبخ الخاص بميزة تحديد المصدر من خلال "بحث Search" في Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ar).
- [مزيد من المعلومات عن الأدوات الأخرى المتاحة](https://ai.google.dev/gemini-api/docs/tools?hl=ar)
- لمزيد من المعلومات حول أفضل ممارسات الذكاء الاصطناعي المسؤول وفلاتر الأمان في Gemini API، يُرجى الاطّلاع على [دليل إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
