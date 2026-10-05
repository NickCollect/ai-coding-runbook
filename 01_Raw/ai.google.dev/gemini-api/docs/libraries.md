---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=ar
fetched_at: 2026-10-05T06:38:52.606032+00:00
title: "\u0645\u0643\u062a\u0628\u0627\u062a Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# مكتبات Gemini API

عند إنشاء تطبيقات باستخدام Gemini API، ننصحك باستخدام **حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي**.
هذه هي المكتبات الرسمية الجاهزة للاستخدام التي نطوّرها ونتولّى صيانتها
لأكثر اللغات شيوعًا. وهي متاحة [لجميع المستخدمين](https://ai.google.dev/gemini-api/docs/libraries?hl=ar#new-libraries) ويتم استخدامها في جميع مستنداتنا وأمثلتنا الرسمية.

إذا كنت تستخدم Gemini API للمرة الأولى، اتّبِع [دليل البدء](https://ai.google.dev/gemini-api/docs/get-started?hl=ar).

## اللغات المتوافقة والتثبيت

تتوفّر حزمة تطوير البرامج من Google للذكاء الاصطناعي التوليدي للغات Python وJavaScript/TypeScript وGo وJava. يمكنك تثبيت مكتبة كل لغة باستخدام أدوات إدارة الحِزم،
أو الانتقال إلى مستودعات GitHub الخاصة بها لمزيد من التفاعل:

### Python

- المكتبة: [`google-genai`](https://pypi.org/project/google-genai)
- مستودع GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- التثبيت: `pip install google-genai`

### JavaScript

- المكتبة: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- مستودع GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- التثبيت: `npm install @google/genai`

### Go

- المكتبة: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- مستودع GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- التثبيت: `go get google.golang.org/genai`

### جافا

- المكتبة: `google-genai`
- مستودع GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- التثبيت: إذا كنت تستخدم Maven، أضِف ما يلي إلى العناصر التابعة:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### #C

- المكتبة: `Google.GenAI`
- مستودع GitHub‏: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- التثبيت: `dotnet add package Google.GenAI`

## متوفر للجمهور العام

اعتبارًا من مايو 2025، أصبحت حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي متاحة للجمهور العام على جميع المنصات المتوافقة، وهي المكتبات المقترَحة للوصول إلى Gemini API.
وهي مستقرة ومتوافقة تمامًا مع الاستخدام في مرحلة الإنتاج، ويتم صيانتها بشكل نشط.
تتيح هذه الأجهزة الوصول إلى أحدث الميزات، وتوفّر أفضل أداء عند استخدامها مع Gemini.

إذا كنت تستخدم إحدى مكتباتنا القديمة، ننصحك بشدة بنقل بياناتك حتى تتمكّن من الاستفادة من أحدث الميزات وتحقيق أفضل أداء عند استخدام Gemini. راجِع قسم [المكتبات القديمة](https://ai.google.dev/gemini-api/docs/libraries?hl=ar#previous-sdks) لمزيد من المعلومات.

## المكتبات القديمة ونقل البيانات

إذا كنت تستخدم إحدى مكتباتنا القديمة، ننصحك [بالانتقال إلى المكتبات الجديدة](https://ai.google.dev/gemini-api/docs/migrate?hl=ar).

لا تتيح المكتبات القديمة الوصول إلى الميزات الحديثة (مثل [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) و[Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar))، وسيتم إيقافها نهائيًا اعتبارًا من 30 تشرين الثاني (نوفمبر) 2025.

تختلف حالة توفّر كل مكتبة قديمة، كما هو موضّح بالتفصيل في الجدول التالي:

| اللغة | المكتبة القديمة | حالة الدعم | المكتبة المقترَحة |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | لم يعُد يتم صيانتها | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | لم يعُد يتم صيانتها | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | لم يعُد يتم صيانتها | `google.golang.org/genai` |
| **Dart وFlutter** | `google_generative_ai` | لم يعُد يتم صيانتها | استخدام [Genkit Dart](https://genkit.dev/docs/dart/get-started/) أو [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | لم يعُد يتم صيانتها | استخدام [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ar) |
| **Android** | `generative-ai-android` | لم يعُد يتم صيانتها | استخدام [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ar) |

**ملاحظة لمطوّري Java:** لم تتوفّر حزمة SDK قديمة للغة Java من Google لواجهة Gemini API، لذا لا يلزم نقل البيانات من مكتبة Google السابقة. يمكنك البدء مباشرةً باستخدام المكتبة الجديدة في قسم [اللغات المتوافقة والتثبيت](#install).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
