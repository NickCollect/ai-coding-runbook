---
source_url: https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=hi
fetched_at: 2026-06-29T05:39:14.024997+00:00
title: "Lyria 3 \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0915\u094d\u0932\u093f\u092a \u0915\u0940 \u091d\u0932\u0915 \u0926\u0947\u0916\u0928\u0947 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Lyria 3 की मदद से क्लिप की झलक देखने की सुविधा

Lyria 3 Clip Preview, Google का एक ऐसा मॉडल है जिसे छोटे म्यूज़िकल क्लिप, लूप, और झलक जनरेट करने के लिए ऑप्टिमाइज़ किया गया है. यह टेक्स्ट प्रॉम्प्ट या इमेज इनपुट से, 30 सेकंड का 48kHz स्टीरियो ऑडियो जनरेट करता है. इसकी क्वालिटी बहुत अच्छी होती है.

[Google AI Studio में आज़माएं](https://aistudio.google.com/prompts/new_chat?model=lyria-3-clip-preview&hl=hi)

## दस्तावेज़

सुविधाओं और उनकी उपलब्धता के बारे में पूरी जानकारी पाने के लिए, [संगीत जनरेट करने से जुड़ी](https://ai.google.dev/gemini-api/docs/music-generation?hl=hi) गाइड पर जाएं.

## lyria-3-clip-preview

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | `lyria-3-clip-preview` |
| saveकौन-कौनसे डेटा टाइप इसके साथ काम करते हैं | **इनपुट**  टेक्स्ट और इमेज  **आउटपुट**  ऑडियो (MP3), टेक्स्ट (गाने के बोल) |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  1,31,072 |
| handymanमिलने वाली अनुमतियां | **[ऑडियो जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)**  काम करता है  **[कैश मेमोरी में सेव होना](https://ai.google.dev/gemini-api/docs/caching?hl=hi)**  काम नहीं करता है  **[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)**  काम नहीं करता है  **[फ़ाइल खोजने की सुविधा](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)**  काम नहीं करता है  **[फ़ंक्शन कॉल करने की सुविधा](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi)**  काम नहीं करता है  **[Google Maps की मदद से भरोसेमंद स्रोतों से जानकारी लेने की सुविधा](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)**  काम नहीं करता है  **[इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)**  काम नहीं करता है  **[लाइव एपीआई](https://ai.google.dev/gemini-api/docs/live-api?hl=hi)**  काम नहीं करता है  **[भरोसेमंद स्रोतों से जानकारी लें](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)**  काम नहीं करता है  **[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi)**  काम नहीं करता है  **[प्रोसेस दिखाएं](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)**  काम नहीं करता है  **[यूआरएल के हिसाब से कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)**  काम नहीं करता है |
| speedConsumption विकल्प | **[बैच एपीआई](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)**  काम नहीं करता है  **[Flex अनुमान](https://ai.google.dev/gemini-api/docs/flex-inference?hl=hi)**  काम नहीं करता है  **[प्राथमिकता अनुमान](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi)**  काम नहीं करता है |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल के वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) के बारे में पढ़ें.  - झलक देखें: `lyria-3-clip-preview` - झलक देखें: `lyria-3-pro-preview` |
| calendar\_monthअपडेट की तारीख | मार्च 2026 |

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-23 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-23 (UTC) को अपडेट किया गया."],[],[]]
