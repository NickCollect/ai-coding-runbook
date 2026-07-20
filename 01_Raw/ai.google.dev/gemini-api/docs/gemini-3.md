---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=hi
fetched_at: 2026-07-20T04:32:56.744769+00:00
title: "Gemini 3 \u0915\u0940 \u0921\u0947\u0935\u0932\u092a\u0930 \u0917\u093e\u0907\u0921 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)

सुझाव भेजें

# Gemini 3 की डेवलपर गाइड

Gemini 3, अब तक का हमारा सबसे ऐडवांस मॉडल है. इसे बेहतरीन रीज़निंग के आधार पर बनाया गया है. इसे इस तरह से डिज़ाइन किया गया है कि यह किसी भी आइडिया को हकीकत में बदल सकता है. इसके लिए, यह एजेंटिक वर्कफ़्लो, अपने-आप होने वाली कोडिंग, और मुश्किल मल्टीमॉडल टास्क में महारत हासिल करता है.
इस गाइड में, Gemini 3 मॉडल फ़ैमिली की मुख्य सुविधाओं के बारे में बताया गया है. साथ ही, इसका ज़्यादा से ज़्यादा फ़ायदा पाने का तरीका भी बताया गया है.

[Gemini 3 की सुविधा वाले ऐप्लिकेशन के हमारे कलेक्शन](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=hi) को एक्सप्लोर करें. इससे आपको यह पता चलेगा कि यह मॉडल, ऐडवांस रीज़निंग, ऑटोनॉमस कोडिंग, और मुश्किल मल्टीमॉडल टास्क को कैसे हैंडल करता है.

कोड की कुछ लाइनों के साथ शुरू करें:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## पेश है Gemini 3 सीरीज़

Gemini 3.1 Pro, मुश्किल कामों के लिए सबसे अच्छा है. इसके लिए, दुनिया के बारे में ज़्यादा जानकारी और अलग-अलग मोड में ऐडवांस रिज़निंग की ज़रूरत होती है.

Gemini 3 Flash, 3-सीरीज़ का हमारा नया मॉडल है. इसमें Pro-लेवल की इंटेलिजेंस की सुविधा मिलती है. साथ ही, यह Flash की स्पीड और कीमत में उपलब्ध है.

Nano Banana Pro (इसे Gemini 3 Pro Image भी कहा जाता है) इमेज जनरेट करने वाला हमारा सबसे बेहतरीन मॉडल है. वहीं, Nano Banana 2 (इसे Gemini 3.1 Flash Image भी कहा जाता है) इमेज जनरेट करने वाला ऐसा मॉडल है जो कम कीमत में, ज़्यादा इमेज जनरेट करता है और ज़्यादा असरदार तरीके से काम करता है.

Gemini 3.1 Flash-Lite, हमारा वर्कहॉर्स मॉडल है. इसे कम लागत में ज़्यादा काम करने के लिए बनाया गया है.

Gemini 3 के सभी मॉडल फ़िलहाल, झलक के तौर पर उपलब्ध हैं.

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

Gemini 3 में नए पैरामीटर जोड़े गए हैं. इनकी मदद से, डेवलपर को लेटेन्सी, लागत, और मल्टीमॉडल फ़िडेलिटी पर ज़्यादा कंट्रोल मिलता है.

### सोचने का लेवल

Gemini 3 सीरीज़ के मॉडल, डिफ़ॉल्ट रूप से डाइनैमिक थिंकिंग का इस्तेमाल करते हैं, ताकि वे प्रॉम्प्ट के बारे में सोच-समझकर जवाब दे सकें. `thinking_level` पैरामीटर का इस्तेमाल किया जा सकता है. यह पैरामीटर, जवाब देने से पहले मॉडल की इंटरनल रीज़निंग प्रोसेस की **ज़्यादा से ज़्यादा** डेप्थ को कंट्रोल करता है. Gemini 3, इन लेवल को टोकन की गारंटी के तौर पर नहीं, बल्कि सोचने के लिए उपलब्ध टोकन की संख्या के तौर पर मानता है.

अगर `thinking_level` के लिए कोई वैल्यू नहीं डाली गई है, तो Gemini 3 डिफ़ॉल्ट रूप से `high` पर सेट होगा. अगर आपको ऐसे जवाब चाहिए जिनमें कम समय लगता हो और जटिल तर्क की ज़रूरत न हो, तो मॉडल के सोचने के लेवल को `low` पर सेट करें.

| सोचने का लेवल | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | ब्यौरा |
| --- | --- | --- | --- | --- |
| **`minimal`** | काम नहीं करता है | काम करता है (डिफ़ॉल्ट) | काम करता है | ज़्यादातर क्वेरी के लिए, यह "सोचने की ज़रूरत नहीं है" सेटिंग से मेल खाती है. मुश्किल कोडिंग टास्क के लिए, मॉडल बहुत कम सोच-विचार कर सकता है. यह चैट या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए, इंतज़ार के समय को कम करता है. ध्यान दें कि `minimal` इस बात की गारंटी नहीं देता कि सोचने की सुविधा बंद हो गई है. |
| **`low`** | काम करता है | काम करता है | काम करता है | इससे इंतज़ार का समय और लागत कम हो जाती है. यह मॉडल, आसान निर्देशों का पालन करने, चैट करने या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए सबसे अच्छा है. |
| **`medium`** | काम करता है | काम करता है | काम करता है | ज़्यादातर कामों के लिए, सोच-समझकर जवाब देता है. |
| **`high`** | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | काम करता है (डाइनैमिक) | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | इससे जवाब में ज़्यादा से ज़्यादा जानकारी शामिल की जा सकती है. मॉडल को पहले (बिना सोचे-समझे) आउटपुट टोकन तक पहुंचने में ज़्यादा समय लग सकता है. हालांकि, आउटपुट पर ज़्यादा ध्यान से विचार किया जाएगा. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### तापमान

हमारा सुझाव है कि Gemini 3 के सभी मॉडल के लिए, तापमान पैरामीटर को डिफ़ॉल्ट वैल्यू `1.0` पर सेट रखें.

पिछले मॉडल में, क्रिएटिविटी और डिटरमिनिज़्म को कंट्रोल करने के लिए, अक्सर टेंपरेचर को ट्यून करने से फ़ायदा मिलता था. हालांकि, Gemini 3 की तर्क करने की क्षमताओं को डिफ़ॉल्ट सेटिंग के लिए ऑप्टिमाइज़ किया गया है. टेंपरेचर को बदलने (इसे 1.0 से कम पर सेट करने) से, मॉडल का व्यवहार अप्रत्याशित हो सकता है. जैसे, लूपिंग या परफ़ॉर्मेंस में गिरावट. ऐसा खास तौर पर, गणित या तर्क से जुड़े मुश्किल टास्क में होता है.

### सोच-समझकर किए गए हस्ताक्षर

Gemini 3 मॉडल, थॉट सिग्नेचर का इस्तेमाल करते हैं. इससे एपीआई कॉल के दौरान, जवाब देने के लिए सही कॉन्टेक्स्ट को बनाए रखने में मदद मिलती है. ये सिग्नेचर, मॉडल की इंटरनल थॉट प्रोसेस के एन्क्रिप्ट किए गए वर्शन होते हैं.

- **स्टेटफ़ुल मोड (सुझाया गया)**: स्टेटफ़ुल मोड में Interactions API का इस्तेमाल करते समय (`previous_interaction_id` उपलब्ध कराना), सर्वर बातचीत के इतिहास और थॉट सिग्नेचर को अपने-आप मैनेज करता है.
- **स्टेटलेस मोड**: अगर बातचीत के इतिहास को मैन्युअल तरीके से मैनेज किया जा रहा है, तो आपको अगले अनुरोधों में, थॉट ब्लॉक और उनके हस्ताक्षर शामिल करने होंगे, ताकि उनकी पुष्टि की जा सके.

ज़्यादा जानकारी के लिए, [थॉट सिग्नेचर](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) पेज देखें.`

### टूल के साथ स्ट्रक्चर्ड आउटपुट

Gemini 3 मॉडल की मदद से, [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) को बिल्ट-इन टूल के साथ जोड़ा जा सकता है. इनमें ये टूल शामिल हैं: [Google Search से जानकारी पाना](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), [यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi), [कोड एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi), और [फ़ंक्शन कॉल करना](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
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
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Image generation

Gemini 3.1 Flash Image और Gemini 3 Pro Image की मदद से, टेक्स्ट प्रॉम्प्ट से इमेज जनरेट की जा सकती हैं और उनमें बदलाव किया जा सकता है. यह किसी प्रॉम्प्ट के बारे में "सोचने" के लिए, तर्क का इस्तेमाल करता है. साथ ही, यह [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) से मिली जानकारी का इस्तेमाल करने से पहले, रीयल-टाइम डेटा को ऐक्सेस कर सकता है. जैसे, मौसम का पूर्वानुमान या स्टॉक चार्ट. इसके बाद, यह ज़्यादा सटीक इमेज जनरेट करता है.

**नई और बेहतर सुविधाएँ:**

- **4K और टेक्स्ट रेंडरिंग:** 2K और 4K रिज़ॉल्यूशन तक के टेक्स्ट और डायग्राम जनरेट करें, जो साफ़ हों और पढ़ने में आसान हों.
- **भरोसेमंद जानकारी के आधार पर कॉन्टेंट जनरेट करना:** `google_search` टूल का इस्तेमाल करके, तथ्यों की पुष्टि करें और असल दुनिया की जानकारी के आधार पर इमेज जनरेट करें. Google *इमेज* की मदद से जवाब में भरोसेमंद जानकारी शामिल करना
  Gemini 3.1 Flash Image के लिए उपलब्ध है.
- **बातचीत करके बदलाव करना:** सिर्फ़ बदलाव करने के लिए कहकर, इमेज में कई बार बदलाव करना. जैसे, "बैकग्राउंड को सूर्यास्त वाली इमेज में बदल दो". यह वर्कफ़्लो, बारी-बारी से बातचीत के दौरान विज़ुअल कॉन्टेक्स्ट को बनाए रखने के लिए, **सोच के आधार पर जवाब देने की सुविधा** पर निर्भर करता है.

आस्पेक्ट रेशियो, बदलाव करने के वर्कफ़्लो, और कॉन्फ़िगरेशन के विकल्पों के बारे में पूरी जानकारी के लिए, [इमेज जनरेट करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) देखें.

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
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
- **इमेज एनोटेशन:** मॉडल, इमेज पर सीधे तौर पर ऐरो, बाउंडिंग बॉक्स या अन्य एनोटेशन बना सकता है. इससे, वह जगह से जुड़े सवालों के जवाब दे सकता है. जैसे, "इस आइटम को कहां रखना चाहिए?".

विज़ुअल थिंकिंग की सुविधा चालू करने के लिए, [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) को टूल के तौर पर कॉन्फ़िगर करें. ज़रूरत पड़ने पर, मॉडल इमेज में बदलाव करने के लिए कोड का इस्तेमाल अपने-आप करेगा.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

इमेज के साथ कोड लागू करने के बारे में ज़्यादा जानकारी के लिए, [कोड लागू करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi#images) लेख पढ़ें.

### मल्टीमोडल फ़ंक्शन के जवाब

[मल्टीमॉडल फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#multimodal) की मदद से, उपयोगकर्ताओं को ऐसे फ़ंक्शन रिस्पॉन्स मिलते हैं जिनमें मल्टीमॉडल ऑब्जेक्ट शामिल होते हैं. इससे मॉडल की फ़ंक्शन कॉलिंग की सुविधाओं का बेहतर तरीके से इस्तेमाल किया जा सकता है. स्टैंडर्ड फ़ंक्शन कॉलिंग की सुविधा, सिर्फ़ टेक्स्ट पर आधारित फ़ंक्शन के जवाबों के साथ काम करती है:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
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

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### पहले से मौजूद टूल और फ़ंक्शन कॉलिंग को एक साथ इस्तेमाल करना

Gemini 3 की मदद से, एक ही एपीआई कॉल में बिल्ट-इन टूल (जैसे, Google Search, यूआरएल कॉन्टेक्स्ट, और [अन्य](https://ai.google.dev/gemini-api/docs/tools?hl=hi)) और कस्टम [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) टूल का इस्तेमाल किया जा सकता है. इससे ज़्यादा मुश्किल वर्कफ़्लो को मैनेज किया जा सकता है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Gemini 2.5 से माइग्रेट करना

Gemini 3, अब तक का हमारा सबसे ऐडवांस मॉडल है. यह Gemini 2.5 से ज़्यादा बेहतर है. माइग्रेट करते समय, इन बातों का ध्यान रखें:

- **सोच-समझकर जवाब देना:** अगर आपने Gemini 2.5 को सोच-समझकर जवाब देने के लिए, पहले मुश्किल प्रॉम्प्ट इंजीनियरिंग (जैसे, चेन ऑफ़ थॉट) का इस्तेमाल किया था, तो `thinking_level: "high"` और आसान प्रॉम्प्ट के साथ Gemini 3 को आज़माएँ.
- **तापमान की सेटिंग:** अगर आपके मौजूदा कोड में तापमान को साफ़ तौर पर सेट किया गया है (खास तौर पर, भरोसेमंद आउटपुट के लिए कम वैल्यू पर सेट किया गया है), तो हमारा सुझाव है कि इस पैरामीटर को हटा दें. साथ ही, Gemini 3 के डिफ़ॉल्ट तापमान 1.0 का इस्तेमाल करें. इससे, लूपिंग से जुड़ी संभावित समस्याओं से बचा जा सकेगा. साथ ही, मुश्किल टास्क में परफ़ॉर्मेंस में गिरावट नहीं आएगी.
- **पीडीएफ़ और दस्तावेज़ को समझना:**
  अगर आपने दस्तावेज़ को पार्स करने के लिए किसी खास तरीके का इस्तेमाल किया था, तो नई `media_resolution_high` सेटिंग को आज़माएं. इससे यह पक्का किया जा सकेगा कि आपको सटीक नतीजे मिलते रहें.
- **टोकन का इस्तेमाल:** Gemini 3 डिफ़ॉल्ट पर माइग्रेट करने से, PDF के लिए टोकन का इस्तेमाल **बढ़ सकता है**. हालांकि, वीडियो के लिए टोकन का इस्तेमाल **कम हो सकता है**. अगर डिफ़ॉल्ट रिज़ॉल्यूशन ज़्यादा होने की वजह से, अनुरोधों की संख्या अब कॉन्टेक्स्ट विंडो से ज़्यादा हो गई है, तो हमारा सुझाव है कि मीडिया रिज़ॉल्यूशन को साफ़ तौर पर कम करें.
- **इमेज सेगमेंटेशन:** इमेज सेगमेंटेशन की सुविधाएं, Gemini 3 Pro या Gemini 3 Flash में काम नहीं करती हैं. इमेज सेगमेंटेशन की मदद से, ऑब्जेक्ट के लिए पिक्सल-लेवल के मास्क दिखाए जाते हैं. जिन वर्कलोड के लिए इमेज सेगमेंटेशन की सुविधा की ज़रूरत होती है उनके लिए, हमारा सुझाव है कि आप सूझ-बूझ वाली सुविधा बंद करके Gemini 2.5 Flash या [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=hi) का इस्तेमाल जारी रखें.
- **कंप्यूटर का इस्तेमाल:** Gemini 3 Pro और Gemini 3 Flash, [कंप्यूटर के इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) की सुविधा के साथ काम करते हैं. 2.5 सीरीज़ के उलट, कंप्यूटर के इस्तेमाल से जुड़े सवालों को ऐक्सेस करने के लिए, आपको अलग मॉडल का इस्तेमाल करने की ज़रूरत नहीं है.
- **टूल के साथ काम करने की सुविधा**: [फ़ंक्शन कॉलिंग के साथ-साथ, पहले से मौजूद टूल का इस्तेमाल करने की सुविधा](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) अब Gemini 3 मॉडल के लिए उपलब्ध है. अब Gemini 3 मॉडल के लिए, [Maps से मिली जानकारी का इस्तेमाल करने की सुविधा](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi) भी उपलब्ध है.

## OpenAI के साथ काम करने की सुविधा

[OpenAI कंपैटबिलिटी लेयर](https://ai.google.dev/gemini-api/docs/openai?hl=hi) का इस्तेमाल करने वाले लोगों के लिए, स्टैंडर्ड पैरामीटर (OpenAI के `reasoning_effort`) अपने-आप Gemini (`thinking_level`) के बराबर मैप हो जाते हैं.

## प्रॉम्प्ट लिखने के सबसे सही तरीके

Gemini 3, रीज़निंग करने वाला मॉडल है. इससे प्रॉम्प्ट देने का तरीका बदल जाता है.

- **सटीक निर्देश:** अपने इनपुट प्रॉम्प्ट में कम शब्दों का इस्तेमाल करें. Gemini 3, सीधे और साफ़ तौर पर दिए गए निर्देशों का सबसे सही जवाब देता है. यह पुराने मॉडल के लिए इस्तेमाल की गई, ज़्यादा शब्दों वाली या बहुत ज़्यादा जटिल प्रॉम्प्ट इंजीनियरिंग तकनीकों का ज़्यादा विश्लेषण कर सकता है.
- **जवाब में शब्दों का इस्तेमाल:** डिफ़ॉल्ट रूप से, Gemini 3 कम शब्दों में जवाब देता है और सीधे तौर पर सटीक जवाब देने को प्राथमिकता देता है. अगर आपको अपने इस्तेमाल के उदाहरण के लिए, ज़्यादा बातचीत करने वाले या "चैटिंग" वाले पर्सोना की ज़रूरत है, तो आपको प्रॉम्प्ट में मॉडल को साफ़ तौर पर निर्देश देना होगा. उदाहरण के लिए, "इसे एक मददगार और बातचीत करने वाले दोस्त की तरह समझाओ".
- **कॉन्टेक्स्ट मैनेजमेंट:** बड़े डेटासेट (जैसे, पूरी किताबें, कोडबेस या लंबे वीडियो) के साथ काम करते समय, अपने खास निर्देश या सवाल, प्रॉम्प्ट के आखिर में रखें. ऐसा डेटा के कॉन्टेक्स्ट के बाद करें. मॉडल को दिए गए डेटा के आधार पर जवाब देने के लिए, अपने सवाल की शुरुआत इस तरह के वाक्यांश से करें, "ऊपर दी गई जानकारी के आधार पर...".

[प्रॉम्प्ट इंजीनियरिंग गाइड](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi) में, प्रॉम्प्ट डिज़ाइन करने की रणनीतियों के बारे में ज़्यादा जानें.

## अक्सर पूछे जाने वाले सवाल

1. **Gemini 3 के लिए, जानकारी अपडेट होने की आखिरी तारीख क्या है?** Gemini 3 मॉडल के लिए, जानकारी अपडेट होने की आखिरी तारीख जनवरी 2025 है. ज़्यादा नई जानकारी के लिए, [खोज के नतीजों से जानकारी पाने](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) वाले टूल का इस्तेमाल करें.
2. **कॉन्टेक्स्ट विंडो की सीमाएं क्या हैं?** Gemini 3 मॉडल, 10 लाख टोकन वाली कॉन्टेक्स्ट विंडो के साथ काम करते हैं. साथ ही, ये 64 हज़ार टोकन तक का आउटपुट दे सकते हैं.
3. **क्या Gemini 3 का इस्तेमाल बिना किसी शुल्क के किया जा सकता है?** Gemini 3 Flash
   `gemini-3-flash-preview`, Gemini API के मुफ़्त टियर में उपलब्ध है. Google AI Studio में, Gemini 3.1 Pro और 3 Flash को बिना किसी शुल्क के आज़माया जा सकता है. हालांकि, Gemini API में `gemini-3.1-pro-preview` के लिए कोई भी मुफ़्त टियर उपलब्ध नहीं है.
4. **क्या मेरा पुराना `thinking_budget` कोड अब भी काम करेगा?** हां, `thinking_budget` अब भी पुराने सिस्टम के साथ काम करता है. हालांकि, हम आपको `thinking_level` पर माइग्रेट करने का सुझाव देते हैं, ताकि आपको बेहतर परफ़ॉर्मेंस मिल सके. एक ही अनुरोध में दोनों का इस्तेमाल न करें.
5. **क्या Gemini 3, Batch API के साथ काम करता है?** हां, Gemini 3, [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi) के साथ काम करता है.
6. **क्या कॉन्टेक्स्ट को कैश मेमोरी में सेव करने की सुविधा काम करती है?** हां, Gemini 3 के लिए [कॉन्टेक्स्ट कैश मेमोरी](https://ai.google.dev/gemini-api/docs/caching?hl=hi) की सुविधा उपलब्ध है.
7. **Gemini 3 में किन टूल का इस्तेमाल किया जा सकता है?** Gemini 3 में ये सुविधाएं उपलब्ध हैं: [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), [Google Maps से जुड़ी जानकारी](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi), [फ़ाइलें खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi), [कोड एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi), और [यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi). यह आपके कस्टम टूल के लिए, स्टैंडर्ड [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) की सुविधा भी देता है. साथ ही, [पहले से मौजूद टूल के साथ मिलकर काम करने की सुविधा](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) भी देता है.
8. **`gemini-3.1-pro-preview-customtools` क्या है?** अगर `gemini-3.1-pro-preview` का इस्तेमाल किया जा रहा है और मॉडल, बैश कमांड के लिए आपके कस्टम टूल को अनदेखा कर रहा है, तो `gemini-3.1-pro-preview-customtools` मॉडल का इस्तेमाल करके देखें.
   ज़्यादा जानकारी [यहां][customtools-model] दी गई है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-08 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-08 (UTC) को अपडेट किया गया."],[],[]]
