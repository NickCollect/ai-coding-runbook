---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar
fetched_at: 2026-05-25T05:28:44.957622+00:00
title: "\u0625\u0639\u062f\u0627\u062f \u0645\u0633\u0627\u0639\u062f \u0627\u0644\u062a\u0631\u0645\u064a\u0632 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini MCP \u0648\"\u0627\u0644\u0645\u0647\u0627\u0631\u0627\u062a\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إعداد مساعد الترميز باستخدام Gemini MCP و"المهارات"

تتسم أدوات المساعدة في البرمجة المستندة إلى الذكاء الاصطناعي بالقوة، ولكن لها حدود، إذ إنّ بيانات التدريب تتوقف عند تاريخ معيّن، ما يؤدي إلى عدم توفّر ميزات وتغييرات جديدة في واجهة برمجة التطبيقات. بدون الوصول إلى مستندات خاصة بـ Gemini، قد تقترح البرامج الآلية أنماطًا عامة بدلاً من أساليب محسّنة.

لإبقاء مساعد الترميز على اطّلاع بآخر التعديلات على Gemini API وطريقة استخدامه المقترَحة، ننصحك بإعداد **Gemini Docs MCP** وتحسين بيئة التطوير باستخدام **مهارات Gemini API**. وعلى الرغم من إمكانية استخدام هذه الأدوات بشكل مستقل، فإنّها مصمّمة للعمل معًا لتوفير تغطية كاملة.

## ربط حزمة MCP الخاصة بـ "مستندات Gemini"

يستضيف Gemini خادمًا عامًا لبروتوكول سياق النموذج (MCP) على
`https://gemini-api-docs-mcp.dev`. يضمن ربط وكيل الترميز بهذا الخادم إمكانية وصول جميع الطلبات إلى أحدث واجهات برمجة التطبيقات وتحديثات الرموز البرمجية وأمثلة الإعدادات المثالية.

نفِّذ الأمر التالي في الوحدة الطرفية أو جذر المشروع الخاصَّين بالوكيل لتثبيت الخادم:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

يضيف هذا الخادم وظيفة `search_documentation` يمكن أن يستخدمها الوكيل لاسترداد تعريفات واجهة برمجة التطبيقات وأنماط الدمج في الوقت الفعلي من ملفات مستندات Gemini الرسمية.

## إضافة مهارات تطوير واجهات برمجة التطبيقات

توفّر المهارات **قواعد وأفضل الممارسات المضمّنة** (مثل فرض استخدام الإصدارات الصحيحة من حزمة تطوير البرامج (SDK) والنماذج الحالية) مباشرةً في سياق مساعدك. تعمل المهارة مع خدمة MCP في Gemini Docs: إذا كان لديك كلتا الخدمتين مثبّتتَين، تستخدم المهارة خدمة MCP للحصول على المستندات، ولكن حتى بدون تثبيت MCP، ستسترد المهارة `llms.txt` من `ai.google.dev` كإجراء احتياطي.

لتثبيت هذه المهارات، يمكنك استخدام إحدى الأدوات المتوافقة التالية. يتم توفير تعليمات التثبيت لكليهما أسفل كل وحدة مهارات:

- ‫**[skills.sh](https://skills.sh)**: يُنصح به. المعيار المفتوح لسلوكيات الوكلاء القابلة للنقل
- **[Context7](https://context7.com)**: متاح للمستخدمين الذين يستفيدون من منظومة Context7 المتكاملة.

### gemini-api-dev

المهارة الأساسية لتطوير Gemini للأغراض العامة توفّر هذه المهارة مستندات وأفضل الممارسات بشأن ما يلي:

- توجيه الطلبات إلى النماذج الحالية (مثل Gemini 3.1 Pro/Flash) وتجنُّب النماذج المتوقّفة
- إنشاء الطلبات المتعددة الوسائط، واستدعاء الدوال، والمخرجات المنظَّمة، وأنماط الدمج الشائعة

#### التثبيت باستخدام skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### التثبيت باستخدام Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

مهارة إنشاء تطبيقات ذكاء اصطناعي حواري في الوقت الفعلي باستخدام واجهة برمجة التطبيقات Gemini Live توفّر هذه المهارة مستندات وأفضل الممارسات بشأن ما يلي:

- اتصالات WebSocket للبث بزمن استجابة منخفض
- بث الصوت والفيديو والنص
- رصد النشاط الصوتي وإمكانية مقاطعة المساعد

#### التثبيت باستخدام skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### التثبيت باستخدام Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

مهارة إنشاء تطبيقات باستخدام
[واجهة Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) ‫Interactions API هي واجهة موحّدة للتفاعل مع نماذج ووكلاء Gemini، وهي مصمَّمة للتطبيقات المستندة إلى الوكلاء. تتضمّن هذه المهارة ما يلي:

- إنشاء النصوص والمحادثات المتعددة الجولات والبث
- استدعاء الدوال والنتائج المنظَّمة وإنشاء الصور
- التنفيذ في الخلفية وعملاء Deep Research
- إدارة حالة المحادثة من جهة الخادم
- أنماط حِزم تطوير البرامج (SDK) في Python وTypeScript

#### التثبيت باستخدام skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### التثبيت باستخدام Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## التحقق من التثبيت

بعد التثبيت، تأكَّد من أنّ مساعد الترميز يمكنه الاتصال بخادم MCP في "مستندات Gemini" واستخدام المهارات المثبَّتة.

### 1. التحقّق من سلوك الوكيل

أكثر طريقة موثوقة للتحقّق هي أن تطرح على الوكيل سؤالاً فنيًا حول Gemini API.

**الطلب:** "كيف يمكنني استخدام التخزين المؤقت للسياق مع Gemini API؟"

عند إعداد ميزة "التحقّق بخطوتين" بنجاح، سيحدث ما يلي:

- **تقديم رمز برمجي دقيق**: يمكنك الرجوع إلى طرق Gemini محدّدة، مثل `cacheContent` أو `cachedContents.create` من أحدث نقاط النهاية.
- **استخدام أداة MCP**: إثبات أنّها مرتبطة **بخادم MCP في Gemini Docs** أو تستخدم أداة `search_documentation` لاسترداد البيانات
- **استدعاء المهارات المحمَّلة**: عرض مؤشر يفيد بأنّه "يتم استخدام المهارة: gemini-api-dev" (في حال الاعتماد على برنامج تضمين ثانوي)

### 2. التحقّق من البيانات والأدوات

إذا قدّم الوكيل ردًا عامًا أو عاديًا، استخدِم أوامر Discovery أو Status المحدّدة لبيئتك للتأكّد من تحميل Docs MCP أو المهارة في الذاكرة.

| البيئة | تأكيد حساب MCP | إثبات المهارات |
| --- | --- | --- |
| **Claude Code** | اكتب `/mcp` في نافذة الوحدة الطرفية لعرض الخوادم النشطة وأدوات `search_documentation`. | اكتب `/skills` في نافذة الأوامر لعرض جميع ملفات البيان النشطة. |
| **المؤشر** | انتقِل إلى **الإعدادات > الميزات > MCP**. تأكَّد من أنّ الخادم "متّصل". | افتح **الإعدادات > القواعد**. تأكَّد من ظهور المهارة ضمن "يقرّر الوكيل". |
| **Antigravity** | تحقَّق من الشريط الجانبي **التخصيصات > عمليات الربط** لمعرفة حالة "برنامج شركاء المحتوى". | اكتب `/skills list` أو ضَع علامة في الشريط الجانبي **التخصيصات > القواعد**. |
| **Gemini CLI** | تشغيل `gemini mcp list` أو استخدام `/mcp list` | نفِّذ `gemini skills list` أو استخدِم الأمر `/skills` الذي يبدأ بشرطة مائلة أثناء الجلسة. |
| **Copilot** | اكتب `@gemini /mcp` لإدراج أدوات ربط البيانات النشطة. | اكتب `@gemini /skills` (أو `/skills`) لعرض الإضافات النشطة. |

## تحديد المشاكل وحلّها

إذا كان وكيلك يقدّم معلومات عامة فقط أو لا يتعرّف على طرق خاصة بـ Gemini، تحقَّق مما يلي:

### لم يكتشف الوكيل المهارة

يفهرس معظم الوكلاء المهارات عند بدء التشغيل فقط.

**الحلّ:** أعِد تشغيل بيئة التطوير المتكاملة (Cursor أو VS Code) بالكامل أو اخرج من الوكيل المستند إلى الجهاز الطرفي (Claude Code) وأعِد فتحه.

### النزاعات العالمية والمحلية

إذا تم التثبيت باستخدام العلامة `--global`، قد يتجاهل الوكيل هذه العلامة لصالح القواعد الخاصة بالمشروع.

**الحلّ:** جرِّب تثبيت المهارة مباشرةً في جذر مشروعك بدون العلامة العامة:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## الموارد

- [مهارات Gemini API على GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar)
- [Quickstart](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar)
- [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
