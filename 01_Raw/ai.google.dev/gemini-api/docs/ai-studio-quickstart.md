---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ar
fetched_at: 2026-06-15T06:25:00.811116+00:00
title: "\u062f\u0644\u064a\u0644 \u0627\u0644\u0628\u062f\u0621 \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# دليل البدء السريع لاستخدام Google AI Studio

تتيح لك أداة [Google AI Studio](https://aistudio.google.com/?hl=ar) تجربة النماذج بسرعة واستخدام طلبات مختلفة. عندما تكون مستعدًا للبدء، يمكنك النقر على "الحصول على الرمز" واختيار لغة البرمجة المفضّلة لديك لاستخدام [Gemini API](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar).

## الطلبات والإعدادات

توفّر أداة Google AI Studio عدة واجهات للطلبات مصمَّمة لحالات استخدام مختلفة. يتناول هذا الدليل **طلبات الدردشة** المستخدَمة لإنشاء تجارب حوارية. تسمح تقنية الطلبات هذه بتعدّد مرات إدخال البيانات والردود لإنشاء الناتج. يمكنك الاطّلاع على المزيد من المعلومات من خلال
[مثال طلب الدردشة أدناه](#chat_example).
تشمل الخيارات الأخرى **البث المباشر في الوقت الفعلي** و**إنشاء الفيديو** وغير ذلك.

توفّر أداة AI Studio أيضًا لوحة **إعدادات التشغيل**، حيث يمكنك إجراء تعديلات على [مَعلمات النموذج](https://ai.google.dev/docs/prompting-strategies?hl=ar#model-parameters) و[إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar) وتفعيل أدوات مثل [النتائج المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) و[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) و[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و[الاستناد إلى مصادر خارجية](https://ai.google.dev/gemini-api/docs/grounding?hl=ar).

## مثال على طلب في Chat: إنشاء تطبيق محادثة مخصّص

إذا سبق لك استخدام روبوت دردشة للأغراض العامة مثل [Gemini](https://gemini.google.com/?hl=ar)، تكون قد جرّبت بنفسك مدى فعالية نماذج الذكاء الاصطناعي التوليدي في الحوارات المفتوحة. على الرغم من أنّ روبوتات الدردشة ذات الأغراض العامة مفيدة، إلا أنّها غالبًا ما تحتاج إلى التكيّف مع حالات استخدام معيّنة.

على سبيل المثال، قد تريد إنشاء روبوت دردشة لخدمة العملاء يتيح فقط إجراء محادثات حول منتج إحدى الشركات. قد تحتاج إلى إنشاء روبوت دردشة يتحدث بأسلوب أو نبرة معيّنة، مثل روبوت يطلق الكثير من النكات أو يكتب الشعر أو يستخدم الكثير من رموز الإيموجي في ردوده.

يوضّح لك هذا المثال كيفية استخدام Google AI Studio لإنشاء روبوت دردشة ودود
يتواصل كما لو كان كائنًا فضائيًا يعيش على أحد أقمار كوكب المشتري، وهو أوروبا.

### الخطوة 1: إنشاء طلب محادثة

لإنشاء روبوت دردشة، عليك تقديم أمثلة على التفاعلات بين المستخدم وروبوت الدردشة لتوجيه النموذج لتقديم الردود التي تبحث عنها.

لإنشاء طلب محادثة، اتّبِع الخطوات التالية:

1. افتح [Google AI Studio](https://aistudio.google.com/?hl=ar). سيتم فتح **Playground** تلقائيًا مع طلب محادثة جديد.
2. انقر على **إعدادات التشغيل** tune في أعلى يسار الصفحة
   لتوسيع اللوحة، وابحث عن حقل الإدخال
   [**تعليمات النظام**](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#system-instructions). الصِق ما يلي في حقل إدخال النص:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

بعد إضافة تعليمات النظام، ابدأ في اختبار تطبيقك من خلال الدردشة مع النموذج:

1. في مربّع إدخال النص الذي يحمل التصنيف **اكتب شيئًا...**، اكتب سؤالاً أو ملاحظة قد يطرحها المستخدم. على سبيل المثال:

   **المستخدم:**

   ```
   What's the weather like?
   ```
2. انقر على الزر **تشغيل** للحصول على ردّ من روبوت الدردشة. قد تكون الاستجابة مشابهة لما يلي:

   **الطراز:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### الخطوة 2: تعليم برنامج التتبُّع كيفية إجراء محادثات أفضل

من خلال تقديم تعليمات بسيطة، تمكّنت من إنشاء برنامج دردشة آلي أساسي خاص بالكائنات الفضائية في أوروبا. ومع ذلك، قد لا تكون التعليمات الفردية كافية لضمان الاتساق والجودة في ردود النموذج. بدون تعليمات أكثر تحديدًا، يميل ردّ النموذج على سؤال حول الطقس إلى أن يكون طويلاً جدًا، ويمكن أن يتخذ شكلًا غير متوقّع.

خصِّص أسلوب روبوت الدردشة من خلال إضافة ما يلي إلى تعليمات النظام:

1. ابدأ بطلب جديد أو استخدِم الطلب نفسه. يمكن تعديل تعليمات النظام بعد بدء جلسة المحادثة.
2. في قسم **تعليمات النظام**، غيِّر التعليمات الحالية إلى ما يلي:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. أعِد إدخال سؤالك (`What's the weather like?`) وانقر على الزر **تنفيذ**. إذا لم تبدأ محادثة جديدة، قد يبدو ردّك على النحو التالي:

   **الطراز:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

يمكنك استخدام هذا الأسلوب لإضافة المزيد من العمق إلى روبوت الدردشة. اطرح المزيد من الأسئلة وعدِّل الإجابات وحسِّن جودة برنامج الدردشة الآلي. تابِع إضافة التعليمات أو تعديلها واختبِر كيف تغيّر سلوك روبوت الدردشة.

### الخطوة 3: الخطوات التالية

كما هو الحال مع أنواع الطلبات الأخرى، بعد أن تصبح راضيًا عن النموذج الأوّلي لطلبك، يمكنك استخدام الزر **الحصول على الرمز** لبدء الترميز أو حفظ طلبك للعمل عليه لاحقًا ومشاركته مع الآخرين.

## محتوى إضافي للقراءة

- إذا كنت مستعدًا للانتقال إلى الرمز، يمكنك الاطّلاع على [البدايات السريعة لواجهة برمجة التطبيقات](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar).
- لمعرفة كيفية صياغة طلبات أفضل، اطّلِع على [إرشادات تصميم الطلبات](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
