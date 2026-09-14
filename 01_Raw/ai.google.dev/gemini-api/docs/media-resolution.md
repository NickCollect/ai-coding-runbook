---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=ar
fetched_at: 2026-09-14T05:45:52.903001+00:00
title: "\u062f\u0631\u062c\u0629 \u062f\u0642\u0629 \u0627\u0644\u0648\u0633\u0627\u0626\u0637 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# درجة دقة الوسائط

تتحكّم المَعلمة `media_resolution` في طريقة معالجة Gemini API لإدخالات الوسائط، مثل الصور والفيديوهات ومستندات PDF، من خلال تحديد **الحد الأقصى لعدد الرموز المميّزة** المخصّصة لإدخالات الوسائط، ما يسمح لك بتحقيق التوازن بين جودة الردّ ووقت الاستجابة والتكلفة. بالنسبة إلى الإعدادات المختلفة، يمكنك الاطّلاع على القيم التلقائية وكيفية مطابقتها للرموز المميّزة في قسم [عدد الرموز المميّزة](#token-counts).

يمكنك ضبط دقة الوسائط لكائنات الوسائط الفردية (عناصر المحتوى) ضِمن طلبك (Gemini 3 فقط).

## دقة الوسائط لكل عنصر محتوى (Gemini 3 فقط)

يسمح لك Gemini 3 بضبط دقة الوسائط لكائنات الوسائط الفردية ضِمن طلبك، ما يوفّر تحسينًا دقيقًا لاستخدام الرموز المميّزة. يمكنك المزج بين مستويات الدقة في طلب واحد. على سبيل المثال، يمكنك استخدام دقة عالية لمخطّط بياني معقّد ودقة منخفضة لصورة سياقية بسيطة.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### راحة

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## قيم الدقة المتاحة

تحدّد Gemini API المستويات التالية لدقة الوسائط:

- `unspecified`: هو الإعداد التلقائي. يختلف عدد الرموز المميّزة لهذا المستوى بشكلٍ كبير بين Gemini 3 ونماذج Gemini السابقة.
- `low`: عدد أقل من الرموز المميّزة، ما يؤدي إلى معالجة أسرع وتكلفة أقل، ولكن مع تفاصيل أقل.
- `medium`: توازن بين التفاصيل والتكلفة ووقت الاستجابة.
- `high`: عدد أكبر من الرموز المميّزة، ما يوفّر مزيدًا من التفاصيل التي يمكن للنموذج استخدامها، ولكن مع زيادة وقت الاستجابة والتكلفة.
- `ultra_high` (لكل عنصر محتوى فقط): أعلى عدد من الرموز المميّزة، وهو مطلوب لحالات استخدام معيّنة، مثل [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar).

يُرجى العِلم أنّ `high` يوفّر الأداء الأمثل لمعظم حالات الاستخدام.

يعتمد العدد الدقيق للرموز المميّزة التي يتم إنشاؤها لكل من هذه المستويات على **نوع الوسائط** (صورة أو فيديو أو PDF) و**إصدار النموذج**.

## عدد الرموز المميّزة

تُلخّص الجداول أدناه الأعداد التقريبية للرموز المميّزة لكل قيمة من قيم `media_resolution` ونوع وسائط لكل مجموعة نماذج.

**نماذج Gemini 3**

| MediaResolution | صورة | فيديو | PDF |
| --- | --- | --- | --- |
| `unspecified` (تلقائي) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + نص أصلي |
| `medium` | 560 | 70 | 560 + نص أصلي |
| `high` | 1120 | 280 | 1120 + نص أصلي |
| `ultra_high` | 2240 | لا ينطبق | لا ينطبق |

## اختيار الدقة المناسبة

- **تلقائي (`unspecified`):** ابدأ بالإعداد التلقائي. تم ضبط هذا الإعداد لتحقيق توازن جيد بين الجودة ووقت الاستجابة والتكلفة لمعظم حالات الاستخدام الشائعة.
- **`low`:** استخدِم هذا الإعداد في السيناريوهات التي تكون فيها التكلفة ووقت الاستجابة في غاية الأهمية، وتكون التفاصيل الدقيقة أقل أهمية.
- **`medium` / `high`:** يمكنك زيادة الدقة عندما تتطلّب المهمة فهم تفاصيل معقّدة ضِمن الوسائط. غالبًا ما يكون ذلك ضروريًا لإجراء تحليل مرئي معقّد أو قراءة المخطّطات أو فهم المستندات الكثيفة.
- **`ultra_high`** : لا يتوفّر هذا الإعداد إلا لكل عنصر محتوى. يُنصح باستخدامه في حالات استخدام معيّنة، مثل استخدام الكمبيوتر أو عندما تُظهر الاختبارات تحسينًا واضحًا مقارنةً بالإعداد `high`.
- **التحكّم لكل عنصر محتوى (Gemini 3):** يؤدي ذلك إلى تحسين استخدام الرموز المميّزة. على سبيل المثال، في طلب يتضمّن صورًا متعدّدة، استخدِم `high` لمخطّط بياني معقّد و`low` أو `medium` لصور سياقية أبسط.

**الإعدادات المقترَحة**

في ما يلي الإعدادات المقترَحة لدقة الوسائط لكل نوع من أنواع الوسائط المتوافقة.

| نوع الوسائط | الإعداد المقترَح | الحد الأقصى لعدد الرموز المميّزة | إرشادات الاستخدام |
| --- | --- | --- | --- |
| **الصور** | `high` | 1120 | يُنصح باستخدامه لمعظم مهام تحليل الصور لضمان تحقيق أقصى جودة. |
| **ملفات PDF** | `medium` | 560 | يُعدّ هذا الإعداد مثاليًا لفهم المستندات، وعادةً ما تصل الجودة إلى الحد الأقصى عند استخدام `medium`. نادرًا ما يؤدي الانتقال إلى `high` إلى تحسين نتائج "التعرّف البصري على الأحرف" للمستندات العادية. |
| **الفيديو** (عام) | `low` (أو `medium`) | 70 (لكل إطار) | **ملاحظة:** بالنسبة إلى الفيديو، يتم التعامل مع الإعدادَين `low` و`medium` بشكلٍ متطابق (70 رمزًا مميّزًا) لتحسين استخدام السياق. ويكفي ذلك لمعظم مهام التعرّف على الإجراءات والأوصاف. |
| **الفيديو** (يحتوي على نص كثيف) | `high` | 280 (لكل إطار) | لا يكون هذا الإعداد مطلوبًا إلا عندما تتضمّن حالة الاستخدام قراءة نص كثيف (التعرّف البصري على الأحرف) أو تفاصيل صغيرة ضِمن إطارات الفيديو. |

عليك دائمًا اختبار وتقييم تأثير إعدادات الدقة المختلفة على تطبيقك للعثور على أفضل حل وسط بين الجودة ووقت الاستجابة والتكلفة.

## ملخّص التوافق مع الإصدارات

- يقتصر ضبط `resolution` على عناصر المحتوى الفردية على **نماذج Gemini 3**.

## الخطوات التالية

- يمكنك التعرّف أكثر على الإمكانات المتعدّدة الوسائط في Gemini API من خلال أدلة [فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar) و[فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar) و[فهم المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
