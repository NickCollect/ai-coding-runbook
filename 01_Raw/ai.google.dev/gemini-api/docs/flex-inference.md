---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi
fetched_at: 2026-08-17T02:26:52.522110+00:00
title: "Flex inference \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Flex inference

Gemini Flex API, अनुमान लगाने वाला टियर है. यह स्टैंडर्ड दरों की तुलना में 50% कम कीमत पर उपलब्ध है. हालांकि, इसमें जवाब मिलने में लगने वाला समय अलग-अलग हो सकता है और यह सबसे अच्छी उपलब्धता के साथ काम करता है. इसे ऐसे वर्कलोड के लिए डिज़ाइन किया गया है जिनमें इंतज़ार का समय कम होता है. साथ ही, जिनमें सिंक्रोनस प्रोसेसिंग की ज़रूरत होती है, लेकिन स्टैंडर्ड एपीआई की रीयल-टाइम परफ़ॉर्मेंस की ज़रूरत नहीं होती.

## Flex का इस्तेमाल कैसे करें

Flex टियर का इस्तेमाल करने के लिए, अपने अनुरोध में `service_tier` को `flex` के तौर पर सेट करें. इस फ़ील्ड को शामिल न करने पर, अनुरोधों के लिए डिफ़ॉल्ट रूप से स्टैंडर्ड टियर का इस्तेमाल किया जाता है.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.6-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
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
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## फ़्लेक्स इन्फ़रेंस कैसे काम करता है

Gemini Flex inference, स्टैंडर्ड एपीआई और [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi) के 24 घंटे के टर्नअराउंड के बीच के अंतर को कम करता है. यह ऑफ़-पीक समय में, "शेड की जा सकने वाली" कंप्यूट क्षमता का इस्तेमाल करता है. इससे बैकग्राउंड टास्क और क्रमवार वर्कफ़्लो के लिए, कम लागत वाला समाधान मिलता है.

| सुविधा | Flex | प्राथमिकता | स्टैंडर्ड | बैच |
| --- | --- | --- | --- | --- |
| **कीमत** | 50% की छूट | स्टैंडर्ड वर्शन की तुलना में 75 से 100% ज़्यादा | फ़ुल टिकट | 50% की छूट |
| **लेटेंसी** | मिनट (1–15 मिनट का टारगेट) | कम (सेकंड) | सेकंड से मिनट | 24 घंटे तक |
| **भरोसेमंद होना** | बेस्ट-एफ़र्ट (शेड किया जा सकता है) | ज़्यादा (न झड़ने वाले) | ज़्यादा / सामान्य से ज़्यादा | ज़्यादा (थ्रूपुट के लिए) |
| **इंटरफ़ेस** | सिंक्रोनस | सिंक्रोनस | सिंक्रोनस | एसिंक्रोनस |

### मुख्य फ़ायदे

- **लागत कम होना**: इससे नॉन-प्रोडक्शन इवैल, बैकग्राउंड एजेंट, और डेटा को बेहतर बनाने में काफ़ी बचत होती है.
- **आसानी से लागू करना**: अपने मौजूदा अनुरोधों में बस एक पैरामीटर जोड़ें.
- **सिंक्रोनस वर्कफ़्लो**: यह क्रम से एपीआई चेन के लिए सबसे सही है. इसमें अगला अनुरोध, पिछले अनुरोध के आउटपुट पर निर्भर करता है. इसलिए, यह एजेंटिक वर्कफ़्लो के लिए बैच से ज़्यादा फ़्लेक्सिबल होता है.

### उपयोग के उदाहरण

- **ऑफ़लाइन आकलन**: "एलएलएम-एज़-अ-जज" रिग्रेशन टेस्ट या लीडरबोर्ड चलाना.
- **बैकग्राउंड एजेंट**: ऐसे टास्क जो क्रम से पूरे होते हैं. जैसे, सीआरएम अपडेट, प्रोफ़ाइल बनाना या कॉन्टेंट मॉडरेशन. इनमें कुछ मिनट की देरी स्वीकार की जा सकती है.
- **बजट की सीमा वाली रिसर्च**: ऐसे शैक्षणिक एक्सपेरिमेंट जिनके लिए सीमित बजट में ज़्यादा टोकन की ज़रूरत होती है.

### तय सीमाएं

फ़्लेक्स इन्फ़रेंस के ट्रैफ़िक को, [दर से जुड़ी सामान्य सीमाओं](https://aistudio.google.com/rate-limit?hl=hi) में गिना जाता है. इसमें [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi) की तरह, दर से जुड़ी ज़्यादा सीमाएं नहीं मिलती हैं.

### कम की जा सकने वाली क्षमता

फ़्लेक्स ट्रैफ़िक को कम प्राथमिकता दी जाती है. अगर स्टैंडर्ड ट्रैफ़िक में अचानक बढ़ोतरी होती है, तो हो सकता है कि Flex के अनुरोधों को पहले से ही रोक दिया जाए या उन्हें हटा दिया जाए. ऐसा इसलिए किया जाता है, ताकि ज़्यादा प्राथमिकता वाले उपयोगकर्ताओं के लिए क्षमता बनी रहे. अगर आपको प्राथमिकता के आधार पर अनुमान लगाने की सुविधा चाहिए, तो [प्राथमिकता के आधार पर अनुमान लगाने की सुविधा](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi) देखें

### गड़बड़ी के कोड

जब फ़्लेक्स क्षमता उपलब्ध नहीं होती है या सिस्टम पर ज़्यादा लोड होता है, तो एपीआई गड़बड़ी के स्टैंडर्ड कोड दिखाएगा:

- **503 कोड वाली गड़बड़ी: सेवा उपलब्ध नहीं है**: इस्तेमाल करने की मौजूदा सीमा पूरी हो गई है.
- **429 कई बार अनुरोध किया गया**: अनुरोधों की संख्या तय सीमा से ज़्यादा हो गई है या संसाधन खत्म हो गया है.

### क्लाइंट की ज़िम्मेदारी

- **सर्वर साइड से फ़ॉलबैक नहीं होता**: अचानक लगने वाले शुल्क से बचने के लिए, अगर Flex की क्षमता पूरी हो जाती है, तो सिस्टम Flex के अनुरोध को स्टैंडर्ड टियर में अपने-आप अपग्रेड नहीं करेगा.
- **फिर से कोशिश करना**: आपको क्लाइंट-साइड पर, फिर से कोशिश करने का अपना लॉजिक लागू करना होगा. इसके लिए, एक्स्पोनेंशियल बैकऑफ़ का इस्तेमाल करें.
- **टाइमआउट**: फ़्लेक्स अनुरोधों को कतार में रखा जा सकता है. इसलिए, हम क्लाइंट-साइड टाइमआउट को 10 मिनट या उससे ज़्यादा बढ़ाने का सुझाव देते हैं, ताकि कनेक्शन समय से पहले बंद न हो.

## टाइम आउट विंडो में बदलाव करना

REST API और क्लाइंट लाइब्रेरी के लिए, हर अनुरोध के हिसाब से टाइमआउट कॉन्फ़िगर किए जा सकते हैं.
हमेशा पक्का करें कि क्लाइंट-साइड टाइमआउट, सर्वर के लिए तय की गई इंतज़ार की अवधि के बराबर हो. उदाहरण के लिए, फ़्लेक्स वेटिंग लाइन के लिए 600 सेकंड से ज़्यादा. एसडीके, टाइम आउट की वैल्यू मिलीसेकंड में लेते हैं.

### हर अनुरोध के लिए समयसीमाएं

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## फिर से कोशिश करने की सुविधा लागू करना

Flex को बंद किया जा सकता है और इसमें 503 गड़बड़ियां होती हैं. इसलिए, यहां उन अनुरोधों को जारी रखने के लिए फिर से कोशिश करने के लॉजिक को लागू करने का एक उदाहरण दिया गया है जिन्हें पूरा नहीं किया जा सका:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.6-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.6-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.6-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## कीमत

फ़्लेक्स इन्फ़रेंस की कीमत, [स्टैंडर्ड एपीआई](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) की कीमत का 50% होती है. इसका बिल हर टोकन के हिसाब से भेजा जाता है.

## इन मॉडल के साथ काम करता है

इन मॉडल के साथ फ़्लेक्स इन्फ़रेंस की सुविधा काम करती है:

| मॉडल | Flex inference |
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

- इंतज़ार का समय बहुत कम रखने से जुड़ी सेटिंग के लिए, [प्राथमिकता के आधार पर अनुमान लगाना](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi).
- [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi): टोकन के बारे में जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
