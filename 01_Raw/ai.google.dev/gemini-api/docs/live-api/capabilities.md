---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=hi
fetched_at: 2026-09-21T05:57:18.925873+00:00
title: "Live API \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e\u0913\u0902 \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u0917\u093e\u0907\u0921 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Live API की सुविधाओं के बारे में गाइड

यह एक पूरी गाइड है. इसमें Live API के साथ उपलब्ध सुविधाओं और कॉन्फ़िगरेशन के बारे में बताया गया है.
लाइव एपीआई के बारे में खास जानकारी और इस्तेमाल के सामान्य उदाहरणों के लिए सैंपल कोड देखने के लिए, [लाइव एपीआई का इस्तेमाल शुरू करें](https://ai.google.dev/gemini-api/docs/live?hl=hi) पेज पर जाएं.

## शुरू करने से पहले

- **बुनियादी कॉन्सेप्ट के बारे में जानें:** अगर आपने अब तक ऐसा नहीं किया है, तो सबसे पहले [Live API का इस्तेमाल शुरू करना](https://ai.google.dev/gemini-api/docs/live?hl=hi)  पेज पढ़ें.
  इससे आपको Live API के बुनियादी सिद्धांतों, इसके काम करने के तरीके, और [लागू करने के अलग-अलग तरीकों](https://ai.google.dev/gemini-api/docs/live?hl=hi#implementation-approach) के बारे में जानकारी मिलेगी.
- **AI Studio में Live API आज़माएं:** ऐप्लिकेशन बनाना शुरू करने से पहले, [Google AI Studio](https://aistudio.google.com/app/live?hl=hi) में Live API आज़माएं. इससे आपको मदद मिल सकती है. Google AI Studio में Live API का इस्तेमाल करने के लिए, **स्ट्रीम करें** को चुनें.

## मॉडल की तुलना

यहां दी गई टेबल में, [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=hi), [ज़्यादा सोच-विचार करके जवाब देने वाला Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=hi), और [Gemini 3.1 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=hi) मॉडल के बीच के मुख्य अंतर को दिखाया गया है:

| सुविधा | Gemini 3.8 Live | Gemini 3.8 Live Extended Thinking | Gemini 3.1 Flash की लाइव प्रीव्यू सुविधा |
| --- | --- | --- | --- |
| **इसके लिए सुझाव दिया गया है** | आवाज़ से निर्देश देने वाले एजेंट की कम से कम रुकावट वाली सुविधाओं के लिए, यह डिफ़ॉल्ट विकल्प है. | इस मोड का इस्तेमाल तब करें, जब ज़्यादा गहराई से विश्लेषण की ज़रूरत हो. | झलक दिखाने वाला लेगसी मॉडल. हमारा सुझाव है कि आप [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=hi) पर अपडेट करें. |
| **[सोचना](#native-audio-output-thinking)** | काम करता है (जवाब में तर्क शामिल किए गए हैं). `thinkingLevel` का इस्तेमाल नहीं किया जा सकता (सेटअप से हटाएं). | काम करता है. कॉन्फ़िगर किया जा सकने वाला बैकग्राउंड रीज़निंग (`thinkingLevel`: `low`, `medium`, `high`; `minimal` काम नहीं करता). | यह `thinkingLevel` का इस्तेमाल करके, जवाब देने के लिए जानकारी के स्तर को कंट्रोल करता है. इसके लिए, `minimal`, `low`, `medium`, और `high` जैसी सेटिंग का इस्तेमाल किया जाता है. डिफ़ॉल्ट रूप से, इसे `minimal` पर सेट किया जाता है, ताकि इंतज़ार के समय को कम किया जा सके. [Live API के बारे में जानकारी](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=hi) देखें. |
| **[जवाब पाना](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentservercontent)** | एक सर्वर इवेंट में, एक साथ कॉन्टेंट के कई हिस्से शामिल हो सकते हैं. | एक सर्वर इवेंट में, एक साथ कॉन्टेंट के कई हिस्से शामिल हो सकते हैं. एसिंक्रोनस रीज़निंग चालू होने पर, `turnComplete: true` से यह पता नहीं चलता कि सेशन निष्क्रिय है. इसलिए, `interaction_status` (`IN_PROGRESS` बनाम `IDLE`) का इस्तेमाल करें. | किसी एक सर्वर इवेंट में, कॉन्टेंट के कई हिस्से एक साथ शामिल हो सकते हैं. उदाहरण के लिए, `inlineData` और ट्रांसक्रिप्ट. पक्का करें कि आपका कोड, हर इवेंट के सभी हिस्सों को प्रोसेस करता हो, ताकि कोई भी कॉन्टेंट न छूटे. |
| **[क्लाइंट का कॉन्टेंट](#incremental-updates)** | `send_client_content` को पूरे सेशन के लाइफ़साइकल के दौरान इस्तेमाल किया जा सकता है. इसके लिए, साफ़ तौर पर भूमिकाएं (`user` या `model`) तय की जाती हैं. `turn_complete=true`, जनरेट होने वाले कॉन्टेंट को तुरंत रोक देता है. | `send_client_content` को पूरे सेशन के लाइफ़साइकल के दौरान इस्तेमाल किया जा सकता है. इसके लिए, साफ़ तौर पर भूमिकाएं (`user` या `model`) तय की जाती हैं. `turn_complete=true`, जनरेट होने वाले कॉन्टेंट को तुरंत रोक देता है. | `send_client_content` को पूरे सेशन के लाइफ़साइकल के दौरान इस्तेमाल किया जा सकता है. इसके लिए, साफ़ तौर पर भूमिकाएं (`user` या `model`) तय की जाती हैं. `turn_complete=true`, जनरेट होने वाले कॉन्टेंट को तुरंत रोक देता है. |
| **[एसिंक्रोनस फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/live-tools?hl=hi#async-function-calling)** (`behavior: NON_BLOCKING`) | काम करता है (डिफ़ॉल्ट). `behavior: NON_BLOCKING` सेट करें या `behavior: BLOCKING` के साथ, पुराने सिस्टम के साथ काम करने वाले ब्लॉकिंग मोड का इस्तेमाल करें. फ़ंक्शन शेड्यूल करने की सुविधा (`SILENT`, `WHEN_IDLE`, `INTERRUPTED`) उपलब्ध है. | उपलब्ध है (सिर्फ़ एक साथ काम नहीं करने वाली प्रोसेस के लिए). सिर्फ़ `NON_BLOCKING` को लागू किया जा सकता है. ब्लॉकिंग मोड और फ़ंक्शन शेड्यूल करने की सुविधा मौजूद नहीं है. | यह सुविधा उपलब्ध नहीं है. फ़ंक्शन कॉलिंग सिर्फ़ क्रम में की जा सकती है. जब तक टूल का जवाब नहीं भेजा जाता, तब तक मॉडल जवाब देना शुरू नहीं करेगा. |

Gemini 3.8 Live पर माइग्रेट करने के लिए, [माइग्रेशन गाइड](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=hi#migrating) देखें.
Thinking के बारे में ज़्यादा जानने के लिए, [Thinking गाइड](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=hi) और [अपग्रेड गाइड](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=hi#upgrading) देखें.

## कनेक्शन बनाया जा रहा है

यहां दिए गए उदाहरण में, एपीआई पासकोड की मदद से कनेक्शन बनाने का तरीका बताया गया है:

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.8-live"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## इंटरैक्शन के तरीके

यहां दिए गए सेक्शन में, Live API में उपलब्ध अलग-अलग इनपुट और आउटपुट मोड के उदाहरण और उनसे जुड़ी जानकारी दी गई है.

### ऑडियो भेजना

ऑडियो को रॉ पीसीएम डेटा (रॉ 16-बिट पीसीएम ऑडियो, 16kHz, लिटिल-एंडियन) के तौर पर भेजा जाना चाहिए.

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### ऑडियो फ़ॉर्मैट

Live API में ऑडियो डेटा हमेशा रॉ, लिटिल-एंडियन, और 16-बिट पीसीएम होता है. ऑडियो डिवाइस हमेशा 24 किलोहर्ट्ज़ के सैंपल रेट का इस्तेमाल करता है. इनपुट ऑडियो मूल रूप से 16 किलोहर्ट्ज़ का होता है. हालांकि, Live API ज़रूरत पड़ने पर इसे फिर से सैंपल करेगा. इसलिए, किसी भी सैंपल रेट को भेजा जा सकता है. इनपुट ऑडियो के सैंपल रेट के बारे में बताने के लिए, ऑडियो वाले हर [Blob](https://ai.google.dev/api/caching?hl=hi#Blob) के एमआईएमई टाइप को `audio/pcm;rate=16000` जैसे किसी वैल्यू पर सेट करें.

### ऑडियो पाना

मॉडल के ऑडियो जवाब, डेटा के हिस्सों के तौर पर मिलते हैं.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### टेक्स्ट भेजा जा रहा है

टेक्स्ट को `send_realtime_input` (Python) या `sendRealtimeInput` (JavaScript) का इस्तेमाल करके भेजा जा सकता है.

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### वीडियो भेजा जा रहा है

वीडियो फ़्रेम को अलग-अलग इमेज (जैसे, JPEG या PNG) के तौर पर, किसी खास फ़्रेम रेट (ज़्यादा से ज़्यादा एक फ़्रेम प्रति सेकंड) पर भेजा जाता है.

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### कॉन्टेंट में धीरे-धीरे किए जाने वाले अपडेट

टेक्स्ट इनपुट भेजने, सेशन का कॉन्टेक्स्ट सेट अप करने या सेशन का कॉन्टेक्स्ट वापस लाने के लिए, इंक्रीमेंटल अपडेट का इस्तेमाल करें. छोटे कॉन्टेक्स्ट के लिए, इवेंट के सटीक क्रम को दिखाने के लिए, बारी-बारी से इंटरैक्शन भेजे जा सकते हैं:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

बड़े कॉन्टेक्स्ट के लिए, हमारा सुझाव है कि एक मैसेज की खास जानकारी दी जाए, ताकि बाद की बातचीत के लिए कॉन्टेक्स्ट विंडो खाली हो जाए. सेशन के कॉन्टेक्स्ट को लोड करने के किसी अन्य तरीके के लिए, [सेशन फिर से शुरू करना](https://ai.google.dev/gemini-api/docs/live-session?hl=hi#session-resumption) देखें.

### ऑडियो ट्रांसक्रिप्शन

मॉडल के जवाब के अलावा, आपको ऑडियो आउटपुट और ऑडियो इनपुट, दोनों की ट्रांसक्रिप्ट भी मिल सकती हैं.

मॉडल के ऑडियो आउटपुट को टेक्स्ट में बदलने की सुविधा चालू करने के लिए, सेटअप कॉन्फ़िगरेशन में `output_audio_transcription` भेजें. बोले जा रहे शब्दों को टेक्स्ट में बदलने के लिए, भाषा का अनुमान मॉडल के जवाब से लगाया जाता है.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

मॉडल के ऑडियो इनपुट को टेक्स्ट में बदलने की सुविधा चालू करने के लिए, सेटअप कॉन्फ़िगरेशन में `input_audio_transcription` भेजें.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### आवाज़ और भाषा बदलना

[नेटिव ऑडियो आउटपुट](#native-audio-output) मॉडल, [लिखाई को बोली में बदलने (टीटीएस)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#voices) मॉडल के लिए उपलब्ध किसी भी आवाज़ के साथ काम करते हैं. [AI Studio](https://aistudio.google.com/app/live?hl=hi) में जाकर, सभी आवाज़ें सुनी जा सकती हैं.

आवाज़ तय करने के लिए, सेशन कॉन्फ़िगरेशन के हिस्से के तौर पर, `speechConfig` ऑब्जेक्ट में आवाज़ का नाम सेट करें:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Live API, [कई भाषाओं](#supported-languages) में काम करता है.
[नेटिव ऑडियो आउटपुट](#native-audio-output) वाले मॉडल, सही भाषा को अपने-आप चुनते हैं. साथ ही, ये भाषा कोड को साफ़ तौर पर सेट करने की सुविधा के साथ काम नहीं करते.

## नेटिव ऑडियो की सुविधाएं

हमारे नए मॉडल में [नेटिव ऑडियो आउटपुट](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=hi) की सुविधा है. इससे आपको नैचुरल और असली आवाज़ मिलती है. साथ ही, यह कई भाषाओं में बेहतर परफ़ॉर्म करता है.

### सूझ-बूझ वाला मॉडल

ज़्यादा सोच-विचार करके जवाब देने वाले Gemini 3.8 Live और Gemini 3.1 मॉडल, `thinkingLevel` का इस्तेमाल करते हैं, ताकि वे ज़्यादा सोच-विचार करके जवाब दे सकें. `gemini-3.8-live` के लिए, `thinkingLevel` मौजूद नहीं है और सेटअप में इसे शामिल नहीं किया जाना चाहिए. ज़्यादा सोच-विचार करके जवाब देने वाले Gemini 3.8 Live में `low`, `medium`, और `high` का इस्तेमाल किया जा सकता है. हालांकि, `minimal` मौजूद नहीं है. Gemini 3.1 मॉडल, `minimal`, `low`, `medium`, और `high` के साथ काम करते हैं. ज़्यादा जानकारी के लिए, [लाइव एपीआई के बारे में जानकारी](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=hi) लेख पढ़ें.

### Python

```
model = "gemini-3.8-live-extended-thinking"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.8-live-extended-thinking';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

इसके अलावा, अपने कॉन्फ़िगरेशन में `includeThoughts` को `true` पर सेट करके, सोच के बारे में खास जानकारी देने वाली सुविधा चालू की जा सकती है. ज़्यादा जानकारी के लिए, [सोच के बारे में खास जानकारी](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#summaries) देखें:

### Python

```
model = "gemini-3.8-live-extended-thinking"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.8-live-extended-thinking';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### अफ़ेक्टिव डायलॉग

इस सुविधा की मदद से, Gemini अपने जवाब देने के तरीके को इनपुट एक्सप्रेशन और टोन के हिसाब से बदल सकता है.

भावनाओं से जुड़े डायलॉग का इस्तेमाल करने के लिए, एपीआई वर्शन को `v1beta` पर सेट करें. साथ ही, सेटअप मैसेज में `enable_affective_dialog` को `true` पर सेट करें:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### आवाज़ सुनकर ज़रूरत के मुताबिक जवाब देने की सुविधा

इस सुविधा के चालू होने पर, Gemini यह तय कर सकता है कि अगर कॉन्टेंट काम का नहीं है, तो जवाब न दिया जाए.

इसका इस्तेमाल करने के लिए, एपीआई वर्शन को `v1beta` पर सेट करें. इसके बाद, सेटअप मैसेज में `proactivity` फ़ील्ड को कॉन्फ़िगर करें और `proactive_audio` को `true` पर सेट करें:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## लाइव अनुवाद

लाइव एपीआई, बोली गई बातचीत का रीयल-टाइम में कम समय में अनुवाद करने की सुविधा देता है. इस सुविधा की मदद से, रीयल-टाइम में बोली का अनुवाद करने वाले ऐप्लिकेशन बनाए जा सकते हैं.

ज़्यादा जानकारी और उदाहरणों के लिए, [रीयल-टाइम में अनुवाद पाने की सुविधा से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=hi) देखें.

## आवाज़ का पता लगाने की तकनीक (वीएडी)

आवाज़ का पता लगाने की तकनीक (वीएडी) की मदद से, मॉडल यह पहचान पाता है कि कोई व्यक्ति कब बोल रहा है. इससे बातचीत को नैचुरल बनाने में मदद मिलती है, क्योंकि यह सुविधा उपयोगकर्ता को किसी भी समय मॉडल को रोकने की अनुमति देती है.

जब VAD को किसी रुकावट का पता चलता है, तो जनरेट की जा रही ऑडियो को रद्द कर दिया जाता है और उसे हटा दिया जाता है. सेशन के इतिहास में, सिर्फ़ वह जानकारी सेव की जाती है जो क्लाइंट को पहले ही भेजी जा चुकी है. इसके बाद, सर्वर [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentservercontent) मैसेज भेजकर, रुकावट की सूचना देता है.

इसके बाद, Gemini का सर्वर फ़ंक्शन कॉल के सभी अनुरोधों को खारिज कर देता है. साथ ही, रद्द किए गए कॉल के आईडी के साथ `BidiGenerateContentServerContent` मैसेज भेजता है.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### ऑटोमैटिक वीएडी

डिफ़ॉल्ट रूप से, मॉडल लगातार ऑडियो इनपुट स्ट्रीम पर वीएडी की प्रोसेस अपने-आप करता है. वीएडी को [सेटअप कॉन्फ़िगरेशन](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentSetup) के [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=hi#RealtimeInputConfig.AutomaticActivityDetection) फ़ील्ड की मदद से कॉन्फ़िगर किया जा सकता है.

अगर ऑडियो स्ट्रीम को एक सेकंड से ज़्यादा समय के लिए रोका जाता है (उदाहरण के लिए, क्योंकि उपयोगकर्ता ने माइक्रोफ़ोन बंद कर दिया है), तो [`audioStreamEnd`](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) इवेंट भेजा जाना चाहिए, ताकि कैश किए गए ऑडियो को हटाया जा सके. क्लाइंट, ऑडियो डेटा भेजना किसी भी समय फिर से शुरू कर सकता है.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

`send_realtime_input` की मदद से, एपीआई वीएडी के आधार पर ऑडियो का जवाब अपने-आप देगा. `send_client_content`, मॉडल के कॉन्टेक्स्ट में मैसेज जोड़ता है. वहीं, `send_realtime_input` को जवाब देने के लिए ऑप्टिमाइज़ किया जाता है. हालांकि, इससे मैसेज के क्रम पर असर पड़ता है.

### वीएडी के अपने-आप कॉन्फ़िगर होने की सुविधा

वीएडी की गतिविधि को ज़्यादा कंट्रोल करने के लिए, यहां दिए गए पैरामीटर कॉन्फ़िगर किए जा सकते हैं. ज़्यादा जानकारी के लिए, [एपीआई का संदर्भ](https://ai.google.dev/api/live?hl=hi#automaticactivitydetection) देखें.

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### हाइब्रिड वीएडी

हाइब्रिड वीएडी में, ऑटोमैटिक वीएडी (बोलना शुरू होने का सटीक पता लगाने की सुविधा) और मैन्युअल वीएडी (कम समय में जवाब तैयार करने की सुविधा) के फ़ायदे मिलते हैं.

इस कॉन्फ़िगरेशन में:

1. सर्वर पर **अपने-आप वीएडी की सुविधा चालू रहती है**. सर्वर, उपयोगकर्ता के बोलने की शुरुआत का अपने-आप पता लगाता है. इसके लिए, प्रीफ़िक्स पैडिंग का इस्तेमाल किया जाता है, ताकि उच्चारण की शुरुआत में आवाज़ न कटे.
2. क्लाइंट, **क्लाइंट-साइड वीएडी** का इस्तेमाल करके यह पता लगाता है कि उपयोगकर्ता ने बोलना कब बंद किया.
3. जब क्लाइंट-साइड वीएडी को बातचीत खत्म होने का पता चलता है, तो वह सर्वर को [`audio_stream_end`](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) सिग्नल भेजता है.
4. सर्वर, `audio_stream_end` सिग्नल को तुरंत जवाब देने के प्रॉम्प्ट के तौर पर लेता है. इससे सर्वर-साइड पर, बातचीत रुकने का पता लगाने में लगने वाला डिफ़ॉल्ट समय नहीं लगता. साथ ही, ट्रांसक्रिप्ट और मॉडल का जवाब कम से कम समय में मिल जाता है.
5. अगर क्लाइंट-साइड वीएडी ट्रिगर नहीं होता है, तो सर्वर-साइड वीएडी, स्पीच के खत्म होने का पता लगाने के लिए फ़ॉलबैक के तौर पर काम करता है.

ध्यान दें कि अगर क्लाइंट-साइड वीएडी थ्रेशोल्ड को बहुत ज़्यादा पर सेट किया जाता है, तो इसकी वजह से स्पीच कटऑफ़ हो सकते हैं. हालांकि, इस तरीके से फ़्रंट-ट्रंकेशन की समस्याओं को रोका जा सकता है. ये समस्याएं, मैन्युअल वीएडी के साथ हो सकती हैं.

### Python

```
# Set up with automatic VAD enabled (default)
config = {
    "response_modalities": ["AUDIO"],
}

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio data normally
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects the end of speech, send:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Set up with automatic VAD enabled (default)
const config = {
  responseModalities: [Modality.AUDIO],
};

// Send audio data normally
session.sendRealtimeInput({
  audio: {
    data: base64Audio,
    mimeType: "audio/pcm;rate=16000"
  }
});

// When client-side VAD detects the end of speech, send:
session.sendRealtimeInput({ audioStreamEnd: true });
```

### अपने-आप वीएडी की सुविधा बंद करना

इसके अलावा, सेटअप मैसेज में `realtimeInputConfig.automaticActivityDetection.disabled` को `true` पर सेट करके, वीएडी की सुविधा को अपने-आप बंद होने से रोका जा सकता है. इस कॉन्फ़िगरेशन में, उपयोगकर्ता की आवाज़ का पता लगाने और सही समय पर [`activityStart`](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) और [`activityEnd`](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) मैसेज भेजने की ज़िम्मेदारी क्लाइंट की होती है. इस कॉन्फ़िगरेशन में `audioStreamEnd` नहीं भेजा जाता है. इसके बजाय, स्ट्रीम में किसी भी तरह की रुकावट को `activityEnd` मैसेज से मार्क किया जाता है.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### वीएडी पैरामीटर और क्वालिटी पर उनके असर के बारे में जानकारी

ऑटोमैटिक वीएडी का इस्तेमाल करते समय, दो मुख्य पैरामीटर यह तय करते हैं कि मॉडल को भेजने से पहले, ऑडियो को स्पीच टर्न में कैसे बांटा जाए:

- **`prefixPaddingMs`**: यह वह ऑडियो है जिसे आवाज़ का पता चलने *से पहले* शामिल किया जाना है. "लुक-बैक" सुविधा की मदद से, यह पक्का किया जाता है कि मॉडल, बोली की शुरुआत को पूरी तरह से कैप्चर करे. इसमें पहला सिलेबल भी शामिल है, जो वीएडी ट्रिगर होने से पहले शुरू हो सकता है. `0` की वैल्यू की वजह से, शब्दों की शुरुआत में मौजूद अक्षर कट सकते हैं.
- **`silenceDurationMs`**: सर्वर, बोलने की बारी खत्म होने से पहले कितने समय तक इंतज़ार करता है. इससे यह तय होता है कि सिस्टम, वाक्य के बीच में रुकने (जैसे, सोचने, सांस लेने या क्लॉज़ की सीमाओं) को कितना बर्दाश्त कर सकता है.

#### ऑडियो की क्वालिटी पर `silenceDurationMs` का असर

`silenceDurationMs` वैल्यू से, मॉडल को प्रोसेस करने के लिए मिलने वाले ऑडियो चंक के साइज़ और पूरे होने पर सीधा असर पड़ता है:

- **सुझाया गया (500 मि॰से॰–800 मि॰से॰):** इससे अच्छा बैलेंस मिलता है. मॉडल को कॉन्टेक्स्ट के हिसाब से ऑडियो के पूरे और काम के हिस्से मिलते हैं. साथ ही, इसमें लगने वाला समय भी कम होता है. सर्वर का इंटरनल डिफ़ॉल्ट समय लगभग 800 मि॰से॰ होता है.
- **बहुत कम (जैसे, 100 मि॰से॰–200 मि॰से॰):** सिस्टम, बातचीत के दौरान स्वाभाविक रूप से रुकने पर, बोलने की बारी को खत्म कर देता है. इससे एक ही वाक्य को कई छोटे-छोटे ऑडियो फ़्रैगमेंट में बांट दिया जाता है. मॉडल को ये फ़्रैगमेंट अलग-अलग मिलते हैं. इस वजह से, उसे फ़्रैगमेंट के बीच के कॉन्टेक्स्ट के बारे में जानकारी नहीं मिल पाती. साथ ही, ट्रांसक्रिप्शन और जवाब की क्वालिटी भी कम हो जाती है.
- **बहुत ज़्यादा (जैसे, 2000 मि॰से॰ से ज़्यादा):** उपयोगकर्ता के बोलना बंद करने के बाद, सिस्टम काफ़ी देर तक इंतज़ार करता है. इससे मॉडल के जवाब देने में लगने वाले समय में बढ़ोतरी होती है.

#### मैन्युअल (क्लाइंट-साइड) वीएडी के लिए सबसे सही तरीके

ऑटोमैटिक वीएडी की सुविधा बंद करने और क्लाइंट-साइड पर आवाज़ पहचानने की सुविधा से `activityStart`/`activityEnd` सिग्नल मैनेज करने पर, ध्यान रखें कि सर्वर के ऑडियो बफ़रिंग के बिल्ट-इन मैकेनिज़्म को बायपास कर दिया जाता है. इसका मतलब है कि:

1. **बोलने से पहले ऑडियो बफ़र नहीं होता:** सर्वर अब, बोली शुरू होने से पहले ऑडियो नहीं जोड़ता है. `activityStart` भेजने से पहले, आपके क्लाइंट को ऑडियो के बारे में ज़रूरी जानकारी देनी चाहिए.
2. **कोई साइलेंस टॉलरेंस नहीं:** सर्वर, आपके `activityEnd` सिग्नल पर तुरंत कार्रवाई करता है. इसके लिए, उसे इंतज़ार नहीं करना पड़ता. अगर क्लाइंट-साइड वीएडी, बातचीत खत्म होने का थ्रेशोल्ड बहुत कम (जैसे, 200 मि॰से॰ का साइलेंस) इस्तेमाल करता है, तो बातचीत के दौरान स्वाभाविक रूप से रुकने पर, वाक्य के बीच में ही आवाज़ कट सकती है.

मैन्युअल वीएडी के साथ ऑडियो की क्वालिटी बनाए रखने के लिए, अपने क्लाइंट के वॉइस ऐक्टिविटी डिटेक्टर में, बातचीत खत्म होने के बाद कम से कम **500 मि॰से॰** का साइलेंस थ्रेशोल्ड इस्तेमाल करें.
इस वैल्यू से कम थ्रेशोल्ड होने पर, ऑडियो के छोटे-छोटे हिस्से मिलते हैं. इससे ट्रांसक्रिप्शन और मॉडल के जवाब की क्वालिटी खराब हो जाती है.

## टोकन की गिनती

इस्तेमाल किए गए टोकन की कुल संख्या, सर्वर से मिले मैसेज के [usageMetadata](https://ai.google.dev/api/live?hl=hi#usagemetadata) फ़ील्ड में देखी जा सकती है.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## मीडिया रिज़ॉल्यूशन

सेशन कॉन्फ़िगरेशन के हिस्से के तौर पर `mediaResolution` फ़ील्ड सेट करके, इनपुट मीडिया के लिए मीडिया रिज़ॉल्यूशन तय किया जा सकता है:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

ऑडियो, वीडियो या इमेज इनपुट वाले मल्टीमॉडल सेशन के लिए, `mediaResolution` को कॉन्फ़िगर किया जा सकता है. `mediaResolution`, विज़ुअल इनपुट के लिए हर फ़्रेम के हिसाब से टोकन का बंटवारा करता है. वहीं, ऑडियो स्ट्रीम को सभी रिज़ॉल्यूशन सेटिंग में, हर सेकंड के हिसाब से एक तय दर पर टोकन में बदला जाता है. ज़्यादा जानकारी के लिए, [मीडिया रिज़ॉल्यूशन](https://ai.google.dev/gemini-api/docs/media-resolution?hl=hi) गाइड देखें.

## सीमाएं

अपना प्रोजेक्ट प्लान करते समय, Live API की इन सीमाओं को ध्यान में रखें.

### जवाब देने के तरीके

नेटिव ऑडियो मॉडल, सिर्फ़ `AUDIO response modality के साथ काम करते हैं. अगर आपको मॉडल से मिले जवाब को टेक्स्ट के तौर पर चाहिए, तो [आउटपुट ऑडियो ट्रांसक्रिप्शन](#audio-transcription) सुविधा का इस्तेमाल करें.

### क्लाइंट प्रमाणीकरण

Live API, डिफ़ॉल्ट रूप से सिर्फ़ सर्वर-टू-सर्वर पुष्टि करने की सुविधा देता है. अगर आपको [क्लाइंट-टू-सर्वर अप्रोच](https://ai.google.dev/gemini-api/docs/live?hl=hi#implementation-approach) का इस्तेमाल करके, Live API ऐप्लिकेशन लागू करना है, तो आपको सुरक्षा से जुड़े जोखिमों को कम करने के लिए, [कुछ समय के लिए मान्य टोकन](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=hi) का इस्तेमाल करना होगा.

### सत्र की अवधि

सिर्फ़ ऑडियो वाले सेशन 15 मिनट तक किए जा सकते हैं. वहीं, ऑडियो और वीडियो, दोनों वाले सेशन सिर्फ़ दो मिनट तक किए जा सकते हैं.
हालांकि, सेशन की अवधि के दौरान असीमित एक्सटेंशन के लिए, अलग-अलग [सेशन मैनेजमेंट तकनीकें](https://ai.google.dev/gemini-api/docs/live-session?hl=hi) कॉन्फ़िगर की जा सकती हैं.

### कॉन्टेक्स्ट विंडो

किसी सेशन के लिए कॉन्टेक्स्ट विंडो की सीमा यह होती है:

- [नेटिव ऑडियो आउटपुट](#native-audio-output) मॉडल के लिए 1,28,000 टोकन
- Live API के अन्य मॉडल के लिए 32 हज़ार टोकन

## इस्तेमाल की जा सकने वाली भाषाएं

लाइव एपीआई, इन 99 भाषाओं में काम करता है.

| भाषा | BCP-47 कोड | भाषा | BCP-47 कोड |
| --- | --- | --- | --- |
| अफ़्रीकान्स | `af` | लातवियन | `lv` |
| आकान | `ak` | लिथुएनियन | `lt` |
| अल्बेनियन | `sq` | मैसेडोनियन | `mk` |
| अमहैरिक | `am` | मलय | `ms` |
| अरबी | `ar` | मलयालम | `ml` |
| आर्मीनियन | `hy` | मोल्टीज़ | `mt` |
| असमिया | `as` | माओरी | `mi` |
| अज़रबैजानी | `az` | मराठी | `mr` |
| बॉस्क | `eu` | मंगोलियन | `mn` |
| बेलारूसी | `be` | नेपाली | `ne` |
| बांग्ला | `bn` | नॉर्वीजन | `no`, `nb` |
| बोस्नियन | `bs` | ओड़िया | `or` |
| बल्गैरियन | `bg` | ओरोमो | `om` |
| बर्मीज़ | `my` | पश्तो | `ps` |
| कैटलैन | `ca` | फ़ारसी | `fa` |
| सेबुआनो | `ceb` | पोलिश | `pl` |
| चाइनीज़ (सिंप्लिफ़ाइड) | `zh-Hans` | पॉर्चुगीज़ (ब्राज़ील) | `pt-BR` |
| चाइनीज़ (ट्रेडिशनल) | `zh-Hant` | पॉर्चगीज़ (पुर्तगाल) | `pt-PT` |
| क्रोएशियन | `hr` | पंजाबी | `pa` |
| चेक | `cs` | क्वेचा | `qu` |
| डैनिश | `da` | रोमानियन | `ro` |
| डच | `nl` | रोमैंश | `rm` |
| अंग्रेज़ी | `en` | रूसी | `ru` |
| एस्टोनियन | `et` | सर्बियन | `sr` |
| फ़ैरोईज़ | `fo` | सिंधी | `sd` |
| फ़िलिपीनी | `fil` | सिंहला | `si` |
| फ़िनिश | `fi` | स्लोवाक | `sk` |
| फ़्रांसीसी | `fr` | स्लोवेनियन | `sl` |
| गैलिशियन | `gl` | सोमाली | `so` |
| जॉर्जियन | `ka` | सदर्न सुटू | `st` |
| जर्मन | `de` | स्पैनिश | `es` |
| ग्रीक | `el` | स्वाहिली | `sw` |
| गुजराती | `gu` | स्वीडिश | `sv` |
| हौसा | `ha` | ताजिक | `tg` |
| हिब्रू | `he` | तमिल | `ta` |
| हिन्दी | `hi` | तेलुगु | `te` |
| हंगेरियन | `hu` | थाई | `th` |
| आइसलैंडिक | `is` | स्वाना | `tn` |
| इंडोनेशियन | `id` | टर्किश | `tr` |
| आयरिश | `ga` | तुर्कमेन | `tk` |
| इटैलियन | `it` | यूक्रेनियन | `uk` |
| जापानी | `ja` | उर्दू | `ur` |
| कन्नड़ | `kn` | उज़्बेक | `uz` |
| कज़ाक | `kk` | वियतनामीज़ | `vi` |
| खमेर | `km` | वेल्श | `cy` |
| किन्यारवांडा | `rw` | वेस्टर्न फ़्रीजन | `fy` |
| कोरियन | `ko` | वोलॉफ़ | `wo` |
| कुर्दिश | `ku` | योरुबा | `yo` |
| किर्गिज़ | `ky` | ज़ुलू | `zu` |
| लाओ | `lo` |  |  |

## आगे क्या करना है

- लाइव एपीआई का असरदार तरीके से इस्तेमाल करने के बारे में ज़रूरी जानकारी पाने के लिए, [टूल इस्तेमाल करने](https://ai.google.dev/gemini-api/docs/live-tools?hl=hi) और [सेशन मैनेज करने](https://ai.google.dev/gemini-api/docs/live-session?hl=hi) से जुड़ी गाइड पढ़ें.
- [Google AI Studio](https://aistudio.google.com/app/live?hl=hi) में Live API को आज़माएं.
- Live API मॉडल के बारे में ज़्यादा जानने के लिए, [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=hi) और [Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=hi) मॉडल के पेज देखें.
- [Live API कुकबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=hi), [Live API Tools कुकबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=hi), और [Live API Get Started स्क्रिप्ट](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py) में दिए गए अन्य उदाहरणों को आज़माएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-19 (UTC) को अपडेट किया गया."],[],[]]
