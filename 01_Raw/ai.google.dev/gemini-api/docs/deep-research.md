---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=fr
fetched_at: 2026-10-26T05:50:07.695266+00:00
title: "Agent Gemini Deep\u00a0Research \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Agent Gemini Deep Research

L'agent Gemini Deep Research planifie, exécute et synthétise de manière autonome des tâches de recherche en plusieurs étapes. Grâce à Gemini, il explore des ensembles d'informations complexes pour produire des rapports détaillés et cités. De nouvelles fonctionnalités vous permettent de planifier des tâches de manière collaborative avec l'agent, de vous connecter à des outils externes à l'aide de serveurs MCP, d'inclure des visualisations (comme des graphiques) et de fournir des documents directement en entrée.

Les tâches de recherche impliquent des recherches et des lectures itératives, et peuvent prendre plusieurs minutes. Vous devez utiliser l'[exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr) (définir `background=true`) pour exécuter l'agent de manière asynchrone et interroger les résultats ou diffuser les mises à jour. Pour en savoir plus, consultez [Gérer les tâches de longue durée](#long-running-tasks).

L'exemple suivant montre comment démarrer une tâche de recherche en arrière-plan et interroger les résultats.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the history of Google TPUs."))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

while (true) {
  interaction =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(interaction.status().orElse(null))) {
    System.out.println(interaction.outputText().orElse(""));
    break;
  } else if (InteractionStatus.FAILED.equals(interaction.status().orElse(null))) {
    System.out.println("Research failed: " + interaction.errors().orElse(Collections.emptyList()));
    break;
  }
  Thread.sleep(10000);
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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
            Agent:      interactions.AgentOption("deep-research-preview-04-2026"),
            Input:      interactions.NewInteractionsInput("Research the history of Google TPUs."),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction
    if interaction.ID != nil {
        fmt.Printf("Research started: %s\n", *interaction.ID)
    }

    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
        if interaction.Status == interactions.InteractionStatusCompleted {
            if interaction.OutputText != nil {
                fmt.Println(*interaction.OutputText)
            }
            break
        } else if interaction.Status == interactions.InteractionStatusFailed {
            fmt.Printf("Research failed: %v\n", interaction.Errors)
            break
        }
        time.Sleep(10 * time.Second)
    }
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Versions compatibles

L'agent Deep Research est disponible en deux versions :

- **Deep Research** (`deep-research-preview-04-2026`) : conçu pour la rapidité et l'efficacité, idéal pour être diffusé en streaming vers une UI client.
- **Deep Research Max** (`deep-research-max-preview-04-2026`) : exhaustivité maximale pour la collecte et la synthèse automatisées de contexte.

## Planification collaborative

La planification collaborative vous permet de contrôler l'orientation de la recherche avant que l'agent ne commence son travail. Vous pouvez ainsi examiner et affiner le plan de recherche avant son exécution. Lorsqu'il est activé, l'agent renvoie un plan de recherche proposé au lieu de l'exécuter immédiatement. Vous pouvez ensuite examiner, modifier ou approuver le plan grâce à des interactions multitours.

### Étape 1 : Demandez un forfait

Définissez `collaborative_planning=True` dans la première interaction. L'agent renvoie un plan de recherche au lieu d'un rapport complet.

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// First interaction: request a research plan
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Do some research on Google TPUs."))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(true)
                .build())
        .background(true)
        .build();

Interaction planInteraction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Wait for and retrieve the plan
Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(planInteraction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(true),
    })

    // First interaction: request a research plan
    planRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Do some research on Google TPUs."),
            AgentConfig: &agentCfg,
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Wait for and retrieve the plan
    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *planRes.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }
    if result.OutputText != nil {
        fmt.Println(*result.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### Étape 2 : Affiner le plan (facultatif)

Utilisez `previous_interaction_id` pour poursuivre la conversation et affiner le plan. Conservez `collaborative_planning=True` pour rester en mode planification.

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();
String planInteractionId = "PLAN_INTERACTION_ID";

// Second interaction: refine the plan
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Focus more on the differences between Google TPUs and competitor hardware, and less on the history."))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(true)
                .build())
        .previousInteractionId(planInteractionId)
        .background(true)
        .build();

Interaction refinedPlan =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(refinedPlan.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    planInteractionID := "PLAN_INTERACTION_ID"
    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(true),
    })

    // Second interaction: refine the plan
    refinedRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("deep-research-preview-04-2026"),
            Input:                 interactions.NewInteractionsInput("Focus more on the differences between Google TPUs and competitor hardware, and less on the history."),
            AgentConfig:           &agentCfg,
            PreviousInteractionID: genai.Ptr(planInteractionID),
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *refinedRes.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }
    if result.OutputText != nil {
        fmt.Println(*result.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### Étape 3 : Approuver et exécuter

Définissez la valeur sur `collaborative_planning=False` (ou omettez-la) pour approuver le plan et lancer la recherche.

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();
String refinedPlanId = "REFINED_PLAN_ID";

// Third interaction: approve the plan and kick off research
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Plan looks good!"))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(false)
                .build())
        .previousInteractionId(refinedPlanId)
        .background(true)
        .build();

Interaction finalReport =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(finalReport.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    refinedPlanID := "REFINED_PLAN_ID"
    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(false),
    })

    // Third interaction: approve the plan and kick off research
    finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("deep-research-preview-04-2026"),
            Input:                 interactions.NewInteractionsInput("Plan looks good!"),
            AgentConfig:           &agentCfg,
            PreviousInteractionID: genai.Ptr(refinedPlanID),
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *finalRes.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }
    if result.OutputText != nil {
        fmt.Println(*result.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Visualisation

Lorsque `visualization` est défini sur `"auto"`, l'agent peut générer des graphiques, des diagrammes et d'autres éléments visuels pour étayer ses résultats de recherche.
Les images générées sont incluses dans les étapes de la réponse et diffusées en streaming sous forme de deltas `image`. Pour obtenir les meilleurs résultats, demandez explicitement des éléments visuels dans votre requête. Par exemple, "Inclure des graphiques montrant les tendances au fil du temps" ou "Générer des graphiques comparant les parts de marché". Si vous définissez `visualization` sur `"auto"`, la fonctionnalité est activée, mais l'agent ne génère des éléments visuels que lorsque la requête le demande.

### Python

```
import base64
import time

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.Visualization;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Analyze global semiconductor market trends. Include graphics showing market share changes."))
        .agentConfig(DeepResearchAgentConfig.builder().visualization(Visualization.AUTO).build())
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}

for (Step step : result.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    for (Content contentItem : ((ModelOutputStep) step).content().orElse(Collections.emptyList())) {
      if (contentItem instanceof TextContent) {
        System.out.println(((TextContent) contentItem).text().orElse(""));
      } else if (contentItem instanceof ImageContent) {
        ImageContent img = (ImageContent) contentItem;
        if (img.data().isPresent()) {
          byte[] imageBytes = Base64.getDecoder().decode(img.data().get());
          System.out.println("Received image: " + imageBytes.length + " bytes");
        }
      }
    }
  }
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "time"

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

    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        Visualization: interactions.VisualizationAuto.ToPointer(),
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Analyze global semiconductor market trends. Include graphics showing market share changes."),
            AgentConfig: &agentCfg,
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.ID != nil {
        fmt.Printf("Research started: %s\n", *res.Interaction.ID)
    }

    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *res.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }

    for _, step := range result.Steps {
        if outStep := step.ModelOutputStep; outStep != nil {
            for _, contentItem := range outStep.Content {
                if textContent := contentItem.TextContent; textContent != nil {
                    fmt.Println(textContent.GetText())
                } else if imgContent := contentItem.ImageContent; imgContent != nil && imgContent.Data != nil {
                    imageBytes, err := base64.StdEncoding.DecodeString(*imgContent.Data)
                    if err == nil {
                        fmt.Printf("Received image: %d bytes\n", len(imageBytes))
                    }
                }
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## Outils compatibles

Deep Research est compatible avec plusieurs outils intégrés et externes. Par défaut (lorsqu'aucun paramètre `tools` n'est fourni), l'agent a accès à la recherche Google, au contexte de l'URL et à l'exécution de code. Vous pouvez spécifier explicitement des outils pour limiter ou étendre les capacités de l'agent.

| Outil | Valeur du type | Description |
| --- | --- | --- |
| Recherche Google | `google_search` | Rechercher sur le Web public Cette option est activée par défaut. |
| Contexte de l'URL | `url_context` | lire et résumer le contenu d'une page Web ; Cette option est activée par défaut. |
| Exécution du code | `code_execution` | Exécuter du code pour effectuer des calculs et analyser des données Cette option est activée par défaut. |
| Serveur MCP | `mcp_server` | Se connecter à des serveurs MCP distants pour accéder à des outils externes |
| Recherche de fichiers | `file_search` | Recherchez dans les corpus de documents que vous avez importés. |

### Recherche Google

Activez explicitement la recherche Google comme seul outil :

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("What are the latest developments in quantum computing?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("What are the latest developments in quantum computing?"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### Contexte de l'URL

Donnez à l'agent la possibilité de lire et de résumer des pages Web spécifiques :

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Summarize the content of https://www.wikipedia.org/."))
        .tools(Arrays.asList(URLContext.builder().build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Summarize the content of https://www.wikipedia.org/."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### Exécution du code

Autorisez l'agent à exécuter du code pour effectuer des calculs et analyser des données :

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Calculate the 50th Fibonacci number."))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Calculate the 50th Fibonacci number."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### Serveurs MCP

Connectez-vous à des serveurs MCP distants pour donner à l'agent l'accès à des outils et services externes.

Indiquez les `name` et `url` du serveur dans la configuration des outils. Vous pouvez également transmettre des identifiants d'authentification et limiter les outils que l'agent peut appeler.

| Champ | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `type` | `string` | Oui | doit être `"mcp_server"` |
| `name` | `string` | Non | Nom à afficher du serveur MCP. |
| `url` | `string` | Non | URL complète du point de terminaison du serveur MCP. |
| `headers` | `object` | Non | Paires clé-valeur envoyées en tant qu'en-têtes HTTP avec chaque requête au serveur (par exemple, jetons d'authentification). |
| `allowed_tools` | `array` | Non | Limitez les outils du serveur que l'agent peut appeler. |

#### Utilisation de base

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.MCPServer;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Check the status of my last server deployment."))
        .tools(
            Arrays.asList(
                MCPServer.builder()
                    .name("Deployment Tracker")
                    .url("https://mcp.example.com/mcp")
                    .headers(Collections.singletonMap("Authorization", "Bearer my-token"))
                    .build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Check the status of my last server deployment."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("Deployment Tracker"),
                    URL:  genai.Ptr("https://mcp.example.com/mcp"),
                    Headers: map[string]string{
                        "Authorization": "Bearer my-token",
                    },
                }),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### Recherche de fichiers

Donnez à l'agent l'accès à vos propres données à l'aide de l'outil [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Compare our 2025 fiscal year report against current public web news."))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/my-store-name"))
                    .build()))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Compare our 2025 fiscal year report against current public web news."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.FileSearch{
                    FileSearchStoreNames: []string{"fileSearchStores/my-store-name"},
                }),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## Orientation et mise en forme

Vous pouvez orienter la sortie de l'agent en fournissant des instructions de mise en forme spécifiques dans votre requête. Cela vous permet de structurer les rapports en sections et sous-sections spécifiques, d'inclure des tableaux de données ou d'adapter le ton à différentes audiences (par exemple, "technique", "exécutif" ou "informel").

Définissez explicitement le format de sortie souhaité dans votre texte d'entrée.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "Research the competitive landscape of EV batteries.\n\n"
        + "Format the output as a technical report with the following structure:\n"
        + "1. Executive Summary\n"
        + "2. Key Players (Must include a data table comparing capacity and chemistry)\n"
        + "3. Supply Chain Risks";

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of(prompt))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    prompt := "Research the competitive landscape of EV batteries.\n\n" +
        "Format the output as a technical report with the following structure:\n" +
        "1. Executive Summary\n" +
        "2. Key Players (Must include a data table comparing capacity and chemistry)\n" +
        "3. Supply Chain Risks"

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:      interactions.AgentOption("deep-research-preview-04-2026"),
            Input:      interactions.NewInteractionsInput(prompt),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## Entrées multimodales

Deep Research est compatible avec les entrées multimodales, y compris les images et les documents (PDF), ce qui permet à l'agent d'analyser le contenu visuel et d'effectuer des recherches sur le Web contextualisées par les entrées fournies.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

String prompt =
    "Analyze the interspecies dynamics and behavioral risks present "
        + "in the provided image of the African watering hole. Specifically, investigate "
        + "the symbiotic relationship between the avian species and the pachyderms "
        + "shown, and conduct a risk assessment for the reticulated giraffes based on "
        + "their drinking posture relative to the specific predator visible in the "
        + "foreground.";

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text(prompt).build(),
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .uri(
                            "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg")
                        .build())))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

while (true) {
  interaction =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(interaction.status().orElse(null))) {
    System.out.println(interaction.outputText().orElse(""));
    break;
  } else if (InteractionStatus.FAILED.equals(interaction.status().orElse(null))) {
    System.out.println("Research failed: " + interaction.errors().orElse(Collections.emptyList()));
    break;
  }
  Thread.sleep(10000);
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    prompt := "Analyze the interspecies dynamics and behavioral risks present " +
        "in the provided image of the African watering hole. Specifically, investigate " +
        "the symbiotic relationship between the avian species and the pachyderms " +
        "shown, and conduct a risk assessment for the reticulated giraffes based on " +
        "their drinking posture relative to the specific predator visible in the " +
        "foreground."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{Text: prompt}),
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    URI:      genai.Ptr("https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"),
                }),
            }),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction
    if interaction.ID != nil {
        fmt.Printf("Research started: %s\n", *interaction.ID)
    }

    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
        if interaction.Status == interactions.InteractionStatusCompleted {
            if interaction.OutputText != nil {
                fmt.Println(*interaction.OutputText)
            }
            break
        } else if interaction.Status == interactions.InteractionStatusFailed {
            fmt.Printf("Research failed: %v\n", interaction.Errors)
            break
        }
        time.Sleep(10 * time.Second)
    }
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Compréhension des documents

La compréhension des documents permet de transmettre directement des documents en tant qu'entrée multimodale.
L'agent analyse les documents fournis et effectue des recherches basées sur leur contenu.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("What is this document about?").build(),
                    DocumentContent.builder()
                        .uri("https://arxiv.org/pdf/1706.03762")
                        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
                        .build())))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{Text: "What is this document about?"}),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr("https://arxiv.org/pdf/1706.03762"),
                    MimeType: interactions.DocumentContentMimeType("application/pdf").ToPointer(),
                }),
            }),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## Gérer les tâches de longue durée

Deep Research est un processus en plusieurs étapes qui comprend la planification, la recherche, la lecture et l'écriture. Ce cycle dépasse généralement les limites de délai standards des appels d'API synchrones.

Les agents sont tenus d'utiliser `background=True`. L'API renvoie immédiatement un objet `Interaction` partiel. Vous pouvez utiliser la propriété `id` pour récupérer une interaction pour le polling. L'état de l'interaction passera de `in_progress` à `completed` ou `failed`. Pour obtenir un guide complet sur la gestion des tâches en arrière-plan, consultez [Exécution en arrière-plan](https://ai.google.dev/gemini-api/docs/background-execution?hl=fr).

### Streaming

Deep Research prend en charge le streaming pour recevoir des informations en temps réel sur l'avancement de la recherche, y compris des résumés de réflexion, des résultats textuels et des images générées.
Vous devez définir `stream=True` et `background=True`.

Pour recevoir des étapes de raisonnement intermédiaires (pensées) et des mises à jour sur la progression, vous devez activer les **résumés de réflexion** en définissant `thinking_summaries` sur `"auto"` dans `agent_config`. Sans cela, le flux ne peut fournir que les résultats finaux.

#### Types d'événements de flux

| Type d'événement | Type de delta | Description |
| --- | --- | --- |
| `step.delta` | `thought` | Étape de raisonnement intermédiaire de l'agent. |
| `step.delta` | `text` | Partie du texte de sortie final. |
| `step.delta` | `image` | Image générée (encodée en base64). |

L'exemple suivant lance une tâche de recherche et traite le flux avec une reconnexion automatique. Il suit les `interaction_id` et `last_event_id` afin de pouvoir reprendre là où il s'est arrêté en cas de perte de connexion (par exemple, après le délai d'expiration de 600 secondes).

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "interaction.error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'interaction.error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.ErrorEvent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionCreatedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.utils.EventStream;

class StreamProcessor {
  String interactionId = null;
  String lastEventId = null;
  boolean isComplete = false;

  void processStream(EventStream<InteractionSSEStreamEvent> stream) {
    for (InteractionSSEStreamEvent streamEvent : stream) {
      InteractionSSEEvent event = streamEvent.data().orElse(null);
      if (event instanceof InteractionCreatedEvent) {
        InteractionCreatedEvent created = (InteractionCreatedEvent) event;
        interactionId = created.interaction().flatMap(i -> i.id()).orElse(null);
        if (created.eventId().isPresent()) {
          lastEventId = created.eventId().get();
        }
      } else if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.eventId().isPresent()) {
          lastEventId = stepDelta.eventId().get();
        }
        if (stepDelta.delta().isPresent()) {
          if (stepDelta.delta().get() instanceof TextDelta) {
            System.out.print(((TextDelta) stepDelta.delta().get()).text().orElse(""));
            System.out.flush();
          } else if (stepDelta.delta().get() instanceof ThoughtSummaryDelta) {
            ThoughtSummaryDelta thought = (ThoughtSummaryDelta) stepDelta.delta().get();
            Content content = thought.content().orElse(null);
            if (content instanceof TextContent) {
              System.out.println("Thought: " + ((TextContent) content).text().orElse(""));
            }
          }
        }
      } else if (event instanceof InteractionCompletedEvent || event instanceof ErrorEvent) {
        isComplete = true;
      }
    }
  }
}

Client client = new Client();
StreamProcessor processor = new StreamProcessor();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the history of Google TPUs."))
        .background(true)
        .stream(true)
        .agentConfig(
            DeepResearchAgentConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(params)).events()) {
  processor.processStream(stream);
}

// Reconnect if the connection drops
while (!processor.isComplete && processor.interactionId != null) {
  Interaction status =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(processor.interactionId).build())
          .interaction()
          .get();
  if (!InteractionStatus.IN_PROGRESS.equals(status.status().orElse(null))) {
    break;
  }
  try (EventStream<InteractionSSEStreamEvent> stream =
      client.interactions
          .get(
              GetInteractionByIdRequest.builder()
                  .id(processor.interactionId)
                  .stream(true)
                  .lastEventId(processor.lastEventId)
                  .build())
          .events()) {
    processor.processStream(stream);
  }
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
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/types/stream"
)

type StreamProcessor struct {
    interactionID string
    lastEventID   *string
    isComplete    bool
}

func (p *StreamProcessor) processStream(s *stream.EventStream[interactions.InteractionSSEStreamEvent]) {
    defer s.Close()
    for s.Next() {
        event := s.Value()
        if created := event.GetDataInteractionCreated(); created != nil {
            p.interactionID = created.Interaction.ID
            if created.EventID != nil {
                p.lastEventID = created.EventID
            }
        } else if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if stepDelta.EventID != nil {
                p.lastEventID = stepDelta.EventID
            }
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            } else if thoughtDelta := stepDelta.GetDeltaThoughtSummary(); thoughtDelta != nil {
                if textContent := thoughtDelta.GetContentText(); textContent != nil {
                    fmt.Printf("Thought: %s\n", textContent.GetText())
                }
            }
        } else if event.GetDataInteractionCompleted() != nil || event.GetDataError() != nil {
            p.isComplete = true
        }
    }
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    processor := &StreamProcessor{}
    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Research the history of Google TPUs."),
            Background:  genai.Ptr(true),
            Stream:      genai.Ptr(true),
            AgentConfig: &agentCfg,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    processor.processStream(res.InteractionSSEStreamEvent)

    // Reconnect if the connection drops
    for !processor.isComplete && processor.interactionID != "" {
        statusRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: processor.interactionID,
        })
        if err != nil || statusRes.Interaction.Status != interactions.InteractionStatusInProgress {
            break
        }
        streamRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID:          processor.interactionID,
            Stream:      genai.Ptr(true),
            LastEventID: processor.lastEventID,
        })
        if err != nil {
            break
        }
        processor.processStream(streamRes.InteractionSSEStreamEvent)
    }
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Questions et interactions complémentaires

Vous pouvez poursuivre la conversation après que l'agent a renvoyé le rapport final en utilisant `previous_interaction_id`. Cela vous permet de demander des clarifications, des résumés ou des détails sur des sections spécifiques de la recherche sans avoir à redémarrer l'ensemble de la tâche.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-4-argon",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-4-argon',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-4-argon")
        .input(InteractionsInput.of("Can you elaborate on the second point in the report?"))
        .previousInteractionId("COMPLETED_INTERACTION_ID")
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-4-argon"),
            Input:                 interactions.NewInteractionsInput("Can you elaborate on the second point in the report?"),
            PreviousInteractionID: genai.Ptr("COMPLETED_INTERACTION_ID"),
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
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-4-argon",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Quand utiliser l'agent Gemini Deep Research

Deep Research est un **agent**, et pas seulement un modèle. Elle est particulièrement adaptée aux charges de travail qui nécessitent une approche "analyst-in-a-box" plutôt qu'un chat à faible latence.

| Fonctionnalité | Modèles Gemini standards | Agent Gemini Deep Research |
| --- | --- | --- |
| **Latence** | Secondes | Minutes (asynchrone/en arrière-plan) |
| **Procédure** | Générer > Sortie | Planifier > Rechercher > Lire > Itérer > Sortie |
| **Résultat** | Texte conversationnel, code, résumés courts | Rapports détaillés, analyses longues, tableaux comparatifs |
| **Recommandé pour** | Chatbots, extraction, écriture créative | Étude de marché, diligence raisonnable, revues de littérature, analyse de la concurrence |

## Configurer l'agent

Deep Research utilise le paramètre `agent_config` pour contrôler le comportement.
Transmettez-le sous forme de dictionnaire avec les champs suivants :

| Champ | Type | Par défaut | Description |
| --- | --- | --- | --- |
| `type` | `string` | Obligatoire | doit être `"deep-research"` |
| `thinking_summaries` | `string` | `"none"` | Définissez la valeur sur `"auto"` pour recevoir des étapes de raisonnement intermédiaires pendant le streaming. Définissez la valeur sur `"none"` pour désactiver la fonctionnalité. |
| `visualization` | `string` | `"auto"` | Défini sur `"auto"` pour activer les graphiques et les images générés par l'agent. Définissez la valeur sur `"off"` pour désactiver la fonctionnalité. |
| `collaborative_planning` | `boolean` | `false` | Définissez la valeur sur `true` pour activer l'examen du plan multitour avant le début de la recherche. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.Visualization;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

DeepResearchAgentConfig agentConfig =
    DeepResearchAgentConfig.builder()
        .thinkingSummaries(ThinkingSummaries.AUTO)
        .visualization(Visualization.AUTO)
        .collaborativePlanning(false)
        .build();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the competitive landscape of cloud GPUs."))
        .agentConfig(agentConfig)
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
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

    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        Visualization:         interactions.VisualizationAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(false),
    })

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Research the competitive landscape of cloud GPUs."),
            AgentConfig: &agentCfg,
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## Disponibilité et prix

Vous pouvez accéder à l'agent Gemini Deep Research à l'aide de l'API Interactions dans Google AI Studio et l'API Gemini.

La tarification suit un [modèle de paiement à l'usage](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#pricing-for-agents) basé sur les modèles Gemini sous-jacents et les outils spécifiques utilisés par l'agent. Contrairement aux requêtes de chat standards, où une requête conduit à une seule sortie, une tâche Deep Research est un workflow agentique. Une seule requête déclenche une boucle autonome de planification, de recherche, de lecture et de raisonnement.

### Coûts estimés

Les coûts varient en fonction de la profondeur de la recherche requise. L'agent détermine de manière autonome la quantité de lecture et de recherche nécessaire pour répondre à votre requête.

- **Deep Research** (`deep-research-preview-04-2026`) : pour une requête typique nécessitant une analyse modérée, l'agent peut utiliser environ 80 requêtes de recherche, environ 250 000 jetons d'entrée (environ 50 à 70% mis en cache) et environ 60 000 jetons de sortie.
  - **Total estimé** : entre 1 et 3 $ par tâche
- **Deep Research Max** (`deep-research-max-preview-04-2026`) : pour une analyse approfondie du paysage concurrentiel ou une due diligence complète, l'agent peut utiliser jusqu'à environ 160 requêtes de recherche, environ 900 000 tokens d'entrée (environ 50 à 70% mis en cache) et environ 80 000 tokens de sortie.
  - **Total estimé** : entre 3 et 7 $ par tâche

## Considérations de sécurité

Accorder à un agent l'accès au Web et à vos fichiers privés nécessite d'examiner attentivement les risques de sécurité.

- **Injection de prompt à l'aide de fichiers** : l'agent lit le contenu des fichiers que vous fournissez. Assurez-vous que les documents importés (PDF, fichiers texte) proviennent de sources fiables. Un fichier malveillant peut contenir du texte caché conçu pour manipuler la sortie de l'agent.
- **Risques liés au contenu Web** : l'agent effectue des recherches sur le Web public. Bien que nous mettions en place des filtres de sécurité robustes, il existe un risque que l'agent rencontre et traite des pages Web malveillantes. Nous vous recommandons de consulter les `citations` fournies dans la réponse pour vérifier les sources.
- **Exfiltration** : soyez prudent lorsque vous demandez à l'agent de résumer des données internes sensibles si vous lui permettez également de naviguer sur le Web.

## Bonnes pratiques

- **Demander des informations inconnues** : indiquez à l'agent comment gérer les données manquantes.
  Par exemple, ajoutez *"Si des chiffres spécifiques pour 2025 ne sont pas disponibles, indiquez explicitement qu'il s'agit de projections ou qu'ils ne sont pas disponibles, plutôt que de les estimer"* à votre requête.
- **Fournissez du contexte** : ancrez la recherche de l'agent en fournissant des informations générales ou des contraintes directement dans la requête d'entrée.
- **Utilisez la planification collaborative** : pour les requêtes complexes, activez la planification collaborative afin d'examiner et d'affiner le plan de recherche avant son exécution.
- **Entrées multimodales** : l'agent Deep Research accepte les entrées multimodales.
  Utilisez cette option avec précaution, car elle augmente les coûts et le risque de dépassement de la fenêtre de contexte.

## Limites

- **Outils personnalisés** : vous ne pouvez pas fournir d'outils d'appel de fonction personnalisés pour le moment, mais vous pouvez utiliser des serveurs MCP (Model Context Protocol) distants avec l'agent Deep Research.
- **Sortie structurée** : l'agent Deep Research n'est actuellement pas compatible avec les sorties structurées.
- **Durée de recherche maximale** : l'agent Deep Research dispose d'une durée de recherche maximale de 60 minutes. La plupart des tâches devraient être effectuées en moins de 20 minutes.
- **Exigence du magasin** : l'exécution de l'agent à l'aide de `background=True` nécessite `store=True`.
- **Recherche Google** : la [recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) est activée par défaut, et des [restrictions spécifiques](https://ai.google.dev/gemini-api/terms?hl=fr#use-restrictions2) s'appliquent aux résultats ancrés.

## Étape suivante

- En savoir plus sur l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr)
- Découvrez comment utiliser vos propres données avec l'outil [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/13 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/13 (UTC)."],[],[]]
