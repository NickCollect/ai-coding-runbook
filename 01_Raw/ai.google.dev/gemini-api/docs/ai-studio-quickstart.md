---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ar
fetched_at: 2026-06-29T05:36:18.972255+00:00
title: "\u062f\u0644\u064a\u0644 \u0627\u0644\u0628\u062f\u0621 \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# دليل البدء السريع لاستخدام Google AI Studio

تتيح لك أداة [Google AI Studio](https://aistudio.google.com/?hl=ar) تجربة
النماذج بسرعة واستخدام طلبات مختلفة. عندما تصبحون مستعدين للإنشاء، يمكنكم اختيار "الحصول على الرمز البرمجي" ولغة البرمجة المفضّلة لاستخدام [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=ar).

## الطلبات والإعدادات

توفّر أداة Google AI Studio عدة واجهات للطلبات المصمّمة لحالات استخدام مختلفة. يغطّي هذا الدليل **طلبات المحادثة** المستخدَمة لإنشاء
تجارب حوارية. تسمح هذه التقنية بتلقّي عدة مدخلات
وتقديم عدة ردود لإنشاء الناتج. يمكنكم معرفة المزيد من خلال
[مثال طلب المحادثة أدناه](#chat_example).
تشمل الخيارات الأخرى **البث في الوقت الفعلي** و**إنشاء الفيديوهات** و
المزيد.

توفر أداة AI Studio أيضًا لوحة **إعدادات التشغيل** التي يمكنكم من خلالها إجراء
تعديلات على [مَعلمات النموذج](https://ai.google.dev/docs/prompting-strategies?hl=ar#model-parameters)،
[إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar)، وتفعيل أدوات مثل
[الناتج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar)، [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)، [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)، و[التثبيت](https://ai.google.dev/gemini-api/docs/grounding?hl=ar).

## مثال على طلب محادثة: إنشاء تطبيق محادثة مخصّص

إذا سبق لكم استخدام روبوت دردشة متعدد الأغراض مثل
[Gemini](https://gemini.google.com/?hl=ar)، فقد اختبرتم بأنفسكم مدى فعالية نماذج الذكاء الاصطناعي التوليدي في الحوارات المفتوحة. على الرغم من أنّ روبوتات الدردشة متعددة الأغراض هذه مفيدة، غالبًا ما يجب تخصيصها لحالات استخدام معيّنة.

على سبيل المثال، قد تريدون إنشاء روبوت دردشة لخدمة العملاء لا يتيح إلا المحادثات التي تتناول منتجًا معيّنًا للشركة. قد تريدون إنشاء روبوت دردشة يتحدث بأسلوب أو نبرة معيّنة، مثل روبوت يطلق الكثير من النكات أو يتحدث بأسلوب الشاعر أو يستخدم الكثير من الرموز الإيموجي في إجاباته.

يوضّح لكم هذا المثال كيفية استخدام Google AI Studio لإنشاء روبوت دردشة ودود يتواصل كما لو كان كائنًا فضائيًا يعيش على أحد أقمار كوكب المشتري، وهو أوروبا.

### الخطوة 1: إنشاء طلب محادثة

لإنشاء روبوت دردشة، يجب تقديم أمثلة على التفاعلات بين المستخدم وروبوت الدردشة لتوجيه النموذج إلى تقديم الردود المطلوبة.

لإنشاء طلب محادثة، اتّبِعوا الخطوات التالية:

1. افتحوا [Google AI Studio](https://aistudio.google.com/?hl=ar). سيتم فتح **ساحة اللعب** تلقائيًا مع طلب محادثة جديد.
2. انقروا على **إعدادات التشغيل** tune في أعلى يسار الشاشة
   لتوسيع اللوحة، وابحثوا عن
   [**تعليمات النظام**](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#system-instructions)
   حقل الإدخال. الصقوا ما يلي في حقل إدخال النص:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

بعد إضافة تعليمات النظام، ابدأوا اختبار تطبيقكم من خلال التحدّث مع النموذج:

1. في مربّع إدخال النص الذي يحمل العنوان **اكتب شيئًا...** ، اكتبوا سؤالاً أو
   ملاحظة قد يطرحها المستخدم. على سبيل المثال:

   **المستخدم:**

   ```
   What's the weather like?
   ```
2. انقروا على الزر **تشغيل** للحصول على ردّ من روبوت الدردشة. قد يكون هذا الردّ على النحو التالي:

   **النموذج:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### الخطوة 2: تعليم روبوت الدردشة التحدّث بشكل أفضل

من خلال تقديم تعليمات واحدة، تمكّنتم من إنشاء روبوت دردشة أساسي للكائن الفضائي في أوروبا. ومع ذلك، قد لا تكون التعليمات الواحدة كافية لضمان الاتساق والجودة في ردود النموذج. بدون تعليمات أكثر تحديدًا، يميل ردّ النموذج على سؤال حول الطقس إلى أن يكون طويلاً جدًا، ويمكن أن يتخذ شكلًا مختلفًا.

خصّصوا نبرة روبوت الدردشة من خلال إضافة تعليمات النظام:

1. ابدأوا طلب محادثة جديدًا أو استخدموا الطلب نفسه. يمكن تعديل تعليمات النظام بعد بدء جلسة المحادثة.
2. في قسم **تعليمات النظام** ، غيِّروا التعليمات الحالية إلى ما يلي:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. أعيدوا إدخال سؤالكم (`What's the weather like?`) وانقروا على الزر **تشغيل**. إذا لم تبدأوا محادثة جديدة، قد يبدو ردّكم على النحو التالي:

   **النموذج:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

يمكنكم استخدام هذا النهج لإضافة المزيد من التفاصيل إلى روبوت الدردشة. اطرحوا المزيد من الأسئلة وعدّلوا الإجابات وحسّنوا جودة روبوت الدردشة. واصلوا إضافة التعليمات أو تعديلها واختبروا كيف تغيّر سلوك روبوت الدردشة.

### الخطوة 3: الخطوات التالية

على غرار أنواع الطلبات الأخرى، بعد إنشاء نموذج أولي للطلب بما يرضيكم، يمكنكم استخدام الزر **الحصول على الرمز البرمجي** لبدء الترميز أو حفظ الطلب للعمل عليه لاحقًا ومشاركته مع الآخرين.

## محتوى إضافي للقراءة

- إذا كنتم مستعدين للانتقال إلى الرمز البرمجي، اطّلِعوا على [أدلة البدء في واجهة برمجة التطبيقات](https://ai.google.dev/gemini-api/docs/get-started?hl=ar).
- للتعرّف على كيفية إنشاء طلبات أفضل، اطّلِعوا على [إرشادات
  تصميم الطلبات](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
