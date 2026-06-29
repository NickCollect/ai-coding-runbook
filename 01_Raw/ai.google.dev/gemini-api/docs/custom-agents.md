---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr
fetched_at: 2026-06-29T05:40:35.143697+00:00
title: "Cr\u00e9er des agents g\u00e9r\u00e9s \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Créer des agents gérés

Les agents gérés de l'API Gemini vous permettent d'étendre l'agent Antigravity avec vos propres instructions, compétences et données. Vous pouvez [personnaliser l'agent de manière intégrée](#customize-inline) au moment de l'interaction ou [enregistrer la configuration](#save-agent) en tant qu'agent géré que vous appelez par ID.

## Personnaliser l'agent Antigravity

Le moyen le plus rapide de créer un agent personnalisé consiste à transmettre votre configuration de manière intégrée lors de la création d'une interaction, sans aucune étape d'enregistrement requise. Vous pouvez étendre l'agent de trois manières :

- **Instructions système** : transmettez du texte intégré via `system_instruction` pour façonner le comportement.
- **Outils** : remplacez les outils par défaut (exécution de code, recherche, contexte d'URL), enregistrez des serveurs MCP distants ou définissez des fonctions personnalisées (appel de fonction).
- **Fichiers et compétences** : montez des fichiers tels que `AGENTS.md` et `SKILL.md` dans l'environnement.

Voici un exemple de transmission des trois éléments de manière intégrée :

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

Tout est défini au moment de l'interaction. Il n'est pas nécessaire d'enregistrer quoi que ce soit au préalable. Le harnais de l'agent Antigravity fournit l'environnement d'exécution (exécution de code, gestion de fichiers, accès Web) et vos couches de configuration par-dessus.

### Outils et instructions système

Vous pouvez personnaliser le comportement et les capacités de l'agent pour une interaction spécifique à l'aide des paramètres `system_instruction` et `tools`.

- **Instructions système** : utilisez le paramètre `system_instruction` pour transmettre du texte intégré qui façonne le comportement de l'agent. Cette solution est idéale pour les ajustements rapides que vous souhaitez modifier par appel. Les paramètres `system_instruction` et `AGENTS.md` sont additifs. Les deux s'appliquent lorsqu'ils sont présents.
- **Outils** : par défaut, l'agent Antigravity a accès à `code_execution`, `google_search` et `url_context`. Vous pouvez remplacer cette liste en transmettant le paramètre `tools` au moment de l'interaction. Vous pouvez également enregistrer des [serveurs MCP distants](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr#mcp-servers) ou définir des [fonctions personnalisées (appel de fonction)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr#function-calling) pour connecter l'agent à vos propres API et bases de données. Pour obtenir des informations complètes sur les outils disponibles, consultez [Agent Antigravity : outils compatibles](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr#supported-tools).

### Personnalisation basée sur des fichiers

#### Structure du répertoire de l'agent

Bien que vous puissiez transmettre la configuration de manière intégrée, nous vous recommandons d'organiser les fichiers de votre agent dans un répertoire structuré. Cela facilite la gestion, le contrôle des versions et le montage dans l'environnement de l'agent.

Un répertoire de projet d'agent type se présente comme suit :

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

L'environnement d'exécution Antigravity analyse `.agents/` (et la racine de l'environnement) pour ces fichiers.

#### AGENTS.md

L'agent charge automatiquement `.agents/AGENTS.md` (ou `/.agents/AGENTS.md`) à partir de l'environnement en tant qu'instructions système au démarrage. Utilisez `AGENTS.md` pour les définitions de persona longues, les consignes détaillées et les instructions dont vous souhaitez contrôler les versions avec votre code.

Montez un fichier `AGENTS.md` à l'aide d'une source intégrée :

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

#### Compétences : SKILL.md

Les compétences sont des fichiers qui étendent les capacités de l'agent. Placez-les sous `.agents/skills/<skill-name>/SKILL.md`. Le harnais les détecte et les enregistre automatiquement.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Montez une compétence à l'aide d'une source intégrée :

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

Les compétences chargées à partir de `.agents/skills/` et `/.agents/skills/` sont toutes deux détectées automatiquement.

## Créer un agent géré

Une fois que vous avez itéré sur votre configuration, vous pouvez la créer en tant qu'agent géré avec `agents.create`. Cela vous permet d'appeler l'agent par ID sans répéter la configuration à chaque fois.

### À partir de sources

Spécifiez `base_agent`, `id`, `system_instruction` et `base_environment` avec des sources. La plate-forme provisionne un bac à sable frais avec vos fichiers à chaque appel. Consultez la section [Environnements](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr) pour connaître les types de sources disponibles (Git, GCS, intégrées).

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

### À partir d'un environnement existant (fork)

Itérez avec l'agent Antigravity de base jusqu'à ce que l'environnement soit correct (packages installés, fichiers en place), puis créez-en un agent géré.

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

### Avec des règles de réseau

Vous pouvez verrouiller l'accès sortant ou injecter des identifiants lorsque vous enregistrez un agent géré. Pour obtenir le schéma complet de la liste d'autorisation, les modèles d'identifiants et les caractères génériques, consultez [Environnements : configuration réseau](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#network-configuration).

L'exemple suivant crée un agent `issue-resolver` qui ne peut accéder qu'à GitHub et PyPI, avec des identifiants injectés pour GitHub :

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

## Appeler l'agent

Appelez votre agent géré avec votre ID d'agent en créant une interaction. Chaque appel crée un fork de l'environnement de base. Chaque exécution démarre donc de manière propre.

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

Pour les conversations multitours et le streaming, consultez le [guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr). Les mêmes modèles `previous_interaction_id` et `environment` s'appliquent aux agents gérés.

Les agents gérés sont également compatibles avec l'exécution en arrière-plan et l'annulation. Pour obtenir des détails et des exemples de code, consultez [Agent Antigravity : exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr#background-execution).

## Remplacer la configuration lors de l'appel

Vous pouvez remplacer les paramètres `system_instruction` et `tools` par défaut de l'agent lors de la création d'une interaction. Cela vous permet de modifier le comportement ou les capacités de l'agent pour une exécution spécifique sans modifier la définition de l'agent stockée.

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

## Gérer les agents

Vous pouvez lister, obtenir et supprimer des agents.

### Répertorier des agents

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

### Obtenir un agent

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

### Supprimer un agent

La suppression supprime la configuration. Les environnements et les interactions existants créés par l'agent ne sont pas affectés.

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

## Documentation de référence sur la définition de l'agent

| Champ | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `id` | chaîne | Oui | Identifiant unique de l'agent. Utilisé pour appeler l'agent. |
| `description` | chaîne | Non | Description de l'agent lisible par l'humain. |
| `base_agent` | chaîne | Oui | ID de l'agent de base (par exemple, `antigravity-preview-05-2026`). |
| `system_instruction` | chaîne | Non | Invite système définissant le comportement et le persona. |
| `tools` | tableau | Non | Outils que l'agent peut utiliser. Si aucune valeur n'est spécifiée, la valeur par défaut est `code_execution`, `google_search` et `url_context`. Les outils compatibles incluent `code_execution`, `google_search`, `url_context`, `mcp_server` et les définitions `function` personnalisées. |
| `base_environment` | chaîne ou objet | Non | `"remote"`, un `environment_id`, ou un objet de configuration avec `sources` et `network`. Consultez la section Environnements. |

## Workflow d'itération

1. **Prototype** avec l'agent Antigravity de base. Transmettez les sources d'instructions système et d'environnement de manière intégrée. Testez les instructions, les compétences et la configuration de l'environnement de manière interactive.
2. **Stabilisez** l'environnement. Installez des packages, montez des sources et vérifiez que tout fonctionne.
3. **Persistez** en tant qu'agent géré en créant un agent, à partir de sources ou en créant un fork de l'environnement.
4. **Mettez à jour** la définition de l'agent. Modifiez les instructions système, échangez des compétences ou ajoutez des sources. Le prochain appel récupère la nouvelle configuration.

## Limites

- **Connaître le niveau de votre entreprise** : les agents gérés sont en version preview. Les fonctionnalités et les schémas sont susceptibles de changer.
- **Agent de base** : seul `antigravity-preview-05-2026` est compatible en tant que `base_agent`.
- **Aucune gestion des versions** : la gestion des versions et la restauration des agents ne sont pas encore disponibles.
- **Aucune imbrication de sous-agents** : la délégation de sous-agents n'est pas encore compatible.
- Vous pouvez avoir jusqu'à 1 000 agents gérés.

## Étape suivante

- [Présentation des agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr) : découvrez les concepts de base des agents gérés.
- [Guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr) : commencez à créer des conversations multitours et du streaming.
- [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr) : découvrez les capacités, les outils et la tarification de l'agent par défaut.
- [Environnements d'agent](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr) : configurez des bacs à sable, des sources et des réseaux.
- [API Agents gérés sur Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=fr) : pour créer des agents avec une gouvernance organisationnelle intégrée.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/26 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/26 (UTC)."],[],[]]
