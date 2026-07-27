---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ar
fetched_at: 2026-07-27T04:49:32.492873+00:00
title: "\u062a\u0633\u0631\u064a\u0639 \u0639\u0645\u0644\u064a\u0629 \u0627\u0644\u0627\u0643\u062a\u0634\u0627\u0641 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini \u0644\u0623\u063a\u0631\u0627\u0636 \u0627\u0644\u0628\u062d\u062b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)

# تسريع عملية الاكتشاف باستخدام Gemini لأغراض البحث

[الحصول على مفتاح Gemini API](https://aistudio.google.com/apikey?hl=ar)

يمكن استخدام نماذج Gemini لتطوير الأبحاث الأساسية في مختلف المجالات.
في ما يلي طرق لاستكشاف Gemini لأغراض بحثك:

- **تحليل نواتج النموذج والتحكّم بها**: لمزيد من التحليل، يمكنك فحص
  ردّ مقترَح أنشأه النموذج باستخدام أدوات مثل
  `CitationMetadata`. يمكنك أيضًا ضبط خيارات إنشاء النموذج ونواتجه، مثل `responseSchema` و`topP` و`topK`. [مزيد من المعلومات](https://ai.google.dev/api/generate-content?hl=ar).
- **الإدخالات المتعدّدة الوسائط**: يمكن لـ Gemini معالجة الصور والمحتوى الصوتي والفيديوهات، ما يتيح العديد من الاتجاهات البحثية المثيرة. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/vision?hl=ar).
- **إمكانات السياق الطويل**: يأتي Gemini 3.0 Flash وGemini Pro مزوَّدين بقدرة استيعاب مليون رمز مميّز. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/long-context?hl=ar).
- **Grow with Google**: يمكنك الوصول بسرعة إلى نماذج Gemini من خلال واجهة برمجة التطبيقات وGoogle AI
  Studio لحالات الاستخدام في مرحلة الإنتاج. إذا كنت تبحث عن منصة مستندة إلى Google Cloud، يمكن أن توفّر منصة وكيل Gemini Enterprise بنية أساسية إضافية داعمة.

لدعم الأبحاث الأكاديمية وتعزيز الأبحاث المتطورة، تتيح Google
للعلماء والباحثين الأكاديميين الوصول إلى أرصدة Gemini API من خلال
[برنامج Gemini الأكاديمي](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ar#gemini-academic-program).

## بدء استخدام Gemini

تساعدك Gemini API وGoogle AI Studio في البدء في استخدام أحدث نماذج Google وتحويل أفكارك إلى تطبيقات قابلة للتوسّع.

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

### راحة

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

## أكاديميون مميّزون

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=ar)

"يبحث بحثنا في Gemini كنموذج لغوي مرئي (VLM) وسلوكياته كوكيل في بيئات متنوعة من منظورَي المتانة والأمان. لقد قيّمنا حتى الآن متانة Gemini في مواجهة عوامل التشتيت، مثل النوافذ المنبثقة عندما تنفّذ وكلاء VLM مهام على الكمبيوتر، واستخدمنا Gemini لتحليل التفاعل الاجتماعي والأحداث المؤقتة وعوامل الخطر استنادًا إلى إدخالات الفيديو".

[موقع Diyi Yang الإلكتروني](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=ar)

"يساعدنا Gemini Pro وGemini Flash، بقدرتهما على استيعاب معلومات كثيرة، في مشروع OK-Robot، وهو مشروعنا الخاص بمعالجة الأجهزة الجوّالة باستخدام مفردات مفتوحة. يتيح Gemini إجراء طلبات وأوامر معقّدة باللغة الطبيعية على "ذاكرة" الروبوت، وفي هذه الحالة، الملاحظات السابقة التي سجّلها الروبوت خلال فترة تشغيل طويلة. أنا وMahi Shafiullah نستخدم أيضًا Gemini لتقسيم المهام إلى تعليمات برمجية يمكن للروبوت تنفيذها في العالم الحقيقي".

[موقع Lerrel Pinto الإلكتروني](https://www.lerrelpinto.com/)

## برنامج Gemini الأكاديمي

يمكن للباحثين الأكاديميين المؤهّلين (مثل أعضاء هيئة التدريس والموظفين وطلاب الدكتوراه) في [البلدان
المؤهّلة](https://ai.google.dev/gemini-api/docs/available-regions?hl=ar) التقديم للحصول على أرصدة Gemini API
وحدود أعلى لمعدّل الاستخدام لمشاريعهم البحثية. يتيح هذا الدعم إنتاجية أعلى للتجارب العلمية ويعزّز الأبحاث.

نحن مهتمون بشكل خاص بمجالات البحث الواردة في القسم التالي، ولكننا نرحّب بالطلبات من مختلف التخصّصات العلمية:

- **التقييمات والمقاييس**: طرق التقييم التي تحظى بموافقة المنتدى والتي
  يمكن أن توفّر إشارة أداء قوية في مجالات مثل الدقة والسلامة و
  اتّباع التعليمات والتحليل والتخطيط.
- **تسريع الاكتشاف العلمي لصالح البشرية**: التطبيقات المحتمَلة للذكاء الاصطناعي في الأبحاث العلمية المتعدّدة التخصّصات، بما في ذلك مجالات مثل الأمراض النادرة والمهملة وعلم الأحياء التجريبي وعلم المواد والاستدامة.
- **التجسيد والتفاعلات**: استخدام النماذج اللغوية الكبيرة للبحث عن تفاعلات جديدة في مجالات الذكاء الاصطناعي المجسّد والتفاعلات المحيطة والروبوتات والتفاعل بين الإنسان والكمبيوتر.
- **الإمكانات الناشئة**: استكشاف إمكانات جديدة للوكيل مطلوبة لـ
  تعزيز التحليل والتخطيط، وكيفية توسيع الإمكانات أثناء
  الاستدلال (على سبيل المثال، باستخدام Gemini Flash).
- **التفاعل والفهم المتعدّد الوسائط**: تحديد الثغرات و
  الفرص المتاحة للنماذج الأساسية المتعدّدة الوسائط للتحليل والتحليل و
  التخطيط في مجموعة متنوعة من المهام.

الأهلية: يمكن فقط للأفراد (أعضاء هيئة التدريس أو الباحثين أو ما يعادلهم) التابعين لمؤسسة أكاديمية صالحة أو مؤسسة بحث أكاديمي التقديم. يُرجى العِلم أنّ Google ستمنح أرصدة الوصول إلى واجهة برمجة التطبيقات وتزيلها وفقًا لتقديرها الخاص. نراجع الطلبات شهريًا.

### بدء البحث باستخدام Gemini API

[تقديم طلب الآن](https://forms.gle/HMviQstU8PxC5iCt5)

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-01 (حسب التوقيت العالمي المتفَّق عليه)

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-01 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
