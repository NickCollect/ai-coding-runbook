---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi
fetched_at: 2026-08-24T02:30:01.709873+00:00
title: "\u092a\u094d\u0930\u093e\u0925\u092e\u093f\u0915\u0924\u093e \u0915\u0947 \u0906\u0927\u093e\u0930 \u092a\u0930 \u0905\u0928\u0941\u092e\u093e\u0928 \u0932\u0917\u093e\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# प्राथमिकता के आधार पर अनुमान लगाना

ब्यौरा: Interactions API में Priority inference tier की मदद से, लेटेन्सी को ऑप्टिमाइज़ करने का तरीका जानें

Gemini Priority API, अनुमान लगाने के लिए प्रीमियम टियर है. इसे कारोबार के लिए ज़रूरी वर्कलोड के लिए डिज़ाइन किया गया है. इसके लिए, कम इंतज़ार का समय और सबसे ज़्यादा भरोसेमंद नतीजे पाने की ज़रूरत होती है. इसके लिए, प्रीमियम कीमत चुकानी पड़ती है. प्रायोरिटी टियर के ट्रैफ़िक को स्टैंडर्ड एपीआई और फ़्लेक्स टियर के ट्रैफ़िक से ज़्यादा प्राथमिकता दी जाती है.

प्राथमिकता के आधार पर अनुमान लगाने की सुविधा, Interactions API के सभी एंडपॉइंट पर उपलब्ध है.

## 'प्राथमिकता' फ़ील्ड का इस्तेमाल करने का तरीका

प्राथमिकता वाले टियर का इस्तेमाल करने के लिए, अपने अनुरोध में `service_tier` फ़ील्ड को `priority` पर सेट करें. अगर फ़ील्ड मौजूद नहीं है, तो डिफ़ॉल्ट टियर स्टैंडर्ड होता है.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## प्राथमिकता का अनुमान लगाने की सुविधा कैसे काम करती है

प्राथमिकता के आधार पर अनुमान लगाने की सुविधा, अनुरोधों को कंप्यूटिंग की ज़्यादा ज़रूरी कतारों पर भेजती है. इससे, लोगों के इस्तेमाल वाले ऐप्लिकेशन के लिए अनुमान लगाने की सुविधा, भरोसेमंद और तेज़ी से काम करती है. इसका मुख्य तरीका यह है कि अगर ट्रैफ़िक, डाइनैमिक सीमाओं से ज़्यादा हो जाता है, तो सर्वर साइड से स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड कर दिया जाता है. इससे अनुरोध को पूरा न करने के बजाय, ऐप्लिकेशन को स्थिर रखा जाता है.

| सुविधा | प्राथमिकता | स्टैंडर्ड | Flex | बैच |
| --- | --- | --- | --- | --- |
| **कीमत** | स्टैंडर्ड वर्शन की तुलना में 75 से 100% ज़्यादा | फ़ुल टिकट | 50% की छूट | 50% की छूट |
| **लेटेंसी** | सेकंड | सेकंड से मिनट | मिनट (1–15 मिनट का टारगेट) | 24 घंटे तक |
| **भरोसेमंद होना** | ज़्यादा (न झड़ने वाले) | ज़्यादा / सामान्य से ज़्यादा | बेस्ट-एफ़र्ट (शेड किया जा सकता है) | ज़्यादा (थ्रूपुट के लिए) |
| **इंटरफ़ेस** | सिंक्रोनस | सिंक्रोनस | सिंक्रोनस | एसिंक्रोनस |

### मुख्य फ़ायदे

- **कम समय में जवाब मिलना**: इसे इंटरैक्टिव और उपयोगकर्ता के लिए उपलब्ध एआई टूल के लिए डिज़ाइन किया गया है. इससे कुछ ही सेकंड में जवाब मिल जाता है.
- **ज़्यादा भरोसेमंद**: ट्रैफ़िक को सबसे ज़्यादा प्राथमिकता दी जाती है और इसे किसी भी हाल में कम नहीं किया जा सकता.
- **ग्रेजुअल डिग्रेडेशन**: डाइनैमिक सीमाओं से ज़्यादा ट्रैफ़िक बढ़ने पर, उसे प्रोसेस करने के लिए स्टैंडर्ड टियर पर अपने-आप डाउनग्रेड कर दिया जाता है. इससे सेवा में रुकावट नहीं आती.
- **कम रुकावट**: यह स्टैंडर्ड और फ़्लेक्स टियर की तरह ही, सिंक्रोनस `create` तरीके का इस्तेमाल करता है.

### उपयोग के उदाहरण

प्रायॉरिटी प्रोसेसिंग, कारोबार के लिए ज़रूरी उन वर्कफ़्लो के लिए सबसे सही है जहां परफ़ॉर्मेंस और भरोसेमंद होना सबसे ज़रूरी है.

- **इंटरैक्टिव एआई ऐप्लिकेशन**: ग्राहक सेवा के लिए चैटबॉट और कोपायलट. इनमें उपयोगकर्ता प्रीमियम चुकाते हैं और उन्हें तेज़ और सटीक जवाब मिलने की उम्मीद होती है.
- **रीयल-टाइम में फ़ैसले लेने वाले इंजन**: ऐसे सिस्टम जिनके लिए भरोसेमंद और कम समय में नतीजे पाना ज़रूरी होता है. जैसे, लाइव टिकट की प्राथमिकता तय करना या धोखाधड़ी का पता लगाना.
- **पैसे चुकाकर इस्तेमाल की जाने वाली सुविधाओं के लिए, प्रीमियम ग्राहक**: ऐसे डेवलपर जिन्हें पैसे चुकाकर इस्तेमाल की जाने वाली सुविधाओं के लिए, सेवा स्तर के ज़्यादा लक्ष्यों (एसएलओ) की गारंटी देनी होती है.

### तय सीमाएं

प्रायोरिटी के साथ इस्तेमाल करने पर, दर से जुड़ी अपनी सीमाएं लागू होती हैं. भले ही, इस्तेमाल को [इंटरैक्टिव ट्रैफ़िक की दर से जुड़ी कुल सीमाओं](https://aistudio.google.com/rate-limit?hl=hi) में गिना जाता हो. प्राथमिकता का अनुमान लगाने के लिए, दर की डिफ़ॉल्ट सीमाएं **मॉडल / टियर के लिए, दर की स्टैंडर्ड सीमा का 0.3 गुना** होती हैं

### ग्रेसफ़ुल डाउनग्रेड लॉजिक

अगर नेटवर्क में ज़्यादा ट्रैफ़िक होने की वजह से, प्राथमिकता वाले अनुरोधों की सीमाएं पार हो जाती हैं, तो ज़्यादा अनुरोधों को 503 या 429 गड़बड़ी के साथ फ़ेल करने के बजाय, **अपने-आप और आसानी से** स्टैंडर्ड प्रोसेसिंग पर डाउनग्रेड कर दिया जाता है. डाउनग्रेड किए गए अनुरोधों के लिए, स्टैंडर्ड दर के हिसाब से बिल भेजा जाता है. इसके लिए, Priority प्रीमियम दर लागू नहीं होती.

### क्लाइंट की ज़िम्मेदारी

- **जवाब की निगरानी करना**: डेवलपर को एपीआई के जवाब में `x-gemini-service-tier`
  हेडर की निगरानी करनी चाहिए, ताकि यह पता लगाया जा सके कि अनुरोधों को बार-बार `standard` पर डाउनग्रेड किया जा रहा है या नहीं.
- **फिर से कोशिश करना**: क्लाइंट को स्टैंडर्ड गड़बड़ियों के लिए, फिर से कोशिश करने का लॉजिक/एक्सपोनेंशियल बैकऑफ़ लागू करना होगा. जैसे, `DEADLINE_EXCEEDED`.

## कीमत

प्राथमिकता के आधार पर अनुमान लगाने की सुविधा के लिए, [स्टैंडर्ड एपीआई](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) की तुलना में 75 से 100% ज़्यादा शुल्क लिया जाता है. साथ ही, इसके लिए टोकन के हिसाब से बिल भेजा जाता है.

## इन मॉडल के साथ काम करता है

इन मॉडल में, प्राथमिकता के आधार पर अनुमान लगाने की सुविधा काम करती है:

| मॉडल | प्राथमिकता के आधार पर अनुमान लगाना |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## आगे क्या करना है

- लागत कम करने के लिए, [फ़्लेक्स इन्फ़रेंस](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi) का इस्तेमाल करें.
- [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi): टोकन के बारे में जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
