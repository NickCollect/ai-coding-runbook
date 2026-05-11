---
source_url: https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=hi
fetched_at: 2026-05-11T05:09:31.455458+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# लिखाई को बोली में बदलने की सुविधा (टीटीएस)

Gemini API, टेक्स्ट इनपुट को एक या एक से ज़्यादा लोगों की आवाज़ वाले ऑडियो में बदल सकता है. इसके लिए, Gemini की टेक्स्ट को सुनने की सुविधा (टीटीएस) का इस्तेमाल किया जाता है.
लिखे गए शब्दों को सुनने की सुविधा (टीटीएस) को *[कंट्रोल किया जा सकता है](#controllable)*.
इसका मतलब है कि बातचीत को बेहतर बनाने के लिए, सामान्य भाषा का इस्तेमाल किया जा सकता है. साथ ही, ऑडियो की *स्टाइल*, *एक्सेंट*, *गति*, और *टोन* को कंट्रोल किया जा सकता है.

टीटीएस की सुविधा, [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) के ज़रिए उपलब्ध कराई गई स्पीच जनरेशन की सुविधा से अलग है. इसे इंटरैक्टिव, अनस्ट्रक्चर्ड ऑडियो, और मल्टीमॉडल इनपुट और आउटपुट के लिए डिज़ाइन किया गया है. लाइव एपीआई, बातचीत के दौरान कॉन्टेक्स्ट के हिसाब से जवाब देने में बेहतर है. वहीं, Gemini API के ज़रिए टीटीएस की सुविधा, उन स्थितियों के लिए तैयार की गई है जिनमें सटीक टेक्स्ट सुनाने की ज़रूरत होती है. साथ ही, स्टाइल और आवाज़ पर बारीकी से कंट्रोल करने की ज़रूरत होती है. जैसे, पॉडकास्ट या ऑडियो बुक जनरेट करना.

इस गाइड में, टेक्स्ट से एक या एक से ज़्यादा स्पीकर वाला ऑडियो जनरेट करने का तरीका बताया गया है.

## शुरू करने से पहले

पक्का करें कि Gemini के टेक्स्ट-टू-स्पीच (टीटीएस) की सुविधाओं के साथ Gemini 2.5 मॉडल के किसी वैरिएंट का इस्तेमाल किया जा रहा हो. इसके बारे में [साथ काम करने वाले मॉडल](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=hi#supported-models) सेक्शन में बताया गया है. सबसे अच्छे नतीजों के लिए, यह तय करें कि आपके इस्तेमाल के हिसाब से कौनसा मॉडल सबसे सही है.

[AI Studio में Gemini 2.5 के टीटीएस मॉडल की जाँच करें]

## एक व्यक्ति की आवाज़ में टीटीएस

टेक्स्ट को एक स्पीकर वाले ऑडियो में बदलने के लिए, रिस्पॉन्स मोड को "audio" पर सेट करें. इसके बाद, आवाज़ के नाम के साथ `speech_config` ऑब्जेक्ट पास करें.
आपको पहले से मौजूद [आउटपुट की आवाज़ों](#voices) में से किसी एक आवाज़ का नाम चुनना होगा.

इस उदाहरण में, मॉडल से मिले आउटपुट ऑडियो को वेव फ़ाइल में सेव किया गया है:

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

data = None
for step in interaction.steps:
    for content_block in step.content:
        if content_block.type == "audio":
            data = base64.b64decode(content_block.data)
            break
    if data:
        break
wave_file('out.wav', data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
   });

   let data = null;
   for (const step of interaction.steps) {
      for (const contentBlock of step.content) {
         if (contentBlock.type === 'audio') {
            data = contentBlock.data;
            break;
         }
      }
      if (data) break;
   }
   const audioBuffer = Buffer.from(data, 'base64');
   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## एक से ज़्यादा लोगों की आवाज़ में टीटीएस

एक से ज़्यादा स्पीकर से ऑडियो चलाने के लिए, आपको `multi_speaker_voice_config` ऑब्जेक्ट की ज़रूरत होगी. इसमें हर स्पीकर (दो तक) को `speaker_voice_config` के तौर पर कॉन्फ़िगर किया गया हो.
आपको हर `speaker` को उन नामों से तय करना होगा जिनका इस्तेमाल [प्रॉम्प्ट](#controllable) में किया गया है:

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_modalities=["audio"],
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

data = None
for step in interaction.steps:
   for content_block in step.content:
      if content_block.type == "audio":
         data = base64.b64decode(content_block.data)
         break
   if data:
      break
wave_file('out.wav', data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   let data = null;
   for (const step of interaction.steps) {
      for (const contentBlock of step.content) {
         if (contentBlock.type === 'audio') {
            data = contentBlock.data;
            break;
         }
      }
      if (data) break;
   }
   const audioBuffer = Buffer.from(data, 'base64');
   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_modalities": ["audio"],
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## प्रॉम्प्ट की मदद से, बोलने के तरीके को कंट्रोल करना

एक या एक से ज़्यादा स्पीकर के लिए, टीटीएस की स्टाइल, टोन, लहजे, और गति को कंट्रोल किया जा सकता है. इसके लिए, आम बोलचाल की भाषा में प्रॉम्प्ट दें.
उदाहरण के लिए, एक स्पीकर वाले प्रॉम्प्ट में यह कहा जा सकता है:

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

एक से ज़्यादा स्पीकर वाले प्रॉम्प्ट में, मॉडल को हर स्पीकर का नाम और उससे जुड़ी ट्रांसक्रिप्ट दें. हर स्पीकर के लिए अलग-अलग निर्देश भी दिए जा सकते हैं:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

अपनी बात को ज़्यादा असरदार बनाने के लिए, [आवाज़ का ऐसा विकल्प](#voices) इस्तेमाल करें जो आपकी बात की स्टाइल या उसमें मौजूद भावना के हिसाब से हो. उदाहरण के लिए, पिछले प्रॉम्प्ट में *एन्सेलडस* की सांस लेने की आवाज़ से "थका हुआ" और "उबाऊ" पर ज़ोर दिया जा सकता है. वहीं, *पक* की तेज़ आवाज़ से "उत्साहित" और "खुश" पर ज़ोर दिया जा सकता है.

## ऑडियो में बदलने के लिए प्रॉम्प्ट जनरेट करना

टीटीएस मॉडल सिर्फ़ ऑडियो आउटपुट देते हैं. हालांकि, पहले ट्रांसक्रिप्ट जनरेट करने के लिए [अन्य मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi) का इस्तेमाल किया जा सकता है. इसके बाद, उस ट्रांसक्रिप्ट को टीटीएस मॉडल को पढ़कर सुनाने के लिए भेजा जा सकता है.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3-flash-preview",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.steps[-1].content[0].text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_modalities=["audio"],
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)

# ...Code to stream or save the output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3-flash-preview",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.steps.at(-1).content[0].text,
   response_modalities: ['audio'],
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## आवाज़ के विकल्प

TTS मॉडल, `voice_name` फ़ील्ड में आवाज़ के इन 30 विकल्पों के साथ काम करते हैं:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | **Charon** -- *Informative* |
| **Kore** -- *Firm* | **Fenrir** -- *Excitable* | **Leda** -- *Youthful* |
| **Orus** -- *कंपनी* | **Aoede** -- *Breezy* | **Callirrhoe** -- *ईज़ी-गोइंग* |
| **ऑटोनो** -- *तेज रोशनी* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *आसानी से काम करने वाला* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *Clear* | **Algenib** -- *Gravelly* | **रसलगेथी** -- *जानकारी देने वाला* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *मैच्योर* | **Pulcherrima** -- *Forward* |
| **Achird** -- *Friendly* | **Zubenelgenubi** -- *कैज़ुअल* | **Vindemiatrix** -- *जेंटल* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Knowledgeable* | **Sulafat** -- *Warm* |

आपको इन सभी आवाज़ों के विकल्प यहां मिलेंगे

## इस्तेमाल की जा सकने वाली भाषाएं

टीटीएस मॉडल, इनपुट की भाषा का पता अपने-आप लगा लेते हैं. इन भाषाओं में यह सुविधा इस्तेमाल की जा सकती है:

| भाषा | BCP-47 कोड | भाषा | BCP-47 कोड |
| --- | --- | --- | --- |
| अरबी | ar | फ़िलिपीनी | fil |
| बांग्ला | bn | फ़िनिश | fi |
| डच | nl | गैलिशियन | gl |
| अंग्रेज़ी | en | जॉर्जियन | ka |
| फ़्रांसीसी | fr | ग्रीक | el |
| जर्मन | de | गुजराती | gu |
| हिन्दी | hi | हैतियन क्रिओल | ht |
| इंडोनेशियन | आईडी | हीब्रू | वह |
| इटैलियन | it | हंगेरियन | hu |
| जैपनीज़ | ja | आइसलैंडिक | है |
| कोरियाई | ko | जावानीज़ | jv |
| मराठी | mr | कन्नड़ | kn |
| पोलिश | pl | कोंकणी | kok |
| पॉर्चुगीज़ | pt | लाओ | lo |
| रोमेनियन | ro | लैटिन | la |
| रूसी | ru | लातवियन | lv |
| स्पैनिश | es | लिथुएनियन | lt |
| तमिल | ta | लक्ज़मबर्गिश | lb |
| तेलुगु | te | मैसेडोनियाई | mk |
| थाई | th | मैथिली | mai |
| तुर्किये | tr | मैलगासी | mg |
| उक्रेनियाई | uk | मलय | ms |
| वियतनामीज़ | vi | मलयालम | ml |
| अफ़्रीकान्स | af | मंगोलियन | mn |
| अल्बेनियन | sq | नेपाली | ne |
| अमहैरिक | am | नॉर्वेजियन, बुकमॉल | nb |
| आर्मीनियन | hy | नॉर्वेजियन, नायनॉर्स्क | nn |
| अज़रबैजानी | az | ओड़िया | या |
| बॉस्क | eu | पश्तो | ps |
| बेलारूसी | be | फ़ारसी | fa |
| बल्गैरियन | bg | पंजाबी | pa |
| बर्मीज़ | my | सर्बियन | sr |
| कैटलैन | ca | सिंधी | sd |
| सेबुआनो | ceb | सिंहली | si |
| चाइनीज़, मैंडरिन | cmn | स्लोवाक | sk |
| क्रोएशियन | घंटा | स्लोवेनियन | sl |
| चेक | cs | स्वाहिली | sw |
| डेनिश | da | स्वीडिश | sv |
| एस्टोनियन | et | उर्दू | ur |

## इन मॉडल के साथ काम करता है

| मॉडल | एक व्यक्ति बोल रहा है | मल्टीस्पीकर |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=hi) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=hi) | ✔️ | ✔️ |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=hi) | ✔️ | ✔️ |

## प्रॉम्प्ट से जुड़ी गाइड

**Gemini Native Audio Generation Text-to-Speech (TTS)** मॉडल, सामान्य टीटीएस मॉडल से अलग है. यह एक लार्ज लैंग्वेज मॉडल का इस्तेमाल करता है. इस मॉडल को ***यह न सिर्फ़ पता होता है कि क्या बोलना है, बल्कि यह भी पता होता है कि कैसे बोलना है***.

ऐडवांस प्रॉम्प्ट को मॉडल के लिए सिस्टम के निर्देश के तौर पर माना जा सकता है, ताकि मॉडल उनका पालन कर सके. इससे मॉडल को ज़्यादा कॉन्टेक्स्ट मिलता है और परफ़ॉर्मेंस को कंट्रोल करने में मदद मिलती है.

इस सुविधा को अनलॉक करने के लिए, उपयोगकर्ता खुद को डायरेक्टर के तौर पर देख सकते हैं. वे वर्चुअल वॉइस टैलेंट के लिए एक सीन सेट कर सकते हैं, ताकि वह परफ़ॉर्म कर सके. प्रॉम्प्ट बनाने के लिए, हम यहां दिए गए कॉम्पोनेंट इस्तेमाल करने का सुझाव देते हैं: **ऑडियो प्रोफ़ाइल**, जिसमें किरदार की मुख्य पहचान और टाइप के बारे में बताया गया हो; **सीन का ब्यौरा**, जिसमें माहौल और किरदार की भावनाओं के बारे में बताया गया हो; और **डायरेक्टर के नोट**, जिसमें स्टाइल, लहजे, और गति को कंट्रोल करने के बारे में ज़्यादा सटीक जानकारी दी गई हो.

बारीकी से निर्देश देने पर, उपयोगकर्ता मॉडल की कॉन्टेक्स्ट अवेयरनेस का फ़ायदा उठा सकते हैं.जैसे, किसी खास इलाके के लहज़े में बोलना, पैरालिंग्विस्टिक की खास सुविधाएं (जैसे, सांस लेने की आवाज़) या बोलने की गति. इससे, डाइनैमिक, स्वाभाविक, और भावपूर्ण ऑडियो परफ़ॉर्मेंस जनरेट की जा सकती हैं. बेहतर परफ़ॉर्मेंस के लिए, हमारा सुझाव है कि **ट्रांसक्रिप्ट** और निर्देशक के प्रॉम्प्ट एक जैसे हों. *इससे "कौन बोल रहा है"* की जानकारी, *"क्या कहा जा रहा है"* और *"कैसे कहा जा रहा है"* की जानकारी से मेल खाती है.

इस गाइड का मकसद, Gemini की टीटीएस ऑडियो जनरेशन सुविधा का इस्तेमाल करके ऑडियो अनुभव डेवलप करने के बारे में बुनियादी जानकारी देना और आइडिया जनरेट करना है. हमें यह देखने में खुशी होगी कि आपने क्या बनाया है!

### ऑडियो टैग

टैग, `[whispers]` या `[laughs]` जैसे इनलाइन मॉडिफ़ायर होते हैं. इनसे आपको डिलीवरी पर ज़्यादा कंट्रोल मिलता है. इनका इस्तेमाल करके, ट्रांसक्रिप्ट की किसी लाइन या सेक्शन की टोन, गति, और भावनात्मक स्थिति में बदलाव किया जा सकता है. इनका इस्तेमाल, परफ़ॉर्मेंस में इंटरजेक्शन और कुछ अन्य नॉन-वर्बल आवाज़ें जोड़ने के लिए भी किया जा सकता है. जैसे, `[cough]`, `[sighs]` या `[gasp]`.

टैग के काम करने और न करने से जुड़ी कोई पूरी सूची नहीं है. हमारा सुझाव है कि आप अलग-अलग भावनाओं और एक्सप्रेशन के साथ एक्सपेरिमेंट करें, ताकि आपको पता चल सके कि आउटपुट में क्या बदलाव होते हैं.

अगर आपकी ट्रांसक्रिप्ट अंग्रेज़ी में नहीं है, तो हमारा सुझाव है कि आप बेहतर नतीजों के लिए, अंग्रेज़ी ऑडियो टैग का इस्तेमाल करें.

**ऑडियो टैग का क्रिएटिव तरीके से इस्तेमाल करना**

ऑडियो टैग की मदद से, अलग-अलग तरह के नतीजे पाए जा सकते हैं. यहां कुछ उदाहरण दिए गए हैं. इनमें हर उदाहरण में एक ही बात कही गई है, लेकिन इस्तेमाल किए गए टैग के आधार पर नतीजे अलग-अलग हैं.

किसी लाइन की शुरुआत में टैग जोड़कर, डिलीवरी के लहजे में बदलाव किया जा सकता है. इससे स्पीकर को उत्साहित, बोर या अनिच्छुक दिखाया जा सकता है:

- `[excitedly]` नमस्ते, मैं टेक्स्ट को स्पीच में बदलने वाला नया मॉडल हूं. मैं किसी भी बात को कई अलग-अलग तरीकों से कह सकता हूं. आज मैं आपकी किस तरह मदद कर सकता हूं?
- `[bored]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[reluctantly]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…

टैग का इस्तेमाल, डिलीवरी की स्पीड को बदलने के लिए भी किया जा सकता है. इसके अलावा, स्पीड को अहमियत के साथ जोड़ने के लिए भी इनका इस्तेमाल किया जा सकता है:

- `[very fast]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[very slow]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[sarcastically, one painfully slow word at a time]` नमस्ते, मैं टेक्स्ट को
  बोली में बदलने वाला नया मॉडल हूँ…

आपके पास अलग-अलग सेक्शन को कंट्रोल करने का विकल्प भी होता है. इसका मतलब है कि आप एक हिस्से को धीरे से और दूसरे हिस्से को ज़ोर से बोल सकते हैं.

- `[whispers]` नमस्ते, मैं लिखाई को बोली में बदलने वाला नया मॉडल हूं. `[shouting]` मैं कई अलग-अलग तरीकों से बोल सकता हूं. `[whispers]` आज मैं आपकी किस तरह मदद कर सकता/सकती हूं

इसके अलावा, अपनी पसंद के किसी भी क्रिएटिव आइडिया को आज़माया जा सकता है:

- `[like a cartoon dog]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[like dracula]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…

आम तौर पर इस्तेमाल होने वाले टैग में ये शामिल हैं:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

टैग की मदद से, ट्रांसक्रिप्ट को तुरंत कंट्रोल किया जा सकता है. ज़्यादा कंट्रोल के लिए, इन्हें कॉन्टेक्स्ट प्रॉम्प्ट के साथ मिलाकर इस्तेमाल किया जा सकता है. इससे परफ़ॉर्मेंस की टोन और वाइब सेट की जा सकती है.

### प्रॉम्प्ट का स्ट्रक्चर

एक अच्छे प्रॉम्प्ट में ये एलिमेंट शामिल होने चाहिए, ताकि आपको बेहतर परफ़ॉर्मेंस मिल सके:

- **ऑडियो प्रोफ़ाइल** - इससे आवाज़ की पहचान तय होती है. इसमें किरदार की पहचान, टाइप, और उम्र, बैकग्राउंड वगैरह जैसी अन्य विशेषताएं शामिल होती हैं.
- **सीन** - इससे कहानी की शुरुआत होती है. इसमें आस-पास के माहौल और "वाइब", दोनों के बारे में बताया गया है.
- **डायरेक्टर के नोट** - परफ़ॉर्मेंस से जुड़ी गाइडेंस. इसमें यह बताया जा सकता है कि आपके वर्चुअल टैलेंट के लिए किन निर्देशों का पालन करना ज़रूरी है. उदाहरण के लिए, स्टाइल, सांस लेने का तरीका, गति, शब्दों का उच्चारण, और लहजा.
- **कॉन्टेक्स्ट का सैंपल** - इससे मॉडल को कॉन्टेक्स्ट के हिसाब से शुरुआती जानकारी मिलती है, ताकि आपका वर्चुअल ऐक्टर आपके सेट अप किए गए सीन में नैचुरल तरीके से एंट्री कर सके.
- **ट्रांसक्रिप्ट** - वह टेक्स्ट जिसे मॉडल बोलेगा. बेहतर परफ़ॉर्मेंस के लिए, ध्यान रखें कि ट्रांसक्रिप्ट का विषय और लिखने का तरीका, आपके दिए गए निर्देशों से मेल खाना चाहिए.
- **ऑडियो टैग** - ये ऐसे मॉडिफ़ायर होते हैं जिन्हें ट्रांसक्रिप्ट में डाला जा सकता है. इनसे टेक्स्ट के किसी हिस्से को डिलीवर करने का तरीका बदल जाता है. जैसे, `[whispers]` या `[shouting]`.

पूरे प्रॉम्प्ट का उदाहरण:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### ज़्यादा जानकारी देने वाली प्रॉम्प्टिंग की रणनीतियां

प्रॉम्प्ट के हर एलिमेंट को इस तरह से तोड़ें:

#### ऑडियो प्रोफ़ाइल

कम शब्दों में, किरदार की पर्सोना के बारे में जानकारी दें.

- **नाम.** अपने किरदार को नाम देने से, मॉडल को बेहतर तरीके से काम करने में मदद मिलती है. सीन और कॉन्टेक्स्ट सेट करते समय, किरदार का नाम इस्तेमाल करें
- **भूमिका.** सीन में किरदार की मुख्य पहचान और टाइप. जैसे, रेडियो डीजे, पॉडकास्टर, न्यूज़ रिपोर्टर वगैरह.

उदाहरण:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### दृश्य

सीन के लिए कॉन्टेक्स्ट सेट करें. इसमें लोकेशन, मूड, और माहौल की जानकारी शामिल करें, ताकि टोन और वाइब तय की जा सके. बताएं कि किरदार के आस-पास क्या हो रहा है और इसका उस पर क्या असर पड़ रहा है. सीन से, पूरे इंटरैक्शन के लिए एनवायरमेंटल कॉन्टेक्स्ट मिलता है. साथ ही, यह ऐक्टिंग परफ़ॉर्मेंस को हल्के और नैचुरल तरीके से गाइड करता है.

उदाहरण:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### डायरेक्टर के नोट

इस ज़रूरी सेक्शन में, परफ़ॉर्मेंस से जुड़े खास दिशा-निर्देश शामिल होते हैं. आपके पास अन्य सभी एलिमेंट को छोड़ने का विकल्प होता है. हालांकि, हमारा सुझाव है कि आप इस एलिमेंट को शामिल करें.

सिर्फ़ उन चीज़ों को तय करें जो परफ़ॉर्मेंस के लिए ज़रूरी हैं. साथ ही, इस बात का ध्यान रखें कि ज़्यादा जानकारी न दी गई हो. बहुत ज़्यादा सख्त नियम लागू करने से, मॉडल की क्रिएटिविटी सीमित हो जाएगी. साथ ही, इससे परफ़ॉर्मेंस खराब हो सकती है. भूमिका और सीन की जानकारी के साथ-साथ, परफ़ॉर्मेंस से जुड़े खास नियमों का भी ध्यान रखें.

आम तौर पर, **स्टाइल, पेसिंग, और ऐक्सेंट** के बारे में निर्देश दिए जाते हैं. हालांकि, मॉडल को सिर्फ़ इन्हीं निर्देशों के हिसाब से काम करने की ज़रूरत नहीं है. अपनी परफ़ॉर्मेंस के लिए ज़रूरी किसी भी अतिरिक्त जानकारी को शामिल करने के लिए, कस्टम निर्देश शामिल करें. साथ ही, ज़रूरत के हिसाब से ज़्यादा या कम जानकारी दें.

उदाहरण के लिए:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**स्टाइल:**

इससे जनरेट की गई स्पीच का टोन और स्टाइल सेट किया जाता है. परफ़ॉर्मेंस को बेहतर बनाने के लिए, इसमें उत्साहित, ऊर्जावान, शांत, बोर वगैरह जैसे शब्द शामिल करें. ज़्यादा से ज़्यादा जानकारी दें: *"Infectious enthusiasm. *"ऊर्जावान और उत्साही"* कहने के बजाय, "सुनने वाले को ऐसा लगना चाहिए कि वह किसी बड़े और दिलचस्प कम्यूनिटी इवेंट का हिस्सा है"* कहना ज़्यादा सही है.

इसके अलावा, वॉइसओवर इंडस्ट्री में लोकप्रिय शब्दों का भी इस्तेमाल किया जा सकता है. जैसे, "वोकल स्माइल". स्टाइल की जितनी चाहें उतनी विशेषताएं जोड़ी जा सकती हैं.

उदाहरण:

सिंपल इमोशन

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

ज़्यादा गहराई

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

पेचीदा लेवल

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**बोलने का लहजा:**

चुने गए ऐक्सेंट के बारे में जानकारी दो. प्रॉम्प्ट में जितनी ज़्यादा जानकारी दी जाएगी, नतीजे उतने ही बेहतर होंगे. उदाहरण के लिए, "*ब्रिटिश लहजा, जैसा कि क्रॉयडन, इंग्लैंड में सुना जाता है*" का इस्तेमाल करें, न कि "*ब्रिटिश लहजा*".

उदाहरण:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**पेसिंग:**

पूरे कॉन्टेंट में पेसिंग और पेस में बदलाव.

उदाहरण:

सिंपल

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

ज़्यादा गहराई

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

पेचीदा लेवल

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**इसे आज़माएं**

[TTS ऐप्लिकेशन](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=hi) पर, इन उदाहरणों को खुद आज़माकर देखें. साथ ही, Gemini को डायरेक्टर की कुर्सी पर बैठने दें. बेहतरीन परफ़ॉर्मेंस देने के लिए, इन बातों का ध्यान रखें:

- ध्यान रखें कि पूरा प्रॉम्प्ट एक जैसा हो. स्क्रिप्ट और निर्देश, दोनों मिलकर एक बेहतरीन परफ़ॉर्मेंस तैयार करते हैं.
- आपको हर चीज़ के बारे में बताने की ज़रूरत नहीं है. कभी-कभी, मॉडल को कुछ जानकारी अपने हिसाब से भरने देने से, जवाब ज़्यादा स्वाभाविक लगता है. (ठीक वैसे ही जैसे कोई टैलेंटेड ऐक्टर)
- अगर आपको स्क्रिप्ट लिखने या परफ़ॉर्म करने में कोई परेशानी आ रही है, तो Gemini से मदद लें.

## सीमाएं

- टीटीएस मॉडल, सिर्फ़ टेक्स्ट इनपुट ले सकते हैं और ऑडियो आउटपुट जनरेट कर सकते हैं.
- TTS सेशन में, [कॉन्टेक्स्ट विंडो](https://ai.google.dev/gemini-api/docs/long-context?hl=hi) की सीमा 32 हज़ार टोकन होती है.
- भाषा से जुड़ी सहायता के लिए, [भाषाएं](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=hi#languages) सेक्शन देखें.
- टीटीएस की सुविधा, स्ट्रीमिंग के साथ काम नहीं करती.

Gemini 3.1 Flash के टीटीएस प्रीव्यू मॉडल का इस्तेमाल करके स्पीच जनरेट करने पर, ये पाबंदियां लागू होती हैं:

- **प्रॉम्प्ट में दिए गए निर्देशों के हिसाब से आवाज़ न होना:** ऐसा हो सकता है कि मॉडल का आउटपुट, हमेशा चुने गए स्पीकर से मेल न खाए. इस वजह से, ऑडियो आपकी उम्मीद के मुताबिक नहीं होता. आवाज़ की टोन में अंतर होने से बचने के लिए (जैसे, किसी पुरुष की भारी आवाज़ का किसी छोटी लड़की की तरह बोलने की कोशिश करना), पक्का करें कि आपके प्रॉम्प्ट में लिखी गई टोन और कॉन्टेक्स्ट, चुने गए स्पीकर की प्रोफ़ाइल के हिसाब से हो.
- **लंबे आउटपुट की क्वालिटी:** कुछ मिनट से ज़्यादा समय के जनरेट किए गए आउटपुट में, आवाज़ की क्वालिटी और एकरूपता में अंतर आ सकता है. हमारा सुझाव है कि आप अपनी ट्रांसक्रिप्ट को छोटे-छोटे हिस्सों में बांट लें.
- **कभी-कभी टेक्स्ट टोकन मिलते हैं:** मॉडल कभी-कभी ऑडियो टोकन के बजाय टेक्स्ट टोकन दिखाता है. इस वजह से, सर्वर अनुरोध को पूरा नहीं कर पाता और `500` गड़बड़ी दिखाता है. ऐसा बहुत कम अनुरोधों में होता है. इसलिए, आपको अपने ऐप्लिकेशन में, अपने-आप फिर से कोशिश करने का लॉजिक लागू करना चाहिए, ताकि इन अनुरोधों को हैंडल किया जा सके.
- **प्रॉम्प्ट क्लासिफ़ायर के ज़रिए प्रॉम्प्ट को गलत तरीके से अस्वीकार करना:** अस्पष्ट प्रॉम्प्ट, स्पीच सिंथेसिस क्लासिफ़ायर को ट्रिगर नहीं कर पाते हैं. इस वजह से, अनुरोध अस्वीकार (`PROHIBITED_CONTENT`) हो जाता है या मॉडल, स्टाइल से जुड़े निर्देशों और डायरेक्टर के नोट को पढ़कर सुनाता है. अपने प्रॉम्प्ट की पुष्टि करें. इसके लिए, एक साफ़ तौर पर प्रीऐंबल जोड़ें. इसमें मॉडल को स्पीच सिंथेसाइज़ करने के निर्देश दिए गए हों. साथ ही, इसमें साफ़ तौर पर यह बताया गया हो कि बोली गई बातों का ट्रांसक्रिप्ट कहां से शुरू होता है.

## आगे क्या करना है

- Gemini का [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi), इंटरैक्टिव ऑडियो जनरेट करने के विकल्प देता है. इन्हें अन्य मोड के साथ इंटरलीव किया जा सकता है.
- ऑडियो *इनपुट* के साथ काम करने के लिए, [ऑडियो समझने की सुविधा](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=hi) गाइड पर जाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया."],[],[]]
