---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr
fetched_at: 2026-07-20T04:34:07.803280+00:00
title: "Y\u00f6netilen Ajanlar Olu\u015fturma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yönetilen Ajanlar Oluşturma

Gemini API'deki yönetilen ajanlar, Antigravity ajanını kendi talimatlarınız, becerileriniz ve verilerinizle genişletmenize olanak tanır. Etkileşim sırasında [aracıyı satır içinde özelleştirebilir](#customize-inline) veya [yapılandırmayı](#save-agent), kimliğe göre çağırdığınız yönetilen bir aracı olarak kaydedebilirsiniz.

## Antigravity ajanını özelleştirme

Özel bir aracı oluşturmanın en hızlı yolu, yeni bir etkileşim oluştururken yapılandırmanızı satır içi olarak iletmektir. Bu işlem için kayıt adımı gerekmez. Aracıyı üç şekilde uzatabilirsiniz:

- **Sistem talimatları**: Davranışı şekillendirmek için satır içi metni `system_instruction` ile iletin.
- **Araçlar**: Varsayılan araçları (Kod Yürütme, Arama, URL Bağlamı) geçersiz kılın, uzak MCP sunucularını kaydedin veya özel işlevler (İşlev Çağırma) tanımlayın.
- **Dosyalar ve beceriler**: `AGENTS.md` ve `SKILL.md` gibi dosyaları ortama yerleştirin.

Üçünün de satır içi olarak iletilmesine ilişkin bir örnek:

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

Her şey etkileşim sırasında tanımlanır. Önceden herhangi bir kayıt işlemi yapmanız gerekmez. Antigravity aracı, çalışma zamanını (kod yürütme, dosya yönetimi, web erişimi) sağlar ve yapılandırma katmanlarınız bunun üzerine eklenir.

### Araçlar ve sistem talimatları

`system_instruction` ve `tools` parametrelerini kullanarak aracının davranışını ve özelliklerini belirli bir etkileşim için özelleştirebilirsiniz.

- **Sistem talimatları**: Aracının davranışını şekillendiren satır içi metni iletmek için `system_instruction` parametresini kullanın. Bu özellik, her görüşmede değiştirmek istediğiniz hızlı düzenlemeler için idealdir. `system_instruction` ve `AGENTS.md` toplamsaldır. Her ikisi de mevcut olduğunda geçerlidir.
- **Araçlar**: Antigravity aracısı varsayılan olarak `code_execution`, `google_search` ve `url_context`'e erişebilir. Etkileşim sırasında `tools` parametresini ileterek bu listeyi geçersiz kılabilirsiniz. Ayrıca, aracıyı kendi API'lerinize ve veritabanlarınıza bağlamak için [uzak MCP sunucuları](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#mcp-servers) kaydedebilir veya [özel işlevler (işlev çağırma)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#function-calling) tanımlayabilirsiniz. Kullanılabilen araçlarla ilgili tüm ayrıntılar için [Antigravity Agent: Desteklenen araçlar](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#supported-tools) başlıklı makaleyi inceleyin.

### Dosyaya dayalı özelleştirme

#### Aracı dizin yapısı

Yapılandırmayı satır içi olarak iletebilirsiniz ancak aracınızın dosyalarını yapılandırılmış bir dizinde düzenlemenizi öneririz. Bu sayede yönetmek, sürüm kontrolü yapmak ve aracının ortamına monte etmek daha kolay olur.

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

Aracı, başlangıçta ortamdan `.agents/AGENTS.md` (veya `/.agents/AGENTS.md`) öğesini sistem talimatları olarak otomatik olarak yükler. Uzun karakter tanımları, ayrıntılı yönergeler ve kodunuzla birlikte sürüm kontrolü yapmak istediğiniz talimatlar için `AGENTS.md` kullanın.

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

Beceriler, ajanın yeteneklerini genişleten dosyalardır. Bunları `.agents/skills/<skill-name>/SKILL.md` altına yerleştirin. Böylece, donanım bunları otomatik olarak keşfedip kaydeder.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Satır içi kaynak kullanarak beceri yükleme:

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

`.agents/skills/` ve `/.agents/skills/` kaynaklarından yüklenen beceriler otomatik olarak keşfedilir.

## Yönetilen aracı oluşturma

Yapılandırmanızı yineledikten sonra `agents.create` ile yönetilen bir aracı olarak oluşturabilirsiniz. Bu sayede, yapılandırmayı her seferinde tekrarlamadan aracıyı kimliğe göre çağırabilirsiniz.

Yönetilen bir aracı oluştururken belirttiğiniz `id`, projenize özel olmalı ve ayrılmış ön eklerle (ör. `google-`, `gemini-`) başlamamalıdır. Kısıtlanmış ön eklerin tam listesi için [Aracı kimliği kısıtlamaları](#agent-id-restrictions) bölümüne bakın.

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

### Mevcut bir ortamdan (çatal)

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
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### Ağ kurallarıyla

Yönetilen bir aracı kaydederken giden erişimi kilitleyebilir veya kimlik bilgilerini ekleyebilirsiniz. İzin verilenler listesi şeması, kimlik bilgisi kalıpları ve joker karakterler hakkında ayrıntılı bilgi için [Ortamlar: Ağ yapılandırması](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#network-configuration) başlıklı makaleyi inceleyin.

Aşağıdaki örnekte, GitHub ve PyPI'ye erişebilen ve GitHub için kimlik bilgilerinin yerleştirildiği bir `issue-resolver` aracısı oluşturulur:

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

## Temsilciyi çağırma

Yeni bir etkileşim oluşturarak yönetilen temsilcinizi temsilci kimliğinizle arayın. Her çağırma işlemi temel ortamı çatalladığından her çalıştırma temiz bir şekilde başlar.

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

Çok turlu görüşmeler ve akış için [Hızlı Başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr) bölümüne bakın. Aynı `previous_interaction_id` ve `environment` kalıpları, yönetilen aracılar için de geçerlidir.

Yönetilen temsilciler, arka planda yürütmeyi ve iptali de destekler. Ayrıntılar ve kod örnekleri için [Antigravity Agent: Background execution](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#background-execution) (Antigravity Agent: Arka planda yürütme) başlıklı makaleyi inceleyin.

## Çağırma sırasında yapılandırmayı geçersiz kılma

Bir etkileşim oluştururken aracının varsayılan `system_instruction`, `tools` ve `environment` ağ yapılandırmasını geçersiz kılabilirsiniz. Bu sayede, depolanan aracı tanımını değiştirmeden belirli bir çalıştırma için aracının davranışını, özelliklerini veya kimlik bilgilerini değiştirebilirsiniz.

### Sistem talimatını ve araçlarını geçersiz kılma

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

### Ağ yapılandırmasını geçersiz kılma (kimlik bilgilerini yenileme)

Yönetilen aracınızın `base_environment` kimlik bilgileri varsa, süresi dolmuş jetonları yenilemek veya API anahtarlarını döndürmek için bunları çağırma sırasında geçersiz kılabilirsiniz. Yeni bir `network` yapılandırmasıyla `environment` nesnesi iletin. Yeni ağ kuralları, söz konusu etkileşim için önceki kuralların tamamen yerini alır. Temel ortamın kaynakları (dosyalar, depolar) korunur.

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

### Aracı edinme

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

Silme işlemi, yapılandırmayı kaldırır. Mevcut ortamlar ve ajan tarafından oluşturulan etkileşimler etkilenmez.

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
| `id` | dize | Evet | Google Cloud projesindeki benzersiz aracı tanımlayıcısı. Aracı çağırmak için kullanılır. Ayrılmış önekler kullanılmamalıdır. [Aracı kimliği kısıtlamaları](#agent-id-restrictions) başlıklı makaleyi inceleyin. |
| `description` | dize | Hayır | Temsilcinin kullanıcılar tarafından okunabilir açıklaması. |
| `base_agent` | dize | Evet | Temel aracı kimliği (ör. `antigravity-preview-05-2026`). |
| `system_instruction` | dize | Hayır | Davranışı ve kullanıcı profilini tanımlayan sistem istemi. |
| `tools` | dizi | Hayır | Ajanın kullanabileceği araçlar. Boş bırakılırsa varsayılan olarak `code_execution`, `google_search` ve `url_context` değerleri kullanılır. Desteklenen araçlar arasında `code_execution`, `google_search`, `url_context`, `mcp_server` ve özel `function` tanımları yer alır. |
| `base_environment` | dize veya nesne | Hayır | `"remote"`, `environment_id` veya `sources` ve `network` içeren bir yapılandırma nesnesi. Ortamlar bölümüne bakın. |

### Aracı kimliği kısıtlamaları

Yönetilen bir aracı oluştururken belirttiğiniz `id` şu kurallara uymalıdır:

- Google Cloud projenize özgü olmalıdır.
- Aksi takdirde oluşturma işlemi başarısız olacağından, aşağıdaki ayrılmış öneklerden (büyük/küçük harfe duyarsız) biriyle **başlamamalıdır**:
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

## Yineleme iş akışı

1. Temel Antigravity temsilcisiyle **prototip oluşturun**. Sistem talimatını ve ortam kaynaklarını satır içi olarak iletin. Talimatları, becerileri ve ortam kurulumunu etkileşimli olarak test edin.
2. Ortamı **dengeleyin**. Paketleri yükleyin, kaynakları bağlayın ve her şeyin çalıştığını doğrulayın.
3. Kaynaklardan veya ortamı çatallayarak yeni bir aracı oluşturup yönetilen aracı olarak **kalıcı hale getirin**.
4. Aracı tanımını **güncelleyin**. Sistem talimatını değiştirme, becerileri değiştirme veya kaynak ekleme Bir sonraki çağırmada yeni yapılandırma kullanılır.

## Sınırlamalar

- **Önizleme durumu**: Yönetilen aracıların önizleme sürümü kullanımdadır. Özellikler ve şemalar değişebilir.
- **Temel aracı**: `base_agent` olarak yalnızca `antigravity-preview-05-2026` desteklenir.
- **Sürüm oluşturma yok**: Ajan sürümü oluşturma ve geri alma henüz kullanılamıyor.
- **Alt temsilci iç içe yerleştirme yok**: Alt temsilci yetkilendirme henüz desteklenmemektedir.
- En fazla 1.000 yönetilen aracınız olabilir.

## Sırada ne var?

- [Ajanlara Genel Bakış](https://ai.google.dev/gemini-api/docs/agents?hl=tr): Yönetilen ajanların temel kavramları hakkında bilgi edinin.
- [Hızlı başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr): Çok adımlı görüşmeler ve akışla geliştirmeye başlayın.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr): Varsayılan temsilcinin özelliklerini, araçlarını ve fiyatlandırmasını keşfedin.
- [Aracı Ortamları](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr): Sanal alanları, kaynakları ve ağı yapılandırın.
- [Agent Platform'da Yönetilen Ajanlar API'si](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=tr): Yerleşik kurumsal yönetim özelliklerine sahip ajanlar oluşturmak için kullanılır.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-08 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-08 UTC."],[],[]]
