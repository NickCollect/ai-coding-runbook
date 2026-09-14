---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=ar
fetched_at: 2026-09-14T05:45:11.451137+00:00
title: "\u062a\u062d\u0648\u064a\u0644 \u0627\u0644\u0635\u0648\u062a \u0625\u0644\u0649 \u0646\u0635 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)

إرسال ملاحظات

# تحويل الصوت إلى نص

تحوّل Gemini API الكلام في الملفات الصوتية إلى نص باستخدام نموذج Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). واستنادًا إلى إمكانات Gemini في فهم الصوت، يقدّم خدمة تحويل الصوت إلى نص بدقة مع التعرّف التلقائي على اللغة، وتحديد المتحدث، والطوابع الزمنية على مستوى الكلمات، وتلميحات المفردات المخصّصة. يتضمّن أيضًا وضع [تحويل الصوت إلى نص بذكاء](#transcription-modes) الذي يزيل الأخطاء اللغوية ويوفّر تنسيقًا ذكيًا.

لتحويل ملف صوتي إلى نص، حمِّل الملف الصوتي وأرسِله إلى `gemini-3.5-transcribe`:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const audioFile = await client.files.upload({
  file: "path/to/sample.mp3",
  config: { mime_type: "audio/mp3" },
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
});

console.log(interaction.output_text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## نظرة عامة

تم تحسين Gemini 3.5 Transcribe لمهام تحويل الكلام إلى نص. تتعامل هذه الميزة مع اللهجات المختلفة والضوضاء في الخلفية والمحادثات المتعددة اللغات.

تشمل الإمكانات الرئيسية ما يلي:

- **التعرّف التلقائي على الكلام (ASR):** يتم تلقائيًا رصد اللغات في أكثر من [85 منطقة](#supported-languages). يتعامل مع التبديل بين اللغات داخل الجملة وبين الجمل بدون إعداد يدوي.
- **المفردات المخصّصة:** يتم تحسين التعرّف على المصطلحات والاختصارات والأسماء الخاصة بالنطاق من خلال إدخال ما يصل إلى 1,000 عبارة.
- **تحديد المتحدّثين:** يميز بين المتحدّثين المتعددين وينسب المقاطع المنطوقة إلى تصنيفات مختلفة.
- **الطوابع الزمنية على مستوى الكلمات:** يتم إنشاء إزاحات دقيقة لوقتَي البدء والانتهاء لكل كلمة يتم التعرّف عليها.
- **تحويل الصوت إلى نص بذكاء:** تنقّح هذه الميزة النص من أخطاء الطلاقة وكلمات الحشو والتكرار، وتطبّق تنسيقًا منظَّمًا.
- **التنسيق والتسوية:** يتم تطبيق الكتابة بالأحرف اللاتينية الكبيرة وعلامات الترقيم وتسوية النص العكسية، مثل تحويل "ستة وعشرون مليون دولار أمريكي" إلى "26 مليون دولار أمريكي".

لفهم المحتوى الصوتي بشكل عام أو الإجابة عن أسئلة حوله، استخدِم [فهم المحتوى الصوتي](https://ai.google.dev/gemini-api/docs/audio?hl=ar). لتركيب الصوت من النص، استخدِم [تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar).

## اكتشاف اللغة وتقديم تلميحات

يتعرّف النموذج تلقائيًا على اللغة المنطوقة. ويبدّل بين اللغات بشكل ديناميكي عندما يغيّر المتحدثون اللغة.

لاستخدام ميزة "الرصد التلقائي"، احذف `language_codes` أو قدِّم قائمة فارغة:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "language_codes": [],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      language_codes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "language_codes": []
      }
    }
  }'
```

إذا كنت تعرف اللغة مسبقًا، حدِّد رموز اللغة BCP-47 في `language_codes` لتحسين دقة النسخ (راجِع [اللغات المتوافقة](#supported-languages)):

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## المفردات المخصّصة

يمكنك توجيه نموذج الكلام نحو الكلمات غير الشائعة أو المصطلحات الفنية أو أسماء العلامات التجارية أو أسماء العَلم. قدِّم ما يصل إلى 1,000 عبارة في مصفوفة `custom_vocabulary` (عادةً ما يتم تحقيق أفضل النتائج باستخدام ما يصل إلى 100 عبارة):

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      custom_vocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## تمييز أصوات المتحدّثِين

تحدّد ميزة "تحديد المتحدّث" الأصوات المختلفة في التسجيل وتضع علامة على كل مقطع باستخدام معرّف المتحدّث، مثل `spk_1` أو `spk_2`. يمكن استخدام ما يصل إلى 8 مكبّرات صوت (تكون ميزة تحديد المصدر لـ 3 مكبّرات صوت أو أكثر تجريبية).

فعِّل ميزة "تمييز أصوات المتحدّثِين" من خلال ضبط `diarization_mode` ضمن `mode`:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "diarization_mode": "speaker",
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        diarization_mode: "speaker",
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "diarization_mode": "speaker"
        }
      }
    }
  }'
```

## الطوابع الزمنية على مستوى الكلمات

توفّر الطوابع الزمنية على مستوى الكلمات إزاحات دقيقة للبداية والنهاية لكل كلمة يتم التعرّف عليها في بث صوتي.

فعِّل الطوابع الزمنية من خلال ضبط `timestamp_granularities` ضمن `mode`:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "timestamp_granularities": ["word"],
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        timestamp_granularities: ["word"],
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "timestamp_granularities": ["word"]
        }
      }
    }
  }'
```

يمكنك الجمع بين `diarization_mode` و`timestamp_granularities` في `mode` لتلقّي تصنيفات المتحدّثين والطوابع الزمنية للكلمات:

### Python

```
generation_config = {
    "transcription_config": {
        "custom_vocabulary": ["Gemini"],
        "mode": {
            "type": "verbatim",
            "diarization_mode": "speaker",
            "timestamp_granularities": ["word"],
        },
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    custom_vocabulary: ["Gemini"],
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "custom_vocabulary": ["Gemini"],
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## أوضاع تحويل الصوت إلى نص

تتيح أداة Gemini 3.5 Transcribe وضعَين لتحويل الصوت إلى نص من خلال المَعلمة `mode`:

- **`verbatim` (الإعداد التلقائي)**: تعرض هذه القيمة نصًا مطابقًا تمامًا لكل ما يُقال، مع الحفاظ على الكلمات الحشو الخام ("أمم" و"آه" و"مثل" و"كما تعلم") والتكرار والتوقفات المؤقتة وبدايات الجمل الخاطئة. يتم ضبط الطوابع الزمنية وتمييز أصوات المتحدّثين ضمن هذا الوضع (`{"type": "verbatim", ...}`).
- **`smart` (النسخ الذكي)**: تحسين النص لتسهيل قراءته من خلال تطبيق معالجة ذكية بعد التسجيل:
  - **إزالة التلعثم**: تزيل هذه الميزة الكلمات التي تُستخدم لملء الفراغات في المحادثة والتلعثم وبدايات الجمل الخاطئة.
  - **التصحيحات الذاتية المضمّنة**: تحلّ التصحيحات المنطوقة مباشرةً (على سبيل المثال، *"لنجتمع يوم الثلاثاء، لا بل يوم الأربعاء في الساعة الثانية"* تصبح *"لنجتمع يوم الأربعاء في الساعة 2:00 ظهرًا"*).
  - **التنسيق المنظَّم التلقائي**: ينظّم الأفكار المنطوقة تلقائيًا في فقرات وقوائم مرقّمة ونقاط تعداد وتواريخ وعملات وأرقام منسَّقة.
  - **التصحيح النحوي**: يضيف علامات الترقيم المناسبة ويعدّل حالة الأحرف في الجملة ويحسّن من سلاسة النص.

| محتوى كلامي صوتي | `verbatim` الناتج | ناتج `smart` (التحويل الذكي من صوت إلى نص) |
| --- | --- | --- |
| "حسنًا، بالنسبة إلى الاجتماع، أعتقد أنّه علينا دعوة "منى"، لا، "عماد" و"كارول". | "حسنًا، بالنسبة إلى الاجتماع، أعتقد أنّه علينا دعوة أليس، لا، بل دعوة بوب وكارول". | "أعتقد أنّه علينا دعوة "بوب" و"كارول" إلى الاجتماع". |
| مراجعة العنصر الأول للميزانية، وضع اللمسات الأخيرة على الجدول الزمني للعنصر الثاني، إرسال ملخّص للعنصر الثالث | "مراجعة العنصر الأول، تحديد الميزانية، وضع اللمسات الأخيرة على الجدول الزمني للعنصر الثاني، إرسال ملخّص للعنصر الثالث" | "1- مراجعة الميزانية 2. إنهاء المخطّط الزمني ‫3. إرسال ملخّص" |

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": "smart",
        }
    },
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: "smart",
    },
  },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": "smart"
      }
    }
  }'
```

## تحليل نتيجة تحويل الصوت إلى نص

يتم عرض نص المحادثة الكامل في `interaction.output_text`.

عند تفعيل `timestamp_granularities` أو `diarization_mode`، تعرض واجهة برمجة التطبيقات أيضًا تعليقات توضيحية مفصّلة على مستوى الكلمات مرفقة بمحتوى التفاعل.

في ما يلي كيفية استخراج الطوابع الزمنية للكلمات ونوبات التحدث وتكرارها:

### Python

```
def extract_word_annotations(interaction):
    words = []
    for step in getattr(interaction, "steps", []) or []:
        for content in getattr(step, "content", []) or []:
            for annotation in getattr(content, "annotations", []) or []:
                if getattr(annotation, "type", None) == "word_info":
                    words.append(annotation)
    return words

words = extract_word_annotations(interaction)

for w in words:
    speaker = f"[{w.speaker}] " if getattr(w, "speaker", None) else ""
    start = getattr(w, "start_offset", "")
    end = getattr(w, "end_offset", "")
    timing = f"({start} -> {end}) " if start and end else ""
    print(f"{speaker}{timing}{w.text}")
```

### JavaScript

```
function extractWordAnnotations(interaction) {
  const words = [];
  for (const step of interaction.steps ?? []) {
    for (const content of step.content ?? []) {
      for (const annotation of content.annotations ?? []) {
        if (annotation.type === "word_info") {
          words.push(annotation);
        }
      }
    }
  }
  return words;
}

const words = extractWordAnnotations(interaction);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.start_offset && w.end_offset) ? `(${w.start_offset} -> ${w.end_offset}) ` : "";
  console.log(`${speaker}${timing}${w.text}`);
}
```

### REST

```
{
  "id": "interactions/abc123xyz",
  "status": "completed",
  "steps": [
    {
      "id": "step_001",
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Hello world",
          "annotations": [
            {
              "type": "word_info",
              "text": "Hello",
              "speaker": "spk_1",
              "start_offset": "0.100s",
              "end_offset": "0.450s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.850s"
            }
          ]
        }
      ]
    }
  ]
}
```

## اللغات المتاحة

تتوفّر ميزة "النسخ الصوتي" في Gemini 3.5 باللغات ورموز اللغة BCP-47 التالية:

| اللغة | رمز BCP-47 | اللغة | رمز BCP-47 |
| --- | --- | --- | --- |
| الأفريقانية | `af-ZA` | اليابانية | `ja-JP` |
| الأمهرية | `am-ET` | الجافانية | `jv-ID` |
| العربية (مصر) | `ar-EG` | كابوفيرديانيو | `kea-CV` |
| الأرمينية | `hy-AM` | الكانادا | `kn-IN` |
| الأسامية | `as-IN` | الكازاخية | `kk-KZ` |
| أذربيجان | `az-AZ` | الكورية | `ko-KR` |
| البيلاروسية | `be-BY` | القيرغيزية | `ky-KG` |
| البنغالية (بنغلاديش) | `bn-BD` | اللاتفية | `lv-LV` |
| البنغالية (الهند) | `bn-IN` | اللينجالا | `ln-CD` |
| البوسنية | `bs-BA` | الليتوانية | `lt-LT` |
| البلغارية | `bg-BG` | المقدونية | `mk-MK` |
| البلغارية (الأرومانية) | `rup-BG` | الماليزية | `ms-MY` |
| البورمية | `my-MM` | المالايالامية | `ml-IN` |
| الكانتونية (التقليدية) | `yue-Hant-HK` | المالطية | `mt-MT` |
| الكتالانية | `ca-ES` | الصينية الماندرين (المبسطة) | `cmn-Hans-CN` |
| السيبيوانية | `ceb` | المراثية | `mr-IN` |
| الخميرية القياسية | `km-KH` | المنغولية | `mn-MN` |
| الكرواتية | `hr-HR` | النيبالية | `ne-NP` |
| التشيكية | `cs-CZ` | النرويجية | `nb-NO` |
| الدانماركية | `da-DK` | الأوريا | `or-IN` |
| الهولندية | `nl-NL` | البولندية | `pl-PL` |
| الإنجليزية (بريطانيا العظمى) | `en-GB` | البرتغالية (البرازيل) | `pt-BR` |
| الإنجليزية (الهند) | `en-IN` | البرتغالية (البرتغال) | `pt-PT` |
| الإنجليزية (الولايات المتحدة) | `en-US` | البنجابية | `pa-IN` |
| الإستونية | `et-EE` | البنجابية (نص غورموخي) | `pa-Guru-IN` |
| الفارسية | `fa-IR` | الرومانية | `ro-RO` |
| الفلبينية | `fil-PH` | الروسية | `ru-RU` |
| الفنلندية | `fi-FI` | الصربية | `sr-RS` |
| الفرنسية | `fr-FR` | السندية (الخط العربي) | `sd-Arab-IN` |
| الغليشيانية | `gl-ES` | السلوفاكية | `sk-SK` |
| الجورجية | `ka-GE` | السلوفينية | `sl-SI` |
| الألمانية | `de-DE` | الإسبانية (أمريكا اللاتينية) | `es-419` |
| اليونانية | `el-GR` | الإسبانية (الولايات المتحدة) | `es-US` |
| الغوجاراتية | `gu-IN` | السواحيلية (كينيا) | `sw-KE` |
| الهوسا | `ha-NG` | السويدية | `sv-SE` |
| العبرية | `he-IL` | الطاجيكية | `tg-TJ` |
| الهندية | `hi-IN` | التيلوغوية | `te-IN` |
| الهنغارية | `hu-HU` | التايلاندية | `th-TH` |
| الأيسلندية | `is-IS` | التركية | `tr-TR` |
| الإنجليزية الهندية | `en-IN` | الأوكرانية | `uk-UA` |
| الإندونيسية | `id-ID` | الأوزبكية | `uz-UZ` |
| الإيطالية | `it-IT` | الفيتنامية | `vi-VN` |

## تنسيقات الصوت المتوافقة

يتوافق Gemini 3.5 Transcribe مع أنواع MIME التالية لتنسيقات الصوت:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- ‫L16 - `audio/l16`
- ‫Opus - ‏`audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

للاطّلاع على القائمة الكاملة بأنواع MIME المتوافقة ومخططات المَعلمات، يُرجى الرجوع إلى [مرجع Interactions API](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Content).

## مرجع المَعلمة

اضبط إعدادات تحويل الصوت إلى نص من خلال تحديد الحقول ضِمن الكائن `transcription_config` في `generation_config`:

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `language_codes` | مصفوفة سلاسل | رموز اللغة BCP-47 (مثل `["en-US"]`). في حال حذفها أو تركها فارغة (`[]`)، يرصد النموذج اللغة تلقائيًا ويتعامل مع تبديل الرموز. |
| `custom_vocabulary` | مصفوفة سلاسل | ما يصل إلى 1,000 مصطلح أو اختصار أو اسم علم مخصّص لتحسين دقة التعرّف على الكلام |
| `mode` | كائن أو سلسلة | إعدادات وضع تحويل الصوت إلى نص يقبل `"smart"` أو عنصر وضع مطابق (`{"type": "verbatim", ...}`). الإعداد التلقائي هو "نسخ مطابق". |
| `mode.type` | سلسلة | *(وضع "النص المطابق" فقط)* معرّف الوضع يجب ضبطها دائمًا على `"verbatim"`. |
| `mode.timestamp_granularities` | مصفوفة سلاسل | *(وضع "المطابقة التامة" فقط)* دقة الطوابع الزمنية التي سيتم عرضها. مرِّر `["word"]` لتفعيل إزاحات بداية الكلمة ونهايتها. |
| `mode.diarization_mode` | سلسلة | *(وضع "النص المطابق" فقط)* وضع تحديد هوية المتحدث. مرِّر `"speaker"` لتحديد المتحدّثين المميّزين وتصنيفهم. |

## أفضل الممارسات

- **توفير صوت واضح:** تأكَّد من أنّ التسجيلات الصوتية تتضمّن فصلًا واضحًا للأصوات وتجنَّب التقطيع الشديد.
- **تقديم تلميحات حول اللغة عند معرفتها:** إذا كنت تعرف لغة الصوت مسبقًا، حدِّد `language_codes` لزيادة الدقة إلى أقصى حد.
- **استهداف المفردات المخصّصة:** لا تضمِّن في `custom_vocabulary` سوى عبارات مميّزة خاصة بالنطاق أو أسماء علامات تجارية أو أسماء علم، بدلاً من الكلمات الشائعة اليومية.
- **استخدام Files API للتسجيلات الكبيرة:** بالنسبة إلى الملفات التي تزيد مدتها عن بضع ثوانٍ، حمِّل الملف باستخدام `client.files.upload` ومرِّر معرّف الموارد المنتظم (URI) للملف الذي تم إرجاعه إلى النموذج.

## القيود

- **مدة الصوت:** تتيح الطلبات الأحادية العادية استخدام ملفات صوتية تصل مدتها إلى ساعة واحدة. تقتصر معالجة الصوت على 30 دقيقة عند تفعيل ميزات، مثل تحديد هوية المتحدث أو الطوابع الزمنية على مستوى الكلمات.
- **الطوابع الزمنية على مستوى الكلمات:** قد يؤدي تفعيل الطوابع الزمنية على مستوى الكلمات إلى انخفاض دقة تحويل الصوت إلى نص بشكل عام.
- **تمييز أصوات المتحدّثِين:** تتيح هذه الميزة التعرّف على ما يصل إلى 8 متحدثين. ميزة تحديد المتحدثين لثلاثة أشخاص أو أكثر هي ميزة تجريبية.
- **المفردات المخصّصة:** يمكنك تقديم ما يصل إلى 1,000 عبارة في `custom_vocabulary`، ولكن عادةً ما يتم تحقيق أفضل النتائج باستخدام ما يصل إلى 100 عبارة.
- **التوافق مع الأوضاع:** لا يمكن دمج ميزة "النسخ الذكي" (`"smart"`) مع `timestamp_granularities` أو `diarization_mode`.

## الخطوات التالية

- يمكنك بث الصوت في الوقت الفعلي باستخدام [دليل "تحويل الصوت إلى نص مباشرةً"](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=ar) من خلال Live API.
- استكشِف [فهم الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar) لتحليل المحتوى الصوتي أو تلخيصه أو البحث فيه.
- تعرَّف على كيفية إنشاء صوت من نص باستخدام ميزة [تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar).
- راجِع [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#gemini-3.5-transcribe) لمعرفة أسعار النماذج وحدود الرموز المميزة.
- راجِع دليل [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar) لمعرفة تفاصيل حول تحميل ملفات الوسائط وإدارتها.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-08-28 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-08-28 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
