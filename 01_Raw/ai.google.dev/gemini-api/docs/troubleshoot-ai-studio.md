---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=ar
fetched_at: 2026-07-20T04:34:00.438352+00:00
title: "\u062a\u062d\u062f\u064a\u062f \u0627\u0644\u0645\u0634\u0627\u0643\u0644 \u0648\u062d\u0644\u0651\u0647\u0627 \u0641\u064a Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تحديد المشاكل وحلّها في Google AI Studio

توفّر هذه الصفحة اقتراحات لتحديد المشاكل في Google AI Studio وحلّها في حال مواجهة أي منها.

## فهم أخطاء "403 Access Restricted" (الوصول محظور)

إذا ظهر لك الخطأ "403 Access Restricted" (الوصول محظور)، يعني ذلك أنّك تستخدم Google AI Studio بطريقة لا تتّبع [بنود الخدمة](https://ai.google.dev/terms?hl=ar). أحد الأسباب الشائعة هو
أنّك لست مقيمًا في منطقة [تتوفّر فيها الخدمة](https://ai.google.dev/available_regions?hl=ar).

## حلّ مشكلة الردود "No Content" (لا يوجد محتوى) في Google AI Studio

تظهر رسالة warning **No Content** على
Google AI Studio إذا تم حظر المحتوى لأي سبب كان. للاطّلاع على مزيد من التفاصيل،
مرِّر المؤشر فوق **No Content** وانقر
warning على **Safety**.

إذا تم حظر الردّ بسبب [إعدادات الأمان](https://ai.google.dev/docs/safety_setting?hl=ar) و
كنت قد أخذت في الاعتبار [المخاطر الأمنية](https://ai.google.dev/docs/safety_guidance?hl=ar) لحالة الاستخدام، يمكنك
تعديل
[إعدادات الأمان](https://ai.google.dev/docs/safety_setting?hl=ar#safety_settings_in_makersuite)
للتأثير في الردّ الذي يتم عرضه.

إذا تم حظر الردّ ولكن ليس بسبب إعدادات الأمان، قد يكون الطلب أو
الردّ مخالفًا لـ [بنود الخدمة](https://ai.google.dev/terms?hl=ar) أو غير متوافق معها.

## التحقّق من استخدام الرموز وحدودها

عند فتح طلب، يعرض الزر **Text Preview** (معاينة النص) في أسفل الشاشة الرموز الحالية المستخدَمة لمحتوى طلبك والحد الأقصى لعدد الرموز للنموذج المستخدَم.

## أذونات Google Cloud IAM لـ AI Studio

يحتاج أعضاء مشروع Google Cloud إلى أذونات محدّدة في "إدارة الهوية وإمكانية الوصول" (IAM) لتنفيذ الإجراءات في Google AI Studio. لمزيد من المعلومات عن هذه الهويات، يُرجى الاطّلاع على [نظرة عامة على الجهات الرئيسية في IAM](https://cloud.google.com/iam/docs/principals?hl=ar).

يملك المستخدمون الذين لديهم دورا **محرِّر** أو **مالك** في مشروع Google Cloud المرتبط أذونات كاملة لعرض لوحات البيانات وإدارة مفاتيح Gemini API. يمكن للمستخدمين الذين لديهم دور **مُشاهد** عرض لوحات البيانات ومفاتيح واجهة برمجة التطبيقات، ولكن لا يمكنهم إنشاءها أو تعديلها أو حذفها.

للتحكّم بشكل أدق، يُرجى الرجوع إلى الجدول التالي للاطّلاع على الأذونات المحدّدة المطلوبة لكل ميزة من ميزات AI Studio. للحصول على تعليمات حول كيفية منح هذه الأذونات، يُرجى الاطّلاع على [منح إذن الوصول إلى الموارد وتغييره وإبطاله](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=ar) في مستندات Google Cloud.

| ميزة AI Studio | أذونات IAM المطلوبة | متطلبات إضافية |
| --- | --- | --- |
| **البحث عن مشروع** (استيراد المشاريع) | `resourcemanager.projects.get` |  |
| **إعادة تسمية المشروع** | `resourcemanager.projects.update` |  |
| **عرض مستوى الحصة** | لا ينطبق |  |
| **إنشاء مفتاح واجهة برمجة التطبيقات** | يجب أن يكون لديك أذونات **البحث عن مشروع** ، بالإضافة إلى:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **عرض قائمة بمفاتيح واجهة برمجة التطبيقات** | يجب أن يكون لديك أذونات **البحث عن مشروع** ، بالإضافة إلى:  `apikeys.keys.list` `serviceusage.services.get` | يجب تفعيل [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=ar) في مشروع Google Cloud. |
| **إعادة تسمية مفاتيح واجهة برمجة التطبيقات** | `apikeys.keys.update` |  |
| **حذف مفاتيح واجهة برمجة التطبيقات** | `apikeys.keys.delete` |  |
| **لوحة بيانات الاستخدام** | يجب أن يكون لديك أذونات **البحث عن مشروع** ، بالإضافة إلى:  `monitoring.timeSeries.list` |  |
| **لوحة بيانات الحدّ الأقصى لمعدّل الطلبات** | يجب أن يكون لديك أذونات **لوحة بيانات الاستخدام** ، بالإضافة إلى:  `cloudquotas.quotas.get` |  |
| **الإنفاق (الحدّ الأقصى للفوترة)** | `billing.resourceCosts.get` (لعرض الإنفاق) `billing.resourcebudgets.read` (لعرض الحدّ الأقصى) `billing.resourcebudgets.write` (لضبط الحدّ الأقصى) |  |
| **لوحة بيانات الفوترة** | `billing.accounts.get` |  |

### عمليات التحقّق الأخرى من إمكانية الوصول

بالإضافة إلى أذونات Google Cloud IAM، يجري AI Studio أيضًا عمليات تحقّق من الأمان والامتثال. قد يظهر لك الخطأ `PERMISSION_DENIED` أو خطأ بشأن تقييد الوصول في واجهة AI Studio أو في ردود واجهة برمجة التطبيقات إذا لم تستوفِ المتطلبات التالية:

- **عمليات التحقّق من الأمان:** يجب أن يجتاز طلبك عمليات التحقّق الأمنية الآلية.
- **بنود الخدمة:** يجب قبول بنود خدمة Google وبنود الخدمة الإضافية الخاصة بالذكاء الاصطناعي التوليدي.
- **المنطقة المتوفّرة فيها الخدمة:** يجب أن تكون مقيمًا في [منطقة تتوفّر فيها الخدمة](https://ai.google.dev/gemini-api/docs/available-regions?hl=ar).
- **الثقة والأمان:** يجب ألا يتم وضع علامة على مشروع Google Cloud للإشارة إلى إساءة الاستخدام.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
