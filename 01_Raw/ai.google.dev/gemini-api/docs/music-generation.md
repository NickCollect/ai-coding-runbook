---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=ar
fetched_at: 2026-06-29T05:36:47.281046+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0645\u0648\u0633\u064a\u0642\u0649 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء موسيقى باستخدام Lyria 3

‫Lyria 3 هي مجموعة نماذج من Google لإنشاء الموسيقى، وهي متاحة من خلال Gemini API. باستخدام Lyria 3، يمكنك إنشاء مقاطع صوتية استيريو عالية الجودة بمعدّل 44.1 كيلوهرتز من الطلبات النصية أو الصور. تقدّم هذه النماذج اتساقًا بنيويًا، بما في ذلك الغناء والكلمات الموقّتة والترتيبات الموسيقية الكاملة.

تتضمّن مجموعة Lyria 3 نموذجَين:

| الطراز | رقم تعريف الطراز | يناسب هذا الخيار: | المدة | الناتج |
| --- | --- | --- | --- | --- |
| **مقطع Lyria 3** | `lyria-3-clip-preview` | المقاطع القصيرة والحلقات المتكرّرة والمعاينات | ‫30 ثانية | MP3 |
| ‫**Lyria 3 Pro** | `lyria-3-pro-preview` | أغانٍ كاملة تتضمّن مقاطع ولوازم وجسورًا موسيقية | بضع دقائق (يمكن التحكّم فيها باستخدام الطلب) | MP3 |

يمكن استخدام كلا النموذجين من خلال واجهة [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) الجديدة التي تتيح إدخال بيانات متعددة الوسائط (نصوص وصور) وإنتاج صوت **استيريو عالي الدقة بتردد 44.1 كيلوهرتز**.

## إنشاء مقطع موسيقي

ينشئ نموذج Lyria 3 Clip دائمًا مقطعًا مدته **30 ثانية**. لإنشاء مقطع، استدعِ طريقة `interactions.create` مع طلب نصي. يتضمّن الرد دائمًا كلمات الأغنية التي تم إنشاؤها وبنيتها إلى جانب الصوت في مخطط `steps`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

يمكنك استرداد بيانات الموسيقى التي تم إنشاؤها باستخدام السمة `interaction.output_audio`، والتي تعرض آخر مقطع صوتي تم إنشاؤه. يمكنك أيضًا استرداد كلمات الأغنية وبنيتها باستخدام السمة `interaction.output_text`. للحصول على تفاصيل حول سمات التسهيل، يُرجى الاطّلاع على
[نظرة عامة على التفاعلات](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar#convenience-properties).

## إنشاء أغنية كاملة

استخدِم نموذج `lyria-3-pro-preview` لإنشاء أغانٍ كاملة الطول تستغرق بضع دقائق. يفهم نموذج Pro البنية الموسيقية ويمكنه إنشاء مقطوعات موسيقية تتضمّن مقاطع وأغاني متكررة وجسورًا موسيقية مميزة. يمكنك التأثير في المدة من خلال تحديدها في طلبك (مثلاً، "إنشاء أغنية مدتها دقيقتان") أو باستخدام [الطوابع الزمنية](#timing) لتحديد البنية.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## اختيار تنسيق الإخراج

تنشئ نماذج Lyria 3 المحتوى الصوتي بتنسيق **MP3** تلقائيًا. بالنسبة إلى Lyria 3 Pro، يمكنك أيضًا طلب الحصول على الناتج بتنسيق **WAV** من خلال ضبط `response_format`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## تحليل الردّ

يتضمّن الردّ من Lyria 3 عدة أقسام للمحتوى ضمن مخطط `steps`.
تعرض التفاعلات سلسلة من الخطوات، حيث تحتوي خطوات `model_output` على المحتوى الذي تم إنشاؤه.
تحتوي مربّعات المحتوى النصي على كلمات الأغنية التي تم إنشاؤها أو وصف بتنسيق JSON لبنية الأغنية.
تحتوي كتل المحتوى من النوع `audio` على بيانات الصوت المشفرة بترميز Base64.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### كلمات الأغاني والموسيقى المتداخلة

بما أنّ المحتوى الناتج من Lyria 3 معقّد ويحتوي على خطوات وكتل منفصلة للكلمات التي تم إنشاؤها (نص) والأغنية نفسها (صوت)، توفّر خصائص الراحة اختصارًا سريعًا وموصى به.

ومع ذلك، إذا كنت تريد التحكّم الكامل آليًا في المخطط الزمني الأولي للخطوات الذي يعرضه الخادم (مثل تسجيل كلّ جزء من المحتوى عند استلامه)، يمكنك تكرار `steps` يدويًا بدلاً من ذلك:

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

## إنشاء موسيقى من الصور

يتوافق Lyria 3 مع الإدخالات المتعدّدة الوسائط، إذ يمكنكم تقديم ما يصل إلى **10 صور**
إلى جانب الطلب النصي في قائمة `input`، وسيقوم النموذج بتأليف موسيقى
مستوحاة من المحتوى المرئي.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## تقديم كلمات أغنية مخصّصة

يمكنك كتابة كلمات الأغنية الخاصة بك وتضمينها في الطلب. استخدِم علامات الأقسام، مثل `[Verse]` و`[Chorus]` و`[Bridge]`، لمساعدة النموذج في فهم بنية الأغنية:

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## التحكّم في التوقيت والبنية

يمكنك تحديد ما يحدث بالضبط في لحظات معيّنة من الأغنية باستخدام الطوابع الزمنية. يفيد ذلك في التحكّم في وقت بدء الآلات الموسيقية ووقت عرض كلمات الأغنية وطريقة تقدّم الأغنية:

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## إنشاء مقاطع صوتية بدون غناء

بالنسبة إلى الموسيقى في الخلفية أو المقاطع الصوتية للألعاب أو أي حالة استخدام لا تتطلّب أصواتًا بشرية، يمكنك أن تطلب من النموذج إنشاء مقاطع صوتية موسيقية فقط:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## إنشاء موسيقى بلغات مختلفة

تنشئ Lyria 3 كلمات الأغاني باللغة التي تستخدمها في طلبك. لإنشاء أغنية
بكلمات فرنسية، اكتب طلبك باللغة الفرنسية. ويعدّل النموذج أسلوبه الصوتي وطريقة لفظه لتتطابق مع اللغة.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## ذكاء النموذج

تحلّل Lyria 3 عملية الطلب التي تقدّمها، حيث يستند النموذج إلى بنية موسيقية (مقدمة، مقطع، لازمة، جسر موسيقي، وما إلى ذلك) بناءً على طلبك.
يحدث ذلك قبل إنشاء الصوت، ويضمن التماسك البنيوي والخصائص الموسيقية.

## الدليل الإرشادي لكتابة الطلبات

كلما كان طلبك أكثر تحديدًا، كانت النتائج أفضل. في ما يلي ما يمكنك تضمينه لتوجيه عملية الإنشاء:

- **النوع**: حدِّد نوعًا أو مزيجًا من الأنواع (مثلاً "هيب هوب منخفض الدقة" أو "موسيقى جاز" أو "موسيقى أوركسترا سينمائية").
- **الآلات الموسيقية**: اسم الآلات الموسيقية المحدّدة (مثلاً "بيانو Fender Rhodes" أو "غيتار منزلق" أو "آلة الطبول TR-808")
- **عدد النبضات في الدقيقة**: ضبط الإيقاع (مثلاً، "120 نبضة في الدقيقة"، "إيقاع بطيء يبلغ حوالي 70 نبضة في الدقيقة")
- **المفتاح الموسيقي/السلم الموسيقي**: حدِّد مفتاحًا موسيقيًا (مثل "في سلم G الكبير" أو "في سلم D الصغير").
- **المزاج والأجواء**: استخدِم صفات وصفية (مثل "حنين" أو "عدواني" أو "أثيري" أو "حالم").
- **البنية**: استخدِم علامات مثل `[Verse]` أو `[Chorus]` أو `[Bridge]` أو `[Intro]` أو `[Outro]` أو الطوابع الزمنية للتحكّم في تقدّم الأغنية.
- **المدة**: ينتج نموذج "المقطع" دائمًا مقاطع مدتها 30 ثانية. بالنسبة إلى طراز Pro، حدِّد المدة المطلوبة في طلبك (مثلاً، "أريد إنشاء أغنية مدتها دقيقتان") أو استخدِم الطوابع الزمنية للتحكّم في المدة.

### أمثلة على الطلبات

إليك بعض الأمثلة على الطلبات الفعّالة:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## أفضل الممارسات

- **التكرار باستخدام Clip أولاً** استخدِم النموذج الأسرع `lyria-3-clip-preview` لتجربة الطلبات قبل الالتزام بإنشاء أغنية كاملة باستخدام `lyria-3-pro-preview`.
- **الدقة** تؤدي الطلبات الغامضة إلى نتائج عامة. اذكر الآلات الموسيقية وسرعة الإيقاع والمفتاح الموسيقي والحالة المزاجية والبنية للحصول على أفضل نتيجة.
- **مطابقة لغتك** اكتب الطلب باللغة التي تريد عرض كلمات الأغنية بها.
- **استخدام علامات الأقسام:** تمنح العلامات `[Verse]` و`[Chorus]` و`[Bridge]` النموذج بنية واضحة يجب اتّباعها.
- **فصل كلمات الأغنية عن التعليمات:** عند تقديم كلمات أغنية مخصّصة، يجب فصلها بوضوح عن تعليمات التوجيه الموسيقي.

## القيود

- **الأمان**: تتحقّق فلاتر الأمان من جميع الطلبات. سيتم حظر الطلبات التي تؤدي إلى تشغيل الفلاتر. ويشمل ذلك الطلبات التي تطلب أصوات فنّانين معيّنين أو إنشاء كلمات أغاني محمية بحقوق الطبع والنشر.
- **وضع العلامات المائية**: تتضمّن جميع المقاطع الصوتية التي يتم إنشاؤها [علامة مائية لمقطع صوتي من SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ar) لتحديدها. هذه العلامة المائية غير مسموعة بالأذن البشرية ولا تؤثر في تجربة الاستماع.
- **التعديل على دفعات**: إنشاء الموسيقى هو عملية تتم في خطوة واحدة.
  لا يتيح الإصدار الحالي من Lyria 3 تعديل المقاطع التي تم إنشاؤها أو تحسينها بشكل متكرر من خلال طلبات متعددة.
- **المدة**: ينشئ نموذج "المقطع" دائمًا مقاطع مدتها 30 ثانية. ينشئ نموذج Pro أغاني تستغرق بضع دقائق، ويمكن التأثير في المدة الدقيقة من خلال الطلب.
- **الحتمية**: قد تختلف النتائج بين الطلبات، حتى مع استخدام الطلب نفسه.

## الخطوات التالية

- اطّلِع على [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) لنماذج Lyria 3.
- جرِّب [إنشاء الموسيقى في الوقت الفعلي](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ar)
  باستخدام Lyria RealTime،
- إنشاء محادثات بين عدة أشخاص باستخدام
  [نماذج تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar)
- تعرَّف على كيفية إنشاء [صور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) أو [فيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar).
- تعرَّف على كيفية [فهم Gemini للملفات الصوتية](https://ai.google.dev/gemini-api/docs/audio?hl=ar)،
- إجراء محادثة في الوقت الفعلي مع Gemini باستخدام
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
