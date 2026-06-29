---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=hi
fetched_at: 2026-06-29T05:29:27.680536+00:00
title: "Google AI Studio \u0938\u0947 \u0921\u093f\u092a\u094d\u0932\u0949\u092f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Google AI Studio से डिप्लॉय करना

Google AI Studio की मदद से, फ़ुल-स्टैक ऐप्लिकेशन को सीधे तौर पर बिल्ड मोड से डिप्लॉय किया जा सकता है. इससे प्रोटोटाइप से लेकर मैनेज किए जा सकने वाले और बड़े पैमाने पर इस्तेमाल किए जा सकने वाले प्रोडक्शन एनवायरमेंट तक तेज़ी से पहुंचा जा सकता है.

## डिप्लॉयमेंट के विकल्प

AI Studio के बिल्ड मोड से ऐप्लिकेशन डिप्लॉय करने के लिए, ज़रूरी शर्तें इस बात पर निर्भर करती हैं कि आपने कौनसी सदस्यता ली है:

- [**Google Cloud का स्टार्टर टियर**](https://docs.cloud.google.com/docs/starter-tier?hl=hi):
  इसकी मदद से, Google Cloud प्रोजेक्ट या बिलिंग खाता सेट अप किए बिना, ज़्यादा से ज़्यादा दो फ़ुल-स्टैक ऐप्लिकेशन पब्लिश किए जा सकते हैं.
- **स्टैंडर्ड डिप्लॉयमेंट**: इसके लिए, आपके AI Studio खाते से लिंक किया गया Google Cloud प्रोजेक्ट होना चाहिए. साथ ही, उस प्रोजेक्ट पर बिलिंग की सुविधा चालू होनी चाहिए.

## Starter टियर के बारे में जानकारी

Google Cloud के स्टार्टर टियर की मदद से, Google AI Studio से सीधे Google Cloud पर ऐप्लिकेशन डिप्लॉय किए जा सकते हैं. इसके लिए, आपको Google Cloud का पूरा एनवायरमेंट या बिलिंग खाता सेट अप करने की ज़रूरत नहीं होती.

Google AI Studio में हर डिप्लॉयमेंट, Cloud Run में एक सेवा बनाता है. Google AI Studio में स्टार्टर टियर के साथ डिप्लॉय की गई सेवाओं पर, ये सीमाएं लागू होती हैं:

- ज़्यादा से ज़्यादा दो सेवाएं डिप्लॉय की जा सकती हैं.
- आपकी सेवाएं, [Cloud Run के एक ही क्षेत्र](https://docs.cloud.google.com/run/docs/locations?hl=hi) में डिप्लॉय की गई हों.

## Starter Tier को डिप्लॉय करने का तरीका

बिल्ड मोड में ऐप्लिकेशन डिज़ाइन करने के बाद, उसे स्टार्टर टियर के साथ डिप्लॉय करें:

1. सबसे ऊपर दाएं कोने में मौजूद, **पब्लिश करें** बटन पर क्लिक करें.
2. **शुरू करें** पर क्लिक करें.
3. **ऐप्लिकेशन पब्लिश करें** पर क्लिक करें.

डिप्लॉयमेंट पूरा होने के बाद, AI Studio एक Cloud Run यूआरएल देता है. इस यूआरएल से, लाइव ऐप्लिकेशन को ऐक्सेस किया जा सकता है.

## स्टैंडर्ड डिप्लॉयमेंट

आपके ऐप्लिकेशन के बेहतर होने के साथ-साथ, आपको स्टार्टर टियर से ज़्यादा सुविधाओं की ज़रूरत पड़ सकती है. जैसे, ज़्यादा कोटा, ज़्यादा कंप्यूट संसाधन या Google Cloud के ऐसे अन्य प्रॉडक्ट जो स्टार्टर टियर में उपलब्ध नहीं हैं. इन सुविधाओं को अनलॉक करने के लिए, पूरी तरह से मैनेज किए जाने वाले Starter Tier प्रोजेक्ट को स्टैंडर्ड Google क्लाउड प्रोजेक्ट में बदला जा सकता है.

इससे यह पक्का होता है कि आपकी प्रोग्रेस में कोई रुकावट नहीं आएगी. [Cloud Billing खाता बनाने](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=hi#create-new-billing-account), Google Cloud की सेवा की मानक शर्तों को औपचारिक तौर पर स्वीकार करने, और [Google Cloud के स्टैंडर्ड प्रोजेक्ट पर अपग्रेड करने](https://docs.cloud.google.com/docs/starter-tier?hl=hi#upgradee) के लिए, यह तरीका अपनाएं. ज़्यादा जानकारी के लिए, [पैसे चुकाकर इस्तेमाल किए जाने वाले खातों का सेटअप](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=hi#paid-setup) देखें.

बिलिंग टियर के बारे में ज़्यादा जानने के लिए, [बिलिंग](https://ai.google.dev/gemini-api/docs/billing?hl=hi) पर जाएं.

## अपना आवेदन मिटाना

अगर आपको अब अपने ऐप्लिकेशन की ज़रूरत नहीं है, तो Google AI Studio में जाकर इसे मिटाया जा सकता है. इसके लिए, यह तरीका अपनाएं:

1. Google AI Studio में, अपने [ऐप्लिकेशन पेज](https://aistudio.google.com/app/apps?hl=hi) पर जाएं.
2. बाईं ओर मौजूद मेन्यू में जाकर, **ऐप्लिकेशन** को चुनें.
3. जिस ऐप्लिकेशन को मिटाना है उस पर पॉइंटर घुमाएं.
4. ऐप्लिकेशन को मिटाने के लिए, लाइन की दाईं ओर मौजूद ट्रैश कैन आइकॉन पर क्लिक करें.

## आगे क्या करना है

- [Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier?hl=hi) के बारे में ज़्यादा जानें.
- Gemini API में [बिलिंग](https://ai.google.dev/gemini-api/docs/billing?hl=hi) के बारे में पढ़ें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-16 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-16 (UTC) को अपडेट किया गया."],[],[]]
