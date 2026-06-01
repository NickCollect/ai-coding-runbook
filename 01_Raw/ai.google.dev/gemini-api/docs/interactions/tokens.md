---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=hi
fetched_at: 2026-06-01T06:02:05.026837+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# टोकन की संख्या समझना और गिनना

Gemini और जनरेटिव एआई के अन्य मॉडल, इनपुट और आउटपुट को *टोकन* नाम की ग्रैनुलैरिटी पर प्रोसेस करते हैं.

**Gemini मॉडल के लिए, एक टोकन करीब-करीब चार वर्णों के बराबर होता है.
100 टोकन, अंग्रेज़ी के करीब 60 से 80 शब्दों के बराबर होते हैं.**

## टोकन के बारे में जानकारी

टोकन, `z` जैसे सिंगल वर्ण या `cat` जैसे पूरे शब्द हो सकते हैं. लंबे शब्दों को कई टोकन में बांटा जाता है. मॉडल के इस्तेमाल किए जाने वाले सभी टोकन के सेट को शब्दावली कहा जाता है. वहीं, टेक्स्ट को टोकन में बांटने की प्रोसेस को *टोकनाइज़ेशन* कहा जाता है.

बिलिंग की सुविधा चालू होने पर, [Gemini API को कॉल करने की लागत](https://ai.google.dev/pricing?hl=hi) इनपुट और आउटपुट टोकन की संख्या के आधार पर तय की जाती है. इसलिए, टोकन की संख्या गिनने का तरीका जानना मददगार साबित हो सकता है.

## टोकन की संख्या गिनना

Gemini API के सभी इनपुट और आउटपुट को टोकनाइज़ किया जाता है. इनमें टेक्स्ट, इमेज फ़ाइलें, और टेक्स्ट के अलावा अन्य मोडैलिटी शामिल हैं.

टोकन की संख्या इन तरीकों से गिनी जा सकती है:

- **अनुरोध के इनपुट के साथ `count_tokens` को कॉल करें.** इससे, *सिर्फ़ इनपुट* में मौजूद टोकन की कुल संख्या मिलती है. अनुरोधों का साइज़ देखने के लिए, इनपुट भेजने से पहले यह कॉल करें.
- **इंटरैक्शन के जवाब में, `usage` का इस्तेमाल करें.** इससे, इनपुट (`total_input_tokens`), आउटपुट (`total_output_tokens`), थिंकिंग (`total_thought_tokens`), कैश मेमोरी में सेव किए गए कॉन्टेंट (`total_cached_tokens`), टूल के इस्तेमाल (`total_tool_use_tokens`), और कुल (`total_tokens`) के लिए टोकन की संख्या मिलती है.

### टेक्स्ट टोकन की संख्या गिनना

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### मल्टी-टर्न टोकन की संख्या गिनना

`previous_interaction_id` का इस्तेमाल करके, बातचीत के इतिहास में मौजूद टोकन की संख्या गिनें:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### मल्टीमॉडल टोकन की संख्या गिनना

Gemini API के सभी इनपुट को टोकनाइज़ किया जाता है. इनमें इमेज, वीडियो, और ऑडियो शामिल हैं.
टोकनाइज़ेशन के बारे में अहम बातें:

- **इमेज**: दोनों डाइमेंशन में ≤384 पिक्सल वाली इमेज को 258 टोकन के तौर पर गिना जाता है. बड़ी इमेज को 768x768 पिक्सल के टाइल में बांटा जाता है. हर टाइल को 258 टोकन के तौर पर गिना जाता है.
- **वीडियो**: हर सेकंड के लिए 263 टोकन
- **ऑडियो**: हर सेकंड के लिए 32 टोकन

#### इमेज टोकन

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**इनलाइन डेटा का उदाहरण:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### वीडियो टोकन

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### ऑडियो टोकन

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### सिस्टम के निर्देशों वाले टोकन की संख्या गिनना

सिस्टम के निर्देशों को, इनपुट टोकन के तौर पर गिना जाता है:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### टूल वाले टोकन की संख्या गिनना

टूल (फ़ंक्शन, कोड एक्ज़ीक्यूशन, Google Search) को भी गिना जाता है:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## कॉन्टेक्स्ट विंडो

हर Gemini मॉडल, टोकन की एक तय संख्या को ही प्रोसेस कर सकता है. कॉन्टेक्स्ट विंडो, इनपुट और आउटपुट टोकन की कुल सीमा तय करती है.

### प्रोग्राम के ज़रिए, कॉन्टेक्स्ट विंडो का साइज़ पाना

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.5-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.5-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

[मॉडल वाले पेज पर, कॉन्टेक्स्ट विंडो के साइज़ देखें.](https://ai.google.dev/gemini-api/docs/models?hl=hi)

## आगे क्या करना है

- [टेक्स्ट जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=hi): जनरेट करने की बुनियादी बातें
- [कैश मेमोरी में सेव करना](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=hi): कैश मेमोरी में सेव करके लागत कम करना
- [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi): लागत के बारे में जानकारी

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-28 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-28 (UTC) को अपडेट किया गया."],[],[]]
