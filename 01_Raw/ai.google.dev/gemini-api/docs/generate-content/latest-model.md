---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=ar
fetched_at: 2026-07-27T04:42:56.604083+00:00
title: "\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0623\u062d\u062f\u062b \u0646\u0645\u0627\u0630\u062c Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استخدام أحدث نماذج Gemini

[هذه الصفحة](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=ar)

يتوفّر للجمهور العام (GA) كلّ من Gemini 3.6 Flash (`gemini-3.6-flash`) وGemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) وهما جاهزان للاستخدام في مرحلة الإنتاج.

- **Gemini 3.6 Flash**: أداء أقوى في المهام المعقّدة التي تتضمّن وكلاء ومتعددة الوسائط مع تقليل استخدام الرموز المميّزة، بسعر أقل من 3.5 Flash.
- **Gemini 3.5 Flash-Lite**: النموذج الأسرع والأقل تكلفة في عائلة 3.5. يتفوّق على الأجيال السابقة من Flash-Lite في التنفيذ عالي الإنتاجية.

يوضّح هذا الدليل الميزات الجديدة في كل نموذج، والتغييرات في واجهة برمجة التطبيقات التي تؤثر في الرمز، وكيفية نقل البيانات.

### Gemini 3.6 Flash

1. تثبيت المهارة:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
   ```
2. تطبيق المهارة:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. تثبيت المهارة:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
   ```
2. تطبيق المهارة:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## نماذج جديدة

| الطراز | رقم تعريف الطراز | مستوى التفكير التلقائي | الأسعار | الوصف |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | ‏1.50 دولار أمريكي لكل مليون رمز إدخال و7.50 دولار أمريكي لكل مليون رمز إخراج | يوازن بين السرعة والذكاء في المهام التي تتضمّن وكلاء ومتعددة الوسائط. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | ‏0.30 دولار أمريكي لكل مليون رمز إدخال و2.50 دولار أمريكي لكل مليون رمز إخراج | النموذج الأسرع والأقل تكلفة في عائلة 3.5 للتنفيذ عالي الإنتاجية. |

يتوافق كلا النموذجين مع قدرة الاستيعاب التي تبلغ مليون رمز مميّز، وأقصى عدد لرموز الإخراج المميّزة يبلغ 64 ألفًا، وإمكانات التفكير، والمجموعة الكاملة من الأدوات المضمّنة، بما في ذلك [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar).

للاطّلاع على المواصفات الكاملة، يُرجى الانتقال إلى صفحات النماذج:

- [صفحة نموذج Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar)
- [صفحة نموذج Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar)

للاطّلاع على الأسعار التفصيلية، يُرجى الانتقال إلى [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## التشغيل السريع

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(response.text);
}

main();
```

### راحة

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## ما جديد Gemini 3.6 Flash؟

- **تقليل الرموز المميّزة والتحويلات:** يُكمل عمليات سير العمل المتعددة الخطوات بعدد أقل من خطوات الاستدلال والتحويلات في المحادثة وعمليات استدعاء الأدوات مقارنةً بـ Gemini 3.5. ويقلّل أيضًا من تكرار حلقات التنفيذ.
- **تحسين إنشاء الرموز:** يُنشئ رموزًا جاهزة للاستخدام في مرحلة الإنتاج بجودة أعلى وعدد أقل من التعديلات غير المرغوب فيها وعدد أقل من حلقات تصحيح الأخطاء.
- **تحسين اتّباع التعليمات**: يقلّل من التغييرات غير المرغوب فيها في الملفات أثناء مهام التشخيص.
- **الاستدلال القوي متعدد الوسائط والمكاني:** أداء محسّن في تفسير الرسوم البيانية وتحويل المخططات المرئية وإنشاء تنسيقات الويب المتعددة العناصر.
- **الفحص المبرمَج المسبق:** يفضّل تشغيل النصوص البرمجية لرموز التشخيص قبل إجراء التغييرات بشكل متكرر أكثر من Gemini 3.5 Flash. يؤدي ذلك إلى تحسين الدقة في المهام المعقّدة، ولكن يمكن أن يضيف خطوات استكشافية إضافية في أعمال الواجهة الأمامية البسيطة.
- **إمكانية استخدام الكمبيوتر:** متوافقة كأداة أصلية لأتمتة واجهة المستخدم التي تتضمّن وكلاء.
- **تفضيل تصميم واجهة المستخدم**: أفضل في إنشاء رموز عملية، على الرغم من أنّ المُقيِّمين البشريين فضّلوا النماذج السابقة للتنسيق والتصميم المرئيين. يمكنك التخفيف من ذلك من خلال تقديم إرشادات تصميم واضحة.
- **مستوى التفكير التلقائي (متوسط):** يستخدم مستوى التفكير التلقائي `medium` نفسه الذي يستخدمه Gemini 3.5 Flash.
- **أسعار مخفّضة**: تكاليف أقل لرموز الإخراج المميّزة (7.50 دولار أمريكي لكل مليون رمز مميّز مقابل 9.00 دولار أمريكي لكل مليون رمز مميّز في 3.5 Flash). تبقى رموز الإدخال المميّزة عند 1.50 دولار أمريكي لكل مليون رمز مميّز.

## ما جديد Gemini 3.5 Flash-Lite؟

- **تقليل وقت استجابة تنفيذ المهام:** أعلى إنتاجية في عائلة 3.5 لتحليل البيانات واستخراج المستندات بكميات كبيرة.
- **أداء محسّن في الاستدلال والمهام المتعددة الوسائط:** مسار نقل بيانات قوي من Gemini 2.5 Flash، مع تحقيق نتائج أعلى في مهام الاستدلال، مثل HLE (18.0% مقابل 11.0%)، وفي المقاييس المتعددة الوسائط، مثل CharXIV (74.5% مقابل 63.7%).
- **تنسيق الوكلاء الفرعيين وموثوقية الأدوات:** يحسّن موثوقية تنفيذ الأدوات لتطبيق الرموز البرمجية والبحث وعمليات سير عمل بروتوكول سياق النموذج (MCP). يمكنك زيادة مستوى التفكير للتخطيط المستقل ومهام الوكلاء الفرعيين المعقّدة.
- **فهم محسّن للمستندات:** يحسّن الدقة في تحليل المستندات واستخراج البيانات المنظَّمة. يمكنك تجربة كلّ من مستويات التفكير المنخفضة والعالية حسب مدى تعقيد المستند.
- **ترميز الويب التفاعلي ومعالجة البيانات الجدولية:** يحقق أداءً قويًا في JavaScript للواجهة الأمامية ومعالجة البيانات الجدولية من خلال التخطيط باستخدام تطبيق الرموز البرمجية البسيط.
- **روبوت الدردشة والاحتفاظ بالشخصية:** اتّباع أقوى للتعليمات في المحادثات المترابطة والحفاظ على الشخصية بشكل أفضل مقارنةً بـ Gemini 3.1 Flash-Lite.
- **إمكانية استخدام الكمبيوتر:** متوافقة كأداة أصلية لأتمتة واجهة المستخدم التي تتضمّن وكلاء.

## اختيار نموذج Flash أو Flash-Lite المناسب

استخدِم هذا الجدول لاختيار النموذج المناسب ومسار نقل البيانات المناسبين لأحمال العمل.

يتطلّب كلا النموذجين إزالة مَعلمات أخذ العيّنات التي تم إيقافها نهائيًا (`temperature` و`top_p` و`top_k`) وتحويلات النموذج التي تم ملؤها مسبقًا. لمزيد من التفاصيل، يُرجى الاطّلاع على [التغييرات في واجهة برمجة التطبيقات](#api-changes-and-parameter-updates).

| الطراز | حالات الاستخدام الأساسية | الهدف المقترَح لنقل البيانات |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | إنشاء الرموز، والاستدلال المكاني/المتعدد الوسائط، وعمليات سير العمل التي تتضمّن وكلاء ومتعددة الخطوات | **Gemini 3.5 Flash** أو **Gemini 3 Flash (إصدار تجريبي)** أو **Gemini 3.1 Pro** |
| **\*\*Gemini 3.5 Flash-Lite\*\***  `gemini-3.5-flash-lite` | تنفيذ الوكلاء الفرعيين المستقلين، وتحليل البيانات واستخراج المستندات بكميات كبيرة، وتحليل JSON المنظَّم | ‫**Gemini 3.1 Flash-Lite** أو **Gemini 2.5 Flash** |

## وكيل Antigravity المعدَّل

نظرًا إلى أدائه المحسّن، أصبح Gemini 3.6 Flash هو النموذج التلقائي الجديد الذي يشغّل وكيل [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=ar) في Gemini Managed Agents. يمكن تغيير ذلك من خلال ضبط حقل جديد في واجهة برمجة التطبيقات.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## التغييرات في واجهة برمجة التطبيقات وتعديلات المَعلمات

بدءًا من Gemini 3.6 Flash وGemini 3.5 Flash-Lite، تنطبق التغييرات التالية في واجهة برمجة التطبيقات على هذين النموذجين وجميع إصدارات نماذج Gemini المستقبلية.

- **إيقاف مَعلمات أخذ العيّنات نهائيًا**: تم إيقاف `temperature` و`top_p` و`top_k` نهائيًا. تتجاهل واجهة برمجة التطبيقات هذه المَعلمات وتعرض خطأ في الأجيال المستقبلية من النماذج.
- **التحقّق من صحة تحويلات النموذج التي تم ملؤها مسبقًا**: لم يعُد ملء تحويلات النموذج مسبقًا متاحًا. إذا كان آخر تحويل غير فارغ في الطلب هو تحويل `model`، تعرض واجهة برمجة التطبيقات خطأ `400`.

في ما يلي تفسيرات تفصيلية ونماذج رموز برمجية لكل تغيير في واجهة برمجة التطبيقات.

### 1. إيقاف مَعلمات أخذ العيّنات نهائيًا (`temperature` و`top_p` و`top_k`)

تم إيقاف `temperature` و`top_p` و`top_k` نهائيًا وسيتم تجاهلها. في الأجيال المستقبلية من النماذج، سيؤدي تقديم هذه المَعلمات إلى عرض خطأ HTTP 400. **يُرجى إزالة هذه المَعلمات من جميع الطلبات.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

لتحسين الحتمية، يمكنك تحديد تعليمات النظام باستخدام قواعد واضحة لحالة الاستخدام المحدّدة.

### 2. التحقّق من صحة تحويلات النموذج التي تم ملؤها مسبقًا

يُحظر إرسال طلبات واجهة برمجة التطبيقات التي تنتهي بتحويل دور نموذج غير فارغ، وسيتم عرض **خطأ HTTP 400**.

#### ⚠️ تجنّب

في حمولات REST الأولية أو `generateContent` القديمة، يُحظر الآن إنهاء الطلب بتحويل دور نموذج:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ نقل البيانات المقترَح

إذا كان تطبيقك يملأ مسبقًا تحويل نموذج لإخفاء المقدمات أو فرض تنسيق JSON، استخدِم `system_instruction` أو [النواتج المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) بدلاً من ذلك.

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## قائمة التحقّق من نقل البيانات

### Gemini 3.6 Flash

1. تثبيت المهارة:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
   ```
2. تطبيق المهارة:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. تثبيت المهارة:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
   ```
2. تطبيق المهارة:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### نقل البيانات إلى gemini-3.6-flash

- **تعديل رقم تعريف النموذج:** غيِّر سلسلة النموذج المستهدَف إلى `gemini-3.6-flash`.
- **إزالة مَعلمات أخذ العيّنات التي تم إيقافها نهائيًا:**
  - أزِل `temperature` و`top_p` و`top_k` من إعدادات الإنشاء.
  - استبدِل `thinking_budget` بتعداد السلسلة `thinking_level` الذي تم ضبطه على `"medium"` أو `"high"`.
  - أزِل `candidate_count` (غير متوافق مع Gemini 3.x).
- **فرض قواعد التحقّق من صحة التحويلات:**
  - أزِل تحويلات النموذج التي تم ملؤها مسبقًا.
  - تأكَّد من أنّ تحويل المستخدم الأخير يحتوي على نص غير فارغ.
- **تدقيق استدعاء الدوال:**
  - تأكَّد من أنّ جميع عناصر `FunctionResponse` تتضمّن `call_id` و`name`.
  - ضَع مواد العرض المتعددة الوسائط داخل حمولة الاستجابة.
  - نسِّق التعليمات المضمّنة باستخدام `\\n\\n`.
  - إذا ظهرت لك أخطاء `Malformed_Function_Call` مرتبطة بالنص الذي يسبق الأداة، يُرجى الاطّلاع على [الحلول البديلة لمتطلبات النص الذي يسبق الأداة](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=ar#workarounds-for-pre-tool-text-requirements).
- **المتطلبات الأساسية لـ Gemini 3.x:** للاطّلاع على تعديلات حزمة تطوير البرامج (SDK) والحفاظ على توقيع التفكير، يُرجى الاطّلاع على [قائمة التحقّق من نقل البيانات إلى Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=ar#migration).

### نقل البيانات إلى gemini-3.5-flash-lite

- **تعديل رقم تعريف النموذج:** غيِّر سلسلة النموذج المستهدَف إلى `gemini-3.5-flash-lite`.
- **ضبط مستوى التفكير:**
  - للاستخراج أو التوجيه أو التصنيف بكميات كبيرة: اترُك `thinking_level` على `"minimal"` (تلقائيًا) لتحقيق أعلى إنتاجية.
  - بالنسبة إلى الوكلاء الفرعيين المستقلين الذين يتضمّنون عمليات استدعاء الأدوات أو تطبيق الرموز البرمجية أو الاستدلال المتعدد الخطوات: اضبط `thinking_level` على `"medium"` أو `"high"` لمنع الإنهاء المبكر للأداة.
- **إزالة المَعلمات التي تم إيقافها نهائيًا والتحقّق من صحة استدعاء الدوال:** طبِّق [القواعد نفسها التي تنطبق على 3.6 Flash](#migrate-to-gemini-3-6-flash).
- **المتطلبات الأساسية لـ Gemini 3.x:** يُرجى الرجوع إلى [قائمة التحقّق من نقل البيانات إلى Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=ar#migration).

## الخطوات التالية

- راجِع مواصفات واجهة برمجة التطبيقات في [نظرة عامة على النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).
- استكشِف تنسيق الوكلاء المتعددين في دليل [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar).
- اختبِر الطلبات وحسِّنها في [Google AI Studio](https://aistudio.google.com/?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-21 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-21 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
