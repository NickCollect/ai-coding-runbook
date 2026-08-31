---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=hi
fetched_at: 2026-08-31T06:37:06.336522+00:00
title: "\u092e\u0940\u0921\u093f\u092f\u093e \u0915\u093e \u0930\u093f\u091c\u093c\u0949\u0932\u094d\u092f\u0942\u0936\u0928 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# मीडिया का रिज़ॉल्यूशन

`media_resolution` पैरामीटर से यह कंट्रोल किया जाता है कि Gemini API, मीडिया इनपुट को कैसे प्रोसेस करता है. जैसे, इमेज, वीडियो, और PDF दस्तावेज़. इसके लिए, यह पैरामीटर मीडिया इनपुट के लिए **ज़्यादा से ज़्यादा टोकन की संख्या** तय करता है. इससे, रिस्पॉन्स की क्वालिटी, इंतज़ार का समय, और लागत के बीच बैलेंस बनाया जा सकता है. अलग-अलग सेटिंग के लिए, डिफ़ॉल्ट वैल्यू और वे टोकन से कैसे जुड़ी हैं, यह जानने के लिए [टोकन की संख्या](#token-counts) सेक्शन देखें.

मीडिया रिज़ॉल्यूशन को दो तरीकों से कॉन्फ़िगर किया जा सकता है:

- [हर हिस्से के लिए](https://ai.google.dev/gemini-api/docs/media-resolution?hl=hi#per-part-media-resolution) (सिर्फ़ Gemini 3)
- [विश्व स्तर पर](https://ai.google.dev/gemini-api/docs/media-resolution?hl=hi#global-media-resolution) पूरे `generateContent` अनुरोध के लिए (सभी मल्टीमॉडल मॉडल)

## हर हिस्से के लिए मीडिया रिज़ॉल्यूशन (सिर्फ़ Gemini 3)

Gemini 3 की मदद से, अनुरोध में शामिल हर मीडिया ऑब्जेक्ट के लिए मीडिया रिज़ॉल्यूशन सेट किया जा सकता है. इससे, टोकन के इस्तेमाल को बेहतर तरीके से ऑप्टिमाइज़ किया जा सकता है. एक ही अनुरोध में, अलग-अलग रिज़ॉल्यूशन लेवल का इस्तेमाल किया जा सकता है. उदाहरण के लिए, किसी जटिल डायग्राम के लिए हाई रिज़ॉल्यूशन और किसी सामान्य कॉन्टेक्चुअल इमेज के लिए लो रिज़ॉल्यूशन का इस्तेमाल किया जा सकता है. यह सेटिंग, किसी खास हिस्से के लिए ग्लोबल कॉन्फ़िगरेशन को ओवरराइड करती है. डिफ़ॉल्ट सेटिंग के लिए, [टोकन की संख्या](https://ai.google.dev/gemini-api/docs/media-resolution?hl=hi#token-counts) सेक्शन देखें.

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## ग्लोबल मीडिया रिज़ॉल्यूशन

`GenerationConfig` का इस्तेमाल करके, किसी अनुरोध में शामिल सभी मीडिया हिस्सों के लिए डिफ़ॉल्ट रिज़ॉल्यूशन सेट किया जा सकता है. यह सुविधा, सभी मल्टीमॉडल मॉडल के साथ काम करती है. अगर किसी अनुरोध
में ग्लोबल और [हर हिस्से के लिए, दोनों तरह की सेटिंग शामिल हैं](https://ai.google.dev/gemini-api/docs/media-resolution?hl=hi#per-part-media-resolution), तो उस खास आइटम के लिए, हर हिस्से के लिए सेट की गई सेटिंग को प्राथमिकता दी जाती है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## उपलब्ध रिज़ॉल्यूशन वैल्यू

Gemini API, मीडिया रिज़ॉल्यूशन के लिए ये लेवल तय करता है:

- `MEDIA_RESOLUTION_UNSPECIFIED`: यह डिफ़ॉल्ट सेटिंग है. इस लेवल के लिए टोकन की गिनती, Gemini 3 और उससे पहले के Gemini मॉडल के बीच काफ़ी अलग-अलग होती है.
- `MEDIA_RESOLUTION_LOW`: इसमें टोकन की गिनती कम होती है. इससे, प्रोसेसिंग की स्पीड बढ़ती है और लागत कम होती है. हालांकि, इसमें कम जानकारी मिलती है.
- `MEDIA_RESOLUTION_MEDIUM`: इसमें जानकारी, लागत, और इंतज़ार के समय के बीच बैलेंस बना रहता है.
- `MEDIA_RESOLUTION_HIGH`: इसमें टोकन की गिनती ज़्यादा होती है. इससे मॉडल को काम करने के लिए ज़्यादा जानकारी मिलती है. हालांकि, इसमें इंतज़ार का समय और लागत बढ़ जाती है.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (सिर्फ़ हर हिस्से के लिए): इसमें टोकन की गिनती सबसे ज़्यादा होती है. यह सेटिंग, इस्तेमाल के कुछ खास उदाहरणों के लिए ज़रूरी होती है. जैसे, [कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi).

ध्यान दें कि `MEDIA_RESOLUTION_HIGH` सेटिंग, ज़्यादातर इस्तेमाल के उदाहरणों के लिए सबसे अच्छी परफ़ॉर्मेंस देती है.

इनमें से हर लेवल के लिए जनरेट होने वाले टोकन की सटीक संख्या, **मीडिया के टाइप** (इमेज, वीडियो, PDF) और **मॉडल के वर्शन**, दोनों पर निर्भर करती है.

## टोकन की संख्या

यहां दी गई टेबल में, मॉडल के हर परिवार के लिए, `media_resolution` की हर वैल्यू और मीडिया के टाइप के हिसाब से, टोकन की अनुमानित संख्या की खास जानकारी दी गई है.

**Gemini 3 मॉडल**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **इमेज** | **वीडियो** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (डिफ़ॉल्ट) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + मौलिक टेक्स्ट |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + मौलिक टेक्स्ट |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + मौलिक टेक्स्ट |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | लागू नहीं | लागू नहीं |

**Gemini 2.5 मॉडल**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **इमेज** | **वीडियो** | **PDF (स्कैन किया गया)** | **PDF (मौलिक)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (डिफ़ॉल्ट) | 256 + पैन और स्कैन (~2048) | 256 | 256 + ओसीआर | 256 + मौलिक टेक्स्ट |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + ओसीआर | 64 + मौलिक टेक्स्ट |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + ओसीआर | 256 + मौलिक टेक्स्ट |
| `MEDIA_RESOLUTION_HIGH` | 256 + पैन और स्कैन | 256 | 256 + ओसीआर | 256 + मौलिक टेक्स्ट |

## सही रिज़ॉल्यूशन चुनना

- **डिफ़ॉल्ट (`UNSPECIFIED`):** डिफ़ॉल्ट सेटिंग से शुरू करें. इसे, इस्तेमाल के ज़्यादातर उदाहरणों के लिए, क्वालिटी, इंतज़ार के समय, और लागत के बीच बेहतर बैलेंस के लिए ऑप्टिमाइज़ किया गया है.
- **`LOW`:** इसका इस्तेमाल उन स्थितियों में करें जहां लागत और इंतज़ार का समय सबसे अहम हो और बारीक जानकारी कम ज़रूरी हो.
- **`MEDIUM` / `HIGH`:** जब टास्क के लिए, मीडिया में मौजूद जटिल जानकारी को समझना ज़रूरी हो, तब रिज़ॉल्यूशन बढ़ाएं. आम तौर पर, इसकी ज़रूरत जटिल विज़ुअल विश्लेषण, चार्ट पढ़ने या ज़्यादा जानकारी वाले दस्तावेज़ को समझने के लिए होती है.
- **`ULTRA HIGH`** - यह सेटिंग सिर्फ़ हर हिस्से के लिए उपलब्ध है. इसका सुझाव, इस्तेमाल के कुछ खास उदाहरणों के लिए दिया जाता है. जैसे, कंप्यूटर का इस्तेमाल या जहां टेस्टिंग से पता चलता है कि `HIGH` के मुकाबले, इसमें साफ़ तौर पर बेहतर नतीजे मिलते हैं.
- **हर हिस्से के लिए कंट्रोल (Gemini 3):** इससे टोकन के इस्तेमाल को ऑप्टिमाइज़ किया जाता है. उदाहरण के लिए, एक ऐसे प्रॉम्प्ट में जिसमें कई इमेज शामिल हैं, किसी जटिल डायग्राम के लिए `HIGH` और सामान्य कॉन्टेक्चुअल इमेज के लिए `LOW` या `MEDIUM` का इस्तेमाल करें.

**सुझाई गई सेटिंग**

यहां, मीडिया के हर टाइप के लिए, मीडिया रिज़ॉल्यूशन की सुझाई गई सेटिंग दी गई हैं.

|  |  |  |  |
| --- | --- | --- | --- |
| **मीडिया का टाइप** | **सुझाई गई सेटिंग** | **ज़्यादा से ज़्यादा टोकन** | **इस्तेमाल करने के लिए दिशा-निर्देश** |
| **इमेज** | `MEDIA_RESOLUTION_HIGH` | 1120 | इमेज के विश्लेषण से जुड़े ज़्यादातर टास्क के लिए, इसका सुझाव दिया जाता है, ताकि सबसे अच्छी क्वालिटी पक्का की जा सके. |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | दस्तावेज़ को समझने के लिए, यह सेटिंग सबसे अच्छी है. आम तौर पर, `medium` सेटिंग पर क्वालिटी सबसे अच्छी होती है. सामान्य दस्तावेज़ों के लिए, `high` सेटिंग पर जाने से ओसीआर के नतीजों में शायद ही कोई सुधार होता है. |
| **वीडियो** (सामान्य) | `MEDIA_RESOLUTION_LOW` (या `MEDIA_RESOLUTION_MEDIUM`) | 70 (हर फ़्रेम के लिए) | **ध्यान दें:** वीडियो के लिए, `low` और `medium` सेटिंग को एक जैसा (70 टोकन) माना जाता है, ताकि कॉन्टेक्स्ट के इस्तेमाल को ऑप्टिमाइज़ किया जा सके. कार्रवाई की पहचान और जानकारी देने से जुड़े ज़्यादातर टास्क के लिए, यह सेटिंग काफ़ी है. |
| **वीडियो** (जिसमें ज़्यादा टेक्स्ट हो) | `MEDIA_RESOLUTION_HIGH` | 280 (हर फ़्रेम के लिए) | इसकी ज़रूरत सिर्फ़ तब होती है, जब इस्तेमाल के उदाहरण में ज़्यादा टेक्स्ट (ओसीआर) या वीडियो फ़्रेम में मौजूद छोटी-छोटी जानकारी को पढ़ना शामिल हो. |

क्वालिटी, इंतज़ार के समय, और लागत के बीच सबसे अच्छा बैलेंस पाने के लिए, अपने ऐप्लिकेशन पर अलग-अलग रिज़ॉल्यूशन सेटिंग की जांच और आकलन करें.

## वर्शन के साथ काम करने वाली सुविधाओं की खास जानकारी

- `MediaResolution` एनम, मीडिया इनपुट की सुविधा वाले सभी मॉडल के लिए उपलब्ध है.
- Gemini 3 मॉडल और Gemini के पुराने वर्शन के लिए, हर एनम लेवल से जुड़े टोकन की संख्या **अलग-अलग** होती है.
- `Part` के अलग-अलग ऑब्जेक्ट पर `media_resolution` सेट करने की सुविधा **सिर्फ़ Gemini 3 मॉडल के लिए उपलब्ध है**.

## अगले चरण

- Gemini API की मल्टीमॉडल क्षमताओं के बारे में ज़्यादा जानने के लिए,
  [इमेज को समझने](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=hi), [वीडियो को समझने](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=hi) और
  [दस्तावेज़ को समझने](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=hi) से जुड़ी गाइड पढ़ें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
