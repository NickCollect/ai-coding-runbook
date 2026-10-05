---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=it
fetched_at: 2026-10-05T06:40:42.567553+00:00
title: "Creazione di agenti gestiti \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Creazione di agenti gestiti

Gli agenti gestiti nell'API Gemini ti consentono di estendere l'agente Antigravity con istruzioni, competenze e dati personalizzati. Puoi [personalizzare l'agente inline](#customize-inline) al momento dell'interazione oppure [salvare la configurazione](#save-agent) come agente gestito che richiami per ID.

## Personalizzare l'agente Antigravity

Il modo più rapido per creare un agente personalizzato è passare la configurazione in linea durante la creazione di una nuova interazione senza la necessità di un passaggio di registrazione. Puoi estendere l'agente in diversi modi chiave:

- **[Selezione del modello](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#model-selection)**: scegli il modello Gemini sottostante tramite `agent_config` (il valore predefinito è **Gemini 3.8 Flash**).
- **Istruzioni di sistema**: passa il testo in linea tramite `system_instruction` per definire il comportamento.
- **Strumenti**: esegui l'override degli strumenti predefiniti (esecuzione di codice, ricerca, contesto URL), registra server MCP remoti o definisci funzioni personalizzate (chiamata di funzioni).
- **File e skill**: monta file come `AGENTS.md` e `SKILL.md` nell'ambiente.

Ecco un esempio di passaggio di tutti e tre i parametri in linea:

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

### Java

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

Tutto viene definito al momento dell'interazione. Non è necessario registrare nulla. L'agente Antigravity fornisce il runtime (esecuzione del codice, gestione dei file, accesso web) e i livelli di configurazione.

### Strumenti e istruzioni di sistema

Puoi personalizzare il comportamento e le funzionalità dell'agente per un'interazione specifica utilizzando i parametri `system_instruction` e `tools`.

- **Istruzioni di sistema**: utilizza il parametro `system_instruction` per passare il testo in linea che modella il comportamento dell'agente. Questa opzione è ideale per le modifiche rapide che vuoi apportare per ogni chiamata. `system_instruction` e `AGENTS.md` sono additivi; entrambi si applicano quando sono presenti.
- **Strumenti**: per impostazione predefinita, l'agente Antigravity ha accesso a `code_execution`, `google_search` e `url_context`. Puoi ignorare questo elenco passando il parametro `tools` al momento dell'interazione. Puoi anche registrare [server MCP remoti](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#mcp-servers) o definire [funzioni personalizzate (chiamata di funzioni)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#function-calling) per connettere l'agente alle tue API e ai tuoi database. Per informazioni dettagliate sugli strumenti disponibili, vedi [Antigravity Agent: strumenti supportati](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#supported-tools).

### Personalizzazione basata su file

#### Struttura delle directory dell'agente

Anche se puoi passare la configurazione inline, ti consigliamo di organizzare i file dell'agente in una directory strutturata. In questo modo è più facile gestire, controllare la versione e montare l'ambiente dell'agente.

Una tipica directory di progetto dell'agente ha questo aspetto:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Il runtime Antigravity esegue la scansione di `.agents/` (e della radice dell'ambiente) per questi file.

#### AGENTS.md

All'avvio, l'agente carica automaticamente `.agents/AGENTS.md` (o `/.agents/AGENTS.md`) dall'ambiente come istruzioni di sistema. Utilizza `AGENTS.md` per definizioni di persona in formato lungo, linee guida dettagliate e istruzioni di cui vuoi controllare la versione insieme al codice.

Monta un `AGENTS.md` utilizzando un'origine in linea:

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

### Java

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

#### Skills: SKILL.md

Le skill sono file che estendono le funzionalità dell'agente. Posizionali sotto `.agents/skills/<skill-name>/SKILL.md` e il cablaggio li rileva e li registra automaticamente.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Monta una skill utilizzando un'origine in linea:

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

### Java

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

Le competenze caricate da `.agents/skills/` e `/.agents/skills/` vengono rilevate automaticamente.

## Crea un agente gestito

Una volta perfezionata la configurazione, puoi crearla come agente gestito con `agents.create`. In questo modo puoi richiamare l'agente per ID senza ripetere la configurazione ogni volta.

Il `id` che specifichi quando crei un agente gestito deve essere univoco per il tuo progetto e non deve iniziare con prefissi riservati (ad es. `google-`, `gemini-`). Per l'elenco completo dei prefissi con limitazioni, consulta [Limitazioni dell'ID agente](#agent-id-restrictions).

### Dalle fonti

Specifica `base_agent`, `id`, `agent_config`, `system_instruction` e `base_environment` con le fonti. La piattaforma esegue il provisioning di una nuova sandbox con i tuoi file a ogni chiamata. Consulta la sezione [Ambienti](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it) per i tipi di origine disponibili (Git, GCS, inline).

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

### Java

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

### Da un ambiente esistente (fork)

Esegui l'iterazione con l'agente Antigravity di base finché l'ambiente non è corretto (pacchetti installati, file in posizione), quindi esegui il fork in un agente gestito.

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

### Java

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

### Con regole di rete

Puoi bloccare l'accesso in uscita o inserire le credenziali quando salvi un agente gestito. Per lo schema completo della lista consentita, i pattern delle credenziali e i caratteri jolly, vedi [Ambienti: configurazione di rete](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#network-configuration).

Fai riferimento a una [credenziale](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=it) archiviata per ID in una regola della lista consentita (`"credential": "github-production"`) e il proxy di uscita inserisce il secret al momento della richiesta, in modo che non venga mai inserito nella definizione dell'agente. Questo esempio imposta l'intestazione in linea con `transform`. Il proxy applica entrambi i moduli allo stesso modo. Una credenziale ti consente inoltre di riutilizzare il secret tra gli agenti e di ruotarlo in un'unica posizione.

L'esempio seguente crea un agente `issue-resolver` che può accedere solo a GitHub e PyPI, con le credenziali inserite per GitHub:

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

### Java

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
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            ))
            .build()
    )))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Basic YOUR_BASE64_TOKEN",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
            },
        }))),
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

## Richiamare l'agente

Chiama il tuo agente gestito con il tuo ID agente creando una nuova interazione. Ogni invocazione esegue il fork dell'ambiente di base, quindi ogni esecuzione inizia da zero.

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

### Java

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

Per conversazioni e streaming multi-turno, consulta la [guida rapida](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it). Gli stessi pattern `previous_interaction_id` e `environment` si applicano agli agenti gestiti.

Gli agenti gestiti supportano anche l'esecuzione e l'annullamento in background. Per dettagli ed esempi di codice, vedi [Antigravity Agent: Background execution](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#background-execution).

## Override della configurazione durante la chiamata

Puoi eseguire l'override della configurazione di rete predefinita `system_instruction`, `tools` e `environment` dell'agente quando crei un'interazione. In questo modo
puoi modificare il comportamento, le funzionalità o le credenziali dell'agente per una
esecuzione specifica senza modificare la definizione dell'agente archiviata.

### Eseguire l'override delle istruzioni di sistema e degli strumenti

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

### Java

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

### Ignora la configurazione di rete (aggiorna le credenziali)

Se il tuo agente gestito ha credenziali di rete integrate nel suo `base_environment`,
puoi eseguirne l'override al momento della chiamata per aggiornare i token scaduti o ruotare le chiavi API. Passa un oggetto `environment` con una nuova configurazione `network`. Le nuove regole di rete sostituiscono completamente quelle precedenti per l'interazione. Le origini (file, repository) dell'ambiente base vengono conservate.

Se `base_environment` fa riferimento a una
[credenziale](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=it) archiviata anziché a un token incorporato, non
devi eseguire l'override di nulla. Ruota la credenziale con un `PATCH` e ogni
agente che la fa riferimento preleva il nuovo secret alla successiva esecuzione.

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

### Java

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
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_REFRESHED_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            ))
            .build()
    )))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
            },
        }))),
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

## Gestisci agenti

Puoi elencare, ottenere ed eliminare gli agenti.

### Elenca agenti

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

### Java

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

### Trovare un agente

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

### Java

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

### Eliminare un agente

L'eliminazione rimuove la configurazione. Gli ambienti e le interazioni esistenti creati dall'agente non sono interessati.

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### Java

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

## Riferimento alla definizione dell'agente

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `id` | stringa | Sì | Identificatore univoco dell'agente all'interno del progetto Google Cloud. Utilizzato per richiamare l'agente. Non deve utilizzare prefissi riservati. Consulta [Limitazioni dell'ID agente](#agent-id-restrictions). |
| `description` | stringa | No | Descrizione dell'agente leggibile. |
| `base_agent` | stringa | Sì | ID agente base (ad es. `antigravity-preview-09-2026`). |
| `agent_config` | oggetto | No | Configurazione dell'agente di base, inclusa la selezione del modello (`{"type": "antigravity", "model": "gemini-3.8-flash"}`). Il valore predefinito è `gemini-3.8-flash` se omesso. Non può essere sostituito al momento dell'interazione per gli agenti denominati. |
| `system_instruction` | stringa | No | Prompt di sistema che definisce il comportamento e la personalità. |
| `tools` | matrice | No | Strumenti che l'agente può utilizzare. Se omesso, il valore predefinito è `code_execution`, `google_search` e `url_context`. Gli strumenti supportati includono `code_execution`, `google_search`, `url_context`, `mcp_server` e definizioni personalizzate di `function`. |
| `base_environment` | stringa o oggetto | No | `"remote"`, un `environment_id` o un oggetto di configurazione con `sources` e `network`. Consulta Ambienti. |

### Limitazioni relative all'ID agente

Quando crei un agente gestito, il `id` che specifichi deve rispettare queste regole:

- Deve essere univoco per il tuo progetto Google Cloud.
- **Non** deve iniziare con uno dei seguenti prefissi riservati (senza distinzione tra maiuscole e minuscole), altrimenti la creazione non andrà a buon fine:
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

## Workflow di iterazione

1. **Prototipo** con l'agente Antigravity di base. Trasmetti l'istruzione di sistema e le fonti dell'ambiente in linea. Testa in modo interattivo le istruzioni, le competenze e la configurazione dell'ambiente.
2. **Stabilizza** l'ambiente. Installa i pacchetti, monta le origini e verifica che tutto funzioni.
3. **Mantieni** l'agente gestito creando un nuovo agente, dalle origini o eseguendo il fork dell'ambiente.
4. **Aggiorna** la definizione dell'agente. Modifica l'istruzione di sistema, scambia le competenze o aggiungi fonti. La chiamata successiva rileva la nuova configurazione.

## Limitazioni

- **Stato dell'anteprima**: gli agenti gestiti sono in anteprima. Le funzionalità e gli schemi potrebbero cambiare.
- **Agente e modelli di base**: è supportato solo `antigravity-preview-09-2026` come `base_agent`. Le opzioni di modello supportate in `agent_config` sono `gemini-3.8-flash` (predefinita), `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash` e `gemini-3.5-flash-lite`. Per gli agenti denominati, il modello non può essere sostituito al momento dell'interazione.
- **Nessun controllo delle versioni**: il controllo delle versioni e il rollback dell'agente non sono ancora disponibili.
- **Nessuna nidificazione di subagenti**: la delega di subagenti non è ancora supportata.
- Puoi avere fino a 1000 agenti gestiti.

## Passaggi successivi

- [Panoramica degli agenti](https://ai.google.dev/gemini-api/docs/agents?hl=it): scopri i concetti fondamentali degli agenti gestiti.
- [Guida rapida](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it): inizia a creare con conversazioni multi-turno e streaming.
- [Agente antigravità](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it): esplora funzionalità, strumenti e prezzi dell'agente predefinito.
- [Agent Environments](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it): configura sandbox, origini e networking.
- [API Managed Agents su Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=it): per creare agenti con governance organizzativa integrata.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-24 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-24 UTC."],[],[]]
