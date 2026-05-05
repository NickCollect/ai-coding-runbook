---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=hi
fetched_at: 2026-05-05T13:26:12.981378+00:00
title: "Gemini Developer API \u092c\u0928\u093e\u092e Gemini Enterprise Agent Platform \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/Gemini की Deep Research की सुविधा) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

- [होम पेज](https://ai.google.dev/gemini-api/docs/होम पेज)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Docs](https://ai.google.dev/gemini-api/docs/Docs)

सुझाव भेजें

# Gemini Developer API बनाम Gemini Enterprise Agent Platform

Gemini की मदद से जनरेटिव एआई के समाधान तैयार करते समय, Google दो एपीआई प्रॉडक्ट उपलब्ध कराता है:
[Gemini Developer API](https://ai.google.dev/gemini-api/docs/Gemini Developer API) और [Gemini Enterprise Agent Platform API](https://ai.google.dev/gemini-api/docs/Gemini Enterprise Agent Platform API).

Gemini Developer API की मदद से, Gemini की सुविधाओं वाले ऐप्लिकेशन को तेज़ी से बनाया, प्रोडक्शन में लाया, और स्केल किया जा सकता है. ज़्यादातर डेवलपर को Gemini Developer API का इस्तेमाल करना चाहिए. हालांकि, अगर एंटरप्राइज़ के लिए खास कंट्रोल की ज़रूरत हो, तो वे Gemini Enterprise API का इस्तेमाल कर सकते हैं.

Gemini Enterprise Agent Platform, एंटरप्राइज़ के लिए तैयार सुविधाओं और सेवाओं का एक पूरा इकोसिस्टम उपलब्ध कराता है. इसकी मदद से, Google Cloud Platform पर जनरेटिव एआई ऐप्लिकेशन बनाए और डिप्लॉय किए जा सकते हैं.

हमने हाल ही में, इन सेवाओं के बीच माइग्रेट करने की प्रोसेस को आसान बनाया है. Gemini Developer API और Gemini Enterprise Agent Platform API, दोनों को अब [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/Google Gen AI SDK) के ज़रिए ऐक्सेस किया जा सकता है.

## कोड की तुलना करना

इस पेज पर, टेक्स्ट जनरेट करने के लिए Gemini Developer API और Gemini Enterprise Agent Platform की क्विकस्टार्ट गाइड के कोड की तुलना की गई है.

### Python

Gemini Developer API और Gemini Enterprise Agent Platform, दोनों की सेवाओं को `google-genai` लाइब्रेरी के ज़रिए ऐक्सेस किया जा सकता है. `google-genai` को इंस्टॉल करने का तरीका जानने के लिए, [लाइब्रेरी](https://ai.google.dev/gemini-api/docs/लाइब्रेरी) पेज पर जाएं.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript और TypeScript

Gemini Developer API और Gemini Enterprise Agent Platform, दोनों की सेवाओं को `@google/genai` लाइब्रेरी के ज़रिए ऐक्सेस किया जा सकता है. `@google/genai` को इंस्टॉल करने का तरीका जानने के लिए, [लाइब्रेरी](https://ai.google.dev/gemini-api/docs/लाइब्रेरी) पेज देखें.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### ऐप पर जाएं

Gemini Developer API और Gemini Enterprise Agent Platform, दोनों की सेवाओं को `google.golang.org/genai` लाइब्रेरी के ज़रिए ऐक्सेस किया जा सकता है. `google.golang.org/genai` को इंस्टॉल करने का तरीका जानने के लिए, [लाइब्रेरी](https://ai.google.dev/gemini-api/docs/लाइब्रेरी) पेज देखें.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### इस्तेमाल के अन्य उदाहरण और प्लैटफ़ॉर्म

अन्य प्लैटफ़ॉर्म और इस्तेमाल के उदाहरणों के लिए, [Gemini Developer API के दस्तावेज़](https://ai.google.dev/gemini-api/docs/Gemini Developer API के दस्तावेज़) और [Gemini Enterprise एजेंट प्लैटफ़ॉर्म के दस्तावेज़](https://ai.google.dev/gemini-api/docs/Gemini Enterprise एजेंट प्लैटफ़ॉर्म के दस्तावेज़) में, इस्तेमाल के उदाहरणों से जुड़ी गाइड देखें.

## माइग्रेशन से जुड़ी ज़रूरी बातें

माइग्रेट करने पर:

- पुष्टि करने के लिए, आपको Google Cloud सेवा खातों का इस्तेमाल करना होगा. ज़्यादा जानकारी के लिए, [Gemini Enterprise Agent Platform का दस्तावेज़](https://ai.google.dev/gemini-api/docs/Gemini Enterprise Agent Platform का दस्तावेज़) देखें.
- अपने मौजूदा Google Cloud प्रोजेक्ट का इस्तेमाल किया जा सकता है. यह वही प्रोजेक्ट होना चाहिए जिसका इस्तेमाल आपने एपीआई पासकोड जनरेट करने के लिए किया था. इसके अलावा, [नया Google Cloud प्रोजेक्ट बनाया](https://ai.google.dev/gemini-api/docs/नया Google Cloud प्रोजेक्ट बनाया) जा सकता है.
- Gemini Developer API और Gemini Enterprise Agent Platform API के लिए, उपलब्ध क्षेत्रों में अंतर हो सकता है. [Google Cloud पर जनरेटिव एआई की सुविधा के लिए, उपलब्ध देशों/इलाकों की सूची](https://ai.google.dev/gemini-api/docs/Google Cloud पर जनरेटिव एआई की सुविधा के लिए, उपलब्ध देशों/इलाकों की सूची) देखें.
- Google AI Studio में बनाए गए सभी मॉडल को Gemini Enterprise Agent Platform में फिर से ट्रेन करना होगा.

अगर आपको Gemini Developer API के लिए, Gemini API पासकोड का इस्तेमाल नहीं करना है, तो सुरक्षा के सबसे सही तरीके अपनाएं और इसे मिटाएं.

किसी एपीआई पासकोड को मिटाने के लिए:

1. [Google Cloud API के क्रेडेंशियल](https://ai.google.dev/gemini-api/docs/Google Cloud API के क्रेडेंशियल) पेज खोलें.
2. वह एपीआई पासकोड ढूंढें जिसे आपको मिटाना है. इसके बाद, **कार्रवाइयां** आइकॉन पर क्लिक करें.
3. **एपीआई पासकोड मिटाएं** को चुनें.
4. **क्रेडेंशियल मिटाएं** मोडल में जाकर, **मिटाएं** को चुनें.

   एपीआई पासकोड को हटाने में कुछ मिनट लगते हैं. प्रॉपगेशन पूरा होने के बाद, मिटाई गई एपीआई कुंजी का इस्तेमाल करने वाले किसी भी ट्रैफ़िक को अस्वीकार कर दिया जाता है.

## अगले चरण

- Gemini Enterprise Agent Platform पर जनरेटिव एआई के समाधानों के बारे में ज़्यादा जानने के लिए, [Gemini Enterprise Agent Platform पर जनरेटिव एआई की खास जानकारी](https://ai.google.dev/gemini-api/docs/Gemini Enterprise Agent Platform पर जनरेटिव एआई की खास जानकारी) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0 License) के तहत और कोड के नमूनों को [Apache 2.0 License](https://ai.google.dev/gemini-api/docs/Apache 2.0 License) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://ai.google.dev/gemini-api/docs/Google Developers साइट नीतियां) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?
