---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=ar
fetched_at: 2026-06-15T06:32:51.204125+00:00
title: "\u0627\u0644\u0646\u0634\u0631 \u0645\u0646 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# النشر من Google AI Studio

يتيح لك Google AI Studio نشر تطبيقاتك المتكاملة مباشرةً من &quot;وضع الإنشاء&quot;. ويوفّر ذلك مسارًا سريعًا من النموذج الأوّلي إلى بيئة إنتاج مُدارة وقابلة للتوسيع.

## خيارات النشر

لتنفيذ تطبيقك من &quot;وضع الإنشاء&quot; في AI Studio، تعتمد المتطلبات على الفئة التي تستخدمها:

- [**فئة Google Cloud Starter**](https://docs.cloud.google.com/docs/starter-tier?hl=ar):
  تتيح لك نشر ما يصل إلى تطبيقَين كاملَي الميزات بدون الحاجة إلى إعداد مشروع على السحابة الإلكترونية أو حساب فوترة على Google Cloud.
- **عملية النشر العادية**: تتطلّب مشروعًا على Google Cloud مرتبطًا بحسابك على AI Studio وتفعيل الفوترة في هذا المشروع.

## لمحة عن "المستوى المبتدئ"

توفّر &quot;فئة المبتدئين&quot; في Google Cloud مسارًا مبسطًا لنشر التطبيقات على Google Cloud مباشرةً من Google AI Studio بدون الحاجة إلى إعداد بيئة Google Cloud كاملة أو حساب فوترة.

يؤدي كل عملية نشر في Google AI Studio إلى إنشاء خدمة مقابلة في Cloud Run. تنطبق القيود التالية على الخدمات التي يتم نشرها في Google AI Studio باستخدام "حزمة المبتدئين":

- يمكنك نشر ما يصل إلى خدمتَين.
- يتم نشر خدماتك في [منطقة واحدة من مناطق Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=ar).

## خطوات نشر المستوى المبتدئ

بعد تصميم تطبيقك في "وضع الإنشاء"، يمكنك نشره باستخدام "الفئة المبتدئة" باتّباع الخطوات التالية:

1. انقر على زر **نشر** في أعلى يسار الصفحة.
2. انقر على **البدء**.
3. انقر على **نشر التطبيق**.

بعد اكتمال عملية النشر، يوفّر AI Studio عنوان URL في Cloud Run يمكنك من خلاله الوصول إلى تطبيقك المباشر.

## النشر العادي

مع تطوّر تطبيقاتك، قد تحتاج إلى إمكانات تتجاوز تلك المتاحة في "الفئة المبتدئة"، مثل حصص أكبر أو موارد حوسبة إضافية أو منتجات أخرى من Google Cloud غير متوفّرة في "الفئة المبتدئة". للاستفادة من هذه الإمكانات، يمكنك تحويل مشروعك في "فئة المبتدئين" المُدارة بالكامل إلى مشروع عادي على Google Cloud.

يضمن ذلك إمكانية التوسّع بسلاسة بدون فقدان مستوى تقدّمك. اتّبِع الخطوات التالية من أجل
[إنشاء حساب فوترة على Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=ar#create-new-billing-account)
والموافقة رسميًا على بنود خدمة Google Cloud العادية
و[الترقية إلى مشروع Google Cloud عادي](https://docs.cloud.google.com/docs/starter-tier?hl=ar#upgradee).
لمزيد من المعلومات، يُرجى الاطّلاع على
[إعداد الحسابات المدفوعة](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ar#paid-setup).

لمزيد من المعلومات عن فئات الفوترة، يُرجى الاطّلاع على [الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar).

## حذف طلبك

إذا لم تعُد بحاجة إلى تطبيقك، يمكنك حذفه في Google AI Studio باتّباع التعليمات التالية:

1. في Google AI Studio، انتقِل إلى
   [صفحة "التطبيقات"](https://aistudio.google.com/app/apps?hl=ar).
2. في القائمة اليمنى، انقر على **التطبيقات**.
3. ضع المؤشر فوق التطبيق الذي تريد حذفه.
4. انقر على رمز سلة المهملات على الجانب الأيسر من الصف لحذف التطبيق.

## الخطوات التالية

- [مزيد من المعلومات حول "فئة المبتدئين" في Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=ar)
- [مزيد من المعلومات حول الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar) في Gemini API

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-16 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-16 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
