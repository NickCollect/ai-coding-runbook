---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=ar
fetched_at: 2026-07-06T05:10:44.900876+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0627\u0644\u0641\u064a\u062f\u064a\u0648\u0647\u0627\u062a \u0641\u064a Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء الفيديوهات في Gemini API

توفر Gemini API نموذجين لإنشاء الفيديوهات،
[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ar) و[Veo](https://ai.google.dev/gemini-api/docs/veo?hl=ar).
تم تصميم كلّ منهما لسير عمل مختلف.

استخدِم Gemini Omni Flash كنموذج تلقائي لإنشاء الفيديوهات. يوفّر هذا النموذج اتساقًا فائقًا للفيديوهات، واستدلالًا متعدد الإدخالات (يدعم إدخالات النصوص والصور والمقاطع الصوتية والفيديوهات في الوقت نفسه)، واتساق الشخصيات، ودقة الحقائق، وتعديل المحادثات المترابطة (مثل استبدال العناصر أو تغيير المنظورات). استخدِم Veo 3.1 إذا كنت بحاجة إلى إمكانات معيّنة، مثل توسيع المشهد أو التحكّم في الإطار الأخير أو الدمج مع مسارات البيانات القديمة.

## Gemini Omni Flash

‫Gemini Omni Flash هو نموذج سريع ومتعدّد الوسائط لإنشاء الفيديوهات وتعديلها في المحادثات. يتفوّق هذا النموذج في تحويل الطلبات النصية والصور بسرعة إلى فيديوهات قصيرة، ويسمح لك بتحسين النتائج على مدار عدة أدوار باستخدام Interactions API.

[ابدأ باستخدام Gemini Omni Flash ←](https://ai.google.dev/gemini-api/docs/omni?hl=ar)

## Veo 3.1

‫Veo 3.1 هو نموذج لإنشاء الفيديوهات مع مقاطع صوتية أصلية. يدعم هذا النموذج ميزات مثل توسيع الفيديوهات والإنشاء على مستوى الإطار والتوجيه المستند إلى الصور من خلال `generateContent` API.

[ابدأ باستخدام Veo 3.1 ←](https://ai.google.dev/gemini-api/docs/veo?hl=ar)

## فهم الفيديوهات

إذا كنت بحاجة إلى استيعاب محتوى الفيديو الحالي وتحليله بدلاً من إنشاء
فيديو جديد، اطّلِع على دليل [فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
