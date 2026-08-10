---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=hi
fetched_at: 2026-08-10T03:22:19.847086+00:00
title: "Gemini 3 \u0915\u0940 \u0921\u0947\u0935\u0932\u092a\u0930 \u0917\u093e\u0907\u0921 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)

सुझाव भेजें

# Gemini 3 की डेवलपर गाइड

Gemini 3, अब तक का हमारा सबसे ऐडवांस मॉडल है. इसे बेहतरीन रीज़निंग के आधार पर बनाया गया है. इसे किसी भी आइडिया को हकीकत में बदलने के लिए डिज़ाइन किया गया है. इसके लिए, यह एजेंटिक वर्कफ़्लो, अपने-आप कोडिंग करने की सुविधा, और मुश्किल मल्टीमॉडल टास्क को बेहतर तरीके से पूरा करता है.
इस गाइड में, Gemini 3 मॉडल फ़ैमिली की मुख्य सुविधाओं के बारे में बताया गया है. साथ ही, इससे ज़्यादा से ज़्यादा फ़ायदा पाने का तरीका भी बताया गया है.

[Gemini 3.1 Pro की झलक आज़माएँ](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=hi)
[Gemini 3 Flash की झलक आज़माएँ](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=hi)
[Gemini 3.1 Flash-Lite आज़माएँ](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=hi)
[Nano Banana 2 आज़माएँ](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=hi)

[Gemini 3 की सुविधा वाले ऐप्लिकेशन के हमारे कलेक्शन](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=hi) को एक्सप्लोर करें. इससे आपको यह पता चलेगा कि यह मॉडल, ऐडवांस रीज़निंग, ऑटोनॉमस कोडिंग, और मुश्किल मल्टीमॉडल टास्क को कैसे हैंडल करता है.

कोड की कुछ लाइनों के साथ शुरू करें:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## पेश है Gemini 3 सीरीज़

Gemini 3.1 Pro, मुश्किल कामों के लिए सबसे अच्छा है. इसके लिए, दुनिया के बारे में ज़्यादा जानकारी और अलग-अलग मोड में ऐडवांस रिज़निंग की ज़रूरत होती है.

Gemini 3 Flash, 3-सीरीज़ का हमारा नया मॉडल है. इसमें Pro-लेवल की इंटेलिजेंस की सुविधा मिलती है. साथ ही, यह Flash की स्पीड और कीमत में उपलब्ध है.

Nano Banana Pro (इसे Gemini 3 Pro Image भी कहा जाता है) इमेज जनरेट करने वाला हमारा सबसे बेहतरीन मॉडल है. वहीं, Nano Banana 2 (इसे Gemini 3.1 Flash Image भी कहा जाता है) इमेज जनरेट करने वाला ऐसा मॉडल है जो कम समय में ज़्यादा इमेज जनरेट करता है, ज़्यादा असरदार है, और कम कीमत में उपलब्ध है.

Gemini 3.1 Flash-Lite, हमारा वर्कहॉर्स मॉडल है. इसे कम लागत में ज़्यादा काम करने के लिए बनाया गया है.

| मॉडल आईडी | कॉन्टेक्स्ट विंडो (इन / आउट) | नॉलेज कटऑफ़ | कीमत (इनपुट / आउटपुट)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 10 लाख / 64 हज़ार | जनवरी 2025 | 0.25 डॉलर (टेक्स्ट, इमेज, वीडियो), 0.50 डॉलर (ऑडियो) / 1.50 डॉलर |
| **gemini-3.1-flash-image-preview** | 128k / 32k | जनवरी 2025 | 0.25 डॉलर (टेक्स्ट इनपुट) / 0.067 डॉलर (इमेज आउटपुट)\*\* |
| **gemini-3.1-pro-preview** | 10 लाख / 64 हज़ार | जनवरी 2025 | 2 डॉलर / 12 डॉलर (<2 लाख टोकन)   4 डॉलर / 18 डॉलर (>2 लाख टोकन) |
| **gemini-3-flash-preview** | 10 लाख / 64 हज़ार | जनवरी 2025 | 0.50 डॉलर / 3 डॉलर |
| **gemini-3-pro-image-preview** | 65 हज़ार / 32 हज़ार | जनवरी 2025 | $2 (टेक्स्ट इनपुट) / $0.134 (इमेज आउटपुट)\*\* |

*\* कीमत, 10 लाख टोकन के हिसाब से तय की जाती है. हालांकि, इसमें बदलाव किया जा सकता है.*
*\*\* इमेज की कीमत, रिज़ॉल्यूशन के हिसाब से अलग-अलग होती है. ज़्यादा जानकारी के लिए, [कीमत तय करने से जुड़ा पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.*

सीमाओं, कीमत, और अन्य जानकारी के बारे में ज़्यादा जानने के लिए, [मॉडल पेज](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi) देखें.

## Gemini 3 में नई API सुविधाएं

Gemini 3 में नए पैरामीटर जोड़े गए हैं. इनकी मदद से डेवलपर को लेटेन्सी, लागत, और मल्टीमॉडल फ़िडेलिटी पर ज़्यादा कंट्रोल मिलता है.

### सूझ-बूझ वाले मॉडल का लेवल

Gemini 3 सीरीज़ के मॉडल, डिफ़ॉल्ट रूप से डाइनैमिक थिंकिंग का इस्तेमाल करते हैं, ताकि वे प्रॉम्प्ट के बारे में सोच-समझकर जवाब दे सकें. `thinking_level` पैरामीटर का इस्तेमाल किया जा सकता है. यह पैरामीटर, मॉडल के जवाब देने से पहले, मॉडल की इंटरनल रीज़निंग प्रोसेस की **ज़्यादा से ज़्यादा** डेप्थ को कंट्रोल करता है. Gemini 3, इन लेवल को टोकन की गारंटी के तौर पर नहीं, बल्कि सोचने के लिए उपलब्ध टोकन की संख्या के तौर पर मानता है.

अगर `thinking_level` के लिए कोई वैल्यू नहीं डाली गई है, तो Gemini 3 डिफ़ॉल्ट रूप से `high` पर सेट होगा. अगर आपको ऐसे जवाब चाहिए जिनमें कम समय लगे और जटिल गहराई से विश्लेषण की ज़रूरत न हो, तो मॉडल के गहराई से विचार के लेवल को `low` पर सेट करें.

| सोचने का लेवल | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | ब्यौरा |
| --- | --- | --- | --- | --- |
| **`minimal`** | काम नहीं करता है | काम करता है (डिफ़ॉल्ट) | काम करता है | ज़्यादातर क्वेरी के लिए, यह "सोचने की ज़रूरत नहीं है" सेटिंग से मेल खाती है. मुश्किल कोडिंग टास्क के लिए, मॉडल बहुत कम सोच-विचार कर सकता है. यह चैट या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए, लेटेन्सी को कम करता है. ध्यान दें कि `minimal` इस बात की गारंटी नहीं देता कि सोचने की सुविधा बंद हो गई है. |
| **`low`** | काम करता है | काम करता है | काम करता है | इससे इंतज़ार का समय और लागत कम हो जाती है. यह मॉडल, आसान निर्देशों का पालन करने, चैट करने या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए सबसे अच्छा है. |
| **`medium`** | काम करता है | काम करता है | काम करता है | ज़्यादातर कामों के लिए, सोच-समझकर जवाब देता है. |
| **`high`** | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | काम करता है (डाइनैमिक) | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | इससे गहराई से विश्लेषण की गहराई बढ़ जाती है. मॉडल को पहली बार (बिना सोचे-समझे) आउटपुट टोकन तक पहुंचने में ज़्यादा समय लग सकता है. हालांकि, आउटपुट ज़्यादा सोच-समझकर दिया जाएगा. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### मीडिया रिज़ॉल्यूशन

Gemini 3 में, `media_resolution` पैरामीटर का इस्तेमाल करके, मल्टीमॉडल विज़न प्रोसेसिंग को बेहतर तरीके से कंट्रोल करने की सुविधा मिलती है. ज़्यादा रिज़ॉल्यूशन से, मॉडल को छोटे टेक्स्ट को पढ़ने या छोटी-छोटी बारीकियों को पहचानने में मदद मिलती है. हालांकि, इससे टोकन का इस्तेमाल और इंतज़ार का समय बढ़ जाता है.
`media_resolution` पैरामीटर से यह तय होता है कि **हर इनपुट इमेज या वीडियो फ़्रेम के लिए, ज़्यादा से ज़्यादा कितने टोकन
मिलेंगे.**

अब हर मीडिया पार्ट या ग्लोबल लेवल पर रिज़ॉल्यूशन को `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` या `media_resolution_ultra_high` पर सेट किया जा सकता है. ग्लोबल लेवल पर रिज़ॉल्यूशन सेट करने के लिए, `generation_config` का इस्तेमाल करें. हालांकि, अल्ट्रा हाई रिज़ॉल्यूशन के लिए ग्लोबल लेवल पर रिज़ॉल्यूशन सेट करने की सुविधा उपलब्ध नहीं है. यह जानकारी उपलब्ध न होने पर, मॉडल मीडिया टाइप के आधार पर सबसे सही डिफ़ॉल्ट सेटिंग का इस्तेमाल करता है.

**सुझाई गई सेटिंग**

| मीडिया किस तरह का है | सुझाई गई सेटिंग | ज़्यादा से ज़्यादा टोकन | इस्तेमाल से जुड़े दिशा-निर्देश |
| --- | --- | --- | --- |
| **इमेज** | `media_resolution_high` | 1120 | ज़्यादातर इमेज विश्लेषण के टास्क के लिए, इस विकल्प का इस्तेमाल करने का सुझाव दिया जाता है, ताकि सबसे अच्छी क्वालिटी मिल सके. |
| **PDF** | `media_resolution_medium` | 560 | दस्तावेज़ को समझने के लिए सबसे सही; क्वालिटी आम तौर पर `medium` पर पहुंच जाती है. `high` बढ़ाने से, स्टैंडर्ड दस्तावेज़ों के लिए ओसीआर के नतीजों में शायद ही कभी सुधार होता है. |
| **वीडियो** (सामान्य) | `media_resolution_low` (या `media_resolution_medium`) | 70 (हर फ़्रेम के लिए) | **ध्यान दें:** वीडियो के लिए, कॉन्टेक्स्ट के इस्तेमाल को ऑप्टिमाइज़ करने के लिए, `low` और `medium` सेटिंग को एक जैसा (70 टोकन) माना जाता है. यह, कार्रवाई की पहचान करने और उसके बारे में बताने वाले ज़्यादातर टास्क के लिए काफ़ी है. |
| **वीडियो** (इसमें ज़्यादातर टेक्स्ट होता है) | `media_resolution_high` | 280 (हर फ़्रेम के लिए) | इसकी ज़रूरत सिर्फ़ तब होती है, जब इस्तेमाल के उदाहरण में, वीडियो फ़्रेम में मौजूद छोटे-छोटे ऑब्जेक्ट या ज़्यादा टेक्स्ट (ओसीआर) को पढ़ना हो. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### तापमान

हमारा सुझाव है कि Gemini 3 के सभी मॉडल के लिए, टेंपरेचर पैरामीटर को डिफ़ॉल्ट वैल्यू `1.0` पर सेट रखें.

पिछले मॉडल में, क्रिएटिविटी और डिटरमिनिज़्म को कंट्रोल करने के लिए, अक्सर टेंपरेचर को ट्यून करने से फ़ायदा मिलता था. हालांकि, Gemini 3 की तर्क करने की क्षमताओं को डिफ़ॉल्ट सेटिंग के लिए ऑप्टिमाइज़ किया गया है. तापमान को बदलने (इसे 1.0 से कम पर सेट करने) से, मॉडल उम्मीद के मुताबिक काम नहीं कर सकता. जैसे, यह एक ही जवाब को बार-बार दोहरा सकता है या इसकी परफ़ॉर्मेंस खराब हो सकती है. ऐसा खास तौर पर, गणित के मुश्किल सवालों या तर्क से जुड़े सवालों के जवाब देते समय हो सकता है.

### सोच-समझकर किए गए हस्ताक्षर

Gemini 3, [Thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi) का इस्तेमाल करता है, ताकि एपीआई कॉल के दौरान तर्क से जुड़े कॉन्टेक्स्ट को बनाए रखा जा सके. ये सिग्नेचर, मॉडल की इंटरनल थॉट प्रोसेस के एन्क्रिप्ट किए गए वर्शन होते हैं. यह पक्का करने के लिए कि मॉडल अपनी तर्क करने की क्षमताओं को बनाए रखे, आपको इन हस्ताक्षर को अपने अनुरोध में मॉडल को ठीक उसी तरह वापस भेजना होगा जिस तरह से वे मिले थे:

- **फ़ंक्शन कॉलिंग (सख्ती से लागू):** एपीआई, "Current Turn" पर पुष्टि करने की प्रक्रिया को सख्ती से लागू करता है. हस्ताक्षर मौजूद न होने पर, 400 गड़बड़ी का मैसेज दिखेगा.
- **टेक्स्ट/चैट:** पुष्टि करने की सुविधा को सख्ती से लागू नहीं किया जाता. हालांकि, हस्ताक्षर शामिल न करने से, मॉडल की गहराई से विश्लेषण करने की क्षमता और जवाब की क्वालिटी खराब हो जाएगी.
- **इमेज जनरेट करना/बदलाव करना (सख्त)**: एपीआई, मॉडल के सभी हिस्सों पर पुष्टि करने की सख्त प्रक्रिया लागू करता है. इसमें `thoughtSignature` भी शामिल है. हस्ताक्षर मौजूद न होने पर, 400 गड़बड़ी का मैसेज दिखेगा.

#### फ़ंक्शन कॉलिंग (सटीक पुष्टि)

जब Gemini कोई `functionCall` जनरेट करता है, तो वह `thoughtSignature` पर भरोसा करता है, ताकि अगले टर्न में टूल के आउटपुट को सही तरीके से प्रोसेस किया जा सके. "मौजूदा बातचीत" में, मॉडल (`functionCall`) और उपयोगकर्ता (`functionResponse`) के वे सभी चरण शामिल होते हैं जो **उपयोगकर्ता** के आखिरी स्टैंडर्ड `text` मैसेज के बाद हुए हैं.

- **सिंगल फ़ंक्शन कॉल:** `functionCall` वाले हिस्से में एक सिग्नेचर होता है. आपको इसे वापस करना होगा.
- **फ़ंक्शन को एक साथ कॉल करना:** सूची में मौजूद सिर्फ़ पहले `functionCall` हिस्से में हस्ताक्षर शामिल होगा. आपको पार्ट्स उसी क्रम में लौटाने होंगे जिस क्रम में आपको मिले थे.
- **एक से ज़्यादा चरणों वाला (क्रमिक):** अगर मॉडल किसी टूल को कॉल करता है, नतीजे पाता है, और *दूसरे* टूल को कॉल करता है (एक ही टर्न में), तो **दोनों** फ़ंक्शन कॉल के सिग्नेचर होते हैं. आपको इतिहास में इकट्ठा किए गए **सभी** हस्ताक्षर वापस भेजने होंगे.

#### टेक्स्ट और स्ट्रीमिंग

स्टैंडर्ड चैट या टेक्स्ट जनरेट करने के लिए, हस्ताक्षर का होना ज़रूरी नहीं है.

- **नॉन-स्ट्रीमिंग**: जवाब के आखिरी हिस्से में `thoughtSignature` हो सकता है. हालांकि, यह हमेशा मौजूद नहीं होता. अगर कोई प्रॉडक्ट वापस आता है, तो आपको उसे वापस भेजना चाहिए, ताकि बेहतर परफ़ॉर्मेंस बनी रहे.
- **स्ट्रीमिंग**: अगर कोई हस्ताक्षर जनरेट किया जाता है, तो यह आखिरी हिस्से में आ सकता है. इसमें टेक्स्ट वाला हिस्सा खाली होता है. पक्का करें कि आपका स्ट्रीम पार्सर, टेक्स्ट फ़ील्ड खाली होने पर भी
  हस्ताक्षरों की जांच करता हो.

#### इमेज जनरेट और एडिट करने की सुविधा

`gemini-3-pro-image-preview` और `gemini-3.1-flash-image-preview` के लिए, बोलकर या लिखकर बदलाव करने की सुविधा के लिए, थॉट सिग्नेचर बहुत ज़रूरी हैं. जब मॉडल से किसी इमेज में बदलाव करने के लिए कहा जाता है, तो वह पिछली बारी में मिले `thoughtSignature` का इस्तेमाल करता है. इससे उसे ओरिजनल इमेज की कंपोज़िशन और लॉजिक को समझने में मदद मिलती है.

- **बदलाव करना:** जवाब के बारे में जानकारी (`text` या `inlineData`) देने के बाद, पहले हिस्से में हस्ताक्षर मौजूद होते हैं. साथ ही, इसके बाद के हर `inlineData` हिस्से में भी हस्ताक्षर मौजूद होते हैं. गड़बड़ियों से बचने के लिए, आपको इन सभी हस्ताक्षर को वापस भेजना होगा.

#### कोड के उदाहरण

#### एक के बाद एक कई फ़ंक्शन कॉल करना

उपयोगकर्ता ने एक ही बार में ऐसा सवाल पूछा है जिसके लिए दो अलग-अलग चरणों (फ़्लाइट की जानकारी देखना -> टैक्सी बुक करना) की ज़रूरत होती है.   
  
**पहला चरण: मॉडल, फ़्लाइट टूल को कॉल करता है.**  
मॉडल, हस्ताक्षर `<Sig_A>` दिखाता है

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**दूसरा चरण: उपयोगकर्ता, फ़्लाइट के नतीजे भेजता है**  
हमें `<Sig_A>` वापस भेजना होगा, ताकि मॉडल को जवाब देने के लिए सही जानकारी मिलती रहे.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**तीसरा चरण: मॉडल, टैक्सी टूल को कॉल करता है**  
मॉडल को `<Sig_A>` के ज़रिए फ़्लाइट में देरी होने की जानकारी मिलती है. अब वह टैक्सी बुक करने का फ़ैसला करता है. इससे *नया* हस्ताक्षर `<Sig_B>` जनरेट होता है.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**चौथा चरण: उपयोगकर्ता, टैक्सी का नतीजा भेजता है**  
बातचीत को पूरा करने के लिए, आपको पूरी चेन वापस भेजनी होगी: `<Sig_A>` और `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### पैरलल फ़ंक्शन कॉलिंग

उपयोगकर्ता पूछता है: "पेरिस और लंदन का मौसम कैसा है." मॉडल, एक जवाब में दो फ़ंक्शन कॉल दिखाता है.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### टेक्स्ट/संदर्भ के हिसाब से तर्क देना (पुष्टि नहीं की गई)

उपयोगकर्ता ऐसा सवाल पूछता है जिसके लिए, बाहरी टूल का इस्तेमाल किए बिना, कॉन्टेक्स्ट के हिसाब से तर्क देने की ज़रूरत होती है. हालांकि, हस्ताक्षर की पुष्टि नहीं की जाती है, लेकिन इसे शामिल करने से मॉडल को फ़ॉलो-अप सवालों के लिए तर्क की चेन बनाए रखने में मदद मिलती है.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### इमेज जनरेट करना और उनमें बदलाव करना

इमेज जनरेट करने के लिए, हस्ताक्षर की पुष्टि करना ज़रूरी है. ये **पहले हिस्से** (टेक्स्ट या इमेज) और **बाद के सभी इमेज वाले हिस्सों** पर दिखते हैं. सभी को अगले टर्न में वापस कर दिया जाना चाहिए.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### दूसरे मॉडल से माइग्रेट करना

अगर किसी दूसरे मॉडल (जैसे, Gemini 2.5) से बातचीत का ट्रेस ट्रांसफ़र किया जा रहा है या Gemini 3 से जनरेट नहीं किया गया कस्टम फ़ंक्शन कॉल डाला जा रहा है, तो आपके पास मान्य हस्ताक्षर नहीं होगा.

इन खास स्थितियों में, पुष्टि करने की सख्त प्रक्रिया को बायपास करने के लिए, फ़ील्ड में यह डमी स्ट्रिंग डालें: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### टूल के साथ स्ट्रक्चर्ड आउटपुट

Gemini 3 मॉडल की मदद से, [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) को बिल्ट-इन टूल के साथ जोड़ा जा सकता है. इनमें ये टूल शामिल हैं: [Google Search से जानकारी पाना](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), [यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi), [कोड एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi), और [फ़ंक्शन कॉल करना](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Image generation

Gemini 3.1 Flash Image और Gemini 3 Pro Image की मदद से, टेक्स्ट प्रॉम्प्ट से इमेज जनरेट की जा सकती हैं और उनमें बदलाव किया जा सकता है. यह किसी प्रॉम्प्ट के बारे में "सोचने" के लिए, गहराई से विश्लेषण का इस्तेमाल करता है. साथ ही, [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) से भरोसेमंद स्रोतों से जानकारी लेने की सुविधा का इस्तेमाल करने से पहले, रीयल-टाइम डेटा को ऐक्सेस कर सकता है. जैसे, मौसम का पूर्वानुमान या स्टॉक चार्ट. इसके बाद, यह हाई फ़िडेलिटी इमेज जनरेट करता है.

**नई और बेहतर सुविधाएँ:**

- **4K और टेक्स्ट रेंडरिंग:** 2K और 4K रिज़ॉल्यूशन तक के टेक्स्ट और डायग्राम जनरेट करें, जो साफ़ हों और पढ़ने में आसान हों.
- **भरोसेमंद जानकारी के आधार पर कॉन्टेंट जनरेट करना:** `google_search` टूल का इस्तेमाल करके, तथ्यों की पुष्टि करें और असल दुनिया की जानकारी के आधार पर इमेज जनरेट करें. Google *इमेज* की मदद से जवाब में भरोसेमंद जानकारी शामिल करना
  Gemini 3.1 Flash Image के लिए उपलब्ध है.
- **बोलकर या लिखकर बदलाव करने की सुविधा:** सिर्फ़ बदलाव करने के लिए कहकर, इमेज में सिलसिलेवार बातचीत करके बदलाव करना. जैसे, "बैकग्राउंड को सूर्यास्त वाली इमेज में बदल दो". यह वर्कफ़्लो, बारी-बारी से बातचीत के दौरान विज़ुअल कॉन्टेक्स्ट को बनाए रखने के लिए, **थॉट सिग्नेचर** पर निर्भर करता है.

आस्पेक्ट रेशियो, बदलाव करने के वर्कफ़्लो, और कॉन्फ़िगरेशन के विकल्पों के बारे में पूरी जानकारी के लिए, [इमेज जनरेट करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) देखें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**जवाब का उदाहरण**

![टोक्यो का मौसम](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=hi)

### इमेज के साथ कोड एक्ज़ीक्यूट करना

Gemini 3 Flash, विज़न को सिर्फ़ एक स्टैटिक झलक के तौर पर नहीं, बल्कि एक ऐक्टिव जांच के तौर पर देख सकता है. [कोड को लागू करने](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) के साथ-साथ तर्क देने की क्षमता का इस्तेमाल करके, मॉडल एक प्लान बनाता है. इसके बाद, Python कोड लिखता है और उसे लागू करता है. इससे इमेज को ज़ूम इन किया जा सकता है, काटा जा सकता है, एनोटेट किया जा सकता है या उनमें अन्य बदलाव किए जा सकते हैं. ऐसा चरण-दर-चरण किया जाता है, ताकि मॉडल अपने जवाबों को विज़ुअल तौर पर बेहतर बना सके.

**इस्तेमाल के उदाहरण:**

- **ज़ूम करके देखना और बारीकी से जांच करना:** मॉडल अपने-आप पता लगा लेता है कि जानकारी बहुत छोटी है.उदाहरण के लिए, दूर से गेज या सीरियल नंबर पढ़ना. इसके बाद, मॉडल उस हिस्से को क्रॉप करने और ज़्यादा रिज़ॉल्यूशन पर फिर से जांच करने के लिए कोड लिखता है.
- **विज़ुअल मैथ और प्लॉटिंग:** मॉडल, कोड का इस्तेमाल करके कई चरणों में हिसाब-किताब कर सकता है. जैसे, रसीद पर मौजूद लाइन आइटम को जोड़ना या निकाले गए डेटा से Matplotlib चार्ट जनरेट करना.
- **इमेज एनोटेशन:** मॉडल, इमेज पर सीधे तौर पर ऐरो, बाउंडिंग बॉक्स या अन्य एनोटेशन बना सकता है. इससे, "यह आइटम कहां रखना चाहिए?" जैसे सवालों के जवाब दिए जा सकते हैं.

विज़ुअल थिंकिंग की सुविधा चालू करने के लिए, [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) को टूल के तौर पर कॉन्फ़िगर करें. ज़रूरत पड़ने पर, मॉडल इमेज में बदलाव करने के लिए कोड का इस्तेमाल अपने-आप करेगा.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

इमेज के साथ कोड एक्ज़ीक्यूशन के बारे में ज़्यादा जानकारी के लिए, [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi#images) लेख पढ़ें.

### टेक्स्ट, इमेज, और वीडियो वगैरह का इस्तेमाल करके की गई क्वेरी के जवाब

[मल्टीमॉडल फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#multimodal) की मदद से, उपयोगकर्ताओं को ऐसे फ़ंक्शन रिस्पॉन्स मिलते हैं जिनमें मल्टीमॉडल ऑब्जेक्ट शामिल होते हैं. इससे मॉडल की फ़ंक्शन कॉलिंग की सुविधाओं का बेहतर तरीके से इस्तेमाल किया जा सकता है. स्टैंडर्ड फ़ंक्शन कॉलिंग की सुविधा, सिर्फ़ टेक्स्ट पर आधारित फ़ंक्शन के जवाबों के साथ काम करती है:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### पहले से मौजूद टूल और फ़ंक्शन कॉलिंग को एक साथ इस्तेमाल करना

Gemini 3, एक ही एपीआई कॉल में बिल्ट-इन टूल (जैसे कि Google Search, यूआरएल कॉन्टेक्स्ट, और [अन्य](https://ai.google.dev/gemini-api/docs/tools?hl=hi)) और कस्टम [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) टूल का इस्तेमाल करने की अनुमति देता है. इससे ज़्यादा मुश्किल वर्कफ़्लो को मैनेज किया जा सकता है. [टूल के कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पेज पर जाकर ज़्यादा जानें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## Gemini 2.5 से माइग्रेट करना

Gemini 3, अब तक का हमारा सबसे ऐडवांस मॉडल है. यह Gemini 2.5 से ज़्यादा बेहतर है. माइग्रेट करते समय, इन बातों का ध्यान रखें:

- **सोच-समझकर जवाब देना:** अगर आपने Gemini 2.5 को सोच-समझकर जवाब देने के लिए, प्रॉम्प्ट इंजीनियरिंग की मुश्किल तकनीकों (जैसे, चेन ऑफ़ थॉट) का इस्तेमाल किया था, तो `thinking_level: "high"` और आसान प्रॉम्प्ट के साथ Gemini 3 को आज़माएँ.
- **टेंपरेचर सेटिंग:** अगर आपके मौजूदा कोड में, टेंपरेचर को साफ़ तौर पर सेट किया गया है (खास तौर पर, भरोसेमंद आउटपुट के लिए कम वैल्यू पर सेट किया गया है), तो हमारा सुझाव है कि इस पैरामीटर को हटा दें. साथ ही, Gemini 3 के डिफ़ॉल्ट टेंपरेचर 1.0 का इस्तेमाल करें. इससे, लूपिंग से जुड़ी समस्याओं या मुश्किल टास्क में परफ़ॉर्मेंस में गिरावट से बचा जा सकेगा.
- **पीडीएफ़ और दस्तावेज़ को समझना:**
  अगर आपने दस्तावेज़ को पार्स करने के लिए किसी खास तरीके का इस्तेमाल किया था, तो नई `media_resolution_high` सेटिंग को आज़माएं. इससे यह पक्का किया जा सकेगा कि आपको सटीक नतीजे मिलते रहें.
- **टोकन का इस्तेमाल:** Gemini 3 डिफ़ॉल्ट पर माइग्रेट करने से, PDF के लिए टोकन का इस्तेमाल **बढ़ सकता है**. हालांकि, वीडियो के लिए टोकन का इस्तेमाल **कम हो सकता है**. अगर डिफ़ॉल्ट रिज़ॉल्यूशन ज़्यादा होने की वजह से, अनुरोधों की संख्या अब कॉन्टेक्स्ट विंडो से ज़्यादा हो गई है, तो हमारा सुझाव है कि मीडिया रिज़ॉल्यूशन को साफ़ तौर पर कम करें.
- **इमेज सेगमेंटेशन:** इमेज सेगमेंटेशन की सुविधाएं, Gemini 3 Pro या Gemini 3 Flash में मौजूद नहीं हैं. इमेज सेगमेंटेशन की मदद से, ऑब्जेक्ट के लिए पिक्सल-लेवल के मास्क दिखाए जाते हैं. अगर आपको इमेज सेगमेंटेशन की सुविधा की ज़रूरत है, तो हमारा सुझाव है कि आप Gemini 2.5 Flash का इस्तेमाल जारी रखें. इसके लिए, आपको 'सोचने की सुविधा' बंद करनी होगी.
- **कंप्यूटर का इस्तेमाल:** Gemini 3 Pro और Gemini 3 Flash, [कंप्यूटर के इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) की सुविधा के साथ काम करते हैं. 2.5 सीरीज़ के उलट, कंप्यूटर के इस्तेमाल से जुड़े टूल को ऐक्सेस करने के लिए, आपको अलग मॉडल का इस्तेमाल करने की ज़रूरत नहीं है.
- **टूल के साथ काम करने की सुविधा**: [फ़ंक्शन कॉलिंग के साथ-साथ, पहले से मौजूद टूल का इस्तेमाल करने की सुविधा](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) अब Gemini 3 मॉडल के लिए उपलब्ध है. अब Gemini 3 मॉडल के लिए, [Maps से मिली जानकारी का इस्तेमाल करने की सुविधा](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi) भी उपलब्ध है.
- **जवाबों की संख्या**: Gemini 3 मॉडल, `candidateCount > 1` के साथ काम नहीं करते.
  इस पैरामीटर को `1` से ज़्यादा वैल्यू पर सेट करने पर, 400 गड़बड़ी दिखेगी.

## OpenAI के साथ काम करने की क्षमता

[OpenAI के साथ काम करने वाली लेयर](https://ai.google.dev/gemini-api/docs/openai?hl=hi) का इस्तेमाल करने वाले लोगों के लिए, स्टैंडर्ड पैरामीटर (OpenAI के `reasoning_effort`) अपने-आप Gemini (`thinking_level`) के बराबर मैप हो जाते हैं.

## प्रॉम्प्ट लिखने के सबसे सही तरीके

Gemini 3, रीज़निंग करने वाला मॉडल है. इससे प्रॉम्प्ट देने का तरीका बदल जाता है.

- **सटीक निर्देश:** अपने इनपुट प्रॉम्प्ट में कम शब्दों का इस्तेमाल करें. Gemini 3, सीधे और साफ़ तौर पर दिए गए निर्देशों का सबसे सही जवाब देता है. यह पुराने मॉडल के लिए इस्तेमाल की गई, ज़्यादा शब्दों वाली या बहुत ज़्यादा मुश्किल प्रॉम्प्ट इंजीनियरिंग तकनीकों का ज़्यादा विश्लेषण कर सकता है.
- **जवाब में शब्दों का इस्तेमाल:** डिफ़ॉल्ट रूप से, Gemini 3 कम शब्दों में जवाब देता है और सीधे तौर पर सटीक जवाब देने को प्राथमिकता देता है. अगर आपको अपने इस्तेमाल के उदाहरण के लिए, ज़्यादा बातचीत करने वाली या "चैटिंग" वाली पर्सोना की ज़रूरत है, तो आपको प्रॉम्प्ट में मॉडल को साफ़ तौर पर निर्देश देना होगा. उदाहरण के लिए, "इसे एक मददगार और बातचीत करने वाले दोस्त की तरह समझाओ".
- **कॉन्टेक्स्ट मैनेजमेंट:** बड़े डेटासेट (जैसे, पूरी किताबें, कोडबेस या लंबे वीडियो) के साथ काम करते समय, अपने खास निर्देश या सवाल प्रॉम्प्ट के आखिर में रखें. ऐसा डेटा के कॉन्टेक्स्ट के बाद करें. मॉडल के जवाब को दिए गए डेटा से जोड़ें. इसके लिए, अपने सवाल की शुरुआत "ऊपर दी गई जानकारी के आधार पर..." जैसे वाक्यांश से करें.

[प्रॉम्प्ट इंजीनियरिंग गाइड](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi) में, प्रॉम्प्ट डिज़ाइन करने की रणनीतियों के बारे में ज़्यादा जानें.

## अक्सर पूछे जाने वाले सवाल

1. **Gemini 3 के लिए, जानकारी अपडेट होने की आखिरी तारीख क्या है?** Gemini 3 मॉडल के लिए, जानकारी अपडेट होने की आखिरी तारीख जनवरी 2025 है. ज़्यादा नई जानकारी के लिए, [खोज के नतीजों से जानकारी पाने](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) वाले टूल का इस्तेमाल करें.
2. **कॉन्टेक्स्ट विंडो की सीमाएं क्या हैं?** Gemini 3 मॉडल, 10 लाख टोकन वाली कॉन्टेक्स्ट विंडो के साथ काम करते हैं. साथ ही, ये 64 हज़ार टोकन तक का आउटपुट दे सकते हैं.
3. **क्या Gemini 3 का इस्तेमाल बिना किसी शुल्क के किया जा सकता है?** Gemini API में Gemini 3 Flash `gemini-3-flash-preview` और 3.1 Flash-Lite `gemini-3.1-flash-lite` के मुफ़्त टियर उपलब्ध हैं. Google AI Studio में, Gemini 3.1 Pro और 3 Flash को बिना किसी शुल्क के आज़माया जा सकता है. हालांकि, Gemini API में `gemini-3.1-pro-preview` के लिए कोई भी मुफ़्त टियर उपलब्ध नहीं है.
4. **क्या मेरा पुराना `thinking_budget` कोड अब भी काम करेगा?** हां, `thinking_budget` अब भी पुराने सिस्टम के साथ काम करता है. हालांकि, हम आपको `thinking_level` पर माइग्रेट करने का सुझाव देते हैं, ताकि आपको बेहतर परफ़ॉर्मेंस मिल सके. एक ही अनुरोध में दोनों का इस्तेमाल न करें.
5. **क्या Gemini 3, Batch API के साथ काम करता है?** हां, Gemini 3, [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi) के साथ काम करता है.
6. **क्या कॉन्टेक्स्ट को कैश मेमोरी में सेव करने की सुविधा काम करती है?** हां, Gemini 3 के लिए [कॉन्टेक्स्ट कैश मेमोरी](https://ai.google.dev/gemini-api/docs/caching?hl=hi) की सुविधा उपलब्ध है.
7. **Gemini 3 में कौनसे टूल इस्तेमाल किए जा सकते हैं?** Gemini 3, [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), [Google Maps के साथ ग्राउंडिंग](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi), [फ़ाइल खोजने की सुविधा](https://ai.google.dev/gemini-api/docs/file-search?hl=hi),
   [कोड एक्ज़ीक्यूट करने की सुविधा](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi), और [यूआरएल के कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) के साथ काम करता है. यह आपके कस्टम टूल के लिए, स्टैंडर्ड [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) की सुविधा भी देता है. साथ ही, [पहले से मौजूद टूल के साथ मिलकर काम करता है](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi).
8. **`gemini-3.1-pro-preview-customtools` क्या है?** अगर `gemini-3.1-pro-preview` का इस्तेमाल किया जा रहा है और मॉडल, बैश कमांड के लिए आपके कस्टम टूल को अनदेखा कर रहा है, तो `gemini-3.1-pro-preview-customtools` मॉडल का इस्तेमाल करके देखें. ज़्यादा जानकारी के लिए [यहां](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi#gemini-31-pro-preview-customtools) जाएं.

## अगले चरण

- [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=hi#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D) का इस्तेमाल शुरू करना
- [सोचने के लेवल](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=hi#gemini3) और थिंकिंग बजट से सोचने के लेवल पर माइग्रेट करने के तरीके के बारे में जानने के लिए, Cookbook की गाइड देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
