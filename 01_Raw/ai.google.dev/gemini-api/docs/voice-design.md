---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=hi
fetched_at: 2026-10-26T05:41:46.314747+00:00
title: "\u0906\u0935\u093e\u091c\u093c \u0915\u093e \u0921\u093f\u091c\u093c\u093e\u0907\u0928 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# आवाज़ का डिज़ाइन

आवाज़ डिज़ाइन करने की सुविधा की मदद से, Gemini API के Voices एंडपॉइंट (`POST /v1beta/voices`) का इस्तेमाल करके, नैचुरल लैंग्वेज में दिए गए ब्यौरे से एक नया और स्थायी वोकल पर्सोना बनाया जा सकता है. पहले से मौजूद आवाज़ों या रेफ़रंस ऑडियो रिकॉर्ड करने के बजाय, किसी कैरेक्टर की उम्र, आवाज़, लहजे, और बोलने के तरीके के बारे में बताया जा सकता है. इसके बाद, आपको एक ऐसा `voice_...` आईडी मिलेगा जिसका दोबारा इस्तेमाल किया जा सकता है. यह आईडी आपके प्रोजेक्ट में सेव होगा.

कस्टम आवाज़ों को डिज़ाइन करने, उन्हें आज़माने, और उनमें बदलाव करने का सबसे तेज़ तरीका है [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में मौजूद इंटरैक्टिव **वॉइस डिज़ाइन** स्टूडियो का इस्तेमाल करना. टेक्स्ट प्रॉम्प्ट से कस्टम पर्सोना जनरेट किए जा सकते हैं. साथ ही, सैंपल स्क्रिप्ट की मदद से उनकी जांच की जा सकती है. इसके अलावा, जनरेट हुए `voice_...` आईडी को सीधे अपने ऐप्लिकेशन कोड में कॉपी किया जा सकता है.

[Google AI Studio में आज़माएं](https://aistudio.google.com/generate-speech?hl=hi)

[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) (`gemini-3.8-flash-tts`) और [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) (`gemini-3.8-flash-lite-tts`), दोनों में वॉइस डिज़ाइन की सुविधा काम करती है.

## डिजाइन की गई आवाज़ बनाना

टेक्स्ट के ब्यौरे से कस्टम आवाज़ बनाने के लिए, Google GenAI SDK (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) या REST API का इस्तेमाल करें. `"prompted"` आवाज़ों के लिए, `voices.create` (`CreateVoice`) और `voices.get` (`GetVoice`), दोनों ही आउटपुट-ओनली `sample_audio` फ़ील्ड (`mime_type: "audio/wav"`, base64-encoded `data`) दिखाते हैं, ताकि जनरेट की गई आवाज़ को तुरंत सुना जा सके:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## आवाज़ के डिज़ाइन की सुविधा कैसे काम करती है

1. **प्रॉम्प्ट के हिसाब से आवाज़ बनाना:** `type="prompted"` और `store=True` के साथ `voices.create` (`POST /v1beta/voices`) को कॉल करें.
2. **स्थायी `voice_id` और `sample_audio` की झलक पाना:** एपीआई, आवाज़ की पहचान जनरेट करता है और उसे आपके प्रोजेक्ट में सेव करता है. साथ ही, एक स्थायी आईडी (उदाहरण के लिए, `voice_abc123...`) और `sample_audio` (`mime_type: "audio/wav"`, base64-encoded `data`) दिखाता है. इसमें आवाज़ की जनरेट की गई झलक का ऑडियो होता है.
3. **स्पीच सिंथेसाइज़ करना:** सिंथेसिस के अनुरोधों में, `voice_id` को उस जगह पर पास करें जहां आवाज़ का नाम स्वीकार किया जाता है.

## अपनी आवाज़ में टेक्स्ट को बोलकर सुनाना

आवाज़ बनाने के बाद, उसे Interactions API को पास करें. इसके लिए, `id` (`voice_...`) का इस्तेमाल करें, ताकि आवाज़ जनरेट की जा सके:

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
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## अपनी आवाज़ें मैनेज करना

Voices API का इस्तेमाल करके, सेव की गई आवाज़ों को कभी भी सूची में देखा जा सकता है, फ़िल्टर किया जा सकता है, उनकी जांच की जा सकती है, और उन्हें मिटाया जा सकता है. सभी फ़िल्टर पैरामीटर के लिए, [आवाज़ की बड़ी लाइब्रेरी और फ़िल्टर करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#voice-library) देखें.

- **स्टोरेज की सीमाएं और टीटीएल:** स्टेटफ़ुल आवाज़ों (`store=True`, प्रॉम्प्ट की गई और रेप्लिका की गई आवाज़ों के साथ शेयर की जाती हैं) के लिए, **हर प्रोजेक्ट में 200 आवाज़ों** की सीमा होती है. साथ ही, इनके लिए **एक साल का टीटीएल** (टाइम-टू-लाइव) होता है.
- **`sample_audio` availability:** `voices.create()` (`CreateVoice`) और
  `voices.get()` (`GetVoice`) `"prompted"` आवाज़ों के लिए, `sample_audio` (`mime_type:
  "audio/wav"`, base64-encoded `data`) की वैल्यू भरते हैं. लिस्टिंग को छोटा रखने के लिए, `voices.list()` (`ListVoices`) `sample_audio` को शामिल नहीं करता है. साथ ही, `"replicated"` और `"prebuilt"` आवाज़ों के लिए `sample_audio` को सेट नहीं किया जाता है.

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## आवाज़ के डिज़ाइन के लिए प्रॉम्प्ट लिखने के सबसे सही तरीके

- **आवाज़ के डिज़ाइन में, आवाज़ की स्थायी विशेषताओं को शामिल करें, न कि `style` में:** `voices.create` में आवाज़ बनाते समय, आवाज़ की
  स्थायी विशेषताओं के बारे में बताएं. जैसे, उम्र, लिंग, टिंबर, वोकल टेक्सचर, और
  क्षेत्रीय लहजा.
- **किसी खास स्थिति में अपनी भावनाएं ज़ाहिर करने के लिए `speech_metadata.style` का इस्तेमाल करें:** कस्टम वॉइस बनाने के बाद, छोटे `style` प्रॉम्प्ट का इस्तेमाल करें. उदाहरण के लिए, `"whispered urgently"` या `"cheerful and energetic"`. इससे स्पीकर की मुख्य पहचान बदले बिना, बारी-बारी से ऐक्टिंग की जा सकेगी.
- **सटीक और कम शब्दों में जानकारी दें:** एक या दो वाक्यों में साफ़ तौर पर जानकारी दें. जैसे, *"30 साल की एक महिला, जो खेल के बारे में उत्साह के साथ जानकारी देती है और जिसका लहजा मिडवेस्टर्न है"*. इससे, विरोधाभासी या बहुत लंबे पैराग्राफ़ की तुलना में ज़्यादा सटीक और बेहतर नतीजे मिलते हैं.

## आगे क्या करना है

- [आवाज़ की नकल बनाने की सुविधा](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi) का इस्तेमाल करके, किसी मौजूदा स्पीकर की आवाज़ की नकल बनाने का तरीका जानें.
- [टेक्स्ट को ऑडियो में बदलने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi) में, टर्न-लेवल स्टाइलिंग, इनलाइन टैग, और एक से ज़्यादा स्पीकर वाले डायलॉग के बारे में जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया."],[],[]]
