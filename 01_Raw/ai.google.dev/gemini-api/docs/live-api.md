---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=ar
fetched_at: 2026-05-18T05:17:24.597274+00:00
title: "Gemini Live API overview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Gemini Live API overview

تتيح Live API التفاعل مع Gemini صوتيًا ومرئيًا في الوقت الفعلي وبزمن انتقال منخفض. تعالج هذه الواجهة تدفقات مستمرة من الصوت والصور والنصوص لتقديم ردود فورية منطوقة تشبه ردود البشر، ما يتيح للمستخدمين تجربة محادثة طبيعية.

![نظرة عامة على Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=ar)

[تجربة Live API في Google AI Studiomic](https://aistudio.google.com/live?hl=ar)
[استنساخ تطبيقات نموذجية من GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[استخدام مهارات وكيل الترميزterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)

## حالات الاستخدام

يمكن استخدام Live API لإنشاء وكلاء صوتيين في الوقت الفعلي لمجموعة متنوعة من المجالات، بما في ذلك:

- **التجارة الإلكترونية والبيع بالتجزئة:** مساعدو التسوّق الذين يقدّمون اقتراحات مخصّصة ووكلاء الدعم الذين يحلّون مشاكل العملاء
- **الألعاب:** شخصيات تفاعلية لا يتحكّم بها اللاعب (NPC) ومساعدون داخل اللعبة وترجمة في الوقت الفعلي للمحتوى داخل اللعبة
- **الجيل التالي من واجهات المستخدم:** تجارب تستخدم الصوت والفيديو في الروبوتات والنظارات الذكية والمركبات
- **الرعاية الصحية:** رفقاء صحيون لتقديم الدعم للمرضى وتثقيفهم
- **الخدمات المالية:** مستشارون يعملون بالذكاء الاصطناعي لإدارة الثروات وتقديم إرشادات حول الاستثمار
- **التعليم:** مرشدون ومرافقون للمتعلّمين يستندون إلى الذكاء الاصطناعي ويقدّمون تعليمات وملاحظات مخصّصة.

## الميزات الرئيسية

تقدّم Live API مجموعة شاملة من الميزات لإنشاء وكلاء صوتيين فعّالين:

- [**دعم لغات متعددة**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#supported-languages):
  يمكنك التحدّث بـ 70 لغة متاحة.
- [**المقاطعة**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#interruptions):
  يمكن للمستخدمين مقاطعة النموذج في أي وقت لإجراء تفاعلات سريعة الاستجابة.
- [**استخدام الأدوات**](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar):
  يدمج هذا الخيار أدوات مثل ميزة "طلب تنفيذ وظيفة" و"بحث Google" لإجراء تفاعلات ديناميكية.
- [**تحويل الصوت إلى نص**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#audio-transcription):
  توفّر هذه الميزة نصوصًا من بيانات أدخلها المستخدم ومن مخرجات النموذج.
- [**الاستجابة الصوتية الاستباقية**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#proactive-audio):
  تتيح لك التحكّم في وقت استجابة النموذج والسياقات التي يستجيب فيها.
- [**حوار تفاعلي تعاطفي**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar#affective-dialog):
  يعدّل أسلوب الرد ونبرته ليناسبا تعبيرات المستخدم.

## المواصفات الفنية

يوضّح الجدول التالي المواصفات الفنية لواجهة Live API:

| الفئة | التفاصيل |
| --- | --- |
| طرق الإدخال | الصوت (صوت PCM خام بمعدل 16 بت، 16 كيلوهرتز، ترتيب البايتات الأصغر أولاً)، والصور (JPEG <= 1 لقطة في الثانية)، والنصوص |
| طُرق الإخراج | الصوت (صوت PCM خام بمعدل 16 بت، و24 كيلوهرتز، وترتيب وحدات البايت الأصغر أولاً) |
| البروتوكول | اتصال WebSocket ذو الحالة (WSS) |

## اختيار طريقة التنفيذ

عند الدمج مع Live API، عليك اختيار أحد أساليب التنفيذ التالية:

- **من الخادم إلى الخادم**: يتصل الخلفية بواجهة Live API باستخدام
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). عادةً، يرسل العميل بيانات البث (الصوت والفيديو والنص) إلى الخادم، الذي يعيد توجيهها إلى Live API.
- **من العميل إلى الخادم**: يتصل رمز الواجهة الأمامية مباشرةً بواجهة برمجة التطبيقات Live API
  باستخدام [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) لبث البيانات، ما يؤدي إلى تجاوز الواجهة الخلفية.

للحد من المخاطر الأمنية.

## البدء

اختَر الدليل الذي يتوافق مع بيئة التطوير:

من خادم إلى خادم

### [برنامج تعليمي حول حزمة تطوير البرامج (SDK) للذكاء الاصطناعي التوليدي](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ar)

يمكنك الربط بواجهة Gemini Live API باستخدام حزمة GenAI SDK لإنشاء تطبيق متعدّد الوسائط في الوقت الفعلي مع خادم خلفي بلغة Python.

من العميل إلى الخادم

### [برنامج تعليمي حول WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ar)

يمكنك الربط بواجهة Gemini Live API باستخدام WebSockets لإنشاء تطبيق متعدّد الوسائط في الوقت الفعلي مع واجهة أمامية JavaScript ورموز مميزة مؤقتة.

مجموعة أدوات تطوير الوكيل

### [برنامج تعليمي حول حزمة تطوير التطبيقات لنظام Android](https://google.github.io/adk-docs/streaming/)

أنشئ وكيلاً واستخدِم ميزة "البث المباشر" في "مجموعة أدوات تطوير الوكلاء" (ADK) لتفعيل التواصل الصوتي والمرئي.

## عمليات الدمج مع الشركاء

لتسهيل عملية تطوير تطبيقات الصوت والفيديو في الوقت الفعلي، يمكنك استخدام عملية دمج تابعة لجهة خارجية تتوافق مع واجهة برمجة التطبيقات Gemini Live عبر WebRTC أو WebSockets.

[LiveKit

استخدام Gemini Live API مع LiveKit Agents](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

إنشاء روبوت دردشة بالذكاء الاصطناعي في الوقت الفعلي باستخدام Gemini Live وPipecat](https://docs.pipecat.ai/guides/features/gemini-live)
[‫Fishjam من Software Mansion

يمكنك إنشاء تطبيقات لبث الفيديو المباشر والصوت باستخدام Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[وكلاء Vision حسب البث

يمكنك إنشاء تطبيقات ذكاء اصطناعي للصوت والفيديو في الوقت الفعلي باستخدام Vision Agents.](https://visionagents.ai/integrations/gemini)
[Voximplant

ربط المكالمات الواردة والصادرة بواجهة برمجة التطبيقات Live API باستخدام Voximplant](https://voximplant.com/products/gemini-client)
[Agora

إنشاء تطبيقات ذكاء اصطناعي حوارية في الوقت الفعلي باستخدام Agora](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

ابدأ استخدام Gemini Live API من خلال Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
