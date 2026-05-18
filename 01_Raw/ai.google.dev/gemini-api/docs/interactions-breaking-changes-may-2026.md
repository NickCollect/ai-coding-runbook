---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=hi
fetched_at: 2026-05-18T05:10:36.979897+00:00
title: "Interactions API: \u092e\u093e\u0907\u0917\u094d\u0930\u0947\u0936\u0928 \u0917\u093e\u0907\u0921 \u092e\u0947\u0902 \u092c\u0921\u093c\u0947 \u092c\u0926\u0932\u093e\u0935 (\u092e\u0908 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Interactions API: माइग्रेशन गाइड में बड़े बदलाव (मई 2026)

Interactions API के `v1beta` में अहम बदलाव किए जा रहे हैं. इससे एपीआई के स्ट्रक्चर में बदलाव होगा. साथ ही, फ़्लाइट के दौरान स्टीयरिंग और टूल कॉल को एसिंक्रोनस तरीके से करने जैसी सुविधाएं मिलेंगी. इस पेज पर, किए जा रहे बदलावों के बारे में बताया गया है. साथ ही, माइग्रेट करने में आपकी मदद करने के लिए, कोड के पहले और बाद के उदाहरण दिए गए हैं. बदलावों की दो कैटगरी हैं:

1. [**स्टेप स्कीमा**](#steps-schema): `outputs` कलेक्शन की जगह, नया `steps` कलेक्शन इस्तेमाल किया जाएगा. इससे हर इंटरैक्शन के लिए, स्ट्रक्चर्ड टाइमलाइन मिलेगी.
2. [**आउटपुट फ़ॉर्मैट कॉन्फ़िगरेशन**](#output-format-config): नया पॉलीमॉर्फिक
   `response_format` आउटपुट फ़ॉर्मैट के सभी कंट्रोल को एक साथ लाता है. साथ ही,
   `response_mime_type` को हटाता है.

अपने इंटिग्रेशन को अपडेट करने के लिए, [नए स्कीमा पर माइग्रेट करने का तरीका](#how-to-migrate) में दिए गए निर्देशों का पालन करें.

## मुख्य बदलाव: `outputs` की जगह `steps` का इस्तेमाल

नए स्कीमा में, `outputs` कलेक्शन की जगह `steps` कलेक्शन का इस्तेमाल किया जाएगा.

- **लेगसी**: जवाबों में, फ़्लैट `outputs` कलेक्शन मिलता था. इसमें सिर्फ़ मॉडल से जनरेट किया गया कॉन्टेंट होता था.
- **नया स्कीमा**: जवाबों में, `steps` कलेक्शन मिलता है. इसमें टाइप डिस्क्रिमिनेटर के साथ स्ट्रक्चर्ड स्टेप होते हैं.

`POST /interactions` से सिर्फ़ आउटपुट स्टेप मिलते हैं. `GET /interactions/{id}`
से, पूरी स्टेप टाइमलाइन मिलती है. इसमें शुरुआती `user_input` स्टेप भी शामिल होता है.

### सामान्य इनपुट/आउटपुट (यूनरी)

#### पहले (लेगसी)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3-flash-preview", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### बाद में (नया स्कीमा)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3-flash-preview", input="Tell me a joke."
)

# Response access
print(interaction.steps[-1].content[0].text)  # CHANGED: steps instead of outputs
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### फ़ंक्शन कॉल करना

अनुरोध का स्ट्रक्चर पहले जैसा ही रहेगा. हालांकि, जवाब में फ़्लैट `outputs` कॉन्टेंट की जगह, स्ट्रक्चर्ड स्टेप मिलेंगे.

#### पहले (लेगसी)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling {output.name} with {JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### बाद में (नया स्कीमा)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling {step.name} with {JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### सर्वर-साइड टूल

सर्वर-साइड टूल (जैसे, Google Search या Code Execution) अब `steps` कलेक्शन में, खास तरह के स्टेप देते हैं. लेगसी स्कीमा में, इन कार्रवाइयों को `outputs` कलेक्शन में खास तरह के कॉन्टेंट के तौर पर दिखाया जाता था. हालांकि, नए स्कीमा में इन्हें `steps` कलेक्शन में ले जाया जाता है. यहां दिए गए उदाहरणों में, Google Search का इस्तेमाल किया गया है.

#### पहले (लेगसी)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: {output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: {output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### बाद में (नया स्कीमा)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result.search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: {step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: {step.result.searchSuggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### स्ट्रीमिंग

स्ट्रीमिंग में, इवेंट के नए टाइप दिखते हैं:

#### इवेंट के नए टाइप

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### इवेंट के पुराने टाइप

ऊपर बताए गए नए इवेंट, इवेंट के इन पुराने टाइप की जगह इस्तेमाल किए जाएंगे:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → इसकी जगह `interaction.in_progress`, `interaction.requires_action` वगैरह का इस्तेमाल किया जाएगा.

**स्ट्रीमिंग फ़ंक्शन कॉल**: फ़ंक्शन कॉल करने के लिए स्ट्रीमिंग का इस्तेमाल करने पर,
`step.start` इवेंट में फ़ंक्शन का नाम दिखता है. वहीं, `step.delta` इवेंट में
आर्ग्युमेंट, JSON स्ट्रिंग के तौर पर स्ट्रीम होते हैं. इसके लिए, `arguments_delta` का इस्तेमाल किया जाता है. पूरे
आर्ग्युमेंट पाने के लिए, आपको इन डेल्टा को इकट्ठा करना होगा. यह यूनरी कॉल से अलग है. यूनरी कॉल में, आपको फ़ंक्शन कॉल का पूरा ऑब्जेक्ट एक साथ मिलता है.

#### उदाहरण

##### पहले (लेगसी)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### बाद में (नया स्कीमा)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a story.",
    stream=True,
):
    if event.type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3-flash-preview",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3-flash-preview"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### स्टेटलेस बातचीत का इतिहास

अगर क्लाइंट साइड पर, बातचीत के इतिहास को मैन्युअल तरीके से मैनेज किया जाता है (स्टेटलेस इस्तेमाल का तरीका), तो आपको पिछले टर्न को एक साथ लाने के तरीके को अपडेट करना होगा.

- **लेगसी**: डेवलपर अक्सर जवाबों से `outputs` कलेक्शन इकट्ठा करते थे और अगले टर्न में, उन्हें `input` फ़ील्ड में वापस भेजते थे.
- **नया स्कीमा**: अब आपको जवाब से `steps` कलेक्शन इकट्ठा करना चाहिए और अगले अनुरोध के `input` फ़ील्ड में इसे पास करना चाहिए. साथ ही, अपने नए उपयोगकर्ता टर्न को `user_input` स्टेप के तौर पर जोड़ना चाहिए.

## आउटपुट फ़ॉर्मैट कॉन्फ़िगरेशन: `response_format` में बदलाव

अपडेट किए गए एपीआई में, आउटपुट फ़ॉर्मैट के सभी कंट्रोल को एक ही पॉलीमॉर्फिक `response_format` फ़ील्ड में शामिल किया गया है. इससे, टॉप लेवल पर आउटपुट कॉन्फ़िगरेशन को केंद्रीकृत किया जाता है. साथ ही, `generation_config` को मॉडल के व्यवहार (जैसे, तापमान, top\_p, और थिंकिंग) पर फ़ोकस किया जाता है.

### मुख्य बदलाव

- **एपीआई, `response_mime_type` को हटाता है.** अब आपको `response_format` में, हर फ़ॉर्मैट की एंट्री के लिए MIME टाइप तय करना होगा.
- **`response_format` अब पॉलीमॉर्फिक ऑब्जेक्ट (या कलेक्शन) है.** हर एंट्री में, `type` डिस्क्रिमिनेटर (`text`, `audio`, `image`) और टाइप के हिसाब से फ़ील्ड होते हैं. आउटपुट के कई तरीके का अनुरोध करने के लिए, फ़ॉर्मैट की एंट्री का कलेक्शन पास करें.
- **`image_config`, `generation_config` से `response_format` में चला जाता है.**
  अब आपको `"type": "image"` के साथ `response_format` एंट्री में, इमेज आउटपुट सेटिंग तय करनी होंगी. जैसे, `aspect_ratio` और `image_size`
  .

### स्ट्रक्चर्ड आउटपुट (JSON)

नए स्कीमा में, `response_mime_type` फ़ील्ड को हटा दिया गया है. इसके बजाय, `response_format` ऑब्जेक्ट में, MIME टाइप और JSON स्कीमा तय करें
`"type": "text"`.

#### पहले (लेगसी)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### बाद में (नया स्कीमा)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### इमेज कॉन्फ़िगरेशन

नए स्कीमा में, `generation_config` से `image_config` को हटा दिया गया है. अब आपको `response_format` एंट्री में, इमेज आउटपुट सेटिंग तय करनी होंगी
`"type": "image"`.

#### पहले (लेगसी)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### बाद में (नया स्कीमा)

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

आउटपुट के कई तरीके का अनुरोध करने के लिए (उदाहरण के लिए, टेक्स्ट और ऑडियो एक साथ), `response_format` में एक ऑब्जेक्ट के बजाय, फ़ॉर्मैट की एंट्री का कलेक्शन पास करें.

## नए स्कीमा पर माइग्रेट करने का तरीका

### एसडीके का इस्तेमाल करने वाले लोग

एसडीके के नए वर्शन (Python ≥2.0.0, JavaScript ≥2.0.0) पर अपग्रेड करें. एसडीके, आपको नए स्कीमा में अपने-आप ऑप्ट-इन कर लेता है. इसके लिए, कोड में किसी तरह के बदलाव की ज़रूरत नहीं होती. आपको सिर्फ़ जवाब पढ़ने के तरीके को अपडेट करना होगा. इसके लिए, ऊपर दिए गए उदाहरण देखें. ध्यान दें कि एसडीके के इन वर्शन में, सिर्फ़ नया स्कीमा काम करता है. एसडीके के पुराने वर्शन (Python 1.x.x, JavaScript 1.x.x), **8 जून, 2026** को लेगसी स्कीमा हटाए जाने तक काम करते रहेंगे.

### REST API का इस्तेमाल करने वाले लोग

नए स्कीमा में अभी ऑप्ट-इन करने के लिए, अपने अनुरोधों में `Api-Revision: 2026-05-20` हेडर जोड़ें. **26 मई** के बाद, नया स्कीमा सभी
अनुरोधों के लिए डिफ़ॉल्ट स्कीमा बन जाएगा. **8 जून** तक, `Api-Revision: 2026-05-07`
का इस्तेमाल करके, अस्थायी तौर पर ऑप्ट-आउट किया जा सकता है. इसके बाद, एपीआई, लेगसी स्कीमा को हमेशा के लिए हटा देगा.

### टाइमलाइन

| तारीख | फ़ेज़ (चरण) | एसडीके का इस्तेमाल करने वाले लोग | REST API का इस्तेमाल करने वाले लोग |
| --- | --- | --- | --- |
| **7 मई** | ऑप्ट-इन करें | एसडीके का नया वर्शन उपलब्ध है (Python ≥2.0.0, JS ≥2.0.0). नए स्कीमा को अपने-आप पाने के लिए, अपग्रेड करें. | ऑप्ट-इन करने के लिए, `Api-Revision: 2026-05-20` हेडर जोड़ें. डिफ़ॉल्ट स्कीमा, लेगसी ही रहेगा. |
| **26 मई** | डिफ़ॉल्ट स्कीमा में बदलाव | अगर पहले ही अपग्रेड कर लिया गया है, तो कुछ करने की ज़रूरत नहीं है. एसडीके के पुराने वर्शन (Python 1.x.x, JS 1.x.x) अब भी काम करेंगे. हालांकि, इनसे लेगसी स्कीमा के जवाब मिलेंगे. | नया स्कीमा अब डिफ़ॉल्ट स्कीमा है. ऑप्ट-आउट करने के लिए, `Api-Revision: 2026-05-07` हेडर भेजें. |
| **8 जून** | सूर्यास्त | Interactions API कॉल के लिए, Python 1.x.x और JS 1.x.x एसडीके वर्शन काम नहीं करेंगे. | Interactions API के लिए, लेगसी स्कीमा हटा दिया गया है. `Api-Revision` हेडर को नज़रअंदाज़ किया जाएगा. |

## माइग्रेशन की चेकलिस्ट

### स्टेप स्कीमा (`steps`)

- जवाब के कॉन्टेंट को `outputs` के बजाय `steps` कलेक्शन से पढ़ने के लिए, कोड अपडेट करें. [उदाहरण देखें](#basic-unary).
- पक्का करें कि आपका कोड, `user_input` और `model_output` दोनों तरह के स्टेप को हैंडल करता हो. [उदाहरण देखें](#basic-unary).
- (फ़ंक्शन कॉल करना) `steps` कलेक्शन में `function_call` स्टेप ढूंढने के लिए, कोड अपडेट करें. [उदाहरण देखें](#function-calling).
- (सर्वर-साइड टूल) टूल के हिसाब से स्टेप (जैसे, `google_search_call`, `google_search_result`) को हैंडल करने के लिए, कोड अपडेट करें. [उदाहरण देखें](#server-side-tools).
- (स्टेटलेस इतिहास) इतिहास को मैनेज करने के तरीके को अपडेट करें, ताकि अगले अनुरोध के `input` फ़ील्ड में `steps` कलेक्शन पास किया जा सके. [जानकारी देखें](#stateless-history).
- (सिर्फ़ स्ट्रीमिंग) नए SSE इवेंट टाइप (`interaction.created`, `step.delta` वगैरह) सुनने के लिए, क्लाइंट को अपडेट करें. [उदाहरण देखें](#streaming).

### आउटपुट फ़ॉर्मैट कॉन्फ़िगरेशन (`response_format`)

- `response_mime_type` की जगह, `response_format` में `mime_type` फ़ील्ड का इस्तेमाल करें. [उदाहरण देखें](#structured-output).
- अपने मौजूदा `response_format` JSON स्कीमा को `{"type": "text", "schema": ...}` ऑब्जेक्ट में रैप करें. [उदाहरण देखें](#structured-output).
- (इमेज जनरेट करना) `image_config` को `generation_config` से हटाकर, `response_format` में `{"type": "image", ...}` एंट्री में ले जाएं. [उदाहरण देखें](#image-config).
- (मल्टीमॉडल) आउटपुट के कई तरीके का अनुरोध करते समय, `response_format` को एक ऑब्जेक्ट से कलेक्शन में बदलें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-12 (UTC) को अपडेट किया गया."],[],[]]
