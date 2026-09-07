---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=hi
fetched_at: 2026-09-07T05:35:46.682168+00:00
title: "\u0935\u0940\u0921\u093f\u092f\u094b \u0915\u0940 \u092c\u093e\u0930\u0940\u0915\u093c\u0940 \u0938\u0947 \u092a\u0939\u091a\u093e\u0928 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# वीडियो की बारीक़ी से पहचान करना

Gemini Robotics ER 2, दो सुविधाओं का इस्तेमाल करके, लगातार वीडियो फ़ीड से टास्क की प्रोग्रेस को ट्रैक कर सकता है:

- मोमेंट फ़ाइंडिंग: इससे सटीक टाइमस्टैंप की पहचान की जा सकती है, जहां कोई मुख्य इवेंट होता है.
- प्रोग्रेस क्लासिफ़िकेशन: इससे हर वीडियो को पांच कंप्लीशन ब्रैकेट में से किसी एक में असाइन किया जा सकता है. ये ब्रैकेट 0–20%, 20–40%, 40–60%, 60–80%, और 80–100% हैं.

## मोमेंट फ़ाइंडिंग

मोमेंट फ़ाइंडिंग से, वीडियो के उस सटीक फ़्रेम की पहचान की जा सकती है जहां कोई अहम इवेंट होता है. उदाहरण के लिए, जब कोई कप भर जाता है या कोई गांठ बांधी जाती है. रोबोट इसका इस्तेमाल, सफलता की पुष्टि करने, चरणों को क्रम से लगाने, और गड़बड़ियों को ठीक करने के लिए करते हैं.

यहां दिए गए उदाहरण में, प्रॉम्प्ट मॉडल से किसी वीडियो में दिए गए टास्क के पूरा होने के मोमेंट की पहचान करने के लिए कहता है:

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

यहां मोमेंट फ़ाइंडिंग वाले वीडियो के उदाहरण के तौर पर फ़्रेम दिखाए गए हैं. इनमें मॉडल, टास्क के पूरा होने का टाइमस्टैंप दिखाता है:

![टाइमस्टैंप ओवरले के साथ, वीडियो फ़्रेम में किसी खास पल को ढूंढने का आउटपुट दिखाने वाले वीडियो फ़्रेम का उदाहरण](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=hi)

## प्रोग्रेस क्लासिफ़िकेशन

प्रोग्रेस क्लासिफ़िकेशन से, किसी वीडियो को पांच कंप्लीशन ब्रैकेट में से किसी एक में असाइन किया जा सकता है. ये ब्रैकेट 0–20%, 20–40%, 40–60%, 60–80%, या 80–100% हैं. इससे रोबोट को रीयल-टाइम में स्थिति की जानकारी मिलती है. इसलिए, वे पूरे वर्कफ़्लो को रीस्टार्ट किए बिना, कार्रवाइयों को अडजस्ट कर सकते हैं या फ़ेल हुए चरणों को फिर से आज़मा सकते हैं.

यहां दिए गए उदाहरण में, प्रॉम्प्ट मॉडल से किसी वीडियो में मौजूदा प्रोग्रेस लेवल को क्लासिफ़ाई करने के लिए कहता है:

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

यहां प्रोग्रेस क्लासिफ़िकेशन वाले वीडियो के उदाहरण के तौर पर फ़्रेम दिखाए गए हैं. इनमें मॉडल, प्रोग्रेस ब्रैकेट असाइन करता है:

![प्रोग्रेस ब्रैकेट के लेबल के साथ, प्रोग्रेस क्लासिफ़िकेशन का आउटपुट दिखाने वाले वीडियो फ़्रेम का उदाहरण](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=hi)

## उदाहरण

मल्टी-स्टेप टास्क ट्रैकिंग की सुविधा वाले, पूरी तरह से रन किए जा सकने वाले उदाहरण देखने के लिए,
[Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) देखें.

## आगे क्या करना है

- [रोबोटिक्स के लिए Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) — रीयल-टाइम में दोनों दिशाओं में स्ट्रीमिंग.
- [टास्क ऑर्केस्ट्रेशन](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=hi) — स्पेस से जुड़ी जानकारी के साथ, लंबे समय तक चलने वाले टास्क.
- [Gemini Robotics ER की खास जानकारी](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=hi) — मॉडल की तुलना और उसकी सुविधाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
