---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar
fetched_at: 2026-09-14T05:40:57.490001+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u062f\u0644\u0627\u0644 \u062d\u0633\u0628 \u0627\u0644\u0623\u0648\u0644\u0648\u064a\u0629 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستدلال حسب الأولوية

الوصف: تعرَّف على كيفية تحسين وقت الاستجابة باستخدام مستوى الاستنتاج "الأولوية" في Interactions API

‫Gemini Priority API هو مستوى استنتاج متميّز مصمّم لأحمال العمل الأساسية للمؤسسة التي تتطلّب وقت استجابة منخفضًا وأعلى مستوى من الموثوقية بسعر متميّز. تُمنح الأولوية لحركة المرور في مستوى "الأولوية" على حركة المرور في واجهة برمجة التطبيقات العادية ومستوى "المرونة".

يتوفّر الاستنتاج في مستوى "الأولوية" في جميع نقاط نهاية Interactions API.

## كيفية استخدام مستوى "الأولوية"

لاستخدام مستوى "الأولوية"، اضبط حقل `service_tier` في طلبك على `priority`. المستوى التلقائي هو "عادي" إذا تم حذف الحقل.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## آلية عمل الاستنتاج في مستوى "الأولوية"

يوجّه الاستنتاج في مستوى "الأولوية" الطلبات إلى قوائم انتظار الحوسبة عالية الأهمية، ما يوفّر أداءً سريعًا ويمكن التنبؤ به للتطبيقات التي يتفاعل معها المستخدمون. آليته الأساسية هي الرجوع السلس من جهة الخادم إلى المعالجة العادية لحركة المرور التي تتجاوز الحدود الديناميكية، ما يضمن استقرار التطبيق بدلاً من تعذُّر معالجة الطلب.

| الميزة | الأولوية | خطة "الرزمة العادية" | التعبير | مجمّعة |
| --- | --- | --- | --- | --- |
| **الأسعار** | أعلى بنسبة %75 إلى %100 من الخطة العادية | السعر الكامل | خصم% 50 | خصم% 50 |
| **وقت الاستجابة** | ثوانٍ | من ثوانٍ إلى دقائق | دقائق (الهدف من دقيقة واحدة إلى 15 دقيقة) | ما يصل إلى 24 ساعة |
| **الموثوقية** | عالية (لا يمكن تقليلها) | عالية / متوسطة إلى عالية | أفضل جهد (يمكن تقليلها) | عالية (للإنتاجية) |
| **الواجهة** | متزامن | متزامن | متزامن | غير متزامن |

### المزايا الرئيسية

- **وقت استجابة منخفض**: مصمّم لأوقات الاستجابة بالثواني لأدوات الذكاء الاصطناعي التفاعلية التي يتفاعل معها المستخدمون.
- **موثوقية عالية**: يتم التعامل مع حركة المرور بأعلى مستوى من الأهمية ولا يمكن
  تقليلها على الإطلاق.
- **التكيّف مع الإصدارات الأقدم**: يتم تلقائيًا الرجوع إلى مستوى "الرزمة العادية" لمعالجة الارتفاعات المفاجئة في حركة المرور التي تتجاوز الحدود الديناميكية بدلاً من تعذُّر معالجتها، ما يمنع انقطاع الخدمة.
- **الحدّ من المش1اكل**: يستخدم الطريقة المتزامنة نفسها `create` التي يستخدمها مستوى "
  الرزمة العادية" ومستوى "المرونة".

### حالات الاستخدام

تكون المعالجة في مستوى "الأولوية" مثالية لسير العمل الأساسي للمؤسسة حيث يكون الأداء والموثوقية في غاية الأهمية.

- **تطبيقات الذكاء الاصطناعي التفاعلية**: روبوتات الدردشة ومساعدو خدمة العملاء حيث
  يدفع المستخدمون سعرًا متميّزًا ويتوقّعون استجابات سريعة ومتّسقة.
- **محركات اتخاذ القرارات في الوقت الفعلي**: الأنظمة التي تتطلّب نتائج موثوقة جدًا ومنخفضة وقت الاستجابة
  ، مثل فرز التذاكر المباشر أو رصد الاحتيال.
- **ميزات العملاء المتميّزين**: المطوّرون الذين يحتاجون إلى ضمان أهداف أعلى على مستوى الخدمة (SLOs) للعملاء الذين يدفعون.

### حدود معدّل الاستخدام

تفرض حدود معدّل الاستخدام الخاصة بها على الاستهلاك في مستوى "الأولوية"، على الرغم من احتساب الاستهلاك
ضمن [حدود معدّل الاستخدام الإجمالية لحركة المرور التفاعلية](https://aistudio.google.com/rate-limit?hl=ar). حدود معدّل الاستخدام التلقائية للاستنتاج في مستوى "الأولوية" هي **0.3 ضعف حدّ معدّل الاستخدام العادي للطراز / المستوى**

### تسلسل منطقي للرجوع السلس

إذا تم تجاوز حدود مستوى "الأولوية" بسبب الازدحام، يتم **تلقائيًا وبشكل سلس** الرجوع إلى المعالجة العادية للطلبات التي تتجاوز الحدّ بدلاً من تعذُّر معالجتها مع ظهور الخطأ 503 أو 429. تتم فوترة الطلبات التي تم الرجوع إلى معالجتها بالسعر العادي، وليس بالسعر المتميّز لمستوى "الأولوية".

### مسؤولية العميل

- **مراقبة الردود**: على المطوّرين مراقبة `x-gemini-service-tier`
  العنوان في ردّ واجهة برمجة التطبيقات لرصد ما إذا كان يتم الرجوع بشكل متكرّر إلى
  `standard` لمعالجة الطلبات.
- **إعادة المحاولات**: على العملاء تنفيذ تسلسل منطقي لإعادة المحاولة/الرجوع الأسي لـ
  الأخطاء العادية، مثل `DEADLINE_EXCEEDED`.

## الأسعار

يتم تسعير الاستنتاج في مستوى "الأولوية" بنسبة %75 إلى %100 أعلى من [واجهة برمجة التطبيقات العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) ويتم تحصيل الرسوم لكل رمز مميّز.

## الطُرز المتوافقة

تسمح الطُرز التالية بالاستنتاج في مستوى "الأولوية":

| الطراز | الاستنتاج في مستوى "الأولوية" |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ‫✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ‫✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ‫✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ‫✔️ |
| [‫Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ‫✔️ |
| [‫Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ‫✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ‫✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ‫✔️ |
| [‫Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ‫✔️ |

## الخطوات التالية

- [الاستنتاج المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar) لتقليل التكلفة
- [الرموز المميّزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar): التعرّف على الرموز المميّزة

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
