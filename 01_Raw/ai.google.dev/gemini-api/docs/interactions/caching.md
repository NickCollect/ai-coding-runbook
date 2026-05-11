---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=ar
fetched_at: 2026-05-11T05:04:28.078860+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تخزين السياق مؤقتًا

في سير عمل الذكاء الاصطناعي النموذجي، قد تُمرِّر الرموز المميّزة نفسها للإدخال مرارًا وتكرارًا إلى أحد النماذج. توفّر Gemini API ميزة التخزين المؤقت الضمني لتحسين الأداء والتكاليف.

## التخزين المؤقت الضمني

يتم تفعيل التخزين المؤقت الضمني تلقائيًا لجميع نماذج Gemini 2.5 والإصدارات الأحدث. ننقل تلقائيًا وفورات التكلفة إذا كان طلبك يطابق البيانات المخزّنة مؤقتًا. ليس عليك اتّخاذ أي إجراء لتفعيل هذه الميزة. يتم إدراج الحد الأدنى لعدد الرموز المميّزة للإدخال من أجل تخزين السياق مؤقتًا في الجدول التالي لكل نموذج:

| الطراز | الحد الأدنى للرموز المميّزة |
| --- | --- |
| ‫Gemini 3 Flash (معاينة) | 1024 |
| ‫Gemini 3 Pro (معاينة) | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

لزيادة فرصة مطابقة البيانات المخزّنة مؤقتًا ضمنيًا:

- حاوِل وضع المحتويات الكبيرة والشائعة في بداية طلبك
- حاوِل إرسال طلبات تتضمّن بادئة مشابهة خلال فترة قصيرة

يمكنك الاطّلاع على عدد الرموز المميّزة التي طابقت البيانات المخزّنة مؤقتًا في حقل `usage_metadata` (بايثون) أو `usageMetadata` (JavaScript) في عنصر الاستجابة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
