---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ar
fetched_at: 2026-06-29T05:39:19.771334+00:00
title: "\u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a Interactions API: \u062f\u0644\u064a\u0644 \u0646\u0642\u0644 \u0627\u0644\u062a\u063a\u064a\u064a\u0631\u0627\u062a \u063a\u064a\u0631 \u0627\u0644\u0645\u062a\u0648\u0627\u0641\u0642\u0629 (\u0645\u0627\u064a\u0648 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# واجهة برمجة التطبيقات Interactions API: دليل نقل التغييرات غير المتوافقة (مايو 2026)

تُجري واجهة برمجة التطبيقات Interactions API في الإصدار `v1beta` تغييرات غير متوافقة مع الإصدارات السابقة تؤدي إلى إعادة هيكلة شكل واجهة برمجة التطبيقات لدعم الإمكانات المستقبلية، مثل التوجيه أثناء الرحلة واستدعاءات الأدوات غير المتزامنة. توضّح هذه الصفحة التغييرات وتوفّر أمثلة على الرموز البرمجية قبل وبعد التغييرات لمساعدتك في نقل البيانات. هناك فئتان من التغييرات:

1. [**مخطط الخطوات**](#steps-schema): تحلّ مصفوفة `steps` جديدة محلّ مصفوفة
   `outputs`، ما يوفّر مخططًا زمنيًا منظّمًا لكل دورة تفاعل.
2. [**إعداد تنسيق الإخراج**](#output-format-config): يوحّد متعدد الأشكال الجديد
   `response_format` جميع عناصر التحكّم في تنسيق الإخراج ويزيل
   `response_mime_type`.

اتّبِع الخطوات الواردة في [كيفية نقل البيانات إلى المخطط الجديد](#how-to-migrate) لتعديل عملية التكامل.

## التغيير الأساسي: من `outputs` إلى `steps`

يستبدل المخطط الجديد مصفوفة `outputs` بمصفوفة `steps`.

- **الإصدار القديم**: كانت الردود تعرض مصفوفة `outputs` مسطّحة لا تحتوي إلا على المحتوى الذي تم إنشاؤه بواسطة النموذج.
- **المخطط الجديد**: تعرض الردود مصفوفة `steps` تحتوي على خطوات منظّمة مع مميّزات النوع.

لا يعرض `POST /interactions` سوى خطوات الإخراج. يعرض `GET /interactions/{id}` المخطط الزمني الكامل للخطوات، بما في ذلك خطوة `user_input` الأولية.

### الإدخال/الإخراج الأساسي (أحادي)

#### قبل (الإصدار القديم)

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

### راحة

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

#### بعد (المخطط الجديد)

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

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### راحة

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

### استدعاء الدالة

يبقى هيكل الطلب بدون تغيير، ولكن يستبدل الردّ محتوى `outputs` المسطّح بخطوات منظّمة.

#### قبل (الإصدار القديم)

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

### راحة

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

#### بعد (المخطط الجديد)

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

### راحة

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

### أدوات من جهة الخادم

تنتج الأدوات من جهة الخادم (مثل "بحث Google" أو "تنفيذ الرموز البرمجية") الآن أنواعًا معيّنة من الخطوات في مصفوفة `steps`. في حين أنّ المخطط القديم كان يعرض هذه العمليات كأنواع محتوى معيّنة ضِمن مصفوفة `outputs`، ينقلها المخطط الجديد إلى مصفوفة `steps`. تستخدِم الأمثلة التالية "بحث Google".

#### قبل (الإصدار القديم)

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

### راحة

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

#### بعد (المخطط الجديد)

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

### راحة

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

### البث

يعرض البث أنواعًا جديدة من الأحداث:

#### أنواع الأحداث الجديدة

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### أنواع الأحداث التي تم إيقافها

يتم استبدال أنواع الأحداث القديمة التالية بالأحداث الجديدة المذكورة أعلاه:

- `interaction.start` ← `interaction.created`
- `content.start` ← `step.start`
- `content.delta` ← `step.delta`
- `content.stop` ← `step.stop`
- `interaction.complete` ← `interaction.completed`
- `interaction.status_update` ← تم استبدالها بـ `interaction.in_progress` و`interaction.requires_action` وما إلى ذلك

**استدعاءات الدوال في البث**: عند استخدام البث مع استدعاء الدوال،
يقدّم الحدث `step.start` اسم الدالة، وتعمل أحداث `step.delta` على
بثّ الوسيطات كسلاسل JSON جزئية (باستخدام `arguments_delta`). يجب
تجميع هذه التغييرات الجزئية للحصول على الوسيطات الكاملة. يختلف ذلك عن الاستدعاءات الأحادية التي تتلقّى فيها كائن استدعاء الدالة الكامل مرة واحدة.

#### أمثلة

##### قبل (الإصدار القديم)

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

### راحة

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

##### بعد (المخطط الجديد)

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

### راحة

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

### سجلّ المحادثات بدون حالة

إذا كنت تدير سجلّ المحادثات يدويًا على جانب العميل (حالة الاستخدام بدون حالة)، عليك تعديل طريقة ربط الأدوار السابقة.

- **الإصدار القديم**: غالبًا ما كان المطوّرون يجمعون مصفوفة `outputs` من الردود ويعيدون إرسالها في حقل `input` في الدور التالي.
- **المخطط الجديد**: عليك الآن جمع مصفوفة `steps` من الردّ وتمريرها في حقل `input` للطلب التالي، مع إلحاق دورة المستخدم الجديدة كخطوة `user_input`.

## إعداد تنسيق الإخراج: تغييرات `response_format`

يوحّد الإصدار المعدَّل من واجهة برمجة التطبيقات جميع عناصر التحكّم في تنسيق الإخراج في حقل `response_format` موحّد ومتعدد الأشكال. يؤدي ذلك إلى مركزة إعداد الإخراج على المستوى الأعلى ويحافظ على تركيز `generation_config` على سلوك النموذج (مثل درجة العشوائية وأعلى احتمال تراكمي والتفكير).

### أهم التغييرات

- **تزيل واجهة برمجة التطبيقات `response_mime_type`.** يمكنك الآن تحديد نوع MIME لكل إدخال تنسيق ضِمن `response_format`.
- **أصبح `response_format` الآن كائنًا (أو مصفوفة) متعدد الأشكال.** يحتوي كل إدخال على مميّز `type` (`text` أو `audio` أو `image`) وحقول خاصة بالنوع. لطلب أوضاع إخراج متعددة، مرِّر مصفوفة من إدخالات التنسيق.
- **ينتقل `image_config` من `generation_config` إلى `response_format`.**
  يمكنك الآن تحديد إعدادات إخراج الصور، مثل `aspect_ratio` و`image_size`
  في إدخال `response_format` مع `"type": "image"`.

### ناتج منظَّم (JSON)

يزيل المخطط الجديد حقل `response_mime_type`. بدلاً من ذلك، حدِّد نوع MIME ومخطط JSON ضِمن كائن `response_format` مع `"type": "text"`.

#### قبل (الإصدار القديم)

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

### راحة

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

#### بعد (المخطط الجديد)

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

### راحة

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

### إعدادات الصور

يزيل المخطط الجديد `image_config` من `generation_config`. يمكنك الآن تحديد إعدادات إخراج الصور
في إدخال `response_format`مع `"type": "image"`.

#### قبل (الإصدار القديم)

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

### راحة

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

#### بعد (المخطط الجديد)

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

### راحة

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

### إعدادات الصوت

يستبدل المخطط الجديد `response_modalities: ["audio"]` بإدخال `response_format` من `"type": "audio"`.

#### قبل (الإصدار القديم)

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

### راحة

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

#### بعد (المخطط الجديد)

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

### راحة

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

لطلب أوضاع إخراج متعددة (على سبيل المثال، النص والصوت معًا)، مرِّر مصفوفة من إدخالات التنسيق إلى `response_format` بدلاً من كائن واحد.

## كيفية نقل البيانات إلى المخطط الجديد

### مستخدِمو حزمة تطوير البرامج (SDK)

رقِّ إلى أحدث إصدار من حزمة تطوير البرامج (Python ≥2.0.0 وJavaScript ≥2.0.0). تختارك حزمة تطوير البرامج (SDK) تلقائيًا في المخطط الجديد، ولا تحتاج إلى إجراء أي تغييرات على الرمز البرمجي بخلاف تعديل طريقة قراءة الردود (راجِع الأمثلة أعلاه). يُرجى العِلم أنّه لا يتم دعم سوى المخطط الجديد في إصدارات حزمة تطوير البرامج (SDK) هذه. ستستمر إصدارات حزمة تطوير البرامج (SDK) الأقدم (Python 1.x.x وJavaScript 1.x.x) في العمل إلى أن تتم إزالة المخطط القديم في **8 يونيو 2026**.

### مستخدِمو REST API

أضِف العنوان `Api-Revision: 2026-05-20` إلى طلباتك للاشتراك في المخطط الجديد الآن. بعد **26 مايو** ، يصبح المخطط الجديد هو المخطط التلقائي لجميع
الطلبات. يمكنك إيقاف الاشتراك مؤقتًا باستخدام `Api-Revision: 2026-05-07`
حتى **8 يونيو**، عندما تزيل واجهة برمجة التطبيقات المخطط القديم نهائيًا.

### المخطط الزمني

| التاريخ | المرحلة | مستخدِمو حزمة تطوير البرامج (SDK) | مستخدِمو REST API |
| --- | --- | --- | --- |
| **‫7 مايو** | اشتراك | يتوفّر إصدار جديد من حزمة تطوير البرامج (SDK) (Python ≥2.0.0 وJS ≥2.0.0). رقِّ للحصول على المخطط الجديد تلقائيًا. | أضِف العنوان `Api-Revision: 2026-05-20` للاشتراك. يبقى المخطط القديم هو المخطط التلقائي. |
| **‫26 مايو** | قلب تلقائي | لا يلزم اتّخاذ أي إجراء إذا تم الترقية من قبل. تستمر حزم تطوير البرامج (SDK) الأقدم (Python 1.x.x وJS 1.x.x) في العمل ولكنها تعرض الردود القديمة. | أصبح المخطط الجديد هو المخطط التلقائي الآن. أرسِل العنوان `Api-Revision: 2026-05-07` لإيقاف الاشتراك. |
| **‫8 يونيو** | الغروب | ستتوقف إصدارات حزمة تطوير البرامج (SDK) من Python 1.x.x وJS 1.x.x عن العمل لاستدعاءات Interactions API. | تمت إزالة المخطط القديم لواجهة برمجة التطبيقات Interactions API. تم تجاهل العنوان `Api-Revision`. |

## قائمة التحقق من الترحيل

### مخطط الخطوات (`steps`)

- عدِّل الرمز البرمجي لقراءة محتوى الردّ من مصفوفة `steps` بدلاً من `outputs`. [اطّلع على أمثلة](#basic-unary).
- تأكَّد من أنّ الرمز البرمجي يعالج نوعَي الخطوات `user_input` و`model_output`. [اطّلع على أمثلة](#basic-unary).
- (استدعاء الدالة) عدِّل الرمز البرمجي للعثور على خطوات `function_call` في مصفوفة `steps`. [اطّلع على أمثلة](#function-calling).
- (أدوات من جهة الخادم) عدِّل الرمز البرمجي لمعالجة الخطوات الخاصة بالأداة (مثل `google_search_call` و`google_search_result`). [اطّلِع على أمثلة](#server-side-tools).
- (السجلّ بدون حالة) عدِّل إدارة السجلّ لتمرير مصفوفة `steps` في حقل `input` للطلب التالي. [اطّلع على التفاصيل](#stateless-history).
- (البث فقط) عدِّل العميل للاستماع إلى أنواع أحداث SSE الجديدة (`interaction.created` و`step.delta` وما إلى ذلك). [اطّلع على أمثلة](#streaming).

### إعداد تنسيق الإخراج (`response_format`)

- استبدِل `response_mime_type` بحقل `mime_type` ضِمن `response_format`. [اطّلع على أمثلة](#structured-output).
- غلِّف مخطط JSON الحالي `response_format` ضِمن كائن `{"type": "text", "schema": ...}`. [اطّلع على أمثلة](#structured-output).
- (إنشاء الصور) انقل `image_config` من `generation_config` إلى إدخال `{"type": "image", ...}` في `response_format`. [اطّلع على أمثلة](#image-config).
- (إنشاء الكلام) استبدِل `response_modalities=["audio"]` بإدخال `{"type": "audio"}` في `response_format`. [اطّلع على أمثلة](#audio-config).
- (متعدد الوسائط) حوِّل `response_format` من كائن واحد إلى مصفوفة عند طلب أوضاع إخراج متعددة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
