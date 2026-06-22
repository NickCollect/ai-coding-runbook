---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=hi
fetched_at: 2026-06-22T06:26:56.924582+00:00
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

`v1beta` Interactions API में कुछ बड़े बदलाव किए जा रहे हैं. इससे एपीआई के स्ट्रक्चर में बदलाव होगा. ऐसा इसलिए किया जा रहा है, ताकि आने वाले समय में, फ़्लाइट के बीच में बदलाव करने और टूल कॉल को एसिंक्रोनस तरीके से इस्तेमाल करने जैसी सुविधाओं को सपोर्ट किया जा सके. इस पेज पर बताया गया है कि क्या बदलाव हो रहा है. साथ ही, माइग्रेट करने में आपकी मदद करने के लिए, कोड के पहले और बाद के उदाहरण दिए गए हैं. बदलावों की दो कैटगरी हैं:

1. [**कदमों का स्कीमा**](#steps-schema): एक नया `steps` ऐरे, `outputs` ऐरे की जगह लेता है. इससे हर इंटरैक्शन टर्न की स्ट्रक्चर्ड टाइमलाइन मिलती है.
2. [**आउटपुट फ़ॉर्मैट कॉन्फ़िगरेशन**](#output-format-config): एक नया पॉलीमॉर्फ़िक `response_format`, आउटपुट फ़ॉर्मैट के सभी कंट्रोल को एक साथ जोड़ता है और `response_mime_type` को हटाता है.

अपने इंटिग्रेशन को अपडेट करने के लिए, [नए स्कीमा पर माइग्रेट करने का तरीका](#how-to-migrate) में दिया गया तरीका अपनाएं.

## मुख्य बदलाव: `outputs` से `steps`

नए स्कीमा में, `outputs` ऐरे की जगह `steps` ऐरे का इस्तेमाल किया जाता है.

- **लेगसी**: जवाब में, `outputs` का एक फ़्लैट कलेक्शन मिलता था. इसमें सिर्फ़ मॉडल से जनरेट किया गया कॉन्टेंट होता था.
- **नया स्कीमा**: जवाबों में `steps` अरे दिखता है. इसमें टाइप डिसक्रिमिनेटर के साथ स्ट्रक्चर्ड चरण शामिल होते हैं.

`POST /interactions` सिर्फ़ आउटपुट के चरण दिखाता है. `GET /interactions/{id}`
यह फ़ंक्शन, पूरे चरण की टाइमलाइन दिखाता है. इसमें शुरुआती `user_input` चरण भी शामिल है.

### बेसिक इनपुट/आउटपुट (यूनरी)

#### पहले (लेगसी)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
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

#### (नए स्कीमा) के बाद

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions#convenience-properties

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
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

### फ़ंक्शन कॉलिंग

अनुरोध का स्ट्रक्चर पहले जैसा ही रहता है. हालांकि, जवाब में फ़्लैट `outputs` कॉन्टेंट की जगह स्ट्रक्चर्ड चरणों को दिखाया जाता है.

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

#### (नए स्कीमा) के बाद

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

सर्वर-साइड टूल (जैसे, Google Search या कोड एक्ज़ीक्यूशन) अब `steps` ऐरे में कुछ खास तरह के चरण दिखाते हैं. लेगसी स्कीमा में, इन कार्रवाइयों को `outputs` कलेक्शन में खास कॉन्टेंट टाइप के तौर पर दिखाया जाता था. हालांकि, नए स्कीमा में इन्हें `steps` कलेक्शन में ले जाया जाता है. यहां दिए गए उदाहरणों में, Google Search का इस्तेमाल किया गया है.

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
    "model": "gemini-3.5-flash",
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

#### (नए स्कीमा) के बाद

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
    "model": "gemini-3.5-flash",
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

स्ट्रीमिंग से नए इवेंट टाइप का पता चलता है:

#### इवेंट के नए टाइप

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### इवेंट के ऐसे टाइप जो अब काम नहीं करते

ऊपर दिए गए नए इवेंट, लेगसी इवेंट के इन टाइप की जगह इस्तेमाल किए जाते हैं:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → इसकी जगह `interaction.in_progress`, `interaction.requires_action` वगैरह का इस्तेमाल किया जाता है

**फ़ंक्शन कॉल की स्ट्रीमिंग**: फ़ंक्शन कॉल के साथ स्ट्रीमिंग का इस्तेमाल करने पर, `step.start` इवेंट फ़ंक्शन का नाम दिखाता है. साथ ही, `step.delta` इवेंट, आर्ग्युमेंट को `arguments_delta` का इस्तेमाल करके, आंशिक JSON स्ट्रिंग के तौर पर स्ट्रीम करते हैं. पूरे आर्ग्युमेंट पाने के लिए, आपको इन डेल्टा को इकट्ठा करना होगा. यह यूनेरी कॉल से अलग है, जहां आपको फ़ंक्शन कॉल ऑब्जेक्ट एक साथ मिलता है.

#### उदाहरण

##### पहले (लेगसी)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
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
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
     "model": "gemini-3.5-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.5-flash"}, "event_type": "interaction.created"}
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

अगर क्लाइंट साइड पर बातचीत के इतिहास को मैन्युअल तरीके से मैनेज किया जाता है (स्टेटलेस इस्तेमाल का उदाहरण), तो आपको यह अपडेट करना होगा कि पिछले टर्न को कैसे स्ट्रिंग किया जाता है.

- **लेगसी**: डेवलपर अक्सर जवाबों से `outputs` ऐरे इकट्ठा करते थे और उन्हें अगले टर्न में `input` फ़ील्ड में वापस भेजते थे.
- **नया स्कीमा**: अब आपको जवाब से `steps` कलेक्शन करना होगा और इसे अगले अनुरोध के `input` फ़ील्ड में पास करना होगा. साथ ही, उपयोगकर्ता के नए टर्न को `user_input` चरण के तौर पर जोड़ना होगा.

## आउटपुट फ़ॉर्मैट कॉन्फ़िगरेशन: `response_format` बदलाव

अपडेट किए गए एपीआई में, आउटपुट फ़ॉर्मैट कंट्रोल को एक ही, बहुरूपी `response_format` फ़ील्ड में शामिल किया गया है. इससे आउटपुट कॉन्फ़िगरेशन को टॉप लेवल पर सेट किया जा सकता है. साथ ही, `generation_config` को मॉडल के व्यवहार (जैसे कि टेंपरेचर, top\_p, और गहराई से विचार) पर फ़ोकस करने में मदद मिलती है.

### मुख्य बदलाव

- **एपीआई, `response_mime_type` को हटा देता है.** अब `response_format` में हर फ़ॉर्मैट एंट्री के लिए, एमआईएमई टाइप तय किया जा सकता है.
- **`response_format` अब एक पॉलीमॉर्फिक ऑब्जेक्ट (या ऐरे) है.** हर एंट्री में `type` डिस्क्रिमिनेटर (`text`, `audio`, `image`) और टाइप के हिसाब से फ़ील्ड होते हैं. एक से ज़्यादा आउटपुट मोडेलिटी का अनुरोध करने के लिए, फ़ॉर्मैट एंट्री का एक कलेक्शन पास करें.
- **`image_config` को `generation_config` से `response_format` में ले जाया गया.**
  अब `"type": "image"` के साथ `response_format` एंट्री में, इमेज आउटपुट की सेटिंग तय की जा सकती हैं. जैसे, `aspect_ratio` और `image_size`.

### स्ट्रक्चर्ड आउटपुट (JSON)

नए स्कीमा में `response_mime_type` फ़ील्ड नहीं है. इसके बजाय, `"type": "text"` के साथ `response_format` ऑब्जेक्ट में एमआईएमई टाइप और JSON स्कीमा बताएं.

#### पहले (लेगसी)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
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

#### (नए स्कीमा) के बाद

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
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

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
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

नए स्कीमा में, `generation_config` से `image_config` को हटा दिया गया है. अब आपको `response_format` एंट्री में `"type": "image"` के साथ, इमेज आउटपुट सेटिंग तय करनी होंगी.

#### पहले (लेगसी)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### (नए स्कीमा) के बाद

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### ऑडियो कॉन्फ़िगरेशन

नए स्कीमा में, `response_modalities: ["audio"]` को `"type": "audio"` की `response_format` एंट्री से बदल दिया जाता है.

#### पहले (लेगसी)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    response_modalities: ['audio'],
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

#### (नए स्कीमा) के बाद

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    # response_modalities is removed — use response_format
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    // response_modalities is removed — use response_format
    response_format: {
        type: 'audio'
    },
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
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
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

अगर आपको आउटपुट के लिए एक से ज़्यादा मोडालिटी (उदाहरण के लिए, टेक्स्ट और ऑडियो एक साथ) का अनुरोध करना है, तो `response_format` को एक ऑब्जेक्ट के बजाय फ़ॉर्मैट एंट्री का ऐरे पास करें.

## नए स्कीमा पर माइग्रेट करने का तरीका

### एसडीके का इस्तेमाल करने वाले लोग

एसडीके टूल के नए वर्शन पर अपग्रेड करें (Python ≥2.0.0, JavaScript ≥2.0.0). एसडीके, आपको नए स्कीमा में अपने-आप ऑप्ट-इन कर देता है. इसके लिए, कोड में किसी तरह का बदलाव करने की ज़रूरत नहीं होती. आपको सिर्फ़ यह अपडेट करना होता है कि जवाबों को कैसे पढ़ा जाए. इसके उदाहरण ऊपर दिए गए हैं. ध्यान दें कि इन एसडीके वर्शन में सिर्फ़ नया स्कीमा काम करता है. एसडीके के पुराने वर्शन (Python 1.x.x, JavaScript 1.x.x) **8 जून, 2026** को लेगसी स्कीमा हटाए जाने तक काम करते रहेंगे.

### REST API का इस्तेमाल करने वाले लोग

नए स्कीमा में ऑप्ट-इन करने के लिए, अपने अनुरोधों में `Api-Revision: 2026-05-20` हेडर जोड़ें. **26 मई** के बाद, सभी अनुरोधों के लिए नया स्कीमा डिफ़ॉल्ट रूप से लागू हो जाएगा. `Api-Revision: 2026-05-07` का इस्तेमाल करके, कुछ समय के लिए ऑप्ट आउट किया जा सकता है. ऐसा **8 जून** तक किया जा सकता है. इसके बाद, एपीआई लेगसी स्कीमा को हमेशा के लिए हटा देगा.

### टाइमलाइन

| तारीख | फ़ेज़ (चरण) | एसडीके का इस्तेमाल करने वाले लोग | REST API का इस्तेमाल करने वाले लोग |
| --- | --- | --- | --- |
| **7 मई** | ऑप्ट-इन करें | SDK टूल का नया वर्शन उपलब्ध है (Python ≥2.0.0, JS ≥2.0.0). नए स्कीमा को अपने-आप लागू करने के लिए, अपग्रेड करें. | ऑप्ट इन करने के लिए, `Api-Revision: 2026-05-20` हेडर जोड़ें. डिफ़ॉल्ट सेटिंग, लेगसी ही रहेगी. |
| **26 मई** | डिफ़ॉल्ट फ़्लिप | अगर आपने पहले ही अपग्रेड कर लिया है, तो आपको कुछ करने की ज़रूरत नहीं है. पुराने SDK (Python 1.x.x, JS 1.x.x) अब भी काम करते हैं, लेकिन लेगसी जवाब देते हैं. | नया स्कीमा अब डिफ़ॉल्ट रूप से उपलब्ध है. ऑप्ट आउट करने के लिए, `Api-Revision: 2026-05-07` हेडर भेजें. |
| **8 जून** | सूर्यास्त | Python 1.x.x और JS 1.x.x SDK वर्शन के लिए, Interactions API कॉल काम नहीं करेंगे. | Interactions API के लिए, लेगसी स्कीमा हटा दिया गया है. `Api-Revision` हेडर को अनदेखा किया गया. |

## माइग्रेशन की चेकलिस्ट

### Steps स्कीमा (`steps`)

- `outputs` के बजाय `steps` ऐरे से जवाब का कॉन्टेंट पढ़ने के लिए, कोड अपडेट करें. [उदाहरण देखें](#basic-unary).
- पुष्टि करें कि आपका कोड, `user_input` और `model_output`, दोनों तरह के चरणों को मैनेज करता हो. [उदाहरण देखें](#basic-unary).
- (फ़ंक्शन कॉल करना) `steps` ऐरे में `function_call` चरणों को ढूंढने के लिए कोड अपडेट करें. [उदाहरण देखें](#function-calling).
- (सर्वर-साइड टूल) टूल के हिसाब से कोड अपडेट करें, ताकि टूल से जुड़े चरणों को पूरा किया जा सके. जैसे, `google_search_call`, `google_search_result`. [उदाहरण देखें](#server-side-tools).
- (स्टेटलेस इतिहास) इतिहास को मैनेज करने की सुविधा को अपडेट करें, ताकि अगले अनुरोध के `input` फ़ील्ड में `steps` ऐरे को पास किया जा सके. [जानकारी देखें](#stateless-history).
- (सिर्फ़ स्ट्रीमिंग के लिए) नए एसएसई इवेंट टाइप (`interaction.created`, `step.delta` वगैरह) सुनने के लिए, क्लाइंट को अपडेट करें. [उदाहरण देखें](#streaming).

### आउटपुट फ़ॉर्मैट कॉन्फ़िगरेशन (`response_format`)

- `response_mime_type` को `response_format` में मौजूद `mime_type` फ़ील्ड से बदलें. [उदाहरण देखें](#structured-output).
- अपने मौजूदा `response_format` JSON स्कीमा को `{"type": "text", "schema": ...}` ऑब्जेक्ट में रैप करें. [उदाहरण देखें](#structured-output).
- (इमेज जनरेट करने की सुविधा) `image_config` को `generation_config` से `response_format` में मौजूद `{"type": "image", ...}` एंट्री में ले जाएं. [उदाहरण देखें](#image-config).
- (स्पीच जनरेशन) `response_modalities=["audio"]` को `response_format` में मौजूद `{"type": "audio"}` एंट्री से बदलें. [उदाहरण देखें](#audio-config).
- (टेक्स्ट, इमेज, और वीडियो वगैरह का इस्तेमाल करके) एक से ज़्यादा आउटपुट मोड का अनुरोध करते समय, किसी एक ऑब्जेक्ट से `response_format` को ऐरे में बदलें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया."],[],[]]
