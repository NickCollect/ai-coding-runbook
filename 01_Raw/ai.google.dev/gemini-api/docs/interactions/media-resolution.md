---
source_url: https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=ar
fetched_at: 2026-05-25T05:18:11.223959+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# درجة دقة الوسائط

يتحكّم المَعلمة `media_resolution` في طريقة معالجة Gemini API لمدخلات الوسائط، مثل الصور والفيديوهات ومستندات PDF، من خلال تحديد **الحد الأقصى لعدد الرموز المميزة** المخصّصة لمدخلات الوسائط، ما يتيح لك تحقيق التوازن بين جودة الردود ووقت الاستجابة والتكلفة. للاطّلاع على الإعدادات المختلفة والقيم التلقائية وكيفية تطابقها مع الرموز المميزة، يُرجى الانتقال إلى قسم [عدد الرموز المميزة](#token-counts).

يمكنك ضبط دقة الوسائط لعناصر الوسائط الفردية (عناصر المحتوى) ضمن طلبك (Gemini 3 فقط).

## دقة الوسائط لكل عنصر محتوى (Gemini 3 فقط)

يتيح لك Gemini 3 ضبط دقة الوسائط لكائنات الوسائط الفردية ضمن طلبك، ما يوفّر تحسينًا دقيقًا لاستخدام الرموز المميزة. يمكنك الجمع بين مستويات الدقة في طلب واحد. على سبيل المثال، استخدام دقة عالية لمخطط بياني معقّد ودقة منخفضة لصورة بسيطة ذات صلة بالسياق

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
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

- `unspecified`: هذا هو الإعداد التلقائي. يختلف عدد الرموز المميزة لهذا المستوى بشكل كبير بين Gemini 3 ونماذج Gemini السابقة.
- `low`: عدد أقل من الرموز المميزة، ما يؤدي إلى معالجة أسرع وتكلفة أقل، ولكن مع تفاصيل أقل
- ‫`medium`: توازن بين التفاصيل والتكلفة ووقت الاستجابة
- ‫`high`: عدد الرموز المميزة أكبر، ما يوفّر تفاصيل أكثر للنموذج للعمل عليها، ولكن على حساب زيادة وقت الاستجابة والتكلفة.
- ‫`ultra_high` (لكل عنصر محتوى فقط): أعلى عدد من الرموز المميزة، وهو مطلوب لحالات استخدام معيّنة مثل [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=ar).

يُرجى العِلم أنّ `high` يوفّر الأداء الأمثل لمعظم حالات الاستخدام.

يعتمد العدد الدقيق للرموز المميزة التي يتم إنشاؤها لكل مستوى من هذه المستويات على كل من **نوع الوسائط** (صورة أو فيديو أو ملف PDF) و**إصدار النموذج**.

## عدد الرموز المميزة

تلخّص الجداول أدناه عدد الرموز التقريبي لكل قيمة `media_resolution` ونوع وسائط لكل مجموعة نماذج.

**نماذج Gemini 3**

| MediaResolution | صورة | فيديو | PDF |
| --- | --- | --- | --- |
| `unspecified` (تلقائي) | 1120 | 70 | 560 |
| `low` | 280 | 70 | ‫280 + نص إعلاني مدمج |
| `medium` | 560 | 70 | ‫560 + نص إعلاني على المنصة نفسها |
| `high` | 1120 | 280 | ‫1120 + نص إعلاني على المنصة نفسها |
| `ultra_high` | 2240 | لا ينطبق | لا ينطبق |

## اختيار درجة الدقة المناسبة

- **تلقائي (`unspecified`):** ابدأ بالخيار التلقائي. تم تحسينها لتحقيق توازن جيد بين الجودة ووقت الاستجابة والتكلفة في معظم حالات الاستخدام الشائعة.
- **`low`:** استخدِم هذا الخيار في الحالات التي تكون فيها التكلفة ووقت الاستجابة في غاية الأهمية، وتكون التفاصيل الدقيقة أقل أهمية.
- **`medium` / `high`:** زيادة الدقة عندما تتطلّب المهمة فهم تفاصيل معقّدة في الوسائط وغالبًا ما يكون ذلك ضروريًا لإجراء تحليل مرئي معقّد أو قراءة المخططات أو فهم المستندات الكثيفة.
- **`ultra_high`**: يتوفّر هذا الخيار فقط لإعدادات كل عنصر من عناصر المحتوى. يُنصح باستخدامها في حالات استخدام معيّنة، مثل استخدام الكمبيوتر أو عندما تُظهر الاختبارات تحسّنًا واضحًا مقارنةً بـ `high`.
- **التحكّم في كل عنصر من عناصر المحتوى (Gemini 3):** يعمل على تحسين استخدام الرموز المميزة. على سبيل المثال، في طلب يتضمّن صورًا متعددة، استخدِم `high` لرسم تخطيطي معقّد و`low` أو `medium` لصور سياقية أبسط.

**الإعدادات المقترَحة**

في ما يلي قائمة بإعدادات دقة الوسائط المقترَحة لكل نوع من أنواع الوسائط المتوافقة.

| نوع الوسائط | الإعداد المقترَح | الحد الأقصى لعدد الرموز المميزة | إرشادات الاستخدام |
| --- | --- | --- | --- |
| **الصور** | `high` | 1120 | يُنصح باستخدامها لمعظم مهام تحليل الصور لضمان الحصول على أعلى جودة. |
| **ملفات PDF** | `medium` | 560 | الأفضل لفهم المستندات، وعادةً ما تصل الجودة إلى الحد الأقصى عند `medium`. لا تؤدي الزيادة إلى `high` عادةً إلى تحسين نتائج التعرّف البصري على الأحرف للمستندات العادية. |
| **الفيديو** (عام) | ‫`low` (أو `medium`) | ‫70 (لكل إطار) | **ملاحظة:** بالنسبة إلى الفيديو، يتم التعامل مع إعدادات `low` و`medium` بشكل مماثل (70 رمزًا مميزًا) لتحسين استخدام السياق. وهذا يكفي لمعظم مهام التعرّف على الإجراءات ووصفها. |
| **الفيديو** (يحتوي على الكثير من النصوص) | `high` | ‫280 (لكل إطار) | يجب توفُّرها فقط عندما تتضمّن حالة الاستخدام قراءة نص كثيف (التعرّف البصري على الأحرف) أو تفاصيل صغيرة ضمن لقطات الفيديو. |

ننصحك دائمًا باختبار وتقييم تأثير إعدادات الدقة المختلفة على تطبيقك للعثور على أفضل حلّ وسط بين الجودة ووقت الاستجابة والتكلفة.

## ملخّص التوافق مع الإصدارات

- إنّ ضبط `resolution` على عناصر المحتوى الفردية **متاح حصريًا في نماذج Gemini 3**.

## الخطوات التالية

- يمكنك الاطّلاع على مزيد من المعلومات حول إمكانات Gemini API المتعددة الوسائط في أدلة [فهم الصور](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=ar) و[فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ar) و[فهم المستندات](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
