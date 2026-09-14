---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi
fetched_at: 2026-09-14T05:51:38.935027+00:00
title: "Google Maps \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0917\u094d\u0930\u093e\u0909\u0902\u0921\u093f\u0902\u0917 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Google Maps की मदद से ग्राउंडिंग करना

Google Maps से जानकारी लेने की सुविधा, Gemini की जनरेटिव क्षमताओं को Google Maps के सटीक, अप-टू-डेट, और ज़्यादा जानकारी वाले डेटा से जोड़ती है. इस सुविधा की मदद से, डेवलपर अपने ऐप्लिकेशन में जगह की जानकारी देने वाली सुविधा को आसानी से शामिल कर सकते हैं. जब किसी उपयोगकर्ता की क्वेरी में Maps के डेटा से जुड़ा कॉन्टेक्स्ट होता है, तो Gemini मॉडल, Google Maps का इस्तेमाल करके तथ्यों पर आधारित और अप-टू-डेट जवाब देता है. ये जवाब, उपयोगकर्ता की बताई गई जगह या जगह की अनुमानित जानकारी के हिसाब से होते हैं.

- **जगह की जानकारी के हिसाब से सटीक जवाब:** भौगोलिक तौर पर खास क्वेरी के लिए, Google Maps के मौजूदा और ज़्यादा डेटा का इस्तेमाल करें.
- **बेहतर तरीके से मनमुताबिक अनुभव देना:** उपयोगकर्ता की बताई गई जगहों के आधार पर, सुझाव और जानकारी दें.

## शुरू करें

इस उदाहरण में, Google Maps से जानकारी लेने की सुविधा को अपने ऐप्लिकेशन में इंटिग्रेट करने का तरीका बताया गया है. इससे उपयोगकर्ता की क्वेरी के सटीक जवाब दिए जा सकते हैं और जगह की जानकारी के हिसाब से जवाब दिए जा सकते हैं. प्रॉम्प्ट में, स्थानीय सुझावों के बारे में पूछा गया है. इसमें उपयोगकर्ता की जगह की जानकारी देने का विकल्प भी है. इससे Gemini मॉडल, Google Maps के डेटा का इस्तेमाल कर सकता है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google Maps से जानकारी लेने की सुविधा कैसे काम करती है

Google Maps से जानकारी लेने की सुविधा, Maps API को सोर्स के तौर पर इस्तेमाल करके, Gemini API को Google Geo इकोसिस्टम के साथ इंटिग्रेट करती है. जब किसी उपयोगकर्ता की क्वेरी में भौगोलिक कॉन्टेक्स्ट होता है, तो Gemini मॉडल, Google Maps से जानकारी लेने की सुविधा को चालू कर सकता है. इसके बाद, मॉडल, दी गई जगह के हिसाब से Google Maps के डेटा के आधार पर जवाब जनरेट कर सकता है.

आम तौर पर, इस प्रोसेस में ये चरण शामिल होते हैं:

1. **उपयोगकर्ता की क्वेरी:** कोई उपयोगकर्ता आपके ऐप्लिकेशन में क्वेरी सबमिट करता है.इसमें भौगोलिक कॉन्टेक्स्ट शामिल हो सकता है. जैसे, "मेरे आस-पास की कॉफ़ी शॉप", "सैन फ़्रांसिस्को में मौजूद म्यूज़ियम".
2. **टूल को चालू करना:** Gemini मॉडल, भौगोलिक इरादे को पहचानकर, Google Maps से जानकारी लेने की सुविधा को चालू करता है. इस टूल को उपयोगकर्ता की `latitude` और `longitude` की जानकारी भी दी जा सकती है. यह टूल, टेक्स्ट के आधार पर खोज करने वाला टूल है और यह Maps पर खोज करने की तरह काम करता है. जैसे, स्थानीय क्वेरी ("मेरे आस-पास") के लिए, निर्देशांकों का इस्तेमाल किया जाएगा. वहीं, खास या गैर-स्थानीय क्वेरी पर, साफ़ तौर पर बताई गई जगह का असर नहीं पड़ेगा.
3. **डेटा वापस पाना:** Google Maps से जानकारी लेने की सुविधा, Google Maps से काम की जानकारी (जैसे, जगहें, समीक्षाएं, फ़ोटो, पते, कारोबार के खुले होने का समय) के लिए क्वेरी करती है.
4. **जानकारी के आधार पर जवाब जनरेट करना:** वापस पाए गए Maps के डेटा का इस्तेमाल, Gemini मॉडल के जवाब के लिए किया जाता है. इससे यह पक्का किया जाता है कि जवाब सटीक और काम का हो.
5. **जवाब और एनोटेशन:** मॉडल, टेक्स्ट में जवाब देता है. इसमें इनलाइन एनोटेशन होते हैं, जो Google Maps के सोर्स से लिंक होते हैं. इससे डेवलपर, सोर्स की जानकारी दिखा सकते हैं.

## Google Maps से जानकारी लेने की सुविधा का इस्तेमाल कब और क्यों करना चाहिए

Google Maps से जानकारी लेने की सुविधा, उन ऐप्लिकेशन के लिए सबसे सही है जिनमें सटीक, अप-टू-डेट, और जगह के हिसाब से जानकारी की ज़रूरत होती है. यह सुविधा, उपयोगकर्ता को काम का और मनमुताबिक कॉन्टेंट देकर, उनके अनुभव को बेहतर बनाती है. यह कॉन्टेंट, Google Maps के दुनिया भर में 25 करोड़ से ज़्यादा जगहों के डेटाबेस पर आधारित होता है.

Google Maps से जानकारी लेने की सुविधा का इस्तेमाल तब करें, जब आपके ऐप्लिकेशन को:

- जगह से जुड़े सवालों के सटीक और पूरे जवाब देने हों.
- बातचीत के ज़रिए ट्रिप प्लानर और स्थानीय गाइड बनाने हों.
- जगह और उपयोगकर्ता की प्राथमिकताओं (जैसे, रेस्टोरेंट या दुकानें) के आधार पर, लोकप्रिय जगहों के सुझाव देने हों.
- सामाजिक, खुदरा या फ़ूड डिलीवरी सेवाओं के लिए, जगह की जानकारी के हिसाब से अनुभव बनाने हों.

Google Maps से जानकारी लेने की सुविधा, उन मामलों में सबसे अच्छी तरह काम करती है जहां आस-पास की जानकारी और मौजूदा सटीक डेटा ज़रूरी होता है. जैसे, "मेरे आस-पास की सबसे अच्छी कॉफ़ी शॉप" ढूंढना या दिशा-निर्देश पाना.

## इस्तेमाल के उदाहरण

Google Maps से जानकारी लेने की सुविधा, जगह की जानकारी के हिसाब से कई तरह के मामलों में काम करती है.

### जगह से जुड़े सवालों के जवाब देना

किसी खास जगह के बारे में ज़्यादा जानकारी वाले सवाल पूछें, ताकि Google पर उपयोगकर्ताओं की समीक्षाओं और Maps के अन्य डेटा के आधार पर जवाब मिल सकें.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### जगह के हिसाब से मनमुताबिक अनुभव देना

उपयोगकर्ता की प्राथमिकताओं और किसी खास इलाके के हिसाब से सुझाव पाएं.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### यात्रा की योजना बनाने में मदद करना

कई दिनों की यात्रा की योजनाएं जनरेट करें. इनमें दिशा-निर्देश और अलग-अलग जगहों के बारे में जानकारी शामिल होती है. यह सुविधा, यात्रा से जुड़े ऐप्लिकेशन के लिए सबसे सही है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## सेवा के इस्तेमाल से जुड़ी ज़रूरी शर्तें

इस सेक्शन में, Google Maps से जानकारी लेने की सुविधा के इस्तेमाल से जुड़ी ज़रूरी शर्तों के बारे में बताया गया है.

### उपयोगकर्ता को Google Maps के सोर्स के इस्तेमाल के बारे में बताना

Google Maps से जानकारी के आधार पर मिले हर नतीजे के साथ, आपको `model_output` चरण के कॉन्टेंट ब्लॉक पर सोर्स के एनोटेशन मिलेंगे. ये एनोटेशन, हर जवाब के साथ दिखते हैं. ये मेटाडेटा दिखाए जाते हैं:

- सोर्स यूआरएल
- नाम

Google Maps से जानकारी लेने की सुविधा से मिले नतीजे दिखाते समय, आपको Google Maps के सोर्स की जानकारी देनी होगी. साथ ही, अपने उपयोगकर्ताओं को यह जानकारी देनी होगी:

- Google Maps के सोर्स, जनरेट किए गए उस कॉन्टेंट के तुरंत बाद दिखने चाहिए जिसके लिए सोर्स की जानकारी दी गई है. जनरेट किए गए इस कॉन्टेंट को, Google Maps से जानकारी के आधार पर मिला नतीजा भी कहा जाता है.
- Google Maps के सोर्स, उपयोगकर्ता के एक इंटरैक्शन में दिखने चाहिए.

### Google Maps के लिंक के साथ, Google Maps के सोर्स दिखाना

सोर्स के हर एनोटेशन के लिए, लिंक का प्रीव्यू जनरेट करना ज़रूरी है. इसके लिए, इन ज़रूरी शर्तों का पालन करें:

- Google Maps के टेक्स्ट
  [एट्रिब्यूशन के दिशा-निर्देशों के मुताबिक, हर सोर्स को Google Maps से एट्रिब्यूट करें.](#maps-attribution-guidelines)
- जवाब में दिए गए सोर्स का नाम दिखाएं.
- एनोटेशन में मौजूद `url` का इस्तेमाल करके, सोर्स से लिंक करें.

### Google Maps के टेक्स्ट एट्रिब्यूशन के दिशा-निर्देश

टेक्स्ट में सोर्स को Google Maps से एट्रिब्यूट करते समय, इन दिशा-निर्देशों का पालन करें:

- Google Maps के टेक्स्ट में किसी भी तरह का बदलाव न करें:
  - Google Maps के केस में बदलाव न करें.
  - Google Maps को कई लाइनों में न दिखाएं.
  - Google Maps को किसी दूसरी भाषा में स्थानीय भाषा में अनुवाद न करें.
  - HTML एट्रिब्यूट translate="no" का इस्तेमाल करके, ब्राउज़र को Google Maps का अनुवाद करने से रोकें.

Google Maps के कुछ डेटा देने वाले पार्टनर और उनकी
लाइसेंस की शर्तों के बारे में ज़्यादा जानकारी के लिए, [Google Maps और Google Earth के कानूनी नोटिस देखें](https://www.google.com/help/legalnotices_maps/?hl=hi).

## सबसे सही तरीके

- **उपयोगकर्ता की जगह की जानकारी देना:** सबसे काम के और मनमुताबिक जवाब पाने के लिए, उपयोगकर्ता की जगह की जानकारी मिलने पर, हमेशा `google_maps` टूल के कॉन्फ़िगरेशन में `latitude` और `longitude` शामिल करें.
- **आखिरी उपयोगकर्ताओं को जानकारी देना:** अपने आखिरी उपयोगकर्ताओं को साफ़ तौर पर बताएं कि उनकी क्वेरी के जवाब देने के लिए, Google Maps के डेटा का इस्तेमाल किया जा रहा है. खास तौर पर, तब जब टूल चालू हो.
- **ज़रूरत न होने पर टॉगल बंद करना:** Google Maps से जानकारी लेने की सुविधा, डिफ़ॉल्ट रूप से बंद होती है. इसे सिर्फ़ तब चालू करें (`"tools": [{"type": "google_maps"}]`) जब किसी क्वेरी में
  भौगोलिक कॉन्टेक्स्ट मौजूद हो. इससे परफ़ॉर्मेंस और लागत को ऑप्टिमाइज़ किया जा सकता है.

## सीमाएं

- फ़िलहाल, Google Maps से जानकारी लेने की सुविधा, सिर्फ़ अंग्रेज़ी भाषा में प्रॉम्प्ट और जवाब देती है.
- ऐसा हो सकता है कि यह टूल सभी देशों/इलाकों में उपलब्ध न हो.
- नतीजे, जगह की सटीक जानकारी और Maps के उपलब्ध डेटा के आधार पर अलग-अलग हो सकते हैं.
- **भौगोलिक दायरा:** Google Maps से जानकारी लेने की सुविधा, दुनिया भर में उपलब्ध है.
- **डिफ़ॉल्ट स्थिति:** Google Maps से जानकारी लेने की सुविधा, डिफ़ॉल्ट रूप से बंद होती है.
  आपको एपीआई के अनुरोधों में इसे साफ़ तौर पर चालू करना होगा.

## कीमत और दर की सीमाएं

Google Maps से जानकारी लेने की सुविधा की कीमत, मॉडल जनरेशन के हिसाब से अलग-अलग होती है:

- **Gemini 3 मॉडल:** आपके प्रोजेक्ट के लिए, **खोज क्वेरी** के हिसाब से बिल भेजा जाता है. यह क्वेरी, मॉडल के ज़रिए एक्ज़ीक्यूट की जाती है. ज़रूरी जानकारी ढूंढने के लिए, मॉडल एक **खोज प्रॉम्प्ट** (मॉडल को भेजा गया आपका एपीआई अनुरोध) के लिए, कई खोज क्वेरी एक्ज़ीक्यूट कर सकता है. इनमें से हर क्वेरी को, टूल के बिल किए जा सकने वाले इस्तेमाल के तौर पर गिना जाता है.
- **Gemini 2.5 और इससे पुराने मॉडल:** आपके प्रोजेक्ट के लिए, **खोज प्रॉम्प्ट** के हिसाब से बिल भेजा जाता है.
  किसी अनुरोध के लिए बिल सिर्फ़ तब भेजा जाता है, जब प्रॉम्प्ट से Google Maps से जानकारी के आधार पर कम से कम एक नतीजा मिलता है. भले ही, उस नतीजे को पाने के लिए मॉडल ने अंदरूनी तौर पर कितनी भी खोज क्वेरी की हों.

कीमत की ज़्यादा जानकारी के लिए, [Gemini API की कीमत वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.

## इस्तेमाल किए जा सकने वाले मॉडल

Google Maps से जानकारी लेने की सुविधा, इन मॉडल के साथ काम करती है:

| मॉडल | Google Maps से जानकारी लेने की सुविधा |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Pro का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## टूल के इस्तेमाल के लिए काम करने वाले कॉम्बिनेशन

Gemini 3 मॉडल, बिल्ट-इन टूल (जैसे, Google Maps से जानकारी लेने की सुविधा) को कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ मिलाकर इस्तेमाल करने की सुविधा देते हैं. ज़्यादा जानने के लिए,
[टूल के कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) वाला पेज देखें.

## आगे क्या करना है

- अन्य [उपलब्ध टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi) के बारे में जानें.
- ज़िम्मेदारी से एआई के इस्तेमाल के सबसे सही तरीकों और Gemini API के सुरक्षा
  फ़िल्टर के बारे में ज़्यादा जानने के लिए, [सुरक्षा सेटिंग के बारे में गाइड देखें](https://ai.google.dev/gemini-api/docs/safety-settings?hl=hi).

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया."],[],[]]
