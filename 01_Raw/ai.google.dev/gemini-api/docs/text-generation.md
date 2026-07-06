---
source_url: https://ai.google.dev/gemini-api/docs/text-generation?hl=hi
fetched_at: 2026-07-06T05:09:36.670341+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# टेक्स्ट जनरेट करने की सुविधा

Gemini API, टेक्स्ट, इमेज, वीडियो, और ऑडियो इनपुट से टेक्स्ट आउटपुट जनरेट कर सकता है.

यहां एक सामान्य उदाहरण दिया गया है:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How does AI work?",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?"
  }'
```

Google के GenAI SDK टूल, मॉडल के जवाब को ऐक्सेस करने के लिए, सीधे तौर पर `Interaction` ऑब्जेक्ट पर सुविधा प्रॉपर्टी उपलब्ध कराते हैं.

सबसे ज़्यादा इस्तेमाल किया जाने वाला हेल्पर **`interaction.output_text`** (स्ट्रिंग) है. यह मॉडल के जवाब में मौजूद आखिरी टेक्स्ट ब्लॉक दिखाता है. अगर जवाब को एक के बाद एक कई `TextContent` ब्लॉक में बांटा गया है, तो यह सुविधा उन्हें अपने-आप जोड़ देती है.
ध्यान दें कि `.output_text` में, पहले के ऐसे टेक्स्ट ब्लॉक शामिल नहीं होते जिन्हें टेक्स्ट के अलावा किसी अन्य तरह के कॉन्टेंट (जैसे कि विचार, इमेज, ऑडियो या टूल कॉल) से अलग किया गया हो. मुश्किल या इंटरलीव किए गए मल्टीमॉडल जवाबों के लिए, आपको `steps` पर मैन्युअल तरीके से दोहराना होगा. मीडिया से जुड़ी अन्य सुविधाओं के बारे में ज़्यादा जानने के लिए, [इंटरैक्शन की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions?hl=hi#convenience-properties) देखें.

## Gemini के साथ मिलकर सोचना

Gemini मॉडल में, ["थिंकिंग"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi) मोड डिफ़ॉल्ट रूप से चालू होता है. इससे मॉडल को किसी अनुरोध का जवाब देने से पहले, जानकारी का विश्लेषण करने यानी तर्क करने की सुविधा मिलती है.

हर मॉडल, अलग-अलग थिंकिंग कॉन्फ़िगरेशन के साथ काम करता है. इससे आपको लागत, लेटेन्सी, और इंटेलिजेंस को कंट्रोल करने में मदद मिलती है. ज़्यादा जानकारी के लिए, [सोचने की गाइड](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi#set-budget) देखें.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## सिस्टम के निर्देश और अन्य कॉन्फ़िगरेशन

सिस्टम के निर्देशों की मदद से, Gemini के मॉडल के व्यवहार को कंट्रोल किया जा सकता है. मॉडल के व्यवहार को कॉन्फ़िगर करने के लिए, `system_instruction` पैरामीटर पास करें.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

`generation_config` पैरामीटर का इस्तेमाल करके, जनरेट करने के डिफ़ॉल्ट पैरामीटर को भी बदला जा सकता है. जैसे, तापमान.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

कॉन्फ़िगर किए जा सकने वाले पैरामीटर और उनके ब्यौरे की पूरी सूची देखने के लिए, [Interactions API का रेफ़रंस](https://ai.google.dev/api/interactions-api?hl=hi) देखें.

## मल्टीमॉडल इनपुट

Gemini API में, टेक्स्ट, इमेज, वीडियो, और ऑडियो, सभी तरह के इनपुट इस्तेमाल किए जा सकते हैं. इससे आपको टेक्स्ट के साथ-साथ मीडिया फ़ाइलें भी इस्तेमाल करने की सुविधा मिलती है. यहां दी गई इमेज में, इमेज उपलब्ध कराने का तरीका दिखाया गया है:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Tell me about this instrument"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

इमेज उपलब्ध कराने के अन्य तरीकों और इमेज प्रोसेसिंग के ज़्यादा बेहतर तरीके के बारे में जानने के लिए, [इमेज समझने से जुड़ी हमारी गाइड](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=hi) देखें.
यह एपीआई, [दस्तावेज़](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=hi), [वीडियो](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=hi), और [ऑडियो](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=hi) इनपुट के साथ-साथ इन्हें समझने की सुविधा भी देता है.

## जवाब स्ट्रीम करना

डिफ़ॉल्ट रूप से, मॉडल जवाब सिर्फ़ तब देता है, जब जनरेट करने की पूरी प्रोसेस पूरी हो जाती है.

बेहतर इंटरैक्शन के लिए, जवाब के चंक जनरेट होने पर उन्हें हैंडल करने के लिए स्ट्रीमिंग का इस्तेमाल करें. इवेंट टाइप, टूल की मदद से स्ट्रीमिंग, थिंकिंग, एजेंट, और इमेज जनरेशन के बारे में पूरी जानकारी देने वाली गाइड के लिए, [स्ट्रीमिंग के दौरान होने वाली बातचीत](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=hi) की गाइड देखें.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

## सिलसिलेवार बातचीत

Interactions API, एक से ज़्यादा बार बातचीत करने की सुविधा देता है. इसके लिए, यह `previous_interaction_id` का इस्तेमाल करके, इंटरैक्शन को एक साथ जोड़ता है. हर बातचीत एक अलग इंटरैक्शन होती है. साथ ही, एपीआई बातचीत के इतिहास को अपने-आप मैनेज करता है.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

स्ट्रीमिंग का इस्तेमाल, सिलसिलेवार बातचीत के लिए भी किया जा सकता है. इसके लिए, `previous_interaction_id` को स्ट्रीमिंग के तरीकों के साथ जोड़ें.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
    stream: true,
  });
  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## स्टेटलेस बातचीत

`previous_interaction_id` का इस्तेमाल करने पर, Interactions API डिफ़ॉल्ट रूप से बातचीत की स्थिति को सर्वर-साइड पर मैनेज करता है. हालांकि, क्लाइंट-साइड पर बातचीत के इतिहास को मैनेज करके, स्टेटलेस मोड में भी काम किया जा सकता है.

स्टेटलेस मोड का इस्तेमाल करने के लिए:
1. सर्वर-साइड स्टोरेज से ऑप्ट आउट करने के लिए, अपने अनुरोध में `store=false` सेट करें.
2. क्लाइंट-साइड पर, बातचीत के इतिहास को **चरणों** की एक कैटगरी के तौर पर बनाए रखें.
3. इसके बाद के अनुरोधों में, `input` फ़ील्ड में इकट्ठा किए गए चरणों को पास करें. साथ ही, अपने नए चरण को `user_input` चरण के तौर पर जोड़ें.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "I have 2 dogs in my house." }]
    }
  ];

  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  history.push(...interaction1.steps);

  history.push({
    type: "user_input",
    content: [{ type: "text", text: "How many paws are in my house?" }]
  });

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history
  });
  console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Turn 1: Send request with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

# Extract the steps from response
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Reconstruct the full history for Turn 2 by combining:
# 1. First user input
# 2. Model response steps
# 3. Second user input
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## प्रॉम्प्ट लिखने से जुड़ी सलाह

Gemini का ज़्यादा से ज़्यादा फ़ायदा पाने के लिए, [प्रॉम्प्ट इंजीनियरिंग गाइड](https://ai.google.dev/gemini/docs/prompting-strategies?hl=hi) देखें.

## आगे क्या करना है

- [Google AI Studio में Gemini](https://aistudio.google.com?hl=hi) को आज़माएं.
- JSON जैसे जवाबों के लिए, [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=hi) का इस्तेमाल करके देखें.
- Gemini की [इमेज](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=hi),
  [वीडियो](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=hi),
  [ऑडियो](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=hi), और
  [दस्तावेज़](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=hi) को समझने की क्षमताओं के बारे में जानें.
- मल्टीमॉडल [फ़ाइल प्रॉम्प्टिंग की रणनीतियों](https://ai.google.dev/gemini-api/docs/interactions/files?hl=hi#prompt-guide) के बारे में जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया."],[],[]]
