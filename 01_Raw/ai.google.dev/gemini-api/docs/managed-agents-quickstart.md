---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr
fetched_at: 2026-10-05T06:45:15.453426+00:00
title: "Guide de d\u00e9marrage rapide sur les agents g\u00e9r\u00e9s \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Guide de démarrage rapide sur les agents gérés

Ce guide vous explique comment créer et utiliser des agents gérés sur l'API Gemini à l'aide de l'[agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr). Vous allez effectuer votre premier appel d'agent, poursuivre une conversation multitours, diffuser la réponse, télécharger des fichiers depuis le bac à sable et travailler avec l'agent géré Antigravity.

## Exécuter votre première interaction avec un agent

Un seul appel à l'[API Interactions](https://ai.google.dev/gemini-api/docs?hl=fr) provisionne un bac à sable Linux, exécute la boucle de l'agent et renvoie le résultat. Vous allez définir trois paramètres :

- Transmettez `agent` en tant que `"antigravity-preview-09-2026"`, qui est la version actuelle de notre agent géré prédéfini et à usage général.
- Définissez `environment="remote"` pour provisionner un nouvel environnement de bac à sable.
- Créez une entrée en définissant ce que vous attendez de l'agent.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
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
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the agent's final output
System.out.println("Interaction ID: " + interaction.id().orElse(""));
System.out.println("Environment ID: " + interaction.environmentId().orElse(""));
System.out.println("Output: " + interaction.outputText().orElse(""));
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
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    // Print the agent's final output
    fmt.Printf("Interaction ID: %s\n", *interaction.ID)
    fmt.Printf("Environment ID: %s\n", *interaction.EnvironmentID)
    fmt.Printf("Output: %s\n", *interaction.OutputText)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

La réponse renvoie un objet `Interaction`. Stockez `interaction.id` et `interaction.environment_id` pour poursuivre la conversation dans le même bac à sable. Utilisez `interaction.output_text` pour accéder à la réponse finale de l'agent. `interaction.steps` liste chaque étape effectuée par l'agent (raisonnement, appels d'outils, exécution de code).

## Poursuivre la conversation (multitour)

L'API suit deux dimensions d'état indépendantes :

- **Contexte de la conversation** : historique des discussions, trace de raisonnement, utilisation d'outils, utilisation de `previous_interaction_id`.
- [**État de l'environnement**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr) : fichiers, packages installés et état du bac à sable, à l'aide de `environment`.

Transmettez les deux dans leur emplacement respectif pour reprendre :

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
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
String interactionId = "INTERACTION_ID";
String environmentId = "ENVIRONMENT_ID";

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .previousInteractionId(interactionId)
    .environment(CreateAgentInteractionEnvironment.of(environmentId))
    .input(InteractionsInput.of("Now plot the Fibonacci sequence as a line chart and save it as chart.png."))
    .build();

Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction2.outputText().orElse(""));
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

    interactionID := "INTERACTION_ID"
    environmentID := "ENVIRONMENT_ID"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            PreviousInteractionID: genai.Ptr(interactionID),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(environmentID)),
            Input:                 interactions.NewInteractionsInput("Now plot the Fibonacci sequence as a line chart and save it as chart.png."),
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
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

Les fichiers du tour 1 (`fibonacci.txt`) sont conservés au tour 2. L'agent conserve également le contexte de la conversation.

Vous pouvez combiner ces éléments indépendamment :

- **Effacer la conversation, conserver les fichiers** : omettez `previous_interaction_id` et ne transmettez que l'ID d'environnement à l'aide de `environment` pour une nouvelle conversation dans le même espace de travail.
- **Conserver la conversation, nouvel espace de travail** : transmettez `previous_interaction_id` et définissez `environment="remote"` pour un nouvel bac à sable.

### Compression automatique du contexte

Dans les conversations longues et multitours, l'historique brut des étapes de raisonnement, des appels d'outils et du contenu des fichiers volumineux peut rapidement s'allonger et consommer un espace de contexte important. Pour éviter les erreurs liées à la limite de jetons et maintenir la concentration de l'agent (en évitant la "détérioration du contexte"), l'API Managed Agents inclut une étape de compaction du contexte natif à environ 135 000 jetons. Ce processus est automatique.

## Diffuser la réponse

Pour les tâches de longue durée, vous pouvez diffuser la réponse en streaming pour voir l'agent travailler en temps réel :

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
    if event.event_type == "step.stop" and event.usage:
        print(event.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
    if (event.event_type === "step.stop" && event.usage) {
        console.log(event.usage);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.StepStop;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Read Hacker News, summarize the top 5 stories, and save the results as a PDF."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .stream(true)
    .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(params)).events()) {
  for (InteractionSSEStreamEvent event : stream) {
    System.out.println(event);
    if (event.data().isPresent() && event.data().get() instanceof StepStop stepStop) {
      stepStop.usage().ifPresent(System.out::println);
    }
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
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Read Hacker News, summarize the top 5 stories, and save the results as a PDF."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Stream:      genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        fmt.Printf("%+v\n", event)
        if stepStop := event.GetDataStepStop(); stepStop != nil && stepStop.Usage != nil {
            fmt.Printf("%+v\n", stepStop.Usage)
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

Le streaming renvoie les deltas d'étapes avec des mises à jour incrémentielles. Lorsqu'une étape est terminée, l'événement `step.stop` inclut des statistiques d'utilisation cumulées. Pour en savoir plus, consultez le [guide sur le streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=fr).

## Télécharger des fichiers depuis l'environnement

Lorsque l'agent crée des fichiers dans le bac à sable. Téléchargez-les à l'aide de l'API Files avec une requête HTTP directe (aucune méthode SDK n'est encore disponible) :

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### Java

```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

String envId = "ENVIRONMENT_ID";
String apiKey = System.getenv("GEMINI_API_KEY");

HttpClient httpClient = HttpClient.newBuilder()
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://generativelanguage.googleapis.com/v1beta/files/environment-" + envId + ":download?alt=media"))
    .header("x-goog-api-key", apiKey)
    .GET()
    .build();

HttpResponse<byte[]> response = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray());
Files.write(Paths.get("snapshot.tar"), response.body());
System.out.println("Saved snapshot to snapshot.tar");
```

### Go

```
package main

import (
    "context"
    "fmt"
    "io"
    "log"
    "net/http"
    "os"
)

func main() {
    ctx := context.Background()
    envID := "ENVIRONMENT_ID"
    apiKey := os.Getenv("GEMINI_API_KEY")

    url := fmt.Sprintf("https://generativelanguage.googleapis.com/v1beta/files/environment-%s:download?alt=media", envID)
    req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
    if err != nil {
        log.Fatal(err)
    }
    req.Header.Set("x-goog-api-key", apiKey)

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()

    data, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    if err := os.WriteFile("snapshot.tar", data, 0644); err != nil {
        log.Fatal(err)
    }
    fmt.Println("Saved snapshot to snapshot.tar")
}
```

### REST

```
ENV_ID="your_environment_id_here"

curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

mkdir -p extracted_snapshot
tar -xf snapshot.tar -C extracted_snapshot
```

## Enregistrer un agent géré

Lors des étapes précédentes, nous avons utilisé l'agent Antigravity par défaut et l'avons personnalisé en ligne. Une fois que vous avez itéré sur votre configuration (instructions, compétences, sélection de modèle et environnement), vous pouvez l'enregistrer en tant qu'agent géré réutilisable. Cela vous permet de l'appeler par ID sans répéter la configuration.

Lorsque vous enregistrez un agent, notez la symétrie architecturale avec les interactions intégrées : vous spécifiez `base_agent: "antigravity-preview-09-2026"` et pouvez transmettre un `agent_config` avec votre `model` choisi, comme vous le feriez sur `interactions.create`. Vous définissez également un `base_environment` (à partir de sources ou en dupliquant un environnement existant). L'agent utilisera cette configuration d'environnement et de modèle pour chaque nouvelle interaction.

**À partir de sources** : définissez des sources intégrées ou à partir d'autres sources telles que GitHub ou Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-09-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.8-flash",
    },
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-09-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.8-flash",
    },
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
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
            .content("Always include a chart and a summary table in your reports.")
            .build(),
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/your-org/skills")
            .target(".agents/skills")
            .build()
    ))
    .build();

Agent agentParams = Agent.builder()
    .id("fibonacci-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .agentConfig(AgentConfig.of(
        AntigravityAgentConfig.builder()
            .model("gemini-3.8-flash")
            .build()
    ))
    .systemInstruction("You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Saved agent: " + agent.id().orElse(""));
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
                Content: genai.Ptr("Always include a chart and a summary table in your reports."),
            },
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/your-org/skills"),
                Target: genai.Ptr(".agents/skills"),
            },
        },
    }

    res, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:        genai.Ptr("fibonacci-analyst"),
            BaseAgent: genai.Ptr("antigravity-preview-09-2026"),
            AgentConfig: genai.Ptr(agents.NewAgentConfig(interactions.AntigravityAgentConfig{
                Model: genai.Ptr("gemini-3.8-flash"),
            })),
            SystemInstruction: genai.Ptr("You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(env)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Saved agent: %s\n", *res.Agent.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-09-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.8-flash"
    },
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Appeler l'agent géré

Une fois que vous avez enregistré un agent géré, vous pouvez l'appeler par son ID. Chaque appel duplique l'environnement de base, de sorte que chaque exécution commence de manière propre :

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

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
    .agent(AgentOption.of("fibonacci-analyst"))
    .input(InteractionsInput.of("Generate the first 50 prime numbers, plot their distribution, and save a PDF report."))
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
            Agent:       interactions.AgentOption("fibonacci-analyst"),
            Input:       interactions.NewInteractionsInput("Generate the first 50 prime numbers, plot their distribution, and save a PDF report."),
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
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## Étape suivante

- [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr) : fonctionnalités, outils compatibles, entrée multimodale, tarifs et limites.
- [Créer des agents gérés](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr) : étendez Antigravity avec vos propres instructions, compétences et données.
- [Environnements](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr) : sources, mise en réseau, cycle de vie, limites de ressources.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) : API sous-jacente pour les modèles et les agents.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/01 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/01 (UTC)."],[],[]]
