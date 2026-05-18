---
source_url: https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=hi
fetched_at: 2026-05-18T05:15:11.689305+00:00
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

# Gemini Deep Research एजेंट

Gemini की Deep Research सुविधा वाला एजेंट, कई चरणों में रिसर्च से जुड़े टास्क को अपने-आप प्लान करता है, उन्हें एक्ज़ीक्यूट करता है, और उनका विश्लेषण करता है. यह सुविधा, Gemini की मदद से काम करती है. यह मुश्किल विषयों पर जानकारी देने के लिए, कई स्रोतों से डेटा इकट्ठा करती है. इसके बाद, यह उद्धरणों के साथ ज़्यादा जानकारी वाली रिपोर्ट तैयार करती है. नई सुविधाओं की मदद से, एजेंट के साथ मिलकर प्लान बनाया जा सकता है. साथ ही, एमसीपी सर्वर का इस्तेमाल करके बाहरी टूल से कनेक्ट किया जा सकता है. इसके अलावा, विज़ुअलाइज़ेशन (जैसे कि चार्ट और ग्राफ़) शामिल किए जा सकते हैं और दस्तावेज़ों को सीधे तौर पर इनपुट के तौर पर इस्तेमाल किया जा सकता है.

रिसर्च के कामों में, बार-बार खोज करना और पढ़ना शामिल होता है. इन्हें पूरा करने में कई मिनट लग सकते हैं. आपको बैकग्राउंड में एक्ज़ीक्यूशन (`background=true` सेट करें) का इस्तेमाल करना होगा, ताकि एजेंट को एसिंक्रोनस तरीके से चलाया जा सके. साथ ही, नतीजों के लिए पोल किया जा सके या अपडेट स्ट्रीम किए जा सकें. ज़्यादा जानकारी के लिए, [लंबे समय तक चलने वाले टास्क मैनेज करना](#long-running-tasks) लेख पढ़ें.

यहां दिए गए उदाहरण में, बैकग्राउंड में रिसर्च टास्क शुरू करने और नतीजों के लिए पोल करने का तरीका बताया गया है.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## इस्तेमाल किए जा सकने वाले वर्शन

Deep Research एजेंट दो वर्शन में उपलब्ध है:

- **डीप रिसर्च** (`deep-research-preview-04-2026`): इसे तेज़ी से और असरदार तरीके से काम करने के लिए डिज़ाइन किया गया है. यह क्लाइंट यूज़र इंटरफ़ेस (यूआई) पर वापस स्ट्रीम करने के लिए सबसे सही है.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): यह सुविधा, अपने-आप कॉन्टेक्स्ट इकट्ठा करने और उसे सिंथेसाइज़ करने के लिए सबसे ज़्यादा जानकारी देती है.

## साथ मिलकर प्लान बनाना

साथ मिलकर प्लान बनाने की सुविधा से, एजेंट के काम शुरू करने से पहले ही आपको रिसर्च की दिशा तय करने का कंट्रोल मिल जाता है. इस सुविधा के चालू होने पर, एजेंट तुरंत जवाब देने के बजाय, रिसर्च प्लान का सुझाव देता है. इसके बाद, आपके पास कई चरणों में बातचीत करके प्लान की समीक्षा करने, उसमें बदलाव करने या उसे स्वीकार करने का विकल्प होता है.

### पहला चरण: प्लान का अनुरोध करना

पहले इंटरैक्शन में `collaborative_planning=True` सेट करें. एजेंट, पूरी रिपोर्ट के बजाय रिसर्च प्लान दिखाता है.

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### दूसरा चरण: प्लान को बेहतर बनाना (ज़रूरी नहीं)

बातचीत जारी रखने और प्लान को बेहतर बनाने के लिए, `previous_interaction_id` का इस्तेमाल करें. प्लानिंग मोड में बने रहने के लिए, `collaborative_planning=True` को चालू रखें.

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### तीसरा चरण: मंज़ूरी देना और लागू करना

प्लान को स्वीकार करने और रिसर्च शुरू करने के लिए, `collaborative_planning=False` को सेट करें या इसे छोड़ दें.

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## विज़ुअलाइज़ेशन

`visualization` को `"auto"` पर सेट करने पर, एजेंट अपनी रिसर्च के नतीजों को बेहतर तरीके से दिखाने के लिए चार्ट, ग्राफ़, और अन्य विज़ुअल एलिमेंट जनरेट कर सकता है.
जनरेट की गई इमेज, जवाब के चरणों में शामिल होती हैं और `image` डेल्टा के तौर पर स्ट्रीम की जाती हैं. बेहतर नतीजे पाने के लिए, अपनी क्वेरी में साफ़ तौर पर विज़ुअल के लिए पूछें. उदाहरण के लिए, "ऐसे चार्ट शामिल करें जिनमें समय के साथ रुझान दिख रहे हों" या "बाज़ार हिस्सेदारी की तुलना करने वाले ग्राफ़ जनरेट करें." `visualization` को `"auto"` पर सेट करने से, यह सुविधा चालू हो जाती है. हालांकि, एजेंट सिर्फ़ तब विज़ुअल जनरेट करता है, जब प्रॉम्प्ट में इसके लिए अनुरोध किया जाता है.

### Python

```
import base64

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## इन टूल के साथ काम करता है

Deep Research की सुविधा, कई बिल्ट-इन और बाहरी टूल के साथ काम करती है. डिफ़ॉल्ट रूप से (जब कोई `tools` पैरामीटर नहीं दिया जाता है), एजेंट के पास Google Search, यूआरएल कॉन्टेक्स्ट, और कोड एक्ज़ीक्यूशन का ऐक्सेस होता है. एजेंट की क्षमताओं को सीमित करने या बढ़ाने के लिए, टूल के बारे में साफ़ तौर पर बताया जा सकता है.

| टूल | वैल्यू टाइप करें | ब्यौरा |
| --- | --- | --- |
| Google Search | `google_search` | सार्वजनिक वेब पर खोजें. यह सुविधा डिफ़ॉल्ट रूप से चालू होती है. |
| यूआरएल का कॉन्टेक्स्ट | `url_context` | वेब पेज पर मौजूद कॉन्टेंट को पढ़ना और उसकी खास जानकारी देना. यह सुविधा डिफ़ॉल्ट रूप से चालू होती है. |
| कोड को चलाना | `code_execution` | कैलकुलेशन और डेटा का विश्लेषण करने के लिए, कोड को एक्ज़ीक्यूट करना. यह सुविधा डिफ़ॉल्ट रूप से चालू होती है. |
| MCP Server | `mcp_server` | इससे बाहरी टूल को ऐक्सेस करने के लिए, रिमोट एमसीपी सर्वर से कनेक्ट किया जा सकता है. |
| फ़ाइल खोजने की सुविधा | `file_search` | अपलोड किए गए दस्तावेज़ कॉर्पस खोजें. |

### Google Search

सिर्फ़ Google Search को टूल के तौर पर इस्तेमाल करने की अनुमति दें:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### यूआरएल का कॉन्टेक्स्ट

एजेंट को वेब पेज पढ़ने और उनकी खास जानकारी देने की सुविधा दें:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### कोड को चलाना

एजेंट को कैलकुलेशन और डेटा के विश्लेषण के लिए कोड लागू करने की अनुमति दें:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### एमसीपी सर्वर

टूल कॉन्फ़िगरेशन में सर्वर `name` और `url` दें. आपके पास पुष्टि करने वाले क्रेडेंशियल पास करने का विकल्प भी होता है. साथ ही, यह तय किया जा सकता है कि एजेंट किन टूल को कॉल कर सकता है.

| फ़ील्ड | प्रकार | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `type` | `string` | हां | `"mcp_server"` होना चाहिए. |
| `name` | `string` | नहीं | एमसीपी सर्वर का डिसप्ले नेम. |
| `url` | `string` | नहीं | एमसीपी सर्वर के एंडपॉइंट का पूरा यूआरएल. |
| `headers` | `object` | नहीं | कुंजी-वैल्यू पेयर, सर्वर को किए गए हर अनुरोध के साथ एचटीटीपी हेडर के तौर पर भेजे जाते हैं. उदाहरण के लिए, पुष्टि करने वाले टोकन. |
| `allowed_tools` | `array` | नहीं | यह तय करें कि एजेंट, सर्वर के किन टूल को कॉल कर सकता है. |

#### बुनियादी इस्तेमाल

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### फ़ाइल खोजने की सुविधा

[फ़ाइल खोजें](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=hi) टूल का इस्तेमाल करके, एजेंट को अपने डेटा का ऐक्सेस दें.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## निर्देश देने और फ़ॉर्मैट करने की सुविधा

अपने प्रॉम्प्ट में फ़ॉर्मैटिंग से जुड़े खास निर्देश देकर, एजेंट के जवाब को अपनी ज़रूरत के हिसाब से बनाया जा सकता है. इससे रिपोर्ट को खास सेक्शन और सब-सेक्शन में व्यवस्थित किया जा सकता है. साथ ही, डेटा टेबल शामिल की जा सकती हैं या अलग-अलग ऑडियंस (जैसे, "तकनीकी," "कार्यकारी," "सामान्य") के हिसाब से टोन को अडजस्ट किया जा सकता है.

अपने इनपुट टेक्स्ट में, आउटपुट का फ़ॉर्मैट साफ़ तौर पर बताएं.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## मल्टीमॉडल इनपुट

Deep Research की सुविधा में, मल्टीमॉडल इनपुट का इस्तेमाल किया जा सकता है. जैसे, इमेज और दस्तावेज़ (PDF). इससे एजेंट को विज़ुअल कॉन्टेंट का विश्लेषण करने और वेब पर आधारित रिसर्च करने की सुविधा मिलती है. यह रिसर्च, दिए गए इनपुट के हिसाब से की जाती है.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### दस्तावेज़ को समझना

दस्तावेज़ों को सीधे मल्टीमॉडल इनपुट के तौर पर पास करें. एजेंट, दिए गए दस्तावेज़ों का विश्लेषण करता है और उनके कॉन्टेंट के आधार पर रिसर्च करता है.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## लंबे समय तक चलने वाले टास्क मैनेज करना

Deep Research की सुविधा, कई चरणों में काम करती है. इसमें प्लानिंग करना, खोजना, पढ़ना, और लिखना शामिल है. आम तौर पर, यह साइकल, सिंक्रोनस एपीआई कॉल के लिए तय की गई स्टैंडर्ड टाइमआउट सीमा से ज़्यादा होता है.

एजेंट को `background=True` का इस्तेमाल करना होगा. यह एपीआई, `Interaction` ऑब्जेक्ट का कुछ हिस्सा तुरंत दिखाता है. पोलिंग के लिए इंटरैक्शन वापस पाने के लिए, `id` प्रॉपर्टी का इस्तेमाल किया जा सकता है. इंटरैक्शन की स्थिति `in_progress` से बदलकर `completed` या `failed` हो जाएगी.

### स्ट्रीमिंग

Deep Research की सुविधा, स्ट्रीमिंग की सुविधा के साथ काम करती है. इससे आपको रिसर्च की प्रोग्रेस के बारे में रीयल-टाइम में अपडेट मिलते हैं. जैसे, सोच की खास जानकारी, टेक्स्ट आउटपुट, और जनरेट की गई इमेज.
आपको `stream=True` और `background=True` को सेट करना होगा. स्ट्रीमिंग से जुड़ी पूरी गाइड के लिए, [स्ट्रीमिंग के दौरान होने वाली बातचीत](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=hi) लेख पढ़ें. इसमें इवेंट के टाइप, टूल स्ट्रीमिंग, और सोचने-समझने से जुड़ी जानकारी शामिल है.

जवाब तैयार करने के दौरान की गई कार्रवाइयों (सोच) और प्रोग्रेस के अपडेट पाने के लिए, आपको **सोच के बारे में खास जानकारी** की सुविधा चालू करनी होगी. इसके लिए, `agent_config` में जाकर `thinking_summaries` को `"auto"` पर सेट करें. इसके बिना, स्ट्रीम सिर्फ़ फ़ाइनल नतीजे दिखा सकती है.

#### स्ट्रीम इवेंट के टाइप

| इवेंट किस तरह का है | डेल्टा टाइप | ब्यौरा |
| --- | --- | --- |
| `step.delta` | `thought` | एजेंट से मिला, लॉजिक वाला जवाब. |
| `step.delta` | `text` | फ़ाइनल टेक्स्ट आउटपुट का हिस्सा. |
| `step.delta` | `image` | जनरेट की गई इमेज (base64 कोड में बदली गई). |

यहां दिए गए उदाहरण में, रिसर्च टास्क शुरू किया जाता है और स्ट्रीम को प्रोसेस किया जाता है. साथ ही, इसमें अपने-आप फिर से कनेक्ट होने की सुविधा होती है. यह `interaction_id` और `last_event_id` को ट्रैक करता है, ताकि कनेक्शन बंद होने पर (उदाहरण के लिए, 600 सेकंड के टाइमआउट के बाद), यह वहीं से शुरू हो सके जहां इसे छोड़ा गया था.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## फ़ॉलो-अप वाले सवाल पूछना और बातचीत करना

एजेंट से फ़ाइनल रिपोर्ट मिलने के बाद, `previous_interaction_id` का इस्तेमाल करके बातचीत जारी रखी जा सकती है. इससे आपको पूरी रिसर्च को फिर से शुरू किए बिना, रिसर्च के किसी खास सेक्शन के बारे में ज़्यादा जानकारी पाने, उसे छोटा करने या उसके बारे में ज़्यादा जानकारी देने के लिए कहा जा सकता है.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Gemini Deep Research Agent का इस्तेमाल कब करना चाहिए

Deep Research एक **एजेंट** है, न कि सिर्फ़ एक मॉडल. यह उन वर्कलोड के लिए सबसे सही है जिनमें कम इंतज़ार के समय वाली चैट के बजाय, "ऐनलिस्ट-इन-अ-बॉक्स" अप्रोच की ज़रूरत होती है.

| सुविधा | Gemini के स्टैंडर्ड मॉडल | Gemini Deep Research एजेंट |
| --- | --- | --- |
| **लेटेंसी** | सेकंड | मिनट (एसिंक/बैकग्राउंड) |
| **प्रोसेस** | जनरेट करें -> आउटपुट | प्लान -> खोजें -> पढ़ें -> दोहराएं -> आउटपुट |
| **आउटपुट** | बातचीत वाला टेक्स्ट, कोड, कम शब्दों में जानकारी | ज़्यादा जानकारी वाली रिपोर्ट, लंबी अवधि का विश्लेषण, तुलना करने वाली टेबल |
| **इन कामों के लिए सबसे सही** | चैटबॉट, डेटा निकालना, क्रिएटिव राइटिंग | मार्केट ऐनलिसिस, ज़रूरी जांच, साहित्य की समीक्षाएं, प्रतिस्पर्धी लैंडस्केपिंग |

## एजेंट का कॉन्फ़िगरेशन

Deep Research, व्यवहार को कंट्रोल करने के लिए `agent_config` पैरामीटर का इस्तेमाल करता है.
इसे डिक्शनरी के तौर पर पास करें. इसमें ये फ़ील्ड शामिल होने चाहिए:

| फ़ील्ड | टाइप | डिफ़ॉल्ट | ब्यौरा |
| --- | --- | --- | --- |
| `type` | `string` | ज़रूरी है | `"deep-research"` होना चाहिए. |
| `thinking_summaries` | `string` | `"none"` | स्ट्रीमिंग के दौरान तर्क के इंटरमीडिएट चरणों को पाने के लिए, इसे `"auto"` पर सेट करें. इसे बंद करने के लिए, `"none"` पर सेट करें. |
| `visualization` | `string` | `"auto"` | एजेंट से जनरेट होने वाले चार्ट और इमेज की सुविधा चालू करने के लिए, इसे `"auto"` पर सेट करें. इसे बंद करने के लिए, `"off"` पर सेट करें. |
| `collaborative_planning` | `boolean` | `false` | रिसर्च शुरू होने से पहले, कई बार प्लान की समीक्षा करने की सुविधा चालू करने के लिए, इसे `true` पर सेट करें. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## उपलब्धता और कीमत

Google AI Studio और Gemini API में, Interactions API का इस्तेमाल करके Gemini Deep Research Agent को ऐक्सेस किया जा सकता है.

कीमत, [इस्तेमाल के हिसाब से पेमेंट करने वाले मॉडल](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#pricing-for-agents) के हिसाब से तय की जाती है. यह Gemini के बुनियादी मॉडल और एजेंट के इस्तेमाल किए गए टूल के हिसाब से तय होती है. स्टैंडर्ड चैट के अनुरोधों में, एक अनुरोध से एक आउटपुट मिलता है. हालांकि, Deep Research के टास्क में एजेंटिक वर्कफ़्लो होता है. एक अनुरोध करने पर, प्लानिंग, खोजने, पढ़ने, और तर्क करने की प्रोसेस अपने-आप शुरू हो जाती है.

### अनुमानित लागतें

रिसर्च की ज़रूरत के हिसाब से लागत अलग-अलग होती है. एजेंट अपने-आप यह तय करता है कि आपके प्रॉम्प्ट का जवाब देने के लिए, कितनी जानकारी पढ़ना और खोजना ज़रूरी है.

- **Deep Research** (`deep-research-preview-04-2026`): किसी ऐसी क्वेरी के लिए जिसमें सामान्य विश्लेषण की ज़रूरत होती है, एजेंट ~80 सर्च क्वेरी, ~2,50,000 इनपुट टोकन (जिनमें से ~50 से 70% कैश मेमोरी में सेव होते हैं), और ~60,000 आउटपुट टोकन का इस्तेमाल कर सकता है.
  - **कुल अनुमानित शुल्क:** हर टास्क के लिए ~100 रुपये से 300 रुपये
- **Deep Research Max** (`deep-research-max-preview-04-2026`): प्रतिस्पर्धी कंपनियों के बारे में ज़्यादा जानकारी पाने या ज़रूरी जांच करने के लिए, एजेंट ज़्यादा से ज़्यादा ~160 खोज क्वेरी, ~900 हज़ार इनपुट टोकन (जिनमें से ~50 से 70% कैश मेमोरी में सेव होते हैं) और ~80 हज़ार आउटपुट टोकन का इस्तेमाल कर सकता है.
  - **कुल अनुमानित शुल्क:** हर टास्क के लिए ~300 रुपये से 700 रुपये

## सुरक्षा से जुड़ी बातें

किसी एजेंट को वेब और आपकी निजी फ़ाइलों का ऐक्सेस देने से पहले, सुरक्षा से जुड़े जोखिमों के बारे में सोच-विचार करना ज़रूरी है.

- **फ़ाइलों का इस्तेमाल करके प्रॉम्प्ट इंजेक्ट करना:** एजेंट, आपकी दी गई फ़ाइलों का कॉन्टेंट पढ़ता है. पक्का करें कि अपलोड किए गए दस्तावेज़ (पीडीएफ़, टेक्स्ट फ़ाइलें) भरोसेमंद सोर्स से लिए गए हों. नुकसान पहुंचाने वाली फ़ाइल में ऐसा छिपा हुआ टेक्स्ट हो सकता है जिसे एजेंट के आउटपुट में बदलाव करने के लिए डिज़ाइन किया गया हो.
- **वेब कॉन्टेंट से जुड़े जोखिम:** एजेंट, सार्वजनिक वेब पर खोज करता है. हम सुरक्षा के लिए बेहतर फ़िल्टर लागू करते हैं. हालांकि, इस बात का खतरा बना रहता है कि एजेंट को नुकसान पहुंचाने वाले वेब पेजों का सामना करना पड़ सकता है और वह उन्हें प्रोसेस कर सकता है. हमारा सुझाव है कि जवाब में दिए गए `citations` की समीक्षा करके, स्रोतों की पुष्टि करें.
- **डेटा चोरी:** अगर आपने एजेंट को वेब ब्राउज़ करने की अनुमति दी है, तो संवेदनशील
  आंतरिक डेटा की खास जानकारी देने के लिए एजेंट से अनुरोध करते समय सावधानी बरतें.

## सबसे सही तरीके

- **जिन सवालों के जवाब नहीं पता उनके लिए प्रॉम्प्ट:** एजेंट को यह निर्देश दें कि वह मौजूद न होने वाले डेटा को कैसे मैनेज करे.
  उदाहरण के लिए, अपने प्रॉम्प्ट में *"अगर साल 2025 के लिए कुछ खास आंकड़े उपलब्ध नहीं हैं, तो अनुमान लगाने के बजाय साफ़ तौर पर बताएं कि वे अनुमानित हैं या उपलब्ध नहीं हैं"* जोड़ें.
- **संदर्भ दें:** एजेंट को रिसर्च करने के लिए, बैकग्राउंड की जानकारी या सीधे तौर पर इनपुट प्रॉम्प्ट में पाबंदियां दें.
- **साथ मिलकर प्लान बनाने की सुविधा का इस्तेमाल करें:** मुश्किल क्वेरी के लिए, साथ मिलकर प्लान बनाने की सुविधा चालू करें. इससे रिसर्च प्लान को लागू करने से पहले, उसकी समीक्षा की जा सकेगी और उसे बेहतर बनाया जा सकेगा.
- **मल्टीमॉडल इनपुट:** Deep Research Agent, मल्टीमॉडल इनपुट के साथ काम करता है.
  इसका इस्तेमाल सावधानी से करें, क्योंकि इससे लागत बढ़ जाती है और कॉन्टेक्स्ट विंडो ओवरफ़्लो होने का खतरा बढ़ जाता है.

## सीमाएं

- **बीटा वर्शन की स्थिति**: Interactions API, सार्वजनिक बीटा वर्शन में उपलब्ध है. सुविधाओं और स्कीमा में बदलाव हो सकता है.
- **कस्टम टूल:** फ़िलहाल, कस्टम फ़ंक्शन कॉलिंग टूल उपलब्ध नहीं कराए जा सकते. हालांकि, डीप रिसर्च एजेंट के साथ रिमोट एमसीपी (मॉडल कॉन्टेक्स्ट प्रोटोकॉल) सर्वर का इस्तेमाल किया जा सकता है.
- **स्ट्रक्चर्ड आउटपुट:** फ़िलहाल, डीप रिसर्च एजेंट स्ट्रक्चर्ड आउटपुट के साथ काम नहीं करता.
- **रिसर्च में लगने वाला ज़्यादा से ज़्यादा समय:** Deep Research एजेंट को रिसर्च करने में ज़्यादा से ज़्यादा 60 मिनट लगते हैं. ज़्यादातर टास्क 20 मिनट में पूरे हो जाने चाहिए.
- **स्टोर से जुड़ी ज़रूरी शर्तें:** `background=True` का इस्तेमाल करके एजेंट को लागू करने के लिए, `store=True` ज़रूरी है.
- **Google Search:** [Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=hi) डिफ़ॉल्ट रूप से चालू होता है. साथ ही, भरोसेमंद स्रोतों से मिली जानकारी के आधार पर तैयार किए गए नतीजों पर [कुछ पाबंदियां](https://ai.google.dev/gemini-api/terms?hl=hi#use-restrictions2) लागू होती हैं.

## आगे क्या करना है

- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi) के बारे में ज़्यादा जानें.
- [फ़ाइल खोजें](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=hi) टूल का इस्तेमाल करके, अपने डेटा को इस्तेमाल करने का तरीका जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-16 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-16 (UTC) को अपडेट किया गया."],[],[]]
