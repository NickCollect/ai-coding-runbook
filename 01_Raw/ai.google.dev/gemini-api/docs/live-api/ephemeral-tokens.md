---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=hi
fetched_at: 2026-06-22T06:30:39.554191+00:00
title: "\u0907\u092b\u093c\u0947\u092e\u0930\u0932 \u091f\u094b\u0915\u0928 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# इफ़ेमरल टोकन

Ephemeral token, [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) के ज़रिए Gemini
API को ऐक्सेस करने के लिए, कम समय के लिए मान्य होने वाले पुष्टि करने वाले टोकन होते हैं. इन्हें सुरक्षा को बेहतर बनाने के लिए डिज़ाइन किया गया है. इनका इस्तेमाल, उपयोगकर्ता के डिवाइस से सीधे एपीआई से कनेक्ट करने पर किया जाता है. इसे
[क्लाइंट-टू-सर्वर](https://ai.google.dev/gemini-api/docs/live?hl=hi#implementation-approach)
के तौर पर लागू किया जाता है. मानक एपीआई पासकोड की तरह, Ephemeral token को क्लाइंट-साइड ऐप्लिकेशन से निकाला जा सकता है. जैसे, वेब ब्राउज़र या मोबाइल ऐप्लिकेशन. हालांकि, Ephemeral token की समयसीमा तेज़ी से खत्म हो जाती है और इन पर पाबंदियां लगाई जा सकती हैं. इसलिए, प्रोडक्शन एनवायरमेंट में सुरक्षा से जुड़े जोखिम काफ़ी कम हो जाते हैं. एपीआई पासकोड की सुरक्षा को बेहतर बनाने के लिए, क्लाइंट-साइड ऐप्लिकेशन से सीधे Live API को ऐक्सेस करते समय, इनका इस्तेमाल करना चाहिए.

## Ephemeral token कैसे काम करते हैं

Ephemeral token, मोटे तौर पर इस तरह काम करते हैं:

1. आपका क्लाइंट (जैसे, वेब ऐप्लिकेशन) आपके बैकएंड से पुष्टि करता है.
2. आपका बैकएंड, Gemini API की प्रोविज़निंग सेवा से Ephemeral token का अनुरोध करता है.
3. Gemini API, कम समय के लिए मान्य होने वाला टोकन जारी करता है.
4. आपका बैकएंड, Live API से WebSocket कनेक्शन के लिए, टोकन को क्लाइंट को भेजता है. इसके लिए, एपीआई पासकोड को Ephemeral token से बदला जा सकता है.
5. इसके बाद, क्लाइंट टोकन का इस्तेमाल, एपीआई पासकोड की तरह करता है.

![अस्थायी टोकन के बारे में खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=hi)

इससे सुरक्षा बेहतर होती है, क्योंकि टोकन को निकालने पर भी, वह कम समय के लिए मान्य होता है. वहीं, क्लाइंट-साइड पर डिप्लॉय किया गया एपीआई पासकोड, लंबे समय के लिए मान्य होता है. क्लाइंट, Gemini को सीधे डेटा भेजता है. इसलिए, इससे लेटेंसी भी बेहतर होती है. साथ ही, आपके बैकएंड को रीयल टाइम डेटा को प्रॉक्सी करने की ज़रूरत नहीं पड़ती.

## कोई Ephemeral token बनाना

Gemini से Ephemeral token पाने का एक आसान उदाहरण यहां दिया गया है.
डिफ़ॉल्ट रूप से, आपके पास इस अनुरोध (`newSessionExpireTime`) से मिले टोकन का इस्तेमाल करके, Live API के नए सेशन शुरू करने के लिए एक मिनट और उस कनेक्शन पर मैसेज भेजने के लिए 30 मिनट (`expireTime`) होंगे.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

`expireTime` की वैल्यू की सीमाओं, डिफ़ॉल्ट वैल्यू, और अन्य फ़ील्ड की खास जानकारी के लिए, [एपीआई का संदर्भ](https://ai.google.dev/api/live?hl=hi#ephemeral-auth-tokens) देखें.
`expireTime` की समयसीमा के अंदर, आपको
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=hi#session-resumption) हर 10 मिनट में कॉल को फिर से कनेक्ट करने के लिए
की ज़रूरत होगी. ऐसा, एक ही टोकन से किया जा सकता है. भले ही,
`uses: 1` हो.

किसी Ephemeral token को कॉन्फ़िगरेशन के सेट के लिए लॉक भी किया जा सकता है. यह आपके ऐप्लिकेशन की सुरक्षा को और बेहतर बनाने और सर्वर साइड पर अपने सिस्टम के निर्देशों को बनाए रखने में मददगार हो सकता है.

### Python

```
from google import genai

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

फ़ील्ड के सबसेट को भी लॉक किया जा सकता है. ज़्यादा जानकारी के लिए, [SDK टूल का दस्तावेज़](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
देखें.

## किसी Ephemeral token की मदद से, Live API से कनेक्ट करना

Ephemeral token मिलने के बाद, इसका इस्तेमाल एपीआई पासकोड की तरह किया जाता है. हालांकि, ध्यान रखें कि यह सिर्फ़ Live API के लिए काम करता है. साथ ही, यह एपीआई के `v1alpha` वर्शन के साथ ही काम करता है.

Ephemeral token का इस्तेमाल, सिर्फ़ उन ऐप्लिकेशन को डिप्लॉय करने पर किया जाता है
जो [क्लाइंट-टू-सर्वर के तौर पर लागू करने के तरीके](https://ai.google.dev/gemini-api/docs/live?hl=hi#implementation-approach) का पालन करते हैं.

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

ज़्यादा उदाहरणों के लिए, [Live API का इस्तेमाल शुरू करना](https://ai.google.dev/gemini-api/docs/live?hl=hi) लेख पढ़ें.

## सबसे सही तरीके

- `expire_time` पैरामीटर का इस्तेमाल करके, समयसीमा खत्म होने की अवधि कम सेट करें.
- टोकन की समयसीमा खत्म हो जाती है. इसलिए, प्रोविज़निंग की प्रोसेस को फिर से शुरू करना पड़ता है.
- अपने बैकएंड के लिए, सुरक्षित पुष्टि की सुविधा की पुष्टि करें. Ephemeral token की सुरक्षा, आपके बैकएंड की पुष्टि करने के तरीके जितनी ही होगी.
- आम तौर पर, बैकएंड-टू-Gemini कनेक्शन के लिए, Ephemeral token का इस्तेमाल न करें, क्योंकि इस पाथ को आम तौर पर सुरक्षित माना जाता है.

## सीमाएं

फ़िलहाल, Ephemeral token सिर्फ़ [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) के साथ काम करते हैं.

## आगे क्या करना है

- ज़्यादा जानकारी के लिए, Ephemeral token के बारे में Live API के [रेफ़रंस](https://ai.google.dev/api/live?hl=hi#ephemeral-auth-tokens)
  को पढ़ें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-12 (UTC) को अपडेट किया गया."],[],[]]
