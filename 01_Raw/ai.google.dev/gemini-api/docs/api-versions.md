---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=ar
fetched_at: 2026-05-05T20:00:43.052626+00:00
title: "\u0634\u0631\u062d \u0625\u0635\u062f\u0627\u0631\u0627\u062a \u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api?hl=ar)

إرسال ملاحظات

# شرح إصدارات واجهة برمجة التطبيقات

تقدّم هذه الوثيقة نظرة عامة عالية المستوى على الاختلافات بين الإصدارَين `v1`
و `v1beta` من Gemini API.

- **v1**: هو الإصدار الثابت من واجهة برمجة التطبيقات. تكون الميزات في الإصدار الثابت متوافقة تمامًا طوال فترة رقم الإصدار الرئيسي. في حال إجراء أي تغييرات قد تؤدي إلى عطل، سيتم إنشاء رقم الإصدار الرئيسي التالي من واجهة برمجة التطبيقات وسيتم إيقاف الإصدار الحالي نهائيًا بعد فترة زمنية معقولة.
  يمكن إضافة تغييرات متوافقة إلى واجهة برمجة التطبيقات بدون تغيير الإصدار الرئيسي.
- **v1beta**: يتضمّن هذا الإصدار ميزات مبكرة قد تكون قيد التطوير وقد تخضع لتغييرات غير متوافقة. ليس هناك أيضًا ما يضمن نقل الميزات في الإصدار التجريبي إلى الإصدار الثابت. **إذا كنت بحاجة إلى الاستقرار في بيئة الإنتاج ولا يمكنك تحمّل مخاطر التغييرات غير المتوافقة، ننصحك بعدم استخدام هذا الإصدار في مرحلة الإنتاج.**

| الميزة | v1 | v1beta |
| --- | --- | --- |
| إنشاء محتوى - إدخال نص فقط |  |  |
| إنشاء محتوى - إدخال نص وصورة |  |  |
| إنشاء محتوى - إخراج نص |  |  |
| إنشاء محتوى - محادثات متعددة الأدوار (محادثة) |  |  |
| إنشاء محتوى - طلبات الدوال |  |  |
| إنشاء محتوى - البث |  |  |
| تضمين محتوى - إدخال نص فقط |  |  |
| إنشاء إجابة |  |  |
| أداة استرجاع دلالية |  |  |
| واجهة برمجة التطبيقات Interactions API |  |  |

- - متاح
- - لن يكون متاحًا أبدًا

## ضبط إصدار واجهة برمجة التطبيقات في حزمة تطوير برامج (SDK)

تستخدم حِزم SDK الخاصة بـ Gemini API الإصدار `v1beta` تلقائيًا، ولكن يمكنك اختيار استخدام إصدارات أخرى من خلال ضبط إصدار واجهة برمجة التطبيقات كما هو موضّح في عينة التعليمات البرمجية التالية:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### راحة

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
