---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ar
fetched_at: 2026-05-05T13:11:08.303545+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/Deep Research من Gemini) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

- [الصفحة الرئيسية](https://ai.google.dev/gemini-api/docs/الصفحة الرئيسية)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)

# تسريع الاكتشاف باستخدام Gemini for Research

[الحصول على مفتاح Gemini API](https://ai.google.dev/gemini-api/docs/الحصول على مفتاح Gemini API)

يمكن استخدام نماذج Gemini لتعزيز الأبحاث الأساسية في مختلف المجالات.
في ما يلي طرق لاستكشاف Gemini لأغراض بحثك:

- **تحليل نواتج النموذج والتحكّم بها**: لمزيد من التحليل، يمكنك فحص
  ردّ مقترَح أنشأه النموذج باستخدام أدوات مثل
  `CitationMetadata`. يمكنك أيضًا ضبط خيارات إنشاء النموذج ونواتجه، مثل `responseSchema` و`topP` و`topK`. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/مزيد من المعلومات).
- **الإدخالات المتعدّدة الوسائط**: يمكن لـ Gemini معالجة الصور والمقاطع الصوتية والفيديوهات، ما يتيح إجراء مجموعة كبيرة من الأبحاث المثيرة. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/مزيد من المعلومات).
- **إمكانات السياق الطويل**: يتضمّن Gemini 3.0 Flash وPro قدرة استيعاب تبلغ مليون رمز مميّز. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/مزيد من المعلومات).
- **Grow with Google**: يمكنك الوصول بسرعة إلى نماذج Gemini من خلال واجهة برمجة التطبيقات وGoogle AI
  Studio لحالات الاستخدام في مرحلة الإنتاج. إذا كنت تبحث عن منصة مستندة إلى Google Cloud، يمكن أن توفّر منصة Gemini Enterprise Agent بنية أساسية إضافية داعمة.

لدعم الأبحاث الأكاديمية وتعزيز الأبحاث المتطورة، تتيح Google
للعلماء والباحثين الأكاديميين الوصول إلى أرصدة Gemini API من خلال
[برنامج Gemini Academic Program](https://ai.google.dev/gemini-api/docs/برنامج Gemini Academic Program).

## بدء استخدام Gemini

تساعدك Gemini API وGoogle AI Studio في البدء في استخدام أحدث نماذج Google وتحويل أفكارك إلى تطبيقات قابلة للتوسّع.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

"يبحث مشروعنا في Gemini كنموذج لغة مرئية (VLM) وسلوكياته المستندة إلى الذكاء الاصطناعي الوكيل في بيئات متنوعة من منظورَي المتانة والأمان. لقد قيّمنا حتى الآن متانة Gemini في مواجهة عوامل التشتيت، مثل النوافذ المنبثقة عندما تنفّذ وكلاء VLM مهام على الكمبيوتر، واستخدمنا Gemini لتحليل التفاعل الاجتماعي والأحداث المؤقتة وعوامل الخطر استنادًا إلى إدخالات الفيديو".

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=ar)

يساعدنا Gemini Pro وFlash، بفضل قدرة استيعابها الطويلة، في OK-Robot، وهو مشروعنا الخاص بالتلاعب بالأشياء على الأجهزة الجوّالة باستخدام مفردات مفتوحة. يتيح Gemini إجراء طلبات وأوامر معقّدة باللغة الطبيعية على "ذاكرة" الروبوت، وفي هذه الحالة، الملاحظات السابقة التي سجّلها الروبوت خلال فترة تشغيل طويلة. أنا وMahi Shafiullah نستخدم أيضًا Gemini لتقسيم المهام إلى تعليمات برمجية يمكن للروبوت تنفيذها في العالم الحقيقي".

## برنامج Gemini Academic Program

يمكن للباحثين الأكاديميين المؤهّلين (مثل أعضاء هيئة التدريس والموظفين وطلاب الدكتوراه) في [البلدان
المتاحة](https://ai.google.dev/gemini-api/docs/البلدانالمتاحة) التقديم للحصول على أرصدة Gemini API
وحدود أعلى للطلبات في مشاريعهم البحثية. يسمح هذا الدعم بزيادة سرعة معالجة البيانات في التجارب العلمية وتعزيز الأبحاث.

نحن مهتمون بشكل خاص بمجالات البحث الواردة في القسم التالي، ولكننا نرحّب بالطلبات من مختلف التخصّصات العلمية:

- **التقييمات والمقاييس**: طُرق التقييم التي تحظى بموافقة المنتدى والتي
  يمكن أن توفّر إشارة أداء قوية في مجالات مثل الدقة والسلامة و
  اتّباع التعليمات والتحليل والتخطيط.
- **تسريع الاكتشاف العلمي لصالح البشرية**: التطبيقات المحتمَلة للذكاء الاصطناعي في الأبحاث العلمية المتعدّدة التخصّصات، بما في ذلك مجالات مثل الأمراض النادرة والمهملة وعلم الأحياء التجريبي وعلم المواد والاستدامة.
- **التجسيد والتفاعلات**: استخدام النماذج اللغوية الكبيرة للبحث عن تفاعلات جديدة في مجالات الذكاء الاصطناعي المجسّد والتفاعلات المحيطة والروبوتات والتفاعل بين الإنسان والكمبيوتر.
- **الإمكانات الناشئة**: استكشاف الإمكانات الجديدة المستندة إلى الذكاء الاصطناعي الوكيل اللازمة لتعزيز الاستدلال والتخطيط، وكيفية توسيع الإمكانات أثناء الاستنتاج (على سبيل المثال، باستخدام Gemini Flash).
- **التفاعل والفهم المتعدّد الوسائط**: تحديد الثغرات و
  الفرص المتاحة للنماذج الأساسية المتعدّدة الوسائط لأغراض التحليل والتحليل و
  التخطيط في مجموعة متنوعة من المهام.

الأهلية: يمكن فقط للأفراد (أعضاء هيئة التدريس أو الباحثين أو ما يعادلهم) التابعين لمؤسسة أكاديمية أو مؤسسة بحث أكاديمي صالحة التقديم. يُرجى العِلم أنّ Google ستمنح أرصدة الوصول إلى واجهة برمجة التطبيقات وتزيلها وفقًا لتقديرها الخاص. نراجع الطلبات شهريًا.

### بدء البحث باستخدام Gemini API

[تقديم طلب الآن](https://ai.google.dev/gemini-api/docs/تقديم طلب الآن)

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://ai.google.dev/gemini-api/docs/ترخيص Creative Commons Attribution 4.0‏) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://ai.google.dev/gemini-api/docs/ترخيص Apache 2.0‏). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://ai.google.dev/gemini-api/docs/سياسات موقع Google Developers‏). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)
