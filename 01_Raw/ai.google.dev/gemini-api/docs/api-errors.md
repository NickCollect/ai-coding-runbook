---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=ar
fetched_at: 2026-08-24T02:28:11.308780+00:00
title: "\u0623\u062e\u0637\u0627\u0621 \u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# أخطاء واجهة برمجة التطبيقات

تقدّم هذه الصفحة مرجعًا لجميع رموز الخطأ في Interactions API، وتصف تنسيق استجابة الخطأ، وتوضّح كيفية عرض واجهة برمجة التطبيقات للأخطاء لأنواع الطلبات المختلفة.

## رموز الخطأ العادية في واجهة برمجة التطبيقات

تتطابق رموز الخطأ العامة على مستوى الطلب مع رموز حالة HTTP العادية.
استخدِم حقل `code` في منطق تطبيقك للتعامل مع الأخطاء آليًا.

| الرمز | حالة HTTP | الوصف | الإجراء المقترَح |
| --- | --- | --- | --- |
| `invalid_request` | 400 Bad Request | الطلب غير مكتمل أو يحتوي على مَعلمات غير صالحة. | راجِع الإدخالات في [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar). |
| `parameter_unknown` | 400 Bad Request | يحتوي الطلب على مَعلمة غير معروفة. | أزِل المَعلمة غير المعروفة وأعِد المحاولة. |
| `authentication` | ‫401 غير مصرّح به | مفتاح واجهة برمجة التطبيقات غير متوفّر أو غير صالح. | أثبِت ملكية [مفتاح واجهة برمجة التطبيقات](https://ai.google.dev/gemini-api/docs/api-key?hl=ar). |
| `permission_denied` | 403 Forbidden | لا يملك مفتاح واجهة برمجة التطبيقات إذن الوصول إلى هذا المورد. | راجِع أذونات مفتاح واجهة برمجة التطبيقات وإذن الوصول إلى المشروع. |
| `not_found` | ‫404 لم يتم العثور على الصفحة | لم يتم العثور على المورد المطلوب. | راجِع مسار المورد والمَعلمات. |
| `model_not_found` | ‫404 لم يتم العثور على الصفحة | لم يتم العثور على النموذج المحدّد. | راجِع اسم النموذج أو استخدِم نموذجًا مختلفًا. |
| `rate_limit_exceeded` | 429 Too Many Requests | تجاوزت الحدّ الأقصى لعدد الطلبات أو الرموز في الدقيقة أو الثانية. | انتظِر وأعِد المحاولة باستخدام خوارزمية الرقود الأسي الثنائي. |
| `quota_exceeded` | 429 Too Many Requests | تجاوزت الحصة اليومية. | انتظِر إلى حين إعادة ضبط الحصة أو اطلب زيادة الحصة. |
| `cancelled` | 499 Client Closed Request | ألغى العميل الطلب قبل اكتماله. | لا يلزم اتخاذ أي إجراء. يعني هذا عادةً أنّ العميل قد قطع الاتصال. |
| `api_error` | 500 Internal Server Error | حدث خطأ غير متوقَّع على الخادم. | أعِد محاولة الطلب. في حال استمرار المشكلة، يُرجى التواصل مع فريق الدعم. |
| `service_unavailable` | ‫503 الخدمة غير متاحة | هناك زيادة مؤقتة في التحميل على الخدمة أو أنّها معطّلة. | انتظِر وأعِد المحاولة باستخدام خوارزمية الرقود الأسي الثنائي. |

## رموز حظر الإنشاء

تشير رموز الخطأ هذه إلى أنّ السياسة أو إعدادات الأمان أو قيود المحتوى حظرت ردّ النموذج. عند تلقّي أحد هذه الرموز، عدِّل الإدخال وأعِد المحاولة.

| الرمز | الوصف |
| --- | --- |
| `safety` | حظرت انتهاكات إعدادات الأمان (المحتوى الضار) الطلب. |
| `recitation` | حظرت قيود حقوق الطبع والنشر أو قيود التلاوة الطلب. |
| `language` | حظرت لغة غير متاحة الطلب. |
| `prohibited_content` | حظرت إرشادات المحتوى المحظور الطلب. |
| `spii` | حظرت قيود المعلومات الحساسة التي تكشف عن الهوية الطلب. |
| `blocklist` | حظرت المصطلحات المحظورة في قائمة الحظر الطلب. |
| `image_safety` | حظرت انتهاكات إعدادات الأمان إنشاء الصور. |
| `image_prohibited_content` | حظرت إرشادات المحتوى المحظور إنشاء الصور. |
| `image_recitation` | حظرت قيود حقوق الطبع والنشر أو قيود التلاوة إنشاء الصور. |
| `image_other` | حظرت أسباب غير محدّدة إنشاء الصور. |
| `content_blocked` | حظرت سياسة غير محدّدة الطلب. |

## رموز خطأ الإنشاء

تشير رموز الخطأ هذه إلى مشكلة هيكلية في الردّ الذي أنشأه النموذج (مثل استدعاء دالة غير مكتمل أو استدعاء أداة غير معلَن عنه).

| الرمز | الوصف |
| --- | --- |
| `malformed_function_call` | أنشأ النموذج استدعاء دالة تعذّر تحليله. |
| `malformed_tool_call` | أنشأ النموذج استدعاء أداة تعذّر تحليله. |
| `unexpected_tool_call` | استدعى النموذج أداة لم يتم الإعلان عنها في الطلب. |
| `no_image` | تعذّر على النموذج إنشاء صورة. |
| `too_many_tool_calls` | أنشأ النموذج عددًا من استدعاءات الأدوات يتجاوز الحدّ المسموح به. |
| `missing_thought_signature` | لا يحتوي الردّ على توقيع الفكرة المطلوب. |

## تنسيق استجابة الخطأ

تعرض جميع الأخطاء من Interactions API كائن `error` يحتوي على `code` و`message`. على سبيل المثال، يؤدي تمرير نوع أداة غير متاح إلى عرض:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `code` | سلسلة | رمز خطأ يمكن قراءته آليًا بتنسيق `snake_case` |
| `message` | سلسلة | وصف يمكن لشخص عادي قراءته لما حدث من خطأ |

## كيفية عرض الأخطاء

تعرض واجهة برمجة التطبيقات الأخطاء بشكل مختلف حسب ما إذا كنت تُرسِل طلب HTTP عاديًا أو طلب بث (SSE).

### طلبات HTTP العادية

بالنسبة إلى الطلبات العادية (غير طلبات البث)، تضبط واجهة برمجة التطبيقات رمز حالة استجابة HTTP (مثل `400 Bad Request` أو `401 Unauthorized` أو `429 Too Many Requests`) وتعرض كائن `error` في نص استجابة JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### طلبات البث (SSE)

بالنسبة إلى طلبات البث (`stream: true`)، تُرسِل واجهة برمجة التطبيقات أحداث الخطأ عبر بث Server-Sent Events (SSE) مع ضبط `event_type` على `"error"`. يحتوي حقل `error` على البنية نفسها لـ `code` و`message`:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

للاطّلاع على مخطط حدث SSE الكامل، يُرجى مراجعة [مرجع Interactions API](https://ai.google.dev/api/interactions-api?hl=ar).

## الخطوات التالية

- [تحديد مشاكل واجهة برمجة التطبيقات وحلّها](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ar): يمكنك حلّ المشاكل الشائعة وسيناريوهات الأخطاء.
- [الحدود القصوى لمعدّل الطلبات](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar): يمكنك التعرّف على الحدود القصوى للطلبات وكيفية التعامل مع الحصص.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
