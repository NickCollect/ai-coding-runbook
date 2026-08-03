---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar
fetched_at: 2026-08-03T04:42:07.552463+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0648\u0643\u0644\u0627\u0621 \u0645\u064f\u062f\u0627\u0631\u064a\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء وكلاء مُدارين

تتيح لك الوكلاء المُدارون على Gemini API توسيع نطاق وكيل Antigravity باستخدام تعليماتك ومهاراتك وبياناتك. يمكنك [تخصيص الوكيل بشكل مضمّن](#customize-inline) في وقت التفاعل، أو [حفظ الإعداد](#save-agent) كوكيل مُدار يمكنك استدعاؤه باستخدام المعرّف.

## تخصيص وكيل Antigravity

أسرع طريقة لإنشاء وكيل مخصّص هي تمرير إعداداتك مضمّنةً أثناء إنشاء تفاعل جديد بدون الحاجة إلى إجراء خطوة التسجيل. يمكنك توسيع نطاق عمل الوكيل بعدة طرق رئيسية:

- **[اختيار النموذج](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#model-selection)**: اختَر نموذج Gemini الأساسي من خلال `agent_config` (يكون النموذج التلقائي هو **Gemini 3.6 Flash**).
- **تعليمات النظام**: يمكنك تمرير نص مضمّن من خلال `system_instruction` لتحديد السلوك.
- **الأدوات**: يمكنك إلغاء الأدوات التلقائية (تنفيذ الرمز البرمجي، والبحث، وسياق عنوان URL)، أو تسجيل خوادم MCP عن بُعد، أو تحديد وظائف مخصّصة (استدعاء الوظائف).
- **الملفات والمهارات**: يمكنك تحميل ملفات مثل `AGENTS.md` و`SKILL.md` في البيئة.

في ما يلي مثال على تمرير المَعلمات الثلاث كلها في السطر:

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

يتم تحديد كل شيء في وقت التفاعل. ليس عليك تسجيل أي شيء أولاً. توفر أداة Antigravity Agent بيئة التشغيل (تنفيذ الرموز البرمجية وإدارة الملفات والوصول إلى الويب) وطبقات الإعدادات في الأعلى.

### الأدوات وتعليمات النظام

يمكنك تخصيص سلوك الوكيل وإمكاناته لتفاعل معيّن باستخدام المَعلمتَين `system_instruction` و`tools`.

- **تعليمات النظام**: استخدِم المَعلمة `system_instruction` لتمرير نص مضمّن يحدّد سلوك الوكيل. هذه الميزة مثالية لإجراء تعديلات سريعة تريد تغييرها لكل مكالمة. تكون `system_instruction` و`AGENTS.md` ترافقيتَين، أي أنّهما تسريان معًا عند توفّرهما.
- **الأدوات**: بشكلٍ تلقائي، يمكن لوكيل Antigravity الوصول إلى `code_execution` و`google_search` و`url_context`. يمكنك تجاوز هذه القائمة من خلال تمرير المَعلمة `tools` في وقت التفاعل. يمكنك أيضًا تسجيل [خوادم MCP عن بُعد](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#mcp-servers) أو تحديد [دوال مخصّصة (استدعاء الدوال)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#function-calling) لربط الوكيل بواجهات برمجة التطبيقات وقواعد البيانات الخاصة بك. للاطّلاع على التفاصيل الكاملة حول الأدوات المتاحة، يُرجى الانتقال إلى [Antigravity Agent: الأدوات المتوافقة](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#supported-tools).

### التخصيص المستند إلى الملفات

#### بنية دليل الوكيل

على الرغم من أنّه يمكنك تمرير الإعدادات مضمّنة، ننصحك بتنظيم ملفات البرنامج في دليل منظَّم. يسهّل ذلك إدارة الملفات والتحكّم في إصداراتها وتثبيتها في بيئة الوكيل.

يبدو دليل مشروع الوكيل النموذجي على النحو التالي:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

يفحص وقت تشغيل Antigravity `.agents/` (وجذر البيئة) بحثًا عن هذه الملفات.

#### AGENTS.md

يحمّل الوكيل تلقائيًا `.agents/AGENTS.md` (أو `/.agents/AGENTS.md`) من البيئة كتعليمات نظام عند بدء التشغيل. استخدِم `AGENTS.md` لتعريفات الشخصيات الطويلة والإرشادات المفصّلة والتعليمات التي تريد التحكّم في إصدارها إلى جانب الرمز البرمجي.

تثبيت `AGENTS.md` باستخدام مصدر مضمّن:

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

المهارات هي ملفات توسّع إمكانات الوكيل. ضَعها تحت `.agents/skills/<skill-name>/SKILL.md`، وسيتعرّف عليها نظام التوصيل تلقائيًا ويسجّلها.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

تثبيت مهارة باستخدام مصدر مضمّن:

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

يتم تلقائيًا اكتشاف المهارات المحمَّلة من `.agents/skills/` و`/.agents/skills/`.

## إنشاء وكيل مُدار

بعد تكرار عملية الإعداد، يمكنك إنشاء الإعداد كبرنامج وكيل مُدار باستخدام `agents.create`. يتيح لك ذلك استدعاء "الوكيل" حسب المعرّف بدون تكرار عملية الإعداد في كل مرة.

يجب أن يكون `id` الذي تحدّده عند إنشاء وكيل مُدار فريدًا لمشروعك ويجب ألا يبدأ بالبادئات المحجوزة (مثل `google-` و`gemini-`). اطّلِع على [قيود رقم تعريف الوكيل](#agent-id-restrictions) للحصول على القائمة الكاملة بالبادئات المحظورة.

### من المصادر

حدِّد `base_agent` و`id` و`agent_config` و`system_instruction` و`base_environment` مع المصادر. توفّر المنصة بيئة اختبار جديدة تتضمّن ملفاتك في كل عملية استدعاء. راجِع [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar) لمعرفة أنواع المصادر المتاحة (Git وGCS والمضمّنة).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.6-flash",
    },
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
    agent_config: {
        type: "antigravity",
        model: "gemini-3.6-flash",
    },
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
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.6-flash"
    },
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

### من بيئة حالية (تشعّب)

كرِّر استخدام وكيل Antigravity الأساسي إلى أن تصبح البيئة مناسبة (تثبيت الحِزم، ووضع الملفات في مكانها)، ثم أنشئ نسخة من الوكيل في وكيل مُدار.

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
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### مع قواعد الشبكة

يمكنك حظر الوصول الخارجي أو إدخال بيانات الاعتماد عند حفظ وكيل مُدار. للاطّلاع على مخطط قائمة السماح الكامل وأنماط بيانات الاعتماد وأحرف البدل، يُرجى الانتقال إلى [البيئات: إعدادات الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration).

ينشئ المثال التالي وكيلاً `issue-resolver` يمكنه الوصول إلى GitHub وPyPI فقط، مع إدخال بيانات الاعتماد الخاصة بـ GitHub:

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

اتّصِل بالوكيل المُدار باستخدام رقم تعريف الوكيل من خلال إنشاء تفاعل جديد. يؤدي كل استدعاء إلى إنشاء نسخة من البيئة الأساسية، لذا تبدأ كل عملية تشغيل بشكل نظيف.

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
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

للمحادثات المترابطة والبث، يُرجى الاطّلاع على [البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar). تنطبق أنماط `previous_interaction_id` و`environment` نفسها على البرامج التي يديرها المشرف.

تتيح الوكلاء المُدارين أيضًا تنفيذ العمليات في الخلفية وإلغاءها. للحصول على التفاصيل وأمثلة الرموز، يُرجى الاطّلاع على [Antigravity Agent: Background execution](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#background-execution).

## تجاوز الإعدادات عند الاستدعاء

يمكنك إلغاء إعدادات الشبكة التلقائية `system_instruction` و`tools` و`environment` الخاصة بالوكيل عند إنشاء تفاعل. يتيح لك ذلك تعديل سلوك الوكيل أو إمكاناته أو بيانات اعتماده لتنفيذ عملية معيّنة بدون تغيير تعريف الوكيل المخزّن.

### تجاوز تعليمات النظام وأدواته

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
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

### تجاوز إعدادات الشبكة (تحديث بيانات الاعتماد)

إذا كان وكيلك المُدار يتضمّن بيانات اعتماد الشبكة في `base_environment`، يمكنك تجاهلها عند الاستدعاء لتجديد الرموز المميزة المنتهية الصلاحية أو تدوير مفاتيح واجهة برمجة التطبيقات. مرِّر عنصر `environment` مع إعداد `network` جديد. تحلّ قواعد الشبكة الجديدة محلّ القواعد السابقة بشكل كامل في ما يتعلّق بهذا التفاعل. يتم الاحتفاظ بمصادر البيئة الأساسية (الملفات والمستودعات).

### Python

```
# Invoke the agent with a fresh token, overriding the base_environment credentials
result = client.interactions.create(
    agent="issue-resolver",
    input="Fix issue #42 and open a PR.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
// Invoke the agent with a fresh token, overriding the base_environment credentials
const result = await client.interactions.create({
    agent: "issue-resolver",
    input: "Fix issue #42 and open a PR.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        },
    },
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "issue-resolver",
      "input": "Fix issue #42 and open a PR.",
      "environment": {
          "type": "remote",
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## إدارة الوكلاء

يمكنك إدراج الوكلاء والحصول عليهم وحذفهم.

### وكلاء القائمة

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

يؤدي الحذف إلى إزالة الإعدادات. لا تتأثر البيئات والتفاعلات الحالية التي أنشأها الوكيل.

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
| `id` | سلسلة | نعم | المعرّف الفريد للوكيل ضمن مشروع Google Cloud يُستخدَم لتفعيل الوكيل. يجب عدم استخدام البادئات المحجوزة. اطّلِع على [قيود معرّف الوكيل](#agent-id-restrictions). |
| `description` | سلسلة | لا | وصف الوكيل يمكن لشخص عادي قراءته |
| `base_agent` | سلسلة | نعم | معرّف الوكيل الأساسي (مثلاً، `antigravity-preview-05-2026`) |
| `agent_config` | عنصر | لا | إعدادات الوكيل الأساسي، بما في ذلك اختيار النموذج (`{"type": "antigravity", "model": "gemini-3.6-flash"}`). يتم ضبط القيمة التلقائية على `gemini-3.6-flash` في حال عدم تحديدها. لا يمكن إلغاؤها في وقت التفاعل مع الوكلاء المحدّدين. |
| `system_instruction` | سلسلة | لا | طلب النظام الذي يحدّد السلوك والشخصية |
| `tools` | صفيف | لا | الأدوات التي يمكن للوكيل استخدامها في حال عدم تحديدها، يتم ضبطها تلقائيًا على `code_execution` و`google_search` و`url_context`. تشمل الأدوات المتوافقة `code_execution` و`google_search` و`url_context` و`mcp_server` وتعريفات `function` المخصّصة. |
| `base_environment` | سلسلة أو عنصر | لا | `"remote"` أو `environment_id` أو عنصر إعدادات يتضمّن `sources` و`network` الاطّلاع على البيئات |

### القيود المفروضة على رقم تعريف الوكيل

عند إنشاء وكيل مُدار، يجب أن يلتزم `id` الذي تحدّده بالقواعد التالية:

- ويجب أن يكون فريدًا لمشروعك على Google Cloud.
- يجب **ألا** يبدأ بأي من البادئات المحجوزة التالية (غير حساسة لحالة الأحرف)، وإلا ستتعذّر عملية الإنشاء:
  - `antigravity-`
  - `veo-`
  - `omni-`
  - `lyria-`
  - `imagen-`
  - `gemma-`
  - `gemini-`
  - `google-`
  - `youtube-`
  - `android-`
  - `chrome-`
  - `pixel-`
  - `waze-`
  - `fitbit-`
  - `nest-`
  - `kaggle-`

## سير عمل التكرار

1. **إنشاء نموذج أولي** باستخدام وكيل Antigravity الأساسي تمرير تعليمات النظام ومصادر البيئة مضمّنة اختبار التعليمات والمهارات وإعداد البيئة بشكل تفاعلي
2. **تثبيت** البيئة ثبِّت الحِزم، واربط المصادر، وتأكَّد من أنّ كل شيء يعمل.
3. **الاستمرار** كوكيل مُدار من خلال إنشاء وكيل جديد، إما من المصادر أو من خلال إنشاء نسخة من البيئة.
4. **عدِّل** تعريف الوكيل. تغيير تعليمات النظام أو تبديل المهارات أو إضافة مصادر سيتم استخدام الإعدادات الجديدة في عملية الاستدعاء التالية.

## القيود

- **حالة المعاينة**: الوكلاء المُدارون في مرحلة المعاينة. قد تتغيّر الميزات والمخططات.
- **الوكيل الأساسي والنماذج**: يُسمح بالقيمة `antigravity-preview-05-2026` فقط كقيمة `base_agent`. خيارات النماذج المتوافقة في `agent_config` هي `gemini-3.5-flash` و`gemini-3.6-flash` (الإعداد التلقائي) و`gemini-3.5-flash-lite`. بالنسبة إلى الوكلاء المحدّدين، لا يمكن تجاهل النموذج في وقت التفاعل.
- **عدم توفّر ميزة التحكم بالإصدارات**: لا تتوفّر ميزة التحكم بإصدارات الوكيل والعودة إلى الإصدار السابق بعد.
- **عدم إمكانية إنشاء وكلاء فرعيين متداخلين**: لا تتوفّر بعد إمكانية تفويض وكيل فرعي.
- يمكنك الحصول على ما يصل إلى 1,000 وكيل مُدار.

## الخطوات التالية

- [نظرة عامة على الوكلاء](https://ai.google.dev/gemini-api/docs/agents?hl=ar): تعرَّف على المفاهيم الأساسية للوكلاء المُدارين.
- [البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): ابدأ إنشاء محادثات مترابطة وبث المحتوى.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar): استكشاف الإمكانات والأدوات والأسعار للوكيل التلقائي
- [بيئات الوكيل](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar): يمكنك ضبط بيئات الاختبار المعزولة والمصادر والشبكات.
- [Managed Agents API على "منصة الوكلاء"](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=ar): لإنشاء الوكلاء المُدارين مع إدارة مؤسسية مدمجة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
