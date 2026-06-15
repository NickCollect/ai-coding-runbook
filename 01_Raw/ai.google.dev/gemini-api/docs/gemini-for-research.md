---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ar
fetched_at: 2026-06-15T06:29:43.569905+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)

# تسريع عملية الاكتشاف باستخدام "Gemini في البحث"

[الحصول على مفتاح Gemini API](https://aistudio.google.com/apikey?hl=ar)

يمكن استخدام نماذج Gemini لتطوير الأبحاث الأساسية في مختلف المجالات.
في ما يلي بعض الطرق التي يمكنك من خلالها استكشاف Gemini لإجراء بحثك:

- **تحليل نواتج النموذج والتحكّم فيها**: لإجراء المزيد من التحليلات، يمكنك فحص الردود المقترَحة التي أنشأها النموذج باستخدام أدوات مثل `CitationMetadata`. يمكنك أيضًا ضبط خيارات لإنشاء النماذج والمخرجات، مثل `responseSchema` و`topP` و`topK`. [مزيد من المعلومات](https://ai.google.dev/api/generate-content?hl=ar)
- **المدخلات المتعددة الوسائط**: يمكن لـ Gemini معالجة الصور والمقاطع الصوتية والفيديوهات، ما يتيح مجموعة كبيرة من طرق البحث الشيّقة. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/vision?hl=ar)
- **القدرة على استيعاب معلومات كثيرة**: يتضمّن كل من Gemini 3.0 Flash وPro قدرة استيعاب تصل إلى مليون رمز مميّز. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/long-context?hl=ar)
- **Grow with Google**: يمكنك الوصول بسرعة إلى نماذج Gemini من خلال واجهة برمجة التطبيقات وGoogle AI Studio لحالات الاستخدام في الإنتاج. إذا كنت تبحث عن منصة مستندة إلى Google Cloud، يمكن أن توفّر لك منصة Gemini Enterprise Agent Platform بنية أساسية إضافية داعمة.

لدعم الأبحاث الأكاديمية وتعزيز الأبحاث المتطوّرة، تتيح Google للعلماء والباحثين الأكاديميين إمكانية الوصول إلى أرصدة Gemini API من خلال [برنامج Gemini الأكاديمي](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ar#gemini-academic-program).

## بدء استخدام Gemini

تساعدك واجهة Gemini API وGoogle AI Studio في بدء العمل باستخدام أحدث نماذج Google وتحويل أفكارك إلى تطبيقات قابلة للتوسّع.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## الأكاديميون المميزون

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=ar)

"يبحث فريقنا في Gemini كنموذج لغة مرئية (VLM) وسلوكياته المستقلة في بيئات متنوعة من منظورَي المتانة والأمان. حتى الآن، قيّمنا مدى فعالية Gemini في التعامل مع عوامل التشتيت، مثل النوافذ المنبثقة، عندما تنفّذ برامج VLM مهام على الكمبيوتر، واستفدنا من Gemini في تحليل التفاعل الاجتماعي والأحداث الزمنية وعوامل الخطر استنادًا إلى إدخال الفيديو".

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=ar)

لقد ساعدنا Gemini Pro وFlash، بفضل نافذة السياق الطويلة الخاصة بهما، في مشروعنا OK-Robot، وهو مشروع مفتوح المصدر للتحكّم في الأجهزة الجوّالة. يتيح Gemini تنفيذ طلبات وأوامر معقّدة باللغة الطبيعية استنادًا إلى "ذاكرة" الروبوت، أي الملاحظات السابقة التي سجّلها الروبوت خلال مدة تشغيل طويلة. أنا و"ماهي شافي الله" نستخدم Gemini أيضًا لتقسيم المهام إلى رموز برمجية يمكن للروبوت تنفيذها في العالم الحقيقي".

## برنامج Gemini الأكاديمي

يمكن للباحثين الأكاديميين المؤهّلين (مثل أعضاء هيئة التدريس والموظفين وطلاب الدكتوراه) في [البلدان
المؤهّلة](https://ai.google.dev/gemini-api/docs/available-regions?hl=ar) تقديم طلب للحصول على رصيد في Gemini API وحدود استخدام أعلى لمشاريعهم البحثية. يتيح هذا الدعم إنتاجية أعلى للتجارب العلمية ويساهم في تطوير الأبحاث.

نحن مهتمون بشكل خاص بمجالات البحث الواردة في القسم التالي،
ولكن نرحّب بطلبات المشاركة من مختلف التخصصات العلمية:

- **التقييمات والمقاييس**: طُرق تقييم يوافق عليها المنتدى ويمكن أن تقدّم إشارة أداء قوية في مجالات مثل الدقة والسلامة واتّباع التعليمات والاستدلال والتخطيط.
- **تسريع الاكتشافات العلمية بما يعود بالنفع على البشرية**: التطبيقات المحتملة للذكاء الاصطناعي في الأبحاث العلمية المتعددة التخصصات، بما في ذلك مجالات مثل الأمراض النادرة والمهملة، وعلم الأحياء التجريبي، وعلم المواد، والاستدامة
- **التجسيد والتفاعلات**: استخدام النماذج اللغوية الكبيرة لاستكشاف تفاعلات جديدة في مجالات الذكاء الاصطناعي المجسَّد والتفاعلات المحيطة والروبوتات والتفاعل بين الإنسان والحاسوب
- **الإمكانات الناشئة**: استكشاف إمكانات جديدة تتطلّبها إمكانات بالذكاء الاصطناعي الوكيل لتحسين الاستدلال والتخطيط، وكيفية توسيع نطاق الإمكانات أثناء الاستنتاج (مثل استخدام Gemini Flash).
- **التفاعل والفهم المتعدّد الوسائط**: تحديد الثغرات والفرص في النماذج الأساسية المتعدّدة الوسائط لإجراء التحليلات والاستدلال والتخطيط في مجموعة متنوعة من المهام

الأهلية: يمكن فقط للأفراد (أعضاء هيئة التدريس أو الباحثين أو ما يعادلهم) التابعين لمؤسسة أكاديمية صالحة أو مؤسسة بحثية أكاديمية تقديم طلب. يُرجى العِلم أنّه سيتم منح إذن الوصول إلى واجهة برمجة التطبيقات والائتمانات وإزالتها وفقًا لتقدير Google. نراجع الطلبات شهريًا.

### بدء البحث باستخدام Gemini API

[تقديم طلب الآن](https://forms.gle/HMviQstU8PxC5iCt5)

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
