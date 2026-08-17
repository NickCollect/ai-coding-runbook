---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=hi
fetched_at: 2026-08-17T02:25:57.586093+00:00
title: "\u090f\u091c\u0947\u0902\u091f\u093f\u0915 \u0935\u093f\u091c\u093c\u0928 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e\u090f\u0901 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# एजेंटिक विज़न की सुविधाएँ

Gemini Robotics ER मॉडल, इमेज में बदलाव करने और जवाब देने से पहले लॉजिक लागू करने के लिए, Python कोड लिख और चला सकते हैं. इस पेज पर, कोड चलाने के उदाहरण दिए गए हैं. जैसे: ज़ूम और क्रॉप करके ऑब्जेक्ट का पता लगाना, इंस्ट्रुमेंट रीडिंग, फ़्लूड मेज़रमेंट, सर्किट बोर्ड रीडिंग, और इमेज एनोटेशन.

इन उदाहरणों को अपने इस्तेमाल के हिसाब से ढालने के लिए, प्रॉम्प्ट में दिए गए टेक्स्ट और अपलोड की गई इमेज फ़ाइल को अपनी जानकारी से बदलें. इसके अलावा, प्रॉम्प्ट में अनुरोध किए गए JSON स्कीमा में बदलाव करके, उसे अपने ऐप्लिकेशन के आउटपुट स्ट्रक्चर से मैच किया जा सकता है. साथ ही, आउटपुट फ़ॉर्मैट और सटीक जानकारी के लिए, `system_instruction` जोड़ा जा सकता है.

रन किया जा सकने वाला पूरा कोड देखने के लिए, [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) देखें.

## सूझ-बूझ वाले मॉडल का लेवल

सटीक जानकारी पाने के लिए, इंतज़ार करने का समय बढ़ाने के लिए, सूझ-बूझ वाले मॉडल के लेवल को कंट्रोल किया जा सकता है. ऑब्जेक्ट का पता लगाने की सुविधा जैसे स्पेस से जुड़े टास्क, सूझ-बूझ वाले मॉडल के कम लेवल पर भी अच्छी तरह काम करते हैं. गिनती करना या वज़न का अनुमान लगाना जैसे मुश्किल टास्क, सूझ-बूझ वाले मॉडल के ज़्यादा लेवल पर अच्छी तरह काम करते हैं.

यहां दिए गए उदाहरण में, गिनती करने जैसे मुश्किल टास्क के लिए, सूझ-बूझ वाले मॉडल का लेवल `high` पर सेट किया गया है:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

ज़्यादा जानकारी के लिए, [सूझ-बूझ वाले मॉडल का लेवल](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=hi) देखें.

## ऑब्जेक्ट का पता लगाने की सुविधा (ज़ूम और क्रॉप करना)

यहां दिए गए उदाहरण में बताया गया है कि ऑब्जेक्ट का पता लगाने और बाउंडिंग बॉक्स दिखाने के लिए, इमेज को ज़ूम और क्रॉप करने के लिए, कोड एक्ज़ीक्यूशन का इस्तेमाल कैसे करें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

मॉडल का आउटपुट, यहां दिए गए JSON रिस्पॉन्स जैसा होगा:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

यहां दी गई इमेज में, मॉडल से मिले बॉक्स दिखाए गए हैं.

![मिली हुई चीज़ों के लिए बाउंडिंग बॉक्स दिखाने वाला उदाहरण](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=hi)

## ऐनलॉग गेज को पढ़ना और लॉजिक लागू करना

यहां दिए गए उदाहरण में बताया गया है कि ऐनलॉग गेज को पढ़ने और समय की कैलकुलेशन करने के लिए, मॉडल का इस्तेमाल कैसे करें. इसमें JSON आउटपुट लागू करने के लिए, सिस्टम इंस्ट्रक्शन का इस्तेमाल किया गया है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## कंटेनर में मौजूद फ़्लूड को मेज़र करना

यहां दिए गए उदाहरण में बताया गया है कि कंटेनर में मौजूद फ़्लूड के लेवल को मेज़र करने के लिए, कोड एक्ज़ीक्यूशन का इस्तेमाल कैसे करें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## सर्किट बोर्ड पर मौजूद निशान पढ़ना

यहां दिए गए उदाहरण में बताया गया है कि सर्किट बोर्ड पर मौजूद निशान पढ़ने के लिए, कोड चलाने की सुविधा का इस्तेमाल कैसे करें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![सर्किट बोर्ड पर मार्किंग दिखाने वाला उदाहरण](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=hi)

## इमेज के ऊपर टेक्स्ट, लिंक वगैरह

यहां दिए गए उदाहरण में बताया गया है कि इमेज को एनोटेट करने के लिए, कोड एक्ज़ीक्यूशन का इस्तेमाल कैसे करें. जैसे, डिस्पोज़ल के निर्देशों के लिए तीर के निशान बनाना और बदली हुई इमेज दिखाना.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

यहां इनपुट के तौर पर इस्तेमाल की गई इमेज का उदाहरण दिया गया है.

![पढ़ने के लिए घड़ी दिखाने वाला उदाहरण](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=hi)

मॉडल का आउटपुट, यहां दिए गए आउटपुट जैसा होगा:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## आगे क्या करना है

- [टास्क ऑर्केस्ट्रेशन](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=hi) — कस्टम रोबोट एपीआई की मदद से, लंबे समय तक चलने वाले टास्क.
- [स्ट्रीमिंग की सुविधा के साथ रोबोटिक्स](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=hi) — रीयल-टाइम में दोनों दिशाओं में स्ट्रीमिंग (सिर्फ़ Gemini Robotics ER 2 में उपलब्ध).
- [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=hi) — अहम पलों का पता लगाना और प्रोग्रेस क्लासिफ़िकेशन (सिर्फ़ Gemini Robotics ER 2 में उपलब्ध).

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
