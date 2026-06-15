---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=ar
fetched_at: 2026-06-15T06:25:15.893901+00:00
title: "\u0645\u0644\u0627\u062d\u0638\u0627\u062a \u062d\u0648\u0644 \u0627\u0644\u0625\u0635\u062f\u0627\u0631 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# ملاحظات حول الإصدار

تتضمّن هذه الصفحة معلومات حول آخر التعديلات التي تم إجراؤها على Gemini API.

## ‫1 يونيو 2026

- تم الآن [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) نماذج Gemini 2.0 التالية:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  يُرجى استخدام [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) أو
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar)
  بدلاً من ذلك.

## ‫28 مايو 2026

- أطلقنا الإصدارين `gemini-3.1-flash-image` (Nano Banana 2) و`gemini-3-pro-image`
  (Nano Banana Pro) المتاحَين للجميع من نماذجنا المرئية الأصلية، وهما [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=ar)
  و[Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=ar).
- **إتاحة إنشاء صور من فيديوهات**: يمكنك الآن تمرير ملف فيديو (عبر التحميل المباشر أو كعنوان URL علني على YouTube) كسياق متعدد الوسائط إلى جانب طلب نصي لإنشاء صور مصغّرة عالية الجودة أو ملصقات سينمائية للأفلام أو رسومات بيانية تلخيصية. تتوفّر هذه الميزة حصريًا على طراز `gemini-3.1-flash-image`. لمزيد من المعلومات، يُرجى الاطّلاع على دليل
  [إنشاء صور من فيديوهات](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#video-to-image).
- إشعار بإيقاف نهائي: تم إيقاف النموذجين `gemini-3.1-flash-image-preview` و`gemini-3-pro-image-preview` نهائيًا، وسيتم [إيقافهما](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) في 25 يونيو 2026.

## ‫25 مايو 2026

- تم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) نموذج `gemini-3.1-flash-lite-preview`. استخدِم
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) بدلاً من ذلك.

## ‫19 مايو 2026

- أصدرنا `gemini-3.5-flash`، الإصدار المتاح للجميع من
  [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar)،
  وهو نموذجنا الأكثر تطورًا لتحقيق أداء متقدّم ومستمر في
  مهام الترميز والمهام التي تتطلب استخدام وكلاء.
- تم إطلاق **الوكلاء المُدارون في Gemini API** في إصدار مبكر متاح للجميع. يتيح ذلك للمطوّرين إنشاء وكلاء مستقلين ومحتفظين بالحالة وتفعيلهم في بيئات معزولة وآمنة على Linux تستضيفها Google. لمزيد من المعلومات، يُرجى الاطّلاع على صفحة [نظرة عامة حول العملاء](https://ai.google.dev/gemini-api/docs/agents?hl=ar) و[دليل البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar).
- أصدرنا الوكيل المُدار **Antigravity Agent** للأغراض العامة،
  [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=ar)، في "الميزات التجريبية المتاحة للجميع".
  يمكن لوكيل Antigravity التخطيط بشكل مستقل، والتفكير، وكتابة الرموز البرمجية وتنفيذها، وإدارة الملفات، وتصفُّح الويب داخل حاوية وضع الحماية. راجِع دليل [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar) للاطّلاع على نماذج الرموز والمواصفات.

## ‫7 مايو 2026

- أصدرنا `gemini-3.1-flash-lite` النسخة المتوفّرة للجمهور العام من
  [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar)،
  المحسَّنة من أجل السرعة وقابلية التوسّع وفعالية التكلفة.
- إشعار بإيقاف نهائي: سيتم إيقاف النموذج `gemini-3.1-flash-lite-preview` نهائيًا في 11 مايو 2026، وسيتم [إيقافه](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) في 25 مايو 2026.

## ‫6 مايو 2026

- **تغيير غير متوافق قادم**: سيتم تغيير مخطط طلب واستجابة [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) (`outputs` → `steps`) وإعدادات تنسيق الإخراج (`response_format`). سيصبح المخطط الجديد هو المخطط التلقائي في **26 مايو**، وستتم إزالة المخطط القديم في **8 يونيو**.
  راجِع
  [دليل نقل البيانات](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ar)
  للاطّلاع على التفاصيل.

## ‫5 مايو 2026

- تم تعديل **البحث عن الملفات** ليتوافق مع البحث المتعدّد الوسائط. يمكنك الآن تضمين الصور والبحث فيها بشكل أصلي باستخدام نموذج `gemini-embedding-2`.
  تتضمّن البيانات الوصفية لتحديد المصدر الآن `media_id` للاقتباسات المرئية و`page_numbers` للإشارة إلى مكان العثور على المعلومات. لمزيد من المعلومات، يُرجى الاطّلاع على دليل [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar).

## ‫4 مايو 2026

- أطلقنا ميزة [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=ar) المستندة إلى الأحداث في Gemini API لاستبدال عمليات سير العمل التي تستخدم الاستقصاء في Batch API والعمليات الطويلة الأمد.

## ‫30 أبريل 2026

- تم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) نموذج `gemini-robotics-er-1.5-preview`. استخدِم
  [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=ar) بدلاً من ذلك.

## ‫22 أبريل 2026

- تم إصدار `gemini-embedding-2` كمنتج متوفّر للجمهور العام. لمزيد من المعلومات، يُرجى الاطّلاع على صفحة [التضمينات](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar).

## ‫21 أبريل 2026

- أصدرنا إصدارات جديدة من وكيل [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar)
  تتضمّن ميزات التخطيط التعاوني، ودعم العرض المرئي، ودمج خادم MCP، والبحث عن الملفات:

  - ‫[`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=ar): تم تصميمه ليكون سريعًا وفعّالاً، وهو مثالي للبث إلى واجهة مستخدم العميل.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=ar): الحد الأقصى
    للشمولية في جمع السياق وتلخيصه بشكل آلي.

## ‫15 أبريل 2026

- أطلقنا [الإصدار التجريبي من نموذج تحويل النص إلى كلام Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ar)، وهو نموذج فعّال من حيث التكلفة، ومعبّر، ويمكن التحكّم فيه. يمكنك الاطّلاع على مستندات [تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar) لمعرفة المزيد.

## ‫14 أبريل 2026

- تم إطلاق `gemini-robotics-er-1.6-preview`، وهو نموذج الروبوتات المعدَّل.
  يتضمّن الآن إمكانات جديدة، مثل قراءة الآلات الموسيقية، وإمكانات محسّنة للاستدلال المكاني والمادي. لمزيد من المعلومات، يُرجى الاطّلاع على صفحة [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ar) و[المدوّنة](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=ar).
- إشعار بإيقاف نهائي: سيتم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) نموذج `gemini-robotics-er-1.5-preview` نهائيًا في 30 أبريل 2026 الساعة 9 صباحًا بتوقيت المحيط الهادئ.

## ‫2 أبريل 2026

- تم إطلاق `gemma-4-26b-a4b-it` و`gemma-4-31b-it`، وهما متوفّران على [AI Studio](https://aistudio.google.com?hl=ar) ومن خلال Gemini API،
  كجزء من إطلاق [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=ar).

## ‫1 أبريل 2026

- أضفنا فئتَي الاستدلال الجديدتَين [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar) و[Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)، ما يوفّر المزيد من الخيارات
  لتحسين التكلفة أو وقت الاستجابة.

## ‫31 مارس 2026

- أطلقنا الإصدار التجريبي من Veo 3.1 Lite، [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=ar)، وهو نموذج [لإنشاء الفيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar) الأكثر فعالية من حيث التكلفة، والمصمّم لتكرار العمليات بسرعة وإنشاء تطبيقات ذات حجم كبير.
- تم إيقاف نموذج `gemini-2.5-flash-lite-preview-09-2025`. استخدِم
  [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ar) بدلاً من ذلك.

## ‫26 مارس 2026

- تم إطلاق [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ar)، وهو أحدث نموذج لتحويل الصوت إلى صوت (A2A) مصمّم للحوار في الوقت الفعلي وتطبيقات الذكاء الاصطناعي التي تعتمد على الصوت. يمكنك الاطّلاع على مستندات [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ar) للبدء.

## ‫25 مارس 2026

- أطلقنا نموذجين لإنشاء الموسيقى [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar): [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=ar)
  (مقاطع مدتها 30 ثانية) و[`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=ar)
  (أغانٍ كاملة). يقبل كلا النموذجين إدخالات نصية وصورًا وينشئان محتوًى صوتيًا عالي الجودة بدقة 48 كيلو هرتز. اطّلِع على دليل [إنشاء الموسيقى](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar) للحصول على التفاصيل وأمثلة على الرموز البرمجية.

## ‫23 مارس 2026

- طرح [خطط الفوترة للدفع المسبق والدفع الآجل](https://ai.google.dev/gemini-api/docs/billing?hl=ar) في AI Studio قد تتأثر الحسابات الحالية، لذا يُرجى قراءة مستندات [الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar) للحصول على مزيد من المعلومات.

## ‫18 مارس 2026

- أطلقنا ميزة [الجمع بين الأدوات المضمّنة واستدعاء الدوال](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar) الجديدة التي تتيح استخدام أدوات Gemini المضمّنة إلى جانب أدوات استدعاء الدوال المخصّصة في طلب بيانات من واجهة برمجة التطبيقات واحد.
- أصبحت ميزة [استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar#supported_models) متاحة الآن لنماذج Gemini 3.

## ‫16 مارس 2026

- تم طرح [فئات الاستخدام](https://ai.google.dev/gemini-api/docs/billing?hl=ar#about-billing) و[حدود الإنفاق في حساب الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar#tier-spend-caps) المحسّنة
  لتقديم تجربة أفضل للمستخدمين في ما يتعلّق بالفوترة.

## ‫12 مارس 2026

- أضفنا [حدود الإنفاق على مستوى المشروع](https://ai.google.dev/gemini-api/docs/billing?hl=ar#project-spend-caps) إلى الفوترة في AI Studio.

## ‫10 مارس 2026

- أطلقنا `gemini-embedding-2-preview`، وهو أول نموذج تضمين متعدد الوسائط.
  يتوافق هذا النموذج مع النصوص والصور والفيديوهات والمحتوى الصوتي وملفات PDF،
  ويعمل على ربط جميع أنواع المحتوى بمساحة تضمين موحّدة. لمزيد من المعلومات، اطّلِع على مقالة [عمليات التضمين](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar).
- إشعار بالإيقاف النهائي: سيتم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) نموذج `gemini-2.5-flash-lite-preview-09-2025` نهائيًا في 31 مارس 2026.

## ‫9 مارس 2026

- تم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) نموذج Gemini 3 Pro Preview. يشير `gemini-3-pro-preview` الآن إلى
  [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar).

## ‫3 مارس 2026

- أطلقنا الإصدار الحصري من Gemini 3.1 Flash-Lite، وهو أول نموذج Flash-Lite في سلسلة Gemini 3. يمكنك الاطّلاع على [صفحة الطراز](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ar) لمعرفة المواصفات والتحديثات المحدّدة وإرشادات المطوّرين.

## ‫26 فبراير 2026

- أطلقنا Nano Banana 2، وهو [إصدار تجريبي من Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=ar)، وهو نموذج عالي الكفاءة ومحسَّن للاستخدام السريع وفي حالات الاستخدام التي تتطلّب معالجة كميات كبيرة من البيانات.
- إشعار بإيقاف الإصدار التجريبي من Gemini 3 Pro (`gemini-3-pro-preview`)
  [نهائيًا](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) في 9 مارس 2026

## ‫19 فبراير 2026

- أطلقنا [إصدارًا تجريبيًا من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar)، وهو أحدث إصدار في سلسلة Gemini 3 الجديدة.
- أطلقنا نقطة نهاية منفصلة `gemini-3.1-pro-preview-customtools`، وهي أفضل في تحديد أولويات الأدوات المخصّصة، للمستخدمين الذين ينشئون باستخدام مزيج من bash والأدوات.

## ‫18 فبراير 2026

- إشعار بإيقاف نهائي: سيتم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) النماذج التالية نهائيًا في 1 يونيو 2026:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## ‫17 فبراير 2026

- تم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) النماذج التالية:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## ‫4 يناير 2026

- أطلقنا ميزة "استخدام الكمبيوتر" في `gemini-3-pro-preview` و`gemini-3-flash-preview`.

## ‫21 يناير 2026

- تم تغيير الأسماء المستعارة لـ `latest`:

  - تم التبديل إلى `gemini-pro-latest``gemini-3-pro-preview`
  - تم التبديل إلى `gemini-flash-latest``gemini-3-flash-preview`

## ‫15 يناير 2026

- إشعار بإيقاف نهائي: سيتم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) النماذج التالية نهائيًا في 17 فبراير 2026:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- تم إيقاف نموذج `gemini-2.5-flash-image-preview`.

## ‫14 يناير 2026

- تم [إيقاف](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) نموذج `text-embedding-004`.

## ‫13 يناير 2026

- تمت إضافة درجات دقة 4K لإنشاء الفيديوهات في [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar)، كما أصبح بإمكانك إنشاء فيديوهات بالوضع العمودي بجميع درجات الدقة.

## ‫12 يناير 2026

- تم إطلاق ميزة مراحل نشاط النموذج. ستحدّد بعض النماذج الآن مرحلة دورة الحياة والجدول الزمني لإيقافها نهائيًا. يُرجى الاطّلاع على المستندات التالية لمزيد من المعلومات:

  - [مراحل النموذج](https://ai.google.dev/api/generate-content?hl=ar#ModelStatus)

## ‫8 يناير 2026

- أتحنا إمكانية استخدام حِزم Cloud Storage وأي عناوين URL عامة وخاصة موقّعة مسبقًا لقواعد البيانات كمصدر لإدخال البيانات في Gemini API. تمت أيضًا زيادة الحد الأقصى لحجم الملف من 20 ميغابايت إلى 100 ميغابايت. لمزيد من التفاصيل، يُرجى الاطّلاع على [دليل
  طرق إدخال الملفات](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar).

## ‫19 ديسمبر 2025

- تم إجراء تغيير غير متوافق مع الإصدارات السابقة على المعاينة العامة لواجهة Interactions API في الإصدار التجريبي 1. تمت إعادة تسمية الحقل `total_reasoning_tokens` ليصبح `total_thought_tokens` بهدف التوافق بشكل أفضل مع مفهوم "الأفكار" في النماذج المفكّرة.

## ‫17 ديسمبر 2025

- أطلقنا الإصدار الحصري من Gemini 3 Flash، `gemini-3-flash-preview`، الذي يقدّم أداءً سريعًا
  بمستوى متطوّر ينافس النماذج الأكبر حجمًا وبتكلفة أقل. مع إمكانات محسّنة للاستدلال المرئي والمكاني والترميز بالذكاء الاصطناعي الوكيل يمكنك الاطّلاع على المستندات حول بعض الميزات الجديدة، بما في ذلك:

  - [الردود المتعدّدة الوسائط من الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#multimodal)
  - [تنفيذ الرموز البرمجية باستخدام الصور](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar#images)

## ‫12 ديسمبر 2025

- تم إصدار `gemini-2.5-flash-native-audio-preview-12-2025`،
  وهو نموذج صوتي جديد مدمج في Live API. يحسّن هذا التحديث قدرة النموذج على التعامل مع مهام سير العمل المعقّدة. لمزيد من المعلومات، يُرجى الاطّلاع على
  [دليل Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar) و[الاستماع إلى الصوت الأصلي في Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=ar).

## ‫11 ديسمبر 2025

- تم إطلاق الإصدار التجريبي من Interactions API. توفر واجهة برمجة التطبيقات هذه واجهة موحّدة للتفاعل مع نماذج Gemini ووكلاء Gemini. لمزيد من المعلومات، يُرجى الاطّلاع على دليل [واجهة برمجة التطبيقات للتفاعلات](https://ai.google.dev/gemini-api/docs/interactions?hl=ar).
- أطلقنا ميزة "وكيل Deep Research" في Gemini في إصدار تجريبي. يمكنها
  تخطيط وتنفيذ وتجميع نتائج مهام البحث المتعدّدة الخطوات بشكل مستقل. يمكنك الاطّلاع على التفاصيل في دليل [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar).

## ‫10 ديسمبر 2025

- أطلقنا تحسينات على [نماذج تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar)، وهي إصدار Gemini 2.5 Flash التجريبي من ميزة تحويل النص إلى كلام (المحسّن لتحقيق سرعة استجابة عالية) وإصدار Gemini 2.5 Pro التجريبي من ميزة تحويل النص إلى كلام (المحسّن لتحقيق جودة عالية)، بما في ذلك تعزيز التعبيرية، وتحديد السرعة بدقة، وإجراء حوار سلس.

## ‫9 ديسمبر 2025

- تم إيقاف نماذج Gemini Live API التالية:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## ‫5 ديسمبر 2025

- سيبدأ تحصيل فواتير Gemini 3 مقابل ميزة [تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) في 5 يناير 2026.

## ‫4 ديسمبر 2025

- إشعار بإيقاف نهائي: سيتم إيقاف نموذج `gemini-2.5-flash-image-preview` نهائيًا في 15 يناير 2026.

## ‫3 ديسمبر 2025

- إشعار بإيقاف نهائي: سيتم إيقاف النموذج `text-embedding-004` نهائيًا في 14 يناير 2026.

## ‫20 نوفمبر 2025

- أطلقنا Gemini 3 Pro Image Preview، وهو `gemini-3-pro-image-preview`، الجيل التالي من نموذج Nano Banana. اطّلِع على صفحة [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) لمزيد من التفاصيل.

## ‫18 نوفمبر 2025

- أطلقنا أول نموذج من سلسلة Gemini 3، وهو `gemini-3-pro-preview`، نموذجنا
  الأكثر تطورًا في الاستدلال وفهم المحتوى المتعدد الوسائط، والذي يتميّز بقدرات
  قوية في الترميز والعمل كوكيل.

  بالإضافة إلى التحسينات في الذكاء والأداء، يقدّم إصدار Gemini 3 Pro التجريبي سلوكًا جديدًا بشأن:

  - [دقّة الوسائط](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ar)
  - [التوقيعات الفكرية](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar)
  - [مستويات التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#thinking-levels)

  يمكنك الاطّلاع على [دليل المطوّرين الخاص بإصدار Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=ar) لمعرفة المزيد حول عملية نقل البيانات والميزات الجديدة والمواصفات.

## ‫11 نوفمبر ٢٠٢٥

- إشعار بإيقاف نهائي: سيتم إيقاف النماذج التالية نهائيًا:

  - ‫12 نوفمبر:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - ‫14 نوفمبر:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## ‫10 نوفمبر 2025

- تم إيقاف النموذج التالي:

  - `imagen-3.0-generate-002`

  يمكنك استخدام [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=ar#imagen-4) بدلاً من ذلك. يمكنك الرجوع إلى
  [جدول إيقاف Gemini نهائيًا](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar) للاطّلاع على مزيد من التفاصيل.

## ‫6 نوفمبر 2025

- أطلقنا واجهة برمجة التطبيقات File Search API في إصدار مبكر متاح للجميع، ما يتيح للمطوّرين الاستناد إلى بياناتهم الخاصة في الردود. يمكنك الانتقال إلى صفحة [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) الجديدة للاطّلاع على مزيد من المعلومات.

## ‫4 نوفمبر 2025

- بالنسبة إلى [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)، تم خفض عدد الرموز المميزة للإدخال الخاصة بالصور من 1,290 إلى 258، ما أدّى إلى خفض تكلفة تعديل الصور.
- إشعار بإيقاف نهائي: سيتم إيقاف النماذج التالية نهائيًا:

  - ‫18 نوفمبر:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - ‫2 ديسمبر:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - ‫9 ديسمبر:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## ‫29 أكتوبر 2025

- أطلقنا أداة [تسجيل البيانات ومجموعات البيانات](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ar) الجديدة
  لـ Gemini API.

## ‫20 أكتوبر 2025

- تم إيقاف نماذج Gemini Live API التالية نهائيًا:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  يمكنك استخدام `gemini-2.5-flash-native-audio-preview-09-2025` بدلاً من ذلك.
- إشعار بإيقاف الخدمة نهائيًا: سيتم إيقاف `gemini-2.0-flash-live-001` و`gemini-live-2.5-flash-preview` نهائيًا في 9 ديسمبر 2025.

## ‫17 أكتوبر 2025

- أصبحت ميزة **استخدام "خرائط Google" كمصدر** متاحة للجميع. لمزيد من المعلومات، يُرجى الاطّلاع على مستندات [استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar).

## ‫15 أكتوبر 2025

- أطلقنا [النموذجَين Veo 3.1 و3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=ar#veo-3.1) في نسخة حصرية متاحة للجميع، مع ميزات جديدة، بما في ذلك:

  - إطالة مدة الفيديوهات التي تم إنشاؤها بواسطة Veo
  - الاستناد إلى ما يصل إلى ثلاث صور لإنشاء فيديو
  - توفير صور الإطار الأول والأخير لإنشاء فيديوهات منها

  أتاحت هذه الميزة أيضًا خيارات إضافية لمدد فيديوهات Veo 3 الناتجة: 4 و6 و8 ثوانٍ.
- إشعار بإيقاف الخدمة نهائيًا: سيتم إيقاف `veo-3.0-generate-preview` و`veo-3.0-fast-generate-preview` نهائيًا في 12 نوفمبر 2025.

## ‫7 أكتوبر 2025

- أطلقنا [النسخة الحصرية من Gemini 2.5 لاستخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar)

## ‫2 أكتوبر 2025

- إطلاق الإصدار العام من Gemini 2.5 Flash Image: [إنشاء الصور باستخدام Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)

## ‫29 سبتمبر 2025

- تم إيقاف نماذج Gemini 1.5 التالية:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## ‫25 سبتمبر 2025

- أطلقنا نموذج Gemini Robotics-ER 1.5 في مرحلة المعاينة. يمكنك الاطّلاع على
  [نظرة عامة حول الروبوتات](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ar)
  للتعرّف على كيفية استخدام النموذج في تطبيق الروبوتات.
- تم إطلاق نماذج المعاينة التالية:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  لمزيد من التفاصيل، انتقِل إلى صفحة [النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

## ‫23 سبتمبر 2025

- تم إطلاق `gemini-2.5-flash-native-audio-preview-09-2025`،
  وهو نموذج صوتي جديد مدمج في واجهة Live API مع ميزة محسّنة لاستدعاء الدوال
  ومعالجة أفضل لعمليات قطع الكلام. لمزيد من المعلومات، يُرجى الاطّلاع على
  [دليل Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar) و[الاستماع إلى الصوت الأصلي في Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-native-audio).

## ‫16 سبتمبر 2025

- إشعار بإيقاف الخدمة: سيتم إيقاف النماذج التالية في أكتوبر 2025:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  راجِع صفحة [التضمينات](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar) للاطّلاع على تفاصيل حول أحدث نموذج للتضمينات.

## ‫10 سبتمبر 2025

- أتحنا استخدام
  [نموذج Embeddings في Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar#batch-embedding)،
  وأضفنا Batch API إلى
  [مكتبة التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar#batch) لتوفير طرق أسهل
  للبدء في استخدام طلبات البحث المجمّعة.

## ‫9 سبتمبر 2025

- أطلقنا الإصدار العام من Veo 3 وVeo 3 Fast، مع أسعار أقل وخيارات جديدة لنسب العرض إلى الارتفاع والدقة والتضمين. يمكنك الاطّلاع على [مستندات Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar#model-features) للحصول على مزيد من المعلومات.

## ‫26 أغسطس 2025

- أطلقنا [معاينة الصور في Gemini 2.5](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-image-preview)،
  أحدث نموذج أصلي لإنشاء الصور.

## ‫18 أغسطس 2025

- أطلقنا [أداة سياق عناوين URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) وأتحناها للجمهور العام، وهي أداة تتيح تقديم عناوين URL كسياق إضافي للطلبات. سيتم إيقاف إمكانية استخدام سياق عنوان URL مع نموذج `gemini-2.0-flash`
  (المتوفّر خلال الإصدار التجريبي) بعد أسبوع واحد.

## ‫14 أغسطس 2025

- أصدرنا نماذج Imagen 4 Ultra وStandard وFast كنسخ متوفّرة للجمهور العام. لمزيد من المعلومات، يُرجى الانتقال إلى صفحة [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ar).

## ‫7 أغسطس 2025

- أصبحت إعدادات `allow_adult` في ميزة "تحويل الصور إلى فيديوهات" متاحة الآن في المناطق المحظورة. يمكنك الاطّلاع على صفحة
  [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=ar#veo-model-parameters)
  للحصول على التفاصيل.

## ‫31 يوليو 2025

- أطلقنا ميزة تحويل الصور إلى فيديوهات في نموذج Veo 3 Preview.
- أصدرنا نموذج Veo 3 Fast Preview.
- لمزيد من المعلومات عن Veo 3، يُرجى الانتقال إلى صفحة [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar).

## ‫22 يوليو 2025

- أصدرنا `gemini-2.5-flash-lite`، وهو نموذج Gemini 2.5 السريع والمنخفض التكلفة والعالي الأداء. لمزيد من المعلومات، اطّلِع على [Gemini 2.5
  Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-lite).

## يوليو 17، ‏2025

- أطلقنا `veo-3.0-generate-preview`، وهو آخر تحديث لـ Veo يتيح إنشاء فيديوهات تتضمّن صوتًا. لمزيد من المعلومات عن Veo 3، يُرجى الانتقال إلى صفحة [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar).
- زيادة حدود المعدّل لكل من Imagen 4 Standard وUltra انتقِل إلى صفحة [الحدود القصوى لعدد الطلبات](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar) لمزيد من التفاصيل.

## ‫14 يوليو 2025

- أطلقنا `gemini-embedding-001`، وهو الإصدار الثابت من نموذج تضمين النصوص. لمزيد من المعلومات، يُرجى الاطّلاع على مقالة [عمليات التضمين](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar). `gemini-embedding-exp-03-07`
  سيتم إيقاف النموذج نهائيًا في 14 أغسطس 2025.

## ‫7 يوليو 2025

- تم إطلاق "وضع الدُفعات" في Gemini API. تجميع الطلبات وإرسالها للمعالجة بشكل غير متزامن لمزيد من المعلومات، اطّلِع على [وضع الدُفعات](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ar).

## ‫26 يونيو 2025

- يتم الآن إعادة توجيه النماذج التجريبية `gemini-2.5-pro-preview-05-06` و`gemini-2.5-pro-preview-03-25` إلى أحدث إصدار ثابت `gemini-2.5-pro`.
- تم إيقاف `gemini-2.5-pro-exp-03-25`.

## ‫24 يونيو 2025

- أطلقنا نماذج الإصدارات الحصرية من Imagen 4 Ultra وStandard. لمزيد من المعلومات، يمكنك الاطّلاع على صفحة [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar).

## ‫17 يونيو 2025

- أطلقنا `gemini-2.5-pro`، وهو الإصدار الثابت من نموذجنا الأكثر تطورًا، والذي يتضمّن الآن ميزة التفكير التكيّفي. لمزيد من المعلومات، يُرجى الاطّلاع على [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-pro) و[التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar). ستتم إعادة توجيه `gemini-2.5-pro-preview-05-06`
  إلى `gemini-2.5-pro` في 26 يونيو 2025.
- أطلقنا `gemini-2.5-flash`، وهو أول نموذج مستقر من ‎2.5 Flash. لمزيد من المعلومات، يُرجى الاطّلاع على [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash).
  سيتم إيقاف `gemini-2.5-flash-preview-04-17` نهائيًا في 15 يوليو 2025.
- أطلقنا `gemini-2.5-flash-lite-preview-06-17`، وهو نموذج Gemini 2.5 منخفض التكلفة وعالي الأداء. لمزيد من المعلومات، اطّلِع على [معاينة Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-lite).

## ‫5 يونيو 2025

- أطلقنا `gemini-2.5-pro-preview-06-05`، وهو إصدار جديد من نموذجنا الأكثر تطورًا، ويتضمّن الآن ميزة التفكير التكيّفي. لمزيد من المعلومات، يُرجى الاطّلاع على [معاينة Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-pro-preview-06-05) و[التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).
  ستتم إعادة التوجيه من `gemini-2.5-pro-preview-05-06` إلى `gemini-2.5-pro` في 26 يونيو 2025.

## ‫27 مايو 2025

- تم إيقاف آخر نموذج متاح للضبط، وهو Gemini 1.5 Flash 001.
  لم يعُد التعديل متاحًا على أي من النماذج.
  اطّلِع على [الضبط الدقيق باستخدام Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ar).

## ‫20 مايو 2025

**تعديلات على واجهة برمجة التطبيقات:**

- أتحنا إمكانية
  [المعالجة المسبقة المخصّصة للفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar#customize-video-processing)
  باستخدام فواصل الاقتطاع وأخذ عيّنات من عدد اللقطات في الثانية يمكن ضبطه.
- أطلقنا ميزة استخدام أدوات متعددة، والتي تتيح إعداد
  [تنفيذ التعليمات البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و
  [تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/grounding?hl=ar) في الطلب نفسه
  `generateContent`.
- أتحنا إمكانية
  [إجراء طلبات غير متزامنة لاستدعاء الدوال](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar#async-function-calling)
  في Live API.
- أطلقنا
  [أداة تجريبية لسياق عناوين URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)
  تتيح تقديم عناوين URL كسياق إضافي للطلبات.

**تعديلات على النموذج:**

- أطلقنا `gemini-2.5-flash-preview-05-20`، وهو نموذج [تجريبي](https://ai.google.dev/gemini-api/docs/models?hl=ar#model-versions) من Gemini محسّن من حيث السعر والأداء والتفكير التكيّفي. لمزيد من المعلومات، يمكنك الاطّلاع على [النسخة الحصرية من Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-preview) و[Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).
- أطلقنا النموذجين
  [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-pro-preview-tts)
  و
  [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-preview-tts)
  القادرَين على
  [إنشاء محتوى صوتي](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar) لشخص واحد أو شخصين.
- أطلقنا نموذج `lyria-realtime-exp` الذي
  [ينشئ الموسيقى](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar) في الوقت الفعلي.
- تم إطلاق `gemini-2.5-flash-preview-native-audio-dialog` و`gemini-2.5-flash-exp-native-audio-thinking-dialog`، وهما نموذجان جديدان من Gemini لواجهة Live API مع إمكانات مصدر إخراج الصوت مدمجة. لمزيد من المعلومات، يُرجى الاطّلاع على [دليل Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#native-audio-output) و[الاستماع إلى الصوت مباشرةً في Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-native-audio).
- تم إطلاق إصدار `gemma-3n-e4b-it` تجريبي، وهو متاح على
  [AI Studio](https://aistudio.google.com?hl=ar) ومن خلال Gemini API،
  كجزء من إطلاق [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=ar).

## ‫7 مايو 2025

- أطلقنا `gemini-2.0-flash-preview-image-generation`، وهو نموذج معاينة لإنشاء الصور وتعديلها. لمزيد من المعلومات، يمكنك الاطّلاع على [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) و[إنشاء الصور باستخدام Gemini 2.0 Flash (نسخة حصرية)](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.0-flash-preview-image-generation).

## ‫6 مايو 2025

- أطلقنا `gemini-2.5-pro-preview-05-06`، وهو إصدار جديد من نموذجنا الأكثر تطورًا، يتضمّن تحسينات على الرموز البرمجية واستدعاء الدوال. سيشير `gemini-2.5-pro-preview-03-25` تلقائيًا إلى الإصدار الجديد من النموذج.

## ‫17 أبريل 2025

- أطلقنا `gemini-2.5-flash-preview-04-17`، وهو نموذج [تجريبي](https://ai.google.dev/gemini-api/docs/models?hl=ar#model-versions) من Gemini محسّن من حيث السعر والأداء والتفكير التكيّفي. لمزيد من المعلومات، يمكنك الاطّلاع على [النسخة الحصرية من Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-preview) و[Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).

## ‫16 أبريل 2025

- تم إطلاق ميزة التخزين المؤقت للسياق في
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.0-flash).

## ‫9 أبريل 2025

**تعديلات على النموذج:**

- أطلقنا `veo-2.0-generate-001`، وهو نموذج متوفّر للجمهور العام يحوّل النصوص والصور إلى فيديوهات، ويمكنه إنشاء فيديوهات مفصّلة ودقيقة من الناحية الفنية. لمزيد من المعلومات، يُرجى الاطّلاع على [مستندات Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar).
- تم إصدار `gemini-2.0-flash-live-001`، وهو إصدار تجريبي عام من نموذج
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) مع تفعيل الفوترة.

  - **إدارة الجلسات والموثوقية المحسّنة**

    - **استئناف الجلسة:** إبقاء الجلسات نشطة عند حدوث انقطاعات مؤقتة في الشبكة تتيح واجهة برمجة التطبيقات الآن تخزين حالة الجلسة من جهة الخادم (لمدة تصل إلى 24 ساعة) وتوفّر معرّفات (session\_resumption) لإعادة الاتصال ومواصلة العمل من حيث توقّفت.
    - **جلسات أطول من خلال ضغط السياق:** يمكنك تفعيل تفاعلات ممتدة تتجاوز الحدود الزمنية السابقة. يمكنك ضبط ضغط قدرة استيعاب باستخدام آلية النافذة المنزلقة لإدارة طول السياق تلقائيًا، ما يمنع عمليات الإنهاء المفاجئة بسبب حدود السياق.
    - **إشعار قطع الاتصال السلس:** يمكنك تلقّي رسالة من الخادم `GoAway` تشير إلى الوقت الذي سيتم فيه إغلاق الاتصال، ما يتيح لك التعامل مع الأمر بسلاسة قبل إنهاء الاتصال.
  - **المزيد من التحكّم في ديناميكية التفاعل**
  - **ميزة "رصد النشاط الصوتي" (VAD) القابلة للإعداد:** يمكنك اختيار مستويات الحساسية أو إيقاف ميزة "رصد النشاط الصوتي" التلقائية بالكامل واستخدام أحداث العميل الجديدة (`activityStart` و`activityEnd`) للتحكّم اليدوي في التشغيل.
  - **التعامل القابل للضبط مع المقاطعات:** يمكنك تحديد ما إذا كان يجب أن تؤدي بيانات أدخلها المستخدم إلى مقاطعة استجابة النموذج.
  - **تغطية قابلة للضبط:** اختَر ما إذا كانت واجهة برمجة التطبيقات تعالج كل مدخلات الصوت والفيديو بشكل مستمر أو تسجّلها فقط عندما يتم رصد المستخدم النهائي وهو يتحدث.
  - **درجة دقة الوسائط القابلة للضبط:** يمكنك تحسين الجودة أو استخدام الرموز المميزة
    من خلال اختيار درجة دقة الوسائط المُدخَلة.
  - **ميزات ونتائج أكثر ثراءً**
  - **خيارات موسّعة للغة والصوت:** يمكنك الاختيار من بين صوتَين جديدَين و30 لغة جديدة لإخراج الصوت. يمكنك الآن ضبط لغة الإخراج ضمن `speechConfig`.
  - **بث النص:** يمكنك تلقّي الردود النصية بشكل تدريجي أثناء إنشائها، ما يتيح عرضها بشكل أسرع للمستخدم.
  - **تقارير استخدام الرموز المميزة:** يمكنك الحصول على إحصاءات حول الاستخدام من خلال أعداد الرموز المميزة المفصّلة المقدَّمة في الحقل `usageMetadata` ضمن رسائل الخادم، مع تقسيمها حسب نوع الوسائط ومراحل الطلب أو الرد.

## ‫4 أبريل 2025

- تم طرح `gemini-2.5-pro-preview-03-25`، وهو إصدار مبكر من Gemini 2.5 Pro متاح للجميع
  مع تفعيل الفوترة. يمكنك مواصلة استخدام `gemini-2.5-pro-exp-03-25` في المستوى المجاني.

## ‫25 مارس 2025

- أطلقنا `gemini-2.5-pro-exp-03-25`، وهو نموذج Gemini تجريبي متاح للجميع
  مع تفعيل وضع "التفكير" قيد التشغيل دائمًا تلقائيًا.
  لمزيد من المعلومات، يُرجى الاطّلاع على [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-pro-preview-03-25).

## ‫12 مارس 2025

**تعديلات على النموذج:**

- أطلقنا نموذجًا تجريبيًا من [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#gemini)
  قادرًا على إنشاء الصور وتعديلها.
- تم إطلاقها في `gemma-3-27b-it`، وهي متاحة على
  [AI Studio](https://aistudio.google.com?hl=ar) ومن خلال Gemini API،
  كجزء من إطلاق [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=ar).

**تعديلات على واجهة برمجة التطبيقات:**

- تمت إضافة إمكانية استخدام
  [عناوين URL على YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=ar#youtube) كمصدر للوسائط.
- أضفنا إمكانية تضمين [فيديو مضمّن](https://ai.google.dev/gemini-api/docs/vision?hl=ar#inline-video) بحجم أقل من 20 ميغابايت.

## ‫11 مارس 2025

**تعديلات حزمة تطوير البرامج (SDK):**

- أطلقنا [حزمة تطوير البرامج (SDK) الخاصة بتكنولوجيات الذكاء الاصطناعي التوليدي من Google والمصمَّمة للّغتَين TypeScript وJavaScript](https://googleapis.github.io/js-genai) في إصدار تجريبي علني.

## ‫7 مارس 2025

**تعديلات على النموذج:**

- أطلقنا `gemini-embedding-exp-03-07`
  [نموذجًا تجريبيًا](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=ar)
  للتضمينات يستند إلى Gemini في برنامج "الميزات التجريبية المتاحة للجميع".

## ‫28 فبراير 2025

**تعديلات على واجهة برمجة التطبيقات:**

- أضفنا ميزة [البحث كأداة](https://ai.google.dev/gemini-api/docs/grounding?hl=ar) إلى `gemini-2.0-pro-exp-02-05`، وهو نموذج تجريبي يستند إلى Gemini 2.0 Pro.

## ‫25 فبراير 2025

**تعديلات على النموذج:**

- أصدرنا `gemini-2.0-flash-lite` نسخة متوفّرة للجمهور العام من
  [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-2.0-flash-lite)،
  وهي نسخة محسَّنة من حيث السرعة وقابلية التوسّع وفعالية التكلفة.

## ‫19 فبراير 2025

**التعديلات في AI Studio:**

- توفير الدعم في
  [مناطق إضافية](https://ai.google.dev/gemini-api/docs/available-regions?hl=ar)
  (كوسوفو وغرينلاند وجزر فارو)

**تعديلات على واجهة برمجة التطبيقات:**

- توفير الدعم في
  [مناطق إضافية](https://ai.google.dev/gemini-api/docs/available-regions?hl=ar)
  (كوسوفو وغرينلاند وجزر فارو)

## ‫18 فبراير 2025

**تعديلات على النموذج:**

- لم يعُد الإصدار 1.0 من Gemini Pro متاحًا. للاطّلاع على قائمة الطُرز المتوافقة، يُرجى الانتقال إلى [طُرز Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar).

## ‫11 فبراير 2025

**تعديلات على واجهة برمجة التطبيقات:**

- تحديثات بشأن
  [توافق مكتبات OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar)

## ‫6 فبراير 2025

**تعديلات على النموذج:**

- أطلقنا `imagen-3.0-generate-002`، وهو إصدار متاح للجمهور العام من
  [Imagen 3 في Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=ar).

**تعديلات حزمة تطوير البرامج (SDK):**

- أطلقنا [حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي في Java](https://github.com/googleapis/java-genai)
  في إصدار تجريبي متاح للجميع.

## ‫5 فبراير 2025

**تعديلات على النموذج:**

- أصدرنا `gemini-2.0-flash-001`، وهو إصدار متوفّر للجمهور العام من
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-2.0-flash) يتيح عرض الناتج كنص فقط.
- أصدرنا `gemini-2.0-pro-exp-02-05`،
  نسخة [تجريبية](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=ar) متاحة للجميع
  من Gemini 2.0 Pro.
- تم إطلاق `gemini-2.0-flash-lite-preview-02-05`، وهو نموذج تجريبي متاح للجميع تم تحسينه لتحقيق فعالية التكلفة.

**تعديلات على واجهة برمجة التطبيقات:**

- تمت إضافة دعم [إدخال الملفات وإخراج الرسوم البيانية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar#input-output) إلى تنفيذ الرموز البرمجية.

**تعديلات حزمة تطوير البرامج (SDK):**

- أطلقنا
  [حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي في Python](https://googleapis.github.io/python-genai/)
  وأصبحت متوفّرة للجمهور العام.

## ‫21 يناير 2025

**تعديلات على النموذج:**

- تم إصدار `gemini-2.0-flash-thinking-exp-01-21`، وهو أحدث إصدار تجريبي من النموذج الذي يستند إليه [نموذج Gemini 2.0 Flash المفكّر](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).

## ‫19 ديسمبر 2024

**تعديلات على النموذج:**

- أطلقنا "وضع Flash المفكّر" في Gemini 2.0 Flash كنسخة تجريبية متاحة للجميع. ‫Thinking Mode هو نموذج حسابي لوقت الاختبار يتيح لك الاطّلاع على عملية تفكير النموذج أثناء إنشاء الرد، كما يتيح إنشاء ردود تتضمّن إمكانات استدلال أقوى.

  يمكنك الاطّلاع على مزيد من المعلومات حول "وضع التفكير" في Gemini 2.0 Flash في [صفحة النظرة العامة](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=ar).

## ‫11 ديسمبر 2024

**تعديلات على النموذج:**

- أطلقنا [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-2.0-flash)
  في إصدار تجريبي علني. تشمل القائمة الجزئية لميزات Gemini 2.0 Flash Experimental ما يلي:
  - أسرع بمرتين من Gemini 1.5 Pro
  - البث ثنائي الاتجاه باستخدام Live API
  - إنشاء ردود متعددة الوسائط على شكل نصوص وصور وكلام
  - استخدام الأدوات المضمّنة مع إمكانية إجراء محادثات متعددة المراحل للاستفادة من ميزات مثل تنفيذ الرموز البرمجية و"بحث Google" واستخدام الدوال وغير ذلك

يمكنك الاطّلاع على مزيد من المعلومات حول ‎2.0 Flash في Gemini في [صفحة النظرة العامة](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=ar).

## ‫21 نوفمبر 2024

**تعديلات على النموذج:**

- أطلقنا `gemini-exp-1121`، وهو نموذج تجريبي أكثر تطورًا من Gemini API.

**تعديلات على النموذج:**

- تم تعديل الأسماء المستعارة للنموذج `gemini-1.5-flash-latest` و`gemini-1.5-flash`
  لاستخدام `gemini-1.5-flash-002`.
  - تغيير في المَعلمة `top_k`: يتيح النموذج `gemini-1.5-flash-002`
    قيم `top_k` تتراوح بين 1 و41 (باستثناء 41).
    سيتم تغيير القيم الأكبر من 40 إلى 40.

## ‫14 نوفمبر 2024

**تعديلات على النموذج:**

- أطلقنا `gemini-exp-1114`، وهو نموذج تجريبي قوي من Gemini API.

## ‫8 نوفمبر 2024

**تعديلات على واجهة برمجة التطبيقات:**

- تمت إضافة [إمكانية استخدام Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=ar) في مكتبات OpenAI / واجهة REST API.

## ‫31 أكتوبر 2024

**تعديلات على واجهة برمجة التطبيقات:**

- أضفنا [ميزة "تحديد المصدر من خلال "بحث Search""](https://ai.google.dev/gemini-api/docs/grounding?hl=ar).

## ‫3 أكتوبر 2024

**تعديلات على النموذج:**

- أصدرنا `gemini-1.5-flash-8b-001`، وهو إصدار ثابت من أصغر نماذج واجهة Gemini API.

## ‫24 سبتمبر 2024

**تعديلات على النموذج:**

- أطلقنا الإصدارَين الجديدَين الثابتَين `gemini-1.5-pro-002` و`gemini-1.5-flash-002` من Gemini 1.5 Pro و1.5 Flash، وهما متاحان الآن للجمهور العام.
- تم تعديل رمز النموذج `gemini-1.5-pro-latest` لاستخدام `gemini-1.5-pro-002`، وتم تعديل رمز النموذج `gemini-1.5-flash-latest` لاستخدام `gemini-1.5-flash-002`.
- تم طرح الإصدار `gemini-1.5-flash-8b-exp-0924` ليحلّ محل الإصدار `gemini-1.5-flash-8b-exp-0827`.
- أطلقنا [فلتر السلامة الخاص بالنزاهة المدنية](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar#safety-filters)
  في Gemini API وAI Studio.
- أتحنا استخدام مَعلمتَين جديدتَين في Gemini 1.5 Pro و1.5 Flash في Python وNodeJS:
  [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=ar#FIELDS.frequency_penalty) و
  [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=ar#FIELDS.presence_penalty).

## ‫19 سبتمبر 2024

**التعديلات في AI Studio:**

- أضفنا زرَّي "يعجبني" و"لا يعجبني" إلى ردود النماذج، وذلك للسماح للمستخدمين بتقديم ملاحظات حول جودة الردّ.

**تعديلات على واجهة برمجة التطبيقات:**

- أضفنا إمكانية استخدام أرصدة Google Cloud في Gemini API.

## ‫17 سبتمبر 2024

**التعديلات في AI Studio:**

- أضفنا زر **الفتح في Colab** الذي يصدّر طلبًا والرمز البرمجي لتشغيله إلى ورقة ملاحظات Colab. لا تتيح الميزة بعد استخدام الأدوات في الطلبات (وضع JSON أو استدعاء الدوال أو تنفيذ الرموز البرمجية).

## ‫13 سبتمبر 2024

**التعديلات في AI Studio:**

- أضفنا ميزة "وضع المقارنة" التي تتيح لك مقارنة الردود من نماذج ومطالبات مختلفة للعثور على أفضل تطابق لحالة الاستخدام.

## ‫30 أغسطس 2024

**تعديلات على النموذج:**

- يتيح Gemini 1.5 Flash
  [توفير مخطط JSON من خلال إعدادات النموذج](https://ai.google.dev/gemini-api/docs/json-mode?hl=ar#supply-schema-in-config).

## ‫27 أغسطس 2024

**تعديلات على النموذج:**

- تم إطلاق [النماذج التجريبية](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=ar) التالية:
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## ‫9 أغسطس 2024

**تعديلات على واجهة برمجة التطبيقات:**

- تمت إضافة إمكانية [معالجة ملفات PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar).

## ‫5 أغسطس 2024

**تعديلات على النموذج:**

- أصبح بإمكانك الآن ضبط نموذج Gemini 1.5 Flash بدقة.

## ‫1 أغسطس 2024

**تعديلات على النموذج:**

- أطلقنا `gemini-1.5-pro-exp-0801`، وهو إصدار تجريبي جديد من
  [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-1.5-pro).

## ‫12 يوليو 2024

**تعديلات على النموذج:**

- تمت إزالة إمكانية استخدام Gemini 1.0 Pro Vision من خدمات وأدوات Google AI.

## ‫27 يونيو 2024

**تعديلات على النموذج:**

- إصدار متوفر للجمهور العام لقدرة الاستيعاب التي تبلغ 2 مليون رمز مميّز في Gemini 1.5 Pro

**تعديلات على واجهة برمجة التطبيقات:**

- تمت إضافة إمكانية [تنفيذ الرموز](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar).

## ‫18 يونيو 2024

**تعديلات على واجهة برمجة التطبيقات:**

- تمت إضافة إمكانية [تخزين السياق مؤقتًا](https://ai.google.dev/gemini-api/docs/caching?hl=ar).

## ‫12 يونيو 2024

**تعديلات على النموذج:**

- تم إيقاف Gemini 1.0 Pro Vision نهائيًا.

## ‫23 مايو 2024

**تعديلات على النموذج:**

- [‫Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) متاح للجمهور العام (GA).
- [‫Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) متوفّر للجمهور العام (GA).

## ‫14 مايو 2024

**تعديلات على واجهة برمجة التطبيقات:**

- طرحنا قدرة استيعاب مليوني رمز مميّز في Gemini 1.5 Pro (قائمة انتظار).
- أتحنا [الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar) بنظام الدفع حسب الاستخدام في Gemini 1.0 Pro، وسنتيحها قريبًا في Gemini 1.5 Pro وGemini 1.5 Flash.
- تم تقديم سقف استخدام أعلى للمستوى المدفوع القادم من Gemini 1.5 Pro.
- تمت إضافة إمكانية استخدام الفيديوهات المضمّنة إلى [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ar).
- تمت إضافة إمكانية استخدام النص العادي في [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ar).
- تمت إضافة إمكانية تنفيذ استدعاءات الدوال بشكل متوازٍ، ما يتيح عرض أكثر من استدعاء واحد في المرة الواحدة.

## ‫10 مايو 2024

**تعديلات على النموذج:**

- أطلقنا [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) في نسخة حصرية.

## ‫9 أبريل 2024

**تعديلات على النموذج:**

- أصدرنا [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-1.5-pro)
  (`gemini-1.5-pro-latest`) في نسخة حصرية.
- أطلقنا نموذجًا جديدًا لتضمين النص، وهو `text-embeddings-004`، ويتيح
  [أحجام التضمين المرن](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar#elastic-embedding)
  التي تقل عن 768.

**تعديلات على واجهة برمجة التطبيقات:**

- تم إطلاق [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ar) لتخزين ملفات الوسائط مؤقتًا لاستخدامها في الطلبات.
- أضفنا إمكانية إنشاء الطلبات باستخدام بيانات نصية وصور وملفات صوتية، ويُعرف ذلك أيضًا باسم إنشاء الطلبات *المتعددة الوسائط*. لمزيد من المعلومات، يُرجى الاطّلاع على مقالة [تقديم الطلبات باستخدام الوسائط](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=ar).
- أطلقنا [تعليمات النظام](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ar) في الإصدار التجريبي.
- تمت إضافة
  [وضع استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#function_calling_mode)،
  الذي يحدّد سلوك التنفيذ عند استدعاء الدوال.
- تمت إضافة خيار الإعداد `response_mime_type` الذي يتيح لك طلب الردود [بتنسيق JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=ar#json).

## ‫19 مارس 2024

**تعديلات على النموذج:**

- تمت إضافة إمكانية
  [ضبط Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)
  في Google AI Studio أو باستخدام Gemini API.

## ‫13 ديسمبر 2023

**تعديلات على النموذج:**

- ‫gemini-pro: نموذج نصي جديد لمجموعة متنوعة من المهام تحقيق التوازن بين الإمكانات والكفاءة
- ‫gemini-pro-vision: نموذج جديد متعدّد الوسائط لأداء مجموعة متنوعة من المهام
  تحقيق التوازن بين القدرة والكفاءة
- ‫embedding-001: نموذج تضمينات جديد
- aqa: نموذج جديد تم ضبطه خصيصًا وتدريبه للإجابة عن الأسئلة باستخدام مقاطع نصية لتحديد مصدر الإجابات التي يتم إنشاؤها.

لمزيد من التفاصيل، يُرجى الاطّلاع على [نماذج Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar).

**تعديلات على إصدار واجهة برمجة التطبيقات:**

- الإصدار 1: قناة واجهة برمجة التطبيقات الثابتة
- v1beta: قناة تجريبية تتضمّن هذه القناة ميزات قد تكون قيد التطوير.

لمزيد من التفاصيل، يمكنك الاطّلاع على [موضوع إصدارات واجهة برمجة التطبيقات](https://ai.google.dev/gemini-api/docs/api-versions?hl=ar).

**تعديلات على واجهة برمجة التطبيقات:**

- ‫`GenerateContent` هي نقطة نهاية موحّدة واحدة للمحادثات والنصوص.
- يمكنك بث المحتوى باستخدام طريقة `StreamGenerateContent`.
- إمكانية استخدام وسائط متعددة: الصورة هي وسيط جديد متوافق
- الميزات التجريبية الجديدة:
  - [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=ar)
  - الإجابة عن الأسئلة مع ذكر المصدر (AQA)
- عدد المرشحين المعدَّل: لا تعرض نماذج Gemini سوى مرشح واحد.
- فئات مختلفة من "إعدادات السلامة الشخصية" و"تقييم السلامة" يمكنك الاطّلاع على [إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar) لمزيد من التفاصيل.
- لا تتوفّر بعد إمكانية ضبط النماذج لنماذج Gemini (نعمل على توفيرها).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
