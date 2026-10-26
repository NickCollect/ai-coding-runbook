---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=hi
fetched_at: 2026-10-26T05:50:38.731775+00:00
title: "Gemini Live API \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0932\u093e\u0907\u0935 \u0905\u0928\u0941\u0935\u093e\u0926 \u0915\u0930\u0928\u0947 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Live API की मदद से लाइव अनुवाद करने की सुविधा

Gemini Live API, [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=hi) मॉडल का इस्तेमाल करके, 70 से ज़्यादा भाषाओं के बीच कम इंतज़ार के समय में रीयल-टाइम में बोली का अनुवाद करने की सुविधा देता है. लाइव एपीआई को अनुवाद की सेटिंग के साथ कॉन्फ़िगर करके, किसी एक भाषा में ऑडियो स्ट्रीम किया जा सकता है. साथ ही, अनुवाद किया गया ऑडियो आउटपुट दूसरी भाषा में पाया जा सकता है. इससे, रीयल-टाइम में एक भाषा से दूसरी भाषा में वॉइस-टू-वॉइस अनुवाद की सुविधा मिलती है.

[Google AI Studio में लाइव ट्रांसलेट की सुविधा आज़माएंmic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=hi)
[उदाहरण के तौर पर दिए गए ऐप्लिकेशन का क्लोन GitHub से बनाएंcode](https://github.com/google-gemini/gemini-live-api-examples)
[कोडिंग एजेंट की स्किल का इस्तेमाल करेंterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi#gemini-live-api-dev)

## लाइव एजेंट बनाम लाइव ट्रांसलेट

लाइव एपीआई का इस्तेमाल, लाइव एजेंट और लाइव ट्रांसलेट, दोनों के लिए किया जा सकता है. हालांकि, लाइव ट्रांसलेट का मेंटल मॉडल, रीयल-टाइम में एजेंट के साथ बातचीत करने के मॉडल से अलग होता है.

| लाइव एजेंट | लाइव ट्रांसलेट |
| --- | --- |
| **यह मॉडल, असिस्टेंट के तौर पर काम करता है.** यह आपकी बात सुनता है, समझता है, और आपकी ओर से कार्रवाइयां करता है. | **यह मॉडल, इंटरप्रेटर के तौर पर काम करता है.** यह रीयल-टाइम में अनुवाद करने वाले पाइपलाइन की तरह काम करता है. |
| **यह बारी-बारी से होने वाले इंटरैक्शन का इस्तेमाल करता है.** यह रुकने, इरादे का पता लगाने, और बीच में होने वाली रुकावटों को मैनेज करने पर काम करता है. | **यह लगातार स्ट्रीम प्रोसेसिंग का इस्तेमाल करता है.** यह बारी का इंतज़ार किए बिना, स्पीकर के बोलते ही अनुवाद करता है. |
| **यह टूल और एजेंट के साथ काम करता है.** यह फ़ंक्शन कॉल करने, Google Search, और निर्देशों के साथ काम करता है. | **यह सिर्फ़ अनुवाद की सुविधा देता है.** यह कम इंतज़ार के समय में अनुवाद करता है. साथ ही, यह टूल या निर्देशों के साथ काम नहीं करता. |
| **यह पूरी तरह से मल्टीमोडल है.** यह टेक्स्ट, ऑडियो, वीडियो, और इमेज इनपुट के साथ काम करता है. | **यह सिर्फ़ ऑडियो के साथ काम करता है.** इसमें सिर्फ़ ऑडियो इनपुट इस्तेमाल किया जा सकता है, ताकि रीयल-टाइम में इंतज़ार के समय की सीमा को बनाए रखा जा सके. |
| **विस्तृत कॉन्फ़िगरेशन.** यह जनरेशन, स्पीच, टूल, और सिस्टम के निर्देशों का इस्तेमाल करता है. | **यह आसानी से कॉन्फ़िगर किया जा सकता है.** `target_language_code` और `echo_target_language` जैसे टॉगल सेट करें. |

## शुरू करें

यहां दिए गए उदाहरणों में, क्लाइंट को शुरू करने और अनुवाद के कॉन्फ़िगरेशन के साथ लाइव एपीआई से कनेक्ट करने का तरीका बताया गया है.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## ऑडियो भेजना

अनुवाद के लिए वॉइस इनपुट स्ट्रीम करने के लिए, आपको रॉ, लिटिल-एंडियन, 16-बिट पीसीएम ऑडियो भेजना होगा.

- **इनपुट ऑडियो का फ़ॉर्मैट**: रॉ 16-बिट पीसीएम, 16 किलोहर्ट्ज़ (मोनो, लिटिल-एंडियन).
- **आउटपुट ऑडियो का फ़ॉर्मैट**: रॉ 16-बिट पीसीएम, 24 किलोहर्ट्ज़ (मोनो, लिटिल-एंडियन).
- **चंक का साइज़ और इंतज़ार का समय**: 100 मि॰से॰ के चंक में ऑडियो भेजें.

यहां दिए गए उदाहरणों में, सेशन में ऑडियो चंक भेजने का तरीका बताया गया है.

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

### WebSockets

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## कॉन्फ़िगरेशन

अनुवाद की सुविधा चालू करने के लिए, आपको सेशन सेटअप के दौरान `generationConfig` में `translationConfig` की जानकारी देनी होगी.

### सेटअप मैसेज का कॉन्फ़िगरेशन

ट्रांसक्रिप्ट की सुविधा चालू करने के लिए, `generationConfig` में ये फ़ील्ड इस्तेमाल किए जा सकते हैं:

- **`inputAudioTranscription`**: यह एक ऐसा ऑब्जेक्ट है जो मौजूद होने पर, मॉडल को इनपुट ऑडियो के टेक्स्ट ट्रांसक्रिप्ट भेजने की अनुमति देता है.
- **`outputAudioTranscription`**: यह एक ऐसा ऑब्जेक्ट है जो मौजूद होने पर, मॉडल को आउटपुट (अनुवाद किए गए) ऑडियो के टेक्स्ट ट्रांसक्रिप्ट भेजने की अनुमति देता है.

`translationConfig` में ये फ़ील्ड इस्तेमाल किए जा सकते हैं:

- **`targetLanguageCode`**: यह उस भाषा का [BCP-47 भाषा कोड](#supported-languages) है जिसमें आपको मॉडल से अनुवाद कराना है. उदाहरण के लिए, पोलिश के लिए `"pl"` और स्पैनिश के लिए `"es"`. डिफ़ॉल्ट रूप से, यह `"en"` पर सेट होता है.
- **`echoTargetLanguage`**: यह एक बूलियन है, जो यह दिखाता है कि टारगेट भाषा में मौजूद इनपुट ऑडियो को कैसे हैंडल किया जाना चाहिए. अगर इसे `true` पर सेट किया जाता है, तो मॉडल, टारगेट भाषा में मौजूद इनपुट ऑडियो को दोहराएगा. अगर इसे `false` पर सेट किया जाता है, तो मॉडल, टारगेट भाषा में मौजूद इनपुट स्पीच के दौरान चुप रहेगा. डिफ़ॉल्ट रूप से, यह `false` पर सेट होता है.

यहां सेटअप मैसेज के स्ट्रक्चर का उदाहरण दिया गया है:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## क्लाइंट-साइड ऐप्लिकेशन में, कुछ समय के लिए मान्य टोकन का इस्तेमाल करना

क्लाइंट-टू-सर्वर ऐप्लिकेशन के लिए, आप अपनी एपीआई कुंजी को सार्वजनिक होने से बचाने के लिए [कुछ समय के लिए मान्य टोकन](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=hi) (फ़िलहाल `v1beta` में उपलब्ध) का इस्तेमाल कर सकते हैं.

लाइव ट्रांसलेट के साथ, कुछ समय के लिए मान्य टोकन का इस्तेमाल करते समय:

1. आपको `v1beta` एंडपॉइंट का इस्तेमाल करना होगा.
2. **कॉन्फ़िगरेशन लॉक करना:** डिफ़ॉल्ट रूप से, आपको अपने सर्वर पर टोकन बनाने की पाबंदियों में `translationConfig` की जानकारी देनी चाहिए. इससे यह पक्का होता है कि अनुवाद का कॉन्फ़िगरेशन लॉक है और क्लाइंट इसमें कोई बदलाव नहीं कर सकता.
3. **कॉन्फ़िगरेशन अनलॉक करना:** अगर आपको क्लाइंट-साइड पर `translationConfig` सेट करने की अनुमति देनी है (उदाहरण के लिए, किसी उपयोगकर्ता को अपनी टारगेट भाषा चुनने की अनुमति देने के लिए), तो आपको टोकन बनाने के अनुरोध से इसे हटाना होगा. इसके बजाय, `"lock_additional_fields": []` सेट करना होगा. इससे क्लाइंट-साइड पर `translationConfig` सेट करने की अनुमति मिल जाएगी.

### पाबंदियों के साथ, कुछ समय के लिए मान्य टोकन बनाना

यहां दिए गए उदाहरणों में, अनुवाद की पाबंदियों के साथ, कुछ समय के लिए मान्य टोकन बनाने का तरीका बताया गया है.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
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
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## सीमाएं

- **इनपुट के तरीके**: अनुवाद के लिए, सिर्फ़ ऑडियो इनपुट इस्तेमाल किया जा सकता है. टेक्स्ट इनपुट इस्तेमाल नहीं किया जा सकता.
- **आवाज़ की कॉपी बनाना**: आवाज़ की कॉपी बनाने में गड़बड़ी हो सकती है. ज़्यादा समय तक रुकने के बाद, आवाज़ें बदल सकती हैं. साथ ही, स्पीच की शुरुआत के आधार पर, गलत जेंडर असाइन हो सकता है. इसके अलावा, एक से ज़्यादा स्पीकर के साथ तेज़ी से बातचीत करने के दौरान, आवाज़ें एक ही आवाज़ पर अटक सकती हैं.
- **भाषा का पता लगाना**: भाषा का पता लगाने में, तेज़ लहजे, मिलती-जुलती भाषाओं (जैसे, स्पैनिश बनाम पॉर्चुगीज़) या तेज़ी से भाषा बदलने में दिक्कत आ सकती है. **ध्यान दें:** इसका असर सिर्फ़ इनपुट ट्रांसक्रिप्ट पर पड़ना चाहिए. भाषा कोड और फ़ाइनल अनुवाद अब भी सटीक होने चाहिए.
- **बैकग्राउंड ऑडियो**: मॉडल को शोर और संगीत को फ़िल्टर करके, साफ़ स्पीच बनाने के लिए डिज़ाइन किया गया है. हालांकि, हो सकता है कि सभी बैकग्राउंड ऑडियो को अनदेखा न किया जाए.
- **टारगेट भाषा को दोहराना**: जब `echoTargetLanguage: true` होता है, तब अगर इनपुट ऑडियो पहले से ही टारगेट भाषा में है, तो बैकग्राउंड में मौजूद शोर या संगीत की वजह से, अनुवाद किए गए ऑडियो में गड़बड़ियां आ सकती हैं.

## इस्तेमाल की जा सकने वाली भाषाएं

लाइव ट्रांसलेट की सुविधा इन भाषाओं में उपलब्ध है.

| भाषा | BCP-47 कोड | भाषा | BCP-47 कोड |
| --- | --- | --- | --- |
| अफ़्रीकान्स | af | कज़ाक़ | kk |
| Akan | ak | ख्मेर | km |
| अल्बेनियन | sq | किनयारवांडा | rw |
| अमहैरिक | am | कोरियन | ko |
| अरबी | ar | लाओ | lo |
| आर्मीनियन | hy | लातवियन | lv |
| अज़रबैजानी | az | लिथुएनियन | lt |
| बॉस्क | eu | मैसेडोनियन | mk |
| बेलारूसी | be | मलय | ms |
| बांग्ला | bn | मलयालम | ml |
| बल्गैरियन | bg | मराठी | mr |
| बर्मी (म्यांमार) | my | मंगोलियन | mn |
| कैटलैन | ca | नेपाली | ne |
| चाइनीज़ (सिंप्लिफ़ाइड) | zh-Hans | नॉर्वीजन | no, nb |
| चाइनीज़ (ट्रेडिशनल) | zh-Hant | फ़ारसी | fa |
| क्रोएशियन | hr | पोलिश | pl |
| चेक | cs | पॉर्चुगीज़ (ब्राज़ील) | pt-BR |
| डैनिश | da | पॉर्चगीज़ (पुर्तगाल) | pt-PT |
| डच | nl | पंजाबी | pa |
| अंग्रेज़ी | en | रोमानियन | ro |
| एस्टोनियन | et | रूसी | ru |
| फ़िलिपीनी | fil | सर्बियन | sr |
| फ़िनिश | fi | सिंधी | sd |
| फ़्रांसीसी | fr | सिंहला | si |
| गैलिशियन | gl | स्लोवाक | sk |
| जॉर्जियन | ka | स्लोवेनियन | sl |
| जर्मन | de | स्पैनिश | es |
| ग्रीक | el | सूडानीज़ | su |
| गुजराती | gu | स्वाहिली | sw |
| हौसा | ha | स्वीडिश | sv |
| हिब्रू | he | तमिल | ta |
| हिन्दी | hi | तेलुगु | te |
| हंगेरियन | hu | थाई | th |
| आइसलैंडिक | is | टर्किश | tr |
| इंडोनेशियन | id | यूक्रेनियन | uk |
| इटैलियन | it | उर्दू | ur |
| जापानी | ja | उज़्बेक | uz |
| जावानीज़ | jv | वियतनामीज़ | vi |
| कन्नड़ | kn | ज़ुलू | zu |

## आगे क्या करना है

- लाइव एपीआई की [क्षमताओं](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=hi) के बारे में पूरी गाइड पढ़ें.
- [एसडीके इस्तेमाल करने की गाइड](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=hi) पढ़ें.
- [WebSockets इस्तेमाल करने की गाइड](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=hi) पढ़ें.
- क्लाइंट-टू-सर्वर ऐप्लिकेशन में सुरक्षित तरीके से पुष्टि करने के लिए, [कुछ समय के लिए मान्य टोकन](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=hi) की गाइड पढ़ें.
- GitHub से, [लाइव एपीआई के उदाहरणों](https://github.com/google-gemini/gemini-live-api-examples) का क्लोन बनाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया."],[],[]]
