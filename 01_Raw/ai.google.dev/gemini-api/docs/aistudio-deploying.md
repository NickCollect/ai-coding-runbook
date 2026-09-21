---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=ar
fetched_at: 2026-09-21T05:46:57.200142+00:00
title: "\u0627\u0644\u0646\u0634\u0631 \u0645\u0646 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# النشر من Google AI Studio

يتيح لك Google AI Studio نشر تطبيقاتك الكاملة مباشرةً من "وضع الإنشاء". ويوفّر ذلك مسارًا سريعًا من النموذج الأوّلي إلى بيئة إنتاج مُدارة وقابلة للتوسّع.

## خيارات النشر

لنشر تطبيقك من "وضع الإنشاء" في AI Studio، تعتمد المتطلبات على المستوى الذي تستخدمه:

- [**Google Cloud Starter Tier**](https://docs.cloud.google.com/docs/starter-tier?hl=ar):
  يتيح لك نشر ما يصل إلى تطبيقَين كاملَين بدون إعداد مشروع Google Cloud أو حساب فوترة.
- **النشر العادي**: يتطلّب مشروع Google Cloud مرتبطًا بحسابك على
  AI Studio وتفعيل الفوترة في هذا المشروع.

## لمحة عن Starter Tier

يوفّر Google Cloud Starter Tier مسارًا مبسطًا لنشر التطبيقات على Google Cloud مباشرةً من Google AI Studio بدون إعداد بيئة Google Cloud كاملة أو حساب فوترة.

ينشئ كل عملية نشر في Google AI Studio خدمة مقابلة في Cloud Run. بالنسبة إلى الخدمات التي يتم نشرها في Google AI Studio باستخدام Starter Tier، تسري القيود التالية:

- يمكنك نشر ما يصل إلى خدمتَين.
- [يتم نشر خدماتك في منطقة واحدة من Cloud Run.](https://docs.cloud.google.com/run/docs/locations?hl=ar)

## خطوات نشر Starter Tier

بعد تصميم تطبيقك في "وضع الإنشاء"، يمكنك نشره باستخدام Starter Tier:

1. انقر على الزر **نشر** في أعلى يسار الصفحة.
2. انقر على **البدء**.
3. انقر على **نشر التطبيق**.

بعد اكتمال عملية النشر، يوفّر AI Studio عنوان URL لـ Cloud Run يمكنك من خلاله الوصول إلى تطبيقك المباشر.

## عناوين URL المخصّصة لـ AI Studio

عند نشر تطبيق من Google AI Studio، يمكنك ضبط نطاق فرعي مخصّص،
لا يُنسى ضمن `ai.studio` (على سبيل المثال،
`https://your-app-name.ai.studio`).

يتطلّب Google AI Studio أن تكون النطاقات الفرعية فريدة على مستوى العالم في جميع المشاريع، ويتم تخصيصها حسب أسبقية الطلب. إذا كان مشروع آخر يستخدم اسمًا، يطلب منك AI Studio اختيار اسم مختلف. إذا ألغيت نشر تطبيق أو حذفْته، يتم إطلاق عنوان URL المخصّص له ويصبح متاحًا للمستخدمين الآخرين للمطالبة به.

### ضبط عنوان URL مخصّص

لضبط عنوان URL مخصّص لتطبيقك أو تعديله، اتّبِع الخطوات التالية:

1. افتح تطبيقك في Google AI Studio في **وضع الإنشاء**.
2. انقر على **نشر** في أعلى يسار الصفحة.
3. في إعدادات النشر، أدخِل النطاق الفرعي المفضّل في حقل **عنوان URL المخصّص** أو اقبل عنوان URL المقترَح.
4. انقر على **نشر التطبيق**.

لنقل عنوان URL مخصّص حالي إلى تطبيق مختلف، عليك أولاً إلغاء نشر التطبيق الذي تم تخصيص عنوان URL المخصّص له أو حذفه، ثم نشر تطبيقك الجديد باستخدام النطاق الفرعي الذي تم اختياره.

### الإبلاغ عن مشاكل العلامات التجارية أو حقوق الطبع والنشر

يجب أن تتوافق النطاقات الفرعية المخصّصة مع الـ
[بنود خدمة Google](https://policies.google.com/terms?hl=ar). [إذا لاحظت عنوان URL مخصّصًا ينتهك علامة تجارية أو يستخدم اسمًا محميًا بحقوق الطبع والنشر بدون إذن، يمكنك الإبلاغ عنه باستخدام أداة حلّ المشاكل القانونية من Google.](https://support.google.com/legal/troubleshooter/1114905?hl=ar)

## النشر العادي

مع تطوّر تطبيقاتك، قد تحتاج إلى إمكانات تتجاوز Starter Tier، مثل حصص أعلى أو موارد حوسبة أكبر أو منتجات Google Cloud أخرى غير متاحة في Starter Tier. للاستفادة من هذه الإمكانات، يمكنك تحويل مشروعك المُدار بالكامل في Starter Tier إلى مشروع Google Cloud عادي.

يضمن ذلك إمكانية التوسّع بسلاسة بدون فقدان التقدّم الذي أحرزته. اتّبِع الخطوات لـ
[إنشاء حساب فوترة على Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=ar#create-new-billing-account)، و
قبول بنود خدمة Google Cloud العادية رسميًا، و
[الترقية إلى مشروع Google Cloud عادي](https://docs.cloud.google.com/docs/starter-tier?hl=ar#upgradee).
لمزيد من المعلومات، يُرجى الاطّلاع على مقالة
[إعداد الحسابات المدفوعة](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ar#paid-setup).

لمزيد من المعلومات عن مستويات الفوترة، يُرجى الاطّلاع على مقالة [الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar).

## حذف تطبيقك

إذا لم تعُد بحاجة إلى تطبيقك، يمكنك حذفه في Google AI Studio باتّباع هذه التعليمات:

1. في Google AI Studio، انتقِل إلى صفحة "
   [التطبيقات](https://aistudio.google.com/app/apps?hl=ar)".
2. في القائمة اليمنى، انقر على **التطبيقات**.
3. مرِّر المؤشر فوق التطبيق الذي تريد حذفه.
4. انقر على رمز سلة المهملات على الجانب الأيسر من الصف لإزالة التطبيق.

## الخطوات التالية

- مزيد من المعلومات عن
  [Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier?hl=ar).
- مزيد من المعلومات عن [الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar) في Gemini API

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-10 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-10 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
