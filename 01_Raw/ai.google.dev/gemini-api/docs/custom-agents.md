---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar
fetched_at: 2026-08-24T02:35:59.118393+00:00
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

تتيح لك الوكلاء المُدارون على Gemini API توسيع نطاق "وكيل Antigravity" باستخدام التعليمات والمهارات والبيانات الخاصة بك. يمكنك [تخصيص الوكيل بشكل مضمّن](#customize-inline) في وقت التفاعل، أو [حفظ الإعداد](#save-agent) كوكيل مُدار تستدعيه حسب رقم التعريف.

## تخصيص "وكيل Antigravity"

أسرع طريقة لإنشاء وكيل مخصّص هي تمرير الإعداد بشكل مضمّن أثناء إنشاء تفاعل جديد بدون الحاجة إلى خطوة التسجيل. يمكنك توسيع نطاق الوكيل بعدة طرق رئيسية:

- **[اختيار النموذج](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#model-selection)**: اختَر نموذج Gemini الأساسي من خلال `agent_config` (الإعداد التلقائي هو **Gemini 3.7 Flash**).
- **تعليمات النظام**: مرِّر نصًا مضمّنًا من خلال `system_instruction` لتحديد السلوك.
- **الأدوات**: يمكنك إلغاء الأدوات التلقائية (تنفيذ الرموز البرمجية والبحث وسياق عنوان URL) أو تسجيل خوادم MCP عن بُعد أو تحديد وظائف مخصّصة (استدعاء الدوال).
- **الملفات والمهارات**: يمكنك تثبيت ملفات، مثل `AGENTS.md` و`SKILL.md`، في البيئة.

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

### راحة

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

يتم تحديد كل شيء في وقت التفاعل. ولست بحاجة إلى تسجيل أي شيء أولاً. يوفر إطار عمل "وكيل Antigravity" وقت التشغيل (تنفيذ الرموز البرمجية وإدارة الملفات والوصول إلى الويب) وطبقات الإعداد الخاصة بك في الأعلى.

### الأدوات وتعليمات النظام

يمكنك تخصيص سلوك الوكيل وإمكاناته لتفاعل معيّن باستخدام المَعلمتَين `system_instruction` و`tools`.

- **تعليمات النظام**: استخدِم المَعلمة `system_instruction` لتمرير نص مضمّن يحدّد سلوك الوكيل. هذا مثالي لإجراء تعديلات سريعة تريد تغييرها لكل مكالمة. إنّ `system_instruction` و`AGENTS.md` إضافيتان، ويتم تطبيق كلتيهما إذا كانتا متوفرتَين.
- **الأدوات**: بشكلٍ تلقائي، يمكن لـ "وكيل Antigravity" الوصول إلى `code_execution` و`google_search` و`url_context`. يمكنك إلغاء هذه القائمة من خلال تمرير المَعلمة `tools` في وقت التفاعل. يمكنك أيضًا تسجيل [خوادم MCP عن بُعد](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#mcp-servers) أو تحديد [وظائف مخصّصة (استدعاء الدوال)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#function-calling) لربط الوكيل بواجهات برمجة التطبيقات وقواعد البيانات الخاصة بك. للاطّلاع على التفاصيل الكاملة حول الأدوات المتاحة، يُرجى الرجوع إلى مقالة "[وكيل Antigravity: الأدوات المتوافقة](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#supported-tools)".

### التخصيص على مستوى الملفات

#### بنية دليل الوكيل

على الرغم من أنّه يمكنك تمرير الإعداد بشكل مضمّن، ننصحك بتنظيم ملفات الوكيل في دليل منظَّم. يسهّل ذلك إدارة الملفات والتحكّم في إصداراتها وتثبيتها في بيئة الوكيل.

يبدو دليل مشروع الوكيل النموذجي على النحو التالي:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

يفحص وقت تشغيل Antigravity الملفات في `.agents/` (وفي جذر البيئة).

#### AGENTS.md

يحمِّل الوكيل تلقائيًا `.agents/AGENTS.md` (أو `/.agents/AGENTS.md`) من البيئة كتعليمات للنظام عند بدء التشغيل. استخدِم `AGENTS.md` لتعريفات الشخصيات الطويلة والإرشادات التفصيلية والتعليمات التي تريد التحكّم في إصداراتها جنبًا إلى جنب مع الرمز البرمجي.

يمكنك تثبيت `AGENTS.md` باستخدام مصدر مضمّن:

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

### راحة

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

المهارات هي ملفات توسّع إمكانات الوكيل. ضَعها ضِمن `.agents/skills/<skill-name>/SKILL.md` وسيكتشفها إطار العمل ويسجّلها تلقائيًا.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

يمكنك تثبيت مهارة باستخدام مصدر مضمّن:

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

### راحة

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

يتم تلقائيًا اكتشاف المهارات التي يتم تحميلها من `.agents/skills/` و`/.agents/skills/`.

## إنشاء وكيل مُدار

بعد تكرار الإعداد، يمكنك إنشاؤه كوكيل مُدار باستخدام `agents.create`. يتيح لك ذلك استدعاء الوكيل حسب رقم التعريف بدون تكرار الإعداد في كل مرة.

يجب أن يكون `id` الذي تحدّده عند إنشاء وكيل مُدار فريدًا لمشروعك ويجب ألا يبدأ بأي من البادئات المحجوزة (مثل `google-` و`gemini-`). للاطّلاع على القائمة الكاملة بالبادئات المحظورة، يُرجى الرجوع إلى مقالة [القيود المفروضة على رقم تعريف الوكيل](#agent-id-restrictions).

### من المصادر

حدِّد `base_agent` و`id` و`agent_config` و`system_instruction` و`base_environment` باستخدام المصادر. توفّر المنصة بيئة تجريبية جديدة تتضمّن ملفاتك في كل عملية استدعاء. للاطّلاع على أنواع المصادر المتاحة (Git وGCS والمضمّنة)، يُرجى الرجوع إلى مقالة [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.7-flash",
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
        model: "gemini-3.7-flash",
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

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.7-flash"
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

كرِّر استخدام "وكيل Antigravity" الأساسي إلى أن تصبح البيئة مناسبة (تم تثبيت الحِزم ووضع الملفات في مكانها)، ثم فرِّغها في وكيل مُدار.

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

### راحة

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

### باستخدام قواعد الشبكة

يمكنك حظر الوصول الصادر أو إدخال بيانات الاعتماد عند حفظ وكيل مُدار. للاطّلاع على المخطط الكامل لقائمة السماح وأنماط بيانات الاعتماد والأحرف البدل، يُرجى الرجوع إلى مقالة [البيئات: إعداد الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration).

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

### راحة

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

يمكنك استدعاء الوكيل المُدار باستخدام رقم تعريف الوكيل من خلال إنشاء تفاعل جديد. في كل عملية استدعاء، يتم تفريغ البيئة الأساسية، لذا تبدأ كل عملية تشغيل من جديد.

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

### راحة

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

للاطّلاع على المحادثات المترابطة والبث، يُرجى الرجوع إلى دليل البدء السريع . تنطبق أنماط `previous_interaction_id` و`environment` نفسها على الوكلاء المُدارين.

تتيح الوكلاء المُدارون أيضًا التنفيذ في الخلفية والإلغاء. للاطّلاع على التفاصيل وأمثلة الرموز البرمجية، يُرجى الرجوع إلى مقالة "[وكيل Antigravity": التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#background-execution).

## إلغاء الإعداد في وقت الاستدعاء

يمكنك إلغاء الإعداد التلقائي للوكيل في ما يخص `system_instruction` و`tools` وإعداد الشبكة `environment` عند إنشاء تفاعل. يتيح لك ذلك تعديل سلوك الوكيل أو إمكاناته أو بيانات اعتماده لتشغيل معيّن بدون تغيير تعريف الوكيل المخزّن.

### إلغاء تعليمات النظام والأدوات

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

### راحة

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

### إلغاء إعداد الشبكة (تحديث بيانات الاعتماد)

إذا كان الوكيل المُدار يتضمّن بيانات اعتماد الشبكة في `base_environment`، يمكنك إلغاؤها في وقت الاستدعاء لتحديث الرموز المميزة المنتهية الصلاحية أو تدوير مفاتيح واجهة برمجة التطبيقات. مرِّر عنصر `environment` يتضمّن إعداد `network` جديدًا. تحل قواعد الشبكة الجديدة محل القواعد السابقة بالكامل لهذا التفاعل. يتم الاحتفاظ بمصادر البيئة الأساسية (الملفات والمستودعات).

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

### راحة

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

### راحة

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

### راحة

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

### راحة

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## مرجع تعريف الوكيل

| الحقل | النوع | مطلوب | الوصف |
| --- | --- | --- | --- |
| `id` | سلسلة | نعم | رقم تعريف فريد للوكيل ضِمن مشروع Google Cloud. يُستخدم لاستدعاء الوكيل. يجب ألا يستخدم البادئات المحجوزة. يُرجى الرجوع إلى مقالة [القيود المفروضة على رقم تعريف الوكيل](#agent-id-restrictions). |
| `description` | سلسلة | لا | وصف للوكيل يمكن لشخص عادي قراءته. |
| `base_agent` | سلسلة | نعم | رقم تعريف الوكيل الأساسي (مثل `antigravity-preview-05-2026`) |
| `agent_config` | عنصر | لا | إعداد الوكيل الأساسي، بما في ذلك اختيار النموذج (`{"type": "antigravity", "model": "gemini-3.7-flash"}`). الإعداد التلقائي هو `gemini-3.7-flash` إذا تم حذفه. لا يمكن إلغاؤه في وقت التفاعل للوكلاء المسمّين. |
| `system_instruction` | سلسلة | لا | طلب النظام الذي يحدّد السلوك والشخصية |
| `tools` | صفيف | لا | الأدوات التي يمكن للوكيل استخدامها إذا تم حذفه، يكون الإعداد التلقائي هو `code_execution` و`google_search` و`url_context`. تشمل الأدوات المتوافقة `code_execution` و`google_search` و`url_context` و`mcp_server` وتعريفات `function` المخصّصة. |
| `base_environment` | سلسلة أو عنصر | لا | `"remote"` أو `environment_id` أو عنصر إعداد يتضمّن `sources` و`network` يُرجى الرجوع إلى مقالة البيئات. |

### القيود المفروضة على رقم تعريف الوكيل

عند إنشاء وكيل مُدار، يجب أن يتّبع `id` الذي تحدّده القواعد التالية:

- يجب أن يكون فريدًا لمشروعك على السحابة الإلكترونية في Google Cloud.
- يجب **ألا** يبدأ بأي من البادئات المحجوزة التالية (غير حساسة لحالة الأحرف)، وإلا ستفشل عملية الإنشاء:
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

1. **إنشاء نموذج أولي** باستخدام "وكيل Antigravity" الأساسي يمكنك تمرير تعليمات النظام ومصادر البيئة بشكل مضمّن. اختبِر التعليمات والمهارات وإعداد البيئة بشكل تفاعلي.
2. **تثبيت** البيئة يمكنك تثبيت الحِزم وتثبيت المصادر والتأكّد من أنّ كل شيء يعمل.
3. **الاحتفاظ** بالوكيل كوكيل مُدار من خلال إنشاء وكيل جديد، إما من المصادر أو من خلال تفريغ البيئة
4. **تعديل** تعريف الوكيل يمكنك تغيير تعليمات النظام أو تبديل المهارات أو إضافة المصادر. ستستخدم عملية الاستدعاء التالية الإعداد الجديد.

## القيود

- **حالة المعاينة**: الوكلاء المُدارون في مرحلة المعاينة. قد تتغيّر الميزات والمخططات.
- **الوكيل الأساسي والنماذج**: لا يمكن استخدام `antigravity-preview-05-2026` إلا كـ `base_agent`. خيارات النماذج المتوافقة في `agent_config` هي `gemini-3.7-flash` (الإعداد التلقائي) و`gemini-3.6-flash` و`gemini-3.5-flash` و`gemini-3.5-flash-lite`. بالنسبة إلى الوكلاء المسمّين، لا يمكن إلغاء النموذج في وقت التفاعل.
- **لا تتوفّر ميزة التحكّم في الإصدارات**: لا تتوفّر بعد ميزة التحكّم في إصدارات الوكيل والتراجع عنها.
- **لا تتوفّر ميزة تضمين الوكلاء الفرعيين**: لا تتوفّر بعد ميزة تفويض الوكلاء الفرعيين.
- يمكنك إنشاء ما يصل إلى 1000 وكيل مُدار.

## الخطوات التالية

- [نظرة عامة على الوكلاء](https://ai.google.dev/gemini-api/docs/agents?hl=ar): يمكنك التعرّف على المفاهيم الأساسية للوكلاء المُدارين.
- [دليل البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): يمكنك البدء في الإنشاء باستخدام المحادثات المترابطة والعرض تدريجيًا.
- "[وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar): يمكنك استكشاف الإمكانات والأدوات والأسعار للوكيل التلقائي."
- [بيئات الوكلاء](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar): يمكنك إعداد البيئات التجريبية والمصادر والشبكات.
- [Managed Agents API على Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=ar): لإنشاء الوكلاء المُدارين بحوكمة مؤسسية مدمجة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-08-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-08-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
