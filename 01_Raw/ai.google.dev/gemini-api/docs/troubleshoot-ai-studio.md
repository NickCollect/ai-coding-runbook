---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=ar
fetched_at: 2026-11-02T07:23:37.404994+00:00
title: "\u062a\u062d\u062f\u064a\u062f \u0627\u0644\u0645\u0634\u0627\u0643\u0644 \u0648\u062d\u0644\u0651\u0647\u0627 \u0641\u064a Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تحديد المشاكل وحلّها في Google AI Studio

توفّر هذه الصفحة اقتراحات لتحديد المشاكل وحلّها في Google AI Studio إذا واجهت أي مشاكل.

## فهم أخطاء "403 الوصول محظور"

إذا ظهرت لك رسالة الخطأ "403: تم حظر الوصول"، يعني ذلك أنّك تستخدم Google AI Studio بطريقة لا تتوافق مع [بنود الخدمة](https://ai.google.dev/terms?hl=ar). من الأسباب الشائعة لذلك هو
عدم إقامتك في [منطقة معتمَدة](https://ai.google.dev/available_regions?hl=ar).

## إثبات السن المسموح به لاستخدام حسابك على Google

يجب ألّا يقل عمرك عن 18 عامًا للتمكُّن من استخدام Google AI Studio. قد تتم إعادة توجيهك إلى هذا
القسم أثناء محاولة فتح [Google AI Studio](https://aistudio.google.com/?hl=ar).
في هذه الحالة، تأكَّد من أنّ حسابك على Google يستوفي السن المسموح به:

- **التحقّق من تاريخ ميلادك:** تأكَّد من أنّ تاريخ ميلادك مضبوط على 18 عامًا أو أكثر في
  [إعدادات تاريخ الميلاد](https://myaccount.google.com/birthday?hl=ar).
- **إثبات عمرك:** يجب إكمال عملية [إثبات العمر](https://myaccount.google.com/age-verification?hl=ar) في حسابك على Google. للاطّلاع على خيارات إثبات العمر، يُرجى مراجعة مقالة [إثبات عمرك في حسابك على Google](https://support.google.com/accounts/answer/10071085?hl=ar).
- **مطابقة تاريخ الميلاد في مستند التعريف:** إذا أثبتّم عمركم باستخدام مستند تعريف، تحقَّقوا من إعدادات حسابكم. تأكَّد من أنّ [تاريخ ميلادك](https://myaccount.google.com/birthday?hl=ar) يتطابق مع التاريخ الوارد في مستند تعريف هويتك.
- **حسابات Google Workspace:** بالنسبة إلى حسابات Google Workspace for Education،
  يُرجى التواصل مع المشرف. ويمكنه تأكيد ما إذا تم تصنيف حسابك على أنّه يخصّ مستخدمًا يبلغ من العمر 18 عامًا أو أكثر. لمزيد من التفاصيل، يُرجى الاطّلاع على مقالة
  [الوصول إلى Google AI Studio باستخدام حسابك على Workspace](https://ai.google.dev/gemini-api/docs/workspace?hl=ar).

## حلّ مشكلة الردود التي تشير إلى عدم توفّر محتوى في Google AI Studio

تظهر رسالة warning **No Content** (لا يتوفّر محتوى) على
Google AI Studio إذا تم حظر المحتوى لأي سبب. للاطّلاع على مزيد من التفاصيل،
مرِّر المؤشر فوق **بلا محتوى** وانقر على
warning **الأمان**.

إذا تم حظر الردّ بسبب [إعدادات الأمان](https://ai.google.dev/docs/safety_setting?hl=ar)
وكنت قد أخذت في الاعتبار [مخاطر الأمان](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ar) لحالة الاستخدام، يمكنك
تعديل
[إعدادات الأمان](https://ai.google.dev/docs/safety_setting?hl=ar#safety_settings_in_makersuite)
للتأثير في الردّ الذي يتم عرضه.

إذا تم حظر الردّ ولكن ليس بسبب إعدادات الأمان، قد يكون الطلب أو الردّ مخالفًا [لبنود الخدمة](https://ai.google.dev/terms?hl=ar) أو غير متوافق معها.

## الاطّلاع على استخدام الرموز المميّزة والحدود القصوى

عند فتح طلب، يعرض زر **معاينة النص** في أسفل الشاشة الرموز المميّزة الحالية المستخدَمة لمحتوى طلبك والحد الأقصى لعدد الرموز المميّزة للنموذج المستخدَم.

## أذونات Google Cloud IAM في AI Studio

يحتاج أعضاء مشروع Google Cloud إلى أذونات محدّدة في "إدارة الهوية وإمكانية الوصول" (IAM) لتنفيذ إجراءات في Google AI Studio. لمزيد من المعلومات حول هذه الهويات، يُرجى الاطّلاع على [نظرة عامة على مستخدمي "إدارة الهوية وإمكانية الوصول"](https://docs.cloud.google.com/iam/docs/principals-overview?hl=ar).

يحصل المستخدمون الذين لديهم دور **محرِّر** أو **مالك** في مشروع Google Cloud المرتبط على أذونات كاملة لعرض لوحات البيانات وإدارة مفاتيح Gemini API. يمكن للمستخدمين الذين لديهم دور **المُشاهد** الاطّلاع على لوحات البيانات ومفاتيح واجهة برمجة التطبيقات، ولكن لا يمكنهم إنشاؤها أو تعديلها أو حذفها.

لمزيد من التحكّم الدقيق، يُرجى الرجوع إلى الجدول التالي للاطّلاع على الأذونات المحدّدة المطلوبة لكل ميزة في AI Studio. للحصول على تعليمات حول كيفية منح هذه الأذونات، يُرجى الاطّلاع على مقالة [منح إذن الوصول إلى الموارد وتغييره وإبطاله](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=ar) في مستندات Google Cloud.

| ميزة AI Studio | أذونات "إدارة الهوية وإمكانية الوصول" المطلوبة | متطلبات إضافية |
| --- | --- | --- |
| **مشروع بحث** (استيراد المشاريع) | `resourcemanager.projects.get` |  |
| **إعادة تسمية المشروع** | `resourcemanager.projects.update` |  |
| **عرض فئة الحصة** | لا ينطبق |  |
| **إنشاء مفتاح واجهة برمجة تطبيقات** | أن يكون لديك أذونات **مشروع البحث**، بالإضافة إلى:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **إدراج مفاتيح واجهة برمجة التطبيقات** | أن يكون لديك أذونات **مشروع البحث**، بالإضافة إلى:  `apikeys.keys.list` `serviceusage.services.get` | يجب أن يكون مشروع Google Cloud مفعَّلاً فيه [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=ar). |
| **إعادة تسمية مفاتيح واجهة برمجة التطبيقات** | `apikeys.keys.update` |  |
| **حذف مفاتيح واجهة برمجة التطبيقات** | `apikeys.keys.delete` |  |
| **لوحة بيانات الاستخدام** | أن يكون لديك أذونات **مشروع البحث**، بالإضافة إلى:  `monitoring.timeSeries.list` |  |
| **لوحة بيانات الحدّ الأقصى للمعدّل** | أن يكون لديك أذونات **لوحة بيانات الاستخدام**، وأن:  `cloudquotas.quotas.get` |  |
| **الإنفاق (حدّ الفوترة)** | ‫`billing.resourceCosts.get` (للاطّلاع على الإنفاق) `billing.resourcebudgets.read` (للاطّلاع على الحدّ الأقصى) `billing.resourcebudgets.write` (لضبط الحدّ الأقصى) |  |
| **لوحة بيانات الفوترة** | `billing.accounts.get` |  |

### عمليات التحقّق الأخرى من الوصول

بالإضافة إلى أذونات Google Cloud IAM، يُجري AI Studio أيضًا عمليات تحقّق من الأمان والامتثال. قد يظهر لك خطأ `PERMISSION_DENIED` أو خطأ في قيود الوصول في واجهة AI Studio أو في الردود من واجهة برمجة التطبيقات إذا لم تستوفِ المتطلبات التالية:

- **عمليات التحقّق من الأمان:** يجب أن يجتاز طلبك عمليات التحقّق من الأمان الآلية.
- **بنود الخدمة:** يجب قبول "بنود خدمة Google" و"بنود الخدمة الإضافية الخاصة بالذكاء الاصطناعي التوليدي".
- **منطقة معتمَدة:** يجب أن تكون مقيمًا في [منطقة معتمَدة](https://ai.google.dev/gemini-api/docs/available-regions?hl=ar).
- **السن المسموح به:** يجب أن تستوفي [السن المسموح به](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=ar#age-requirements) (18 عامًا أو أكثر) في حسابك على Google.
- **الثقة والأمان:** يجب ألا يتم الإبلاغ عن مشروع على السحابة الإلكترونية من Google Cloud بسبب إساءة الاستخدام.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
