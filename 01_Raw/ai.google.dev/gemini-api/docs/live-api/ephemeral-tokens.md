---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ar
fetched_at: 2026-09-28T06:11:02.818070+00:00
title: "\u0627\u0644\u0631\u0645\u0648\u0632 \u0627\u0644\u0645\u0645\u064a\u0651\u0632\u0629 \u0627\u0644\u0645\u0624\u0642\u062a\u0629 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الرموز المميّزة المؤقتة

الرموز المميزة المؤقتة هي رموز مصادقة قصيرة الأجل للوصول إلى Gemini
API من خلال [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). تم تصميمها لتعزيز الأمان عند
الاتصال مباشرةً من جهاز المستخدم بواجهة برمجة التطبيقات (تنفيذ من
[العميل إلى الخادم](https://ai.google.dev/gemini-api/docs/live?hl=ar#implementation-approach)
). على غرار مفاتيح واجهة برمجة التطبيقات العادية، يمكن استخراج الرموز المميزة المؤقتة من التطبيقات من جهة العميل، مثل متصفّحات الويب أو تطبيقات الأجهزة الجوّالة. ولكن نظرًا إلى أنّ الرموز المميزة المؤقتة تنتهي صلاحيتها بسرعة ويمكن تقييدها، فإنّها تقلّل بشكلٍ كبير من المخاطر الأمنية في بيئة التشغيل الفعلي. عليك استخدامها عند الوصول إلى Live API مباشرةً من التطبيقات من جهة العميل لتعزيز أمان مفتاح واجهة برمجة التطبيقات.

## آلية عمل الرموز المميزة المؤقتة

في ما يلي آلية عمل الرموز المميزة المؤقتة على مستوى عالٍ:

1. يتم التحقّق من هوية العميل (مثل تطبيق الويب) باستخدام الخلفية.
2. تطلب الخلفية رمزًا مميزًا مؤقتًا من خدمة توفير Gemini API.
3. يصدر Gemini API رمزًا مميزًا قصير الأجل.
4. ترسل الخلفية الرمز المميز إلى العميل من أجل اتصالات WebSocket بـ Live API. يمكنك إجراء ذلك من خلال استبدال مفتاح واجهة برمجة التطبيقات برمز مميز مؤقت.
5. يستخدم العميل بعد ذلك الرمز المميز كما لو كان مفتاح واجهة برمجة تطبيقات.

![نظرة عامة على الرموز المميزة المؤقتة](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=ar)

يؤدي ذلك إلى تعزيز الأمان لأنّه حتى في حال استخراج الرمز المميز، يكون قصير الأجل، على عكس مفتاح واجهة برمجة التطبيقات الطويل الأجل الذي يتم نشره من جهة العميل. بما أنّ العميل يرسل البيانات مباشرةً إلى Gemini، يؤدي ذلك أيضًا إلى تحسين وقت الاستجابة وتجنُّب حاجة الخلفيات إلى توجيه بيانات الوقت الفعلي.

## إنشاء رمز مميز مؤقت

في ما يلي مثال مبسط على كيفية الحصول على رمز مميز مؤقت من Gemini.
بشكلٍ تلقائي، سيكون لديك دقيقة واحدة لبدء جلسات Live API جديدة باستخدام الرمز المميز من هذا الطلب (`newSessionExpireTime`) و30 دقيقة لإرسال الرسائل عبر هذا الاتصال (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
    },
  });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

للاطّلاع على قيود قيمة `expireTime` والإعدادات التلقائية ومواصفات الحقول الأخرى، يُرجى مراجعة مرجع واجهة برمجة التطبيقات
.
ضمن الإطار الزمني `expireTime`، ستحتاج إلى
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=ar#session-resumption) لإعادة ربط المكالمة كل 10 دقائق (يمكن إجراء ذلك باستخدام الرمز المميز نفسه حتى
إذا كانت `uses: 1`).

من الممكن أيضًا ربط رمز مميز مؤقت بمجموعة من الإعدادات. قد يكون ذلك مفيدًا لزيادة تحسين أمان تطبيقك والاحتفاظ بتعليمات النظام من جهة الخادم.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.8-live',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.8-live',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.8-live",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

يمكنك أيضًا ربط مجموعة فرعية من الحقول، يُرجى الاطّلاع على [مستندات حزمة تطوير البرامج (SDK)](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
لمزيد من المعلومات.

## الاتصال بـ Live API باستخدام رمز مميز مؤقت

بعد الحصول على رمز مميز مؤقت، يمكنك استخدامه كما لو كان مفتاح واجهة برمجة تطبيقات (ولكن تذكَّر أنّه لا يعمل إلا مع Live API ومع الإصدار `v1beta` من واجهة برمجة التطبيقات فقط).

لا تكون الرموز المميزة المؤقتة مفيدة إلا عند نشر التطبيقات
التي تتّبع نهج التنفيذ من [العميل إلى الخادم](https://ai.google.dev/gemini-api/docs/live?hl=ar#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

يُرجى الاطّلاع على مقالة [البدء في استخدام Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) لمزيد من الأمثلة.

## أفضل الممارسات

- اضبط مدة انتهاء صلاحية قصيرة باستخدام المَعلمة `expire_time`.
- تنتهي صلاحية الرموز المميزة، ما يتطلب إعادة بدء عملية التوفير.
- تحقَّق من المصادقة الآمنة للخلفية. لن تكون الرموز المميزة المؤقتة آمنة إلا بقدر أمان طريقة المصادقة في الخلفية.
- بشكلٍ عام، تجنَّب استخدام الرموز المميزة المؤقتة للاتصالات من الخلفية إلى Gemini، لأنّ هذا المسار يُعتبر آمنًا عادةً.

## القيود

في الوقت الحالي، تتوافق الرموز المميزة المؤقتة مع [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) فقط.

## الخطوات التالية

- يُرجى قراءة مرجع Live API [حول الرموز المميزة المؤقتة](https://ai.google.dev/api/live?hl=ar#ephemeral-auth-tokens)
  لمزيد من المعلومات.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-17 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-17 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
