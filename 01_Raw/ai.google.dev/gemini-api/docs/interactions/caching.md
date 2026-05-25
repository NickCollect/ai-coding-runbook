---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=hi
fetched_at: 2026-05-25T05:18:07.296318+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# कॉन्टेक्स्ट को कैश में सेव करना

एआई के सामान्य वर्कफ़्लो में, किसी मॉडल को एक ही इनपुट टोकन बार-बार पास किया जा सकता है. Gemini API, परफ़ॉर्मेंस और लागत को ऑप्टिमाइज़ करने के लिए, इंप्लिसिट कैशिंग की सुविधा देता है.

## इंप्लिसिट कैशिंग

Gemini 2.5 और इसके बाद के सभी मॉडल के लिए, इंप्लिसिट कैशिंग की सुविधा डिफ़ॉल्ट रूप से चालू होती है. अगर आपका अनुरोध कैश से मैच होता है, तो हम लागत में होने वाली बचत को अपने-आप पास कर देते हैं. इसे चालू करने के लिए, आपको कुछ भी करने की ज़रूरत नहीं है. कॉन्टेक्स्ट कैशिंग के लिए, हर मॉडल के लिए इनपुट टोकन की कम से कम संख्या यहां दी गई है:

| मॉडल | टोकन की कम से कम सीमा |
| --- | --- |
| Gemini 3.5 Flash | 1024 |
| Gemini 3 Pro की झलक | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

इंप्लिसिट कैश हिट होने की संभावना बढ़ाने के लिए:

- अपने प्रॉम्प्ट की शुरुआत में, बड़ा और सामान्य कॉन्टेंट शामिल करें
- कम समय में, एक जैसे प्रीफ़िक्स वाले अनुरोध भेजने की कोशिश करें

रिस्पॉन्स ऑब्जेक्ट के `usage_metadata` (Python) या `usageMetadata` (JavaScript) फ़ील्ड में, कैश हिट होने वाले टोकन की संख्या देखी जा सकती है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-19 (UTC) को अपडेट किया गया."],[],[]]
