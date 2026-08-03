---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=hi
fetched_at: 2026-08-03T04:29:28.213690+00:00
title: "\u0932\u0949\u0917 \u0914\u0930 \u0921\u0947\u091f\u093e\u0938\u0947\u091f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# लॉग और डेटासेट

इस गाइड में, आपको यह जानकारी मिलेगी कि Google AI Studio के डैशबोर्ड में, Gemini API के इस्तेमाल से जुड़े लॉग कैसे देखें. इससे आपको मॉडल के व्यवहार और इस बारे में बेहतर जानकारी मिलेगी कि उपयोगकर्ता आपके ऐप्लिकेशन के साथ कैसे इंटरैक्ट कर सकते हैं. लॉगिंग का इस्तेमाल करके, Gemini के इस्तेमाल से जुड़ी समस्याओं को ठीक करें और *Google के साथ इस्तेमाल से जुड़ा सुझाव/राय दें या शिकायत करें. इससे डेवलपर के इस्तेमाल के सभी मामलों में Gemini को बेहतर बनाने में मदद मिलेगी*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=hi)

`GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` एपीआई कॉल और एजेंट बनाने और मैनेज करने की सुविधा को छोड़कर, [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=hi) एपीआई कॉल काम करते हैं. इसमें [OpenAI के साथ काम करने वाले](https://ai.google.dev/gemini-api/docs/openai?hl=hi) एंडपॉइंट के ज़रिए किए गए कॉल शामिल हैं.

## प्रोजेक्ट के लिए लॉगिंग की सुविधा कॉन्फ़िगर करना

डिफ़ॉल्ट रूप से, एपीआई सभी इंटरैक्शन ऑब्जेक्ट (`store=true`) को सेव करता है, ताकि सर्वर-साइड स्टेट मैनेजमेंट की सुविधाओं का इस्तेमाल आसान हो सके. इसके उलट, Generate Content API डिफ़ॉल्ट रूप से अनुरोधों को सेव नहीं करता है. इसके लिए, हर अनुरोध के हिसाब से या प्रोजेक्ट-लेवल पर, AI Studio से स्टोरेज की सुविधा चालू करनी होती है.

Google [AI Studio](https://aistudio.google.com/logs?hl=hi) में, सभी प्रोजेक्ट या कुछ प्रोजेक्ट के लिए लॉगिंग की सुविधा चालू या बंद की जा सकती है. साथ ही, [लॉग और डेटासेट](https://aistudio.google.com/logs?hl=hi) पेज पर मौजूद **सेटिंग** पैनल में जाकर, इन प्राथमिकताओं को कभी भी बदला जा सकता है. किसी प्रोजेक्ट के लिए, स्टोरेज के डिफ़ॉल्ट तरीके को बदलने के लिए, `generateContent` API और [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=hi) API के लिए लॉगिंग को अलग-अलग चालू या बंद किया जा सकता है.

### अनुरोध के लेवल पर लॉगिंग

स्टोरेज और लॉगिंग का तरीका, एपीआई के हिसाब से अलग-अलग होता है:

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi):** यह कुकी, अनुरोधों को डिफ़ॉल्ट रूप से (`store=true`) सेव करती है, ताकि सर्वर-साइड स्टेट मैनेजमेंट को आसान बनाया जा सके.
- **Content API (`generateContent`) जनरेट करता है:** यह डिफ़ॉल्ट रूप से अनुरोधों को सेव नहीं करता (`store=false`).

`store` प्रॉपर्टी को इस तरह सेट किया जा सकता है:

**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## AI Studio में प्रोजेक्ट लॉग देखना

1. [AI Studio](https://aistudio.google.com/logs?hl=hi) में लॉग पेज पर जाएं.
2. ड्रॉप-डाउन से कोई प्रोजेक्ट चुनें.
3. अगर Interactions API के लिए लॉग मौजूद हैं, तो वे टेबल में उल्टे कालानुक्रम में दिखेंगे.
4. Generate Content API के लिए प्रोजेक्ट लॉग देखने के लिए, पहले इसे [सेटिंग पैनल](#configure-logging) में चालू करें.

पेलोड की झलक देखने के लिए, किसी एंट्री पर क्लिक करें. Gemini से मिले जवाब और पूरे प्रॉम्प्ट के साथ-साथ, पिछली बातचीत का कॉन्टेक्स्ट देखा जा सकता है. **Interactions API** के अनुरोधों के लिए, लॉग में `previous_interaction_id` का डायरेक्ट लिंक भी शामिल होता है.

## प्रोजेक्ट के स्टोरेज के लिए डेटा रखरखाव की अवधि कॉन्फ़िगर करना

डिफ़ॉल्ट रूप से, लॉग 55 दिनों तक सेव रहते हैं. इसके बाद, इन्हें मिटाने के लिए मार्क कर दिया जाता है. हालांकि, अगर इन्हें [डेटासेट में सेव किया जाता है](#create), तो ये कभी नहीं मिटते.
किसी प्रोजेक्ट के लॉग के रखरखाव की अवधि को ज़्यादा से ज़्यादा 7, 14, 28 या 55 दिनों के लिए कॉन्फ़िगर किया जा सकता है.

## डेटासेट बनाना और उन्हें शेयर करना

लॉग को डेटासेट में सेव किया जा सकता है, ताकि उन्हें ज़्यादा असरदार तरीके से व्यवस्थित और एक्सपोर्ट किया जा सके.

- [लॉग पेज](https://aistudio.google.com/logs?hl=hi) पर, सबसे ऊपर मौजूद फ़िल्टर बार ढूंढें. इसकी मदद से, फ़िल्टर करने के लिए कोई प्रॉपर्टी चुनें.
- फ़िल्टर किए गए व्यू में, सभी या अलग-अलग लॉग चुनने के लिए चेकबॉक्स का इस्तेमाल करें.
- सूची में सबसे ऊपर मौजूद, **डेटासेट बनाएं** बटन पर क्लिक करें.
- अपने नए डेटासेट को नाम दें और उससे जुड़ी जानकारी दें. हालांकि, जानकारी देना ज़रूरी नहीं है.
- आपको अभी-अभी बनाया गया डेटासेट दिखेगा. इसमें लॉग का चुना गया सेट होगा.
- अपने डेटासेट को CSV, JSONL फ़ाइलों या Google Sheets के तौर पर एक्सपोर्ट करें, ताकि उसका बेहतर तरीके से विश्लेषण किया जा सके.

डेटासेट, कई तरह के कामों के लिए मददगार हो सकते हैं.

- **चैलेंज सेट तैयार करना:** इससे आपको उन क्षेत्रों में आने वाले समय में सुधार करने में मदद मिलेगी जहां आपको एआई को बेहतर बनाना है.
- **सैंपल सेट तैयार करना:** उदाहरण के लिए, किसी अन्य मॉडल से जवाब जनरेट करने के लिए, असली इस्तेमाल का सैंपल या डिप्लॉयमेंट से पहले रूटीन जांच के लिए, कुछ मुश्किल मामलों का कलेक्शन.
- **इवैलुएशन सेट:** ये सेट, अहम क्षमताओं के लिए असली इस्तेमाल को दिखाते हैं. इनका इस्तेमाल, अन्य मॉडल या सिस्टम के निर्देश के वर्शन की तुलना करने के लिए किया जाता है.

Gemini के रिसर्च और डेवलपमेंट में योगदान दिया जा सकता है. इसके लिए, अपने डेटासेट को Google के साथ शेयर करें, ताकि उन्हें उदाहरण के तौर पर दिखाया जा सके.

## सीमाएं

फ़िलहाल, इनके लिए लॉगिंग की सुविधा उपलब्ध नहीं है:

- Imagen और Veo मॉडल
- Gemini के एम्बेडिंग मॉडल
- Gemini Robotics का मॉडल
- वीडियो, GIF या PDF फ़ाइलें शामिल करने वाले इनपुट
- Gemini API में एजेंट की पब्लिक प्रीव्यू सुविधा

## आगे क्या करना है

- **सेशन के इतिहास के साथ प्रोटोटाइप बनाएं:** वाइब कोड वाले ऐप्लिकेशन बनाने के लिए, [AI Studio Build](https://aistudio.google.com/apps?hl=hi) का इस्तेमाल करें. साथ ही, एआई की सुविधाओं के लिए Gemini API के लॉग का इतिहास देखने की सुविधा चालू करने के लिए, अपना एपीआई पासकोड जोड़ें.
- **Gemini Batch API की मदद से लॉग फिर से चलाएं:** जवाब के सैंपल के लिए डेटासेट का इस्तेमाल करें. साथ ही, [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb) की मदद से लॉग फिर से चलाकर, मॉडल या ऐप्लिकेशन लॉजिक का आकलन करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-22 (UTC) को अपडेट किया गया."],[],[]]
