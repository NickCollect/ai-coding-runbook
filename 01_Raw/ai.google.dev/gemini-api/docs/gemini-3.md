---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=hi
fetched_at: 2026-08-24T02:37:48.309596+00:00
title: "Gemini 3 \u0915\u0940 \u0921\u0947\u0935\u0932\u092a\u0930 \u0917\u093e\u0907\u0921 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)

सुझाव भेजें

# Gemini 3 की डेवलपर गाइड

Gemini 3, अब तक का हमारा सबसे ऐडवांस मॉडल है. यह रीज़निंग की सबसे नई टेक्नोलॉजी पर आधारित है. इसे एजेंटिक वर्कफ़्लो, ऑटोनॉमस कोडिंग, और मल्टीमॉडल के मुश्किल टास्क को पूरा करके, किसी भी आइडिया को हकीकत में बदलने के लिए डिज़ाइन किया गया है.
इस गाइड में, Gemini 3 मॉडल की मुख्य सुविधाओं और उनका ज़्यादा से ज़्यादा फ़ायदा पाने के तरीके के बारे में बताया गया है.

[Gemini 3 के ऐप्लिकेशन का हमारा कलेक्शन](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=hi) देखें. इससे आपको यह समझने में मदद मिलेगी कि मॉडल, ऐडवांस रीज़निंग, ऑटोनॉमस कोडिंग, और मल्टीमॉडल के मुश्किल टास्क को कैसे मैनेज करता है.

कोड की कुछ लाइनों के साथ शुरुआत करें:

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

## Gemini 3 सीरीज़ के बारे में जानकारी

Gemini 3.1 Pro, उन मुश्किल टास्क के लिए सबसे सही है जिनके लिए दुनिया भर के तथ्यों और बारीकियों की बेहतर समझ और अलग-अलग तरीकों से ऐडवांस रीज़निंग की ज़रूरत होती है.

Gemini 3 Flash, 3-सीरीज़ का हमारा सबसे नया मॉडल है. यह Pro-लेवल की इंटेलिजेंस के साथ, Flash की स्पीड और कीमत पर उपलब्ध है.

Nano Banana Pro (इसे Gemini 3 Pro Image के तौर पर भी जाना जाता है) इमेज जनरेट करने वाला हमारा सबसे बेहतरीन मॉडल है. वहीं, Nano Banana 2 (इसे Gemini 3.1 Flash Image के तौर पर भी जाना जाता है) ज़्यादा वॉल्यूम, ज़्यादा क्षमता, और कम कीमत वाला मॉडल है.

Gemini 3.1 Flash-Lite, हमारा वर्कहॉर्स मॉडल है. इसे लागत के हिसाब से बेहतर मॉडल और ज़्यादा वॉल्यूम वाले टास्क के लिए बनाया गया है.

फ़िलहाल, Gemini 3 के सभी मॉडल, झलक के तौर पर उपलब्ध हैं.

| मॉडल आईडी | कॉन्टेक्स्ट विंडो (इनपुट / आउटपुट) | जानकारी न मिलना | कीमत (इनपुट / आउटपुट)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 10 लाख / 64 हज़ार | जनवरी 2025 | 0.25 डॉलर (टेक्स्ट, इमेज, वीडियो), 0.50 डॉलर (ऑडियो) / 1.50 डॉलर |
| **gemini-3.1-flash-image-preview** | 1 लाख 28 हज़ार / 32 हज़ार | जनवरी 2025 | 0.25 डॉलर (टेक्स्ट इनपुट) / 0.067 डॉलर (इमेज आउटपुट)\*\* |
| **gemini-3.1-pro-preview** | 10 लाख / 64 हज़ार | जनवरी 2025 | 2 डॉलर / 12 डॉलर (2 लाख से कम टोकन)   4 डॉलर / 18 डॉलर (2 लाख से ज़्यादा टोकन) |
| **gemini-3-flash-preview** | 10 लाख / 64 हज़ार | जनवरी 2025 | 0.50 डॉलर / 3 डॉलर |
| **gemini-3-pro-image-preview** | 65 हज़ार / 32 हज़ार | जनवरी 2025 | 2 डॉलर (टेक्स्ट इनपुट) / 0.134 डॉलर (इमेज आउटपुट)\*\* |

*\* कीमत, 10 लाख टोकन के हिसाब से है. हालांकि, कुछ मामलों में यह अलग हो सकती है.*
*\*\* इमेज की कीमत, रिज़ॉल्यूशन के हिसाब से अलग-अलग होती है. ज़्यादा जानकारी के लिए, [कीमत वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.*

सीमाओं, कीमत, और अन्य जानकारी के बारे में ज़्यादा जानने के लिए, [मॉडल वाला पेज](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi) देखें.

## Gemini 3 में API की नई सुविधाएं

Gemini 3 में नए पैरामीटर जोड़े गए हैं. इनकी मदद से, डेवलपर को लेटेंसी, लागत, और मल्टीमॉडल की फ़िडेलिटी पर ज़्यादा कंट्रोल मिलता है.

### थिंकिंग लेवल

Gemini 3 सीरीज़ के मॉडल, प्रॉम्प्ट के हिसाब से जवाब देने के लिए, डिफ़ॉल्ट रूप से डाइनैमिक थिंकिंग का इस्तेमाल करते हैं. `thinking_level` पैरामीटर का इस्तेमाल किया जा सकता है. यह पैरामीटर, मॉडल की इंटरनल रीज़निंग प्रोसेस की **ज़्यादा से ज़्यादा** डेप्थ को कंट्रोल करता है. इसके बाद ही मॉडल, जवाब जनरेट करता है. Gemini 3, इन लेवल को टोकन की पक्की गारंटी के तौर पर नहीं, बल्कि थिंकिंग के लिए रिलेटिव अलाउंस के तौर पर लेता है.

अगर `thinking_level` की जानकारी नहीं दी जाती है, तो Gemini 3 डिफ़ॉल्ट रूप से `high` पर सेट होगा. अगर मुश्किल गहराई से विश्लेषण की ज़रूरत नहीं है, तो कम इंतज़ार का समय वाले जवाब पाने के लिए, मॉडल के गहराई से विचार लेवल को `low` पर सेट किया जा सकता है.

| थिंकिंग लेवल | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | ब्यौरा |
| --- | --- | --- | --- | --- |
| **`minimal`** | काम नहीं करता है | काम करता है (डिफ़ॉल्ट) | काम करता है | ज़्यादातर क्वेरी के लिए, यह "नो थिंकिंग" सेटिंग के हिसाब से काम करता है. कोडिंग के मुश्किल टास्क के लिए, मॉडल बहुत कम सोच-विचार कर सकता है. चैट या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए, यह लेटेंसी को कम करता है. ध्यान दें, `minimal` का मतलब यह नहीं है कि थिंकिंग बंद है. |
| **`low`** | काम करता है | काम करता है | काम करता है | यह लेटेंसी और लागत को कम करता है. यह आसान निर्देशों को फ़ॉलो करने, चैट या ज़्यादा थ्रूपुट वाले ऐप्लिकेशन के लिए सबसे सही है. |
| **`medium`** | काम करता है | काम करता है | काम करता है | ज़्यादातर टास्क के लिए, यह बैलेंस थिंकिंग का इस्तेमाल करता है. |
| **`high`** | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | काम करता है (डाइनैमिक) | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | यह रीज़निंग की डेप्थ को बढ़ाता है. मॉडल को पहले (नो थिंकिंग) आउटपुट टोकन तक पहुंचने में काफ़ी समय लग सकता है . हालांकि, आउटपुट ज़्यादा सोच-समझकर दिया जाएगा. |

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

हमारा सुझाव है कि Gemini 3 के सभी मॉडल के लिए, टेंपरेचर पैरामीटर को डिफ़ॉल्ट वैल्यू `1.0` पर सेट रखें.

पिछले मॉडल में, क्रिएटिविटी बनाम डिटरमिनिज़म को कंट्रोल करने के लिए, टेंपरेचर को ट्यून करने से अक्सर फ़ायदा मिलता था. हालांकि, Gemini 3 की गहराई से विश्लेषण क्षमताओं को डिफ़ॉल्ट सेटिंग के लिए ऑप्टिमाइज़ किया गया है. तापमान बदलने (इसे 1.0 से कम पर सेट करने) से, अनचाहा व्यवहार हो सकता है. जैसे, लूपिंग या परफ़ॉर्मेंस में गिरावट. खास तौर पर, गणित या रीज़निंग के मुश्किल टास्क में ऐसा हो सकता है.

### थॉट सिग्नेचर

Gemini 3 मॉडल, एपीआई कॉल के दौरान रीज़निंग कॉन्टेक्स्ट को बनाए रखने के लिए, थॉट सिग्नेचर का इस्तेमाल करते हैं. ये सिग्नेचर, मॉडल की इंटरनल थॉट प्रोसेस के एन्क्रिप्ट किए गए वर्शन होते हैं.

- **स्टेटफ़ुल मोड (सुझाया जाता है)**: स्टेटफ़ुल मोड में इंटरैक्शन एपीआई का इस्तेमाल करते समय (`previous_interaction_id` उपलब्ध कराने पर), सर्वर, बातचीत के इतिहास और थॉट सिग्नेचर को अपने-आप मैनेज करता है.
- **स्टेटलेस मोड**: अगर बातचीत के इतिहास को मैन्युअल तरीके से मैनेज किया जा रहा है, तो आपको असली होने की पुष्टि करने के लिए, बाद के अनुरोधों में सिग्नेचर के साथ थॉट ब्लॉक शामिल करने होंगे.

ज़्यादा जानकारी के लिए, [थॉट सिग्नेचर](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) वाला पेज देखें.

### टूल के साथ स्ट्रक्चर्ड आउटपुट

Gemini 3 मॉडल की मदद से, [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) को बिल्ट-इन टूल के साथ जोड़ा जा सकता है. इनमें,
[Google Search के साथ ग्राउंडिंग](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), [यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi), [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi), और [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) शामिल हैं.

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

Gemini 3.1 Flash Image और Gemini 3 Pro Image की मदद से, टेक्स्ट प्रॉम्प्ट से इमेज जनरेट की जा सकती हैं और उनमें बदलाव किया जा सकता है. यह गहराई से विश्लेषण का इस्तेमाल करके, प्रॉम्प्ट के हिसाब से "सोचता" है और रीयल-टाइम डेटा—जैसे, मौसम के पूर्वानुमान या स्टॉक चार्ट—को वापस पा सकता है. इसके बाद, [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) भरोसेमंद स्रोतों से जानकारी लेने की सुविधा का इस्तेमाल करके, हाई-फ़िडेलिटी इमेज जनरेट करता है.

**नई और बेहतर सुविधाएं:**

- **4K और टेक्स्ट रेंडरिंग:** 2K और 4K रिज़ॉल्यूशन तक, साफ़ और आसानी से पढ़े जा सकने वाले टेक्स्ट और डायग्राम जनरेट करें.
- **ग्राउंडेड जनरेशन:** तथ्यों की पुष्टि करने और असली दुनिया की जानकारी के आधार पर इमेज जनरेट करने के लिए, `google_search` टूल का इस्तेमाल करें. Gemini 3.1 Flash Image के लिए, Google *Image* Search के साथ ग्राउंडिंग की सुविधा उपलब्ध है.
- **बोलकर या लिखकर बदलाव करने की सुविधा:** सिर्फ़ बदलाव करने के लिए कहकर, इमेज में सिलसिलेवार बातचीत के ज़रिए बदलाव करें. जैसे, "बैकग्राउंड को सनसेट जैसा बनाओ". इस वर्कफ़्लो में, **थॉट सिग्नेचर** का इस्तेमाल किया जाता है, ताकि अलग-अलग चरणों के बीच विज़ुअल कॉन्टेक्स्ट को बनाए रखा जा सके.

आस्पेक्ट रेशियो, एडिटिंग वर्कफ़्लो, और कॉन्फ़िगरेशन
के विकल्पों के बारे में पूरी जानकारी पाने के लिए, [इमेज जनरेशन गाइड](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) देखें.

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

### इमेज के साथ कोड एक्ज़ीक्यूशन

Gemini 3 Flash, विज़न को सिर्फ़ एक झलक के तौर पर नहीं, बल्कि एक ऐक्टिव जांच के तौर पर ले सकता है. रीज़निंग को [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) के साथ जोड़कर, मॉडल एक प्लान बनाता है. इसके बाद, ज़ूम इन करने, क्रॉप करने, एनोटेट करने या इमेज में अन्य बदलाव करने के लिए, Python कोड लिखता है और उसे
एक्ज़ीक्यूट करता है
. इससे, अपने जवाबों को विज़ुअली ग्राउंड किया जा सकता है.

**इस्तेमाल के उदाहरण:**

- **ज़ूम और जांच:** मॉडल, यह अपने-आप पता लगा लेता है कि जानकारी बहुत छोटी है या नहीं.जैसे, दूर से गेज या सीरियल नंबर पढ़ना. इसके बाद, ज़्यादा रिज़ॉल्यूशन पर उस हिस्से को क्रॉप करके फिर से जांचने के लिए, कोड लिखता है.
- **विज़ुअल मैथ और प्लॉटिंग:** मॉडल, कोड का इस्तेमाल करके कई चरणों में कैलकुलेशन कर सकता है. जैसे, रसीद पर मौजूद लाइन आइटम को जोड़ना या निकाले गए डेटा से Matplotlib चार्ट जनरेट करना.
- **इमेज एनोटेशन:** मॉडल, "यह आइटम कहां होना चाहिए?" जैसे सवालों के जवाब देने के लिए, इमेज पर सीधे तौर पर तीर, बाउंडिंग बॉक्स या अन्य एनोटेशन बना सकता है.

विज़ुअल थिंकिंग की सुविधा चालू करने के लिए, [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) को एक टूल के तौर पर कॉन्फ़िगर करें. ज़रूरत पड़ने पर, मॉडल इमेज में बदलाव करने के लिए, कोड का इस्तेमाल अपने-आप करेगा.

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

इमेज के साथ कोड एक्ज़ीक्यूशन के बारे में ज़्यादा जानने के लिए, [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi#images) देखें.

### मल्टीमॉडल फ़ंक्शन के जवाब

[मल्टीमॉडल फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#multimodal)
की मदद से, उपयोगकर्ताओं को ऐसे फ़ंक्शन के जवाब मिल सकते हैं जिनमें
मल्टीमॉडल ऑब्जेक्ट शामिल होते हैं. इससे, मॉडल की फ़ंक्शन कॉलिंग
क्षमताओं का बेहतर इस्तेमाल किया जा सकता है. स्टैंडर्ड फ़ंक्शन कॉलिंग में, सिर्फ़ टेक्स्ट पर आधारित फ़ंक्शन के जवाब मिलते हैं:

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

### बिल्ट-इन टूल और फ़ंक्शन कॉलिंग को जोड़ना

[Gemini 3 में, एक ही एपीआई कॉल में बिल्ट-इन टूल (जैसे, Google Search, यूआरएल
कॉन्टेक्स्ट वगैरह) और कस्टम [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) टूल का इस्तेमाल किया जा सकता है. इससे, ज़्यादा मुश्किल वर्कफ़्लो बनाए जा सकते हैं.](https://ai.google.dev/gemini-api/docs/tools?hl=hi)

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

Gemini 3, अब तक का हमारा सबसे बेहतरीन मॉडल है. यह Gemini 2.5 से बेहतर है. माइग्रेट करते समय, इन बातों का ध्यान रखें:

- **थिंकिंग:** अगर पहले Gemini 2.5 से जवाब पाने के लिए, प्रॉम्प्ट इंजीनियरिंग की मुश्किल तकनीकों (जैसे
  चेन ऑफ़ थॉट) का इस्तेमाल किया जाता था, तो Gemini 3 को
  `thinking_level: "high"` और आसान प्रॉम्प्ट के साथ आज़माएं.
- **तापमान की सेटिंग:** अगर आपके मौजूदा कोड में तापमान को साफ़ तौर पर सेट किया गया है (खास तौर पर, डिटरमिनिस्टिक आउटपुट के लिए कम वैल्यू पर), तो हमारा सुझाव है कि इस पैरामीटर को हटा दें और Gemini 3 के डिफ़ॉल्ट तापमान 1.0 का इस्तेमाल करें. इससे, लूपिंग की समस्याओं या मुश्किल टास्क में परफ़ॉर्मेंस में गिरावट से बचा जा सकता है.
- **पीडीएफ़ और दस्तावेज़ को समझना:** अगर आपको दस्तावेज़ को पार्स करने के लिए, किसी खास तरीके की ज़रूरत है, तो नई `media_resolution_high` सेटिंग की जांच करें, ताकि यह पक्का किया जा सके कि सटीक जानकारी मिलती रहे.
- **टोकन का इस्तेमाल:** Gemini 3 के डिफ़ॉल्ट पर माइग्रेट करने से, पीडीएफ़ के लिए टोकन का इस्तेमाल **बढ़** सकता है. हालांकि, वीडियो के लिए टोकन का इस्तेमाल **कम** हो सकता है. अगर डिफ़ॉल्ट रिज़ॉल्यूशन ज़्यादा होने की वजह से, अब अनुरोध कॉन्टेक्स्ट विंडो से ज़्यादा हो जाते हैं, तो हमारा सुझाव है कि मीडिया रिज़ॉल्यूशन को साफ़ तौर पर कम करें.
- **इमेज सेगमेंटेशन:** Gemini 3 Pro या Gemini 3 Flash में, इमेज सेगमेंटेशन की सुविधाएं (ऑब्जेक्ट के लिए पिक्सल-लेवल मास्क दिखाना) उपलब्ध नहीं हैं. जिन वर्कलोड के लिए, बिल्ट-इन इमेज सेगमेंटेशन की ज़रूरत होती है उनके लिए, हमारा सुझाव है कि थिंकिंग बंद करके, Gemini 2.5 Flash का इस्तेमाल जारी रखें.
- **कंप्यूटर का इस्तेमाल:** Gemini 3 Pro और Gemini 3 Flash में, [कंप्यूटर
  के इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) की सुविधा उपलब्ध है. 2.5 सीरीज़ के उलट, आपको कंप्यूटर के इस्तेमाल वाले टूल को ऐक्सेस करने के लिए, किसी अलग मॉडल का इस्तेमाल करने की ज़रूरत नहीं है.
- **टूल का इस्तेमाल**: [बिल्ट-इन टूल को फ़ंक्शन कॉलिंग के साथ इस्तेमाल किया जा सकता है](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) अब Gemini 3 मॉडल के लिए. अब Gemini 3
  मॉडल के लिए, [Maps
  ग्राउंडिंग](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi) की सुविधा भी उपलब्ध है.

## OpenAI के साथ काम करने की क्षमता

[OpenAI के साथ काम करने की सुविधा](https://ai.google.dev/gemini-api/docs/openai?hl=hi) का इस्तेमाल करने वाले उपयोगकर्ताओं के लिए,
स्टैंडर्ड पैरामीटर (OpenAI का `reasoning_effort`),
Gemini (`thinking_level`) के बराबर पैरामीटर पर अपने-आप मैप हो जाते हैं.

## प्रॉम्प्ट करने के सबसे सही तरीके

Gemini 3, एक रीज़निंग मॉडल है. इससे प्रॉम्प्ट करने का तरीका बदल जाता है.

- **सटीक निर्देश:** इनपुट प्रॉम्प्ट में अपनी बात कम शब्दों में रखें. Gemini 3, सीधे और साफ़ तौर पर दिए गए निर्देशों के हिसाब से सबसे अच्छा जवाब देता है. यह पुराने मॉडल के लिए इस्तेमाल की जाने वाली, प्रॉम्प्ट इंजीनियरिंग की ज़्यादा शब्दों वाली या मुश्किल तकनीकों का ज़्यादा विश्लेषण कर सकता है.
- **आउटपुट वर्बोसिटी:** डिफ़ॉल्ट रूप से, Gemini 3 कम शब्दों में जवाब देता है और सीधे, असरदार जवाब देना पसंद करता है. अगर आपके इस्तेमाल के उदाहरण के लिए, ज़्यादा बातचीत करने वाले या "चैट करने वाले" मॉडल की ज़रूरत है, तो आपको प्रॉम्प्ट में साफ़ तौर पर मॉडल को निर्देश देना होगा. जैसे, "इसे एक दोस्त की तरह, बातूनी असिस्टेंट के तौर पर समझाओ".
- **कॉन्टेक्स्ट मैनेजमेंट:** बड़े डेटासेट (जैसे, पूरी किताबें, कोडबेस या लंबे वीडियो) के साथ काम करते समय, अपने खास निर्देश या सवाल, डेटा कॉन्टेक्स्ट के बाद, प्रॉम्प्ट के आखिर में रखें. मॉडल की रीज़निंग को दिए गए डेटा से जोड़ने के लिए, अपने सवाल की शुरुआत "ऊपर दी गई जानकारी के आधार पर..." जैसे वाक्यांश से करें.

प्रॉम्प्ट डिज़ाइन की रणनीतियों के बारे में ज़्यादा जानने के लिए, [प्रॉम्प्ट इंजीनियरिंग गाइड](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi) देखें.

## अक्सर पूछे जाने वाले सवाल

1. **Gemini 3 के लिए, जानकारी न मिलने की तारीख क्या है?** Gemini 3 मॉडल के लिए, जानकारी न मिलने की तारीख जनवरी 2025 है. हाल ही की जानकारी पाने के लिए, [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) टूल का इस्तेमाल करें.
2. **कॉन्टेक्स्ट विंडो की सीमाएं क्या हैं?** Gemini 3 मॉडल, 10 लाख टोकन वाली इनपुट कॉन्टेक्स्ट विंडो और 64 हज़ार टोकन तक के आउटपुट के साथ काम करते हैं.
3. **क्या Gemini 3 के लिए कोई मुफ़्त टियर उपलब्ध है?** Gemini API में, Gemini 3 Flash `gemini-3-flash-preview` के लिए एक मुफ़्त टियर उपलब्ध है. Google AI Studio में, Gemini 3.1 Pro और 3 Flash को बिना किसी शुल्क के आज़माया जा सकता है. हालांकि, Gemini API में `gemini-3.1-pro-preview` के लिए कोई मुफ़्त टियर उपलब्ध नहीं है.
4. **क्या मेरा पुराना `thinking_budget` कोड अब भी काम करेगा?** हां, `thinking_budget` अब भी बैकवर्ड कंपैटबिलिटी के लिए काम करता है. हालांकि, ज़्यादा अनुमानित परफ़ॉर्मेंस के लिए, हमारा सुझाव है कि `thinking_level` पर माइग्रेट करें. एक ही अनुरोध में, दोनों का इस्तेमाल न करें.
5. **क्या Gemini 3, बैच एपीआई के साथ काम करता है?** [हां, Gemini 3, बैच एपीआई के साथ काम करता है.](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)
6. **क्या कॉन्टेक्स्ट कैशिंग की सुविधा उपलब्ध है?** हां, [कॉन्टेक्स्ट कैशिंग](https://ai.google.dev/gemini-api/docs/caching?hl=hi) की सुविधा Gemini 3 के लिए उपलब्ध है.
7. **Gemini 3 में कौनसे टूल इस्तेमाल किए जा सकते हैं?** Gemini 3 में,
   [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi),
   [Google Maps के साथ ग्राउंडिंग](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi),
   [फ़ाइल सर्च](https://ai.google.dev/gemini-api/docs/file-search?hl=hi),
   [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi), और
   [यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) का इस्तेमाल किया जा सकता है. [इसमें, आपके कस्टम टूल के लिए स्टैंडर्ड [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) की सुविधा भी उपलब्ध है. साथ ही, इसे बिल्ट-इन टूल के साथ भी इस्तेमाल किया जा सकता है.](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi)
8. **क्या है `gemini-3.1-pro-preview-customtools`?** अगर
   `gemini-3.1-pro-preview` का इस्तेमाल किया जा रहा है और मॉडल,
   bash कमांड के लिए आपके कस्टम टूल को अनदेखा कर रहा है, तो इसके बजाय `gemini-3.1-pro-preview-customtools` मॉडल का इस्तेमाल करें.
   ज़्यादा जानकारी के लिए, [यहां][customtools-model] जाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-08-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-08-19 (UTC) को अपडेट किया गया."],[],[]]
