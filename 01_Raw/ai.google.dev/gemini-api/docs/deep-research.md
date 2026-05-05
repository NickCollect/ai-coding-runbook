---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=ar
fetched_at: 2026-05-05T20:45:23.161631+00:00
title: "\u0648\u0643\u064a\u0644 Deep Research \u0641\u064a Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# وكيل Deep Research في Gemini

يخطّط وكيل Deep Research من Gemini وينفّذ ويجمع مهام البحث المتعدّدة الخطوات بشكل مستقل. يستند هذا المنتج إلى Gemini، ويتيح التنقّل في مساحات شاسعة من المعلومات المعقّدة لإنشاء تقارير مفصّلة مع ذكر المصادر. تتيح لك الإمكانات الجديدة التخطيط بشكل تعاوني مع الوكيل، والربط بأدوات خارجية باستخدام خوادم MCP، وتضمين رسومات توضيحية (مثل المخططات والرسوم البيانية)، وتقديم المستندات مباشرةً كمدخلات.

تتضمّن مهام البحث عمليات بحث وقراءة متكرّرة، وقد تستغرق عدة دقائق لإكمالها. يجب استخدام التنفيذ في الخلفية (ضبط `background=true`) لتشغيل الوكيل بشكل غير متزامن وطلب النتائج أو بث التحديثات. لمزيد من التفاصيل، اطّلِع على مقالة [التعامل مع المهام التي تستغرق وقتًا طويلاً](#long-running-tasks).

يوضّح المثال التالي كيفية بدء مهمة بحث في الخلفية
والتحقّق من النتائج.

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
        print(interaction.outputs[-1].text)
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
        console.log(result.outputs[result.outputs.length - 1].text);
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## الإصدارات المتوافقة

يتوفّر وكيل Deep Research بإصدارَين:

- **Deep Research** (`deep-research-preview-04-2026`): تم تصميمه ليكون سريعًا وفعّالاً، وهو مثالي لعرضه في واجهة مستخدم العميل.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): أقصى قدر من الشمولية لعملية جمع السياق وتلخيصه بشكل آلي

## التخطيط التعاوني

تمنحك ميزة "التخطيط التعاوني" إمكانية التحكّم في اتجاه البحث
قبل أن يبدأ الوكيل عمله. عند تفعيل هذه الميزة، يعرض الوكيل خطة بحث مقترَحة بدلاً من تنفيذها على الفور. يمكنك بعد ذلك مراجعة الخطة أو تعديلها أو الموافقة عليها من خلال التفاعلات المتعدّدة الأدوار.

### الخطوة 1: طلب خطة

اضبط `collaborative_planning=True` في التفاعل الأول. يعرض الوكيل خطة بحث بدلاً من تقرير كامل.

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
print(result.outputs[-1].text)
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
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
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

### الخطوة 2: تحسين الخطة (اختيارية)

استخدِم `previous_interaction_id` لمواصلة المحادثة وتكرار الخطة. اضغط على `collaborative_planning=True` للبقاء في وضع التخطيط.

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
print(result.outputs[-1].text)
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
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
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

### الخطوة 3: الموافقة والتنفيذ

اضبط القيمة على `collaborative_planning=False` (أو احذفها) للموافقة على الخطة وبدء البحث.

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
print(result.outputs[-1].text)
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
console.log(result.outputs[result.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
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

## التمثيل البصري

عندما تكون قيمة `visualization` هي `"auto"`، يمكن للوكيل إنشاء رسومات بيانية ومخططات وعناصر مرئية أخرى لدعم نتائج البحث.
يتم تضمين الصور التي تم إنشاؤها في نواتج الردود ويتم بثها كقيم
`image` دلتا. للحصول على أفضل النتائج، اطلب بشكل صريح تضمين عناصر مرئية في طلب البحث، مثلاً "تضمين رسوم بيانية تعرض المؤشرات بمرور الوقت" أو "إنشاء رسومات تقارن الحصة السوقية". يؤدي ضبط `visualization` على
`"auto"` إلى تفعيل هذه الإمكانية، ولكن لا ينشئ الوكيل مرئيات إلا
عندما يطلبها الطلب.

### Python

```
import base64
from IPython.display import Image, display

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

for output in result.outputs:
    if output.type == "text":
        print(output.text)
    elif output.type == "image" and output.data:
        image_bytes = base64.b64decode(output.data)
        print(f"Received image: {len(image_bytes)} bytes")
        # To display in a Jupyter notebook:
        # from IPython.display import display, Image
        # display(Image(data=image_bytes))
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

for (const output of result.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    } else if (output.type === 'image' && output.data) {
        console.log(`[Image Output: ${output.data.substring(0, 20)}...]`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
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

## الأدوات المتوافقة

تتيح ميزة Deep Research استخدام أدوات متعددة مضمّنة وخارجية. بشكل تلقائي (عند عدم توفير المَعلمة `tools`)، يمكن للوكيل الوصول إلى &quot;بحث Google&quot; و&quot;سياق عنوان URL&quot; و&quot;تنفيذ الرمز&quot;. يمكنك تحديد الأدوات بشكل صريح لحظر إمكانات الوكيل أو توسيعها.

| الأداة | نوع القيمة | الوصف |
| --- | --- | --- |
| بحث Google | `google_search` | البحث في شبكة الويب المتاحة للجميع يكون مفعَّلاً تلقائيًا. |
| سياق عنوان URL | `url_context` | قراءة محتوى صفحة الويب وتلخيصه يكون مفعَّلاً تلقائيًا. |
| تنفيذ الرموز البرمجية | `code_execution` | تنفيذ الرموز البرمجية لإجراء العمليات الحسابية وتحليل البيانات يكون مفعَّلاً تلقائيًا. |
| خادم MCP | `mcp_server` | الربط بخوادم MCP البعيدة للوصول إلى الأدوات الخارجية |
| البحث عن الملفات | `file_search` | البحث في مجموعات مستنداتك المحمّلة |

### بحث Google

تفعيل "بحث Google" بشكلٍ صريح كالأداة الوحيدة:

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### سياق عنوان URL

امنح الوكيل إذن قراءة وتلخيص صفحات ويب معيّنة:

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### تنفيذ الرموز البرمجية

السماح للوكيل بتنفيذ الرموز لإجراء العمليات الحسابية وتحليل البيانات:

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Calculate the 50th Fibonacci number.",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### خوادم MCP

قدِّم الخادم `name` و`url` في إعدادات الأدوات. يمكنك أيضًا تمرير بيانات اعتماد المصادقة وتقييد الأدوات التي يمكن للوكيل استدعاؤها.

| الحقل | النوع | مطلوب | الوصف |
| --- | --- | --- | --- |
| `type` | `string` | نعم | يجب أن تكون `"mcp_server"`. |
| `name` | `string` | لا | اسم معروض لخادم MCP. |
| `url` | `string` | لا | عنوان URL الكامل لنقطة نهاية خادم MCP |
| `headers` | `object` | لا | أزواج المفتاح والقيمة التي يتم إرسالها كعناوين HTTP مع كل طلب إلى الخادم (على سبيل المثال، رموز المصادقة المميزة). |
| `allowed_tools` | `array` | لا | تحديد الأدوات التي يمكن للوكيل استدعاؤها من الخادم |

#### الاستخدام الأساسي

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
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

### البحث عن الملفات

امنح الوكيل إذن الوصول إلى بياناتك الخاصة باستخدام أداة [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar).

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## إمكانية التوجيه والتنسيق

يمكنك توجيه ناتج الوكيل من خلال تقديم تعليمات تنسيق محدّدة في طلبك. يتيح لك ذلك تنظيم التقارير في أقسام وأقسام فرعية محدّدة، أو تضمين جداول البيانات، أو تعديل النبرة لتناسب شرائح جمهور مختلفة (مثل "فنية" أو "تنفيذية" أو "عادية").

حدِّد تنسيق الناتج المطلوب بشكل واضح في النص الذي تدخله.

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## إدخالات متعددة الوسائط

تتيح ميزة Deep Research إدخال طلبات متعددة الوسائط، بما في ذلك الصور والمستندات (ملفات PDF)، ما يسمح للوكيل بتحليل المحتوى المرئي وإجراء بحث مستنِد إلى الويب مع مراعاة السياق الذي توفّره الطلبات.

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
        print(interaction.outputs[-1].text)
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
        console.log(result.outputs[result.outputs.length - 1].text);
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### فهم المستندات

تمرير المستندات مباشرةً كإدخال متعدد الوسائط يحلّل الوكيل المستندات المقدَّمة ويجري بحثًا استنادًا إلى محتواها.

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## التعامل مع المهام الطويلة المدى

‫Deep Research هي عملية متعددة الخطوات تشمل التخطيط والبحث والقراءة والكتابة. يتجاوز هذا الإجراء عادةً حدود المهلة الزمنية العادية لطلبات البيانات المتزامنة من واجهة برمجة التطبيقات.

على الموظفين استخدام `background=True`. تعرض واجهة برمجة التطبيقات عنصر `Interaction` جزئيًا على الفور. يمكنك استخدام السمة `id` لاسترداد تفاعل مع استطلاع. ستنتقل حالة التفاعل من
`in_progress` إلى `completed` أو `failed`.

### البث

تتيح ميزة Deep Research إمكانية البث المباشر لتلقّي آخر المعلومات في الوقت الفعلي حول تقدّم البحث، بما في ذلك ملخّصات الأفكار والنص الناتج والصور التي تم إنشاؤها.
يجب ضبط `stream=True` و`background=True`.

لتلقّي خطوات الاستدلال الوسيطة (الأفكار) وإشعارات التقدّم، عليك تفعيل **ملخّصات التفكير** من خلال ضبط `thinking_summaries` على `"auto"` في `agent_config`. وبدون ذلك، قد لا يوفّر البث سوى النتائج النهائية.

#### أنواع أحداث البث

| نوع الحدث | نوع التغيير | الوصف |
| --- | --- | --- |
| `content.delta` | `thought_summary` | خطوة الاستدلال الوسيطة من الوكيل |
| `content.delta` | `text` | جزء من النص النهائي الناتج |
| `content.delta` | `image` | صورة تم إنشاؤها (مشفرة بترميز base64) |

يبدأ المثال التالي مهمة بحث ويعالج البث مع إعادة الاتصال تلقائيًا. يتتبّع هذا الإجراء `interaction_id` و`last_event_id`، وبالتالي، إذا انقطع الاتصال (على سبيل المثال، بعد انتهاء مهلة الـ 600 ثانية)، يمكنه استئناف العملية من حيث توقّفت.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for chunk in stream:
        if chunk.event_type == "interaction.start":
            interaction_id = chunk.interaction.id
        if chunk.event_id:
            last_event_id = chunk.event_id
        if chunk.event_type == "content.delta":
            if chunk.delta.type == "text":
                print(chunk.delta.text, end="", flush=True)
            elif chunk.delta.type == "thought_summary":
                print(f"Thought: {chunk.delta.content.text}", flush=True)
        elif chunk.event_type in ("interaction.complete", "error"):
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
    for await (const chunk of stream) {
        if (chunk.event_type === 'interaction.start') {
            interactionId = chunk.interaction.id;
        }
        if (chunk.event_id) lastEventId = chunk.event_id;
        if (chunk.event_type === 'content.delta') {
            if (chunk.delta.type === 'text') {
                process.stdout.write(chunk.delta.text);
            } else if (chunk.delta.type === 'thought_summary') {
                console.log(`Thought: ${chunk.delta.content.text}`);
            }
        } else if (['interaction.complete', 'error'].includes(chunk.event_type)) {
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

## أسئلة المتابعة والتفاعلات

يمكنك مواصلة المحادثة بعد أن يرسل لك موظف الدعم التقرير النهائي باستخدام `previous_interaction_id`. يتيح لك ذلك طلب توضيح أو تلخيص أو تفصيل أقسام معيّنة من البحث بدون إعادة تشغيل المهمة بأكملها.

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

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
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

## حالات استخدام Gemini Deep Research Agent

‫Deep Research هي **وكيل**، وليست مجرد نموذج. وهي الأنسب لأحمال العمل التي تتطلّب أسلوب "محلّل جاهز للاستخدام" بدلاً من المحادثة ذات وقت الاستجابة المنخفض.

| الميزة | نماذج Gemini العادية | ‫Gemini Deep Research Agent |
| --- | --- | --- |
| **وقت الاستجابة** | الثواني | الدقائق (غير متزامنة/في الخلفية) |
| **المعالجة** | إنشاء -> الناتج | التخطيط -> البحث -> القراءة -> التكرار -> الإخراج |
| **الناتج** | نص حواري ورموز وملخّصات قصيرة | التقارير التفصيلية والتحليلات الطويلة وجداول المقارنة |
| **الأفضل لـ** | برامج الدردشة الآلية واستخراج المعلومات والكتابة الإبداعية | تحليل السوق، وبذل العناية الواجبة، ومراجعات الأبحاث، والتحليل التنافسي |

## إعدادات الوكيل

تستخدم ميزة Deep Research المَعلمة `agent_config` للتحكّم في السلوك.
مرِّرها كقاموس يتضمّن الحقول التالية:

| الحقل | النوع | القيمة التلقائية | الوصف |
| --- | --- | --- | --- |
| `type` | `string` | مطلوب | يجب أن تكون `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | اضبط القيمة على `"auto"` لتلقّي خطوات الاستدلال الوسيطة أثناء البث. اضبط القيمة على `"none"` لإيقافها. |
| `visualization` | `string` | `"auto"` | اضبط القيمة على `"auto"` لتفعيل المخططات والصور التي ينشئها الوكيل. اضبط القيمة على `"off"` لإيقافها. |
| `collaborative_planning` | `boolean` | `false` | اضبط هذا الخيار على `true` لتفعيل مراجعة الخطة المتعددة الجولات قبل بدء البحث. |

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

## التوفّر والأسعار

يمكنك الوصول إلى وكيل البحث العميق من Gemini باستخدام Interactions API في Google AI Studio وGemini API.

تتّبع الأسعار [نموذج الدفع حسب الاستخدام](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#pricing-for-agents) استنادًا إلى نماذج Gemini الأساسية والأدوات المحدّدة التي يستخدمها الوكيل. على عكس طلبات المحادثة العادية التي تؤدي إلى نتيجة واحدة، فإنّ مهمة Deep Research هي سير عمل قائم على الوكالة. يؤدي طلب واحد إلى تشغيل حلقة مستقلة من التخطيط والبحث والقراءة والاستنتاج.

### التكاليف المقدَّرة

تختلف التكاليف حسب مدى تفصيل البحث المطلوب. يحدّد الوكيل بشكل مستقل مقدار القراءة والبحث اللازمَين للإجابة عن طلبك.

- **‫Deep Research** (`deep-research-preview-04-2026`): بالنسبة إلى طلب بحث نموذجي يتطلّب تحليلًا معتدلاً، قد يستخدم الوكيل حوالي 80 طلب بحث و250 ألف رمز مميز للإدخال (يتم تخزين حوالي %50 إلى %70 منها مؤقتًا) و60 ألف رمز مميز للإخراج.
  - **الإجمالي المقدّر:** من 1.00 إلى 3.00 دولار أمريكي لكل مهمة
- **‫Deep Research Max** (`deep-research-max-preview-04-2026`): لإجراء تحليل معمّق للمشهد التنافسي أو العناية الواجبة الشاملة، قد يستخدم الوكيل ما يصل إلى 160 طلب بحث و900 ألف رمز مميز للإدخال (يتم تخزين %50 إلى %70 منها مؤقتًا) و80 ألف رمز مميز للإخراج.
  - **الإجمالي المقدّر:** من 3.00 إلى 7.00 دولار أمريكي لكل مهمة

## اعتبارات السلامة

يتطلّب منح أحد العملاء إذن الوصول إلى الويب وملفاتك الخاصة مراعاة دقيقة لمخاطر الأمان.

- **حقن الطلبات باستخدام الملفات:** يقرأ الوكيل محتوى الملفات التي تقدّمها. تأكَّد من أنّ المستندات التي تم تحميلها (ملفات PDF وملفات نصية) واردة من مصادر موثوقة. قد يحتوي ملف ضار على نص مخفي مصمّم للتلاعب بمخرجات الوكيل.
- **مخاطر المحتوى على الويب:** يبحث الوكيل في شبكة الويب المتاحة للجميع. على الرغم من أنّنا نطبّق فلاتر أمان قوية، هناك خطر من أن يواجه الوكيل صفحات ويب ضارة ويعالجها. ننصحك بمراجعة `citations` الواردة
  في الردّ للتأكّد من المصادر.
- **استخراج البيانات:** توخَّ الحذر عند الطلب من الوكيل تلخيص بيانات داخلية حساسة إذا كنت تسمح له أيضًا بتصفّح الويب.

## أفضل الممارسات

- **طلب معلومات غير معروفة:** يمكنك توجيه الوكيل بشأن كيفية التعامل مع البيانات المفقودة.
  على سبيل المثال، أضِف *"إذا لم تتوفّر أرقام محدّدة لعام 2025،
  اذكر بوضوح أنّها توقّعات أو غير متوفّرة بدلاً من
  تقديرها"* إلى طلبك.
- **توفير السياق:** يمكنك توجيه بحث الوكيل من خلال تقديم معلومات أساسية أو قيود مباشرةً في طلب الإدخال.
- **استخدام التخطيط التعاوني:** بالنسبة إلى طلبات البحث المعقّدة، فعِّل التخطيط التعاوني لمراجعة خطة البحث وتحسينها قبل تنفيذها.
- **إدخالات متعددة الوسائط:** يتيح Deep Research Agent إدخالات متعددة الوسائط.
  استخدِم هذه الميزة بحذر، لأنّها تزيد التكاليف وتزيد من خطر تجاوز قدرة الاستيعاب.

## القيود

- **حالة الإصدار التجريبي**: تتوفّر Interactions API في إصدار تجريبي عام. قد تتغيّر الميزات والمخططات.
- **أدوات مخصّصة:** لا يمكنك حاليًا توفير أدوات مخصّصة لاستخدامها مع "استدعاء الدوال"، ولكن يمكنك استخدام خوادم MCP (بروتوكول سياق النموذج) عن بُعد مع وكيل "البحث العميق".
- **الناتج المنظَّم:** لا يتيح Deep Research Agent حاليًا
  الناتج المنظَّم.
- **الحد الأقصى لمدة البحث:** يبلغ الحد الأقصى لمدة البحث التي يمكن أن يستغرقها وكيل Deep Research‏ 60 دقيقة. من المفترض أن تكتمل معظم المهام في غضون 20 دقيقة.
- **متطلبات المتجر:** يتطلّب تنفيذ الوكيل باستخدام `background=True` توفّر `store=True`.
- **بحث Google:** تكون ميزة [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) مفعّلة تلقائيًا، وتسري [قيود محدّدة](https://ai.google.dev/gemini-api/terms?hl=ar#use-restrictions2) على النتائج المستندة إلى معلومات من العالم الحقيقي.

## الخطوات التالية

- [مزيد من المعلومات حول Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar)
- جرِّب [Deep Research في كتاب وصفات Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Deep_Research.ipynb?hl=ar).
- تعرَّف على كيفية استخدام بياناتك الخاصة باستخدام أداة [البحث في الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
