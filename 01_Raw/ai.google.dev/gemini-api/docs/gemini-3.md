---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=ar
fetched_at: 2026-05-25T05:28:06.901849+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# دليل المطوّرين في Gemini 3

‫Gemini 3 هي عائلة النماذج الأكثر ذكاءً لدينا حتى الآن، وهي تستند إلى أساس متين من إمكانات الاستدلال المتطورة. تم تصميم هذا النموذج لتحويل أي فكرة إلى واقع من خلال إتقان مهام سير العمل المستندة إلى الوكلاء والترميز المستقل والمهام المعقّدة المتعددة الوسائط.
يتناول هذا الدليل الميزات الرئيسية في مجموعة نماذج Gemini 3 وكيفية الاستفادة منها إلى أقصى حد.

[تجربة الإصدار التجريبي من Gemini 3.1 Pro](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=ar)
[تجربة الإصدار التجريبي من Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=ar)
[تجربة Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=ar)
[تجربة Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=ar)

يمكنك استكشاف [مجموعة تطبيقات Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ar) لمعرفة كيف يتعامل النموذج مع الاستدلال المتقدّم والترميز الذاتي والمهام المعقّدة المتعددة الوسائط.

ابدأ ببضعة أسطر من الرموز البرمجية:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## التعرّف على سلسلة Gemini 3

‫Gemini 3.1 Pro هو الخيار الأفضل للمهام المعقّدة التي تتطلب معرفة واسعة بالعالم واستدلالاً متقدّمًا في مختلف الوسائط.

‫Gemini 3 Flash هو أحدث نموذج من السلسلة 3، ويتميّز بذكاء على مستوى Pro وبسرعة Flash وأسعاره.

‫Nano Banana Pro (المعروف أيضًا باسم Gemini 3 Pro Image) هو نموذجنا الأعلى جودة لإنشاء الصور، وNano Banana 2 (المعروف أيضًا باسم Gemini 3.1 Flash Image) هو النموذج المكافئ الذي يتيح إنشاء عدد كبير من الصور بكفاءة عالية وبتكلفة أقل.

‫Gemini 3.1 Flash-Lite هو نموذجنا الأكثر كفاءةً والمصمَّم ليكون فعالاً من حيث التكلفة ولإنجاز المهام الكبيرة.

| رقم تعريف الطراز | قدرة الاستيعاب (داخل / خارج) | تاريخ آخر تحديث للبيانات | التسعير (الإدخال / الإخراج)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | يناير 2025 | ‫0.25 دولار أمريكي (نص وصورة وفيديو)، 0.50 دولار أمريكي (ملف صوتي) / 1.50 دولار أمريكي |
| **gemini-3.1-flash-lite-preview** | 1M / 64k | يناير 2025 | ‫0.25 دولار أمريكي (نص وصورة وفيديو)، 0.50 دولار أمريكي (ملف صوتي) / 1.50 دولار أمريكي |
| **gemini-3.1-flash-image-preview** | ‫128 ألف / 32 ألف | يناير 2025 | ‫0.25 دولار أمريكي (إدخال نصي) / 0.067 دولار أمريكي (إخراج صورة)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | يناير 2025 | ‫2 دولار أمريكي / 12 دولار أمريكي (أقل من 200 ألف رمز مميّز)   4 دولار أمريكي / 18 دولار أمريكي (أكثر من 200 ألف رمز مميّز) |
| **gemini-3-flash-preview** | 1M / 64k | يناير 2025 | 0.50 دولار أمريكي / 3 دولار أمريكي |
| **gemini-3-pro-image-preview** | ‫65 ألف / 32 ألف | يناير 2025 | ‫$2 (إدخال النص) / $0.134 (إخراج الصورة)\*\* |

*\* الأسعار هي لكل مليون رمز مميز ما لم يُذكر خلاف ذلك.*
*\*\* يختلف سعر الصورة حسب درجة الدقة. يمكنك الاطّلاع على [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) للحصول على التفاصيل.*

للاطّلاع على الحدود القصوى والأسعار والتفاصيل الإضافية، يُرجى الانتقال إلى [صفحة النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar).

## ميزات جديدة في واجهة برمجة التطبيقات في Gemini 3

يقدّم Gemini 3 مَعلمات جديدة مصمّمة لمنح المطوّرين مزيدًا من التحكّم في وقت الاستجابة والتكلفة ودقة الوسائط المتعددة.

### مستوى التفكير

تستخدم نماذج سلسلة Gemini 3 ميزة "التفكير الديناميكي" تلقائيًا للاستنتاج من خلال الطلبات. يمكنك استخدام المَعلمة `thinking_level` التي تتحكّم في
**الحد الأقصى** لعمق عملية الاستدلال الداخلية للنموذج قبل أن ينتج
ردًا. يتعامل Gemini 3 مع هذه المستويات على أنّها حدود نسبية للتفكير
بدلاً من ضمانات صارمة للرموز المميزة.

إذا لم يتم تحديد `thinking_level`، سيتم تلقائيًا ضبط Gemini 3 على `high`. للحصول على ردود أسرع وبزمن استجابة أقل عندما لا يكون الاستنتاج المعقّد مطلوبًا، يمكنك حصر مستوى التفكير في النموذج على `low`.

| مستوى التفكير | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | الوصف |
| --- | --- | --- | --- | --- |
| **`minimal`** | غير متاح | متاح (الإعداد التلقائي) | متاح | يتطابق هذا الخيار مع الإعداد "بدون تفكير" لمعظم طلبات البحث. قد يفكّر النموذج بشكل محدود جدًا لإنجاز مهام الترميز المعقّدة. يقلّل من وقت الاستجابة للتطبيقات التي تتضمّن محادثات أو تتطلّب معدّل أعلى لنقل البيانات. يُرجى العِلم أنّ `minimal` لا يضمن إيقاف التفكير. |
| **`low`** | متاح | متاح | متاح | يقلّل من زمن الانتقال والتكلفة. الأفضل للتطبيقات التي تتطلّب اتّباع تعليمات بسيطة أو المحادثة أو معالجة البيانات بسرعة كبيرة. |
| **`medium`** | متاح | متاح | متاح | تفكير متوازن لمعظم المهام |
| **`high`** | متاح (تلقائي، ديناميكي) | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | زيادة عمق الاستدلال إلى أقصى حد قد يستغرق النموذج وقتًا أطول بكثير للوصول إلى الرمز المميز الأول (غير المفكّر)، ولكن سيكون الناتج أكثر دقة. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### درجة دقة الوسائط

يقدّم Gemini 3 إمكانية تحكّم دقيقة في معالجة الصور المتعددة الوسائط من خلال المَعلمة
`media_resolution`. تؤدي الدقة الأعلى إلى تحسين قدرة النموذج على قراءة النصوص الدقيقة أو تحديد التفاصيل الصغيرة، ولكنها تزيد من استخدام الرموز المميزة ووقت الاستجابة.
تحدّد المَعلمة `media_resolution` **الحدّ الأقصى لعدد الرموز المميّزة
المخصّصة لكل صورة إدخال أو إطار فيديو.**

يمكنك الآن ضبط دقة الوضوح على `media_resolution_low` أو `media_resolution_medium` أو `media_resolution_high` أو `media_resolution_ultra_high` لكل جزء من الوسائط بشكل فردي أو على مستوى العالم (من خلال `generation_config`، ولا تتوفّر الدقة الفائقة على مستوى العالم). في حال عدم تحديدها، يستخدم النموذج الإعدادات التلقائية المثالية استنادًا إلى نوع الوسائط.

**الإعدادات المقترَحة**

| نوع الوسائط | الإعداد المقترَح | الحد الأقصى لعدد الرموز المميزة | إرشادات الاستخدام |
| --- | --- | --- | --- |
| **الصور** | `media_resolution_high` | 1120 | يُنصح باستخدامها لمعظم مهام تحليل الصور لضمان الحصول على أعلى جودة. |
| **ملفات PDF** | `media_resolution_medium` | 560 | الأفضل لفهم المستندات، وعادةً ما تصل الجودة إلى الحد الأقصى عند `medium`. لا تؤدي الزيادة إلى `high` عادةً إلى تحسين نتائج التعرّف البصري على الأحرف للمستندات العادية. |
| **الفيديو** (عام) | ‫`media_resolution_low` (أو `media_resolution_medium`) | ‫70 (لكل إطار) | **ملاحظة:** بالنسبة إلى الفيديو، يتم التعامل مع إعدادات `low` و`medium` بشكل مماثل (70 رمزًا مميزًا) لتحسين استخدام السياق. وهذا يكفي لمعظم مهام التعرّف على الإجراءات ووصفها. |
| **الفيديو** (يحتوي على الكثير من النصوص) | `media_resolution_high` | ‫280 (لكل إطار) | يجب توفُّرها فقط عندما تتضمّن حالة الاستخدام قراءة نص كثيف (التعرّف البصري على الأحرف) أو تفاصيل صغيرة ضمن لقطات الفيديو. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### درجة الحرارة

بالنسبة إلى جميع طُرز Gemini 3، ننصح بشدة بإبقاء مَعلمة درجة العشوائية عند قيمتها التلقائية البالغة `1.0`.

في حين أنّ النماذج السابقة كانت تستفيد غالبًا من ضبط درجة العشوائية للتحكّم في مستوى الإبداع مقابل الحتمية، تم تحسين إمكانات الاستدلال في Gemini 3 للإعداد التلقائي. قد يؤدي تغيير درجة العشوائية (ضبطها على قيمة أقل من 1.0) إلى سلوك غير متوقّع، مثل التكرار أو انخفاض الأداء، خاصةً في المهام الرياضية أو الاستدلالية المعقدة.

### توقيعات الأفكار

يستخدم Gemini 3 [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar) للحفاظ على سياق الاستنتاج في جميع طلبات البيانات من واجهة برمجة التطبيقات. هذه التواقيع هي تمثيلات مشفّرة لعملية المعالجة الداخلية للأفكار التي يجريها النموذج. لضمان احتفاظ النموذج بقدراته على الاستدلال، يجب إعادة هذه التواقيع إلى النموذج في طلبك تمامًا كما تم تلقّيها:

- **استدعاء الدوال (وضع صارم):** تفرض واجهة برمجة التطبيقات التحقّق الصارم من صحة "الجولة الحالية". سيؤدي عدم توفّر التواقيع إلى ظهور الخطأ 400.
- **النص/الدردشة:** لا يتم فرض التحقّق من صحة التوقيعات بشكل صارم، ولكن سيؤدي حذفها إلى خفض جودة الإجابات والاستدلال الذي يستند إليه النموذج.
- **إنشاء الصور/تعديلها (صارم)**: تفرض واجهة برمجة التطبيقات عملية تحقّق صارمة على جميع أجزاء النموذج، بما في ذلك `thoughtSignature`. سيؤدي عدم توفّر التواقيع إلى ظهور الخطأ 400.

#### استدعاء الدالة (التحقّق الدقيق)

عندما ينشئ Gemini `functionCall`، يعتمد على `thoughtSignature` لمعالجة نتيجة الأداة بشكل صحيح في الجولة التالية. يتضمّن "الدور الحالي"
جميع خطوات "النموذج" (`functionCall`) و"المستخدم" (`functionResponse`) التي
حدثت منذ آخر رسالة **مستخدم** `text` عادية.

- **استدعاء دالة واحدة:** يحتوي الجزء `functionCall` على توقيع. يجب إرجاعها.
- **استدعاء الدوال المتوازية:** سيحتوي الجزء الأول فقط من `functionCall` في القائمة على التوقيع. يجب إرجاع الأجزاء بالترتيب نفسه الذي تم استلامها به.
- **متعددة الخطوات (متسلسلة):** إذا استدعى النموذج أداة، وتلقّى نتيجة، ثم استدعى أداة *أخرى* (في إطار التفاعل نفسه)، سيتضمّن **كلا** استدعاءَي الدالة توقيعات. يجب عرض **جميع** التواقيع المتراكمة في السجلّ.

#### النص والبث

بالنسبة إلى المحادثات العادية أو إنشاء النصوص، لا يمكن ضمان توفّر توقيع.

- **غير متوفرة**: قد يتضمّن الجزء الأخير من الرد
  `thoughtSignature`، ولكن ليس دائمًا. وفي حال تم إرجاع إحدى هذه القيم، عليك إعادة إرسالها للحفاظ على أفضل أداء.
- **البث**: إذا تم إنشاء توقيع، قد يصل في جزء نهائي
  يحتوي على جزء نصي فارغ. تأكَّد من أنّ محلّل البث يتحقّق من التواقيع حتى إذا كان حقل النص فارغًا.

#### إنشاء الصور وتعديلها

بالنسبة إلى `gemini-3-pro-image-preview` و`gemini-3.1-flash-image-preview`، تُعد توقيعات الأفكار مهمة جدًا لإجراء تعديلات حوارية. عندما تطلب من النموذج تعديل صورة، يعتمد على `thoughtSignature` من المحادثة السابقة لفهم تركيبة الصورة الأصلية ومنطقها.

- **التعديل:** يتم تضمين التوقيعات في الجزء الأول بعد أفكار الرد (`text` أو `inlineData`) وفي كل جزء لاحق من `inlineData`. عليك إرجاع جميع هذه التواقيع لتجنُّب حدوث أخطاء.

#### أمثلة على الرموز

#### استدعاء الدوال المتعددة الخطوات (التسلسلي)

يطرح المستخدم سؤالاً يتطلّب خطوتَين منفصلتَين (التحقّق من الرحلة الجوية -> حجز سيارة أجرة) في ردّ واحد.   
  
**الخطوة 1: يطلب النموذج "أداة الرحلات الجوية".**  
يعرض النموذج توقيعًا `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**الخطوة 2: يرسل المستخدم "نتيجة الرحلة"**  
يجب أن نردّ بـ `<Sig_A>` للحفاظ على تسلسل أفكار النموذج.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  { 
    "role": "model", 
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} }, 
        "thoughtSignature": "<Sig_A>" // REQUIRED
      } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**الخطوة 3: النموذج يستدعي أداة سيارة الأجرة**  
يتذكّر النموذج تأخير الرحلة الجوية من خلال `<Sig_A>` ويقرّر الآن حجز سيارة أجرة. يؤدي ذلك إلى إنشاء توقيع *جديد* `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**الخطوة 4: يرسل المستخدم نتيجة سيارة الأجرة**  
لإكمال المحادثة، عليك إعادة إرسال السلسلة بأكملها: `<Sig_A>` و`<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### استدعاء الدوال بشكل متوازٍ

يطرح المستخدم السؤال التالي: "ما هي حالة الطقس في باريس ولندن؟". يعرض النموذج استدعاءَين للدالة في ردّ واحد.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### الاستدلال النصي/داخل السياق (بدون التحقّق من الصحة)

يطرح المستخدم سؤالاً يتطلّب التفكير في السياق بدون أدوات خارجية. على الرغم من أنّ التوقيع لا يتم التحقّق منه بدقة، إلا أنّ تضمينه يساعد النموذج في الحفاظ على سلسلة الاستدلال للأسئلة اللاحقة.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### إنشاء الصور وتعديلها

بالنسبة إلى إنشاء الصور، يتم التحقّق من صحة التواقيع بدقة. تظهر هذه الإعلانات على **الجزء الأول** (نص أو صورة) و**جميع أجزاء الصور اللاحقة**. يجب إعادة كل البطاقات في الدور التالي.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### نقل البيانات من طُرز أخرى

إذا كنت تنقل أثر محادثة من نموذج آخر (مثل Gemini 2.5) أو تُدرج استدعاء دالة مخصّصة لم يتم إنشاؤها بواسطة Gemini 3، لن يكون لديك توقيع صالح.

لتجاوز عملية التحقّق الصارمة في هذه السيناريوهات المحدّدة، املأ الحقل بالسلسلة الوهمية المحدّدة التالية: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### مُخرجات منظَّمة مع أدوات

تتيح لك نماذج Gemini 3 الجمع بين [النتائج المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) والأدوات المضمّنة، بما في ذلك
[تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) و[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) و[تنفيذ الرمز البرمجي](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### إنشاء الصور

تتيح لك أداتا Gemini 3.1 Flash Image وGemini 3 Pro Image إنشاء الصور وتعديلها
من خلال طلبات نصية. يستخدم هذا النموذج ميزة "الاستدلال" "للتفكير" في الطلب، ويمكنه استرداد بيانات في الوقت الفعلي، مثل توقعات الطقس أو الرسوم البيانية للأسهم، قبل استخدام ميزة [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) لتحديد المصدر قبل إنشاء صور عالية الدقة.

**الإمكانات الجديدة والمحسّنة:**

- **عرض النص بدقة 4K:** يمكنك إنشاء نص ورسوم بيانية واضحة وسهلة القراءة بدقة تصل إلى 2K و4K.
- **إنشاء المحتوى استنادًا إلى مصادر موثوقة:** استخدِم أداة `google_search` للتحقّق من الحقائق وإنشاء صور استنادًا إلى معلومات واقعية. تتوفّر ميزة "الاستناد إلى مصادر خارجية" باستخدام *بحث الصور* من Google في Gemini 3.1 Flash Image.
- **التعديل الحواري:** تعديل الصور في محادثة متعدّدة الجولات من خلال طلب إجراء تغييرات (مثلاً، "اجعل الخلفية غروب الشمس"). تعتمد سير العمل هذا على
  **التوقيعات الفكرية** للحفاظ على السياق المرئي بين الأدوار.

للحصول على تفاصيل كاملة حول نسب العرض إلى الارتفاع، وسير عمل التعديل، وخيارات الإعداد، يُرجى الاطّلاع على [دليل إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**مثال على الرد**

![الطقس في طوكيو](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ar)

### تنفيذ الرموز البرمجية باستخدام الصور

يمكن أن يتعامل Gemini 3 Flash مع الرؤية على أنّها تحقيق نشط، وليس مجرد نظرة سريعة ثابتة. من خلال الجمع بين الاستدلال و[تنفيذ الرمز البرمجي](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)، يضع النموذج خطة، ثم يكتب وينفّذ رمز Python البرمجي لتكبير الصور أو اقتصاصها أو إضافة تعليقات توضيحية إليها أو معالجتها بطريقة أخرى خطوة بخطوة لتحديد إجاباته بصريًا.

**حالات الاستخدام:**

- **التكبير والتدقيق:** يرصد النموذج ضمنيًا الحالات التي تكون فيها التفاصيل صغيرة جدًا (مثل قراءة مقياس أو رقم تسلسلي بعيد)، ويكتب رمزًا برمجيًا لاقتصاص المنطقة وإعادة فحصها بدقة أعلى.
- **الرياضيات المرئية والرسم البياني:** يمكن للنموذج إجراء عمليات حسابية متعددة الخطوات باستخدام الرموز البرمجية (مثل جمع بنود الإيصال أو إنشاء رسم بياني باستخدام Matplotlib من البيانات المستخرَجة).
- **التعليق التوضيحي على الصور:** يمكن للنموذج رسم أسهم أو مربّعات محيطة أو تعليقات توضيحية أخرى مباشرةً على الصور للإجابة عن أسئلة مكانية مثل "أين يجب وضع هذا العنصر؟".

لتفعيل ميزة "التفكير المرئي"، اضبط [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) كأداة. سيستخدم النموذج تلقائيًا الرمز البرمجي لمعالجة الصور عند الحاجة.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

لمزيد من التفاصيل حول تنفيذ الرمز باستخدام الصور، يُرجى الاطّلاع على [تنفيذ الرمز](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar#images).

### استجابات الوظائف المتعددة الوسائط

تتيح ميزة [استدعاء الدوال المتعددة الوسائط](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#multimodal) للمستخدمين الحصول على ردود تتضمّن كائنات متعددة الوسائط، ما يتيح الاستفادة بشكل أفضل من إمكانات استدعاء الدوال في النموذج. تتيح ميزة "استدعاء الدوال" العادية الردود المستندة إلى النصوص فقط:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### الجمع بين الأدوات المضمّنة واستدعاء الدوال

يتيح Gemini 3 استخدام أدوات مضمّنة (مثل &quot;بحث Google&quot; وسياق عنوان URL و[المزيد](https://ai.google.dev/gemini-api/docs/tools?hl=ar)) وأدوات مخصّصة [لاستدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) في طلب بيانات من واجهة برمجة التطبيقات واحد، ما يتيح إمكانية تنفيذ مهام سير عمل أكثر تعقيدًا. يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## الترحيل من Gemini 2.5

‫Gemini 3 هي مجموعة النماذج الأكثر تطورًا لدينا حتى الآن، وهي تقدّم تحسينًا تدريجيًا مقارنةً بـ Gemini 2.5. عند نقل البيانات، يجب مراعاة ما يلي:

- **التفكير:** إذا كنت تستخدم سابقًا هندسة الطلبات المعقّدة (مثل سلسلة الأفكار) لإجبار Gemini 2.5 على التفكير، جرِّب Gemini 3 مع `thinking_level: "high"` وطلبات مبسطة.
- **إعدادات درجة العشوائية:** إذا كان الرمز الحالي يضبط درجة العشوائية بشكل صريح (خاصةً على قيم منخفضة للحصول على نتائج خوارزمية حتمية)، ننصحك بإزالة هذا المَعلمة واستخدام القيمة التلقائية 1.0 في Gemini 3 لتجنُّب أي مشاكل محتملة في التكرار أو انخفاض الأداء في المهام المعقّدة.
- **فهم مستندات PDF والمستندات الأخرى:**
  إذا كنت تعتمد على سلوك معيّن لتحليل المستندات الكثيفة، اختبِر الإعداد الجديد
  `media_resolution_high` لضمان استمرار الدقة.
- **استخدام الرموز المميزة:** قد يؤدي الانتقال إلى الإعدادات التلقائية في Gemini 3 إلى **زيادة** استخدام الرموز المميزة لملفات PDF، ولكن **تقليل** استخدام الرموز المميزة للفيديوهات. إذا تجاوزت الطلبات الآن قدرة الاستيعاب بسبب زيادة الدقة التلقائية، ننصحك بتقليل دقة الوسائط بشكل صريح.
- **تقسيم الصور:** لا تتوفّر إمكانات تقسيم الصور (عرض أقنعة على مستوى البكسل للكائنات) في Gemini 3 Pro أو Gemini 3 Flash. بالنسبة إلى أحمال العمل التي تتطلّب تقسيم الصور الأصلي، ننصحك بمواصلة استخدام Gemini 2.5 Flash مع إيقاف ميزة "التفكير" أو [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ar).
- **استخدام الكمبيوتر:** يتوافق Gemini 3 Pro وGemini 3 Flash مع ميزة [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar). على عكس السلسلة 2.5، لن تحتاج إلى استخدام نموذج منفصل للوصول إلى أداة &quot;استخدام الكمبيوتر&quot;.
- **التوافق مع الأدوات**: تتوافق الآن نماذج Gemini 3 مع [الجمع بين الأدوات المضمّنة وميزة استدعاء الدالة](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar). أصبحت ميزة [الربط بالواقع في "خرائط Google"](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) متاحة أيضًا في نماذج Gemini 3.

## التوافق مع OpenAI

بالنسبة إلى المستخدمين الذين يستفيدون من [طبقة التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar)، يتم تلقائيًا ربط المَعلمات العادية (`reasoning_effort` من OpenAI) بمثيلاتها في Gemini (`thinking_level`).

## أفضل الممارسات المتعلّقة بإنشاء الطلبات

‫Gemini 3 هو نموذج استدلال، ما يغيّر طريقة تقديم الطلبات.

- **تعليمات دقيقة:** يجب أن تكون طلبات الإدخال موجزة. يستجيب Gemini 3 بشكل أفضل للتعليمات المباشرة والواضحة. قد يبالغ في تحليل أساليب هندسة الطلبات المطوّلة أو المعقّدة جدًا المستخدَمة مع النماذج القديمة.
- **مستوى التفصيل في الإجابات:** يكون مستوى التفصيل في الإجابات التي يقدّمها Gemini 3 أقل بشكل تلقائي، وهو يفضّل تقديم إجابات مباشرة وفعّالة. إذا كانت حالة الاستخدام تتطلّب شخصية أكثر
  تفاعلية أو "ودودة"، عليك توجيه النموذج بشكل صريح في الطلب (على سبيل المثال، "اشرح هذا الموضوع بأسلوب ودود ومحادث").
- **إدارة السياق:** عند العمل على مجموعات بيانات كبيرة (مثل الكتب الكاملة أو قواعد الرموز أو الفيديوهات الطويلة)، ضَع تعليماتك أو أسئلتك المحدّدة في نهاية الطلب، بعد سياق البيانات. استند في استنتاج النموذج إلى البيانات المقدَّمة من خلال بدء سؤالك بعبارة مثل "استنادًا إلى المعلومات الواردة أعلاه...".

يمكنك الاطّلاع على مزيد من المعلومات حول استراتيجيات تصميم الطلبات في [دليل هندسة الطلبات](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar).

## الأسئلة الشائعة

1. **ما هو تاريخ آخر تحديث للبيانات لـ Gemini 3؟** تاريخ آخر تحديث لبيانات نماذج Gemini 3 هو يناير 2025. للحصول على معلومات أحدث، استخدِم أداة
   [البحث عن المستندات الأساسية](https://ai.google.dev/gemini-api/docs/google-search?hl=ar).
2. **ما هي الحدود القصوى لقدرة الاستيعاب؟** تتيح نماذج Gemini 3 قدرة استيعاب تصل إلى مليون رمز مميّز، كما تتيح إخراج ما يصل إلى 64 ألف رمز مميّز.
3. **هل تتوفّر فئة مجانية من Gemini 3؟** يتضمّن Gemini API فئات مجانية من Gemini 3 Flash`gemini-3-flash-preview` و3.1 Flash-Lite`gemini-3.1-flash-lite`. يمكنك تجربة Gemini 3.1 Pro و3 Flash مجانًا في Google AI Studio، ولكن لا تتوفّر طبقة مجانية من `gemini-3.1-pro-preview` في Gemini API.
4. **هل سيظلّ رمز `thinking_budget` القديم صالحًا؟** نعم، لا يزال `thinking_budget` متاحًا للتوافق مع الأنظمة القديمة، ولكن ننصحك بالانتقال إلى `thinking_level` لتحقيق أداء أكثر قابلية للتوقّع. يُرجى عدم استخدام كليهما في الطلب نفسه.
5. **هل يتوافق Gemini 3 مع Batch API؟** نعم، يتوافق Gemini 3 مع
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar).
6. **هل تتوفّر ميزة "التخزين المؤقت للسياق"؟** نعم، تتوافق [ميزة "التخزين المؤقت للسياق"](https://ai.google.dev/gemini-api/docs/caching?hl=ar) مع Gemini 3.
7. **ما هي الأدوات المتوافقة مع Gemini 3؟** يتوافق Gemini 3 مع [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) و[استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) و[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) و[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar). يتيح أيضًا استخدام [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) العادي لأدواتك المخصّصة،
   و[بالتزامن مع الأدوات المضمّنة](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).
8. **ما هي `gemini-3.1-pro-preview-customtools`؟** إذا كنت تستخدم `gemini-3.1-pro-preview` وتجاهل النموذج أدواتك المخصّصة لصالح أوامر bash، جرِّب النموذج `gemini-3.1-pro-preview-customtools` بدلاً من ذلك. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar#gemini-31-pro-preview-customtools)

## الخطوات التالية

- بدء استخدام [كتاب وصفات Gemini 3](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=ar#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- راجِع دليل Cookbook المخصّص حول [مستويات التفكير](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=ar#gemini3) وكيفية نقل البيانات من ميزانية التفكير إلى مستويات التفكير.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
