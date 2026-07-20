---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=hi
fetched_at: 2026-07-20T04:35:42.034979+00:00
title: "Google Maps \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0917\u094d\u0930\u093e\u0909\u0902\u0921\u093f\u0902\u0917 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Google Maps की मदद से ग्राउंडिंग करना

Grounding with Google Maps की मदद से, Gemini की जनरेटिव क्षमताओं को Google Maps के सटीक, अप-टू-डेट, और ज़्यादा जानकारी वाले डेटा से जोड़ा जा सकता है. इस सुविधा की मदद से, डेवलपर अपने ऐप्लिकेशन में जगह की जानकारी के आधार पर काम करने वाली सुविधाएं आसानी से शामिल कर सकते हैं. जब किसी उपयोगकर्ता की क्वेरी में Maps के डेटा से जुड़ा कॉन्टेक्स्ट होता है, तो Gemini मॉडल, Google Maps का इस्तेमाल करके, तथ्यों पर आधारित और अप-टू-डेट जवाब देता है. ये जवाब, उपयोगकर्ता की बताई गई जगह या जगह की अनुमानित जानकारी के हिसाब से होते हैं.

- **जगह की जानकारी के आधार पर सटीक जवाब:** भौगोलिक तौर पर खास क्वेरी के लिए, Google Maps के मौजूदा और ज़्यादा डेटा का इस्तेमाल करें.
- **बेहतर मनमुताबिक अनुभव:** उपयोगकर्ता की बताई गई जगहों के आधार पर, सुझाव और जानकारी को अपने हिसाब से बनाएं.

## शुरू करें

इस उदाहरण में, Grounding with Google Maps को अपने ऐप्लिकेशन में इंटिग्रेट करने का तरीका बताया गया है. इससे उपयोगकर्ता की क्वेरी के सटीक और जगह की जानकारी के आधार पर जवाब दिए जा सकते हैं. प्रॉम्प्ट में, स्थानीय सुझावों के बारे में पूछा जाता है. इसमें उपयोगकर्ता की जगह की जानकारी देने का विकल्प भी होता है. इससे Gemini मॉडल, Google Maps के डेटा का इस्तेमाल कर पाता है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Google Maps से जानकारी लेने की सुविधा कैसे काम करती है

Grounding with Google Maps, Maps API को सोर्स के तौर पर इस्तेमाल करके, Gemini API को Google Geo इकोसिस्टम के साथ इंटिग्रेट करता है. जब किसी उपयोगकर्ता की क्वेरी में भौगोलिक कॉन्टेक्स्ट शामिल होता है, तो Gemini मॉडल, Grounding with Google Maps टूल को शुरू कर सकता है. इसके बाद, मॉडल, दी गई जगह के हिसाब से Google Maps के डेटा के आधार पर जवाब जनरेट कर सकता है.

आम तौर पर, इस प्रोसेस में ये चरण शामिल होते हैं:

1. **उपयोगकर्ता की क्वेरी:** कोई उपयोगकर्ता आपके ऐप्लिकेशन में क्वेरी सबमिट करता है.इसमें भौगोलिक कॉन्टेक्स्ट शामिल हो सकता है. जैसे, "मेरे आस-पास की कॉफ़ी शॉप," "सैन फ़्रांसिस्को में मौजूद म्यूज़ियम".
2. **टूल शुरू करना:** Gemini मॉडल, भौगोलिक इरादे को पहचानकर, Grounding with Google Maps टूल को शुरू करता है. इस टूल को उपयोगकर्ता के `latitude` और `longitude` की जानकारी भी दी जा सकती है. हालांकि, यह ज़रूरी नहीं है. यह टूल, टेक्स्ट के आधार पर खोज करने वाला टूल है. यह Maps पर खोज करने की तरह ही काम करता है. जैसे, स्थानीय क्वेरी ("मेरे आस-पास") के लिए, निर्देशांकों का इस्तेमाल किया जाएगा. वहीं, खास या गैर-स्थानीय क्वेरी पर, साफ़ तौर पर बताई गई जगह का असर नहीं पड़ेगा.
3. **डेटा वापस पाना:** Grounding with Google Maps सेवा, Google Maps से काम की जानकारी (जैसे, जगहें, समीक्षाएं, फ़ोटो, पते, कारोबार के खुले होने का समय) के लिए क्वेरी करती है.
4. **डेटा के आधार पर जवाब जनरेट करना:** वापस पाए गए Maps के डेटा का इस्तेमाल, Gemini मॉडल के जवाब के लिए किया जाता है. इससे यह पक्का किया जाता है कि जवाब सटीक और काम का हो.
5. **जवाब:** मॉडल, टेक्स्ट में जवाब देता है. इसमें Google Maps के सोर्स के साइटेशन शामिल होते हैं.

## Google Maps से जानकारी लेने की सुविधा का इस्तेमाल कब और क्यों करना चाहिए

Grounding with Google Maps, उन ऐप्लिकेशन के लिए सबसे सही है जिनमें सटीक, अप-टू-डेट, और जगह के हिसाब से जानकारी की ज़रूरत होती है. यह उपयोगकर्ता अनुभव को बेहतर बनाता है. इसके लिए, Google Maps के 25 करोड़ से ज़्यादा जगहों के डेटाबेस के आधार पर, काम का और मनमुताबिक कॉन्टेंट उपलब्ध कराया जाता है.

Grounding with Google Maps का इस्तेमाल तब करें, जब आपके ऐप्लिकेशन को:

- जगह के हिसाब से पूछे गए सवालों के सटीक और पूरे जवाब देने हों.
- बातचीत के ज़रिए यात्रा की योजना बनाने वाले टूल और स्थानीय गाइड बनाने हों.
- जगह और उपयोगकर्ता की प्राथमिकताओं (जैसे, रेस्टोरेंट या दुकानें) के आधार पर, दिलचस्पी की जगहों के सुझाव देने हों.
- सामाजिक, खुदरा या फ़ूड डिलीवरी सेवाओं के लिए, जगह की जानकारी के आधार पर अनुभव बनाने हों.

Grounding with Google Maps, उन मामलों में सबसे अच्छा काम करता है जहां आस-पास की जगहें और मौजूदा सटीक डेटा ज़रूरी होता है. जैसे, "मेरे आस-पास सबसे अच्छी कॉफ़ी शॉप ढूंढना" या दिशा-निर्देश पाना.

## एपीआई के तरीके और पैरामीटर

Grounding with Google Maps, Gemini API के ज़रिए एक टूल के तौर पर
[`generateContent`](https://ai.google.dev/api/generate-content?hl=hi) तरीके में उपलब्ध है. Grounding with Google Maps को चालू और कॉन्फ़िगर करने के लिए, अपने अनुरोध के `tools` पैरामीटर में [`googleMaps`](https://ai.google.dev/api/caching?hl=hi#GoogleMaps) ऑब्जेक्ट शामिल करें.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

इसके अलावा, टूल, कॉन्टेक्चुअल जगह को `toolConfig` के तौर पर पास करने की सुविधा भी देता है.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### भरोसेमंद स्रोतों से मिले जवाब को समझना

जब किसी जवाब को Google Maps के डेटा के आधार पर जनरेट किया जाता है, तो उसमें
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=hi#GroundingMetadata) फ़ील्ड शामिल होता है.
यह स्ट्रक्चर्ड डेटा, दावों की पुष्टि करने और आपके ऐप्लिकेशन में साइटेशन का बेहतर अनुभव बनाने के लिए ज़रूरी है. साथ ही, यह सेवा के इस्तेमाल की ज़रूरी शर्तों को पूरा करने में भी मदद करता है.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API,
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=hi#GroundingMetadata) के साथ यह जानकारी दिखाता है:

- `groundingChunks`: ऑब्जेक्ट का कलेक्शन. इसमें `maps` सोर्स (`uri`, `placeId`, और `title`) शामिल होते हैं.
- `groundingSupports`: `groundingChunks` में मौजूद सोर्स से, मॉडल के जवाब के टेक्स्ट को कनेक्ट करने के लिए, चंक का कलेक्शन. हर चंक, टेक्स्ट स्पैन (`startIndex` और `endIndex` से तय किया गया) को एक या उससे ज़्यादा `groundingChunkIndices` से लिंक करता है. यह इनलाइन साइटेशन बनाने की कुंजी है.

टेक्स्ट में इनलाइन साइटेशन दिखाने के तरीके के बारे में कोड का स्निपेट देखने के लिए, Google Search से जानकारी लेने की सुविधा के दस्तावेज़ों में दिया गया [उदाहरण](https://ai.google.dev/gemini-api/docs/google-search?hl=hi#attributing_sources_with_inline_citations)
देखें.

## इस्तेमाल के उदाहरण

Grounding with Google Maps, जगह की जानकारी के आधार पर काम करने वाले कई मामलों में इस्तेमाल किया जा सकता है. यहां दिए गए उदाहरणों में बताया गया है कि अलग-अलग प्रॉम्प्ट और पैरामीटर, Grounding with Google Maps का इस्तेमाल कैसे कर सकते हैं. Google Maps से मिले नतीजों में मौजूद जानकारी, असल हालात से अलग हो सकती है.

### जगह के हिसाब से पूछे गए सवालों को मैनेज करना

किसी खास जगह के बारे में ज़्यादा जानकारी वाले सवाल पूछें, ताकि Google पर उपयोगकर्ता की समीक्षाओं और Maps के अन्य डेटा के आधार पर जवाब मिल सकें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### जगह के हिसाब से मनमुताबिक अनुभव देना

किसी उपयोगकर्ता की प्राथमिकताओं और किसी खास इलाके के हिसाब से सुझाव पाएं.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### यात्रा की योजना बनाने में मदद करना

कई दिनों की यात्रा की योजनाएं जनरेट करें. इनमें अलग-अलग जगहों के बारे में दिशा-निर्देश और जानकारी शामिल होती है. यह यात्रा से जुड़े ऐप्लिकेशन के लिए सबसे सही है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## सेवा के इस्तेमाल की ज़रूरी शर्तें

इस सेक्शन में, Grounding with Google Maps के इस्तेमाल की ज़रूरी शर्तों के बारे में बताया गया है.

### उपयोगकर्ता को Google Maps के सोर्स के इस्तेमाल के बारे में बताना

Google Maps से मिले हर नतीजे के साथ, आपको `groundingChunks` में सोर्स मिलेंगे. ये सोर्स, हर जवाब के लिए काम के होते हैं. इसके अलावा, यह मेटाडेटा भी दिखाया जाता है:

- सोर्स यूआरआई
- title
- आईडी

Grounding with Google Maps से मिले नतीजे दिखाते समय, आपको Google Maps के सोर्स की जानकारी देनी होगी. साथ ही, अपने उपयोगकर्ताओं को यह जानकारी देनी होगी:

- Google Maps के सोर्स, जनरेट किए गए उस कॉन्टेंट के तुरंत बाद दिखने चाहिए जिसके लिए सोर्स काम के हैं. जनरेट किए गए इस कॉन्टेंट को, Google Maps से मिले नतीजे के तौर पर भी जाना जाता है.
- Google Maps के सोर्स, उपयोगकर्ता के एक इंटरैक्शन में दिखने चाहिए.

### Google Maps के लिंक के साथ, Google Maps के सोर्स दिखाना

`groundingChunks` और `grounding_chunks.maps.placeAnswerSources.reviewSnippets` में मौजूद हर सोर्स के लिए, इन ज़रूरी शर्तों के मुताबिक लिंक का प्रीव्यू जनरेट करना होगा:

- Google Maps के टेक्स्ट
  [एट्रिब्यूशन के दिशा-निर्देशों के मुताबिक, हर सोर्स को Google Maps से एट्रिब्यूट करें.](#maps-attribution-guidelines)
- जवाब में दिए गए सोर्स का टाइटल दिखाएं.
- जवाब में मौजूद `uri` या `googleMapsUri` का इस्तेमाल करके, सोर्स से लिंक करें.

इन इमेज में, सोर्स और Google Maps के लिंक दिखाने की ज़रूरी शर्तें दिखाई गई हैं.

![जवाब के साथ सोर्स दिखाने वाला प्रॉम्प्ट](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=hi)

सोर्स के व्यू को छोटा किया जा सकता है.

![जवाब और सोर्स को छोटा करके दिखाया गया प्रॉम्प्ट](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=hi)

ज़रूरी नहीं: लिंक के प्रीव्यू को अन्य कॉन्टेंट के साथ बेहतर बनाएं. जैसे:

- Google Maps के टेक्स्ट एट्रिब्यूशन से पहले, [Google Maps का फ़ेविकॉन](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=hi)
  डाला जाता है.
- सोर्स यूआरएल (`og:image`) से कोई फ़ोटो.

Google Maps के कुछ डेटा प्रोवाइडर और उनकी
लाइसेंस की शर्तों के बारे में ज़्यादा जानने के लिए, [Google Maps और Google Earth के कानूनी नोटिस देखें](https://www.google.com/help/legalnotices_maps/?hl=hi).

### Google Maps के टेक्स्ट एट्रिब्यूशन के दिशा-निर्देश

टेक्स्ट में सोर्स को Google Maps से एट्रिब्यूट करते समय, इन दिशा-निर्देशों का पालन करें:

- Google Maps के टेक्स्ट में किसी भी तरह का बदलाव न करें:
  - Google Maps के केस में बदलाव न करें.
  - Google Maps को कई लाइनों में रैप न करें.
  - Google Maps को किसी दूसरी भाषा में स्थानीय भाषा में अनुवादित न करें.
  - HTML एट्रिब्यूट translate="no" का इस्तेमाल करके, ब्राउज़र को Google Maps का अनुवाद करने से रोकें.
- Google Maps के टेक्स्ट को, यहां दी गई टेबल में बताए गए तरीके से स्टाइल करें:

| प्रॉपर्टी | शैली |
| --- | --- |
| `Font family` | Roboto. फ़ॉन्ट लोड करना ज़रूरी नहीं है. |
| `Fallback font family` | आपके प्रॉडक्ट में पहले से इस्तेमाल किया जा रहा कोई भी sans serif बॉडी फ़ॉन्ट या डिफ़ॉल्ट सिस्टम फ़ॉन्ट को शुरू करने के लिए "Sans-Serif" |
| `Font style` | सामान्य |
| `Font weight` | 400 |
| `Font color` | सफ़ेद, काला (#1F1F1F) या ग्रे (#5E5E5E). बैकग्राउंड के मुकाबले, 4.5:1 का कंट्रास्ट बनाए रखें, ताकि टेक्स्ट आसानी से पढ़ा जा सके. |
| `Font size` | - कम से कम फ़ॉन्ट साइज़: 12sp - ज़्यादा से ज़्यादा फ़ॉन्ट साइज़: 16sp - sp के बारे में जानने के लिए, [मटीरियल डिज़ाइन की वेबसाइट](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc) पर फ़ॉन्ट साइज़ की इकाइयां देखें. |
| `Spacing` | सामान्य |

#### सीएसएस का उदाहरण

यहां दी गई सीएसएस, Google Maps को सफ़ेद या हल्के बैकग्राउंड पर, सही टाइपोग्राफ़िक स्टाइल और रंग के साथ रेंडर करती है.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### जगह का आईडी और समीक्षा का आईडी

Google Maps के डेटा में, जगह का आईडी और समीक्षा का आईडी शामिल होता है. जवाब के इस डेटा को कैश किया जा सकता है, सेव किया जा सकता है, और एक्सपोर्ट किया जा सकता है:

- `placeId`
- `reviewId`

Grounding with Google Maps की शर्तों में, कैशिंग पर लगी पाबंदियां लागू नहीं होती हैं.

### रोकी गई गतिविधि और इलाका

Grounding with Google Maps के लिए, कुछ कॉन्टेंट और गतिविधियों पर अतिरिक्त पाबंदियां हैं, ताकि प्लैटफ़ॉर्म को सुरक्षित और भरोसेमंद बनाए रखा जा सके. शर्तों में इस्तेमाल की पाबंदियों
के अलावा [शर्तों](https://ai.google.dev/gemini-api/terms?hl=hi#grounding-with-google-maps):

- Grounding with Google Maps का इस्तेमाल, ज़्यादा जोखिम वाली गतिविधियों के लिए नहीं किया जा सकता. इनमें, आपातकालीन सेवाओं के लिए जवाब देने वाली सेवाएं भी शामिल हैं.
- आप अपने उस ऐप्लिकेशन को किसी ऐसे इलाके में डिस्ट्रिब्यूट या मार्केट नहीं करेंगे जहां Grounding with Google Maps की सुविधा उपलब्ध नहीं है. ज़्यादा जानकारी के लिए, [Google Maps Platform के लिए पाबंदी वाले इलाके](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=hi) देखें.
  पाबंदी वाले इलाकों की सूची को समय-समय पर अपडेट किया जा सकता है.

## सबसे सही तरीके

- **उपयोगकर्ता की जगह की जानकारी देना:** सबसे काम के और मनमुताबिक जवाब पाने के लिए, `googleMapsGrounding` कॉन्फ़िगरेशन में हमेशा `user_location` (अक्षांश और देशांतर) शामिल करें. ऐसा तब करें, जब उपयोगकर्ता की जगह की जानकारी उपलब्ध हो.
- **आखिरी उपयोगकर्ताओं को जानकारी देना:** अपने आखिरी उपयोगकर्ताओं को साफ़ तौर पर बताएं कि उनकी क्वेरी के जवाब देने के लिए, Google Maps के डेटा का इस्तेमाल किया जा रहा है. खास तौर पर, तब जब टूल चालू हो.
- **लेटेंसी की निगरानी करना:** बातचीत वाले ऐप्लिकेशन के लिए, पक्का करें कि Grounding with Google Maps से मिले जवाबों के लिए P95 लेटेंसी, स्वीकार की जा सकने वाली थ्रेशोल्ड के अंदर हो. इससे उपयोगकर्ता अनुभव को बेहतर बनाए रखा जा सकता है.
- **ज़रूरत न होने पर टॉगल ऑफ़ करना:** Grounding with Google Maps, डिफ़ॉल्ट रूप से बंद होता है. इसे सिर्फ़ तब चालू करें (`"tools": [{"googleMaps": {}}]`), जब किसी क्वेरी में
  भौगोलिक कॉन्टेक्स्ट शामिल हो. इससे परफ़ॉर्मेंस और लागत को ऑप्टिमाइज़ किया जा सकता है.

## सीमाएं

- **भौगोलिक दायरा:** Grounding with Google Maps, दुनिया भर में उपलब्ध है
- **मॉडल के साथ काम करने की सुविधा:** काम करने वाले [मॉडल](#supported-models) सेक्शन देखें.
- **मल्टीमॉडल इनपुट/आउटपुट:** फ़िलहाल, Grounding with Google Maps, टेक्स्ट के अलावा मल्टीमॉडल इनपुट या आउटपुट के साथ काम नहीं करता.
- **डिफ़ॉल्ट स्थिति:** Grounding with Google Maps टूल, डिफ़ॉल्ट रूप से बंद होता है.
  आपको इसे अपने एपीआई अनुरोधों में साफ़ तौर पर चालू करना होगा.

## कीमत और रेट लिमिट

Grounding with Google Maps की कीमत, क्वेरी के आधार पर तय की जाती है. फ़िलहाल, इसकी दर **25 डॉलर / 1,000 प्रॉम्प्ट** है. मुफ़्त टियर में, हर दिन 500 अनुरोध किए जा सकते हैं. किसी अनुरोध को कोटा में सिर्फ़ तब गिना जाता है, जब कोई प्रॉम्प्ट, Google Maps से मिले कम से कम एक नतीजे को वापस करता है. इसका मतलब है कि नतीजों में Google Maps का कम से कम एक सोर्स शामिल हो. अगर एक अनुरोध से Google Maps को कई क्वेरी भेजी जाती हैं, तो इसे रेट लिमिट के हिसाब से एक अनुरोध के तौर पर गिना जाता है.

कीमत की ज़्यादा जानकारी के लिए, [Gemini API की कीमत वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.

## काम करने वाले मॉडल

ये मॉडल, Grounding with Google Maps के साथ काम करते हैं:

| मॉडल | Grounding with Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Pro का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## टूल के साथ काम करने वाले कॉम्बिनेशन

Gemini 3 मॉडल, बिल्ट-इन टूल (जैसे, Grounding with Google Maps) को कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ इस्तेमाल करने की सुविधा देते हैं. ज़्यादा जानने के लिए,
[टूल के कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) वाला पेज देखें.

## आगे क्या करना है

- [Gemini API की कुकबुक में, Google Search से जानकारी लेने की सुविधा आज़माएं.](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=hi)
- [अन्य उपलब्ध टूल के बारे में जानें.](https://ai.google.dev/gemini-api/docs/tools?hl=hi)
- ज़िम्मेदारी से एआई के इस्तेमाल के सबसे सही तरीकों और Gemini API के सुरक्षा
  फ़िल्टर के बारे में ज़्यादा जानने के लिए, [सुरक्षा सेटिंग की गाइड देखें](https://ai.google.dev/gemini-api/docs/safety-settings?hl=hi).

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-24 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-24 (UTC) को अपडेट किया गया."],[],[]]
