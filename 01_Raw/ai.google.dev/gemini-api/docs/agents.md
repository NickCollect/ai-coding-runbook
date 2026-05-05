---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=ar
fetched_at: 2026-05-05T19:44:25.429945+00:00
title: "\u0646\u0638\u0631\u0629 \u0639\u0627\u0645\u0629 \u0639\u0644\u0649 \u0627\u0644\u0648\u0643\u0644\u0627\u0621 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# نظرة عامة على الوكلاء

الوكلاء هم أنظمة تستفيد من نماذج Gemini ومجموعة من الأدوات وإمكانيات الاستدلال لأداء مهام معقّدة ومتعدّدة الخطوات وتحقيق أهداف معيّنة. على عكس استدعاء نموذج واحد، يمكن للوكيل التخطيط وتنفيذ سلسلة من الإجراءات والتفاعل مع الأنظمة الخارجية وتجميع المعلومات لتلبية طلب المستخدم.

باستخدام Gemini API، يمكنك إنشاء وكلاء فعّالين من خلال الاستفادة من ميزات مثل:

- **[نماذج Gemini](https://ai.google.dev/gemini-api/docs/models?hl=ar):** هي الذكاء الأساسي الذي يوفّر إمكانيات التحليل المنطقي وفهم اللغة.
- **[الأدوات](https://ai.google.dev/gemini-api/docs/tools?hl=ar):** هي الإمكانيات التي تربط النموذج بـ
  المعلومات والإجراءات في العالم الحقيقي. يمكن أن تكون هذه الأدوات مضمّنة (مثل "بحث Google" أو "خرائط Google" أو "تنفيذ الرموز البرمجية") أو أدوات مخصّصة.
- **[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar):** هي الآلية التي تتيح لك
  تحديد أدواتك وواجهات برمجة التطبيقات المخصّصة وربطها بنموذج Gemini.
- **[\*\*Thinking\*\*](https://ai.google.dev/gemini-api/docs/thinking?hl=ar):** هي الميزات التي تُحسّن قدرة النموذج على التحليل المنطقي والتخطيط للمهام المعقّدة.
- **[\*\*السياق الطويل\*\*](https://ai.google.dev/gemini-api/docs/long-context?hl=ar):** يتيح للوكلاء
  الاحتفاظ بالحالة والمعلومات خلال التفاعلات المطوّلة.

## الوكلاء المتاحون

- **[وكيل الأبحاث المتعمّقة](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar):** هو وكيل مستقل يخطّط وينفّذ ويجمع مهام بحث متعدّدة الخطوات لحالات استخدام مثل تحليل السوق والعناية الواجبة ومراجعات الأدبيات.

## إنشاء الوكلاء

يستخدم الوكلاء النماذج والأدوات لإكمال المهام المتعدّدة الخطوات. في حين يوفّر Gemini إمكانيات التحليل المنطقي (العقل) والأدوات الأساسية (الأيدي)، غالبًا ما تحتاج إلى إطار عمل للتنسيق من أجل إدارة ذاكرة الوكيل وحلقات التخطيط وتنفيذ ربط الأدوات المعقّد.

لتحقيق أقصى قدر من الموثوقية في عمليات سير العمل المتعدّدة الخطوات، عليك إنشاء تعليمات تتحكّم بشكل صريح في طريقة تحليل النموذج وتخطيطه. في حين يوفّر Gemini إمكانيات تحليل منطقي عامة قوية، تستفيد الوكلاء المعقّدون من الطلبات التي تفرض سلوكيات معيّنة، مثل الثبات في مواجهة المشاكل وتقييم المخاطر والتخطيط الاستباقي.

[يمكنك الاطّلاع على عمليات سير العمل المستندة إلى الوكلاء للحصول على استراتيجيات حول تصميم هذه الطلبات.](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar#agentic-workflows) [في ما يلي مثال على تعليمات النظام التي حسّنت الأداء في العديد من المقاييس المستندة إلى الوكلاء بنسبة %5 تقريبًا.](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar#agentic-si-template)

## أطر عمل الوكلاء

يتكامل Gemini مع أطر عمل الوكلاء الرائدة والمفتوحة المصدر، مثل:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=ar): يمكنك إنشاء تدفقات تطبيقات معقّدة ومستندة إلى الحالة وأنظمة متعدّدة الوكلاء باستخدام هياكل الرسم البياني.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=ar): يمكنك ربط وكلاء Gemini بـ
  بياناتك الخاصة لعمليات سير العمل المحسّنة باستخدام تقنية الاسترجاع المعزّز للتوليد (RAG).
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=ar)
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=ar): يمكنك إنشاء واجهات مستخدم ووكلاء مستندين إلى الذكاء الاصطناعي بلغة JavaScript/TypeScript.
- [**\*\*Google ADK\*\***](https://google.github.io/adk-docs/get-started/python/): هو إطار عمل مفتوح المصدر لإنشاء وكلاء ذكاء اصطناعي قابلين للتشغيل المتبادل وتنسيقهم.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
