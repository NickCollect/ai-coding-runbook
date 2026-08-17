---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-BR
fetched_at: 2026-08-17T02:16:41.868206+00:00
title: "Como criar agentes gerenciados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Como criar agentes gerenciados

Os Agentes Gerenciados na API Gemini permitem ampliar o agente do Antigravity com suas próprias instruções, capacidades e dados. É possível [personalizar o agente inline](#customize-inline) no momento da interação ou [salvar a configuração](#save-agent) como um agente gerenciado invocado por ID.

## Personalizar o agente do Antigravity

A maneira mais rápida de criar um agente personalizado é transmitir a configuração inline ao criar uma nova interação sem precisar de uma etapa de registro. É possível ampliar o agente de várias maneiras importantes:

- **[Seleção de modelo](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br#model-selection)**: escolha o modelo do Gemini subjacente usando `agent_config` (o padrão é **Gemini 3.6 Flash**).
- **Instruções do sistema**: transmita texto inline usando `system_instruction` para moldar o comportamento.
- **Ferramentas**: substitua as ferramentas padrão (execução de código, pesquisa, contexto de URL), registre servidores MCP remotos ou defina funções personalizadas (chamada de função).
- **Arquivos e habilidades**: monte arquivos como `AGENTS.md` e `SKILL.md` no ambiente.

Confira um exemplo de transmissão dos três inline:

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

Tudo é definido no momento da interação. Não é necessário registrar nada primeiro. O harness do agente do Antigravity fornece o ambiente de execução (execução de código, gerenciamento de arquivos, acesso à Web) e as camadas de configuração.

### Ferramentas e instruções do sistema

É possível personalizar o comportamento e os recursos do agente para uma interação específica usando os parâmetros `system_instruction` e `tools`.

- **Instruções do sistema**: use o parâmetro `system_instruction` para transmitir texto inline que molda o comportamento do agente. Isso é ideal para ajustes rápidos que você quer mudar por chamada. Os parâmetros `system_instruction` e `AGENTS.md` são aditivos. Os dois são aplicados quando presentes.
- **Ferramentas**: por padrão, o agente do Antigravity tem acesso a `code_execution`, `google_search`, e `url_context`. É possível substituir essa lista transmitindo o parâmetro `tools` no momento da interação. Também é possível registrar [servidores MCP remotos](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br#mcp-servers) ou definir [funções personalizadas (chamada de função)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br#function-calling) para conectar o agente às suas próprias APIs e bancos de dados. Para mais detalhes sobre as ferramentas disponíveis, consulte [Agente Antigravity: ferramentas compatíveis](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br#supported-tools).

### Personalização baseada em arquivos

#### Estrutura do diretório do agente

Embora seja possível transmitir a configuração inline, recomendamos organizar os arquivos do agente em um diretório estruturado. Isso facilita o gerenciamento, o controle de versões e a montagem no ambiente do agente.

Um diretório de projeto de agente típico é assim:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

O ambiente de execução do Antigravity verifica `.agents/` (e a raiz do ambiente) em busca desses arquivos.

#### AGENTS.md

O agente carrega automaticamente `.agents/AGENTS.md` (ou `/.agents/AGENTS.md`) do ambiente como instruções do sistema na inicialização. Use `AGENTS.md` para definições de persona longas, diretrizes detalhadas e instruções que você quer controlar o controle de versões junto com o código.

Monte um `AGENTS.md` usando uma origem inline:

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

#### Habilidades: SKILL.md

As habilidades são arquivos que ampliam os recursos do agente. Coloque-os em `.agents/skills/<skill-name>/SKILL.md`. O harness os descobre e registra automaticamente.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Monte uma habilidade usando uma origem inline:

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

As habilidades carregadas de `.agents/skills/` e `/.agents/skills/` são descobertas automaticamente.

## Criar um agente gerenciado

Depois de iterar na configuração, é possível criá-la como um agente gerenciado com `agents.create`. Isso permite invocar o agente por ID sem repetir a configuração a cada vez.

O `id` especificado ao criar um agente gerenciado precisa ser exclusivo do seu projeto e não pode começar com prefixos reservados (por exemplo, `google-`, `gemini-`). Consulte [Restrições de ID do agente](#agent-id-restrictions) para conferir a lista completa de prefixos restritos.

### De origens

Especifique `base_agent`, `id`, `agent_config`, `system_instruction` e `base_environment` com origens. A plataforma provisiona um sandbox novo com seus arquivos em cada invocação. Consulte [Ambientes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br) para conferir os tipos de origem disponíveis (Git, GCS, inline).

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

### De um ambiente atual (fork)

Itere com o agente do Antigravity de base até que o ambiente esteja correto (pacotes instalados, arquivos no lugar) e, em seguida, bifurque-o em um agente gerenciado.

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

### Com regras de rede

É possível bloquear o acesso de saída ou inserir credenciais ao salvar um agente gerenciado. Para conferir o esquema completo da lista de permissões, os padrões de credenciais e os curingas, consulte [Ambientes: configuração de rede](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#network-configuration).

O exemplo a seguir cria um agente `issue-resolver` que só pode acessar o GitHub e o PyPI, com credenciais injetadas para o GitHub:

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

## Invocar o agente

Chame o agente gerenciado com o ID dele criando uma nova interação. Cada invocação faz um fork do ambiente de base, então cada execução começa limpa.

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

Para conversas multiturno e streaming, consulte o [guia de início rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-br). Os mesmos padrões `previous_interaction_id` e `environment` se aplicam a agentes gerenciados.

Os agentes gerenciados também oferecem suporte à execução e ao cancelamento em segundo plano. Para mais detalhes e exemplos de código, consulte [Agente Antigravity: execução em segundo plano](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br#background-execution).

## Como modificar a configuração na invocação

É possível modificar a configuração de rede `system_instruction`, `tools` e `environment` padrão do agente ao criar uma interação. Isso permite modificar o comportamento, os recursos ou as credenciais do agente para uma execução específica sem mudar a definição do agente armazenado.

### Modificar a instrução do sistema e as ferramentas

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

### Modificar a configuração de rede (atualizar credenciais)

Se o agente gerenciado tiver credenciais de rede incorporadas ao `base_environment`, é possível modificá-las no momento da invocação para atualizar tokens expirados ou alternar chaves de API. Transmita um objeto `environment` com uma nova configuração de `network`. As novas regras de rede substituem totalmente as anteriores para essa interação. As origens do ambiente de base (arquivos, repositórios) são preservadas.

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

## Gerenciar agentes

É possível listar, receber e excluir agentes.

### Listar agentes

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

### Obter um agente

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

### Excluir um agente

A exclusão remove a configuração. Os ambientes e as interações criados pelo agente não são afetados.

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

## Referência da definição do agente

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `id` | string | Sim | Identificador exclusivo do agente no projeto do Google Cloud. Usado para invocar o agente. Não pode usar prefixos reservados. Consulte [Restrições de ID do agente](#agent-id-restrictions). |
| `description` | string | Não | Descrição do agente legível por humanos. |
| `base_agent` | string | Sim | ID do agente de base (por exemplo, `antigravity-preview-05-2026`). |
| `agent_config` | objeto | Não | Configuração do agente de base, incluindo a seleção do modelo (`{"type": "antigravity", "model": "gemini-3.6-flash"}`). O padrão é `gemini-3.6-flash` se omitido. Não pode ser modificado no momento da interação para agentes nomeados. |
| `system_instruction` | string | Não | Comando do sistema que define o comportamento e a persona. |
| `tools` | matriz | Não | Ferramentas que o agente pode usar. Se omitido, o padrão será `code_execution`, `google_search` e `url_context`. As ferramentas compatíveis incluem `code_execution`, `google_search`, `url_context`, `mcp_server` e definições de `function` personalizadas. |
| `base_environment` | string ou objeto | Não | `"remote"`, um `environment_id` ou um objeto de configuração com `sources` e `network`. Consulte Ambientes. |

### Restrições de ID do agente

Ao criar um agente gerenciado, o `id` especificado precisa seguir estas regras:

- Ele precisa ser exclusivo do seu projeto do Google Cloud.
- Ele **não** pode começar com nenhum dos seguintes prefixos reservados (sem distinção entre maiúsculas e minúsculas). Caso contrário, a criação vai falhar:
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

## Fluxo de trabalho de iteração

1. **Crie um protótipo** com o agente do Antigravity de base. Transmita a instrução do sistema e as origens do ambiente inline. Teste instruções, habilidades e configuração do ambiente de forma interativa.
2. **Estabilize** o ambiente. Instale pacotes, monte origens e verifique se tudo funciona.
3. **Persista** como um agente gerenciado criando um novo agente, seja de origens ou fazendo um fork do ambiente.
4. **Atualize** a definição do agente. Mude a instrução do sistema, troque habilidades ou adicione origens. A próxima invocação vai usar a nova configuração.

## Limitações

- **Status de visualização**: os agentes gerenciados estão em visualização. Os recursos e esquemas podem mudar.
- **Agente de base e modelos**: apenas `antigravity-preview-05-2026` é compatível como `base_agent`. As opções de modelo compatíveis em `agent_config` são `gemini-3.5-flash`, `gemini-3.6-flash` (padrão) e `gemini-3.5-flash-lite`. Para agentes nomeados, o modelo não pode ser modificado no momento da interação.
- **Sem controle de versões**: o controle de versões e o rollback do agente ainda não estão disponíveis.
- **Sem aninhamento de subagentes**: a delegação de subagentes ainda não é compatível.
- É possível ter até 1.000 agentes gerenciados.

## A seguir

- [Visão geral dos agentes](https://ai.google.dev/gemini-api/docs/agents?hl=pt-br): saiba mais sobre os conceitos básicos dos agentes gerenciados.
- [Guia de início rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-br): comece a criar com conversas multiturno e streaming.
- [Agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br): conheça os recursos, as ferramentas e os preços do agente padrão.
- [Ambientes de agente](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br): configure sandboxes, origens e rede.
- [API de Agentes Gerenciados na Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=pt-br): para criar agentes com governança organizacional integrada.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
