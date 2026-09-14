---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=hi
fetched_at: 2026-09-14T05:54:42.007435+00:00
title: "Gemini Live API \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u0916\u093e\u0938 \u091c\u093e\u0928\u0915\u093e\u0930\u0940 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Live API के बारे में खास जानकारी

Live API की मदद से, Gemini के साथ कम समय में रीयल-टाइम में आवाज़ और विज़न से जुड़ी बातचीत की जा सकती है. यह ऑडियो, इमेज, और टेक्स्ट की लगातार स्ट्रीम को प्रोसेस करता है, ताकि आपको तुरंत और इंसानों जैसी आवाज़ में जवाब मिल सकें. इससे आपके उपयोगकर्ताओं को बातचीत का नैचुरल अनुभव मिलता है.

![Live API के बारे में खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=hi)

[Google AI Studio में Live API आज़माएंmic](https://aistudio.google.com/live?hl=hi)
[GitHub से उदाहरण ऐप्लिकेशन क्लोन करेंcode](https://github.com/google-gemini/gemini-live-api-examples)
[कोडिंग एजेंट की क्षमताओं का इस्तेमाल करेंterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi)

## उपयोग के उदाहरण

लाइव एपीआई का इस्तेमाल, कई तरह के उद्योगों के लिए रीयल-टाइम में वॉइस एजेंट बनाने के लिए किया जा सकता है. जैसे:

- **ई-कॉमर्स और खुदरा कारोबार:** शॉपिंग असिस्टेंट, लोगों की दिलचस्पी के हिसाब से सुझाव देती हैं. साथ ही, सहायता एजेंट खरीदारों की समस्याओं को हल करते हैं.
- **गेमिंग:** इंटरैक्टिव नॉन-प्लेयर कैरेक्टर (एनपीसी), गेम में मदद करने वाले असिस्टेंट, और गेम में मौजूद कॉन्टेंट का रीयल-टाइम में अनुवाद.
- **नेक्स्ट जनरेशन इंटरफ़ेस:** रोबोटिक्स, स्मार्ट ग्लास, और वाहनों में आवाज़ और वीडियो की सुविधा वाले अनुभव.
- **स्वास्थ्य सेवा:** मरीज़ों की मदद करने और उन्हें जानकारी देने के लिए स्वास्थ्य से जुड़े कंपैनियन.
- **वित्तीय सेवाएं:** वेल्थ मैनेजमेंट और निवेश से जुड़ी सलाह देने के लिए एआई सलाहकार.
- **शिक्षा:** एआई मेंटर और सीखने वाले लोगों के साथी, जो उनके हिसाब से निर्देश और सुझाव देते हैं.
- **अनुवाद और स्थानीयकरण:** बोली गई बातचीत का रीयल-टाइम में और कम समय में अनुवाद किया जा सकता है. इससे अलग-अलग भाषाओं में आसानी से बातचीत की जा सकती है.
- **लाइव ट्रांसक्रिप्शन और कैप्शन:** रीयल-टाइम में बोले गए शब्दों को लेख में बदलकर कैप्शन बनाने की सुविधा. इसका इस्तेमाल लाइव सबटाइटल, मीटिंग ट्रांसक्रिप्शन, बोलकर टाइप करने, और ग्राहक की कॉल लॉग करने के लिए किया जा सकता है.

## मुख्य सुविधाएं

Live API में, आवाज़ से काम करने वाले एजेंट बनाने के लिए कई तरह की सुविधाएँ उपलब्ध हैं:

- [**कई भाषाओं में बातचीत करने की सुविधा**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#supported-languages):
  70 भाषाओं में बातचीत करें.
- [**बार्ज-इन**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#interruptions):
  उपयोगकर्ता, जवाब देने के लिए मॉडल को किसी भी समय बाधित कर सकते हैं.
- [**टूल का इस्तेमाल करना**](https://ai.google.dev/gemini-api/docs/live-tools?hl=hi):
  इसमें डाइनैमिक इंटरैक्शन के लिए, फ़ंक्शन कॉलिंग और Google Search जैसे टूल इंटिग्रेट किए जाते हैं.
- [**ऑडियो ट्रांसक्रिप्ट**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#audio-transcription):
  इसमें उपयोगकर्ता के इनपुट और मॉडल आउटपुट, दोनों की टेक्स्ट ट्रांसक्रिप्ट मिलती है.
- [**पहले से ही ऑडियो जनरेट करने की सुविधा**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#proactive-audio):
  इस सुविधा की मदद से, यह कंट्रोल किया जा सकता है कि मॉडल कब और किन संदर्भों में जवाब दे.
- [**अफ़ेक्टिव डायलॉग**](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi#affective-dialog):
  जवाब देने की स्टाइल और टोन को, उपयोगकर्ता के इनपुट एक्सप्रेशन के हिसाब से बदला जाता है.
- [**लाइव ट्रांसक्रिप्शन**](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=hi):
  यह सुविधा, बोली को रीयल-टाइम में लगातार लिखाई में बदलती है. इसमें भाषा की अपने-आप पहचान होने की सुविधा और कस्टम शब्दावली शामिल है.
- [**लाइव ट्रांसलेशन**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=hi):
  70 से ज़्यादा भाषाओं में, बोले जा रहे शब्दों का रीयल-टाइम में अनुवाद.

## तकनीकी जानकारी

यहां दी गई टेबल में, Live API की तकनीकी खास जानकारी दी गई है:

| कैटगरी | विवरण |
| --- | --- |
| इनपुट के तरीके | ऑडियो (रॉ 16-बिट पीसीएम ऑडियो, 16 किलोहर्ट्ज़, लिटिल-एंडियन), इमेज (JPEG <= 1 एफ़पीएस), टेक्स्ट |
| आउटपुट के तरीके | ऑडियो (रॉ 16-बिट पीसीएम ऑडियो, 24 किलोहर्ट्ज़, लिटिल-एंडियन) |
| प्रोटोकॉल | स्टेटफ़ुल WebSocket कनेक्शन (WSS) |

## लागू करने का तरीका चुनना

Live API के साथ इंटिग्रेट करते समय, आपको लागू करने के लिए इनमें से कोई एक तरीका चुनना होगा:

- **सर्वर-टू-सर्वर**: आपका बैकएंड, [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) का इस्तेमाल करके Live API से कनेक्ट होता है. आम तौर पर, आपका क्लाइंट स्ट्रीम डेटा (ऑडियो, वीडियो, टेक्स्ट) को आपके सर्वर पर भेजता है. इसके बाद, सर्वर इसे Live API को भेजता है.
- **क्लाइंट-टू-सर्वर**: आपका फ़्रंटएंड कोड, डेटा स्ट्रीम करने के लिए सीधे तौर पर Live API से कनेक्ट होता है. इसके लिए, [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) का इस्तेमाल किया जाता है. इससे आपका बैकएंड बायपास हो जाता है.

## अपनी प्रोफ़ाइल बनाना शुरू करें

अपने डेवलपमेंट एनवायरमेंट के हिसाब से गाइड चुनें:

सर्वर-टू-सर्वर

### [GenAI SDK ट्यूटोरियल](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=hi)

Python बैकएंड के साथ रीयल-टाइम मल्टीमॉडल ऐप्लिकेशन बनाने के लिए, GenAI SDK का इस्तेमाल करके Gemini Live API से कनेक्ट करें.

क्लाइंट से सर्वर

### [WebSocket ट्यूटोरियल](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=hi)

WebSockets का इस्तेमाल करके, Gemini Live API से कनेक्ट करें. इससे JavaScript फ़्रंटएंड और कुछ समय के लिए मान्य टोकन के साथ, रीयल-टाइम मल्टीमॉडल ऐप्लिकेशन बनाया जा सकता है.

Agent development kit

### [ADK ट्यूटोरियल](https://google.github.io/adk-docs/streaming/)

कोई एजेंट बनाएं और आवाज़ और वीडियो के ज़रिए बातचीत करने की सुविधा चालू करने के लिए, Agent Development Kit (ADK) स्ट्रीमिंग का इस्तेमाल करें.

## पार्टनर इंटिग्रेशन

रीयल-टाइम में ऑडियो और वीडियो ऐप्लिकेशन डेवलप करने के लिए, तीसरे पक्ष के इंटिग्रेशन का इस्तेमाल किया जा सकता है. यह इंटिग्रेशन, WebRTC या WebSockets के ज़रिए Gemini Live API के साथ काम करता है.

[LiveKit

LiveKit एजेंट के साथ Gemini Live API का इस्तेमाल करें.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

Gemini Live और Pipecat का इस्तेमाल करके, रीयल-टाइम में एआई चैटबॉट बनाएँ.](https://docs.pipecat.ai/guides/features/gemini-live)
[Software Mansion का Fishjam

Fishjam की मदद से, लाइव वीडियो और ऑडियो स्ट्रीमिंग वाले ऐप्लिकेशन बनाएं.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[स्ट्रीम के हिसाब से विज़न एजेंट

Vision Agents की मदद से, रीयल-टाइम में आवाज़ और वीडियो वाले एआई ऐप्लिकेशन बनाएं.](https://visionagents.ai/integrations/gemini)
[Voximplant

Voximplant की मदद से, आने वाले और जाने वाले कॉल को Live API से कनेक्ट करें.](https://voximplant.com/products/gemini-client)
[अगोरा

Agora की मदद से, रीयल-टाइम में बातचीत करने वाले एआई ऐप्लिकेशन बनाएं.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Firebase AI Logic का इस्तेमाल करके, Gemini Live API का इस्तेमाल शुरू करें.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-10 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-10 (UTC) को अपडेट किया गया."],[],[]]
