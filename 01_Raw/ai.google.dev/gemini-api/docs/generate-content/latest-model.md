---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=ar
fetched_at: 2026-11-02T07:02:01.117781+00:00
title: "\u0645\u0627 \u0627\u0644\u062c\u062f\u064a\u062f \u0641\u064a Gemini 4 Argon\u061f \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)

إرسال ملاحظات

# ما الجديد في Gemini 4 Argon؟

‫Gemini 4 Argon‏ (`gemini-4-argon`) هو نموذجنا الأحدث والأكثر تطورًا. يمكنه الاستدلال لفترة أطول على المشاكل الصعبة للحصول على نتائج أفضل في المهام المعقّدة في الترميز والمهام المستندة إلى الوكلاء والرياضيات والعلوم. يتوفّر Gemini 4 Argon من خلال Gemini API وفي Google AI Studio.

يتيح Gemini 4 Argon حدًا أقصى موحّدًا لعدد الرموز المميّزة في الإدخال والإخراج يبلغ مليون رمز، وفك ترميز طويل يصل إلى مليون رمز، ومستويات تفكير قابلة للتعديل (`low` و`medium` و`high`).

[experiment

تجربة الميزة في AI Studio

أنشِئ تطبيقات من الصفر باستخدام Gemini 4 Argon وAI Studio.](https://aistudio.google.com/apps?model=gemini-4-argon&hl=ar)
[smart\_toy

معرض التطبيقات

استخدِم التطبيقات وأنشئ ريمكسات لها، وكل ذلك من خلال Gemini 4 Argon.](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=ar)
[rocket\_launch

البدء

ابدأ باستخدام Gemini 4 Argon من خلال الطلبات الأولية.](https://aistudio.google.com/learn/gemini-4-argon?hl=ar)

يشرح هذا الدليل الميزات الجديدة في Gemini 4 Argon، والتغييرات في واجهة برمجة التطبيقات، وأمثلة على الرموز البرمجية، وإرشادات نقل البيانات.

## النموذج الجديد

| الطراز | رقم تعريف الطراز | مستوى التفكير التلقائي | الأسعار | الوصف |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | يتوفّر حتى 30 نوفمبر 2026 بسعر تمهيدي يبلغ دولارَين أمريكيَّين لكل مليون رمز إدخال و10 دولار أمريكي لكل مليون رمز إخراج (4 دولار أمريكي لكل مليون رمز إدخال و20 دولار أمريكي لكل مليون رمز إخراج بعد ذلك). لمزيد من التفاصيل، يُرجى الاطّلاع على [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar). | نموذجنا الأكثر تطوّرًا، المصمَّم لحلّ أصعب المشاكل بعمق ودقة في مهام هندسة البرمجيات والعمل المعرفي في العالم الحقيقي. |

## البدء السريع

استخدِم المثال التالي لإرسال طلب إلى `gemini-4-argon` باستخدام الإعداد التلقائي المقترَح `thinking_level` (`medium`) والحدّ الأقصى لعدد الرموز المميّزة في الناتج وهو 64 ألف:

### Python

```
pip install -U "google-genai>=2.30.1"
```

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
    config=types.GenerateContentConfig(
        max_output_tokens=65536,
        thinking_config=types.ThinkingConfig(thinking_level="medium"),
    ),
)

print(response.text)
```

### JavaScript

```
npm install "@google/genai@>=2.29.1"
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-4-argon",
  contents: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
  config: {
    maxOutputTokens: 65536,
    thinkingConfig: {
      thinkingLevel: "medium",
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."}]
    }],
    "generationConfig": {
      "maxOutputTokens": 65536,
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## ما الجديد في Gemini 4 Argon؟

- **حدّ موحّد لرموز الإدخال والإخراج يبلغ مليون رمز:** تشترك رموز الإدخال والتفكير والإخراج في نافذة واحدة تتّسع لمليون رمز، مع حدّ أقصى يبلغ 32 ألف رمز لكل طلب للمكالمات غير المباشرة و64 ألف رمز لكل بث للمكالمات المباشرة.
- **فك ترميز طويل يصل إلى مليون رمز مميّز:** يمكن للنموذج إنشاء ردود تتجاوز الحد الأقصى لكل طلب، بما يصل إلى مليون رمز مميّز مطروحًا منه الإدخال. ستبقى أحدث إصدارات حِزم تطوير البرامج (SDK) للذكاء الاصطناعي التوليدي من Google متاحة لك تلقائيًا.
- **فهم الفيديو المستند إلى الذكاء الاصطناعي الوكيل (متوفّر للجمهور العام):** أصبحت ميزة [فهم الفيديو المستند إلى الذكاء الاصطناعي الوكيل](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar#agentic-video-understanding) متوفّرة الآن للجمهور العام.
- **متاح في "الوكلاء المُدارون":** أصبح [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar) في "الوكلاء المُدارون" في Gemini متوافقًا مع Gemini 4 Argon.

لمزيد من التفاصيل، يُرجى الاطّلاع على [صفحة نموذج Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ar). لمعرفة تفاصيل الأسعار، يُرجى الاطّلاع على [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#gemini-4-argon).

## مخرجات أكبر وفك ترميز طويل

عندما تتطلّب المهمة استدلالاً عميقًا، يمكن لـ Gemini 4 Argon التفكير لفترة أطول والعمل بجهد أكبر لحلّ المسائل الرياضية والعلمية والبرمجية المعقّدة في ردّ واحد.

- **حدّ موحّد لرموز الإدخال والإخراج يبلغ مليون رمز:** يمكن لـ Argon استخدام ما يصل إلى مليون رمز مميّز، مطروحًا منها رموز الإدخال، لعملية التفكير والإخراج معًا.
- **يتم احتساب الرموز المميّزة للتفكير ضمن رصيد `max_output_tokens`:** في المهام الصعبة، يستخدم النموذج قدرًا أكبر من رصيد `max_output_tokens` للوصول إلى إجابة أفضل. استخدِم `thinking_level` للتحكّم في استخدام الرموز المميّزة.
- **الحدود القصوى لكل طلب (64 ألف رمز مميّز للطلبات التي تتضمّن بثًا / 32 ألف رمز مميّز للطلبات التي لا تتضمّن بثًا):** يعرض طلب البث الواحد ما يصل إلى 65,536 رمزًا مميّزًا. يُرجع الطلب الواحد غير المتعلّق بالبث ما يصل إلى 32,768 رمزًا مميزًا، مقارنةً بـ 65,536 في Gemini 3.x. بالنسبة إلى طلبات REST، تكون هذه الحدود القصوى هي أيضًا الإعدادات التلقائية.

تنفّذ أحدث حِزم تطوير البرامج (SDK) للذكاء الاصطناعي التوليدي من Google عملية فك الترميز الطويل تلقائيًا نيابةً عنك. استخدِم الإصدار 2.30.1 من Python `google-genai` أو إصدارًا أحدث، أو الإصدار 2.29.1 من JavaScript `@google/genai` أو إصدارًا أحدث.

في هذه الإصدارات، تكون قيمة `automatic_continuation` هي `True` تلقائيًا، لذا لا تحتاج إلى ضبطها. عند ضبط `max_output_tokens` على قيمة أعلى من الحدّ الأقصى لكل طلب، يواصل `generate_content` و`generate_content_stream` تلقائيًا معالجة الطلبات إلى أن ينتهي النموذج أو يصل إلى `max_output_tokens`، ما يؤدي إلى عرض ردّ واحد مجمّع.

```
response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a complete, rigorous proof of the prime number theorem.",
    config=types.GenerateContentConfig(
        max_output_tokens=262144,
        thinking_config=types.ThinkingConfig(thinking_level="high"),
        automatic_continuation=True,  # Default.
    ),
)
```

لتشغيل التكرار بنفسك، اضبط `automatic_continuation=False`. إذا طلبت REST أو استخدمت حزمة تطوير برامج (SDK) قديمة، ستتوقف الطلبات عند الحد الأقصى لكل طلب. للاطّلاع على معلومات حول تكرار طلبات REST وأُطر العمل التابعة لجهات خارجية واحتساب الرموز المميّزة وحالات استخدام ميزة "فك الترميز الطويل"، يُرجى مراجعة [دليل ميزة "فك الترميز الطويل"](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=ar).

### ضبط الحدود القصوى لرموز الناتج المميّزة

يحدّد `max_output_tokens` إجمالي الرموز المميّزة للتفكير والناتج لعملية إنشاء واحدة، بما في ذلك جميع طلبات المتابعة. اضبطه على قيمة عالية بما يكفي لكي لا يؤدي التفكير إلى اختصار الإجابة. اضبطه على قيمة منخفضة بما يكفي للحدّ من الإنفاق عندما يستهلك طلب صعب كل الرصيد.

يمكنك الاستعانة بالإرشادات التالية كنقطة بداية:

- **المهام العادية:** احتفِظ بالإعداد التلقائي.
- **التطبيقات الحالية التي يقلّ الحدّ الأقصى فيها عن 32 ألفًا:** يجب رفع قيمة `max_output_tokens` إلى 32,768. لاستخدام عدد أقل من الرموز المميّزة، يمكنك خفض قيمة `thinking_level`.
- **المهام التي استخدمت أكثر من 32 ألف رمز مميّز في السابق:** اضبط `max_output_tokens` على 65,536.
- **الاستدلال المعقّد والترميز:** اضبط `max_output_tokens` على 131,072 أو 262,144، بحد أقصى 1,048,576 ناقص الرموز المميّزة للإدخال.

إذا استخدم الطلب كل `max_output_tokens`، فإنه يعرض `finish_reason: "MAX_TOKENS"` ويتضمن `continuation_token`. يمكنك استئنافها أو البدء من جديد.

- **الاستئناف من نقطة التحقّق:** أرسِل الطلب الأصلي مع أحدث `continuation_token` وقيمة أعلى لـ `max_output_tokens`. إذا لم ترفع قيمة `max_output_tokens`، سيعرض الطلب `400 INVALID_ARGUMENT`.
- **البدء من جديد:** أرسِل الطلب الأصلي مع قيمة أعلى لـ `max_output_tokens` وبدون `continuation_token`.

### فهم مستويات التفكير

[مستوى التفكير](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ar) هو عنصر التحكّم الرئيسي في الجودة ووقت الاستجابة واستخدام الرموز المميّزة في Gemini 4 Argon:

| مستوى التفكير | استخدام الرموز المميّزة | حالات الاستخدام |
| --- | --- | --- |
| `low` | أقل عدد من الرموز المميّزة وأقل وقت استجابة | المهام الأبسط والأعمال التي تتأثر بالتكلفة يمكنه أيضًا مساعدتك في مهام التحليل والكتابة التي تتطلّب تفكيرًا بسيطًا. قد تنخفض الجودة في المهام الصعبة. |
| `medium` (تلقائي) | متوازن | يُنصح به لمعظم المهام، بما في ذلك الرموز البرمجية المعقّدة وحالات الاستخدام التي تتطلّب وكيلًا. |
| `high` | أكبر عدد من الرموز المميّزة، وأبطأ رمز مميّز أول | الاستدلال المعقّد، والرياضيات والعلوم الصعبة، ومهام الترميز أو الوكلاء الأكثر صعوبة ويعمل بشكل جيد مع فك الترميز الطويل للنتائج الطويلة. |

أجرِ تقييماتك على المستويات الثلاثة باستخدام قيمة `max_output_tokens` عالية كي لا يتم اختصار الإجابات. بعد ذلك، اختَر أقل `thinking_level` يفي بمعايير الجودة لديك.

## قائمة التحقّق الخاصة بنقل البيانات

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### نقل البيانات إلى gemini-4-argon

- **تعديل معرّف النموذج:** غيِّر سلسلة النموذج إلى `gemini-4-argon`.
- **ضبط `max_output_tokens` بشكل صريح:** القيمة التلقائية هي 64 ألفًا لطلبات البث وحزمة تطوير البرامج (SDK)، و32 ألفًا لطلبات REST غير المتعلّقة بالبث.
- **رفع الحدود القصوى التي تقلّ عن 32 ألف:** ارفع أي حدّ أقصى يقلّ عن 32 ألف إلى 32,768 على الأقل. استخدِم `thinking_level` لتقليل إنفاق الرموز المميّزة.
- **التخطيط لعمليات فك الترميز الطويلة:** بالنسبة إلى المهام التي تتجاوز الحد الأقصى لكل طلب، استخدِم أحدث حزمة تطوير برامج (SDK) أو أضِف حلقة `continuation_token`.
- **استبدال `thinking_budget` بـ `thinking_level`:** لا يزال `thinking_budget` يعمل ويتم ربطه بأقرب `thinking_level`، ولكنّه يعرض تحذيرًا. اختبِر عبء العمل عند `low` و`medium` و`high`.
- **التوقّف عن استخدام التخزين المؤقت للسياق الصريح:** لا يتوافق التخزين المؤقت الصريح (`cachedContents` /
  `caches.create`) مع Gemini 4 Argon ويعرض رسالة خطأ.
  أزِل الطلبات التي تنشئ `cached_content` أو تمرّره في `GenerateContentConfig`.
  يتم تفعيل ميزة [التخزين المؤقت الضمني](https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=ar) تلقائيًا للطلبات التي تحتوي على 4,096 رمز مميّز على الأقل، ويتم خصم% 95 من الرموز المميّزة للإدخال المخزّنة مؤقتًا عند نتيجة ذاكرة التخزين المؤقت.
- **إزالة المَعلمات المتوقّفة نهائيًا:** أزِل `temperature` و`top_p` و`top_k` و`candidate_count` من الطلبات. في حال توفيرها، يتم تجاهل مَعلمات أخذ العينات.
- **زيادة مهلات العميل:** اضبط مهلات عميل HTTP على 20 دقيقة على الأقل لكل طلب.
- **حفظ توقيعات الأفكار:** يمكنك تمرير سجلّ المحادثات الكامل، بما في ذلك [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ar#signatures)، في طلبات المحادثات المتعدّدة واستدعاء الدوال.
- **مراجعة تقديرات التكلفة:** تتم فوترة كل رمز مميّز يعالجه النموذج، بما في ذلك تعليمات نظام الأدوات الداخلية وتعريفات الدوال عند استخدام ميزة "الربط بمصادر البيانات" (يُرجى الاطّلاع على [الأسعار](#pricing)).

## الأسعار

يتوفّر Gemini 4 Argon بسعر تمهيدي حتى 30 نوفمبر 2026:

- **الرموز المميّزة للإدخال:** ‏2.00 دولار أمريكي لكل مليون رمز مميّز (‏4.00 دولار أمريكي اعتبارًا من 1 ديسمبر 2026)
  - **الرموز المميّزة للإدخال المخزّنة مؤقتًا:** يوفّر التخزين المؤقت الضمني خصمًا بنسبة %95 على الإدخال المخزّن مؤقتًا، ليصبح السعر 0.10 دولار أمريكي لكل مليون رمز مميّز (0.20 دولار أمريكي اعتبارًا من 1 ديسمبر 2026).
- **رموز الناتج المميّزة، بما في ذلك الرموز المميّزة للتفكير:** ‏10.00 دولار أمريكي لكل مليون رمز مميّز (‏20.00 دولار أمريكي اعتبارًا من 1 ديسمبر 2026)

يتم احتساب كل رمز مميّز يعالجه النموذج وتحصيل رسوم مقابله، بما في ذلك الرموز المميّزة للتفكير وتعليمات نظام الأدوات الداخلية وتعريفات الدوال عند استخدام ميزة "التحقّق من المصادر". وستبقى ميزة تحديد المصدر من خلال "بحث Search" خاضعة للفوترة لكل طلب بحث.

لا يتوفّر Gemini 4 Argon في المستوى المجاني. للاطّلاع على فئات الأسعار الكاملة، يُرجى الانتقال إلى [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#gemini-4-argon).

## نماذج أخرى

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8?hl=ar)
- [‫Gemini 3.6 Flash و3.5‎ Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=ar)
- [عرض جميع النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar)

## الخطوات التالية

- يمكنك قراءة [دليل المطوّرين حول ميزة Long Decode](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=ar) للاطّلاع على أنماط البث الكامل وإعادة الاتصال واحتساب الرموز المميّزة.
- يمكنك الاطّلاع على [دليل التفكير](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ar) لمعرفة طريقة عمل مستويات التفكير وملخّصات الأفكار.
- اختبِر Gemini 4 Argon في [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-27 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-27 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
