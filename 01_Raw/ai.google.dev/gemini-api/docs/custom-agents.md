---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419
fetched_at: 2026-10-12T06:56:05.063849+00:00
title: "C\u00f3mo crear agentes administrados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Cómo crear agentes administrados

Los agentes administrados en la API de Gemini te permiten extender el agente de Antigravity con tus propias instrucciones, habilidades y datos. Puedes [personalizar el agente de forma intercalada](#customize-inline) en el momento de la interacción o [guardar la configuración](#save-agent) como un agente administrado al que invocas por ID.

## Personaliza el agente de Antigravity

La forma más rápida de compilar un agente personalizado es pasar tu configuración intercalada mientras creas una interacción nueva sin necesidad de un paso de registro. Puedes extender el agente de varias maneras clave:

- **[Selección de modelo](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#model-selection)**: Elige el modelo de Gemini subyacente a través de `agent_config` (de forma predeterminada, se usa **Gemini 3.8 Flash**).
- **Instrucciones del sistema**: Pasa texto intercalado a través de `system_instruction` para dar forma al comportamiento.
- **Herramientas**: Anula las herramientas predeterminadas (ejecución de código, búsqueda, contexto de URL), registra servidores de MCP remotos o define funciones personalizadas (llamadas a funciones).
- **Archivos y habilidades**: Se montan archivos como `AGENTS.md` y `SKILL.md` en el entorno.

Aquí tienes un ejemplo de cómo pasar los tres parámetros de forma intercalada:

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

Todo se define en el momento de la interacción. No es necesario registrar nada primero. El arnés del agente de Antigravity proporciona el entorno de ejecución (ejecución de código, administración de archivos, acceso web) y tus capas de configuración en la parte superior.

### Instrucciones del sistema y herramientas

Puedes personalizar el comportamiento y las capacidades del agente para una interacción específica con los parámetros `system_instruction` y `tools`.

- **Instrucciones del sistema**: Usa el parámetro `system_instruction` para pasar texto intercalado que defina el comportamiento del agente. Esto es ideal para los ajustes rápidos que deseas cambiar por llamada. `system_instruction` y `AGENTS.md` son aditivos; ambos se aplican cuando están presentes.
- **Herramientas**: De forma predeterminada, el agente de Antigravity tiene acceso a `code_execution`, `google_search` y `url_context`. Puedes anular esta lista pasando el parámetro `tools` en el momento de la interacción. También puedes registrar [servidores de MCP remotos](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#mcp-servers) o definir [funciones personalizadas (llamadas a funciones)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#function-calling) para conectar el agente a tus propias APIs y bases de datos. Para obtener todos los detalles sobre las herramientas disponibles, consulta [Agente de Antigravity: Herramientas compatibles](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#supported-tools).

### Personalización basada en archivos

#### Estructura del directorio del agente

Si bien puedes pasar la configuración de forma intercalada, te recomendamos que organices los archivos de tu agente en un directorio estructurado. Esto facilita la administración, el control de versiones y el montaje en el entorno del agente.

Un directorio típico de proyectos de agentes se ve de la siguiente manera:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

El entorno de ejecución de Antigravity analiza `.agents/` (y la raíz del entorno) en busca de estos archivos.

#### AGENTS.md

El agente carga automáticamente `.agents/AGENTS.md` (o `/.agents/AGENTS.md`) desde el entorno como instrucciones del sistema al inicio. Usa `AGENTS.md` para definiciones de arquetipos de formato largo, instrucciones detalladas y pautas que quieras controlar por versión junto con tu código.

Cómo unir un `AGENTS.md` con una fuente intercalada:

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

#### Habilidades: SKILL.md

Las habilidades son archivos que amplían las capacidades del agente. Colócalos debajo del `.agents/skills/<skill-name>/SKILL.md`, y el arnés los detectará y registrará automáticamente.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Activa una skill con una fuente intercalada:

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

Las habilidades cargadas desde `.agents/skills/` y `/.agents/skills/` se descubren automáticamente.

## Crea un agente administrado

Una vez que hayas iterado en tu configuración, puedes crearla como un agente administrado con `agents.create`. Esto te permite invocar el agente por ID sin repetir la configuración cada vez.

El `id` que especifiques cuando crees un agente administrado debe ser único para tu proyecto y no debe comenzar con prefijos reservados (p.ej., `google-`, `gemini-`). Consulta las [restricciones del ID del agente](#agent-id-restrictions) para ver la lista completa de prefijos restringidos.

### De fuentes

Especifica `base_agent`, `id`, `agent_config`, `system_instruction` y `base_environment` con fuentes. La plataforma aprovisiona un entorno de pruebas nuevo con tus archivos en cada invocación. Consulta [Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419) para ver los tipos de fuentes disponibles (Git, GCS, intercalado).

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

### Desde un entorno existente (fork)

Itera con el agente de Antigravity base hasta que el entorno sea el adecuado (paquetes instalados, archivos en su lugar) y, luego, crea una bifurcación en un agente administrado.

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

### Con reglas de red

Puedes bloquear el acceso saliente o insertar credenciales cuando guardas un agente administrado. Para ver el esquema completo de la lista de entidades permitidas, los patrones de credenciales y los comodines, consulta [Entornos: Configuración de red](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#network-configuration).

Haz referencia a una [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) almacenada por ID en una regla de lista de entidades permitidas (`"credential": "github-production"`), y el proxy de salida inserta el secreto en el momento de la solicitud, por lo que nunca llega a la definición de tu agente. En este ejemplo, se establece el encabezado intercalado con `transform`. El proxy aplica ambas formas de la misma manera, y una credencial también te permite reutilizar el secreto en todos los agentes y rotarlo en un solo lugar.

En el siguiente ejemplo, se crea un agente `issue-resolver` que solo puede acceder a GitHub y PyPI, con credenciales insertadas para GitHub:

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

## Invoca el agente

Crea una interacción nueva para llamar a tu agente administrado con tu ID de agente. Cada invocación bifurca el entorno base, por lo que cada ejecución comienza de forma limpia.

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

Para conversaciones de varios turnos y transmisión, consulta la [guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419). Los mismos patrones de `previous_interaction_id` y `environment` se aplican a los agentes administrados.

Los agentes administrados también admiten la ejecución en segundo plano y la cancelación. Para obtener detalles y ejemplos de código, consulta [Agente de Antigravity: Ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#background-execution).

## Anulación de la configuración en la invocación

Puedes anular la configuración de red predeterminada `system_instruction`, `tools` y `environment` del agente cuando crees una interacción. Esto te permite modificar el comportamiento, las capacidades o las credenciales del agente para una ejecución específica sin cambiar la definición almacenada del agente.

### Anula las instrucciones y herramientas del sistema

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

### Anula la configuración de red (actualiza las credenciales)

Si tu agente administrado tiene credenciales de red integradas en su `base_environment`, puedes anularlas en el momento de la invocación para actualizar los tokens vencidos o rotar las claves de API. Pasa un objeto `environment` con una nueva configuración de `network`. Las nuevas reglas de red reemplazan por completo las anteriores para esa interacción. Se conservan las fuentes (archivos, repositorios) del entorno base.

Si el objeto `base_environment` hace referencia a una [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) almacenada en lugar de un token intercalado, no es necesario que anules nada. Rota la credencial con un `PATCH` y cada agente que la referencia recupera el nuevo secreto en la próxima ejecución.

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

## Administrar los agentes

Puedes enumerar, obtener y borrar agentes.

### Mostrar lista de agentes

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

### Obtén un agente

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

### Borra un agente

Si borras la configuración, se quitará. Los entornos y las interacciones existentes creados por el agente no se ven afectados.

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

## Referencia de la definición del agente

| Campo | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `id` | string | Sí | Es el identificador único del agente dentro del proyecto de Google Cloud. Se usa para invocar al agente. No debe usar prefijos reservados. Consulta las [restricciones del ID de agente](#agent-id-restrictions). |
| `description` | string | No | Es una descripción del agente legible por humanos. |
| `base_agent` | string | Sí | Es el ID del agente base (p.ej., `antigravity-preview-09-2026`). |
| `agent_config` | objeto | No | Es la configuración del agente base, incluida la selección del modelo (`{"type": "antigravity", "model": "gemini-3.8-flash"}`). El valor predeterminado es `gemini-3.8-flash` si se omite. No se puede anular en el momento de la interacción para los agentes con nombre. |
| `system_instruction` | string | No | Es la instrucción del sistema que define el comportamiento y la personificación. |
| `tools` | array | No | Son las herramientas que el agente puede usar. Si se omite, el valor predeterminado es `code_execution`, `google_search` y `url_context`. Las herramientas admitidas incluyen `code_execution`, `google_search`, `url_context`, `mcp_server` y definiciones personalizadas de `function`. |
| `base_environment` | cadena o objeto | No | `"remote"`, un `environment_id` o un objeto de configuración con `sources` y `network`. Consulta la sección sobre entornos. |

### Restricciones del ID del agente

Cuando crees un agente administrado, el `id` que especifiques debe cumplir con las siguientes reglas:

- Debe ser único para tu proyecto de Google Cloud.
- **No** debe comenzar con ninguno de los siguientes prefijos reservados (no distingue mayúsculas de minúsculas); de lo contrario, fallará la creación:
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

## Flujo de trabajo de iteración

1. **Prototipa** con el agente de Antigravity base. Pasa la instrucción del sistema y las fuentes del entorno de forma intercalada. Probar instrucciones, habilidades y configuración del entorno de forma interactiva
2. **Estabiliza** el entorno. Instala paquetes, conecta fuentes y verifica que todo funcione.
3. **Persiste** como un agente administrado creando un agente nuevo, ya sea a partir de fuentes o bifurcando el entorno.
4. **Actualiza** la definición del agente. Cambiar la instrucción del sistema, intercambiar habilidades o agregar fuentes La siguiente invocación recupera la configuración nueva.

## Limitaciones

- **Estado de vista previa**: Los agentes administrados están en versión preliminar. Las funciones y los esquemas pueden cambiar.
- **Agente y modelos básicos**: Solo se admite `antigravity-preview-09-2026` como `base_agent`. Las opciones de modelos admitidas en `agent_config` son `gemini-3.8-flash` (predeterminado), `gemini-3.6-flash` y `gemini-3.5-flash-lite`. En el caso de los agentes con nombre, el modelo no se puede anular en el momento de la interacción.
- **Sin control de versiones**: El control de versiones y la reversión del agente aún no están disponibles.
- **No se admite la anidación de subagentes**: Aún no se admite la delegación de subagentes.
- Puedes tener hasta 1,000 agentes administrados.

## ¿Qué sigue?

- [Descripción general de los agentes](https://ai.google.dev/gemini-api/docs/agents?hl=es-419): Obtén información sobre los conceptos básicos de los agentes administrados.
- [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419): Comienza a compilar con conversaciones de varios turnos y transmisión.
- [Agente de antigravedad](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419): Explora las capacidades, las herramientas y los precios del agente predeterminado.
- [Entornos de agentes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419): Configura zonas de pruebas, fuentes y redes.
- [API de Managed Agents en Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=es-419): Para crear agentes con administración organizacional integrada.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-09 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-09 (UTC)"],[],[]]
