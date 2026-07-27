---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=ar
fetched_at: 2026-07-27T04:37:11.157513+00:00
title: "\u0627\u0644\u062a\u062e\u0632\u064a\u0646 \u0627\u0644\u0645\u0624\u0642\u062a \u0644\u0644\u0633\u064a\u0627\u0642 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# التخزين المؤقت للسياق

في سير عمل الذكاء الاصطناعي النموذجي، قد يتم تمرير رموز الإدخال نفسها بشكل متكرّر إلى أحد النماذج. توفّر Gemini API ميزة التخزين المؤقت الضمني لتحسين الأداء والتكاليف.

## التخزين المؤقت الضمني

يتم تفعيل التخزين المؤقت الضمني تلقائيًا لجميع نماذج Gemini 2.5 والإصدارات الأحدث. [وهو متاح لكل من [أوضاع المحادثات التي تحتفظ بالحالة](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#multi-turn-conversations) (باستخدام `previous_interaction_id`)
وتلك التي لا تحتفظ بالحالة](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#stateless-conversations).
ننقل تلقائيًا وفورات التكلفة إذا تم العثور على طلبك في ذاكرات التخزين المؤقت. ليس عليك اتّخاذ أي إجراء لتفعيل هذه الميزة. يتم إدراج الحد الأدنى لعدد رموز الإدخال من أجل التخزين المؤقت للسياق في الجدول التالي لكل نموذج:

| الطراز | الحد الأدنى لعدد الرموز |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| ‫Gemini 3.1 Pro (معاينة) | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

لزيادة فرصة العثور على البيانات في ذاكرة التخزين المؤقت الضمني:

- حاوِل وضع المحتويات الكبيرة والشائعة في بداية طلبك.
- حاوِل إرسال الطلبات التي تتضمّن بادئة مشابهة خلال فترة قصيرة.

يمكنك الاطّلاع على عدد الرموز التي تم العثور عليها في ذاكرة التخزين المؤقت في الحقل `usage.total_cached_tokens` (Python وJavaScript) في عنصر الاستجابة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-07 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-07 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
