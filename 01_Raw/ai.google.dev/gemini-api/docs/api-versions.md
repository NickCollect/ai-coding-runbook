---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=ar
fetched_at: 2026-08-31T06:31:26.610695+00:00
title: "\u0634\u0631\u062d \u0625\u0635\u062f\u0627\u0631\u0627\u062a \u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api?hl=ar)

إرسال ملاحظات

# شرح إصدارات واجهة برمجة التطبيقات

تقدّم هذه المستندات نظرة عامة عالية المستوى على الاختلافات بين الإصدارَين `v1`
و `v1beta` من Gemini API.

- **v1**: هو إصدار مستقر من واجهة برمجة التطبيقات. تكون الميزات في الإصدار الثابت متوافقة تمامًا طوال فترة رقم الإصدار الرئيسي. في حال إجراء أي تغييرات قد تؤدي إلى عطل، سيتم إنشاء رقم إصدار رئيسي جديد من واجهة برمجة التطبيقات وسيتم إيقاف الإصدار الحالي نهائيًا بعد فترة زمنية معقولة.
  يمكن إضافة تغييرات متوافقة إلى واجهة برمجة التطبيقات بدون تغيير رقم الإصدار الرئيسي. تتوفّر **‫Interactions API** وميزاتها الأساسية بشكل عام في الإصدار `v1`.
- **v1beta**: يتضمّن هذا الإصدار ميزات وإمكانات مبكرة قيد التطوير حاليًا. قد تخضع الميزات في الإصدار `v1beta` للتغييرات أثناء تحسينها استنادًا إلى الملاحظات، ولكنها تتيح لك تجربة إمكانات جديدة قبل ترقيتها إلى إصدار مستقر.

## الإمكانات والميزات المتوافقة

يوضّح الجدول التالي مدى توفّر الإمكانات في الإصدارَين `v1` (إصدار عام)
و `v1beta` (إصدار تجريبي). تنطبق إمكانات وأدوات واجهة برمجة التطبيقات الأساسية على كلٍّ من Interactions API و`generateContent` ما لم يتم تحديد خلاف ذلك:

| الميزة | v1 | v1beta |
| --- | --- | --- |
| **إمكانات واجهة برمجة التطبيقات الأساسية** |  |  |
| [‫Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=ar) |  |  |
| [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) |  |  |
| [الناتج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) |  |  |
| [التفكير / الاستدلال](https://ai.google.dev/gemini-api/docs/thinking?hl=ar) |  |  |
| [تعليمات النظام](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ar) |  |  |
| [إخراج الصوت (إعدادات الكلام)](https://ai.google.dev/gemini-api/docs/audio?hl=ar) |  |  |
| [مستوى الخدمة (الأولوية / المرونة)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar) |  |  |
| **الأدوات** |  |  |
| [أداة تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) |  |  |
| [الاستناد إلى "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) |  |  |
| [الاستناد إلى "خرائط Google"](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) |  |  |
| [أداة سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) |  |  |
| [أداة البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) |  |  |
| [أداة استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar) |  |  |
| [أداة خوادم MCP](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=ar) |  |  |
| **واجهات برمجة التطبيقات في الوقت الفعلي** |  |  |
| [‫Live API (بروتوكولات WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=ar) |  |  |
| [‫Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ar) |  |  |
| [الرموز المميّزة المؤقتة (‫Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ar) |  |  |
| **واجهات برمجة التطبيقات للمنصات** |  |  |
| [‫Models API](https://ai.google.dev/gemini-api/docs/models?hl=ar) |  |  |
| [مسار خدمة الملفات](https://ai.google.dev/gemini-api/docs/files?hl=ar) |  |  |
| [مسار مساحات تخزين البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) |  |  |
| [‫Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=ar) |  |  |
| [‫Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=ar) |  |  |
| [تخزين السياق مؤقتًا](https://ai.google.dev/gemini-api/docs/caching?hl=ar) |  |  |

- - متاح

## ضبط إصدار واجهة برمجة التطبيقات في حزمة تطوير برامج (SDK)

تستخدم حزم تطوير البرامج (SDK) الخاصة بـ Gemini API الإصدار `v1beta` تلقائيًا، ولكن يمكنك تحديد الإصدارات بشكلٍ صريح من خلال ضبط إصدار واجهة برمجة التطبيقات كما هو موضّح في عينة التعليمات البرمجية التالية:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
  }'
```

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-28 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-28 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
