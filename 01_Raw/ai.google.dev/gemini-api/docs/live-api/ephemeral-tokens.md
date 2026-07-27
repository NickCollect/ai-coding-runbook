---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=hi
fetched_at: 2026-07-27T04:42:03.464244+00:00
title: "\u0907\u092b\u093c\u0947\u092e\u0930\u0932 \u091f\u094b\u0915\u0928 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# इफ़ेमरल टोकन

Ephemeral token, कम समय के लिए मान्य होने वाले ऐसे टोकन होते हैं जिनकी मदद से [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) के ज़रिए Gemini
API को ऐक्सेस किया जा सकता है. इन्हें, सुरक्षा को बेहतर बनाने के लिए डिज़ाइन किया गया है. इनका इस्तेमाल, उपयोगकर्ता के डिवाइस से सीधे एपीआई से कनेक्ट करने पर किया जाता है. इसे
[क्लाइंट-टू-सर्वर](https://ai.google.dev/gemini-api/docs/live?hl=hi#implementation-approach)
लागू करने का तरीका कहा जाता है. मानक एपीआई पासकोड की तरह, ephemeral token को क्लाइंट-साइड ऐप्लिकेशन से निकाला जा सकता है. जैसे, वेब ब्राउज़र या मोबाइल ऐप्लिकेशन. हालांकि, ephemeral token की समयसीमा बहुत कम होती है और इन पर पाबंदियां लगाई जा सकती हैं. इसलिए, प्रोडक्शन एनवायरमेंट में सुरक्षा से जुड़े जोखिम काफ़ी कम हो जाते हैं. लाइव एपीआई को क्लाइंट-साइड ऐप्लिकेशन से सीधे ऐक्सेस करते समय, इनका इस्तेमाल करना चाहिए. इससे एपीआई पासकोड की सुरक्षा बेहतर होती है.

## Ephemeral token कैसे काम करते हैं

यहां, ephemeral token के काम करने का तरीका बताया गया है:

1. आपका क्लाइंट (जैसे, वेब ऐप्लिकेशन) आपके बैकएंड से पुष्टि करता है.
2. आपका बैकएंड, Gemini API की प्रोविज़निंग सेवा से ephemeral token का अनुरोध करता है.
3. Gemini API, कम समय के लिए मान्य होने वाला टोकन जारी करता है.
4. आपका बैकएंड, लाइव एपीआई से WebSocket कनेक्शन के लिए, क्लाइंट को टोकन भेजता है. इसके लिए, एपीआई पासकोड को ephemeral token से बदला जा सकता है.
5. इसके बाद, क्लाइंट इस टोकन का इस्तेमाल, एपीआई पासकोड की तरह करता है.

![कुछ समय के लिए इस्तेमाल किए जाने वाले टोकन के बारे में खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=hi)

इससे सुरक्षा बेहतर होती है, क्योंकि टोकन को निकालने पर भी, यह कम समय के लिए मान्य होता है. वहीं, क्लाइंट-साइड पर डिप्लॉय किया गया एपीआई पासकोड, लंबे समय के लिए मान्य होता है. क्लाइंट, Gemini को सीधे डेटा भेजता है. इसलिए, इससे लेटेंसी भी बेहतर होती है. साथ ही, आपके बैकएंड को रीयल टाइम डेटा को प्रॉक्सी करने की ज़रूरत नहीं पड़ती.

## Ephemeral token बनाना

यहां, Gemini से ephemeral token पाने का एक आसान उदाहरण दिया गया है.
डिफ़ॉल्ट रूप से, आपके पास इस अनुरोध (`newSessionExpireTime`) से मिले टोकन का इस्तेमाल करके, लाइव एपीआई के नए सेशन शुरू करने के लिए एक मिनट और उस कनेक्शन पर मैसेज भेजने के लिए 30 मिनट (`expireTime`) होंगे.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
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
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

`expireTime` की वैल्यू की सीमाओं, डिफ़ॉल्ट वैल्यू, और अन्य फ़ील्ड की खास जानकारी के लिए, [एपीआई का संदर्भ](https://ai.google.dev/api/live?hl=hi#ephemeral-auth-tokens) देखें.
`expireTime` की समयसीमा के अंदर, आपको
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=hi#session-resumption) हर 10 मिनट में कॉल को फिर से कनेक्ट करने के लिए
की ज़रूरत होगी. ऐसा, उसी टोकन से किया जा सकता है, भले ही
`uses: 1` हो.

किसी खास कॉन्फ़िगरेशन के लिए, ephemeral token को लॉक भी किया जा सकता है. यह आपके ऐप्लिकेशन की सुरक्षा को बेहतर बनाने और सर्वर साइड पर अपने सिस्टम के निर्देशों को बनाए रखने में मददगार हो सकता है.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
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
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
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
      "model": "models/gemini-3.1-flash-live-preview",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

फ़ील्ड के सबसेट को भी लॉक किया जा सकता है. ज़्यादा जानकारी के लिए, [SDK टूल का दस्तावेज़](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
देखें.

## Ephemeral token की मदद से, लाइव एपीआई से कनेक्ट करना

Ephemeral token मिलने के बाद, इसका इस्तेमाल एपीआई पासकोड की तरह किया जा सकता है. हालांकि, ध्यान रखें कि यह सिर्फ़ लाइव एपीआई के लिए काम करता है. साथ ही, यह एपीआई के `v1beta` वर्शन के साथ ही काम करता है.

[क्लाइंट-टू-सर्वर लागू करने के तरीके का इस्तेमाल करने वाले ऐप्लिकेशन
को डिप्लॉय करने पर ही, ephemeral token का इस्तेमाल करने से फ़ायदा मिलता है.](https://ai.google.dev/gemini-api/docs/live?hl=hi#implementation-approach)

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

ज़्यादा उदाहरणों के लिए, [लाइव एपीआई का इस्तेमाल शुरू करना](https://ai.google.dev/gemini-api/docs/live?hl=hi) लेख पढ़ें.

## सबसे सही तरीके

- `expire_time` पैरामीटर का इस्तेमाल करके, समयसीमा कम सेट करें.
- टोकन की समयसीमा खत्म हो जाती है. इसलिए, प्रोविज़निंग की प्रोसेस को फिर से शुरू करना पड़ता है.
- अपने बैकएंड के लिए, सुरक्षित पुष्टि की सुविधा की पुष्टि करें. Ephemeral token की सुरक्षा, आपके बैकएंड की पुष्टि करने के तरीके जितनी ही होगी.
- आम तौर पर, बैकएंड-टू-Gemini कनेक्शन के लिए, ephemeral token का इस्तेमाल न करें. ऐसा इसलिए, क्योंकि इस पाथ को आम तौर पर सुरक्षित माना जाता है.

## सीमाएं

फ़िलहाल, ephemeral token सिर्फ़ [लाइव एपीआई](https://ai.google.dev/gemini-api/docs/live?hl=hi) के साथ काम करते हैं.

## आगे क्या करना है

- ज़्यादा जानकारी के लिए, ephemeral token के बारे में लाइव एपीआई के [रेफ़रंस](https://ai.google.dev/api/live?hl=hi#ephemeral-auth-tokens)
  पढ़ें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया."],[],[]]
