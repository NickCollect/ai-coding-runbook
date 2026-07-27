---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=ar
fetched_at: 2026-07-27T04:35:23.882326+00:00
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

‫Lyria 3 هي مجموعة نماذج من Google لإنشاء الموسيقى، وهي متاحة من خلال Gemini API. باستخدام Lyria 3، يمكنكم إنشاء ملفات صوتية ستيريو عالية الجودة بتردد 44.1 كيلوهرتز من الطلبات النصية أو من الصور. تقدّم هذه النماذج اتساقًا هيكليًا، بما في ذلك الغناء وكلمات الأغاني المحدّدة بوقت وترتيبات الآلات الموسيقية الكاملة.

تتضمّن مجموعة Lyria 3 نموذجين:

| الطراز | رقم تعريف الطراز | الخيار الأمثل مع | المدة | الناتج |
| --- | --- | --- | --- | --- |
| ‫**Lyria 3 Clip** | `lyria-3-clip-preview` | مقاطع قصيرة، حلقات، معاينات | ‫30 ثانية | MP3 |
| ‫**Lyria 3 Pro** | `lyria-3-pro-preview` | أغانٍ كاملة تتضمّن أبياتًا وجوقات وجسورًا | بضع دقائق (يمكن التحكّم فيها باستخدام الطلب) | MP3 |

يمكن استخدام كلا الطرازَين باستخدام واجهة برمجة التطبيقات الجديدة
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar)، التي تتيح إدخال بيانات متعددة الوسائط (نصوص وصور)، وتنتج ملفات صوتية **ستيريو عالية الجودة بتردد 44.1 كيلوهرتز**.

## إنشاء مقطع موسيقي

ينشئ نموذج Lyria 3 Clip دائمًا مقطعًا **مدته 30 ثانية**. لإنشاء مقطع، استدعوا طريقة `interactions.create` باستخدام طلب نصي. يتضمّن الرد دائمًا كلمات الأغنية التي تم إنشاؤها وبنية الأغنية إلى جانب الصوت في مخطط `steps`.

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

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

يمكنكم استرداد بيانات الموسيقى التي تم إنشاؤها باستخدام السمة `interaction.output_audio`، التي تعرض آخر كتلة صوتية تم إنشاؤها. يمكنكم أيضًا استرداد كلمات الأغنية وبنيتها باستخدام السمة `interaction.output_text`. لمعرفة تفاصيل حول السمات المريحة، يمكنكم الاطّلاع على نظرة عامة على
[Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar#convenience-properties).

## إنشاء أغنية كاملة

استخدِموا نموذج `lyria-3-pro-preview` لإنشاء أغانٍ كاملة تستغرق بضع دقائق. يفهم نموذج Pro البنية الموسيقية ويمكنه إنشاء مؤلفات تتضمّن أبياتًا وجوقات وجسورًا مميزة. يمكنكم التأثير في المدة من خلال تحديدها في طلبكم (مثل "إنشاء أغنية مدتها دقيقتان") أو باستخدام [الطوابع الزمنية](#timing) لتحديد البنية.

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

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## اختيار تنسيق الرد

تنشئ نماذج Lyria 3 تلقائيًا ملفات صوتية بتنسيق **MP3**. بالنسبة إلى Lyria 3 Pro، يمكنكم أيضًا طلب الناتج بتنسيق **WAV** من خلال ضبط `response_format`.

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

### راحة

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

## تحليل الرد

يحتوي الرد من Lyria 3 على عدة كتل محتوى ضمن مخطط `steps`.
تعرض Interactions سلسلة من الخطوات، حيث تحتوي خطوات `model_output` على المحتوى الذي تم إنشاؤه.
تحتوي كتل المحتوى النصي على كلمات الأغنية التي تم إنشاؤها أو وصف JSON لبنية الأغنية.
تحتوي كتل المحتوى من النوع `audio` على البيانات الصوتية المشفرة بترميز base64.

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

### راحة

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### كلمات الأغنية والموسيقى المتداخلتان

نظرًا إلى أنّ الناتج من Lyria 3 معقد، إذ يحتوي على خطوات وكتل منفصلة لكلمات الأغنية التي تم إنشاؤها (نص) والأغنية نفسها (صوت)، تقدّم السمات المريحة اختصارًا سريعًا وموصى به.

ومع ذلك، إذا كنتم تريدون تحكّمًا كاملاً على مستوى البرنامج في المخطط الزمني الأولي للخطوات التي يعرضها الخادم (مثل تسجيل كتل المحتوى الفردية عند استلامها)، يمكنكم تكرار `steps` يدويًا بدلاً من ذلك:

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

تتيح Lyria 3 إدخال بيانات متعددة الوسائط، إذ يمكنكم تقديم ما يصل إلى **10 صور** إلى جانب طلبكم النصي في قائمة `input` وسينشئ النموذج موسيقى مستوحاة من المحتوى المرئي.

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

### راحة

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

يمكنكم كتابة كلمات الأغنية الخاصة بكم وتضمينها في الطلب. استخدِموا علامات الأقسام، مثل `[Verse]` و`[Chorus]` و`[Bridge]` لمساعدة النموذج في فهم بنية الأغنية:

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

### راحة

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

يمكنكم تحديد ما يحدث بالضبط في لحظات معيّنة من الأغنية باستخدام الطوابع الزمنية. يفيد ذلك في التحكّم في وقت ظهور الآلات الموسيقية ووقت عرض كلمات الأغنية وكيفية تقدّم الأغنية:

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

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## إنشاء مقاطع موسيقية آلية

بالنسبة إلى الموسيقى الخلفية أو الموسيقى التصويرية للألعاب أو أي حالة استخدام لا يكون فيها الغناء مطلوبًا، يمكنكم الطلب من النموذج إنشاء مقاطع موسيقية آلية فقط:

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

### راحة

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

تنشئ Lyria 3 كلمات الأغنية باللغة التي تكتبون بها الطلب. لإنشاء أغنية بكلمات فرنسية، اكتبوا طلبكم بالفرنسية. يعدّل النموذج أسلوبه الصوتي ونطقه ليطابق اللغة.

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

### راحة

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

تحلّل Lyria 3 عملية الطلب التي تستخدمونها، حيث يحلّل النموذج البنية الموسيقية (المقدمة والبيت والجوقة والجسر وما إلى ذلك) استنادًا إلى طلبكم.
يحدث ذلك قبل إنشاء الصوت ويضمن الاتساق الهيكلي والجمالية الموسيقية.

## الدليل الإرشادي لكتابة الطلبات

كلما كان طلبكم أكثر تحديدًا، كانت النتائج أفضل. إليكم ما يمكنكم تضمينه لتوجيه عملية الإنشاء:

- **النوع**: حدِّدوا نوعًا أو مزيجًا من الأنواع (مثل "لو-فاي هيب هوب"،
  "جاز فيوجن"، "موسيقى أوركسترا سينمائية").
- **الآلات الموسيقية**: اذكروا آلات موسيقية معيّنة (مثل "بيانو Fender Rhodes"،
  "غيتار slide"، "آلة الطبول TR-808").
- **عدد النبضات في الدقيقة**: اضبطوا الإيقاع (مثل "120 نبضة في الدقيقة" أو "إيقاع بطيء حوالي 70 نبضة في الدقيقة").
- **المفتاح/السلم الموسيقي**: حدِّدوا مفتاحًا موسيقيًا (مثل "في سلم G الكبير" أو "في سلم D الصغير").
- **الحالة المزاجية والجو**: استخدِموا صفات وصفية (مثل "حنين" أو
  "عدواني" أو "أثيري" أو "حالم").
- **البنية**: استخدِموا علامات مثل `[Verse]` و`[Chorus]` و`[Bridge]` و`[Intro]` و
  `[Outro]` أو الطوابع الزمنية للتحكّم في تقدّم الأغنية.
- **المدة**: ينشئ نموذج Clip دائمًا مقاطع مدتها 30 ثانية. بالنسبة إلى نموذج Pro، حدِّدوا المدة المقصودة في طلبكم (مثل "إنشاء أغنية مدتها دقيقتان") أو استخدِموا الطوابع الزمنية للتحكّم في المدة.

### أمثلة على الطلبات

في ما يلي بعض الأمثلة على الطلبات الفعّالة:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## أفضل الممارسات

- **كرِّروا المحاولات باستخدام Clip أولاً.** استخدِموا نموذج `lyria-3-clip-preview` الأسرع لتجربة الطلبات قبل الالتزام بإنشاء أغنية كاملة باستخدام `lyria-3-pro-preview`.
- **الدقة** تنتج الطلبات الغامضة نتائج عامة. اذكروا الآلات الموسيقية وعدد النبضات في الدقيقة والمفتاح والحالة المزاجية والبنية للحصول على أفضل ناتج.
- **استخدِموا اللغة نفسها.** اكتبوا الطلب باللغة التي تريدون أن تكون كلمات الأغنية بها.
- **استخدِموا علامات الأقسام.** تمنح العلامات `[Verse]` و`[Chorus]` و`[Bridge]` النموذج بنية واضحة ليتبعها.
- **افصلوا كلمات الأغنية عن التعليمات.** عند تقديم كلمات أغنية مخصّصة، افصلوها بوضوح عن تعليماتكم المتعلقة بالاتجاه الموسيقي.

## القيود

- **الأمان**: تتحقّق فلاتر الأمان من جميع الطلبات. وسيتم حظر الطلبات التي تؤدي إلى تفعيل الفلاتر. ويشمل ذلك الطلبات التي تطلب أصوات فنانين معيّنين أو إنشاء كلمات أغنية محمية بموجب حقوق الطبع والنشر.
- **العلامات المائية**: يتضمّن كل ملف صوتي تم إنشاؤه
  [علامة SynthID مائية صوتية](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ar) لتحديد
  الهوية. لا يمكن للأذن البشرية ملاحظة هذه العلامة المائية ولا تؤثر في تجربة الاستماع.
- **التعديل عبر سلسلة من الطلبات**: إنشاء الموسيقى هو عملية تتم في طلب واحد.
  لا يتيح الإصدار الحالي من Lyria 3 التعديل التكراري أو تحسين مقطع تم إنشاؤه من خلال طلبات متعددة.
- **الطول**: ينشئ نموذج Clip دائمًا مقاطع مدتها 30 ثانية. ينشئ نموذج Pro أغانٍ تستغرق بضع دقائق، ويمكن التأثير في المدة الدقيقة من خلال طلبكم.
- **الحتمية**: قد تختلف النتائج بين المكالمات، حتى مع استخدام الطلب نفسه.

## الخطوات التالية

- يمكنكم الاطّلاع على [أسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) نماذج Lyria 3.
- يمكنكم تجربة [إنشاء الموسيقى في الوقت الفعلي وبشكل متواصل](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ar)
  باستخدام Lyria RealTime.
- يمكنكم إنشاء محادثات متعددة المتحدثين باستخدام نماذج تحويل النص إلى كلام.
- يمكنكم التعرّف على كيفية إنشاء [الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) أو [الفيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar).
- يمكنكم معرفة كيف يمكن أن يفهم Gemini [الملفات الصوتية](https://ai.google.dev/gemini-api/docs/audio?hl=ar).
- يمكنكم إجراء محادثة في الوقت الفعلي مع Gemini باستخدام الـ
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-16 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-16 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
