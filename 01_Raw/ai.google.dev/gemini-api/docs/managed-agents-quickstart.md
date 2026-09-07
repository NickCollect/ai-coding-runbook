---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar
fetched_at: 2026-09-07T05:42:34.595421+00:00
title: "\u0627\u0644\u0628\u062f\u0621 \u0627\u0644\u0633\u0631\u064a\u0639 \u0641\u064a \u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0627\u0644\u0648\u0643\u0644\u0627\u0621 \u0627\u0644\u0645\u064f\u062f\u0627\u0631\u064a\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البدء السريع في استخدام الوكلاء المُدارين

يرشدك هذا الدليل إلى كيفية إنشاء واستخدام "الوكلاء المُدارون" على Gemini API باستخدام [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=ar). ستجري مكالمتك الأولى مع الوكيل، وتواصل محادثة مترابطة، وتبث الرد، وتنزّل الملفات من وضع الحماية، وتعمل مع وكيل Antigravity المُدار.

## إجراء تفاعلك الأول مع الوكيل

يؤدي طلب واحد إلى [واجهة برمجة التطبيقات Interactions API](https://ai.google.dev/gemini-api/docs?hl=ar) إلى توفير بيئة اختبارية لنظام التشغيل Linux، وتشغيل حلقة الوكيل، وعرض النتيجة. عليك تحديد ثلاث مَعلمات:

- مرِّر `agent` كـ `"antigravity-preview-05-2026",`، وهو الإصدار الحالي من الوكيل المُدار المحدّد مسبقًا والعام.
- حدِّد `environment="remote"` لتوفير بيئة وضع الحماية جديدة.
- أنشئ إدخالاً يحدّد ما تريد أن يفعله الوكيل.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

تعرض الاستجابة عنصر `Interaction`. يمكنك تخزين `interaction.id` و`interaction.environment_id` لمواصلة المحادثة في بيئة الاختبار المعزولة نفسها. استخدِم `interaction.output_text` للوصول إلى الردّ النهائي من الموظف. تعرض `interaction.steps` كل خطوة اتّخذها الوكيل (الاستدلال، واستدعاء الأدوات، وتطبيق الرموز البرمجية).

## مواصلة المحادثة (محادثة مترابطة)

تتتبّع واجهة برمجة التطبيقات سمتَين مستقلتَين للحالة:

- **سياق المحادثة:** سجلّ المحادثات، وتتبُّع الاستدلال، واستخدام الأدوات، واستخدام `previous_interaction_id`
- [**حالة البيئة:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar) الملفات والحِزم المثبَّتة وحالة وضع الحماية، باستخدام `environment`

يجب تمرير كليهما في مكانهما المناسب لاستئناف العملية:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

تظل الملفات من الجولة الأولى (`fibonacci.txt`) متوفرة في الجولة الثانية. يحتفظ الوكيل أيضًا بسياق المحادثة.

يمكنك الجمع بين هذه الخيارات بشكل مستقل:

- **محو المحادثة والاحتفاظ بالملفات:** احذف `previous_interaction_id`، ومرِّر رقم تعريف البيئة فقط باستخدام `environment` لإجراء محادثة جديدة في مساحة العمل نفسها.
- **الاحتفاظ بالمحادثة، مساحة عمل جديدة:** أدخِل `previous_interaction_id`، واضبط `environment="remote"` لإنشاء بيئة اختبارية جديدة.

### ضغط السياق التلقائي

في المحادثات الطويلة المتعددة الأدوار، يمكن أن يزداد حجم السجلّ الأولي لخطوات الاستدلال واستدعاء الأدوات ومحتوى الملفات الكبيرة بسرعة ويستهلك مساحة كبيرة من السياق. لمنع حدوث أخطاء بسبب تجاوز الحد الأقصى للرموز المميزة والحفاظ على تركيز الوكيل (منع "تدهور السياق")، تتضمّن واجهة برمجة التطبيقات "الوكلاء المُدارون" خطوة مدمجة لضغط السياق عند حوالي 135 ألف رمز مميز. وتتم هذه العملية تلقائيًا.

## عرض الرد تدريجيًا

بالنسبة إلى المهام التي تستغرق وقتًا طويلاً، يمكنك بث الردّ لمشاهدة الوكيل وهو يعمل في الوقت الفعلي:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
    if event.event_type == "step.stop" and event.usage:
        print(event.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
    if (event.event_type === "step.stop" && event.usage) {
        console.log(event.usage);
    }
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

تعرض ميزة البث فروق الخطوات مع التعديلات المتزايدة. عند اكتمال إحدى الخطوات، يتضمّن الحدث `step.stop` إحصاءات الاستخدام المتراكمة. يمكنك الاطّلاع على مزيد من المعلومات في [دليل البث](https://ai.google.dev/gemini-api/docs/streaming?hl=ar).

## تنزيل ملفات من البيئة

عندما ينشئ الوكيل ملفات داخل البيئة التجريبية يمكنك تنزيلها باستخدام Files API من خلال طلب HTTP مباشر (لا تتوفّر طريقة SDK حتى الآن):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## حفظ وكيل مُدار

في الخطوات السابقة، استخدمنا وكيل Antigravity التلقائي وعدّلناه بشكل مضمّن. بعد تكرار عملية الإعداد (التعليمات والمهارات واختيار النموذج والبيئة)، يمكنك حفظها كوكيل مُدار قابل لإعادة الاستخدام. يتيح لك ذلك استدعاءه حسب رقم التعريف بدون تكرار الإعداد.

عند حفظ وكيل، لاحظ التماثل المعماري مع التفاعلات المضمّنة: يمكنك تحديد `base_agent: "antigravity-preview-05-2026"` ويمكنك تمرير `agent_config` مع `model` الذي اخترته تمامًا كما تفعل على `interactions.create`. يمكنك أيضًا تحديد `base_environment` (إما من المصادر أو عن طريق إنشاء نسخة من بيئة حالية). سيستخدم الوكيل إعدادات البيئة والنموذج هذه لكل تفاعل جديد.

**من المصادر:** يمكنك تحديد المصادر مباشرةً أو من مصادر أخرى، مثل GitHub أو Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.7-flash",
    },
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.7-flash",
    },
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.7-flash"
    },
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## استدعاء الوكيل المُدار

بعد حفظ وكيل مُدار، يمكنك استدعاؤه باستخدام المعرّف. يؤدي كل استدعاء إلى إنشاء نسخة من البيئة الأساسية، لذا يبدأ كل تشغيل بشكل نظيف:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## الخطوات التالية

- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar): الإمكانات والأدوات المتوافقة والإدخال المتعدد الوسائط والأسعار والقيود
- [إنشاء وكلاء مُدارين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar): يمكنك توسيع نطاق Antigravity باستخدام التعليمات والمهارات والبيانات الخاصة بك.
- [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar): المصادر والشبكات ودورة الحياة وحدود الموارد
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar): هي واجهة برمجة التطبيقات الأساسية للنماذج والوكلاء.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-08-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-08-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
