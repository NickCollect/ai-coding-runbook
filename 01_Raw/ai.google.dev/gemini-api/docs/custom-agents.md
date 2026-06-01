---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr
fetched_at: 2026-06-01T06:09:09.759636+00:00
title: "Y\u00f6netilen Ajanlar Olu\u015fturma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yönetilen Ajanlar Oluşturma

Gemini API'deki yönetilen ajanlar, Antigravity ajanını kendi talimatlarınız, becerileriniz ve verilerinizle genişletmenize olanak tanır. Etkileşim sırasında [aracıyı satır içinde özelleştirebilir](#customize-inline) veya [yapılandırmayı kaydedebilirsiniz](#save-agent). Bu durumda, aracıyı kimliğe göre çağırarak yönetebilirsiniz.

## Antigravity aracısını özelleştirme

Özel bir aracı oluşturmanın en hızlı yolu, yeni bir etkileşim oluştururken yapılandırmanızı satır içi olarak iletmektir. Kayıt adımı gerekmez. Aracıyı üç şekilde genişletebilirsiniz:

- **Sistem talimatları**: Davranışı şekillendirmek için satır içi metni `system_instruction` ile iletin.
- **Araçlar**: Varsayılan araçları (Kod Yürütme, Arama, URL Bağlamı) geçersiz kılın.
- **Dosyalar ve beceriler**: `AGENTS.md` ve `SKILL.md` gibi dosyaları ortama yerleştirin.

Üçünün de satır içi olarak iletilmesine ilişkin bir örneği aşağıda bulabilirsiniz:

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

Her şey etkileşim sırasında tanımlanır. Önceden herhangi bir kayıt işlemi yapmanız gerekmez. Antigravity aracı donanımı, çalışma zamanını (kod yürütme, dosya yönetimi, web erişimi) sağlar ve yapılandırma katmanlarınız bu donanımın üzerinde yer alır.

### Araçlar ve sistem talimatları

`system_instruction` ve `tools` parametrelerini kullanarak aracının davranışını ve özelliklerini belirli bir etkileşim için özelleştirebilirsiniz.

- **Sistem talimatları**: Aracının davranışını şekillendiren satır içi metni iletmek için `system_instruction` parametresini kullanın. Bu özellik, her görüşmede değiştirmek istediğiniz hızlı düzenlemeler için idealdir. `system_instruction` ve `AGENTS.md` toplamsaldır. Her ikisi de mevcut olduğunda geçerlidir.
- **Araçlar**: Antigravity aracısı varsayılan olarak `code_execution`, `google_search` ve `url_context`'e erişebilir. Etkileşim sırasında `tools` parametresini ileterek bu listeyi geçersiz kılabilirsiniz. Kullanılabilir araçlar ve bunların nasıl kullanılacağıyla ilgili tüm ayrıntılar için [Antigravity Agent: Desteklenen araçlar](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#supported-tools) başlıklı makaleyi inceleyin.

### Dosyaya dayalı özelleştirme

#### Aracı dizin yapısı

Yapılandırmayı satır içi olarak iletebilirsiniz ancak aracınızın dosyalarını yapılandırılmış bir dizinde düzenlemenizi öneririz. Bu sayede yönetmek, sürüm denetimi yapmak ve aracının ortamına monte etmek daha kolay olur.

Tipik bir aracı projesi dizini şu şekilde görünür:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Antigravity çalışma zamanı, bu dosyalar için `.agents/` (ve ortamın kökünü) tarar.

#### AGENTS.md

Aracı, başlatıldığında ortamdan `.agents/AGENTS.md` (veya `/.agents/AGENTS.md`) öğesini sistem talimatları olarak otomatik olarak yükler. Uzun persona tanımları, ayrıntılı yönergeler ve kodunuzla birlikte sürüm denetimi yapmak istediğiniz talimatlar için `AGENTS.md` kullanın.

Satır içi kaynak kullanarak `AGENTS.md` bağlama:

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

#### Beceriler: SKILL.md

Beceriler, aracının yeteneklerini genişleten dosyalardır. Bunları `.agents/skills/<skill-name>/SKILL.md` altına yerleştirin. Böylece, koşum otomatik olarak keşfedip kaydeder.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Satır içi kaynak kullanarak beceri bağlama:

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

`.agents/skills/` ve `/.agents/skills/` kaynaklarından yüklenen beceriler otomatik olarak keşfedilir.

## Yönetilen aracı oluşturma

Yapılandırmanızı yineledikten sonra `agents.create` ile yönetilen bir aracı olarak oluşturabilirsiniz. Bu sayede, yapılandırmayı her seferinde tekrarlamadan aracıyı kimliğe göre çağırabilirsiniz.

### Kaynaklardan

Kaynaklarla birlikte `base_agent`, `id`, `system_instruction` ve `base_environment` değerlerini belirtin. Platform, her çağırmada dosyalarınızla yeni bir sanal alan sağlar. Kullanılabilir kaynak türleri (Git, GCS, satır içi) için [Ortamlar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr) bölümüne bakın.

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

### Mevcut bir ortamdan (fork)

Ortam doğru olana kadar (paketler yüklendi, dosyalar yerinde) temel Antigravity aracısıyla yineleme yapın, ardından bunu yönetilen bir aracıya çatallayın.

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

### Ağ kurallarıyla

Yönetilen bir aracı kaydederken giden erişimi kilitleyebilir veya kimlik bilgilerini ekleyebilirsiniz. İzin verilenler listesi şemasının, kimlik bilgisi kalıplarının ve joker karakterlerin tam listesi için [Ortamlar: Ağ yapılandırması](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#network-configuration) başlıklı makaleyi inceleyin.

Aşağıdaki örnekte, GitHub ve PyPI'ye erişebilen ve GitHub için kimlik bilgilerinin yerleştirildiği bir `issue-resolver` aracısı oluşturuluyor:

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

## Temsilciyi çağırma

Yeni bir etkileşim oluşturarak yönetilen aracınızı arayın. Her çağırma işlemi temel ortamı çatalladığından her çalıştırma temiz bir şekilde başlar.

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

Çok adımlı görüşmeler ve yayın için [Hızlı Başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr) bölümüne bakın. Aynı `previous_interaction_id` ve `environment` kalıpları, yönetilen temsilciler için de geçerlidir.

## Çağırma sırasında yapılandırmayı geçersiz kılma

Etkileşim oluştururken aracının varsayılan `system_instruction` ve `tools` değerlerini geçersiz kılabilirsiniz. Bu sayede, depolanan aracı tanımını değiştirmeden belirli bir çalıştırma için aracının davranışını veya özelliklerini değiştirebilirsiniz.

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

## Aracıları yönet

Aracıları listeleyebilir, alabilir ve silebilirsiniz.

### Aracıları listeleyin

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

### Müşteri temsilcisine bağlanma

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

### Temsilci silme

Silme işlemi, yapılandırmayı kaldırır. Mevcut ortamlar ve aracının oluşturduğu etkileşimler etkilenmez.

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

## Aracı tanımı referansı

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `id` | dize | Evet | Benzersiz aracı tanımlayıcısı. Ajanı çağırmak için kullanılır. |
| `description` | dize | Hayır | Temsilcinin, kullanıcılar tarafından okunabilir açıklaması. |
| `base_agent` | dize | Evet | Temel temsilci kimliği (ör. `antigravity-preview-05-2026`). |
| `system_instruction` | dize | Hayır | Davranışı ve kullanıcı profilini tanımlayan sistem istemi. |
| `tools` | dize veya nesne | Hayır | Temsilcinin kullanabileceği araçlar. Bu araçlar `code_execution`, `google_search` ve `url_context` erişimine sahip olacak. |
| `base_environment` | dize veya nesne | Hayır | `"remote"`, `environment_id` veya `sources` ve `network` içeren bir yapılandırma nesnesi. Ortamlar bölümüne bakın. |

## Yineleme iş akışı

1. Temel Antigravity temsilcisiyle **prototip oluşturun**. Sistem talimatını ve ortam kaynaklarını satır içi olarak iletin. Talimatları, becerileri ve ortam kurulumunu etkileşimli olarak test edin.
2. Ortamı **dengeleyin**. Paketleri yükleyin, kaynakları bağlayın ve her şeyin çalıştığını doğrulayın.
3. Kaynaklardan veya ortamı çatallayarak yeni bir aracı oluşturup yönetilen aracı olarak **kalıcı hale getirin**.
4. Temsilci tanımını **güncelleyin**. Sistem talimatını değiştirme, becerileri değiştirme veya kaynak ekleme Bir sonraki çağırma işleminde yeni yapılandırma kullanılır.

## Sınırlamalar

- **Önizleme durumu**: Yönetilen aracılar önizleme aşamasındadır. Özellikler ve şemalar değişebilir.
- **Temel aracı**: `base_agent` olarak yalnızca `antigravity-preview-05-2026` desteklenir.
- **Sürüm oluşturma yok**: Temsilci sürüm oluşturma ve geri alma henüz kullanılamıyor.
- **Alt temsilci iç içe yerleştirme yok**: Alt temsilci yetkilendirme henüz desteklenmemektedir.
- En fazla 1.000 yönetilen aracınız olabilir.

## Sırada ne var?

- [Temsilcilere Genel Bakış](https://ai.google.dev/gemini-api/docs/agents?hl=tr): Yönetilen temsilcilerin temel kavramları hakkında bilgi edinin.
- [Hızlı başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr): Çok adımlı görüşmeler ve akışla geliştirmeye başlayın.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr): Varsayılan temsilcinin özelliklerini, araçlarını ve fiyatlandırmasını keşfedin.
- [Aracı Ortamları](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr): Sanal alanları, kaynakları ve ağı yapılandırın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-20 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-20 UTC."],[],[]]
