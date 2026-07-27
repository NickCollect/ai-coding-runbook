---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=ar
fetched_at: 2026-07-27T04:39:56.838232+00:00
title: "\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0623\u062d\u062f\u062b \u0646\u0645\u0627\u0630\u062c Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استخدام أحدث نماذج Gemini

[هذه الصفحة](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=ar)

يتوفّر كلّ من Gemini 3.6 Flash (`gemini-3.6-flash`) وGemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) للجمهور العام وهما جاهزان للاستخدام في مرحلة الإنتاج.

- **Gemini 3.6 Flash**: أداء أقوى في المهام المعقّدة التي تتضمّن وكلاء ومتعددة الوسائط، مع تقليل استخدام الرموز المميزة، وبسعر أقل من 3.5 Flash.
- **‫Gemini 3.5 Flash-Lite**: هو أسرع نموذج وأقل تكلفة في عائلة 3.5. تتفوق على الأجيال السابقة من Flash-Lite في التنفيذ العالي الإنتاجية.

يوضّح هذا الدليل الميزات الجديدة في كل نموذج، والتغييرات في واجهة برمجة التطبيقات التي تؤثّر في الرمز البرمجي، وكيفية نقل البيانات.

### Gemini 3.6 Flash

1. ثبِّت المهارة باتّباع الخطوات التالية:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. طبِّق المهارة باتّباع الخطوات التالية:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. ثبِّت المهارة باتّباع الخطوات التالية:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. طبِّق المهارة باتّباع الخطوات التالية:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## طُرز جديدة

| الطراز | رقم تعريف الطراز | مستوى التفكير التلقائي | الأسعار | الوصف |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | ‫1.50 دولار أمريكي لكل مليون رمز مميّز للإدخال و7.50 دولار أمريكي لكل مليون رمز مميّز للإخراج | يوازن بين السرعة والذكاء لتنفيذ المهام المستندة إلى وكيل والمهام المتعددة الوسائط. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | ‫0.30 دولار أمريكي لكل مليون رمز مميّز مُدخَل و2.50 دولار أمريكي لكل مليون رمز مميّز ناتج | أسرع نموذج 3.5 وأقل تكلفة لتنفيذ المهام التي تتطلّب معدل نقل بيانات عاليًا |

يتيح كلا النموذجين قدرة استيعاب تبلغ مليون رمز مميّز، و64 ألف رمز مميّز كحد أقصى للناتج، وإمكانات التفكير، والحزمة الكاملة من الأدوات المدمجة، بما في ذلك [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar).

للاطّلاع على المواصفات الكاملة، يُرجى الانتقال إلى صفحات الطُرز:

- [صفحة نموذج Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar)
- [صفحة نموذج Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar)

للاطّلاع على الأسعار التفصيلية، يُرجى الانتقال إلى [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## البدء السريع

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a three.js script that renders an interactive 3D robot."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(interaction.outputText);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": {
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }
  }'
```

## ما هو الجديد في Gemini 3.6 Flash؟

- **تقليل عدد الرموز المميزة وعدد مرات التفاعل:** يكمل هذا النموذج مهام سير العمل المتعددة الخطوات بعدد أقل من خطوات الاستدلال ومرات التفاعل مع المستخدم وطلبات استخدام الأدوات مقارنةً بـ Gemini 3.5. ويقلّل أيضًا من تكرار حلقات التنفيذ.
- **تحسين عملية إنشاء الرموز البرمجية:** إنشاء رموز برمجية عالية الجودة وجاهزة للاستخدام مع تقليل التعديلات غير المرغوب فيها وتقليل عمليات تصحيح الأخطاء
- **اتّباع التعليمات بشكل أفضل**: يقلّل من التغييرات غير المرغوب فيها في الملفات أثناء مهام التشخيص.
- **قدرات قوية في الاستدلال المكاني والمتعدد الوسائط:** تحسين الأداء في تفسير الرسوم البيانية وتحويل المخططات المرئية وإنشاء تخطيطات ويب متعددة العناصر
- **الفحص الآلي المسبق:** يفضّل تشغيل نصوص برمجية لتشخيص الأخطاء قبل إجراء التغييرات بشكل متكرّر أكثر من Gemini 3.5 Flash. يؤدي ذلك إلى تحسين الدقة في المهام المعقّدة، ولكن يمكن أن يضيف خطوات استكشافية إضافية في مهام الواجهة الأمامية البسيطة.
- **دعم استخدام الكمبيوتر:** يتم توفير هذه الميزة كأداة أصلية لأتمتة واجهة المستخدم المستقلة.
- **تفضيل تصميم واجهة المستخدم**: أفضل في إنشاء رمز برمجي وظيفي، على الرغم من أنّ المقيّمين البشريين فضّلوا النماذج السابقة من حيث التصميم والتنسيق المرئيين. يمكنك الحدّ من هذه المشكلة من خلال تقديم إرشادات تصميم واضحة.
- **مستوى التفكير التلقائي (متوسط):** يستخدم مستوى التفكير التلقائي `medium` نفسه الذي يستخدمه Gemini 3.5 Flash.
- **الأسعار المخفَّضة**: انخفاض تكاليف رموز الإخراج (7.50 دولار أمريكي لكل مليون رمز مقارنةً بـ 9.00 دولار أمريكي لكل مليون رمز في الإصدار 3.5 Flash). تبقى تكلفة الرموز المميزة المدخَلة 1.50 دولار أمريكي لكل مليون رمز مميز.

## الميزات الجديدة في Gemini 3.5 Flash-Lite

- **وقت استجابة أقل لتنفيذ المهام:** أعلى سرعة نقل بيانات في السلسلة 3.5 لتحليل البيانات الكبيرة واستخراج المستندات.
- **أداء محسّن في الاستدلال والوسائط المتعددة:** مسار نقل قوي من Gemini 2.5 Flash، مع تحقيق نتائج أعلى في مهام الاستدلال، مثل HLE (‏18.0% مقارنةً بـ 11.0%)، ومعايير الوسائط المتعددة، مثل CharXIV (‏74.5% مقارنةً بـ 63.7%).
- **تنظيم الوكلاء الفرعيين وموثوقية الأدوات:** يحسّن موثوقية تنفيذ الأدوات في ما يتعلق بتنفيذ الرموز البرمجية والبحث وسير عمل MCP. زيادة مستوى التفكير في التخطيط المستقل ومهام الوكيل الفرعي المعقّدة
- **تحسين فهم المستندات:** تحسين دقة تحليل المستندات واستخراج البيانات المنظَّمة جرِّب مستويات التفكير المنخفضة والعالية حسب درجة تعقيد المستند.
- **الترميز التفاعلي على الويب ومعالجة البيانات الجدولية:** يحقّق أداءً قويًا في JavaScript من جهة العميل ومعالجة البيانات الجدولية من خلال التخطيط باستخدام تنفيذ الرموز البرمجية البسيط.
- **الاحتفاظ بروبوت الدردشة والشخصية:** إمكانية أفضل في اتّباع التعليمات في المحادثات المترابطة والحفاظ على اتساق الشخصية مقارنةً بنموذج Gemini 3.1 Flash-Lite.
- **دعم استخدام الكمبيوتر:** يتم توفير هذه الميزة كأداة أصلية لأتمتة واجهة المستخدم المستقلة.

## اختيار نموذج Flash أو Flash-Lite المناسب

استخدِم هذا الجدول لاختيار النموذج ومسار نقل البيانات المناسبَين لأحمال العمل.

يتطلّب كلا النموذجين إزالة مَعلمات أخذ العيّنات المتوقّفة نهائيًا (`temperature` و`top_p` و`top_k`) والجُمل النموذجية المُعبّأة مسبقًا. لمزيد من التفاصيل، يُرجى الاطّلاع على [التغييرات في واجهة برمجة التطبيقات](#api-changes-and-parameter-updates).

| الطراز | حالات الاستخدام الأساسية | الهدف المقترَح لعملية نقل البيانات |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | إنشاء الرموز البرمجية، والاستدلال المكاني/المتعدّد الوسائط، وسير العمل المتعدّد الخطوات بالذكاء الاصطناعي الوكيل | **Gemini 3.5 Flash** أو **Gemini 3 Flash (إصدار تجريبي)** أو **Gemini 3.1 Pro** |
| **‫Gemini 3.5 Flash-Lite** `gemini-3.5-flash-lite` | تنفيذ المهام من قِبل وكلاء فرعيين مستقلين، وتحليل البيانات واستخراج المستندات بكميات كبيرة، وتحليل JSON المنظَّم | **Gemini 3.1 Flash-Lite** أو **Gemini 2.5 Flash** |

## وكيل Antigravity المعدَّل

بفضل أدائه المحسّن، أصبح Gemini 3.6 Flash الآن النموذج التلقائي الجديد الذي يشغّل [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar) في الوكلاء المُدارون. يمكن تغيير ذلك من خلال ضبط حقل جديد في واجهة برمجة التطبيقات.

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

### REST

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

بدءًا من Gemini 3.6 Flash وGemini 3.5 Flash-Lite، تنطبق تغييرات واجهة برمجة التطبيقات التالية على هذه النماذج وجميع إصدارات نماذج Gemini المستقبلية.

- **إيقاف مَعلمات أخذ العيّنات نهائيًا**: تم إيقاف `temperature` و`top_p` و`top_k` نهائيًا. تتجاهل واجهة برمجة التطبيقات هذه المَعلمات وتعرض خطأً في عمليات إنشاء النماذج المستقبلية.
- **التحقّق من صحة الردود الجاهزة**: لم يعُد من الممكن ملء الردود الجاهزة مسبقًا. إذا كانت آخر محادثة غير فارغة في الطلب هي محادثة `model`، ستعرض واجهة برمجة التطبيقات الخطأ `400`.

في ما يلي توضيحات مفصّلة وعيّنات من الرموز البرمجية لكل تغيير في واجهة برمجة التطبيقات.

### 1. إيقاف مَعلمات أخذ العيّنات نهائيًا (`temperature` و`top_p` و`top_k`)

تم إيقاف `temperature` و`top_p` و`top_k` نهائيًا وسيتم تجاهلها. في الأجيال المستقبلية من النماذج، سيؤدي تقديم هذه المَعلمات إلى عرض الخطأ HTTP 400. **إزالة هذه المَعلمات من جميع الطلبات**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

لتحسين الحتمية، حدِّد تعليمات نظام تتضمّن قواعد واضحة لحالة الاستخدام المحدّدة.

### 2. التحقّق من صحة الردود الجاهزة

يُحظر إرسال طلبات إلى واجهة برمجة التطبيقات تنتهي بدور نموذج غير فارغ، ويتم عرض **الخطأ HTTP 400**.

#### ⚠️ تجنَّب

في حمولات REST القديمة `generateContent` أو حمولات REST الأولية، لم يعُد مسموحًا أن تنتهي حمولة REST بدور النموذج
كما يلي:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ عملية نقل البيانات المُقترَحة (واجهة Interactions API)

في Interactions API، لا تتم تعبئة أدوار النموذج مسبقًا يدويًا. إذا كان تطبيقك يملأ نموذجًا مسبقًا لإخفاء المقدمات أو فرض تنسيق JSON، استخدِم system\_instruction أو [النتائج المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) بدلاً من ذلك.

```
# ✅ RECOMMENDED: Use system_instruction in the Interactions API to specify output format
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Translate 'Hello world' to Spanish.",
    system_instruction="Output only the translation without introductory text.",
)
```

## قائمة التحقّق الخاصة بعملية نقل البيانات

### Gemini 3.6 Flash

1. ثبِّت المهارة باتّباع الخطوات التالية:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. طبِّق المهارة باتّباع الخطوات التالية:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. ثبِّت المهارة باتّباع الخطوات التالية:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. طبِّق المهارة باتّباع الخطوات التالية:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### نقل البيانات إلى gemini-3.6-flash

- **تعديل رقم تعريف النموذج:** غيِّر سلسلة النموذج المستهدَف إلى `gemini-3.6-flash`.
- **إزالة مَعلمات أخذ العيّنات المتوقّفة نهائيًا:**
  - إزالة `temperature` و`top_p` و`top_k` من إعدادات الإنشاء
  - استبدِل `thinking_budget` بسلسلة التعداد `thinking_level` التي تم ضبطها على `"medium"` أو `"high"`.
  - إزالة `candidate_count` (غير متوافق مع الإصدار 3.x من Gemini)
- **فرض قواعد التحقّق من صحة الأرقام:**
  - توحيد المحادثات المترابطة على `previous_interaction_id` من جهة الخادم
  - إزالة الردود النموذجية المُعبّأة مسبقًا
- **تدقيق استدعاء الدوال:**
  - ضَع مواد العرض المتعدّدة الوسائط داخل حمولة الردّ.
  - يمكنك تنسيق التعليمات المضمّنة باستخدام `\n\n`.
  - إذا ظهرت لك أخطاء `Malformed_Function_Call` مرتبطة بنص ما قبل الأداة، اطّلِع على [حلول بديلة لمتطلبات نص ما قبل الأداة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#workarounds-for-pre-tool-text-requirements).
  - في حال استخدام generateContent API فقط: تأكَّد من أنّ جميع عناصر `FunctionResponse` تتضمّن `call_id` و`name`.
- **متطلبات Baseline Gemini 3.x:** للاطّلاع على تحديثات حزمة تطوير البرامج (SDK) والحفاظ على توقيع الفكرة، يُرجى الرجوع إلى [قائمة التحقّق من عملية نقل البيانات إلى Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=ar#migration).

### نقل البيانات إلى gemini-3.5-flash-lite

- **تعديل رقم تعريف النموذج:** غيِّر سلسلة النموذج المستهدَف إلى `gemini-3.5-flash-lite`.
- **ضبط مستوى الجهد الذهني:**
  - بالنسبة إلى عمليات الاستخراج أو التوجيه أو التصنيف الكبيرة الحجم، اترُك القيمة `thinking_level` على `"minimal"` (الإعداد التلقائي) لتحقيق الحد الأقصى من معدل النقل.
  - بالنسبة إلى الوكلاء الفرعيين المستقلين الذين يستخدمون طلبات الأدوات أو تطبيق الرموز البرمجية أو الاستدلال المتعدّد الخطوات، اضبط قيمة `thinking_level` على `"medium"` أو `"high"` لمنع إنهاء الأداة قبل الأوان.
- **إزالة المَعلمات المتوقّفة نهائيًا والتحقّق من صحة استدعاء الدوال:** طبِّق [القواعد نفسها المتّبعة في الإصدار 3.6 من Flash](#migrate-to-gemini-3-6-flash).
- **متطلبات الإصدار الأساسي من Gemini 3.x:** يُرجى الرجوع إلى [قائمة التحقّق من نقل البيانات إلى Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=ar#migration).

## الخطوات التالية

- راجِع مواصفات واجهة برمجة التطبيقات في [نظرة عامة على النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).
- استكشِف عملية التنسيق بين عدة وكلاء في [دليل Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar).
- اختبار الطلبات وتحسينها في [Google AI Studio](https://aistudio.google.com/?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-23 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-23 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
