---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar
fetched_at: 2026-05-05T19:44:12.844805+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u0627\u062f \u0625\u0644\u0649 \"\u062e\u0631\u0627\u0626\u0637 Google\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستناد إلى "خرائط Google"

استخدام "خرائط Google" كمصدر يربط بين الإمكانات الإنشائية لـ Gemini والبيانات الغنية والحقيقية والحديثة في "خرائط Google". تتيح هذه الميزة للمطوّرين دمج وظائف تستند إلى الموقع الجغرافي بسهولة في تطبيقاتهم. عندما يتضمّن طلب المستخدم سياقًا مرتبطًا ببيانات "خرائط Google"، يستفيد نموذج Gemini من "خرائط Google" لتقديم إجابات دقيقة ومحدّثة ذات صلة بالموقع الجغرافي أو المنطقة العامة التي حدّدها المستخدم.

- **إجابات دقيقة ومستندة إلى الموقع الجغرافي:** يمكنك الاستفادة من بيانات "خرائط Google" الشاملة والحديثة للردّ على طلبات البحث الجغرافية.
- **تخصيص محسّن:** يمكنك تخصيص الاقتراحات والمعلومات استنادًا إلى المواقع الجغرافية التي يقدّمها المستخدم.
- **معلومات وأدوات سياقية:** يمكنك استخدام رموز السياق لعرض أدوات تفاعلية من "خرائط Google" بجانب المحتوى الذي تم إنشاؤه.

## البدء

يوضّح هذا المثال كيفية دمج ميزة "استخدام "خرائط Google" كمصدر" في تطبيقك لتقديم إجابات دقيقة ومستندة إلى الموقع الجغرافي لطلبات المستخدمين. يطلب منك هذا النموذج اقتراحات محلية مع موقع جغرافي اختياري للمستخدم، ما يتيح لنموذج Gemini استخدام بيانات "خرائط Google".

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
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
    model: "gemini-3-flash-preview",
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
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

## آلية عمل ميزة "تحديد المصدر باستخدام خرائط Google"

تدمج ميزة استخدام "خرائط Google" كمصدر واجهة Gemini API مع منظومة Google Geo المتكاملة من خلال استخدام Maps API كمصدر لتحديد المصدر. عندما يتضمّن طلب المستخدم سياقًا جغرافيًا، يمكن لنموذج Gemini استدعاء أداة "تحديد المصدر باستخدام خرائط Google". بعد ذلك، يمكن للنموذج إنشاء ردود تستند إلى بيانات "خرائط Google" ذات الصلة بالموقع الجغرافي المقدَّم.

تتضمّن العملية عادةً ما يلي:

1. **طلب المستخدم:** يرسل المستخدم طلبًا إلى تطبيقك، وقد يتضمّن سياقًا جغرافيًا (مثل "مقاهي بالقرب مني" أو "متاحف في سان فرانسيسكو").
2. **استدعاء الأداة:** يستدعي نموذج Gemini أداة "استخدام "خرائط Google" كمصدر" بعد التعرّف على الغرض الجغرافي من الطلب. يمكن تزويد هذه الأداة اختياريًا بـ
   و`latitude` و`longitude`. الأداة هي أداة بحث نصي وتعمل بطريقة مشابهة للبحث على "خرائط Google"، حيث تستخدم الطلبات المحلية ("بالقرب مني") الإحداثيات، بينما من غير المرجّح أن تتأثر الطلبات المحدّدة أو غير المحلية بالموقع الجغرافي الصريح.
3. **استرجاع البيانات:** تطلب خدمة "استخدام "خرائط Google" كمصدر" معلومات ذات صلة من "خرائط Google" (مثل الأماكن والمراجعات والصور والعناوين وساعات العمل).
4. **الإنشاء المستند إلى المصدر:** يتم استخدام بيانات "خرائط Google" التي تم استرجاعها لتقديم ردّ نموذج Gemini، ما يضمن الدقة والصلة بالوقائع.
5. **الردّ والرمز المميّز للأداة:** يعرض النموذج ردًا نصيًا يتضمّن مراجع لمصادر "خرائط Google". اختياريًا، قد تحتوي استجابة واجهة برمجة التطبيقات أيضًا على `google_maps_widget_context_token`، ما يتيح للمطوّرين عرض أداة سياقية من "خرائط Google" في تطبيقهم للتفاعل المرئي.

## أسباب استخدام ميزة "استخدام خرائط Google كمصدر" والحالات التي يجب استخدامها فيها

يُعدّ استخدام "خرائط Google" كمصدر مثاليًا للتطبيقات التي تتطلّب معلومات دقيقة ومحدّثة ومستندة إلى الموقع الجغرافي. تعزّز هذه الميزة تجربة المستخدم من خلال تقديم محتوى ذي صلة ومخصّص يستند إلى قاعدة بيانات "خرائط Google" الشاملة التي تضم أكثر من 250 مليون مكان في جميع أنحاء العالم.

عليك استخدام ميزة "استخدام "خرائط Google" كمصدر" عندما يحتاج تطبيقك إلى ما يلي:

- تقديم ردود كاملة ودقيقة على الأسئلة الجغرافية المحدّدة
- إنشاء أدلة محلية ومخططات رحلات محادثة
- اقتراح نقاط اهتمام استنادًا إلى الموقع الجغرافي وتفضيلات المستخدم، مثل المطاعم أو المتاجر.
- إنشاء تجارب مستندة إلى الموقع الجغرافي لخدمات التوصيل الغذائي أو خدمات البيع بالتجزئة أو الخدمات الاجتماعية

يتميّز استخدام "خرائط Google" كمصدر في حالات الاستخدام التي تكون فيها القرب والبيانات الواقعية الحالية مهمة، مثل العثور على "أفضل مقهى بالقرب مني" أو الحصول على الاتجاهات.

## طرق واجهة برمجة التطبيقات والمعلَمات

تظهر ميزة "استخدام "خرائط Google" كمصدر" من خلال Gemini API كأداة ضمن الـ [`generateContent`](https://ai.google.dev/api/generate-content?hl=ar) طريقة. يمكنك تفعيل ميزة "استخدام "خرائط Google" كمصدر" وضبطها من خلال تضمين عنصر [`googleMaps`](https://ai.google.dev/api/caching?hl=ar#GoogleMaps) في مَعلمة `tools` الخاصة بطلبك.

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

يمكن أن تقبل الأداة [`googleMaps`](https://ai.google.dev/api/caching?hl=ar#GoogleMaps) أيضًا مَعلمة
منطقية `enableWidget`، تُستخدم للتحكّم في ما إذا كان سيتم عرض الحقل
[`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=ar#GroundingMetadata)
في الردّ. يمكن استخدام هذه المَعلمة لعرض أداة سياقية من "أماكن Google"
.

### JSON

```
{
"contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": { "enableWidget": true } }
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

### فهم استجابة تحديد المصدر

عندما يتم تحديد مصدر الردّ بنجاح باستخدام بيانات "خرائط Google"، يتضمّن الردّ
الحقل [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ar#GroundingMetadata).
هذه البيانات المنظَّمة ضرورية للتحقّق من الادعاءات وإنشاء تجربة إسناد غنية في تطبيقك، بالإضافة إلى استيفاء متطلبات استخدام الخدمة.

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
        ],
        "googleMapsWidgetContextToken": "widgetcontent/..."
      }
    }
  ]
}
```

تعرض Gemini API المعلومات التالية مع الـ
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ar#GroundingMetadata):

- `groundingChunks`: مصفوفة من الكائنات التي تحتوي على مصادر `maps` (`uri` و`placeId` و`title`)
- `groundingSupports`: مصفوفة من الأجزاء لربط نص ردّ النموذج بالمصادر في `groundingChunks` يربط كل جزء نطاقًا نصيًا (محدّدًا بواسطة `startIndex` و`endIndex`) بواحد أو أكثر من `groundingChunkIndices`. هذا هو المفتاح لإنشاء مراجع مضمّنة.
- `googleMapsWidgetContextToken`: رمز مميّز نصي يمكن استخدامه لعرض أداة [سياقية من "أماكن Google"](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=ar).

للحصول على مقتطف الرمز الذي يوضّح كيفية عرض مراجع مضمّنة في النص، يمكنك الاطّلاع على [المثال](https://ai.google.dev/gemini-api/docs/google-search?hl=ar#attributing_sources_with_inline_citations)
في مستندات ميزة "تحديد المصدر من خلال بحث Google".

### عرض الأداة السياقية من "خرائط Google"

لاستخدام `googleMapsWidgetContextToken` الذي تم عرضه، عليك [تحميل
Google Maps JavaScript
API](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=ar).

## حالات الاستخدام

تتيح ميزة استخدام "خرائط Google" كمصدر مجموعة متنوعة من حالات الاستخدام المستندة إلى الموقع الجغرافي. توضّح الأمثلة التالية كيف يمكن أن تستفيد الطلبات والمعلَمات المختلفة من استخدام "خرائط Google" كمصدر. قد تختلف المعلومات في "النتائج المستندة إلى المصدر من خرائط Google" عن الظروف الفعلية.

### التعامل مع الأسئلة الخاصة بمكان معيّن

يمكنك طرح أسئلة مفصّلة حول مكان معيّن للحصول على إجابات استنادًا إلى مراجعات مستخدمي Google وبيانات "خرائط Google" الأخرى.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
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

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
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

يمكنك الحصول على اقتراحات مخصّصة لتفضيلات المستخدم ومنطقة جغرافية معيّنة.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
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

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
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

### المساعدة في تخطيط برنامج الرحلة

يمكنك إنشاء خطط لعدة أيام تتضمّن الاتجاهات والمعلومات حول مواقع جغرافية مختلفة، ما يجعلها مثالية لتطبيقات السفر.

في هذا المثال، تم طلب `googleMapsWidgetContextToken` من خلال تفعيل الأداة في أداة "خرائط Google". عند تفعيلها، يمكن استخدام الرمز المميّز الذي تم عرضه
لعرض أداة سياقية من "أماكن Google" باستخدام
`<gmp-places-contextual> component`
من Google Maps JavaScript API.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
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

  if widget_token := grounding.google_maps_widget_context_token:
    print('-' * 40)
    print(f'<gmp-place-contextual context-token="{widget_token}"></gmp-place-contextual>')
```

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: prompt,
    config: {
      tools: [{googleMaps: {enableWidget: true}}],
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

    if (groundingMetadata.googleMapsWidgetContextToken) {
      console.log('-'.repeat(40));
      document.body.insertAdjacentHTML('beforeend', `<gmp-place-contextual context-token="${groundingMetadata.googleMapsWidgetContextToken}`"></gmp-place-contextual>`);
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {"enableWidget":"true"}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

عند عرض الأداة، ستبدو على النحو التالي:

![مثال على تطبيق مصغّر لـ &quot;خرائط Google&quot; عند عرضه](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=ar)

## متطلبات استخدام الخدمة

يصف هذا القسم متطلبات استخدام خدمة "تحديد المصدر باستخدام خرائط Google".

### إعلام المستخدم بشأن استخدام مصادر "خرائط Google"

مع كل نتيجة مستندة إلى المصدر من "خرائط Google"، ستتلقّى مصادر في `groundingChunks` تدعم كل ردّ. يتم أيضًا عرض البيانات الوصفية التالية:

- معرف الموارد المنتظم (URI) للمصدر
- title
- رقم التعريف

عند عرض نتائج من ميزة "استخدام "خرائط Google" كمصدر"، عليك تحديد مصادر "خرائط Google" المرتبطة بها وإعلام المستخدمين بما يلي:

- يجب أن تتبع مصادر "خرائط Google" مباشرةً المحتوى الذي تم إنشاؤه والذي تدعمه المصادر. يُشار أيضًا إلى هذا المحتوى الذي تم إنشاؤه باسم "النتائج المستندة إلى المصدر من خرائط Google".
- يجب أن تكون مصادر "خرائط Google" قابلة للعرض خلال تفاعل واحد للمستخدم.

### عرض مصادر "خرائط Google" مع روابط "خرائط Google"

لكل مصدر في `groundingChunks` وفي `grounding_chunks.maps.placeAnswerSources.reviewSnippets`، يجب إنشاء معاينة للرابط استنادًا إلى المتطلبات التالية:

- يجب تحديد مصدر كل مراجعة على أنّه "خرائط Google" وفقًا لإرشادات تحديد المصدر النصي في "خرائط Google"
  .
- يجب عرض عنوان المصدر المقدَّم في الردّ.
- يجب الربط بالمصدر باستخدام `uri` أو `googleMapsUri` من الردّ.

تعرض هذه الصور الحد الأدنى من المتطلبات لعرض المصادر وروابط "خرائط Google".

![طلب مع ردّ يعرض المصادر](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=ar)

يمكنك تصغير طريقة عرض المصادر.

![الطلب مع الرد والمصادر مصغّرة](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=ar)

اختياري: يمكنك تحسين معاينة الرابط بمحتوى إضافي، مثل:

- إدراج [رمز مفضل من "خرائط Google"](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=ar) قبل تحديد المصدر النصي في "خرائط Google".
- صورة من عنوان URL للمصدر (`og:image`)

لمزيد من المعلومات حول بعض مزوّدي بيانات "خرائط Google" وشروط الترخيص الخاصة بهم، يمكنك الاطّلاع على [الإشعارات القانونية في "خرائط Google" وGoogle Earth](https://www.google.com/help/legalnotices_maps/?hl=ar).

### إرشادات تحديد المصدر النصي في "خرائط Google"

عند تحديد مصادر "خرائط Google" في النص، اتّبِع الإرشادات التالية:

- لا تعدِّل النص "خرائط Google" بأي شكل من الأشكال:
  - لا تغيِّر حالة الأحرف في "خرائط Google".
  - لا تنقل "خرائط Google" إلى أسطر متعددة.
  - لا تترجِم "خرائط Google" إلى لغة أخرى.
  - امنع المتصفّحات من ترجمة "خرائط Google" باستخدام سمة HTML‏ `translate="no"`.
- نسِّق نص "خرائط Google" كما هو موضّح في الجدول التالي:

| الموقع | النمط |
| --- | --- |
| `Font family` | Roboto تحميل الخط اختياري. |
| `Fallback font family` | أي خط نص أساسي من نوع sans serif مستخدَم حاليًا في منتجك أو "Sans-Serif" لاستدعاء خط النظام التلقائي |
| `Font style` | عادي |
| `Font weight` | 400 |
| `Font color` | أبيض أو أسود (#1F1F1F) أو رمادي (#5E5E5E) يجب الحفاظ على تباين يسهل الوصول إليه (4.5:1) مع الخلفية. |
| `Font size` | - الحد الأدنى لحجم الخط: 12sp - الحد الأقصى لحجم الخط: 16sp - للتعرّف على وحدات sp، يمكنك الاطّلاع على وحدات حجم الخط على موقع [التصميم المتعدد الأبعاد](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | عادي |

#### مثال على نمط CSS

يعرض نمط CSS التالي "خرائط Google" بالنمط اللغوي واللون المناسبَين على خلفية بيضاء أو فاتحة.

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

### رمز السياق ورقم تعريف المكان ورقم تعريف المراجعة

تتضمّن بيانات "خرائط Google" رمز السياق ورقم تعريف المكان ورقم تعريف المراجعة. يمكنك تخزين بيانات الردّ التالية مؤقتًا وحفظها وتصديرها:

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

لا تنطبق القيود المفروضة على التخزين المؤقت في بنود استخدام "خرائط Google" كمصدر.

### النشاط والمنطقة المحظوران

يتضمن استخدام "خرائط Google" كمصدر قيودًا إضافية على محتوى وأنشطة معيّنة للحفاظ على منصة آمنة وموثوق بها. بالإضافة إلى قيود الاستخدام الواردة في [البنود](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-maps):

- لن تستخدم ميزة "استخدام خرائط Google كمصدر" للأنشطة عالية المخاطر، بما في ذلك خدمات الاستجابة للطوارئ.
- لن توزع أو تسوّق تطبيقك الذي يقدّم ميزة "تحديد المصدر باستخدام خرائط Google" في منطقة محظورة. المناطق المحظورة حاليًا هي:

  - الصين
  - شبه جزيرة القرم
  - كوبا
  - جمهورية دونيتسك الشعبية
  - إيران
  - جمهورية لوهانسك الشعبية
  - كوريا الشمالية
  - سوريا
  - فيتنام

  قد يتم تعديل هذه القائمة من حين لآخر.

## أفضل الممارسات

- **توفير موقع المستخدم:** للحصول على الردود الأكثر صلة وتخصيصًا، عليك دائمًا تضمين `user_location` (خط العرض وخط الطول) في إعدادات `googleMapsGrounding` عندما يكون موقع المستخدم معروفًا.
- **عرض الأداة السياقية من "خرائط Google":** يتم عرض الأداة السياقية باستخدام رمز السياق `googleMapsWidgetContextToken` الذي يتم عرضه في استجابة Gemini API ويمكن استخدامه لعرض محتوى مرئي من "خرائط Google". لمزيد من المعلومات حول الأداة السياقية، يمكنك الاطّلاع على
  [استخدام "خرائط Google" كمصدر](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=ar)
  في دليل المطوّر من Google.
- **إعلام المستخدمين النهائيين:** عليك إعلام المستخدمين النهائيين بوضوح بأنّه يتم استخدام بيانات "خرائط Google" للإجابة عن طلباتهم، خاصةً عند تفعيل الأداة.
- **مراقبة وقت الاستجابة:** بالنسبة إلى التطبيقات المحادثة، تأكّد من أنّ وقت الاستجابة في المئوي الخامس والتسعين للردود المستندة إلى المصدر يظل ضمن الحدود المقبولة للحفاظ على تجربة مستخدم سلسة.
- **إيقاف الميزة عند عدم الحاجة إليها:** يكون استخدام "خرائط Google" كمصدر غير مفعّل تلقائيًا. عليك تفعيلها فقط (`"tools": [{"googleMaps": {}}]`) عندما يتضمّن الطلب سياقًا جغرافيًا واضحًا لتحسين الأداء والتكلفة.

## القيود

- **النطاق الجغرافي:** تتوفّر ميزة استخدام "خرائط Google" كمصدر على مستوى العالم
- **النماذج المتوافقة:** يمكنك الاطّلاع على قسم [النماذج المتوافقة](#supported-models).
- **المدخلات والمخرجات بتنسيقات متعدّدة:** لا تتيح ميزة "استخدام "خرائط Google" كمصدر" حاليًا المدخلات أو المخرجات بتنسيقات متعدّدة بخلاف النص وأدوات الخرائط السياقية.
- **الحالة التلقائية:** تكون أداة "استخدام "خرائط Google" كمصدر" غير مفعّلة تلقائيًا.
  عليك تفعيلها صراحةً في طلبات واجهة برمجة التطبيقات.

## التسعير وحدود المعدّل

يستند تسعير ميزة "استخدام خرائط Google كمصدر" إلى الطلبات. المعدّل الحالي هو **25 دولارًا أمريكيًا لكل 1000 طلب مستند إلى المصدر**. تتضمّن الطبقة المجانية أيضًا ما يصل إلى 500 طلب في اليوم. لا يتم احتساب الطلب ضمن الحصة إلا عندما يعرض الطلب بنجاح نتيجة واحدة على الأقل مستندة إلى المصدر من "خرائط Google" (أي نتائج تحتوي على مصدر واحد على الأقل من "خرائط Google"). إذا تم إرسال طلبات متعددة إلى "خرائط Google" من طلب واحد، يتم احتسابها كطلب واحد ضمن حد المعدّل.

للحصول على معلومات مفصّلة عن الأسعار، يمكنك الاطّلاع على [صفحة تسعير Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

تتيح النماذج التالية ميزة "استخدام خرائط Google كمصدر":

| الطراز | استخدام "خرائط Google" كمصدر |
| --- | --- |
| [Gemini 3.1 Pro (إصدار تجريبي)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [Gemini 3.1 Flash-Lite (إصدار تجريبي)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ar) | ✔️ |
| [Gemini 3 Flash (إصدار تجريبي)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=ar) | ✔️ |

## مجموعات الأدوات المتوافقة

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "تحديد المصدر باستخدام خرائط Google") والأدوات المخصّصة (استدعاء الدوال). يمكنك الاطّلاع على مزيد من المعلومات في صفحة
[مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## الخطوات التالية

- يمكنك تجربة ميزة [تحديد المصدر من خلال "بحث Search" في Gemini API
  Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ar).
- يمكنك التعرّف على الأدوات الأخرى [المتاحة](https://ai.google.dev/gemini-api/docs/tools?hl=ar).
- لمزيد من المعلومات حول أفضل ممارسات الذكاء الاصطناعي المسؤول وفلاتر الأمان في Gemini API
  ، يمكنك الاطّلاع على [دليل إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
