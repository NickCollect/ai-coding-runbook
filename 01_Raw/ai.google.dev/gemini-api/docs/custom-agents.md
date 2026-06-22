---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar
fetched_at: 2026-06-22T06:26:49.657000+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0648\u0643\u0644\u0627\u0621 \u0645\u064f\u062f\u0627\u0631\u064a\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء وكلاء مُدارين

تتيح لك الوكلاء المُدارون على Gemini API توسيع نطاق "وكيل Antigravity" باستخدام التعليمات والمهارات والبيانات الخاصة بك. يمكنك [تخصيص الوكيل بشكل مضمّن](#customize-inline) في وقت التفاعل، أو [حفظ الإعداد](#save-agent) كوكيل مُدار تستدعيه حسب رقم التعريف.

## تخصيص "وكيل Antigravity"

أسرع طريقة لإنشاء وكيل مخصّص هي تمرير الإعداد بشكل مضمّن أثناء إنشاء تفاعل جديد بدون الحاجة إلى خطوة تسجيل. يمكنك توسيع نطاق الوكيل بثلاث طرق:

- **تعليمات النظام**: يمكنك تمرير نص مضمّن من خلال `system_instruction` لتحديد السلوك.
- **الأدوات**: يمكنك إلغاء الأدوات التلقائية (تنفيذ الرموز البرمجية والبحث وسياق عنوان URL) أو تحديد دوالّ مخصّصة (استدعاء الدوالّ).
- **الملفات والمهارات**: يمكنك تحميل ملفات، مثل `AGENTS.md` و`SKILL.md`، إلى البيئة.

في ما يلي مثال على تمرير كل من هذه العناصر الثلاثة بشكل مضمّن:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a slide deck.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",        
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a slide deck.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",        
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the Q1 revenue data and create a slide deck.",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            }
        ]
    }
}'
```

يتم تحديد كل شيء في وقت التفاعل. ما مِن حاجة إلى تسجيل أي شيء أولاً. يوفر إطار عمل "وكيل Antigravity" وقت التشغيل (تنفيذ الرموز البرمجية وإدارة الملفات والوصول إلى الويب) وطبقات الإعداد الخاصة بك في الأعلى.

### الأدوات وتعليمات النظام

يمكنك تخصيص سلوك الوكيل وإمكاناته لتفاعل معيّن باستخدام المَعلمتَين `system_instruction` و`tools`.

- **تعليمات النظام**: استخدِم المَعلمة `system_instruction` لتمرير نص مضمّن يحدّد سلوك الوكيل. هذا مثالي للتعديلات السريعة التي تريد تغييرها لكل مكالمة. تكون المَعلمة `system_instruction` والملف `AGENTS.md` إضافيَين، ويتم تطبيق كلتَيهما عند توفّرهما.
- **الأدوات**: بشكلٍ تلقائي، يمكن لـ "وكيل Antigravity" الوصول إلى `code_execution` و`google_search` و`url_context`. يمكنك إلغاء هذه القائمة من خلال تمرير المَعلمة `tools` في وقت التفاعل. يمكنك أيضًا تحديد [دوالّ مخصّصة (استدعاء الدوالّ)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#function-calling) لربط الوكيل بواجهات برمجة التطبيقات وقواعد البيانات الخاصة بك. للاطّلاع على التفاصيل الكاملة حول الأدوات المتاحة، يُرجى الرجوع إلى مقالة "[وكيل Antigravity: الأدوات المتوافقة](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#supported-tools)".

### التخصيص المستند إلى الملفات

#### بنية دليل الوكيل

على الرغم من أنّه يمكنك تمرير الإعداد بشكل مضمّن، ننصحك بتنظيم ملفات الوكيل في دليل منظَّم. يسهّل ذلك إدارة الملفات والتحكّم في إصداراتها وتحميلها في بيئة الوكيل.

يبدو دليل مشروع الوكيل النموذجي على النحو التالي:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

يفحص وقت تشغيل Antigravity الملفات التالية في `.agents/` (وفي جذر البيئة).

#### AGENTS.md

يحمّل الوكيل تلقائيًا الملف `.agents/AGENTS.md` (أو `/.agents/AGENTS.md`) من البيئة كتعليمات للنظام عند بدء التشغيل. استخدِم الملف `AGENTS.md` لتعريفات الشخصيات الطويلة والإرشادات التفصيلية والتعليمات التي تريد التحكّم في إصداراتها إلى جانب الرمز البرمجي.

يمكنك تحميل ملف `AGENTS.md` باستخدام مصدر مضمّن:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a report.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a report.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Analyze the Q1 revenue data and create a report.",
      "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/AGENTS.md",
                  "content": "Always use matplotlib for charts. Include a summary table in every report."
              }
          ]
      }
  }'
```

#### المهارات: SKILL.md

المهارات هي ملفات توسّع إمكانات الوكيل. ضَعها ضِمن `.agents/skills/<skill-name>/SKILL.md` وسيكتشفها إطار العمل ويسجّلها تلقائيًا.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

يمكنك تحميل مهارة باستخدام مصدر مضمّن:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Create a presentation about our Q1 results.",
    system_instruction="You create presentations from data.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Create a presentation about our Q1 results.",
    system_instruction: "You create presentations from data.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Create a presentation about our Q1 results.",
      "system_instruction": "You create presentations from data.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/skills/slide-maker/SKILL.md",
                  "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"
              }
          ]
      }
  }'
```

يتم اكتشاف المهارات التي يتم تحميلها من `.agents/skills/` و`/.agents/skills/` تلقائيًا.

## إنشاء وكيل مُدار

بعد تكرار الإعداد، يمكنك إنشاؤه كوكيل مُدار باستخدام `agents.create`. يتيح لك ذلك استدعاء الوكيل حسب رقم التعريف بدون تكرار الإعداد في كل مرة.

### من المصادر

حدِّد `base_agent` و`id` و`system_instruction` و`base_environment` باستخدام المصادر. توفّر المنصة بيئة اختبار جديدة تتضمّن ملفاتك في كل عملية استدعاء. يمكنك الاطّلاع على أنواع المصادر المتاحة (Git وGCS والمضمّنة) في مقالة [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates",
            },
        ],
    },
)

print(f"Created agent: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                type: "repository",
                source: "https://github.com/my-org/analysis-templates",
                target: "/workspace/templates",
            },
        ],
    },
});

console.log(`Created agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates"
            }
        ]
    }
}'
```

### من بيئة حالية (تفريع)

كرِّر استخدام "وكيل Antigravity" الأساسي إلى أن تصبح البيئة مناسبة (الحِزم مثبَّتة والملفات في مكانها)، ثم فرِّعها إلى وكيل مُدار.

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment=interaction.environment_id,
)

print(f"Forked agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### باستخدام قواعد الشبكة

يمكنك حظر الوصول الصادر أو إدخال بيانات الاعتماد عند حفظ وكيل مُدار. للاطّلاع على المخطط الكامل لقائمة السماح وأنماط بيانات الاعتماد والأحرف البدل، يُرجى الرجوع إلى مقالة [البيئات: إعدادات الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration).

ينشئ المثال التالي وكيل `issue-resolver` لا يمكنه الوصول إلا إلى GitHub وPyPI، مع إدخال بيانات الاعتماد لـ GitHub:

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/my-org/backend",
                "target": "/workspace/repo",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(f"Created issue-resolver agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "issue-resolver",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/my-org/backend",
                target: "/workspace/repo",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        }
    },
});

console.log(`Created issue-resolver agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-05-2026",
      "system_instruction": "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
      "base_environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "repository",
                  "source": "https://github.com/my-org/backend",
                  "target": "/workspace/repo"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Basic YOUR_BASE64_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## استدعاء الوكيل

يمكنك استدعاء الوكيل المُدار باستخدام رقم تعريف الوكيل من خلال إنشاء تفاعل جديد. في كل عملية استدعاء، يتم تفريع البيئة الأساسية، لذا تبدأ كل عملية تشغيل من جديد.

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

للاطّلاع على المحادثات المترابطة والبث، يُرجى الرجوع إلى دليل البدء السريع . تنطبق أنماط `previous_interaction_id` و`environment` نفسها على الوكلاء المُدارين.

## إلغاء الإعداد في وقت الاستدعاء

يمكنك إلغاء `system_instruction` و`tools` التلقائيتَين للوكيل عند إنشاء تفاعل. يتيح لك ذلك تعديل سلوك الوكيل أو إمكاناته لعملية تشغيل معيّنة بدون تغيير تعريف الوكيل المخزَّن.

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction="You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools=[{"type": "code_execution"}], # Override to only use code execution
    environment="remote",
)
print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction: "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools: [{ type: "code_execution" }], // Override to only use code execution
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

## إدارة الوكلاء

يمكنك إدراج الوكلاء والحصول عليهم وحذفهم.

### إدراج الوكلاء

### Python

```
agents = client.agents.list()
for a in agents.agents:
    print(f"{a.id}: {a.description}")
```

### JavaScript

```
const agents = await client.agents.list();
if (agents.agents) {
    for (const a of agents.agents) {
        console.log(`${a.id}: ${a.description}`);
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### الحصول على وكيل

### Python

```
agent = client.agents.get(id="data-analyst")
print(agent)
```

### JavaScript

```
const agent = await client.agents.get("data-analyst");
console.log(agent);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### حذف وكيل

يؤدي الحذف إلى إزالة الإعداد. لا تتأثر البيئات الحالية والتفاعلات التي أنشأها الوكيل.

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## مرجع تعريف الوكيل

| الحقل | النوع | مطلوب | الوصف |
| --- | --- | --- | --- |
| `id` | سلسلة | نعم | رقم تعريف فريد للوكيل. يُستخدَم لاستدعاء الوكيل. |
| `description` | سلسلة | لا | وصف للوكيل يمكن لشخص عادي قراءته. |
| `base_agent` | سلسلة | نعم | رقم تعريف الوكيل الأساسي (مثلاً، `antigravity-preview-05-2026`). |
| `system_instruction` | سلسلة | لا | طلب النظام الذي يحدّد السلوك والشخصية. |
| `tools` | سلسلة أو عنصر | لا | الأدوات التي يمكن للوكيل استخدامها، وإذا تم حذفها، سيتمكّن الوكيل من الوصول إلى `code_execution` و`google_search` و`url_context`. |
| `base_environment` | سلسلة أو عنصر | لا | `"remote"` أو `environment_id` أو عنصر إعداد يتضمّن `sources` و`network`. يُرجى الرجوع إلى مقالة البيئات. |

## سير عمل التكرار

1. **إنشاء نموذج أولي** باستخدام "وكيل Antigravity" الأساسي. يمكنك تمرير تعليمات النظام ومصادر البيئة بشكل مضمّن. اختبِر التعليمات والمهارات وإعداد البيئة بشكل تفاعلي.
2. **تثبيت** البيئة. يمكنك تثبيت الحِزم وتحميل المصادر والتحقّق من أنّ كل شيء يعمل.
3. **الاحتفاظ** بالوكيل كوكيل مُدار من خلال إنشاء وكيل جديد، إما من المصادر أو من خلال تفريع البيئة.
4. **تعديل** تعريف الوكيل. يمكنك تغيير تعليمات النظام أو تبديل المهارات أو إضافة المصادر. ستستخدم عملية الاستدعاء التالية الإعداد الجديد.

## القيود

- **حالة المعاينة**: الوكلاء المُدارون في مرحلة المعاينة. قد تتغيّر الميزات والمخططات.
- **الوكيل الأساسي**: لا يمكن استخدام سوى `antigravity-preview-05-2026` كـ `base_agent`.
- **ما مِن ميزة للتحكّم في الإصدارات**: لا تتوفّر بعد ميزتا التحكّم في إصدارات الوكيل والرجوع إلى إصدار سابق.
- **ما مِن ميزة لتضمين وكلاء فرعيين**: لا تتوفّر بعد ميزة تفويض الوكلاء الفرعيين.
- يمكنك استخدام ما يصل إلى 1,000 وكيل مُدار.

## الخطوات التالية

- [نظرة عامة على الوكلاء](https://ai.google.dev/gemini-api/docs/agents?hl=ar): يمكنك التعرّف على المفاهيم الأساسية للوكلاء المُدارين.
- [دليل البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): يمكنك البدء في الإنشاء باستخدام المحادثات المترابطة والعرض تدريجيًا.
- [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar): يمكنك استكشاف إمكانات الوكيل التلقائي وأدواته وأسعاره.
- [بيئات الوكلاء](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar): يمكنك إعداد بيئات الاختبار والمصادر والشبكات.
- [Managed Agents API على "منصة الوكلاء"](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=ar): يمكنك إنشاء وكلاء باستخدام حوكمة تنظيمية مضمّنة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-17 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-17 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
