---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi
fetched_at: 2026-10-26T06:00:02.582550+00:00
title: "\u0932\u093f\u0916\u0947 \u0917\u090f \u0936\u092c\u094d\u0926\u094b\u0902 \u0915\u094b \u0938\u0941\u0928\u0928\u0947 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e (\u091f\u0940\u091f\u0940\u090f\u0938) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# लिखे गए शब्दों को सुनने की सुविधा (टीटीएस)

Gemini API, Gemini की लिखे गए शब्दों को सुनने की सुविधा (टीटीएस) जनरेशन केपबिलिटी का इस्तेमाल करके, टेक्स्ट इनपुट को एक स्पीकर या कई स्पीकर वाले ऑडियो में बदल सकता है.
टेक्स्ट को स्पीच में बदलने की सुविधा को *[कंट्रोल किया जा सकता है](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#controllable)*. इसका मतलब है कि ऑडियो की *स्टाइल*, *एक्सेंट*, *रफ़्तार*, और *टोन* को कंट्रोल करने के लिए, स्ट्रक्चर्ड टर्न मेटाडेटा (`speech_metadata`) और इनलाइन वोकल टैग को एक साथ इस्तेमाल किया जा सकता है.

टीटीएस की सुविधा, [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) के ज़रिए उपलब्ध कराई जाने वाली स्पीच जनरेशन की सुविधा से अलग है. Live API को इंटरैक्टिव, अनस्ट्रक्चर्ड ऑडियो, और मल्टीमोडल इनपुट और आउटपुट के लिए डिज़ाइन किया गया है. Live API, डाइनैमिक बातचीत के लिए बेहतरीन है. वहीं, Gemini API के ज़रिए टीटीएस का इस्तेमाल उन स्थितियों के लिए किया जाता है जिनमें टेक्स्ट को सटीक तरीके से पढ़ने की ज़रूरत होती है. साथ ही, स्टाइल और आवाज़ पर बारीकी से कंट्रोल की ज़रूरत होती है. जैसे, पॉडकास्ट या ऑडियो बुक जनरेट करना.

इस गाइड में, [Gemini 3.8 Flash टीटीएस](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) (`gemini-3.8-flash-tts`) और [Gemini 3.8 Flash-Lite टीटीएस](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) (`gemini-3.8-flash-lite-tts`) का इस्तेमाल करके, टेक्स्ट से सिंगल-स्पीकर और मल्टी-स्पीकर ऑडियो जनरेट करने का तरीका बताया गया है.

## शुरू करने से पहले

पक्का करें कि आपने [साथ काम करने वाले मॉडल](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#supported-models) सेक्शन में दिए गए Gemini TTS मॉडल का इस्तेमाल किया हो. साथ ही, Google GenAI SDK (Python के लिए `google-genai >= 2.25.0` या JavaScript/TypeScript के लिए `@google/genai >= 2.24.0`) के नए वर्शन पर अपग्रेड करें या REST API का इस्तेमाल करें.
बेहतर नतीजे पाने के लिए, [किस मॉडल का इस्तेमाल कब करना चाहिए](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#when-to-use-which-model) लेख पढ़ें. इससे आपको अपने वर्कलोड के लिए सबसे सही मॉडल चुनने में मदद मिलेगी.

ऐप्लिकेशन बनाना शुरू करने से पहले, [AI Studio में Gemini के टीटीएस मॉडल को टेस्ट करना](https://aistudio.google.com/generate-speech?hl=hi) आपके लिए फ़ायदेमंद हो सकता है.

## एक ही आवाज़ में टीटीएस

Gemini 3.8 टीटीएस मॉडल का इस्तेमाल करके, टेक्स्ट को सिंगल-स्पीकर ऑडियो में बदलने के लिए, `input` में हूबहू ट्रांसक्रिप्ट पास करें. साथ ही, `speech_metadata` एनोटेशन का इस्तेमाल करके, टर्न-लेवल स्टाइलिंग अटैच करें और `generation_config.speech_config` में अपनी आवाज़ कॉन्फ़िगर करें. पहले से मौजूद [वॉइस के विकल्पों](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#voices), एक्सटेंडेड वॉइस लाइब्रेरी (`GET /v1beta/voices`), कस्टम [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) आईडी (`voice_...`) या [वॉइस रेप्लिकेशन](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi) आईडी (`voice_...` या वैकल्पिक स्टेटलेस `voicekey_...`) में से कोई आवाज़ चुनी जा सकती है.

इस उदाहरण में, मॉडल से मिले डिफ़ॉल्ट WAV आउटपुट ऑडियो (`audio/wav`) को सीधे किसी फ़ाइल में सेव किया गया है:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

Python और JavaScript SDK में, जनरेट किए गए ऑडियो डेटा को वापस पाने के लिए, `interaction.output_audio` सुविधा प्रॉपर्टी का इस्तेमाल किया जा सकता है. यह प्रॉपर्टी, जनरेट किए गए आखिरी ऑडियो ब्लॉक को दिखाती है. रॉ REST JSON रिस्पॉन्स में, base64-encoded ऑडियो को `steps[].content[].data` में सेव किया जाता है. सुविधा प्रॉपर्टी के बारे में ज़्यादा जानने के लिए, [इंटरैक्शन की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi#convenience-properties) देखें.

## एक से ज़्यादा लोगों की आवाज़ में टीटीएस

एक से ज़्यादा स्पीकर वाले डायलॉग के लिए, `speech_config.speakers` में दो स्पीकर कॉन्फ़िगर करें. साथ ही, हर टर्न को अलग टेक्स्ट आइटम के तौर पर पास करें. इसमें `speech_metadata` एनोटेशन शामिल होना चाहिए, जो `speaker` और वैकल्पिक टर्न-लेवल `style` के बारे में बताता हो. ध्यान दें कि `speech_config`, एक स्पीकर के लिए अरे (`[{"voice": "..."}]`) और कई स्पीकर के लिए ऑब्जेक्ट (`{"speakers": [...]}`) स्वीकार करता है:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## मेटाडेटा और टैग की मदद से, बोलने के अंदाज़ को कंट्रोल करना

Gemini 3.8 टीटीएस, `text` फ़ील्ड को हूबहू ट्रांसक्रिप्ट के तौर पर इस्तेमाल करता है. स्टेज के निर्देशों को तेज़ आवाज़ में सुने बिना डिलीवरी को कंट्रोल करने के लिए, अपने निर्देशों को स्कोप के हिसाब से बांटें:

- **टर्न-लेवल पर लगातार डिलीवरी (`speech_metadata.style`):** `style` फ़ील्ड में, भावनाएं, डिलीवरी स्टाइल, प्रोसोडी, पेसिंग, और वॉल्यूम डालें. ये पूरे टर्न पर लागू होते हैं. उदाहरण के लिए, `"style": "whispered urgently"`, `"style": "out of breath"` या `"style": "warm and enthusiastic"`.
- **किसी समय पर होने वाले इवेंट (इनलाइन टैग):** कुछ समय के लिए बिना बोले आवाज़ में होने वाले बदलाव या ठहराव को सीधे तौर पर ट्रांसक्रिप्ट में शामिल करने के लिए, ऐंगल ब्रैकेट का इस्तेमाल करें. उदाहरण के लिए, `"Wait... <short pause> did you hear that? <sigh>"` या `"Excuse me <cough> as I was saying..."`.

सबसे सही तरीकों के बारे में ज़्यादा जानने के लिए, [प्रॉम्प्ट के लिए गाइड](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#prompting-guide) देखें.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Dr. Anya",
                    "style": "whispered urgently",
                }],
            },
            {
                "type": "text",
                "text": "<gasp> No way! <laugh> We've been searching for this species all season!",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Liam",
                    "style": "warm and enthusiastic",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Dr. Anya", "voice": "Kore"},
                {"speaker": "Liam", "voice": "Puck"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: 'Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Dr. Anya',
                  style: 'whispered urgently',
               }],
            },
            {
               type: 'text',
               text: "<gasp> No way! <laugh> We've been searching for this species all season!",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Liam',
                  style: 'warm and enthusiastic',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Dr. Anya', voice: 'Kore' },
               { speaker: 'Liam', voice: 'Puck' },
            ],
         },
      },
   });

   if (interaction.output_audio?.data) {
      const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
      fs.writeFileSync('out.wav', audioBuffer);
   }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Dr. Anya",
            "style": "whispered urgently"
          }]
        },
        {
          "type": "text",
          "text": "<gasp> No way! <laugh> We'\''ve been searching for this species all season!",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Liam",
            "style": "warm and enthusiastic"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "speakers": [
          { "speaker": "Dr. Anya", "voice": "Kore" },
          { "speaker": "Liam", "voice": "Puck" }
        ]
      }
    }
  }'
```

## स्ट्रीमिंग स्पीच जनरेशन

`stream: true` को सेट करके, जनरेट किए जा रहे ऑडियो को सिंथेसाइज़ होते समय स्ट्रीम किया जा सकता है. यूनरी अनुरोधों (जो RIFF हेडर के साथ पूरी WAV फ़ाइल दिखाते हैं) के उलट, **स्ट्रीमिंग अनुरोध डिफ़ॉल्ट रूप से हेडरलेस रॉ 16-बिट साइन्ड लिटिल-एंडियन लीनियर पीसीएम (`audio/l16`, 24 किलोहर्ट्ज़, मोनो) चंक दिखाते हैं**. इसलिए, ऑडियो चंक को कंटेनर हेडर के बिना लगातार चलाया या जोड़ा जा सकता है.

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## ऑडियो आउटपुट के फ़ॉर्मैट

Gemini 3.8 टीटीएस मॉडल, अलग-अलग डिफ़ॉल्ट ऑडियो फ़ॉर्मैट का इस्तेमाल करते हैं. यह इस बात पर निर्भर करता है कि अनुरोध यूनेरी है या स्ट्रीमिंग:

- **यूनरी अनुरोध (`stream=False`):** स्टैंडर्ड RIFF हेडर (24 किलोहर्ट्ज़, मोनो, 16-बिट साइंड लिटिल-एंडियन पीसीएम) के साथ पूरा **WAV (`audio/wav`)** ऑडियो वापस पाएं. डिकोड किए गए ऑडियो बाइट को सीधे `.wav` फ़ाइल में सेव किया जा सकता है. इसके लिए, WAV हेडर को मैन्युअल तरीके से जोड़ने की ज़रूरत नहीं है.
- **स्ट्रीमिंग के अनुरोध (`stream=True`):** डिफ़ॉल्ट रूप से, **बिना हेडर वाला रॉ लीनियर पीसीएम (`audio/l16`)** चंक (24 किलोहर्ट्ज़, मोनो, 16-बिट साइन्ड लिटिल-एंडियन पीसीएम) दिखाता है. इससे हर चंक पर कंटेनर हेडर के बिना, चंक को लगातार स्ट्रीम किया जा सकता है या जोड़ा जा सकता है.

ऑडियो को कोड में बदलने का कोई दूसरा तरीका या सैंपल रेट का अनुरोध करने के लिए, `response_format` में `mime_type` और वैकल्पिक `sample_rate` को कॉन्फ़िगर करें:

| फ़ॉर्मैट | `mime_type` की कीमत का | ब्यौरा |
| --- | --- | --- |
| **WAV** *(unary default)* | `"audio/wav"` | RIFF हेडर वाली अनकंप्रेस्ड WAV फ़ाइल (16-बिट साइन किया गया लिटिल-एंडियन पीसीएम, मोनो, 24 किलोहर्ट्ज़ डिफ़ॉल्ट). यूनरी अनुरोधों के लिए डिफ़ॉल्ट. |
| **Raw PCM (L16)** *(स्ट्रीमिंग के लिए डिफ़ॉल्ट)* | `"audio/l16"` | अनकंप्रेस्ड, हेडरलेस 16-बिट साइन्ड लिटिल-एंडियन लीनियर पीसीएम ऑडियो (24 किलोहर्ट्ज़, मोनो). स्ट्रीमिंग के अनुरोधों के लिए डिफ़ॉल्ट. |
| **Mu-law** | `"audio/mulaw"` | 8-बिट G.711 mu-law एन्कोडेड ऑडियो (आम तौर पर, उत्तरी अमेरिका और जापान के टेलीफ़ोनी/आईवीआर सिस्टम में इस्तेमाल किया जाता है). |
| **A-law** | `"audio/alaw"` | 8-बिट G.711 A-law एन्कोडेड ऑडियो (आम तौर पर, यूरोप और अंतरराष्ट्रीय टेलीफ़ोनी सिस्टम में इस्तेमाल किया जाता है). |

`sample_rate` को हर्ट्ज़ में भी बताया जा सकता है. उदाहरण के लिए, `24000`, `16000` या `8000`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### आराम का समय

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## बोलकर लिखवाने के विकल्प

Gemini 3.8 TTS में, आवाज़ें चुनने या बनाने के चार तरीके उपलब्ध हैं:

1. **पहले से मौजूद स्टूडियो वॉइस:** यहां दी गई टेबल में, 30 चुनिंदा आवाज़ें दी गई हैं.
2. **Extended Voice Library:** इसमें अलग-अलग भाषाओं, लहजों, और किरदारों के लिए सैकड़ों अतिरिक्त आवाज़ें उपलब्ध हैं. इन्हें `client.voices.list()` (`GET /v1beta/voices`) का इस्तेमाल करके ऐक्सेस किया जा सकता है.
3. **[वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi):** [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में नैचुरल लैंग्वेज में दी गई जानकारी से, पसंद के मुताबिक आवाज़ जनरेट करें या `POST /v1beta/voices` (`type="prompted"` का इस्तेमाल करें. इससे, `CreateVoice` और `GetVoice` में एक स्थायी `voice_...` आईडी और `sample_audio` WAV फ़ॉर्मैट में झलक मिलती है.
4. **[वॉइस रेप्लिकेशन](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi):** [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में या `POST /v1beta/voices` (`type="replicated"`, डिफ़ॉल्ट रूप से परसिस्टेंट `store=True` या वैकल्पिक स्टेटलेस `store=False`) का इस्तेमाल करके, रेफ़रंस और सहमति वाले ऑडियो से स्पीकर की आवाज़ को रेप्लिकेट करें.

### कस्टम वॉइस की सीमाएं और टीटीएल

| बोलकर लिखवाएँ | स्टोरेज मोड | कोटा / सीमा | डेटा का रखरखाव (टीटीएल) |
| --- | --- | --- | --- |
| **स्टेटफ़ुल आवाज़ें** (`voice_...`, प्रॉम्प्ट की गई या कॉपी की गई) | `store=True` | **हर प्रोजेक्ट के लिए 200 आवाज़ें** (प्रॉम्प्ट और रेप्लिकेट की गई आवाज़ों के बीच शेयर की जाती हैं) | **आखिरी बार इस्तेमाल करने के एक साल बाद\*** |
| **स्टेटलेस वॉइस की** (`voicekey_...`, रेप्लिका) | `store=False` | क्लाइंट की ओर से मैनेज किया जाने वाला | **सात दिन** |

\* **TTL एक्सटेंशन:** आवाज़ को सेव करके रखने की एक साल की अवधि, हर बार आवाज़ का इस्तेमाल करने पर रीसेट हो जाती है. जैसे, आवाज़ का इस्तेमाल करके टेक्स्ट को बोली में बदलने या रीमिक्स करने के लिए बेस वॉइस के तौर पर इस्तेमाल करने पर. अगर किसी आवाज़ का इस्तेमाल एक साल तक नहीं किया जाता है, तो उसे अपने-आप मिटा दिया जाता है.

### पहले से मौजूद आवाज़ें

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **पक** -- *उत्साह बढ़ाने वाला* | **Charon** -- *Informative* |
| **Kore** -- *Firm* | **Fenrir** -- *उत्साहित* | **Leda** -- *Youthful* |
| **Orus** -- *कंपनी* | **Aoede** -- *Breezy* | **Callirrhoe** -- *ईज़ी-गोइंग* |
| **Autonoe** -- *ब्राइट* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *आसानी से काम करने वाला* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *Clear* | **अल्जेनिब** -- *ग्रैवली* | **Rasalgethi** -- *जानकारी देने वाला* |
| **लाओमेडिया** -- *अपबीट* | **Achernar** -- *सॉफ़्ट* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *मैच्योर* | **पुल्कैरिमा** -- *फ़ॉरवर्ड* |
| **Achird** -- *दोस्ताना* | **Zubenelgenubi** -- *कैज़ुअल* | **Vindemiatrix** -- *जेंटल* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Knowledgeable* | **Sulafat** -- *Warm* |

### वॉइस लाइब्रेरी और फ़िल्टर करने की बेहतर सुविधा

ऊपर दी गई टेबल में मौजूद 30 स्टूडियो आवाज़ों के अलावा, **एक्सटेंडेड वॉइस लाइब्रेरी** में सैकड़ों अन्य आवाज़ें उपलब्ध हैं. ये आवाज़ें अलग-अलग भाषाओं, क्षेत्रीय लहज़ों, किरदारों, और डोमेन में उपलब्ध हैं. [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में, पूरी वॉइस लाइब्रेरी को इंटरैक्टिव तरीके से ब्राउज़ किया जा सकता है. साथ ही, इसे फ़िल्टर किया जा सकता है और इसकी जांच की जा सकती है. इसके अलावा, `client.voices.list()` (`GET /v1beta/voices`, `google-genai` 2.25.0+ / `@google/genai` 2.24.0+ का इस्तेमाल करके) का इस्तेमाल करके, इसे प्रोग्राम के हिसाब से क्वेरी किया जा सकता है.

`ListVoices`, सेव की गई आपकी कस्टम आवाज़ें दिखाता है. इनमें सबसे नई आवाज़ें पहले दिखती हैं. इसके बाद, पहले से तैयार कैटलॉग की वे आवाज़ें दिखती हैं जो आपके फ़िल्टर की शर्तों से मेल खाती हैं. जब सूची वाले फ़िल्टर के लिए एक से ज़्यादा वैल्यू पास की जाती हैं, तो उस फ़िल्टर में मौजूद **किसी भी** वैल्यू से मेल खाने वाली आवाज़ें दिखाई जाती हैं (`OR`). वहीं, अलग-अलग फ़िल्टर पैरामीटर `AND` के साथ जुड़ जाते हैं:

| पैरामीटर | टाइप | ब्यौरा |
| --- | --- | --- |
| `language_code` | `list[str]` | BCP-47 भाषा टैग (उदाहरण के लिए, `["en-US", "en-GB"]`). केस-इनसेंसिटिव एग्ज़ैक्ट मैच. |
| `region_code` | `list[str]` | ISO 3166-1 alpha-2 या UN M.49 क्षेत्र कोड (उदाहरण के लिए, `["US", "GB"]`). |
| `accent` | `list[str]` | क्षेत्रीय लहज़े के बारे में बताने वाले डिस्क्रिप्टर (उदाहरण के लिए, `["American", "British"]`). |
| `gender` | `list[str]` | लिंग की पहचान (`"female"`, `"male"` या `"neutral"`). |
| `pitch` | `list[str]` | आवाज़ की पिच का क्लासिफ़िकेशन (`"low"`, `"medium"` या `"high"`). |
| `persona` | `list[str]` | आवाज़ का व्यक्तित्व या किरदार का आर्किटाइप (उदाहरण के लिए, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (REST में `context`) | `list[str]` | इस्तेमाल करने के लिए सबसे सही डोमेन (उदाहरण के लिए, `["Audiobook", "Conversational", "News"]`). |
| `type` (Python में `type_`) | `list[str]` | आवाज़ के सोर्स के हिसाब से फ़िल्टर करें: `"prebuilt"`, `"prompted"` ([आवाज़ का डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi)) या `"replicated"` ([आवाज़ की नकल](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi)). |
| `search` | `str` | फ़्री-टेक्स्ट सबस्ट्रिंग सर्च, केस-इनसेंसिटिव तरीके से `display_name` और `description`, दोनों से मैच होती है. |
| `page_size` | `int` | हर पेज पर ज़्यादा से ज़्यादा कितनी आवाज़ें दिखाई जाएं. डिफ़ॉल्ट रूप से `50` और ज़्यादा से ज़्यादा `1000` आवाज़ें दिखाई जा सकती हैं. |
| `page_token` | `str` | `response.next_page_token` से मिला टोकन, ताकि नतीजों का अगला पेज फ़ेच किया जा सके. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### आराम का समय

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## इस्तेमाल की जा सकने वाली भाषाएं

टीटीएस मॉडल, इनपुट की भाषा का पता अपने-आप लगा लेते हैं.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi)
(`gemini-3.8-flash-tts`) **130 से ज़्यादा भाषाओं** में काम करता है. वहीं, [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi)
(`gemini-3.8-flash-lite-tts`) **100 से ज़्यादा भाषाओं** में काम करता है:

| भाषा | Gemini 3.8 Flash टीटीएस | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| एचनीज़ (ऐरेबिक स्क्रिप्ट) | ✔️ | ✔️ |
| अफ़्रीकान्स | ✔️ | ✔️ |
| आकान | ✔️ | ✔️ |
| अमहैरिक | ✔️ | ✔️ |
| आर्मीनियन | ✔️ | ✔️ |
| असमिया | ✔️ | ✔️ |
| अवधी | ✔️ | ✔️ |
| बालीनीज़ | ✔️ | ✔️ |
| बांग्ला | ✔️ | ✔️ |
| बंजार (ऐरेबिक स्क्रिप्ट) | ✔️ | — |
| बंजार (लैटिन स्क्रिप्ट) | ✔️ | ✔️ |
| बाश्कियर | ✔️ | — |
| बॉस्क | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| बेंबा | ✔️ | — |
| भोजपुरी | ✔️ | ✔️ |
| बोस्नियन | ✔️ | ✔️ |
| ब्‍यूगिनी | ✔️ | ✔️ |
| बल्गैरियन | ✔️ | ✔️ |
| बर्मीज़ | ✔️ | — |
| कैंटोनीज़ | ✔️ | ✔️ |
| कैटलैन | ✔️ | ✔️ |
| सेबुआनो | ✔️ | ✔️ |
| सेंट्रल कुर्दिश | ✔️ | ✔️ |
| छत्तीसगढ़ी | ✔️ | ✔️ |
| चाइनीज़ (हान्स स्क्रिप्ट) | ✔️ | ✔️ |
| चाइनीज़ (हंत स्क्रिप्ट) | ✔️ | ✔️ |
| क्राइमियन टाटर | ✔️ | — |
| क्रोएशियन | ✔️ | ✔️ |
| चेक | ✔️ | ✔️ |
| डैनिश | ✔️ | ✔️ |
| डच | ✔️ | ✔️ |
| ड्यूला | ✔️ | — |
| जोंगखा | ✔️ | — |
| मिस्री अरबी | ✔️ | ✔️ |
| अंग्रेज़ी | ✔️ | ✔️ |
| एस्टोनियन | ✔️ | ✔️ |
| फ़िलिपीनी | ✔️ | ✔️ |
| फ़िनिश | ✔️ | — |
| फ़्रांसीसी | ✔️ | ✔️ |
| गैलिशियन | ✔️ | ✔️ |
| गांदा | ✔️ | ✔️ |
| जॉर्जियन | ✔️ | ✔️ |
| जर्मन | ✔️ | ✔️ |
| ग्रीक | ✔️ | ✔️ |
| गुअरानी | ✔️ | — |
| गुजराती | ✔️ | ✔️ |
| हैतियन क्रिओल | ✔️ | ✔️ |
| हल्ह मंगोलियन | ✔️ | ✔️ |
| हौसा | ✔️ | ✔️ |
| हिब्रू | ✔️ | ✔️ |
| हिन्दी | ✔️ | ✔️ |
| हंगेरियन | ✔️ | ✔️ |
| आइसलैंडिक | ✔️ | ✔️ |
| इग्बो | ✔️ | — |
| ईलोको | ✔️ | ✔️ |
| इंडोनेशियन | ✔️ | ✔️ |
| ईरानी फ़ारसी | ✔️ | ✔️ |
| इटैलियन | ✔️ | ✔️ |
| जापानी | ✔️ | ✔️ |
| जावानीज़ | ✔️ | ✔️ |
| कबाइल | ✔️ | — |
| कांबा | ✔️ | ✔️ |
| कन्नड़ | ✔️ | ✔️ |
| कश्मीरी (ऐरेबिक स्क्रिप्ट) | ✔️ | ✔️ |
| कश्मीरी (देवनागरी लिपि) | ✔️ | ✔️ |
| कज़ाक | ✔️ | ✔️ |
| ख्मेर | ✔️ | ✔️ |
| किकुयू | ✔️ | ✔️ |
| किनयारवांडा | ✔️ | ✔️ |
| कॉन्गो | ✔️ | ✔️ |
| कोरियन | ✔️ | ✔️ |
| किर्गिज़ | ✔️ | ✔️ |
| लाओ | ✔️ | ✔️ |
| लैजालियन | ✔️ | — |
| लिंगाला | ✔️ | ✔️ |
| लिथुएनियन | ✔️ | — |
| लक्ज़मबर्गिश | ✔️ | — |
| मैसेडोनियन | ✔️ | ✔️ |
| मगही | ✔️ | ✔️ |
| मैथिली | ✔️ | ✔️ |
| मलयालम | ✔️ | ✔️ |
| मोल्टीज़ | ✔️ | ✔️ |
| मणिपुरी | ✔️ | ✔️ |
| मराठी | ✔️ | ✔️ |
| मिनांग्काबाउ (अरबी लिपि) | ✔️ | ✔️ |
| मिनांग्काबाउ (लैटिन स्क्रिप्ट) | ✔️ | — |
| मिज़ो | ✔️ | ✔️ |
| नेपाली (अलग भाषा) | ✔️ | ✔️ |
| नाइजीरियन फ़ुलफ़ुल्दे | ✔️ | ✔️ |
| उत्तरी अज़रबैजानी | ✔️ | ✔️ |
| नॉर्दर्न सोथो | ✔️ | ✔️ |
| नॉर्दर्न उज़्बेक | ✔️ | ✔️ |
| नॉर्वेजियन बोकमाल | ✔️ | ✔️ |
| नार्वेजियन नॉर्स्क | ✔️ | ✔️ |
| न्यान्जा | ✔️ | ✔️ |
| ओसीटन | ✔️ | — |
| ओड़िया (इंडिविजुअल लैंग्वेज) | ✔️ | ✔️ |
| पंगासिनान | ✔️ | — |
| पर्शन (अफ़ग़ानिस्तान) | ✔️ | ✔️ |
| पोलिश | ✔️ | ✔️ |
| पॉर्चुगीज़ | ✔️ | ✔️ |
| पंजाबी | ✔️ | ✔️ |
| रोमानियन | ✔️ | ✔️ |
| रूसी | ✔️ | ✔️ |
| संथाली | ✔️ | ✔️ |
| सर्बियन | ✔️ | ✔️ |
| सिंधी | ✔️ | — |
| सिंहला | ✔️ | ✔️ |
| स्लोवाक | ✔️ | ✔️ |
| स्लोवेनियन | ✔️ | — |
| सोमाली | ✔️ | — |
| दक्षिणी अज़रबैजानी | ✔️ | ✔️ |
| दक्षिणी पश्तो | ✔️ | ✔️ |
| साउदर्न सोथो | ✔️ | — |
| स्पैनिश | ✔️ | ✔️ |
| स्टैंडर्ड ऐरेबिक (ऐरेबिक स्क्रिप्ट) | ✔️ | ✔️ |
| स्टैंडर्ड ऐरेबिक (लैटिन स्क्रिप्ट) | ✔️ | ✔️ |
| स्टैंडर्ड लातवियन | ✔️ | ✔️ |
| स्टैंडर्ड मलय | ✔️ | ✔️ |
| स्वाहिली (इंडिविजुअल लैंग्वेज) | ✔️ | — |
| स्वाटी | ✔️ | — |
| स्वीडिश | ✔️ | — |
| ताजिक | ✔️ | — |
| तमिल | ✔️ | ✔️ |
| तेलुगु | ✔️ | ✔️ |
| थाई | ✔️ | — |
| तिग्रिन्या | ✔️ | — |
| टॉस्क अल्बानियन | ✔️ | — |
| टर्किश | ✔️ | ✔️ |
| विगर | ✔️ | — |
| वियतनामीज़ | ✔️ | ✔️ |

## इस्तेमाल किए जा सकने वाले मॉडल

| मॉडल | एक व्यक्ति बोल रहा है | एक से ज़्यादा स्पीकर | आवाज़ का डिज़ाइन | वॉइस रेप्लिकेशन |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite टीटीएस](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=hi) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=hi) | ✔️ | ✔️ | — | — |

### किस मॉडल का इस्तेमाल कब करना चाहिए

Gemini 3.8 के दोनों टीटीएस मॉडल, एक ही एपीआई स्कीमा और प्रॉम्प्ट फ़ॉर्मैट का इस्तेमाल करते हैं. इसलिए, एक पैरामीटर में बदलाव करके, इन दोनों मॉडल के बीच स्विच किया जा सकता है:

- **[Gemini 3.8 Flash टीटीएस](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi)
  (`gemini-3.8-flash-tts`)** का इस्तेमाल तब करें, जब आपको बेहतरीन आवाज़, बारीकियों के साथ ऐक्टिंग, और आवाज़ के उतार-चढ़ाव पर पूरा कंट्रोल चाहिए. यह स्टूडियो-ग्रेड के क्रिएटिव काम, कई लोगों के बीच होने वाले मुश्किल डायलॉग, आवाज़ में उतार-चढ़ाव वाले टैग, मुश्किल उच्चारण, क्षेत्रीय या कम बोली जाने वाली भाषाओं, और लंबी कहानियों के लिए सबसे सही है. इसके लिए, आवाज़ और रूम-टोन में स्थिरता की ज़रूरत होती है.
- **`gemini-3.1-flash-tts-preview` की जगह, [Gemini 3.8 Flash-Lite टीटीएस](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi)
  (`gemini-3.8-flash-lite-tts`)** का इस्तेमाल करें. यह तेज़ी से काम करता है और इसमें कम लागत लगती है. इसे बड़े पैमाने पर कॉन्टेंट बनाने, बातचीत करने वाले वॉइस एजेंट कैस्केड, तेज़ आवाज़ में कॉन्टेंट सुनाने की सुविधाओं, भरोसेमंद वॉइस रेप्लिकेशन, और प्रमुख भाषाओं में रोज़ाना एक स्पीकर की आवाज़ में कॉन्टेंट सुनाने के लिए ऑप्टिमाइज़ किया गया है.

### माइग्रेशन गाइड

अगर आपको `gemini-3.1-flash-tts-preview` या Gemini के टीटीएस मॉडल के पुराने वर्शन से Gemini 3.8 टीटीएस पर माइग्रेट करना है, तो:

1. **मोड़ के हिसाब से निर्देशों को `speech_metadata` में ले जाएं:** Gemini 3.8 टीटीएस, इनपुट किए गए टेक्स्ट को हूबहू ट्रांसक्रिप्ट के तौर पर लेता है. लगातार डिलीवरी के निर्देश (`style`—जैसे कि `"whispering"`, `"out of breath"` या `"speaking slowly"`) और स्पीकर लेबल (`speaker`) को ट्रांसक्रिप्ट टेक्स्ट में स्टेज के निर्देशों को एम्बेड करने के बजाय, स्ट्रक्चर्ड `speech_metadata` एनोटेशन में ले जाएं.
2. **सिर्फ़ कुछ समय के लिए होने वाली आवाज़ से जुड़ी घटनाओं के लिए, ऐंगल-ब्रैकेट वाले इनलाइन टैग इस्तेमाल करें:** कुछ समय के लिए होने वाली आवाज़ों और पॉज़ को ट्रांसक्रिप्ट में इनलाइन रखें. इसके लिए, ऐंगल ब्रैकेट (जैसे कि `<laugh>`, `<sigh>`, `<cough>`, `<breath>` या `<short pause>`) का इस्तेमाल करें. आवाज़ के इफ़ेक्ट वाले टैग (जैसे कि तालियां या धमक) का इस्तेमाल न करें और डिलीवरी स्टाइल को `speech_metadata.style` में रखें.
3. **एक से ज़्यादा स्पीकर वाले अनुरोधों में, हर टर्न पर `speaker` की जानकारी दें:** एक से ज़्यादा स्पीकर वाले अनुरोध में, हर टर्न पर `speech_metadata` के अंदर `speaker` की जानकारी साफ़ तौर पर दी जानी चाहिए. यह जानकारी, कॉन्फ़िगर किए गए स्पीकर में से किसी एक से मैच होनी चाहिए.
4. **वॉइस डिज़ाइन की मदद से, पहले से ही पर्सोना डिज़ाइन करें:** [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) में बनाई गई कस्टम आवाज़ से, कई पैराग्राफ़ वाले `"Audio Profile"` या `"Director's Notes"` ब्लॉक बदलें. इसके बाद, कम से कम या खाली `style` स्ट्रिंग वाले टीटीएस अनुरोधों के ज़रिए, उस `voice_...` आईडी को पास करें.
5. **एकल अनुरोधों पर, डिफ़ॉल्ट रूप से WAV (`audio/wav`) फ़ॉर्मैट में आउटपुट देने वाला खाता:** `gemini-3.1-flash-tts-preview` और इससे पहले के टीटीएस मॉडल (जो डिफ़ॉल्ट रूप से हेडरलेस रॉ पीसीएम `audio/l16` फ़ॉर्मैट में आउटपुट देते थे) के उलट, Gemini 3.8 TTS, एकल अनुरोधों के लिए डिफ़ॉल्ट रूप से स्टैंडर्ड RIFF हेडर के साथ WAV ऑडियो (`audio/wav`) फ़ॉर्मैट में आउटपुट देता है.
   - अगर आपके कोड ने पहले रॉ पीसीएम बाइट को WAV हेडर में रैप किया था (उदाहरण के लिए, Python के `wave` मॉड्यूल या `ffmpeg` का इस्तेमाल करके), तो मैन्युअल हेडर रैपर को हटाएं और मिले बाइट को सीधे `.wav` फ़ाइल में लिखें.
   - अगर आपकी पाइपलाइन को हेडरलेस रॉ पीसीएम, म्यू-लॉ या ए-लॉ ऑडियो की ज़रूरत है, तो `response_format.mime_type` को साफ़ तौर पर `"audio/l16"`, `"audio/mulaw"` या `"audio/alaw"` पर सेट करें. उदाहरण के लिए, Interactions API में `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` या `generateContent` में `AUDIO_L16`. [ऑडियो आउटपुट फ़ॉर्मैट](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#audio-output-formats) देखें.

## प्रॉम्प्ट से जुड़ी गाइड

Gemini 3.8 टीटीएस मॉडल, इनपुट टेक्स्ट को **हूबहू ट्रांसक्रिप्ट** के तौर पर इस्तेमाल करते हैं.
पहले के झलक वाले मॉडल में, स्टेज के निर्देश सादे टेक्स्ट में एम्बेड किए जाते थे. हालांकि, Gemini 3.8 TTS, टर्न-लेवल के निर्देशों (`speech_metadata`) को पॉइंट-इन-टाइम इनलाइन वोकल टैग से अलग करता है.

### स्टाइल फ़ील्ड बनाम इनलाइन टैग

परफ़ॉर्मेंस से जुड़े निर्देशों को स्कोप के हिसाब से बांटें:

- **टर्न-लेवल डिलीवरी (`speech_metadata.style`):** `speech_metadata` के `style` फ़ील्ड में, लगातार डिलीवरी वाले एट्रिब्यूट डालें. जैसे, भावना, लय, कुल रफ़्तार या डिलीवरी का स्टाइल (जैसे, `"whispering"`, `"out of breath"`, `"muttering"` या `"sarcastic"`). अगर आपको हर टर्न में एक जैसा कैरेक्टर और परफ़ॉर्मेंस चाहिए, तो [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) में जाकर पहले ही पर्सोना डिज़ाइन कर लें. इसके बाद, टर्न-लेवल पर ज़रूरी बदलाव करने के लिए, सिर्फ़ `style` का इस्तेमाल करें.
- **किसी समय पर होने वाले इवेंट (इनलाइन टैग):** ट्रांसक्रिप्ट में, कुछ समय के लिए बिना बोले की गई आवाज़, सांस लेने या रुकने की आवाज़ को ऐंगल ब्रैकेट (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`) का इस्तेमाल करके इनलाइन में रखें. सबसे अच्छी ऑडियो क्वालिटी के लिए, ऐंगल ब्रैकेट (`<...>`) का इस्तेमाल करें. साथ ही, बिना आवाज़ वाले साउंड इफ़ेक्ट के बजाय, इंसानों की आवाज़ों का इस्तेमाल करें.

| दायरा | कहां जोड़ें | उदाहरण |
| --- | --- | --- |
| **टर्न-लेवल** (पूरे टर्न में जारी रहता है) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **पॉइंट-इन-टाइम** (किसी खास शब्द पर होता है) | `text` (`<...>`) में इनलाइन | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### बोलने की रफ़्तार और विराम

रिदम और साइलेंस को तीन लेवल पर कंट्रोल किया जा सकता है:

- **विराम चिह्न और एलिप्सिस:** बातचीत में स्वाभाविक रूप से हिचकिचाहट दिखाने के लिए, कॉमा, डैश (`--`), और एलिप्सिस (`...`) का इस्तेमाल करें.
- **इनलाइन पॉज़ टैग:** स्क्रिप्ट में उन जगहों पर `<short pause>` या `<long pause>` डालें जहां स्पीकर को रुकना चाहिए:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **टर्न-लेवल पेस:** `speech_metadata` में `"style": "speaking rapidly"` या `"style": "speaking slowly"` सेट करें, ताकि पूरे टर्न के दौरान बोलने की रफ़्तार को कंट्रोल किया जा सके.

### प्रोसोडी और पिच

किसी टर्न में प्रोसोडी, पिच, और इन्फ़्लेक्शन को कंट्रोल करने के लिए, **`speech_metadata.style`** का इस्तेमाल करें. उदाहरण के लिए, `"style": "high pitch, cheerful and excited inflection"` या `"style": "monotone and flat"`. अगर डायलॉग के बीच में इमोशन या प्रोसोडी बदलती है, तो स्क्रिप्ट को अलग-अलग टर्न में बांटें. साथ ही, हर टर्न के लिए अलग-अलग `style` वैल्यू इस्तेमाल करें.

### ज़ोर देना

ट्रांसक्रिप्ट में कुछ शब्दों को कैपिटल लेटर में लिखें. साथ ही, विराम चिह्न और इनलाइन वोकल टैग का इस्तेमाल करें, ताकि मुख्य शब्दों पर नैचुरल वोकल स्ट्रेस डाला जा सके:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### बोलने में रुकावट और बोली के अलावा अन्य आवाज़ें

बिना बोले की जाने वाली मानवीय आवाज़ों को ऐंगल ब्रैकेट (`<...>`) का इस्तेमाल करके, उसी जगह पर इनलाइन करें जहां आवाज़ होनी चाहिए. सुझाए गए वोकल टैग में ये शामिल हैं:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### बैकचैनल और ओवरलैप होने वाली स्पीच

एक से ज़्यादा स्पीकर वाली बातचीत में, सुनने वाले की प्रतिक्रियाओं को पाइप कैरेक्टर (`|reaction|`) में रैप करें. ऐसा स्पीकर के टर्न के दौरान किया जाता है, ताकि नैचुरल बैकचैनल या ओवरलैपिंग स्पीच बनाई जा सके. इससे हर प्रतिक्रिया के लिए अलग टर्न नहीं लेना पड़ता.

- **बैकचैनल पर की गई छोटी बातचीत:** बोलने वाले व्यक्ति के बोलने के दौरान, सुनने वाले लोगों की छोटी प्रतिक्रियाएं (`|oh hmm|`,
  `|oh really?|`, `|absolutely|`) दिखाएं:
  - **टर्न 1 (स्पीकर A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **दूसरा टर्न (स्पीकर B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **तीसरी बारी (स्पीकर A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **एक साथ बोली गई और बीच-बीच में बोली गई आवाज़:** दो लोगों के एक साथ बोलने या बीच-बीच में बोलने की आवाज़ को सिम्युलेट करने के लिए, एक से ज़्यादा पाइप सेगमेंट का इस्तेमाल करें. यह सुविधा, `gemini-3.8-flash-tts` के साथ सबसे अच्छी तरह काम करती है:
  - **एक साथ काउंटडाउन/कोरस:** `"Let's surprise him on three |ok| ready?"` इसके बाद `"one. two. three. |happy| happy |birthday| birthday!"`
  - **स्पीकर की आवाज़ पूरी तरह से ओवरलैप हो रही है:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### जनरेट किए गए सभी वर्शन में एकरूपता बनाए रखना और क्या नहीं करना है

अपनी आवाज़ की पहचान को हर बार एक जैसा रखने के लिए, इन दिशा-निर्देशों का पालन करें:

- **वॉइस डिज़ाइन में, लंबे स्टाइल ब्लॉक के बजाय पहले से ही डिज़ाइन किए गए पर्सोना का इस्तेमाल करें:**
  पुराने मॉडल से लिए गए लंबे `"Audio Profile"` पैराग्राफ़ और कई बुलेट पॉइंट `"Director's Notes"`, वॉइस ड्रिफ़्ट की सबसे आम वजह हैं.
  [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) में उसी क्रिएटिव इंट्यूशन का इस्तेमाल करके, एक स्थायी कस्टम `voice_...` पर्सोना जनरेट करें. इसके बाद, टीटीएस कॉल के ज़रिए उस वॉइस आईडी का इस्तेमाल करें.
- **स्थिरता के लिए, आवाज़ के रेफ़रंस पर भरोसा करें (मेटा-निर्देशों को छोड़ें):**
  Gemini 3.8 टीटीएस मॉडल को सबसे पहले ऑडियो रेफ़रंस पर ऐंकर करने के लिए ट्रेन किया गया है.
  ऐसे निर्देश शामिल न करें जिनमें मॉडल को आवाज़ को स्थिर रखने के लिए कहा गया हो (जैसे कि `"do not switch speaker identity"` या `"maintain identical timbre"`)—ज़्यादा प्रॉम्प्ट टेक्स्ट से ड्रिफ़्ट बढ़ता है. स्टाइल से जुड़े ग़ैर-ज़रूरी निर्देश हटा दें. साथ ही, मॉडल को आवाज़ के रेफ़रंस के हिसाब से, नैचुरल तरीके से अलग-अलग स्टाइल में जवाब देने दें.
- **`style` में स्पीकर की ऐसी विशेषताओं को बदलने की कोशिश न करें जिन्हें बदला नहीं जा सकता:** `speech_metadata.style` में उम्र, लिंग, नाम या उच्चारण में स्थायी बदलावों को शामिल करने से बचें.
  इसके बजाय, Extended Voice Library से कोई क्षेत्रीय आवाज़ चुनें या [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) की मदद से कोई आवाज़ जनरेट करें.

### सुझाया गया वर्कफ़्लो

1. **एक बार में ही किरदार तैयार करें:** [आवाज़ डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) में अपना किरदार बनाएं या एक्सटेंडेड वॉइस लाइब्रेरी से ऐसी क्षेत्रीय आवाज़ चुनें जो आपकी टारगेट की गई भाषा और पर्सोना से मेल खाती हो.
2. **बोलचाल की भाषा में ट्रांसक्रिप्ट लिखें:** `text` को ज़्यादा से ज़्यादा स्वाभाविक बनाने के लिए, इसे बोलचाल की भाषा में ट्रांसक्रिप्ट के तौर पर लिखें. इसमें बातचीत के दौरान होने वाली स्वाभाविक रुकावटें और हिचकिचाहटें भी शामिल करें. उदाहरण के लिए, `"Oh uh yeah I think... hm, so that's interesting"`.
3. **सबसे पहले, सामान्य टीटीएस को आज़माएं:** सबसे पहले, अपनी ट्रांसक्रिप्ट को खाली `style` फ़ील्ड के साथ सिंथेसाइज़ करें. ज़्यादातर अनुरोधों के लिए, `style` निर्देश की ज़रूरत नहीं होती.
4. **बदलाव करने के लिए, सिर्फ़ छोटे `style` प्रॉम्प्ट जोड़ें:** सिर्फ़ उन टर्न के लिए एक छोटा `style` स्ट्रिंग (जैसे, `"casual, friendly"` या `"muttering, then reassuring"`) जोड़ें जिनमें डिलीवरी में खास बदलाव की ज़रूरत हो. साथ ही, जब आपको एक जैसी बेसलाइन चाहिए, तो टर्न के लिए उसी छोटे स्ट्रिंग का दोबारा इस्तेमाल करें.

### सिलसिलेवार बातचीत और वॉइस एजेंट

रीयल-टाइम में बातचीत करने वाले वॉइस एजेंट या सिलसिलेवार बातचीत वाले ऐप्लिकेशन बनाते समय:

- एलएलएम टेक्स्ट के अलग-अलग हिस्सों के लिए, **हर बार एक टीटीएस कॉल** करें.
- कॉन्फ़िगर किए गए `voice` (पहले से बने, डिज़ाइन किए गए `voice_...` या डुप्लीकेट किए गए `voice_...` / `voicekey_...`) को हर बार स्पीकर की पहचान करने दें. हर बार लंबी अवधि के किरदार की पर्सोना को फिर से न भेजें.
- हर बातचीत के लिए `style` फ़ील्ड को खाली छोड़ें या पूरी बातचीत के लिए एक छोटी स्ट्रिंग (जैसे, `"casual, friendly"`) भेजें.
- एजेंट के लंबे जवाबों को छोटे-छोटे हिस्सों में बांटें. इसके लिए, स्टाइल से जुड़े ज़्यादा बेहतर प्रॉम्प्ट का इस्तेमाल न करें.

## सीमाएं

- टीटीएस मॉडल, सिर्फ़ टेक्स्ट इनपुट स्वीकार करते हैं और सिर्फ़ ऑडियो आउटपुट जनरेट करते हैं.
- एक ही अनुरोध में कई स्पीकर के लिए ऑडियो जनरेट करने की सुविधा (`speech_config.speakers`), पहले से मौजूद आवाज़ों का इस्तेमाल करके ज़्यादा से ज़्यादा दो स्पीकर के लिए ऑडियो जनरेट कर सकती है. एक से ज़्यादा किरदार वाले डायलॉग में, कस्टम डिज़ाइन की गई (`voice_...`) या कॉपी की गई (`voice_...` / `voicekey_...`) आवाज़ों को एक साथ इस्तेमाल करने के लिए, हर किरदार के डायलॉग को अलग-अलग सिंथेसाइज़ करें.
  यूनरी अनुरोधों में `audio/wav` डिफ़ॉल्ट
  रूप से, 44 बाइट का RIFF हेडर होता है. इसलिए, रॉ पीसीएम (`{"type": "audio", "mime_type": "audio/l16"}`) का अनुरोध करें या
  24 किलोहर्ट्ज़ पीसीएम
  ऑडियो फ़्रेम को जोड़ने से पहले, हर टर्न से WAV हेडर हटाएं.
- **कस्टम वॉइस के लिए स्टोरेज की सीमाएं और TTL:**
  - **स्टेटफ़ुल आवाज़ें (`store=True`, प्रॉम्प्ट की गई या प्रतिरूप):** **हर प्रोजेक्ट के लिए ज़्यादा से ज़्यादा 200 आवाज़ें**. इनका **TTL (टाइम-टू-लाइव) एक साल** होता है.
  - **स्टेटलेस वॉइस की (`store=False`, `voicekey_...`):** **सात दिन का TTL**
    (टाइम-टू-लाइव).
- भाषा कवरेज के लिए, [उपलब्ध भाषाएं](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#languages) सेक्शन देखें.

## आगे क्या करना है

- [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) की मदद से, नैचुरल लैंग्वेज का इस्तेमाल करके अपनी पसंद के मुताबिक़ आवाज़ें बनाएं.
- [वॉइस रेप्लिकेशन](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi) में, किसी मौजूदा स्पीकर की आवाज़ को रेप्लिकेट करें.
- [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) और [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) मॉडल के पेजों पर जाकर, मॉडल की खास बातों की तुलना करें.
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) की मदद से, दोनों भाषाओं में इंटरैक्टिव ऑडियो की सुविधा का इस्तेमाल करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-12 (UTC) को अपडेट किया गया."],[],[]]
