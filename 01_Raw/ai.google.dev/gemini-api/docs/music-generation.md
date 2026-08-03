---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=hi
fetched_at: 2026-08-03T04:27:04.713257+00:00
title: "Lyria 3 \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u092e\u094d\u092f\u0942\u091c\u093c\u093f\u0915 \u091c\u0928\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Lyria 3 की मदद से म्यूज़िक जनरेट करना

Lyria 3, Google के संगीत जनरेट करने की सुविधा मॉडल का परिवार है. यह Gemini API के ज़रिए उपलब्ध है. Lyria 3 की मदद से, टेक्स्ट प्रॉम्प्ट या इमेज से हाई-क्वालिटी वाला 44.1 kHz स्टीरियो ऑडियो जनरेट किया जा सकता है. ये मॉडल, स्ट्रक्चरल कोहेरेंस (संगीत के अलग-अलग हिस्सों के बीच तालमेल) देते हैं. इनमें वोकल, टाइम किए गए गाने के बोल, और इंस्ट्रुमेंटल अरेंजमेंट शामिल हैं.

Lyria 3 के परिवार में दो मॉडल शामिल हैं:

| मॉडल | मॉडल आईडी | इन स्थितियों में बेहतर है | कुल समय | आउटपुट |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | शॉर्ट क्लिप, लूप, प्रिव्यू | 30 सेकंड | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | वर्सेज़, कोरस, ब्रिज वाले पूरे गाने | कुछ मिनट (प्रॉम्प्ट का इस्तेमाल करके कंट्रोल किया जा सकता है) | MP3 |

इन दोनों मॉडल का इस्तेमाल, नए
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) की मदद से किया जा सकता है. यह मल्टीमॉडल
इनपुट (टेक्स्ट और इमेज) के साथ काम करता है. साथ ही, **44.1 kHz हाई-फ़िडेलिटी स्टीरियो**
ऑडियो जनरेट करता है.

## म्यूज़िक क्लिप जनरेट करना

Lyria 3 Clip मॉडल हमेशा **30 सेकंड** की क्लिप जनरेट करता है. क्लिप जनरेट करने के लिए, टेक्स्ट प्रॉम्प्ट के साथ `interactions.create` तरीके को कॉल करें. जवाब में, जनरेट किए गए गाने के बोल और गाने का स्ट्रक्चर, `steps` स्कीमा में ऑडियो के साथ हमेशा शामिल होता है.

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

`interaction.output_audio` प्रॉपर्टी का इस्तेमाल करके, जनरेट किए गए म्यूज़िक का डेटा वापस पाया जा सकता है. यह प्रॉपर्टी, जनरेट किए गए ऑडियो के आखिरी ब्लॉक को वापस करती है. `interaction.output_text` प्रॉपर्टी का इस्तेमाल करके, गाने के बोल और स्ट्रक्चर भी वापस पाया जा सकता है. सुविधा के लिए दी गई प्रॉपर्टी के बारे में ज़्यादा जानने के लिए, [Interactions की खास जानकारी देखें](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi#convenience-properties).

## पूरा गाना जनरेट करना

`lyria-3-pro-preview` मॉडल का इस्तेमाल करके, पूरे गाने जनरेट किए जा सकते हैं. इनकी अवधि कुछ मिनट होती है. Pro मॉडल, म्यूज़िकल स्ट्रक्चर को समझता है. साथ ही, अलग-अलग वर्सेज़, कोरस, और ब्रिज वाले कंपोज़िशन बना सकता है. प्रॉम्प्ट में अवधि तय करके (उदाहरण के लिए, "दो मिनट का गाना बनाएं") या स्ट्रक्चर तय करने के लिए [टाइमस्टैंप](#timing) का इस्तेमाल करके, अवधि को कंट्रोल किया जा सकता है.

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

## आउटपुट फ़ॉर्मैट चुनना

डिफ़ॉल्ट रूप से, Lyria 3 मॉडल, **MP3** फ़ॉर्मैट में ऑडियो जनरेट करते हैं. Lyria 3 Pro के लिए, `response_format` सेट करके, **WAV** फ़ॉर्मैट में भी आउटपुट का अनुरोध किया जा सकता है.

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

## जवाब को पार्स करना

Lyria 3 के जवाब में, `steps` स्कीमा में कॉन्टेंट के कई ब्लॉक शामिल होते हैं.
Interactions, चरणों का क्रम दिखाते हैं. इनमें `model_output` चरणों में, जनरेट किया गया कॉन्टेंट शामिल होता है.
टेक्स्ट कॉन्टेंट ब्लॉक में, जनरेट किए गए गाने के बोल या गाने के स्ट्रक्चर का JSON ब्यौरा शामिल होता है.
`audio` टाइप वाले कॉन्टेंट ब्लॉक में, base64 एन्कोड किया गया ऑडियो डेटा शामिल होता है.

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

#### इंटरलीव्ड गाने के बोल और संगीत

Lyria 3 से मिलने वाला आउटपुट मुश्किल होता है. इसमें जनरेट किए गए गाने के बोल (टेक्स्ट) और गाने (ऑडियो) के लिए अलग-अलग चरण और ब्लॉक शामिल होते हैं. इसलिए, सुविधा के लिए दी गई प्रॉपर्टी, तेज़ और सुझाया गया शॉर्टकट उपलब्ध कराती हैं.

हालांकि, अगर आपको सर्वर से मिले चरणों की रॉ टाइमलाइन पर पूरा, प्रोग्रामैटिक कंट्रोल चाहिए (जैसे, मिलने पर कॉन्टेंट के अलग-अलग ब्लॉक को लॉग करना), तो इसके बजाय, मैन्युअल तरीके से `steps` को दोहराया जा सकता है:

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

## इमेज से संगीत जनरेट करना

Lyria 3, मल्टीमॉडल इनपुट के साथ काम करता है. `input` सूची में, टेक्स्ट प्रॉम्प्ट के साथ **10 इमेज** तक दी जा सकती हैं. मॉडल, विज़ुअल कॉन्टेंट से प्रेरित संगीत कंपोज़ करेगा.

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

## अपने हिसाब से गाने के बोल देना

अपने हिसाब से गाने के बोल लिखे जा सकते हैं और उन्हें प्रॉम्प्ट में शामिल किया जा सकता है. मॉडल को गाने का स्ट्रक्चर समझने में मदद करने के लिए, `[Verse]`, `[Chorus]`, और `[Bridge]` जैसे सेक्शन टैग का इस्तेमाल करें:

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

## टाइमिंग और स्ट्रक्चर कंट्रोल करना

टाइमस्टैंप का इस्तेमाल करके, यह तय किया जा सकता है कि गाने में खास पलों पर क्या होगा. यह कंट्रोल करने के लिए काम आता है कि इंस्ट्रुमेंट कब शुरू होंगे, गाने के बोल कब सुनाए जाएंगे, और गाना कैसे आगे बढ़ेगा:

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

## इंस्ट्रुमेंटल ट्रैक जनरेट करना

बैकग्राउंड म्यूज़िक, गेम साउंडट्रैक या ऐसे किसी भी इस्तेमाल के लिए जहां वोकल की ज़रूरत नहीं है, मॉडल को सिर्फ़ इंस्ट्रुमेंटल ट्रैक जनरेट करने के लिए प्रॉम्प्ट किया जा सकता है:

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

## अलग-अलग भाषाओं में संगीत जनरेट करना

Lyria 3, आपके प्रॉम्प्ट की भाषा में गाने के बोल जनरेट करता है. फ़्रेंच में गाने के बोल जनरेट करने के लिए, अपना प्रॉम्प्ट फ़्रेंच में लिखें. मॉडल, भाषा के हिसाब से अपनी वोकल स्टाइल और उच्चारण बदलता है.

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

## मॉडल की इंटेलिजेंस

Lyria 3, आपके प्रॉम्प्ट प्रोसेस का विश्लेषण करता है. इसमें मॉडल, आपके प्रॉम्प्ट के आधार पर म्यूज़िकल स्ट्रक्चर (इंट्रो, वर्स, कोरस, ब्रिज वगैरह) के हिसाब से काम करता है.
यह प्रोसेस, ऑडियो जनरेट होने से पहले होती है. इससे स्ट्रक्चरल कोहेरेंस (संगीत के अलग-अलग हिस्सों के बीच तालमेल) और म्यूज़िकैलिटी (संगीत की क्वालिटी) पक्का होती है.

## प्रॉम्प्ट से जुड़ी गाइड

आपका प्रॉम्प्ट जितना सटीक होगा, नतीजे उतने ही बेहतर होंगे. जनरेशन को गाइड करने के लिए, ये चीज़ें शामिल की जा सकती हैं:

- **शैली**: कोई शैली या शैलियों का मिश्रण तय करें. जैसे, "लो-फ़ाई हिप हॉप",
  "जैज़ फ़्यूज़न", "सिनेमैटिक ऑर्केस्ट्रल".
- **इंस्ट्रुमेंट**: खास इंस्ट्रुमेंट के नाम तय करें. जैसे, "फ़ेंडर रोड्स पियानो",
  "स्लाइड गिटार", "टीआर-808 ड्रम मशीन".
- **बीपीएम**: टेंपो सेट करें. जैसे, "120 बीपीएम", "करीब 70 बीपीएम का धीमा टेंपो".
- **की/स्केल**: म्यूज़िकल की तय करें. जैसे, "जी मेजर में", "डी माइनर".
- **मूड और माहौल**: जानकारी देने वाले विशेषणों का इस्तेमाल करें. जैसे, "नॉस्टैल्जिक",
  "एग्रेसिव", "इथीरियल", "ड्रीम".
- **स्ट्रक्चर**: गाने की प्रोग्रेस को कंट्रोल करने के लिए, `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]` जैसे टैग या टाइमस्टैंप का इस्तेमाल करें.
- **अवधि**: Clip मॉडल हमेशा 30 सेकंड की क्लिप जनरेट करता है. Pro मॉडल के लिए, अपने प्रॉम्प्ट में अवधि तय करें. जैसे, "दो मिनट का गाना बनाएं" या अवधि को कंट्रोल करने के लिए टाइमस्टैंप का इस्तेमाल करें.

### प्रॉम्प्ट के उदाहरण

यहां असरदार प्रॉम्प्ट के कुछ उदाहरण दिए गए हैं:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## सबसे सही तरीके

- **सबसे पहले, Clip मॉडल के साथ दोहराएं.** `lyria-3-pro-preview` मॉडल से पूरा गाना जनरेट करने से पहले, प्रॉम्प्ट के साथ एक्सपेरिमेंट करने के लिए, `lyria-3-clip-preview` मॉडल का इस्तेमाल करें. यह मॉडल, तेज़ी से काम करता है.
- **सटीक जानकारी दें.** अस्पष्ट प्रॉम्प्ट से सामान्य नतीजे मिलते हैं. बेहतर आउटपुट के लिए, इंस्ट्रुमेंट, बीपीएम, की, मूड, और स्ट्रक्चर के बारे में बताएं.
- **अपनी भाषा से मेल खाएं.** जिस भाषा में गाने के बोल चाहिए, उसी भाषा में प्रॉम्प्ट दें.
- **सेक्शन टैग का इस्तेमाल करें.** `[Verse]`, `[Chorus]`, `[Bridge]` टैग से मॉडल को फ़ॉलो करने के लिए साफ़ स्ट्रक्चर मिलता है.
- **गाने के बोल को निर्देशों से अलग करें.** अपने हिसाब से गाने के बोल देते समय, उन्हें म्यूज़िकल डायरेक्शन के निर्देशों से साफ़ तौर पर अलग करें.

## सीमाएं

- **सुरक्षा**: सभी प्रॉम्प्ट की जांच, सुरक्षा फ़िल्टर से की जाती है. फ़िल्टर को ट्रिगर करने वाले प्रॉम्प्ट ब्लॉक कर दिए जाएंगे. इनमें, किसी खास कलाकार की आवाज़ का अनुरोध करने वाले प्रॉम्प्ट या कॉपीराइट वाले गाने के बोल जनरेट करने का अनुरोध करने वाले प्रॉम्प्ट शामिल हैं.
- **वॉटरमार्किंग**: जनरेट किए गए सभी ऑडियो में, पहचान के लिए
  [SynthID ऑडियो वॉटरमार्क](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=hi) शामिल होता है. यह वॉटरमार्क, लोगों को सुनाई नहीं देता है. साथ ही, इससे सुनने के अनुभव पर कोई असर नहीं पड़ता है.
- **एक से ज़्यादा बार बदलाव करने की सुविधा**: संगीत जनरेट करने की सुविधा, एक बार की प्रोसेस है.
  Lyria 3 के मौजूदा वर्शन में, जनरेट की गई क्लिप में एक से ज़्यादा प्रॉम्प्ट के ज़रिए बार-बार बदलाव करने या उसे बेहतर बनाने की सुविधा उपलब्ध नहीं है.
- **अवधि**: Clip मॉडल हमेशा 30 सेकंड की क्लिप जनरेट करता है. Pro मॉडल, कुछ मिनट के गाने जनरेट करता है. प्रॉम्प्ट के ज़रिए, अवधि को कंट्रोल किया जा सकता है.
- **डिटरमिनिज़म**: एक ही प्रॉम्प्ट के साथ भी, कॉल के बीच नतीजे अलग-अलग हो सकते हैं.

## आगे क्या करना है

- Lyria 3 मॉडल की [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.
- Lyria RealTime की मदद से, [रीयल-टाइम में स्ट्रीमिंग संगीत जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=hi) आज़माएं.
- [टीटीएस मॉडल की मदद से, एक से ज़्यादा स्पीकर वाली बातचीत जनरेट करें.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)
- जानें कि [इमेज](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) या [वीडियो](https://ai.google.dev/gemini-api/docs/video?hl=hi) कैसे जनरेट किए जाते हैं.
- जानें कि Gemini, ऑडियो फ़ाइलों को कैसे [समझ सकता है](https://ai.google.dev/gemini-api/docs/audio?hl=hi).
- Live API का इस्तेमाल करके, Gemini के साथ रीयल-टाइम में बातचीत करें
  .

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
