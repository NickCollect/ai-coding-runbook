---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar
fetched_at: 2026-10-26T05:51:44.673239+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0648\u0643\u0644\u0627\u0621 \u0645\u064f\u062f\u0627\u0631\u064a\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

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

- **[اختيار النموذج](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#model-selection)**: اختَر نموذج Gemini الأساسي من خلال `agent_config` (يكون الخيار التلقائي هو **Gemini 3.8 Flash**).
- **تعليمات النظام**: يمكنك تمرير النص المضمّن عبر `system_instruction` لتحديد سلوك الشكل.
- **الأدوات**: يمكنك تجاهل الأدوات التلقائية (تنفيذ التعليمات البرمجية، والبحث، وسياق عنوان URL)، أو تسجيل خوادم MCP عن بُعد، أو تحديد وظائف مخصّصة (استدعاء الوظائف).
- **الملفات والمهارات**: يمكنك تحميل ملفات مثل `AGENTS.md` و`SKILL.md` في البيئة.

في ما يلي مثال على تمرير جميع المَعلمات الثلاث مضمّنة:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the Q1 revenue data and create a slide deck."))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/AGENTS.md"),
                Content: genai.Ptr("Always use matplotlib for charts. Include a summary table in every report."),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/skills/slide-maker/SKILL.md"),
                Content: genai.Ptr("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:             interactions.AgentOption("antigravity-preview-09-2026"),
            Input:             interactions.NewInteractionsInput("Analyze the Q1 revenue data and create a slide deck."),
            SystemInstruction: genai.Ptr("You are a data analyst. Always include visualizations and export results as PDF."),
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
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

يتم تحديد كل شيء في وقت التفاعل. ليس عليك تسجيل أي شيء أولاً. توفر أداة "وكيل Antigravity" وقت التشغيل (تنفيذ الرموز البرمجية وإدارة الملفات والوصول إلى الويب) وطبقات الإعداد في الأعلى.

### الأدوات وتعليمات النظام

يمكنك تخصيص سلوك الوكيل وإمكاناته لتفاعل معيّن باستخدام المَعلمتَين `system_instruction` و`tools`.

- **تعليمات النظام**: استخدِم المَعلمة `system_instruction` لتمرير نص مضمّن يحدّد سلوك الوكيل. هذه الطريقة مثالية لإجراء تعديلات سريعة تريد تغييرها لكل مكالمة. تُضاف السمتان `system_instruction` و`AGENTS.md` إلى بعضهما، أي أنّهما تسريان معًا عند توفّرهما.
- **الأدوات**: بشكلٍ تلقائي، يمكن لوكيل Antigravity الوصول إلى `code_execution` و`google_search` و`url_context`. يمكنك تجاوز هذه القائمة من خلال تمرير المَعلمة `tools` في وقت التفاعل. يمكنك أيضًا تسجيل [خوادم MCP عن بُعد](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#mcp-servers) أو تحديد [وظائف مخصّصة (استدعاء الدوال)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#function-calling) لربط الوكيل بواجهات برمجة التطبيقات وقواعد البيانات الخاصة بك. للاطّلاع على التفاصيل الكاملة حول الأدوات المتاحة، يُرجى الانتقال إلى [وكيل Antigravity: الأدوات المتوافقة](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#supported-tools).

### التخصيص المستند إلى الملف

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

يحمّل الوكيل تلقائيًا `.agents/AGENTS.md` (أو `/.agents/AGENTS.md`) من البيئة كتعليمات نظام عند بدء التشغيل. استخدِم `AGENTS.md` لتعريفات الشخصيات الطويلة والإرشادات والتعليمات المفصّلة التي تريد التحكّم في إصدارها إلى جانب الرمز البرمجي.

تثبيت `AGENTS.md` باستخدام مصدر مضمّن:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the Q1 revenue data and create a report."))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/AGENTS.md"),
                Content: genai.Ptr("Always use matplotlib for charts. Include a summary table in every report."),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:             interactions.AgentOption("antigravity-preview-09-2026"),
            Input:             interactions.NewInteractionsInput("Analyze the Q1 revenue data and create a report."),
            SystemInstruction: genai.Ptr("You are a data analyst. Always include visualizations and export results as PDF."),
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
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

المهارات هي ملفات توسّع إمكانات الوكيل. ضَعها تحت `.agents/skills/<skill-name>/SKILL.md` وسيتم العثور عليها وتسجيلها تلقائيًا.

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
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Create a presentation about our Q1 results."))
    .systemInstruction("You create presentations from data.")
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/skills/slide-maker/SKILL.md"),
                Content: genai.Ptr("---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:             interactions.AgentOption("antigravity-preview-09-2026"),
            Input:             interactions.NewInteractionsInput("Create a presentation about our Q1 results."),
            SystemInstruction: genai.Ptr("You create presentations from data."),
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
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

بعد تكرار عملية الإعداد، يمكنك إنشاء وكيل مُدار باستخدام `agents.create`. يتيح لك ذلك استدعاء الوكيل حسب المعرّف بدون تكرار الإعداد في كل مرة.

يجب أن يكون `id` الذي تحدّده عند إنشاء وكيل مُدار فريدًا لمشروعك ويجب ألا يبدأ بالبادئات المحجوزة (مثل `google-` و`gemini-`). اطّلِع على [قيود معرّف الوكيل](#agent-id-restrictions) للحصول على القائمة الكاملة بالبادئات المحظورة.

### من المصادر

حدِّد `base_agent` و`id` و`agent_config` و`system_instruction` و`base_environment` مع المصادر. توفّر المنصة بيئة اختبار معزولة جديدة تتضمّن ملفاتك في كل عملية استدعاء. راجِع [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar) لمعرفة أنواع المصادر المتاحة (Git وGCS والمضمّنة).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-09-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.8-flash",
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
    base_agent: "antigravity-preview-09-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.8-flash",
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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.AgentConfig;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.")
            .build(),
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/my-org/analysis-templates")
            .target("/workspace/templates")
            .build()
    ))
    .build();

Agent agentParams = Agent.builder()
    .id("data-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .agentConfig(AgentConfig.of(
        AntigravityAgentConfig.builder()
            .model("gemini-3.8-flash")
            .build()
    ))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Created agent: " + agent.id().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/agents"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/AGENTS.md"),
                Content: genai.Ptr("Always use matplotlib for charts. Include a summary table in every report."),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/skills/slide-maker/SKILL.md"),
                Content: genai.Ptr("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."),
            },
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/my-org/analysis-templates"),
                Target: genai.Ptr("/workspace/templates"),
            },
        },
    }

    res, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:        genai.Ptr("data-analyst"),
            BaseAgent: genai.Ptr("antigravity-preview-09-2026"),
            AgentConfig: genai.Ptr(agents.NewAgentConfig(interactions.AntigravityAgentConfig{
                Model: genai.Ptr("gemini-3.8-flash"),
            })),
            SystemInstruction: genai.Ptr("You are a data analyst. Always include visualizations and export results as PDF."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(env)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created agent: %s\n", *res.Agent.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-09-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.8-flash"
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

### من بيئة حالية (تفريغ)

كرِّر استخدام وكيل Antigravity الأساسي إلى أن تصبح البيئة مناسبة (تثبيت الحِزم، ووضع الملفات في مكانها)، ثم أنشئ نسخة من الوكيل الأساسي في وكيل مُدار.

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-09-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// Step 1: set up the environment interactively
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Step 2: fork that environment into a managed agent
Agent agentParams = Agent.builder()
    .id("my-data-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .systemInstruction("You are a data analyst. Use the template at /workspace/template.py for all reports.")
    .baseEnvironment(BaseEnvironment.of(interaction.environmentId().orElse("")))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Forked agent successfully: " + agent.id().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/agents"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Step 1: set up the environment interactively
    intRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := intRes.Interaction

    // Step 2: fork that environment into a managed agent
    agentRes, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:                genai.Ptr("my-data-analyst"),
            BaseAgent:         genai.Ptr("antigravity-preview-09-2026"),
            SystemInstruction: genai.Ptr("You are a data analyst. Use the template at /workspace/template.py for all reports."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(*interaction.EnvironmentID)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Forked agent successfully: %s\n", *agentRes.Agent.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### باستخدام قواعد الشبكة

يمكنك حظر الوصول الخارجي أو إدخال بيانات الاعتماد عند حفظ وكيل مُدار. للاطّلاع على مخطط قائمة السماح الكاملة وأنماط بيانات الاعتماد وأحرف البدل، يُرجى الانتقال إلى [البيئات: إعدادات الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration).

يمكنك الإشارة إلى [بيانات اعتماد](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ar) مخزَّنة حسب المعرّف في قاعدة القائمة المسموح بها (`"credential": "github-production"`)، ويُدرج الخادم الوكيل للخروج السر في وقت الطلب، وبالتالي لا يظهر أبدًا في تعريف الوكيل. يضبط هذا المثال العنوان مضمّنًا مع `transform` بدلاً من ذلك. يطبّق الخادم الوكيل كلا النموذجين بالطريقة نفسها، كما تتيح لك بيانات الاعتماد إعادة استخدام كلمة المرور في جميع البرامج وتغييرها في مكان واحد.

ينشئ المثال التالي وكيلاً `issue-resolver` يمكنه الوصول إلى GitHub وPyPI فقط، مع إدخال بيانات الاعتماد الخاصة بـ GitHub:

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-09-2026",
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
    base_agent: "antigravity-preview-09-2026",
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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/my-org/backend")
            .target("/workspace/repo")
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            )))
            .build()
    ))
    .build();

Agent agentParams = Agent.builder()
    .id("issue-resolver")
    .baseAgent("antigravity-preview-09-2026")
    .systemInstruction("You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Created issue-resolver agent successfully: " + agent.id().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/agents"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/my-org/backend"),
                Target: genai.Ptr("/workspace/repo"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Basic YOUR_BASE64_TOKEN",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
            })),
        })),
    }

    res, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:                genai.Ptr("issue-resolver"),
            BaseAgent:         genai.Ptr("antigravity-preview-09-2026"),
            SystemInstruction: genai.Ptr("You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(env)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created issue-resolver agent successfully: %s\n", *res.Agent.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-09-2026",
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

اتّصِل بالوكيل المُدار باستخدام معرّف الوكيل من خلال إنشاء تفاعل جديد. يؤدي كل استدعاء إلى إنشاء نسخة من البيئة الأساسية، لذا تبدأ كل عملية تشغيل بشكل نظيف.

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("data-analyst"))
    .input(InteractionsInput.of("Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(result.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("data-analyst"),
            Input:       interactions.NewInteractionsInput("Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

للمحادثات المتعددة الأدوار والبث، يُرجى الاطّلاع على [البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar). ينطبق النمطان `previous_interaction_id` و`environment` نفسهما على الوكلاء المُدارين.

تتيح الوكلاء المُدارين أيضًا تنفيذ المهام في الخلفية وإلغاءها. للاطّلاع على التفاصيل وأمثلة الرموز البرمجية، يُرجى الاطّلاع على [وكيل Antigravity: التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar#background-execution).

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("data-analyst"))
    .input(InteractionsInput.of("Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table."))
    .systemInstruction("You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.")
    .tools(List.of(CodeExecution.builder().build())) // Override to only use code execution
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(result.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:             interactions.AgentOption("data-analyst"),
            Input:             interactions.NewInteractionsInput("Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table."),
            SystemInstruction: genai.Ptr("You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides."),
            Tools:             []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})}, // Override to only use code execution
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

### تجاوز إعدادات الشبكة (إعادة تحميل بيانات الاعتماد)

إذا كان وكيلك المُدار يتضمّن بيانات اعتماد شبكة مضمّنة في `base_environment`، يمكنك إلغاء هذه البيانات في وقت الاستدعاء لتحديث الرموز المميزة المنتهية الصلاحية أو تدوير مفاتيح واجهة برمجة التطبيقات. مرِّر عنصر `environment` مع إعدادات `network` جديدة. تحلّ قواعد الشبكة الجديدة محلّ القواعد السابقة بشكل كامل في ما يتعلّق بهذا التفاعل. يتم الاحتفاظ بمصادر البيئة الأساسية (الملفات والمستودعات).

إذا كان `base_environment` يشير إلى [بيانات اعتماد](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ar) مخزّنة بدلاً من رمز مميّز مضمّن، لن تحتاج إلى إلغاء أي شيء. يمكنك تدوير بيانات الاعتماد باستخدام `PATCH`، وسيتمكّن كل وكيل يشير إليها من الحصول على الرمز السري الجديد في عملية التشغيل التالية.

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Invoke the agent with a fresh token, overriding the base_environment credentials
Environment env = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_REFRESHED_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("issue-resolver"))
    .input(InteractionsInput.of("Fix issue #42 and open a PR."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(result.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Invoke the agent with a fresh token, overriding the base_environment credentials
    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("issue-resolver"),
            Input:       interactions.NewInteractionsInput("Fix issue #42 and open a PR."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

### عرض قائمة الوكلاء

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import java.util.List;

Client client = new Client();

List<Agent> agents = client.agents.listDirect().agentListResponse().get().agents().orElse(List.of());
for (Agent a : agents) {
    System.out.println(a.id().orElse("") + ": " + a.description().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Agents.List(ctx, operations.ListAgentsRequest{})
    if err != nil {
        log.Fatal(err)
    }

    if res.AgentListResponse != nil {
        for _, a := range res.AgentListResponse.Agents {
            fmt.Printf("%s: %v\n", *a.ID, a.Description)
        }
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

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;

Client client = new Client();

Agent agent = client.agents.get("data-analyst").agent().get();
System.out.println(agent);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Agents.Get(ctx, operations.GetAgentRequest{
        ID: "data-analyst",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("%+v\n", res.Agent)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### حذف وكيل

يؤدي الحذف إلى إزالة الإعدادات. لن تتأثر البيئات والتفاعلات الحالية التي أنشأها الوكيل.

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### جافا

```
import com.google.genai.Client;

Client client = new Client();

client.agents.delete("data-analyst");
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Agents.Delete(ctx, operations.DeleteAgentRequest{
        ID: "data-analyst",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## مرجع تعريف الوكيل

| الحقل | النوع | مطلوب | الوصف |
| --- | --- | --- | --- |
| `id` | سلسلة | نعم | المعرّف الفريد للوكيل ضمن مشروع Google Cloud يُستخدَم لاستدعاء الوكيل. يجب عدم استخدام البادئات المحجوزة. اطّلِع على [قيود معرّف الوكيل](#agent-id-restrictions). |
| `description` | سلسلة | لا | وصف الوكيل يمكن لشخص عادي قراءته |
| `base_agent` | سلسلة | نعم | معرّف الوكيل الأساسي (مثلاً، `antigravity-preview-09-2026`) |
| `agent_config` | عنصر | لا | إعدادات الوكيل الأساسي، بما في ذلك اختيار النموذج (`{"type": "antigravity", "model": "gemini-3.8-flash"}`). يتم ضبط القيمة التلقائية على `gemini-3.8-flash` في حال عدم إدخالها. لا يمكن إلغاؤها في وقت التفاعل مع العملاء المحدّدين. |
| `system_instruction` | سلسلة | لا | تلقين النظام الذي يحدّد السلوك والشخصية |
| `tools` | صفيف | لا | الأدوات التي يمكن للوكيل استخدامها في حال عدم تحديدها، يتم ضبطها تلقائيًا على `code_execution` و`google_search` و`url_context`. تشمل الأدوات المتوافقة `code_execution` و`google_search` و`url_context` و`mcp_server` وتعريفات `function` المخصّصة. |
| `base_environment` | سلسلة أو عنصر | لا | `"remote"` أو `environment_id` أو عنصر إعدادات يتضمّن `sources` و`network` راجِع قسم "البيئات". |

### القيود المفروضة على معرّف الوكيل

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

1. **إنشاء نموذج أولي** باستخدام وكيل Antigravity الأساسي تمرير تعليمات النظام ومصادر البيئة مضمّنة اختبار التعليمات والمهارات وإعداد البيئة بشكلٍ تفاعلي
2. **تثبيت** البيئة ثبِّت الحِزم، واربط المصادر، وتأكَّد من أنّ كل شيء يعمل بشكل سليم.
3. **الاستمرار** كوكيل مُدار من خلال إنشاء وكيل جديد، إما من المصادر أو من خلال إنشاء نسخة من البيئة.
4. **عدِّل** تعريف الوكيل. تغيير تعليمات النظام أو تبديل المهارات أو إضافة مصادر سيتم استخدام الإعدادات الجديدة في عملية الاستدعاء التالية.

## القيود

- **حالة المعاينة**: الوكلاء المُدارون في مرحلة المعاينة. قد تتغيّر الميزات والمخططات.
- **الوكيل والنماذج الأساسية**: لا تتوفّر سوى القيمة `antigravity-preview-09-2026` كـ `base_agent`. خيارات النماذج المتوافقة في `agent_config` هي `gemini-3.8-flash` (الإعداد التلقائي) و`gemini-3.6-flash` و`gemini-3.5-flash-lite`. بالنسبة إلى الوكلاء المحدّدين، لا يمكن تجاهل النموذج في وقت التفاعل.
- **عدم توفّر ميزة التحكم بالإصدار**: لا تتوفّر بعد ميزة التحكم بإصدارات الوكيل والرجوع إلى إصدار سابق.
- **عدم إمكانية إنشاء وكلاء فرعيين متداخلين**: لا تتوفّر بعد إمكانية تفويض وكيل فرعي.
- يمكنك إضافة ما يصل إلى 1,000 وكيل مُدار.

## الخطوات التالية

- [نظرة عامة على الوكلاء](https://ai.google.dev/gemini-api/docs/agents?hl=ar): تعرَّف على المفاهيم الأساسية للوكلاء المُدارين.
- [البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): ابدأ إنشاء تطبيقات باستخدام المحادثات المتعددة الأدوار والبث.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar): استكشاف الإمكانات والأدوات والأسعار الخاصة بوكيل Antigravity
- [بيئات الوكيل](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar): يمكنك ضبط البيئات التجريبية والمصادر والشبكات.
- [واجهة برمجة التطبيقات الخاصة بالوكلاء المُدارين على "منصة الوكلاء"](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=ar): لإنشاء وكلاء مع أدوات حوكمة مدمجة في المؤسسة

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-09 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-09 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
