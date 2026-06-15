---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ar
fetched_at: 2026-06-15T06:25:19.101062+00:00
title: "\u0627\u0644\u0631\u0645\u0648\u0632 \u0627\u0644\u0645\u0645\u064a\u0651\u0632\u0629 \u0627\u0644\u0645\u0624\u0642\u062a\u0629 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الرموز المميّزة المؤقتة

الرموز المميزة المؤقتة هي رموز مميزة قصيرة الأمد للمصادقة تُستخدَم للوصول إلى Gemini API من خلال [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). وهي مصمَّمة لتعزيز الأمان عند الربط مباشرةً من جهاز المستخدم بواجهة برمجة التطبيقات (تنفيذ [من العميل إلى الخادم](https://ai.google.dev/gemini-api/docs/live?hl=ar#implementation-approach)). مثل مفاتيح واجهة برمجة التطبيقات العادية، يمكن استخراج الرموز المميزة المؤقتة من التطبيقات من جهة العميل، مثل متصفّحات الويب أو تطبيقات الأجهزة الجوّالة. ولكن بما أنّ الرموز المميزة المؤقتة تنتهي صلاحيتها بسرعة ويمكن حصر استخدامها، فإنّها تقلّل بشكل كبير من المخاطر الأمنية في بيئة التشغيل الفعلي. يجب استخدامها عند الوصول إلى Live API مباشرةً من التطبيقات من جهة العميل لتحسين أمان مفتاح واجهة برمجة التطبيقات.

## طريقة عمل الرموز المميزة المؤقتة

في ما يلي كيفية عمل الرموز المميزة المؤقتة على مستوى عالٍ:

1. يتم مصادقة العميل (مثل تطبيق الويب) مع الخلفية.
2. يطلب الخلفية رمزًا مميّزًا مؤقتًا من خدمة التوفير في Gemini API.
3. يصدر Gemini API رمزًا مميزًا صالحًا لفترة قصيرة.
4. يرسل الخلفية الرمز المميّز إلى العميل لإجراء اتصالات WebSocket بواجهة Live API. يمكنك إجراء ذلك عن طريق استبدال مفتاح واجهة برمجة التطبيقات برمز مميّز مؤقت.
5. يستخدم العميل بعد ذلك الرمز المميز كما لو كان مفتاح واجهة برمجة تطبيقات.

![نظرة عامة على الرموز المميزة المؤقتة](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=ar)

يؤدي ذلك إلى تعزيز الأمان لأنّ الرمز المميز يكون صالحًا لفترة قصيرة حتى إذا تم استخراجه، على عكس مفتاح واجهة برمجة التطبيقات الذي يكون صالحًا لفترة طويلة ويتم نشره من جهة العميل. وبما أنّ العميل يرسل البيانات مباشرةً إلى Gemini، يؤدي ذلك أيضًا إلى تحسين وقت الاستجابة وتجنُّب الحاجة إلى أن تعمل الخلفيات كوكيل للبيانات في الوقت الفعلي.

## إنشاء رمز مميّز مؤقت

في ما يلي مثال مبسّط على كيفية الحصول على رمز مميّز مؤقت من Gemini.
بشكلٍ تلقائي، سيكون لديك دقيقة واحدة لبدء جلسات جديدة في Live API باستخدام الرمز المميّز من هذا الطلب (`newSessionExpireTime`)، و30 دقيقة لإرسال الرسائل عبر هذا الاتصال (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
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
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

للاطّلاع على قيود القيمة التلقائية `expireTime` والإعدادات التلقائية ومواصفات الحقول الأخرى، يُرجى الرجوع إلى
[مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/live?hl=ar#ephemeral-auth-tokens).
خلال الإطار الزمني `expireTime`، عليك
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=ar#session-resumption) إعادة ربط المكالمة كل 10 دقائق (يمكن إجراء ذلك باستخدام الرمز المميز نفسه حتى إذا كان `uses: 1`).

يمكن أيضًا ربط رمز مميّز مؤقت بمجموعة من الإعدادات. قد يكون ذلك مفيدًا لتعزيز أمان تطبيقك والحفاظ على تعليمات نظامك على الخادم.

### Python

```
from google import genai

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
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
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

يمكنك أيضًا قفل مجموعة فرعية من الحقول، راجِع [مستندات حزمة SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
للحصول على مزيد من المعلومات.

## الربط بواجهة Live API باستخدام رمز مميز مؤقت

بعد الحصول على رمز مميّز مؤقت، يمكنك استخدامه كما لو كان مفتاح واجهة برمجة تطبيقات (ولكن تذكَّر أنّه يعمل فقط مع واجهة برمجة التطبيقات المباشرة، ومع الإصدار `v1alpha` من واجهة برمجة التطبيقات فقط).

لا يضيف استخدام الرموز المميزة المؤقتة قيمة إلا عند نشر التطبيقات التي تتّبع نهج [التنفيذ من العميل إلى الخادم](https://ai.google.dev/gemini-api/docs/live?hl=ar#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
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

يمكنك الاطّلاع على [بدء استخدام Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) للحصول على مزيد من الأمثلة.

## أفضل الممارسات

- اضبط مدة انتهاء صلاحية قصيرة باستخدام المَعلمة `expire_time`.
- تنتهي صلاحية الرموز المميزة، ما يتطلّب إعادة بدء عملية توفير المتطلبات اللازمة.
- تأكَّد من أنّ عملية المصادقة الآمنة متوافقة مع الخلفية البرمجية الخاصة بك، لأنّ الرموز المميزة المؤقتة لن تكون آمنة إلا إذا كانت طريقة المصادقة في الخلفية البرمجية آمنة.
- بشكل عام، تجنَّب استخدام الرموز المميزة المؤقتة للاتصالات بين الخلفية وGemini، لأنّ هذا المسار يُعدّ آمنًا عادةً.

## القيود

تتوافق الرموز المميزة المؤقتة مع [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) فقط في الوقت الحالي.

## الخطوات التالية

- يمكنك الاطّلاع على [مرجع](https://ai.google.dev/api/live?hl=ar#ephemeral-auth-tokens) Live API بشأن الرموز المميزة المؤقتة للحصول على مزيد من المعلومات.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
