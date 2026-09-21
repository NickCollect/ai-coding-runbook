---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=hi
fetched_at: 2026-09-21T05:53:51.677232+00:00
title: "Gemini Live API \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947, \u0932\u093e\u0907\u0935 \u091f\u094d\u0930\u093e\u0902\u0938\u0915\u094d\u0930\u093f\u092a\u094d\u0936\u0928 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Live API की मदद से, लाइव ट्रांसक्रिप्शन की सुविधा

Gemini Live API, [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=hi) मॉडल का इस्तेमाल करके, कम समय में बोली को लिखाई में बदलने की सुविधा देता है. WebSockets के ज़रिए Live API से कनेक्ट करके या Google Gen AI SDK का इस्तेमाल करके, लगातार ऑडियो इनपुट स्ट्रीम किया जा सकता है. साथ ही, बोली गई बातों को रीयल-टाइम में टेक्स्ट में बदला जा सकता है.

[Google AI Studio में लाइव ट्रांसक्रिप्शन की सुविधा आज़माएँmic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=hi)
[Colab कुकबुक खोलेंcode](https://github.com/google-gemini/cookbook)
[कोडिंग एजेंट की क्षमताओं का इस्तेमाल करेंterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi#gemini-live-api-dev)

Gemini Live API का इस्तेमाल करके, डेवलपर प्लैटफ़ॉर्म जैसे कि [Agora](https://docs.agora.io/en/ai/models/asr/gemini), [Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration), [LiveKit](https://docs.livekit.io/agents/models/stt/gemini/), [Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google), [Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text), और [Vision Agents](https://visionagents.ai/integrations/stt/gemini), डेवलपर को आसानी से, आवाज़ से कंट्रोल होने वाले बेहतरीन इंटरफ़ेस बनाने और उन्हें डिप्लॉय करने की सुविधा देते हैं. ये प्लैटफ़ॉर्म, पर्दे के पीछे जटिल रीयल-टाइम मीडिया स्ट्रीमिंग इंफ़्रास्ट्रक्चर को मैनेज करते हैं. इससे डेवलपर, उपयोगकर्ता अनुभव को बेहतर बनाने पर पूरी तरह से फ़ोकस कर पाते हैं.

## लाइव एजेंट और लाइव ट्रांसक्रिप्शन की सुविधा के बीच अंतर

दोनों ही Live API के द्विदिशीय स्ट्रीमिंग कनेक्शन का इस्तेमाल करते हैं. हालांकि, लाइव ट्रांसक्रिप्शन, बातचीत करने वाले एजेंट के बजाय, कम समय में बोली को पहचानने वाली पाइपलाइन के तौर पर काम करता है.

| सुविधा | लाइव एजेंट | बोले जा रहे शब्दों को रीयल-टाइम में टेक्स्ट में बदलने की सुविधा |
| --- | --- | --- |
| **मुख्य भूमिका** | बातचीत करने वाली Assistant, जो सुनती है, वजह बताती है, और जवाब देती है. | रीयल-टाइम में बोली को लिखाई में बदलने वाली पाइपलाइन, जो इनकमिंग ऑडियो को ट्रांसक्राइब करती है. |
| **जवाब देने का तरीका** | बोला गया ऑडियो और टेक्स्ट (`response_modalities=["AUDIO"]`). | स्ट्रीम किए जा रहे टेक्स्ट की ट्रांसक्रिप्ट (`response_modalities=["TEXT"]`). |
| **इंटरैक्शन स्टाइल** | बारी-बारी से बातचीत करने की सुविधा, जिसमें रुकने और बीच में बोलने का पता लगाया जाता है. | स्पीकर के बोलते समय, स्ट्रीम की लगातार प्रोसेसिंग होती है. |
| **उपलब्ध सुविधाएं** | फ़ंक्शन कॉलिंग, Google Search, सिस्टम के निर्देश. | बोली को प्राथमिकता देना (`custom_vocabulary`), भाषा का पता लगाना, मैन्युअल और हाइब्रिड वीएडी, स्मार्ट ट्रांसक्रिप्शन. |
| **इनपुट स्ट्रीम** | मल्टीमोडल: ऑडियो, वीडियो, इमेज, टेक्स्ट. | ऑडियो इनपुट (रॉ 16-बिट पीसीएम). |

## अपनी प्रोफ़ाइल बनाना शुरू करें

यहां दिए गए उदाहरणों में, `gemini-3.5-transcribe-live` के साथ दोनों दिशाओं में काम करने वाला स्ट्रीमिंग सेशन खोलने और रीयल-टाइम ट्रांसक्रिप्शन पाने का तरीका बताया गया है.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## अस्थायी और फ़ाइनल ट्रांसक्रिप्ट

ऑडियो को Live API में स्ट्रीम करने पर, सर्वर `server_content` में दो ट्रांसक्रिप्शन फ़ील्ड दिखाता है:

- **`interim_input_transcription`**: कम समय में नतीजे मिलते हैं. साथ ही, स्पीकर के बोलते समय, अनुमानित तौर पर कुछ शब्दों को अपडेट किया जाता है. ये आंशिक अपडेट, बहुत कम समय में हो जाते हैं. `interim_input_transcription` का इस्तेमाल करके, लाइव यूज़र इंटरफ़ेस (यूआई) के रिस्पॉन्सिव सबटाइटल या कैप्शन की झलक रेंडर करें.
- **`input_transcription`**: यह स्पीकर के रुकने, बारी पूरी होने या स्पीच के फ़ाइनल होने पर जारी की गई फ़ाइनल ट्रांसक्रिप्ट होती है. यह टेक्स्ट, मॉडल के उस स्पीच सेगमेंट की आधिकारिक ट्रांसक्रिप्ट को दिखाता है. स्मार्ट ट्रांसक्रिप्शन मोड में, इसमें साफ़ तौर पर फ़ॉर्मैट किया गया जवाब शामिल होगा.

यहां दिए गए उदाहरण में, स्ट्रीमिंग के दौरान मिलने वाले इंटरिम पार्शियल को दिखाने और फ़ाइनल ट्रांसक्रिप्ट को सेव करने का तरीका बताया गया है:

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSockets

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## ऑडियो भेजना

ऐक्टिव कनेक्शन पर, ऑडियो के हिस्सों को 16-बिट पीसीएम ऑडियो के तौर पर स्ट्रीम करें.

- **ऑडियो फ़ॉर्मैट:** रॉ 16-बिट पीसीएम, 16 किलोहर्ट्ज़ पर (मोनो, लिटिल-एंडियन).
- **चंक का साइज़:** ऑडियो को 100 मि॰से॰ (1,024 से 2,048 फ़्रेम) के चंक में भेजें.
- **एमआईएमई टाइप:** `audio/pcm;rate=16000` (या मैचिंग सैंपलिंग रेट).

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## बोले जा रहे शब्दों को टेक्स्ट में बदलने की सुविधाएं

### अपने-आप भाषा पहचानने की सुविधा

डिफ़ॉल्ट रूप से, `language_codes` को शामिल न करने या `language_codes=[]` को सेट करने पर, भाषा की अपने-आप पहचान होने की सुविधा चालू हो जाती है. यह मॉडल, अलग-अलग भाषाओं में की गई बातचीत और कोड-स्विचिंग के साथ-साथ, अलग-अलग भाषाओं में बोले गए शब्दों का पता लगाता है.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### किसी खास भाषा के बारे में जानकारी

BCP-47 के भाषा कोड (उदाहरण के लिए, स्पैनिश के लिए `["es-ES"]` या फ़्रेंच के लिए `["fr-FR"]`) साफ़ तौर पर दें, ताकि पहचान करने की सुविधा को खास भाषाओं के लिए बेहतर बनाया जा सके. [सुविधा के साथ काम करने वाली भाषाएं](#supported-languages) देखें.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### कस्टम शब्दावली के हिसाब से पक्षपात करना

`custom_vocabulary` में ज़्यादा से ज़्यादा 1,000 वाक्यांश, व्यक्तिवाचक संज्ञाएं, ब्रैंड के नाम या तकनीकी शब्द जोड़ें, ताकि बोली की पहचान करने वाली सुविधा, खास शब्दावली पर फ़ोकस कर सके. आम तौर पर, ज़्यादा से ज़्यादा 100 शब्दों का इस्तेमाल करने पर सबसे अच्छे नतीजे मिलते हैं.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### स्मार्ट ट्रांसक्रिप्शन

`input_audio_transcription` में `mode` पैरामीटर का इस्तेमाल करके, ट्रांसक्रिप्शन के आउटपुट फ़ॉर्मैट को कॉन्फ़िगर करें:

- **`VERBATIM` (डिफ़ॉल्ट)**: इसमें बोले गए हर शब्द की सटीक ट्रांसक्रिप्ट तैयार की जाती है. इसमें फ़िलर शब्दों ("अम", "अह", "जैसे"), दोहराए गए शब्दों, और गलत शुरुआत को भी शामिल किया जाता है.
- **`SMART` (स्मार्ट ट्रांसक्रिप्शन)**: यह ट्रांसक्रिप्ट को पढ़ने में आसान बनाने के लिए, उसे साफ़-सुथरा और व्यवस्थित करता है:

  - **बोलने में होने वाली रुकावटों को हटाना**: इससे फ़िलर शब्द, हकलाना, और गलत शुरुआत को हटाया जाता है.
  - **बोले गए शब्दों में सुधार करने की सुविधा**: यह सुविधा, बोले गए शब्दों में सुधार करने की सुविधा को नैचुरल तरीके से काम करने देती है.
  - **स्ट्रक्चर्ड फ़ॉर्मैटिंग**: यह सुविधा, सूचियों, बुलेट पॉइंट, संख्याओं, तारीखों, और पैराग्राफ़ ब्रेक को अपने-आप फ़ॉर्मैट करती है.
  - **व्याकरण और केसिंग**: इसमें नैचुरल कैपिटल लेटर और विराम चिह्न को बेहतर बनाया जाता है.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## आवाज़ का पता लगाने की तकनीक (वीएडी) से जुड़ी रणनीतियां

### अपने-आप वीएडी की सुविधा चालू होना (डिफ़ॉल्ट)

डिफ़ॉल्ट रूप से, सर्वर-साइड पर मौजूद वॉइस ऐक्टिविटी डिटेक्शन की सुविधा यह पता लगाती है कि स्पीकर ने बोलना कब शुरू किया और कब बंद किया.

### हाइब्रिड वीएडी

[हाइब्रिड वीएडी](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=hi#hybrid-vad), सर्वर-साइड पर अपने-आप बातचीत शुरू होने का पता लगाने की सुविधा को क्लाइंट-साइड पर बातचीत खत्म होने का पता लगाने की सुविधा के साथ जोड़ता है, ताकि बिना किसी रुकावट के जवाब दिया जा सके:

1. **सर्वर-साइड पर वीएडी की सुविधा अपने-आप चालू रहती है**, ताकि प्रीफ़िक्स ऑडियो पैडिंग की मदद से, स्पीच की शुरुआत का सटीक पता लगाया जा सके. इससे पहले शब्द के कुछ हिस्से के कटने की समस्या नहीं होती.
2. **क्लाइंट-साइड वीएडी को आवाज़ न होने का पता चलता है**: जब उपयोगकर्ता के डिवाइस पर मौजूद लोकल वीएडी को पता चलता है कि बोलने वाले व्यक्ति ने बोलना बंद कर दिया है, तो क्लाइंट तुरंत `audio_stream_end` सिग्नल भेजता है.
3. **जल्दी फ़ाइनल करना**: सर्वर, `audio_stream_end` को तुरंत फ़ाइनल करने के प्रॉम्प्ट के तौर पर लेता है. इससे सर्वर साइड से मिलने वाले जवाब के लिए इंतज़ार करने का डिफ़ॉल्ट समय कम हो जाता है. साथ ही, फ़ाइनल की गई ट्रांसक्रिप्ट कम से कम समय में मिल जाती है.
4. **फ़ॉलबैक**: अगर क्लाइंट वीएडी ट्रिगर नहीं होता है, तो सर्वर-साइड वीएडी अपने-आप फ़ॉलबैक के तौर पर काम करता है.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### मैन्युअल वीएडी (पुश-टू-टॉक)

वॉकी-टॉकी इंटरफ़ेस या पुश-टू-टॉक बटन के लिए, वीएडी की सुविधा को पूरी तरह से बंद करें. साथ ही, `activity_start` और `activity_end` का इस्तेमाल करके, बोलने की सीमा को कंट्रोल करें:

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## क्लाइंट ऐप्लिकेशन में कुछ समय के लिए उपलब्ध टोकन

क्लाइंट-टू-सर्वर ऐप्लिकेशन (जैसे कि सीधे माइक्रोफ़ोन से स्ट्रीम करने वाले मोबाइल या वेब ऐप्लिकेशन) के लिए, [अस्थायी टोकन](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=hi) का इस्तेमाल करें. इससे क्लाइंट कोड में आपकी एपीआई कुंजी को ज़ाहिर होने से रोका जा सकेगा.

क्लाइंट कनेक्शन शुरू करने से पहले, अपने सर्वर पर सीमित समय के लिए मान्य टोकन बनाएं:

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## इस्तेमाल की जा सकने वाली भाषाएं

Gemini 3.5 की Live बातचीत को ट्रांसक्रिप्ट करने की सुविधा के लिए, ये भाषाएँ और BCP-47 भाषा कोड उपलब्ध हैं:

| भाषा | BCP-47 कोड | भाषा | BCP-47 कोड |
| --- | --- | --- | --- |
| अफ़्रीकान्स | `af-ZA` | जापानी | `ja-JP` |
| अमहैरिक | `am-ET` | जावानीज़ | `jv-ID` |
| अरबी (मिस्र) | `ar-EG` | Kabuverdianu | `kea-CV` |
| आर्मीनियन | `hy-AM` | कन्नड़ | `kn-IN` |
| असमिया | `as-IN` | कज़ाक | `kk-KZ` |
| अज़रबैजानी | `az-AZ` | कोरियन | `ko-KR` |
| बेलारूसी | `be-BY` | किर्गिज़ | `ky-KG` |
| बांग्ला (बांग्लादेश) | `bn-BD` | लातवियन | `lv-LV` |
| बांग्ला (भारत) | `bn-IN` | लिंगाला | `ln-CD` |
| बोस्नियन | `bs-BA` | लिथुएनियन | `lt-LT` |
| बल्गैरियन | `bg-BG` | मैसेडोनियन | `mk-MK` |
| बल्गेरियन (ऐरोमेनियन) | `rup-BG` | मलय | `ms-MY` |
| बर्मीज़ | `my-MM` | मलयालम | `ml-IN` |
| कैंटोनीज़ (ट्रेडिशनल) | `yue-Hant-HK` | मोल्टीज़ | `mt-MT` |
| कैटलैन | `ca-ES` | मैंडरिन चाइनीज़ (सिंप्लिफ़ाइड) | `cmn-Hans-CN` |
| सेबुआनो | `ceb` | मराठी | `mr-IN` |
| सेंट्रल खमेर | `km-KH` | मंगोलियन | `mn-MN` |
| क्रोएशियन | `hr-HR` | नेपाली | `ne-NP` |
| चेक | `cs-CZ` | नॉर्वीजन | `nb-NO` |
| डैनिश | `da-DK` | ओड़िया | `or-IN` |
| डच | `nl-NL` | पोलिश | `pl-PL` |
| अंग्रेज़ी (ग्रेट ब्रिटेन) | `en-GB` | पॉर्चुगीज़ (ब्राज़ील) | `pt-BR` |
| अंग्रेज़ी (भारत) | `en-IN` | पॉर्चगीज़ (पुर्तगाल) | `pt-PT` |
| अंग्रेज़ी (संयुक्त राज्य अमेरिका) | `en-US` | पंजाबी | `pa-IN` |
| एस्टोनियन | `et-EE` | पंजाबी (गुरमुखी लिपि) | `pa-Guru-IN` |
| फ़ारसी | `fa-IR` | रोमानियन | `ro-RO` |
| फ़िलिपीनी | `fil-PH` | रूसी | `ru-RU` |
| फ़िनिश | `fi-FI` | सर्बियन | `sr-RS` |
| फ़्रांसीसी | `fr-FR` | सिंधी (अरबी लिपि) | `sd-Arab-IN` |
| गैलिशियन | `gl-ES` | स्लोवाक | `sk-SK` |
| जॉर्जियन | `ka-GE` | स्लोवेनियन | `sl-SI` |
| जर्मन | `de-DE` | स्पैनिश (लैटिन अमेरिका) | `es-419` |
| ग्रीक | `el-GR` | स्पैनिश (संयुक्त राज्य अमेरिका) | `es-US` |
| गुजराती | `gu-IN` | स्वाहिली (केन्या) | `sw-KE` |
| हौसा | `ha-NG` | स्वीडिश | `sv-SE` |
| हिब्रू | `he-IL` | ताजिक | `tg-TJ` |
| हिन्दी | `hi-IN` | तेलुगु | `te-IN` |
| हंगेरियन | `hu-HU` | थाई | `th-TH` |
| आइसलैंडिक | `is-IS` | टर्किश | `tr-TR` |
| इंडियन इंग्लिश | `en-IN` | यूक्रेनियन | `uk-UA` |
| इंडोनेशियन | `id-ID` | उज़्बेक | `uz-UZ` |
| इटैलियन | `it-IT` | वियतनामीज़ | `vi-VN` |

## पैरामीटर का रेफ़रंस

`input_audio_transcription` और `realtime_input_config` में मौजूद फ़ील्ड का इस्तेमाल करके, बोली को लेख में बदलने की सुविधा को कॉन्फ़िगर करें:

| पैरामीटर | टाइप | ब्यौरा |
| --- | --- | --- |
| `language_codes` | स्ट्रिंग का कलेक्शन | BCP-47 भाषा कोड (जैसे, `["en-US"]`). अगर इसे शामिल नहीं किया जाता है या यह खाली (`[]`) है, तो मॉडल अपने-आप भाषा का पता लगाता है और एक से ज़्यादा भाषाओं में बोले गए शब्दों को प्रोसेस करता है. |
| `custom_vocabulary` | स्ट्रिंग का कलेक्शन | ज़्यादा से ज़्यादा 1,000 कस्टम शब्द, संक्षिप्त नाम, ब्रैंड के नाम या व्यक्तिवाचक संज्ञाएं, ताकि स्पीच रिकग्निशन को बेहतर बनाया जा सके. |
| `mode` | स्ट्रिंग | बोली को लेख में बदलने का मोड: `"VERBATIM"` (डिफ़ॉल्ट) या `"SMART"` (स्मार्ट ट्रांसक्रिप्शन). `"SMART"` पर सेट होने पर, मॉडल फ़िलर शब्दों को हटा देता है, सूचियों को फ़ॉर्मैट करता है, और बोलने में होने वाली गलतियों को ठीक करता है. |
| `automatic_activity_detection.disabled` | बूलियन | आवाज़ की गतिविधि का अपने-आप पता लगने की सुविधा बंद करने के लिए, इसे `true` पर सेट करें. साथ ही, `activityStart` और `activityEnd` सिग्नल मैन्युअल तरीके से भेजें. |

### सर्वर के जवाब वाले फ़ील्ड

| फ़ील्ड | ब्यौरा |
| --- | --- |
| `server_content.interim_input_transcription` | कम समय में, कुछ समय के लिए आंशिक ट्रांसक्रिप्शन का अनुमान लगाया जाता है. यह अनुमान तब तक लगातार लगाया जाता है, जब तक उपयोगकर्ता बोलता रहता है. |
| `server_content.input_transcription` | जब कोई व्यक्ति बोलना बंद कर देता है, तब यह ट्रांसक्रिप्ट जारी की जाती है. यह ट्रांसक्रिप्ट, भरोसेमंद इनपुट पर आधारित होती है. |

## सीमाएं

- **सेशन कितनी देर चला:** लाइव ट्रांसक्रिप्शन की सुविधा के साथ, लगातार 10 मिनट तक स्ट्रीमिंग की जा सकती है.
- **स्पीकर डायराइज़ेशन:** स्पीकर डायराइज़ेशन की सुविधा, लाइव स्ट्रीमिंग सेशन में काम नहीं करती. स्पीकर के हिसाब से ऑडियो को टेक्स्ट में बदलने के लिए, नॉन-स्ट्रीमिंग [ऑडियो ट्रांसक्रिप्शन](https://ai.google.dev/gemini-api/docs/transcribe?hl=hi#speaker-diarization) एंडपॉइंट का इस्तेमाल करें.
- **शब्द के लेवल पर टाइमस्टैंप:** Live API पर, शब्द के लेवल पर टाइमस्टैंप की सुविधा काम नहीं करती. Live API, बोले गए शब्दों के लेवल के टाइमस्टैंप (`interim_input_transcription` और `input_transcription`) दिखाता है.
- **कस्टम शब्दावली:** `custom_vocabulary` में ज़्यादा से ज़्यादा 1,000 शब्द जोड़े जा सकते हैं. हालांकि, आम तौर पर 100 शब्दों से ही सबसे अच्छे नतीजे मिलते हैं.
- **मोड के साथ काम करने की सुविधा:** स्मार्ट ट्रांसक्रिप्शन (`"mode": "SMART"`) की सुविधा, फ़ालतू शब्दों को हटाती है और इंटेंट के हिसाब से टेक्स्ट को फ़ॉर्मैट करती है. हालांकि, इसे शब्द के एनोटेशन के साथ इस्तेमाल नहीं किया जा सकता.

## आगे क्या करना है

- स्ट्रीम नहीं की जा रही ऑडियो फ़ाइलों के लिए, [Gemini Transcribe से जुड़ा दस्तावेज़](https://ai.google.dev/gemini-api/docs/transcribe?hl=hi) पढ़ें.
- बातचीत करने वाले वॉइस एजेंट के लिए, [Live API की खास जानकारी](https://ai.google.dev/gemini-api/docs/live-api?hl=hi) पढ़ें.
- बोले जा रहे शब्दों का रीयल-टाइम में अनुवाद पाने के लिए, [लाइव ट्रांसलेशन गाइड](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=hi) पढ़ें.
- लाइव एपीआई स्ट्रीमिंग की कीमत जानने के लिए, [कीमत तय करने से जुड़ा पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#gemini-3.5-transcribe-live) देखें.
- [Live API की सुविधाओं के बारे में जानकारी देने वाली गाइड](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-10 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-10 (UTC) को अपडेट किया गया."],[],[]]
