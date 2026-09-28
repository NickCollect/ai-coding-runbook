---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ar
fetched_at: 2026-09-28T06:25:26.463202+00:00
title: "\u062f\u0631\u062c\u0629 \u062f\u0642\u0629 \u0627\u0644\u0648\u0633\u0627\u0626\u0637 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 3.8 Flash متاح الآن. [جرِّبه](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)

إرسال ملاحظات

# درجة دقة الوسائط

يتحكّم المَعلمة `media_resolution` في طريقة معالجة Gemini API لمدخلات الوسائط، مثل الصور والفيديوهات والصوت ومستندات PDF، من خلال تحديد **الحد الأقصى لعدد الرموز المميزة** المخصّصة لمدخلات الوسائط، ما يتيح لك تحقيق التوازن بين جودة الردود ووقت الاستجابة والتكلفة. في حين أنّ المدخلات المرئية ومدخلات المستندات تحدّد عدد الرموز المميزة المخصّصة استنادًا إلى إعداد درجة الدقة، يتم تحويل المدخلات الصوتية إلى رموز مميزة بمعدّل ثابت في الثانية على جميع مستويات الدقة. للاطّلاع على الإعدادات المختلفة والقيم التلقائية وكيفية توافقها مع الرموز المميّزة، يُرجى الانتقال إلى قسم [عدد الرموز المميّزة](#token-counts).

يمكنك ضبط دقة الوسائط بطريقتَين:

- [لكل جزء](#per-part-media-resolution) (Gemini 3 فقط)
- [على مستوى العالم](#global-media-resolution) لطلب `generateContent` كامل (جميع النماذج المتعدّدة الوسائط)

## دقة الوسائط لكل جزء (في Gemini 3 فقط)

يتيح لك Gemini 3 ضبط دقة الوسائط لكائنات الوسائط الفردية ضمن طلبك، ما يوفّر تحسينًا دقيقًا لاستخدام الرموز المميزة. يمكنك الجمع بين مستويات الدقة المختلفة في طلب واحد. على سبيل المثال، يمكنك استخدام دقة عالية لمخطط بياني معقّد ودقة منخفضة لصورة سياقية. يلغي هذا الإعداد أي ضبط عام لجزء معيّن. للاطّلاع على الإعدادات التلقائية، راجِع قسم [عدد الرموز المميزة](#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## درجة دقة الوسائط على مستوى العالم

يمكنك ضبط دقة تلقائية لجميع أجزاء الوسائط في الطلب باستخدام
`GenerationConfig`. تتوفّر هذه الميزة في جميع النماذج المتعدّدة الوسائط. إذا تضمّن الطلب إعدادات عامة و[إعدادات خاصة بكل جزء](#per-part-media-resolution)، ستكون الأولوية للإعدادات الخاصة بكل جزء بالنسبة إلى هذا العنصر المحدّد.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## قيم الدقة المتاحة

تحدّد Gemini API المستويات التالية لدقة الوسائط:

- `MEDIA_RESOLUTION_UNSPECIFIED`: هذا هو الإعداد التلقائي. يختلف عدد الرموز المميزة لهذا المستوى بشكل كبير بين Gemini 3 ونماذج Gemini السابقة.
- `MEDIA_RESOLUTION_LOW`: عدد أقل من الرموز المميزة، ما يؤدي إلى معالجة أسرع
  وتكلفة أقل، ولكن مع تفاصيل أقل
- ‫`MEDIA_RESOLUTION_MEDIUM`: تحقيق التوازن بين التفاصيل والتكلفة ووقت الاستجابة
- ‫`MEDIA_RESOLUTION_HIGH`: عدد الرموز المميزة أكبر، ما يوفّر تفاصيل أكثر للنموذج للعمل عليها، ولكن مع زيادة وقت الاستجابة والتكلفة.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (لكل جزء فقط): أعلى عدد من الرموز المميزة، وهو مطلوب لحالات استخدام محدّدة، مثل [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar).

يُرجى العِلم أنّ `MEDIA_RESOLUTION_HIGH` يوفّر الأداء الأمثل لمعظم حالات الاستخدام.

يعتمد العدد الدقيق للرموز المميزة التي يتم إنشاؤها لكل مستوى من هذه المستويات على **نوع الوسائط** (صورة أو فيديو أو صوت أو ملف PDF) و**إصدار النموذج**.

## عدد الرموز المميّزة

تلخّص الجداول أدناه عدد الرموز المميزة التقريبي لكل قيمة `media_resolution` ونوع وسائط لكل مجموعة نماذج.

**نماذج Gemini 3**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **صورة** | **الفيديو** | **الصوت** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (تلقائي) | 1120 | 70 | ‫25 (في الثانية) | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | ‫25 (في الثانية) | ‫280 + نص أصلي |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | ‫25 (في الثانية) | ‫560 + نص أصلي |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | ‫25 (في الثانية) | ‫1120 + نص إعلاني على المنصة نفسها |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | لا ينطبق | لا ينطبق | لا ينطبق |

**نماذج Gemini 2.5**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MediaResolution** | **صورة** | **الفيديو** | **الصوت** | **ملف PDF (ممسوح ضوئيًا)** | **ملف PDF (مدمَج مع المحتوى)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (تلقائي) | ‫256 + Pan & Scan (~2048) | 256 | ‫32 (في الثانية) | ‫256 + التعرّف البصري على الأحرف | ‫256 + نص أصلي |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | ‫32 (في الثانية) | ‫64 + OCR | ‫64 + نص أصلي |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | ‫32 (في الثانية) | ‫256 + التعرّف البصري على الأحرف | ‫256 + نص أصلي |
| `MEDIA_RESOLUTION_HIGH` | ‫256 + Pan & Scan | 256 | ‫32 (في الثانية) | ‫256 + التعرّف البصري على الأحرف | ‫256 + نص أصلي |

## اختيار درجة الدقة المناسبة

- **تلقائي (`UNSPECIFIED`):** ابدأ بالخيار التلقائي. تم تحسين هذا الخيار لتحقيق توازن جيد بين الجودة والوقت المستغرَق والتكلفة في معظم حالات الاستخدام الشائعة.
- **`LOW`:** استخدِم هذا الخيار في الحالات التي تكون فيها التكلفة ووقت الاستجابة في غاية الأهمية،
  ويكون الحصول على تفاصيل دقيقة أقل أهمية.
- ‫**`MEDIUM` / `HIGH`:** زيادة درجة الدقة عندما تتطلّب المهمة فهم تفاصيل دقيقة في الوسائط وغالبًا ما تكون هذه الميزة مطلوبة
  لتحليل الصور المعقّدة أو قراءة الرسوم البيانية أو فهم المستندات الكبيرة.
- **`ULTRA HIGH`**: يتوفّر هذا الخيار فقط لإعدادات كل جزء. يُنصح باستخدامها في حالات استخدام معيّنة، مثل استخدام الكمبيوتر أو عندما تُظهر الاختبارات تحسّنًا واضحًا مقارنةً بـ `HIGH`.
- **التحكّم في كل جزء (Gemini 3):** يحسِّن استخدام الرموز المميزة. على سبيل المثال، في طلب يتضمّن صورًا متعددة، استخدِم `HIGH` لرسم تخطيطي معقّد و`LOW` أو `MEDIUM` لصور سياقية أبسط.

**الإعدادات المقترَحة**

في ما يلي قائمة بإعدادات دقة الوسائط المقترَحة لكل نوع من أنواع الوسائط المتوافقة.

|  |  |  |  |
| --- | --- | --- | --- |
| **نوع الوسائط** | **الإعدادات المقترَحة** | **الحد الأقصى لعدد الرموز المميزة** | **إرشادات الاستخدام** |
| **الصور** | `MEDIA_RESOLUTION_HIGH` | 1120 | يُنصح باستخدامها لمعظم مهام تحليل الصور لضمان الحصول على أعلى جودة. |
| **ملفات PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | الأفضل لفهم المستندات، وعادةً ما تصل الجودة إلى الحد الأقصى عند `medium`. لا تؤدي الزيادة إلى `high` في أغلب الأحيان إلى تحسين نتائج التعرّف البصري على الأحرف للمستندات العادية. |
| **الفيديو** (عام) | ‫`MEDIA_RESOLUTION_LOW` (أو `MEDIA_RESOLUTION_MEDIUM`) | ‫70 (لكل إطار) | **ملاحظة:** بالنسبة إلى الفيديو، يتم التعامل مع إعدادات `low` و`medium` بشكل مماثل (70 رمزًا مميزًا) لتحسين استخدام السياق. وهذا يكفي لمعظم مهام التعرّف على الإجراءات ووصفها. |
| **الفيديو** (يحتوي على الكثير من النصوص) | `MEDIA_RESOLUTION_HIGH` | ‫280 (لكل إطار) | يجب توفُّرها فقط عندما تتضمّن حالة الاستخدام قراءة نص كثيف (التعرّف البصري على الأحرف) أو تفاصيل صغيرة ضمن إطارات الفيديو. |
| **الصوت** | `MEDIA_RESOLUTION_UNSPECIFIED` (تلقائي) | ‫25 (في الثانية) لنموذج Gemini 3 و32 (في الثانية) لنموذج Gemini 2.5 | يتم تحويل الصوت إلى رموز بمعدل ثابت في الثانية الواحدة على مستوى جميع إعدادات الدقة المتوافقة (`unspecified` و`low` و`medium` و`high`). |

ننصحك دائمًا باختبار وتقييم تأثير إعدادات الدقة المختلفة على تطبيقك المحدّد للعثور على أفضل موازنة بين الجودة ووقت الاستجابة والتكلفة.

## العلاقة بأوضاع معالجة الفيديو

تتحكّم المَعلمتَين `media_resolution` والمعالجة في جوانب مختلفة من إدخال الفيديو:

- يتحكّم `media_resolution` في **دقة** كل إطار (عدد الرموز المميزة لكل إطار).
- تتحكّم `processing` / `media_processing` في **المحتوى الذي يتم تحميله من الفيديو** إلى السياق.

يمكنك ضبط كليهما على إدخال الفيديو نفسه. على سبيل المثال، يمكنك استخدام المعالجة المستندة إلى الوكيل مع درجة دقة منخفضة للوسائط لتقليل إجمالي استخدام الرموز المميزة لفيديو طويل.

للحصول على تفاصيل حول أوضاع معالجة الفيديو، يُرجى الاطّلاع على دليل [فهم الفيديو المستند إلى الذكاء الاصطناعي](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar#agentic-video-understanding).

## ملخّص التوافق مع الإصدارات

- تتوفّر السمة `MediaResolution` enum لجميع النماذج التي تتيح إدخال الوسائط.
- تختلف أعداد الرموز المميزة المرتبطة بكل مستوى من مستويات التعداد بين نماذج Gemini 3 وإصدارات Gemini السابقة.
- يقتصر ضبط `media_resolution` على عناصر `Part` الفردية **على نماذج Gemini 3**.

## الخطوات التالية

- يمكنك الاطّلاع على مزيد من المعلومات حول إمكانات Gemini API المتعددة الوسائط في أدلة
  [فهم الصور](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=ar) و[فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar) و[فهم الصوت](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ar) و[فهم المستندات](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
