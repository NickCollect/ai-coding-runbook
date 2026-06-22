---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=hi
fetched_at: 2026-06-22T06:36:21.235787+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# यूआरएल का कॉन्टेक्स्ट

यूआरएल कॉन्टेक्स्ट टूल की मदद से, मॉडल को यूआरएल के तौर पर ज़्यादा कॉन्टेक्स्ट दिया जा सकता है. अपने अनुरोध में यूआरएल शामिल करके, मॉडल उन पेजों का कॉन्टेंट ऐक्सेस कर पाएगा. हालांकि, ऐसा तब ही होगा, जब वह यूआरएल, [सीमाएं सेक्शन](#limitations) में दिए गए यूआरएल टाइप में शामिल न हो. इससे मॉडल को जवाब देने और उसे बेहतर बनाने में मदद मिलेगी.

यूआरएल कॉन्टेक्स्ट टूल, इन जैसे कामों के लिए मददगार होता है:

- **डेटा निकालना**: एक से ज़्यादा यूआरएल से, कीमत, नाम या मुख्य नतीजे जैसी खास जानकारी पाना.
- **दस्तावेज़ों की तुलना करना**: अंतरों का पता लगाने और रुझानों को ट्रैक करने के लिए, एक से ज़्यादा रिपोर्ट, लेख या PDF का विश्लेषण करें.
- **कॉन्टेंट बनाना और जानकारी इकट्ठा करना**: सटीक जवाब, ब्लॉग पोस्ट या रिपोर्ट जनरेट करने के लिए, अलग-अलग सोर्स यूआरएल से जानकारी इकट्ठा करें.
- **कोड और दस्तावेज़ों का विश्लेषण करना**: कोड के बारे में बताने, सेटअप के निर्देश जनरेट करने या सवालों के जवाब देने के लिए, GitHub रिपॉज़िटरी या तकनीकी दस्तावेज़ की ओर इशारा करें.

यहां दिए गए उदाहरण में, अलग-अलग वेबसाइटों की दो रेसिपी की तुलना करने का तरीका बताया गया है.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## यह कैसे काम करता है

यूआरएल कॉन्टेक्स्ट टूल, डेटा को दो चरणों में इकट्ठा करता है. इससे, तेज़ी से डेटा इकट्ठा करने, कम लागत, और नए डेटा को ऐक्सेस करने के बीच संतुलन बनाए रखने में मदद मिलती है. यूआरएल देने पर, यह टूल सबसे पहले इंटरनल इंडेक्स कैश मेमोरी से कॉन्टेंट फ़ेच करने की कोशिश करता है. यह एक ऑप्टिमाइज़ की गई कैश मेमोरी के तौर पर काम करता है. अगर कोई यूआरएल इंडेक्स में उपलब्ध नहीं है (उदाहरण के लिए, अगर यह बहुत नया पेज है), तो टूल अपने-आप लाइव फ़ेच करने लगता है.
यह सीधे तौर पर यूआरएल को ऐक्सेस करता है, ताकि रीयल टाइम में उसका कॉन्टेंट वापस पाया जा सके.

## अन्य टूल के साथ इस्तेमाल करना

यूआरएल के कॉन्टेक्स्ट की जानकारी देने वाले टूल को अन्य टूल के साथ मिलाकर, ज़्यादा बेहतर वर्कफ़्लो बनाए जा सकते हैं.

[Gemini 3 मॉडल](#supported-models), कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ-साथ, बिल्ट-इन टूल (जैसे, यूआरएल कॉन्टेक्स्ट) को एक साथ इस्तेमाल करने की सुविधा देते हैं. [टूल के कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पेज पर जाकर, इस बारे में ज़्यादा जानें.

### खोज के नतीजों से जानकारी पाना

यूआरएल कॉन्टेक्स्ट और [Google Search से जानकारी पाना](https://ai.google.dev/gemini-api/docs/grounding?hl=hi), दोनों चालू होने पर मॉडल, खोज से जुड़ी सुविधाओं का इस्तेमाल करके ऑनलाइन काम की जानकारी ढूंढ सकता है. इसके बाद, यूआरएल कॉन्टेक्स्ट टूल का इस्तेमाल करके, खोजे गए पेजों के बारे में ज़्यादा जानकारी पा सकता है. यह तरीका उन प्रॉम्प्ट के लिए बहुत कारगर है जिनमें व्यापक खोज और खास पेजों का बारीकी से विश्लेषण, दोनों की ज़रूरत होती है.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## जवाब को समझना

जब मॉडल, यूआरएल कॉन्टेक्स्ट टूल का इस्तेमाल करता है, तो जवाब में `url_context_metadata` ऑब्जेक्ट शामिल होता है. इस ऑब्जेक्ट में उन यूआरएल की सूची होती है जिनसे मॉडल ने कॉन्टेंट को फिर से हासिल किया है. साथ ही, इसमें हर यूआरएल से कॉन्टेंट को फिर से हासिल करने की कोशिश का स्टेटस भी होता है. यह ऑब्जेक्ट, पुष्टि करने और डीबग करने के लिए काम का होता है.

यहां जवाब के उस हिस्से का उदाहरण दिया गया है. जवाब के कुछ हिस्सों को छोटा करने के लिए हटाया गया है:

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

इस ऑब्जेक्ट के बारे में पूरी जानकारी के लिए , [`UrlContextMetadata` एपीआई के बारे में जानकारी](https://ai.google.dev/api/generate-content?hl=hi#UrlContextMetadata) देखें.

### सुरक्षा जांच

सिस्टम, यूआरएल पर कॉन्टेंट मॉडरेशन की जांच करता है. इससे यह पुष्टि की जाती है कि यूआरएल, सुरक्षा मानकों के मुताबिक है. अगर आपके दिए गए यूआरएल की पुष्टि नहीं हो पाती है, तो आपको `url_retrieval_status` में से `URL_RETRIEVAL_STATUS_UNSAFE` मिलेगा.

### टोकन की संख्या

आपके प्रॉम्प्ट में दिए गए यूआरएल से हासिल किए गए कॉन्टेंट को, इनपुट टोकन के तौर पर गिना जाता है. आपको मॉडल के आउटपुट के [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=hi#UsageMetadata) ऑब्जेक्ट में, अपने प्रॉम्प्ट और टूल के इस्तेमाल के लिए टोकन की संख्या दिख सकती है. यहां आउटपुट का एक उदाहरण दिया गया है:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

हर टोकन की कीमत, इस्तेमाल किए गए मॉडल पर निर्भर करती है. ज़्यादा जानकारी के लिए, [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) वाला पेज देखें.

## इन मॉडल के साथ काम करता है

| मॉडल | यूआरएल का कॉन्टेक्स्ट |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## सबसे सही तरीके

- **खास यूआरएल दें**: बेहतर नतीजे पाने के लिए, उस कॉन्टेंट के डायरेक्ट यूआरएल दें जिसका विश्लेषण आपको मॉडल से कराना है. मॉडल सिर्फ़ आपके दिए गए यूआरएल से कॉन्टेंट हासिल करेगा. वह नेस्ट किए गए लिंक से कोई कॉन्टेंट हासिल नहीं करेगा.
- **पक्का करें कि यूआरएल ऐक्सेस किए जा सकते हों**: पुष्टि करें कि आपके दिए गए यूआरएल, ऐसे पेजों पर रीडायरेक्ट न करते हों जिन्हें ऐक्सेस करने के लिए लॉग इन करने या पैसे चुकाने की ज़रूरत होती है.
- **पूरा यूआरएल इस्तेमाल करें**: पूरा यूआरएल दें. इसमें प्रोटोकॉल भी शामिल होना चाहिए
  (जैसे, सिर्फ़ google.com के बजाय https://www.google.com).

## सीमाएं

- फ़ंक्शन कॉलिंग: फ़िलहाल, फ़ंक्शन कॉलिंग के साथ टूल इस्तेमाल करने की सुविधा काम नहीं करती. जैसे, यूआरएल कॉन्टेक्स्ट, Google Search के साथ ग्राउंडिंग वगैरह.
- अनुरोध की सीमा: यह टूल, हर अनुरोध में ज़्यादा से ज़्यादा 20 यूआरएल प्रोसेस कर सकता है.
- यूआरएल के कॉन्टेंट का साइज़: किसी एक यूआरएल से लिए गए कॉन्टेंट का साइज़ 34 एमबी से ज़्यादा नहीं होना चाहिए.
- सार्वजनिक तौर पर ऐक्सेस किया जा सकने वाला यूआरएल: यूआरएल ऐसे होने चाहिए जिन्हें वेब पर सार्वजनिक तौर पर ऐक्सेस किया जा सके.
  लोकलहोस्ट पते (जैसे, localhost, 127.0.0.1), निजी नेटवर्क, और टनलिंग सेवाएं (जैसे, ngrok, pinggy) काम नहीं करती हैं.
- सिर्फ़ Gemini API के लिए: यूआरएल कॉन्टेक्स्ट की सुविधा सिर्फ़ Gemini API में उपलब्ध है. यह Gemini Enterprise Agent Platform के ज़रिए उपलब्ध नहीं है.

### इस्तेमाल किए जा सकने वाले और इस्तेमाल न किए जा सकने वाले कॉन्टेंट टाइप

यह टूल, इन तरह के कॉन्टेंट वाले यूआरएल से कॉन्टेंट निकाल सकता है:

- टेक्स्ट (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- इमेज (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

इस तरह के कॉन्टेंट के लिए, यह सुविधा **काम नहीं करती**:

- Paywall की गई सामग्री
- YouTube वीडियो (YouTube यूआरएल प्रोसेस करने का तरीका जानने के लिए, [वीडियो समझने की सुविधा](https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi#youtube) देखें)
- Google Workspace की फ़ाइलें, जैसे कि Google Docs या स्प्रेडशीट
- वीडियो और ऑडियो फ़ाइलें

## आगे क्या करना है

- ज़्यादा उदाहरणों के लिए, [यूआरएल कॉन्टेक्स्ट कुकबुक](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=hi#url-context) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया."],[],[]]
