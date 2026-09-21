---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=hi
fetched_at: 2026-09-21T05:44:42.910708+00:00
title: "Gemini Robotics ER 2 \u0915\u0940 \u0938\u094d\u091f\u094d\u0930\u0940\u092e\u093f\u0902\u0917 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Robotics ER 2 की स्ट्रीमिंग

Gemini Robotics ER 2 Streaming, रोबोटिक्स के लिए विज़न-लैंग्वेज मॉडल (वीएलएम) है. इसे Live API का इस्तेमाल करके, रीयल-टाइम में टेक्स्ट स्ट्रीमिंग के लिए ऑप्टिमाइज़ किया गया है. यह टेक्स्ट, इमेज, वीडियो, और ऑडियो इनपुट स्वीकार करता है. साथ ही, फ़ंक्शन कॉलिंग के साथ-साथ दोनों दिशाओं में स्ट्रीमिंग की सुविधा देता है.

[Google AI Studio में आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=hi)

## दस्तावेज़

सुविधाओं और क्षमताओं के बारे में पूरी जानकारी पाने के लिए, [रोबोटिक्स के लिए Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) पेज पर जाएं.

## gemini-robotics-er-2-streaming-preview

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

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-08-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-08-19 (UTC) को अपडेट किया गया."],[],[]]
