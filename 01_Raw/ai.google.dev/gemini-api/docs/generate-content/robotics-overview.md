---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=hi
fetched_at: 2026-08-31T06:42:54.011709+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Robotics ER

Gemini Robotics ER (embodied reasoning) मॉडल, विज़न-लैंग्वेज मॉडल (वीएलएम) होते हैं. इनकी मदद से रोबोट, असल दुनिया को समझ पाते हैं और उससे इंटरैक्ट कर पाते हैं. ये विज़ुअल डेटा को समझते हैं, स्पेशल और टेंपोरल रीज़निंग करते हैं, कई चरणों वाले टास्क की योजना बनाते हैं, और रोबोट और टूल को व्यवस्थित करते हैं.

## मॉडल

Gemini Robotics ER 2 मॉडल, Gemini Robotics का नया मॉडल है.
यह हमारा अपडेट किया गया रीज़निंग मॉडल है. इसकी मदद से, रोबोट अपने आस-पास के माहौल को सटीक तरीके से समझ पाते हैं. यह एम्बॉडिड रीज़निंग की क्षमताओं में माहिर है. जैसे, रोबोट का एजेंटिक ऑर्केस्ट्रेशन (उदाहरण के लिए, वीएलए का इस्तेमाल करना), रोबोट के वीडियो को समझना, जिसमें प्रोग्रेस को समझना और सफलता का पता लगाना, इंस्ट्रूमेंट पढ़ना, पॉइंट करना, और स्पेशल रीज़निंग शामिल है.

Gemini Robotics ER 2 मॉडल में दो मॉडल एंडपॉइंट शामिल हैं:

- **`gemini-robotics-er-2-preview`**: यह स्टैंडर्ड ER 2 मॉडल है. यह Gemini 3.5 Flash पर आधारित है. इसमें ये सुविधाएं बेहतर की गई हैं: स्पेस के बारे में तर्क देना, वीडियो में खास पल ढूंढना, वीडियो की प्रोग्रेस को कैटगरी में बांटना, एक साथ कई रोबोट को कंट्रोल करना, और एक से ज़्यादा चरणों में टूल का इस्तेमाल करना.
- **`gemini-robotics-er-2-streaming-preview`**: इसे [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) के ज़रिए रीयल-टाइम में स्ट्रीम करने के लिए ऑप्टिमाइज़ किया गया है. इस मॉडल का इस्तेमाल, कम समय में जवाब देने वाले रोबोट एजेंट के लिए करें. यह मॉडल, लगातार ऑडियो और वीडियो इनपुट को प्रोसेस करता है.

अगर Gemini Robotics ER 1.6 का इस्तेमाल किया जा रहा है, तो Gemini Robotics ER 2 पर अपग्रेड करें. इसके लिए, अपने एपीआई कॉल में `model="gemini-robotics-er-1.6-preview"` को `model="gemini-robotics-er-2-preview"` या `model="gemini-robotics-er-2-streaming-preview"` से बदलें. ध्यान दें कि Gemini Robotics ER 1.6 मॉडल को [अगस्त के आखिर में](https://ai.google.dev/gemini-api/docs/deprecations?hl=hi#robotics-models) बंद कर दिया जाएगा.

[Google AI Studio में Gemini Robotics ER 2 को आज़माएँ](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=hi)

## रोबोटिक्स की सुविधाएं

Gemini Robotics ER, कई तरह की एम्बॉडीड रिज़निंग की क्षमताओं के साथ काम करता है.
ज़्यादा जानने के लिए, कोई सुविधा चुनें:

| अनुमति | ब्यौरा | गाइड |
| --- | --- | --- |
| स्पेशल रीज़निंग | ऑब्जेक्ट की ओर इशारा करना, वीडियो में उन्हें ट्रैक करना, बाउंडिंग बॉक्स की मदद से उनकी पहचान करना, और ट्रैजेक्ट्री प्लान करना. | [स्पेशल रीज़निंग](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=hi) |
| एजेंटिक विज़न | इमेज में बदलाव करने वाले टूल का इस्तेमाल करके, अन्य सुविधाओं को बेहतर बनाने के लिए कोड एक्ज़ीक्यूशन का इस्तेमाल करें. | [एजेंटिक विज़न](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=hi) |
| टास्क ऑर्केस्ट्रेशन | लंबी अवधि के टास्क पूरे करने के लिए, स्पेशल रीज़निंग को कस्टम रोबोट एपीआई के साथ मिलाएं. | [टास्क ऑर्केस्ट्रेशन](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=hi) |
| स्ट्रीमिंग (सिर्फ़ Gemini Robotics ER 2 स्ट्रीमिंग एंडपॉइंट) | कम समय में फ़ंक्शन कॉल करने की सुविधा के साथ, रीयल-टाइम में काम करने वाले रोबोट एजेंट के लिए, दोनों दिशाओं में स्ट्रीमिंग की सुविधा. | [रोबोटिक्स के लिए स्ट्रीमिंग](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) |
| वीडियो की प्रोग्रेस (सिर्फ़ Gemini Robotics ER 2 के लिए) | लगातार वीडियो फ़ीड से, मोमेंट ढूंढना और प्रोग्रेस को कैटगरी में बांटना. | [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=hi) |

## शुरू करना

यहां दिए गए उदाहरण में, किसी इमेज में मौजूद ऑब्जेक्ट का पता लगाया गया है. साथ ही, उनके सामान्य किए गए 2D कोऑर्डिनेट और लेबल दिखाए गए हैं. रोबोट की कार्रवाइयां जनरेट करने के लिए, इस आउटपुट को सीधे तौर पर रोबोटिक्स एपीआई या वीएलए मॉडल को पास किया जा सकता है.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

आउटपुट के तौर पर एक JSON कलेक्शन मिलेगा. इसमें ऑब्जेक्ट शामिल होंगे. हर ऑब्जेक्ट में `point` (सामान्य किए गए `[y, x]` कोऑर्डिनेट) और ऑब्जेक्ट की पहचान करने वाला `label` होगा.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

नीचे दी गई इमेज में, इन पॉइंट को दिखाने का तरीका बताया गया है:

![इमेज में मौजूद ऑब्जेक्ट के पॉइंट दिखाने वाला उदाहरण](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=hi)

## यह कैसे काम करता है

Gemini Robotics ER, इमेज, वीडियो या ऑडियो इनपुट लेता है. इसके लिए, नैचुरल लैंग्वेज में प्रॉम्प्ट दिए जाते हैं. यह ऑब्जेक्ट की पहचान करता है, सीन के कॉन्टेक्स्ट और जगह से जुड़े संबंधों के बारे में जानकारी देता है, और स्ट्रक्चर्ड आउटपुट देता है. जैसे, कोऑर्डिनेट या बाउंडिंग बॉक्स.

Gemini Robotics ER भी एजेंटिक है. यह मुश्किल टास्क को छोटे-छोटे टास्क में बाँटता है और उन्हें पूरा करता है. इसके लिए, यह आपके रोबोट के फ़ंक्शन को कॉल करता है या जनरेट किए गए कोड को चलाता है. उदाहरण के लिए, "सेब को कटोरे में रखो" निर्देश को, ढूंढो, पकड़ो, और रखो जैसे चरणों के क्रम में बदल दिया जाता है.

Gemini, टूल कॉल को कैसे पूरा करता है, इस बारे में ज़्यादा जानने के लिए [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=hi#how-it-works) देखें.

## सुरक्षा

Gemini Robotics ER को सुरक्षा को ध्यान में रखकर बनाया गया है. हालांकि, यह आपकी ज़िम्मेदारी है कि आप रोबोट के आस-पास सुरक्षित माहौल बनाए रखें. जनरेटिव एआई मॉडल से गलतियां हो सकती हैं. साथ ही, फ़िज़िकल रोबोट से नुकसान हो सकता है. ज़्यादा जानने के लिए, [Google DeepMind के रोबोटिक्स की सुरक्षा से जुड़े पेज](https://deepmind.google/models/gemini-robotics/safety?hl=hi) पर जाएं.

## सबसे सही तरीके

1. आम बोलचाल की भाषा का इस्तेमाल करें. बताएं कि आपको रोबोट से क्या काम करवाना है. ठीक उसी तरह जैसे किसी व्यक्ति को बताया जाता है. अगर कोई शब्द काम नहीं कर रहा है, तो उसका कोई सामान्य समानार्थी शब्द आज़माएं.
2. विज़ुअल इनपुट को ऑप्टिमाइज़ करें. इमेज भेजने से पहले, छोटे या साफ़ नहीं दिखने वाले ऑब्जेक्ट को काटें या ज़ूम करें. रोशनी और कम कलर कंट्रास्ट से, इंसान की मौजूदगी का पता लगाने की सुविधा पर असर पड़ सकता है.
3. मुश्किल टास्क को चरणों में बांटें. हर चरण को अलग-अलग प्रॉम्प्ट के तौर पर भेजें, ताकि मॉडल का फ़ोकस बना रहे और सटीक जवाब मिल सके.
4. ज़्यादा सटीक जवाब पाने के लिए, एक ही क्वेरी को कई बार करें और मिले हुए जवाबों का औसत निकालें. सहमति के इस तरीके से, जगह की जानकारी से जुड़े आउटपुट में अंतर कम हो जाता है.

## सीमाएं

Gemini Robotics ER का इस्तेमाल करके डेवलपमेंट करते समय, इन सीमाओं का ध्यान रखें:

- **एपीआई पासकोड से जुड़ी पाबंदियां:** Gemini API, बिना पाबंदी वाले एपीआई पासकोड से मिले अनुरोधों को स्वीकार नहीं करता है. साथ ही, `403 Forbidden` गड़बड़ी का मैसेज दिखाता है. [AI Studio](https://aistudio.google.com/api-keys?hl=hi) में पाबंदियां लगाकर, अपनी एपीआई कुंजी को सुरक्षित रखें.
  ज़्यादा जानकारी के लिए, [बिना पाबंदी के इस्तेमाल की अनुमति देने वाली एपीआई कुंजियों को सुरक्षित करना](https://ai.google.dev/gemini-api/docs/api-key?hl=hi#secure-unrestricted-keys) लेख पढ़ें.
- **लेटेंसी बनाम परफ़ॉर्मेंस:** जटिल क्वेरी, हाई रिज़ॉल्यूशन वाले इनपुट या ज़्यादा सोचने की ज़रूरत वाले सवालों को प्रोसेस करने में ज़्यादा समय लग सकता है. सोचने के लेवल के लिए, इंतज़ार के समय और परफ़ॉर्मेंस के बीच बेहतर संतुलन बनाए रखने के लिए, मीडियम का इस्तेमाल करें.
- **मनगढ़ंत जानकारी:** सभी लार्ज लैंग्वेज मॉडल की तरह, Gemini Robotics ER मॉडल कभी-कभी "मनगढ़ंत जानकारी" दे सकते हैं या गलत जानकारी दे सकते हैं. ऐसा खास तौर पर, अस्पष्ट प्रॉम्प्ट या आउट-ऑफ़-डिस्ट्रिब्यूशन इनपुट के लिए होता है.
- **प्रॉम्प्ट की क्वालिटी पर निर्भरता:** आउटपुट की क्वालिटी, इनपुट प्रॉम्प्ट की क्लैरिटी पर निर्भर करती है. सटीक और व्यवस्थित प्रॉम्प्ट का इस्तेमाल करें.
- **कैलकुलेशन की लागत:** मॉडल को चलाने में, खास तौर पर वीडियो इनपुट या ज़्यादा `thinking_budget` के साथ, कैलकुलेशन के संसाधनों का इस्तेमाल होता है और लागत लगती है.
  ज़्यादा जानकारी के लिए, [सोचना](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=hi) पेज देखें.
- **इनपुट टाइप:** हर मोड के लिए तय की गई सीमाओं के बारे में जानने के लिए, यहां दिए गए विषय देखें.
  - [इमेज इनपुट](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=hi#technical-details-image)
  - [वीडियो इनपुट](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=hi#supported-formats)
  - [ऑडियो इनपुट](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=hi#supported-formats)

## निजता नोटिस

आप स्वीकार करते हैं कि इस दस्तावेज़ में बताए गए मॉडल ("रोबोटिक्स मॉडल") को चलाने और आपके निर्देशों के मुताबिक आपके हार्डवेयर को मूव करने के लिए, वीडियो और ऑडियो डेटा का इस्तेमाल किया जाता है. इसलिए, आपके पास रोबोटिक्स मॉडल को इस तरह से चलाने का विकल्प होता है कि वे पहचान ज़ाहिर करने वाली जानकारी इकट्ठा कर सकें. जैसे, आवाज़, इमेज, और मिलती-जुलती जानकारी ("निजी डेटा"). अगर आपने Robotics Models को इस तरह से इस्तेमाल करने का विकल्प चुना है कि वह निजी डेटा इकट्ठा करता है, तो इसका मतलब है कि आपने इस बात पर सहमति दी है कि आप किसी भी ऐसे व्यक्ति को Robotics Models के साथ इंटरैक्ट करने या उसके आस-पास मौजूद रहने की अनुमति नहीं देंगे जिसकी पहचान की जा सकती है. ऐसा तब तक नहीं किया जा सकेगा, जब तक ऐसे व्यक्ति को यह सूचना न दे दी जाए कि उसका निजी डेटा, Gemini API की सेवा की अतिरिक्त शर्तों में बताए गए तरीके से Google को दिया जा सकता है और Google उसका इस्तेमाल कर सकता है. Gemini API की सेवा की अतिरिक्त शर्तें, [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=hi) पर उपलब्ध हैं. इन्हें "शर्तें" कहा जाता है. इसमें "Google आपके डेटा का इस्तेमाल कैसे करता है" सेक्शन में दी गई जानकारी भी शामिल है. आपको यह पक्का करना होगा कि इस तरह की सूचना में, शर्तों में बताए गए तरीके से निजी डेटा को इकट्ठा करने और इस्तेमाल करने की अनुमति दी गई हो. साथ ही, आपको कारोबार के नज़रिए से सही प्रयास करने होंगे, ताकि निजी डेटा को कम से कम इकट्ठा किया जा सके और उसे कम से कम डिस्ट्रिब्यूट किया जा सके. इसके लिए, आपको चेहरे को धुंधला करने जैसी तकनीकों का इस्तेमाल करना होगा. साथ ही, रोबोटिक्स मॉडल को ऐसे इलाकों में ऑपरेट करना होगा जहां लोगों की पहचान ज़ाहिर न हो.

## कीमत

कीमत और उपलब्धता वाले देशों के बारे में ज़्यादा जानने के लिए, [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) पेज पर जाएं.

## मॉडल एंडपॉइंट

### Gemini Robotics ER 2 की झलक

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | `gemini-robotics-er-2-preview` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज, वीडियो, ऑडियो  **आउटपुट**  टेक्स्ट |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  131,072  **आउटपुट टोकन की सीमा**  65,536 |
| handymanसुविधाएँ | **[ऑडियो जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)**  काम नहीं करता है  **[कैश मेमोरी में सेव होना](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**  काम करता है  **[कोड एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**  काम करता है  **[कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)**  काम करता है  **[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**  काम करता है  **[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)**  काम करता है  **[Google Maps की मदद से जवाब तैयार करना](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**  काम करता है  **[इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)**  काम नहीं करता है  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi)**  काम नहीं करता है  **[भरोसेमंद स्रोतों से जानकारी लेना](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)**  काम करता है  **[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)**  काम करता है  **[सोचना](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)**  काम करता है  **[यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**  काम करता है |
| speedकॉन्टेंट देखने के विकल्प | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**  काम करता है  **[फ़्लेक्स अनुमान](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)**  काम नहीं करता है  **[प्राथमिकता का अनुमान लगाना](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)**  काम नहीं करता है |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - झलक देखें: `gemini-robotics-er-2-preview` |
| calendar\_monthनया अपडेट | जुलाई 2026 |
| id\_cardमॉडल कार्ड | [मॉडल कार्ड](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=hi) |

### Gemini Robotics ER 2 की स्ट्रीमिंग की झलक

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | `gemini-robotics-er-2-streaming-preview` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज, वीडियो, ऑडियो  **आउटपुट**  टेक्स्ट |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  131,072  **आउटपुट टोकन की सीमा**  65,536 |
| handymanसुविधाएँ | **[ऑडियो जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)**  काम नहीं करता है  **[कैश मेमोरी में सेव होना](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**  काम नहीं करता है  **[कोड एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**  काम नहीं करता है  **[कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)**  काम नहीं करता है  **[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**  काम नहीं करता है  **[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)**  काम करता है  **[Google Maps की मदद से जवाब तैयार करना](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**  काम नहीं करता है  **[इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)**  काम नहीं करता है  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi)**  काम करता है  **[भरोसेमंद स्रोतों से जानकारी लेना](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)**  काम करता है  **[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)**  काम नहीं करता है  **[सोचना](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)**  काम करता है  **[यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**  काम नहीं करता है |
| speedकॉन्टेंट देखने के विकल्प | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**  काम नहीं करता है  **[फ़्लेक्स अनुमान](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)**  काम नहीं करता है  **[प्राथमिकता का अनुमान लगाना](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)**  काम नहीं करता है |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - झलक देखें: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthनया अपडेट | जुलाई 2026 |
| id\_cardमॉडल कार्ड | [मॉडल कार्ड](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=hi) |

### Gemini Robotics ER 1.6 की झलक

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | `gemini-robotics-er-1.6-preview` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज, वीडियो, ऑडियो  **आउटपुट**  टेक्स्ट |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  131,072  **आउटपुट टोकन की सीमा**  65,536 |
| handymanसुविधाएँ | **[ऑडियो जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)**  काम नहीं करता है  **[कैश मेमोरी में सेव होना](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**  काम करता है  **[कोड एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**  काम करता है  **[कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)**  काम करता है  **[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**  काम करता है  **[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)**  काम करता है  **[Google Maps की मदद से जवाब तैयार करना](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**  काम करता है  **[इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)**  काम नहीं करता है  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi)**  काम नहीं करता है  **[भरोसेमंद स्रोतों से जानकारी लेना](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)**  काम करता है  **[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)**  काम करता है  **[सोचना](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)**  काम करता है  **[यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**  काम करता है |
| speedकॉन्टेंट देखने के विकल्प | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**  काम करता है  **[फ़्लेक्स अनुमान](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)**  काम नहीं करता है  **[प्राथमिकता का अनुमान लगाना](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)**  काम नहीं करता है |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - झलक देखें: `gemini-robotics-er-1.6-preview` |
| calendar\_monthनया अपडेट | दिसंबर 2025 |
| cognition\_2जानकारी उपलब्ध न होना | जनवरी 2025 |

## आगे क्या करना है

- [स्पेशल रीज़निंग](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=hi) — पॉइंट करना, ट्रैक करना, बाउंडिंग बॉक्स, ट्रैजेक्ट्री.
- [एजेंटिक एआई की सुविधाएँ](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=hi) — कोड एक्ज़ीक्यूशन, इंस्ट्रुमेंट को पढ़ना, इमेज की व्याख्या करना.
- [टास्क ऑर्केस्ट्रेशन](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=hi) — कस्टम रोबोट एपीआई के साथ लंबे समय तक चलने वाले टास्क.
- [स्ट्रीमिंग के साथ रोबोटिक्स](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) — रीयल-टाइम में दोनों तरफ़ से स्ट्रीमिंग (सिर्फ़ Gemini Robotics ER 2 के लिए).
- [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=hi) — वीडियो में किसी खास पल को ढूंढना और प्रोग्रेस को कैटगरी में बांटना (सिर्फ़ Gemini Robotics ER 2 के लिए).
- [Google DeepMind की रोबोटिक्स सुरक्षा](https://deepmind.google/models/gemini-robotics/safety?hl=hi) — मॉडल फ़ैमिली के पीछे सुरक्षा से जुड़ा रिसर्च.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
