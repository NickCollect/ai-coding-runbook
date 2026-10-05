---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr
fetched_at: 2026-10-05T06:47:52.053326+00:00
title: "Environnements dans les agents g\u00e9r\u00e9s \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Environnements dans les agents gérés

Les environnements sont des bacs à sable Linux gérés qui offrent aux agents un espace isolé pour exécuter du code et conserver des fichiers. Ils sont dissociés du contexte d'interaction. Vous pouvez donc réutiliser le même environnement pour plusieurs interactions ou repartir de zéro à tout moment.

L'exemple suivant montre comment créer une interaction avec un environnement distant et récupérer son ID :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas and matplotlib, verify the imports, and print the versions.",
    environment="remote",
)

print(f"Environment ID: {interaction.environment_id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Install pandas and matplotlib, verify the imports, and print the versions.",
    environment: "remote",
});

console.log(`Environment ID: ${interaction.environment_id}`);
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
    .input(InteractionsInput.of("Install pandas and matplotlib, verify the imports, and print the versions."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Environment ID: " + interaction.environmentId().orElse(""));
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
            Input:       interactions.NewInteractionsInput("Install pandas and matplotlib, verify the imports, and print the versions."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.EnvironmentID != nil {
        fmt.Printf("Environment ID: %s\n", *res.Interaction.EnvironmentID)
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
    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",
    "environment": "remote"
}'
```

## Paramètre `environment`

Le paramètre `environment` accepte trois formes :

| Formulaire | Exemple | Quand les utiliser ? |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | Provisionnez un bac à sable. |
| ID de l'environnement | `environment="env_abc123"` | Réutilisez un bac à sable existant avec tous ses fichiers et packages. |
| Objet de configuration | `environment={...}` | Provisionnez un bac à sable avec des sources, des règles réseau, des variables d'environnement ou une combinaison de ces éléments. |

Les exemples suivants illustrent les trois façons d'utiliser le paramètre `environment`.

### Python

```
from google import genai

client = genai.Client()

# Fresh sandbox
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a hello world script.",
    environment="remote",
)

# Reuse an existing sandbox
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Modify the script to accept a name argument.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# New sandbox with sources
interaction_3 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List all files and summarize the project.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            }
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Fresh sandbox
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Write a hello world script.",
    environment: "remote",
});

// Reuse an existing sandbox
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Modify the script to accept a name argument.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

// New sandbox with sources
const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List all files and summarize the project.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
        ],
    },
});

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

// Fresh sandbox
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Write a hello world script."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();
Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Reuse an existing sandbox
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Modify the script to accept a name argument."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction.id().orElse(""))
    .build();
Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// New sandbox with sources
Environment env3 = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/octocat/Spoon-Knife")
            .target("/workspace/spoon-knife")
            .build()
    ))
    .build();

CreateAgentInteraction params3 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List all files and summarize the project."))
    .environment(CreateAgentInteractionEnvironment.of(env3))
    .build();
Interaction interaction3 = client.interactions.create(CreateInteractionRequestBody.of(params3)).interaction().get();

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

    // Fresh sandbox
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Write a hello world script."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res1.Interaction

    // Reuse an existing sandbox
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Modify the script to accept a name argument."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res2

    // New sandbox with sources
    env3 := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/octocat/Spoon-Knife"),
                Target: genai.Ptr("/workspace/spoon-knife"),
            },
        },
    }

    res3, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List all files and summarize the project."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env3)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res3

    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

### REST

```
# Fresh sandbox
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Write a hello world script."}],
    "environment": "remote"
}'

# Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-09-2026\",
    \"input\": [{\"type\": \"text\", \"text\": \"Modify the script to accept a name argument.\"}],
    \"environment\": \"$ENV_ID\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
}"

# New sandbox with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "List all files and summarize the project."}],
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            }
        ]
    }
}'
```

## Configurer un environnement

Une façon de configurer un environnement consiste à indiquer à l'agent ce que vous devez installer.
Il gère la résolution des dépendances et le dépannage. Une fois l'environnement prêt, enregistrez le `environment_id` et réutilisez-le.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment="remote",
)

# Reuse the configured environment
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# Reuse the configured environment
interaction_3 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Using the tools in /workspace/tools, list the files.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction_2.id,
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment: "remote",
});

const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Using the tools in /workspace/tools, list the files.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction2.id,
});
console.log(interaction.output_text);
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

CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();
Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Reuse the configured environment
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction.id().orElse(""))
    .build();
Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Reuse the configured environment
CreateAgentInteraction params3 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Using the tools in /workspace/tools, list the files."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction2.id().orElse(""))
    .build();
Interaction interaction3 = client.interactions.create(CreateInteractionRequestBody.of(params3)).interaction().get();

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

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res1.Interaction

    // Reuse the configured environment
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction2 := res2.Interaction

    // Reuse the configured environment
    res3, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Using the tools in /workspace/tools, list the files."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction2.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res3

    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

### REST

```
# Create interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    "environment": "remote"
}'
```

### Monter à partir d'une source

Si vous savez exactement quels fichiers l'agent a besoin, installez-les en un seul appel au lieu d'itérer. L'objet de configuration `environment` accepte un tableau `sources` avec trois types :

| Type de source | Valeur `type` | Description | Limite |
| --- | --- | --- | --- |
| Dépôt Git | `repository` | Clone un dépôt à partir d'une URL dans le bac à sable à l'adresse `target`. | 500 Mo |
| Cloud Storage | `gcs` | Copie un fichier ou un répertoire depuis Cloud Storage dans le bac à sable à l'emplacement `target`. | 2 Go |
| Contenu intégré | `inline` | Écrit le contenu du texte brut dans un fichier du bac à sable à l'emplacement `target`. | 1 Mo par fichier, 2 Mo au total |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List all files under /workspace and describe what you find.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data",
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md",
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
    input: "List all files under /workspace and describe what you find.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
            {
                type: "gcs",
                source: "gs://cloud-samples-data/bigquery/us-states/",
                target: "/workspace/gcs-data",
            },
            {
                type: "inline",
                content: "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                target: "/workspace/notes/readme.md",
            },
        ],
    },
});

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
            .type(SourceType.REPOSITORY)
            .source("https://github.com/octocat/Spoon-Knife")
            .target("/workspace/spoon-knife")
            .build(),
        Source.builder()
            .type(SourceType.GCS)
            .source("gs://cloud-samples-data/bigquery/us-states/")
            .target("/workspace/gcs-data")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .content("# Project Notes\n\n- Analyze state population data\n- Create visualizations\n")
            .target("/workspace/notes/readme.md")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List all files under /workspace and describe what you find."))
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
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/octocat/Spoon-Knife"),
                Target: genai.Ptr("/workspace/spoon-knife"),
            },
            {
                Type:   interactions.SourceTypeGcs.ToPointer(),
                Source: genai.Ptr("gs://cloud-samples-data/bigquery/us-states/"),
                Target: genai.Ptr("/workspace/gcs-data"),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Content: genai.Ptr("# Project Notes\n\n- Analyze state population data\n- Create visualizations\n"),
                Target:  genai.Ptr("/workspace/notes/readme.md"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List all files under /workspace and describe what you find."),
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
# Create interaction with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "List all files under /workspace and describe what you find.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data"
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md"
            }
        ]
    }
}'
```

Vous pouvez combiner les deux approches : monter les sources connues de manière déclarative, puis itérer avec des interactions de suivi pour installer des packages ou exécuter des scripts de configuration. Vous ne pouvez pas définir la racine (`/`) comme cible lorsque vous ajoutez une source personnalisée. Vous devez toujours spécifier un sous-répertoire.

### Accroches

Vous pouvez également monter un fichier de configuration `.agents/hooks.json` et des scripts d'interception personnalisés dans le bac à sable pour appliquer des mesures de sécurité ou exécuter des validations automatiques chaque fois que des outils sont exécutés. Pour obtenir des définitions de schéma et des exemples de code, consultez [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fr).

### Sources privées

Vous pouvez également télécharger des fichiers à partir de dépôts GitHub privés ou de buckets Cloud Storage privés en authentifiant le domaine source dans la configuration réseau.

Une option consiste à utiliser des [identifiants](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr) stockés référencés par ID. Vous stockez ainsi le secret une seule fois, et chaque environnement qui a besoin de cette source peut le référencer :

```
"network": {
    "allowlist": [
        { "domain": "github.com", "credential": "github-production" },
        { "domain": "*" }
    ]
}
```

Vous pouvez également définir l'en-tête en ligne avec `transform`, comme le font les exemples suivants. Le proxy de sortie applique les deux formes de la même manière, et dans aucun des cas, le secret n'atterrit dans le bac à sable.

Pour les **dépôts Git privés**, utilisez l'authentification `Basic` avec votre [jeton d'accès personnel (PAT) GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
Encodez le jeton en utilisant `x-oauth-basic` comme nom d'utilisateur :

```
echo -n "x-oauth-basic:ghp_YourPATHere" | base64
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the test for my backend app and fix any issue.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the test for my backend app and fix any issue.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app"
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
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
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/your-org/backend")
            .target("/backend-app")
            .build()
    ))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run the test for my backend app and fix any issue."))
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
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/your-org/backend"),
                Target: genai.Ptr("/backend-app"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Basic YOUR_BASE64_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run the test for my backend app and fix any issue."),
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
    "agent": "antigravity-preview-09-2026",
    "input": "Run the test for my backend app and fix any issue.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

Pour les **buckets Cloud Storage privés**, utilisez un jeton de support OAuth 2.0 standard :

```
gcloud auth print-access-token
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the discrepancies across the data in workspace",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "*.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Analyze the discrepancies across the data in workspace",
    environment: {
        type: "remote",
        sources: [
            {
                type: "gcs",
                source: "gs://my-private-bucket/data",
                target: "/workspace",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
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
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.GCS)
            .source("gs://my-private-bucket/data")
            .target("/workspace")
            .build()
    ))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("*.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer YOUR_GCS_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the discrepancies across the data in workspace"))
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
                Type:   interactions.SourceTypeGcs.ToPointer(),
                Source: genai.Ptr("gs://my-private-bucket/data"),
                Target: genai.Ptr("/workspace"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "*.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer YOUR_GCS_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Analyze the discrepancies across the data in workspace"),
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
    "agent": "antigravity-preview-09-2026",
    "input": "Analyze the discrepancies across the data in workspace",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

## Logiciel pré-installé

Le bac à sable s'exécute sur Ubuntu et est fourni avec des environnements d'exécution et des packages courants préinstallés. L'agent peut installer des packages supplémentaires au moment de l'exécution à l'aide de `pip
install` ou `npm install`. Les packages installés lors d'une interaction persistent lorsque vous réutilisez le même `environment_id`.

| Catégorie | Packages pré-installés |
| --- | --- |
| **Outils UNIX** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## Variables d'environnement

Utilisez le champ `env` pour définir les variables d'environnement dans le bac à sable. Chaque entrée mappe un nom de variable à une chaîne littérale pour la configuration ou à une référence à un [identifiant](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr) stocké pour un secret. L'agent les voit comme dans n'importe quel shell. Les outils et les scripts qui lisent l'environnement de processus les récupèrent donc sans câblage supplémentaire.

| Champ | Type | Description |
| --- | --- | --- |
| `env` | `object` | Mappage du nom de la variable à la valeur. Une valeur est soit un littéral `string`, soit une référence d'identifiant au format `{"credential": "credential-id"}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build the project and run the test suite.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "LOG_LEVEL": "debug",
            "API_TOKEN": {"credential": "my-api-token"},
        },
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
    input: "Build the project and run the test suite.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            LOG_LEVEL: "debug",
            API_TOKEN: { credential: "my-api-token" },
        },
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Build the project and run the test suite."}],
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "LOG_LEVEL": "debug",
            "API_TOKEN": {"credential": "my-api-token"}
        }
    }
}'
```

Les variables s'appliquent à chaque commande exécutée par l'agent lors de cette interaction, y compris les commandes shell, les étapes de compilation et tout processus qu'il lance.

Ces deux types de valeurs se comportent différemment. Une chaîne littérale est écrite dans le conteneur en tant que texte brut. Une référence d'identifiant n'est pas : la variable reçoit un espace réservé, et le proxy de sortie remplace le véritable secret uniquement dans les requêtes sortantes vers les domaines de confiance de cet identifiant. Pour en savoir plus, consultez [Utiliser des identifiants comme variables d'environnement](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr#environment-variables).

## Configuration du réseau

Par défaut, les environnements disposent d'un accès réseau sortant illimité. Utilisez le champ `network` pour limiter le trafic sortant à des domaines spécifiques. Chaque règle spécifie un `domain`, ainsi qu'un `credential` facultatif pour injecter un secret stocké et un objet `transform` facultatif pour injecter des en-têtes dans les requêtes correspondantes.
Ces en-têtes peuvent être uniques pour chaque interaction et vous pouvez les mettre à jour pour le même environnement.

| Champ | Type | Description |
| --- | --- | --- |
| `domain` | `string` | Domaine à mettre en correspondance. Utilisez un nom d'hôte exact ou `*` pour tous les domaines. |
| `credential` | `string` | ID d'un [identifiant](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr) stocké. Le proxy de sortie le résout et injecte l'en-tête d'authentification au moment de la requête. |
| `transform` | `object` | Objet contenant des paires clé/valeur plates représentant les en-têtes à injecter dans les requêtes correspondantes, par exemple `{"Authorization": "Bearer ..."}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                {"domain": "pypi.org"},
                {"domain": "*"},
            ]
        },
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
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                { domain: "pypi.org" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
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

Environment env = Environment.builder()
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_your_github_token"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build(),
                AllowlistEntry.builder().domain("*").build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Fetch the latest issues from the GitHub API for my-org/my-repo."))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_your_github_token",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Fetch the latest issues from the GitHub API for my-org/my-repo."),
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
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Fetch the latest issues from the GitHub API for my-org/my-repo."}],
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    }
                },
                {"domain": "pypi.org"},
                {"domain": "*"}
            ]
        }
    }
}'
```

Lorsqu'une liste d'autorisation est définie, seules les requêtes adressées aux domaines explicitement listés sont autorisées. Vous pouvez utiliser des caractères génériques pour faire correspondre des sous-domaines (par exemple, `{"domain":
"*.example.com"}`), mais notez que cela ne correspond pas au domaine racine `example.com`, qui doit être ajouté séparément. Pour autoriser tout autre trafic, comme le routage de domaines non listés sans en-têtes injectés, ajoutez `{"domain": "*"}` en tant qu'entrée générique.

### Identifiants

Il existe deux façons d'authentifier le trafic sortant : un identifiant d'informations d'identification stockées et un `transform` intégré à la règle de liste d'autorisation. Le proxy de sortie s'applique à la fois sur le réseau. Dans les deux cas, le secret n'entre jamais dans le bac à sable et n'apparaît jamais dans vos charges utiles d'interaction.

Les [identifiants gérés](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr) sont ceux à utiliser lorsque vous souhaitez stocker le secret une seule fois et le réutiliser. Chaque environnement, agent et déclencheur de votre projet peut faire référence au même ID, et vous pouvez le faire pivoter à un seul endroit.

### Python

```
from google import genai

client = genai.Client()

# Store the secret once
client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_your_github_token",
)

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {"domain": "api.github.com", "credential": "github-production"},
                {"domain": "*"},
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Store the secret once
await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_your_github_token",
});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
```

### REST

```
# Store the secret once
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_your_github_token"
}'

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                { "domain": "api.github.com", "credential": "github-production" },
                { "domain": "*" }
            ]
        }
    }
}'
```

Un identifiant `oauth2` actualise également son jeton d'accès de manière autonome. Ainsi, une interaction de longue durée ne s'interrompt pas lorsque le jeton expire. Pour obtenir la liste complète des types d'identifiants et des opérations de gestion, consultez [Identifiants](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr).

Vous pouvez également définir des en-têtes en ligne avec `transform`. Cela convient lorsque la valeur appartient à un seul appel, par exemple un jeton que vous générez juste avant de créer l'interaction. Les en-têtes définis de cette manière sont injectés par le même proxy de sortie. Ils ne sont jamais exposés dans le bac à sable en tant que variables d'environnement ou fichiers.

### Python

```
import subprocess
from google import genai

# Fetch a short-lived access token from your local gcloud CLI
gcloud_token = subprocess.check_output(
    ["gcloud", "auth", "print-access-token"], text=True
).strip()

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": f"Bearer {gcloud_token}"
                    },
                }
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import { execSync } from "child_process";

const gcloudToken = execSync("gcloud auth print-access-token").toString().trim();

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": `Bearer ${gcloudToken}`
                    },
                }
            ]
        }
    },
});

console.log(interaction.output_text);
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
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

// Fetch a short-lived access token from your local gcloud CLI
Process process = new ProcessBuilder("gcloud", "auth", "print-access-token").start();
String gcloudToken = new String(process.getInputStream().readAllBytes(), StandardCharsets.UTF_8).trim();

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer " + gcloudToken
                    )))
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List the files in gs://my-bucket/reports/ using the GCS JSON API."))
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
    "os/exec"
    "strings"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()

    // Fetch a short-lived access token from your local gcloud CLI
    out, err := exec.Command("gcloud", "auth", "print-access-token").Output()
    if err != nil {
        log.Fatal(err)
    }
    gcloudToken := strings.TrimSpace(string(out))

    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer " + gcloudToken,
                    })),
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List the files in gs://my-bucket/reports/ using the GCS JSON API."),
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
    "agent": "antigravity-preview-09-2026",
    "input": "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer <YOUR_GCLOUD_TOKEN>"
                    }
                }
            ]
        }
    }
}'
```

`credential` et `transform` peuvent apparaître dans la même règle. L'identifiant est appliqué en premier, et `transform` est fusionné par-dessus. Par conséquent, un en-tête `transform` explicite est prioritaire si les deux définissent la même clé. Un modèle courant est un identifiant pour l'en-tête d'authentification, plus un `transform` pour les en-têtes supplémentaires attendus par le service.

### Désactiver l'accès au réseau

Pour bloquer tous les accès réseau sortants, définissez `network` sur `disabled` :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the local files only.",
    environment={
        "type": "remote",
        "network": "disabled",
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
    input: "Analyze the local files only.",
    environment: {
        type: "remote",
        network: "disabled",
    },
});

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
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.NetworkEnum;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(NetworkEnum.DISABLED))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the local files only."))
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
        Network: genai.Ptr(interactions.NewNetwork(interactions.NetworkEnumDisabled)),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Analyze the local files only."),
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
    "agent": "antigravity-preview-09-2026",
    "input": "Analyze the local files only.",
    "environment": {
        "type": "remote",
        "network": "disabled"
    }
}'
```

### Actualiser les identifiants

Les jetons intégrés tels que les jetons d'accès et les clés API de courte durée expirent.
Vous pouvez les actualiser en transmettant le `environment_id` existant avec une nouvelle configuration `network` lors de la prochaine interaction. Les nouvelles règles réseau remplacent entièrement les précédentes, tandis que l'état du système de fichiers de l'environnement (packages, fichiers, dépôts installés) est conservé.

Si vous utilisez un [identifiant](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fr) stocké, vous n'en avez pas besoin. Un identifiant `oauth2` s'actualise automatiquement. La rotation d'un identifiant est une `PATCH` sur l'identifiant qui laisse intactes toutes les règles de liste autorisée le référençant.

### Python

```
from google import genai

client = genai.Client()

# First interaction: use an initial token
first = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        },
    },
)

# Later: refresh the token on the same environment
result = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Now download the file reports/q1.csv from the same bucket.",
    environment={
        "type": "remote",
        "environment_id": first.environment_id,
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First interaction: use an initial token
const first = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        }
    },
});

// Later: refresh the token on the same environment
const result = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Now download the file reports/q1.csv from the same bucket.",
    environment: {
        type: "remote",
        environment_id: first.environment_id,
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        }
    },
});

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

// First interaction: use an initial token
Environment initialEnv = Environment.builder()
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer INITIAL_TOKEN"
                    )))
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction firstParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List the files in gs://my-bucket/reports/ using the GCS JSON API."))
    .environment(CreateAgentInteractionEnvironment.of(initialEnv))
    .build();

Interaction first = client.interactions.create(CreateInteractionRequestBody.of(firstParams)).interaction().get();

// Later: refresh the token on the same environment
Environment refreshedEnv = Environment.builder()
    .environmentId(first.environmentId().orElse(""))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer REFRESHED_TOKEN"
                    )))
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction secondParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Now download the file reports/q1.csv from the same bucket."))
    .environment(CreateAgentInteractionEnvironment.of(refreshedEnv))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(secondParams)).interaction().get();
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

    // First interaction: use an initial token
    initialEnv := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer INITIAL_TOKEN",
                    })),
                },
            },
        }))),
    }

    firstRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List the files in gs://my-bucket/reports/ using the GCS JSON API."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(initialEnv)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    first := firstRes.Interaction

    // Later: refresh the token on the same environment
    refreshedEnv := interactions.Environment{
        EnvironmentID: first.EnvironmentID,
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer REFRESHED_TOKEN",
                    })),
                },
            },
        }))),
    }

    secondRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Now download the file reports/q1.csv from the same bucket."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(refreshedEnv)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if secondRes.Interaction.OutputText != nil {
        fmt.Println(*secondRes.Interaction.OutputText)
    }
}
```

### REST

```
# Use the environment_id from a previous interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Now download the file reports/q1.csv from the same bucket.",
    "environment": {
        "type": "remote",
        "environment_id": "<ENVIRONMENT_ID_FROM_PREVIOUS_INTERACTION>",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    }
                }
            ]
        }
    }
}'
```

## Cycle de vie de l'environnement

Les environnements suivent ce cycle de vie :

| État | Comportement |
| --- | --- |
| **Créé** | Fourni lorsqu'une interaction spécifie `environment: "remote"` ou un objet de configuration. |
| **Actif** | S'exécuter pendant qu'une interaction est en cours. |
| **Inactif** | Instantané automatique et arrêt après 15 minutes d'inactivité. |
| **Hors connexion** | Conservées pendant sept jours après la dernière activité. Vous pouvez la reprendre en transmettant son ID. |
| **Supprimé** | Supprimés automatiquement du système une fois le délai de conservation de sept jours expiré ou en cas de suppression manuelle. |

## API Environments

Vous pouvez utiliser l'API Environments pour gérer les sessions de bac à sable de manière programmatique.
L'énumération des environnements vous permet de découvrir les ID de session actifs et de récupérer l'état si une connexion client se termine lors d'une tâche de longue durée. Vous pouvez également inspecter les métadonnées de session et supprimer explicitement les environnements à la fin des workflows au lieu d'attendre l'expiration automatique de la durée de vie.

### Répertorier les environnements

Répertoriez les environnements actifs appartenant à votre projet. Utilisez les paramètres de pagination pour contrôler la taille de lot des réponses.

### Python

```
from google import genai

client = genai.Client()

response = client.environments.list(page_size=10)
for env in response.environments:
    print(f"Environment ID: {env.id}, Status: {env.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.list({ page_size: 10 });
for (const env of response.environments) {
    console.log(`Environment ID: ${env.id}, Status: ${env.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.environments.Environment;
import com.google.genai.gaos.models.environments.ListEnvironmentsResponse;
import java.util.List;

Client client = new Client();

ListEnvironmentsResponse response = client.environments.listEnvironments()
    .pageSize(10)
    .call()
    .listEnvironmentsResponse()
    .get();

for (Environment env : response.environments().orElse(List.of())) {
    System.out.println("Environment ID: " + env.id().orElse("") + ", Status: " + env.status().orElse(null));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Environments.ListEnvironments(ctx, operations.ListEnvironmentsRequest{
        PageSize: genai.Ptr(10),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.ListEnvironmentsResponse != nil {
        for _, env := range res.ListEnvironmentsResponse.Environments {
            fmt.Printf("Environment ID: %s, Status: %v\n", env.ID, env.Status)
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments?pageSize=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

La réponse ressemble à ce qui suit :

```
{
  "environments": [
    {
      "id": "140128b2a13c12c00a5a0d8cf7af9469",
      "status": "active"
    },
    {
      "id": "362b738275a1d74af6f1c62bc050da73",
      "status": "active"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

### Obtenir un environnement

Récupérez les métadonnées et les informations de configuration d'un environnement spécifique à l'aide de son nom de ressource.

### Python

```
from google import genai

client = genai.Client()

env = client.environments.get(id="YOUR_ENVIRONMENT_ID")
print(f"Environment ID: {env.id}, Status: {env.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const env = await client.environments.get("YOUR_ENVIRONMENT_ID");
console.log(`Environment ID: ${env.id}, Status: ${env.status}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.environments.Environment;

Client client = new Client();

Environment env = client.environments.getEnvironment("YOUR_ENVIRONMENT_ID").environment().get();
System.out.println("Environment ID: " + env.id().orElse("") + ", Status: " + env.status().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Environments.GetEnvironment(ctx, operations.GetEnvironmentRequest{
        ID: "YOUR_ENVIRONMENT_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    env := res.Environment
    fmt.Printf("Environment ID: %s, Status: %v\n", env.ID, env.Status)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

La réponse ressemble à ce qui suit :

```
{
  "id": "140128b2a13c12c00a5a0d8cf7af9469",
  "status": "active",
  "sources": [
    {
      "type": "repository",
      "source": "https://github.com/octocat/Spoon-Knife",
      "target": "/workspace/spoon-knife"
    }
  ],
  "network": {
    "allowlist": [
      {
        "domain": "api.github.com"
      },
      {
        "domain": "github.com"
      }
    ]
  }
}
```

### Supprimer un environnement

Mettez fin à un environnement et supprimez-le explicitement pour nettoyer les ressources du bac à sable une fois vos tâches ou pipelines terminés.

### Python

```
from google import genai

client = genai.Client()

client.environments.delete(id="YOUR_ENVIRONMENT_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

await client.environments.delete("YOUR_ENVIRONMENT_ID");
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

client.environments.deleteEnvironment("YOUR_ENVIRONMENT_ID");
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Environments.DeleteEnvironment(ctx, operations.DeleteEnvironmentRequest{
        ID: "YOUR_ENVIRONMENT_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Gérer les fichiers dans l'environnement

L'agent crée et modifie des fichiers dans le bac à sable lors de l'exécution. Vous pouvez parcourir le contenu des répertoires, obtenir les métadonnées des fichiers, télécharger des fichiers individuels ou des répertoires entiers sous forme d'archives TAR, et importer des fichiers ou extraire des archives directement dans l'environnement. Le stockage dans les environnements de bac à sable est soumis à des limites d'utilisation équitable.

### Lister les fichiers d'un répertoire

Affichez le contenu d'un répertoire dans l'environnement. Par défaut, la liste affiche le répertoire racine.

#### Paramètres de requête

| Paramètre | Type | Description |
| --- | --- | --- |
| `recursive` | booléen | Lorsque la valeur est `true`, liste tous les fichiers et répertoires de manière récursive. Valeur par défaut : `false`. |

### Python

```
from google import genai

client = genai.Client()

# List root directory
response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="",
)
for file in response.files:
    print(f"{file.name} ({file.type}) - {file.path}")

# List a subdirectory recursively
response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="src",
    recursive=True,
)
for file in response.files:
    print(f"{file.name} ({file.type}) - {file.path}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// List root directory
const response = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "",
});
for (const file of response.files) {
    console.log(`${file.name} (${file.type}) - ${file.path}`);
}

// List a subdirectory recursively
const srcResponse = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src",
    recursive: true,
});
for (const file of srcResponse.files) {
    console.log(`${file.name} (${file.type}) - ${file.path}`);
}
```

### REST

```
# List root directory
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# List a subdirectory
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# List all files recursively
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?recursive=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

La réponse renvoie un tableau `files` avec les métadonnées de chaque entrée :

```
{
  "files": [
    {
      "name": "config",
      "path": "config",
      "type": "DIRECTORY",
      "created": "2026-08-12T07:44:18Z",
      "modified": "2026-08-12T07:44:18Z"
    },
    {
      "name": "main.py",
      "path": "src/main.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python; charset=utf-8",
      "created": "2026-08-12T07:44:20Z",
      "modified": "2026-08-12T07:44:20Z"
    }
  ]
}
```

#### Champs de saisie de fichier

| Champ | Type | Description |
| --- | --- | --- |
| `name` | chaîne | Nom du fichier ou du répertoire. |
| `path` | chaîne | Chemin d'accès complet par rapport à la racine de l'environnement. |
| `type` | chaîne | `FILE` ou `DIRECTORY`. |
| `size_bytes` | chaîne | Taille du fichier en octets (fichiers uniquement). |
| `mime_type` | chaîne | Type MIME (fichiers uniquement). |
| `created` | chaîne | Code temporel de création au format ISO 8601. |
| `modified` | chaîne | Code temporel de la dernière modification au format ISO 8601. |

### Obtenir les métadonnées d'un fichier

Obtenez les métadonnées d'un fichier spécifique par chemin d'accès.

### Python

```
from google import genai

client = genai.Client()

response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="src/main.py",
)
file = response.files[0]
print(f"Name: {file.name}, Size: {file.size_bytes} bytes, Type: {file.mime_type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src/main.py",
});
const file = response.files[0];
console.log(`Name: ${file.name}, Size: ${file.size_bytes} bytes, Type: ${file.mime_type}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src/main.py" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

La réponse renvoie les métadonnées du fichier encapsulées dans un tableau `files` :

```
{
  "files": [
    {
      "name": "main.py",
      "path": "src/main.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python; charset=utf-8",
      "created": "2026-08-12T07:44:20Z",
      "modified": "2026-08-12T07:44:20Z"
    }
  ]
}
```

Si le fichier n'existe pas, l'API renvoie une erreur `404` :

```
{
  "error": {
    "message": "Path 'nonexistent.txt' not found in environment 'ENV_ID'.",
    "code": "not_found"
  }
}
```

### Télécharger un seul fichier

Téléchargez le contenu d'un fichier spécifique. Dans les SDK, utilisez la méthode `download()`. Dans les requêtes REST, ajoutez le paramètre de requête `?alt=media` au chemin d'accès au fichier. Le serveur répond avec `200 OK` et diffuse le contenu brut du fichier.

### Python

```
from google import genai

client = genai.Client()

content = client.environments.files.download(
    environment="YOUR_ENVIRONMENT_ID",
    path="src/main.py",
)

with open("main.py", "wb") as f:
    f.write(content)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const bytes = await client.environments.files.download({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src/main.py",
});

fs.writeFileSync("main.py", Buffer.from(bytes));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src/main.py?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o main.py
```

### Télécharger un répertoire en tant qu'archive tar

Téléchargez un répertoire entier sous forme d'archive tar en demandant le chemin d'accès au répertoire avec `?alt=media`. Cela renvoie un fichier tar POSIX (non compressé). Utilisez `recursive=true` pour inclure les sous-répertoires imbriqués.

### Python

```
import tarfile
from google import genai

client = genai.Client()

# Download a subdirectory archive
archive = client.environments.files.download(
    environment="YOUR_ENVIRONMENT_ID",
    path="src",
)

with open("src.tar", "wb") as f:
    f.write(archive)

with tarfile.open("src.tar") as tar:
    tar.extractall(path="./extracted")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { execSync } from "child_process";
import * as fs from "fs";

const client = new GoogleGenAI({});

// Download a subdirectory archive
const bytes = await client.environments.files.download({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src",
});

fs.writeFileSync("src.tar", Buffer.from(bytes));
execSync("tar -xf src.tar -C ./extracted");
```

### REST

```
# Download a subdirectory (top-level files only)
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o src.tar

# Download a subdirectory recursively (includes nested directories)
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/config?alt=media&recursive=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o config.tar

# Download root directory
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o snapshot.tar

# Extract the archive
tar xf snapshot.tar -C ./extracted
```

#### Matrice de comportement

La matrice de comportement suivante récapitule la réponse attendue et le comportement d'archivage pour les points de terminaison de fichiers et de répertoires, les méthodes HTTP et les paramètres de requête :

| Requête | `alt` | `recursive` | `extract` | `overwrite` | Réponse |
| --- | --- | --- | --- | --- | --- |
| `GET /files` | (aucun) | (aucun) | - | - | Liste JSON du répertoire racine |
| `GET /files/{path}` (fichier) | (aucun) | - | - | - | Métadonnées JSON du fichier |
| `GET /files/{path}` (dir) | (aucun) | `false` | - | - | Liste JSON des enfants immédiats |
| `GET /files/{path}` (dir) | (aucun) | `true` | - | - | Liste JSON de tous les descendants |
| `GET /files/{path}?alt=media` (fichier) | `media` | - | - | - | Contenu brut du fichier |
| `GET /files/{path}?alt=media` (dir) | `media` | `false` | - | - | Archive tar des fichiers immédiats dans le répertoire |
| `GET /files/{path}?alt=media` (dir) | `media` | `true` | - | - | Archive TAR de tous les fichiers de manière récursive |
| `GET /files?alt=media` | `media` | `false` | - | - | Archive TAR des fichiers de niveau racine uniquement |
| `PUT /files/{path}` (fichier) | - | - | `false` | `false` | Écrit le fichier au chemin d'accès. Renvoie `409 Conflict` s'il existe déjà |
| `PUT /files/{path}?overwrite=true` | - | - | `false` | `true` | Écrit ou écrase le fichier au chemin d'accès |
| `PUT /files/{path}?extract=true` | - | - | `true` | `false` | Décompresse l'archive dans le répertoire de destination. Renvoie `409 Conflict` si un fichier cible existe. |
| `PUT /files/{path}?extract=true&overwrite=true` | - | - | `true` | `true` | Décompresse l'archive en remplaçant les fichiers existants |

### Importer des fichiers dans l'environnement

Importez des fichiers individuels ou des archives de répertoire directement dans un bac à sable d'environnement existant à l'aide de HTTP `PUT`. Les répertoires parents sont créés automatiquement s'ils n'existent pas. Le stockage dans les environnements est soumis à des limites d'utilisation équitable.

#### Importer un seul fichier

### Python

```
from google import genai

client = genai.Client()

with open("local_file.txt", "rb") as f:
    result = client.environments.files.upload(
        environment="YOUR_ENVIRONMENT_ID",
        path="workspace/data/file.txt",
        file=f,
        mime_type="text/plain",
        overwrite=True,
    )

file = result.files[0]
print(f"Uploaded: {file.name} ({file.size_bytes} bytes)")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const content = fs.readFileSync("local_file.txt");
const result = await client.environments.files.upload({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "workspace/data/file.txt",
    file: content,
    mime_type: "text/plain",
    overwrite: true,
});

const file = result.files[0];
console.log(`Uploaded: ${file.name} (${file.size_bytes} bytes)`);
```

### REST

```
curl -X PUT "https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/data/file.txt" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: text/plain" \
  --data-binary @local_file.txt
```

La réponse renvoie les métadonnées du fichier importé, encapsulées dans un tableau `files` pour assurer la cohérence avec les points de terminaison list et get :

```
{
  "files": [
    {
      "name": "file.txt",
      "path": "workspace/data/file.txt",
      "type": "FILE",
      "size_bytes": "1024",
      "mime_type": "text/plain"
    }
  ]
}
```

#### Importer et extraire une archive de répertoire

Pour amorcer une codebase ou une structure de répertoire entières en une seule requête, importez une archive `.tar` ou `.tar.gz` avec `extract=true`.

### Python

```
from google import genai

client = genai.Client()

with open("source.tar.gz", "rb") as f:
    result = client.environments.files.upload(
        environment="YOUR_ENVIRONMENT_ID",
        path="workspace/src/",
        file=f,
        extract=True,
    )

for entry in result.files:
    print(f"Extracted: {entry.path}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const archive = fs.readFileSync("source.tar.gz");
const result = await client.environments.files.upload({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "workspace/src/",
    file: archive,
    extract: true,
});

for (const entry of result.files) {
    console.log(`Extracted: ${entry.path}`);
}
```

### REST

```
curl -X PUT "https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/src/?extract=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/x-tar" \
  --data-binary @source.tar.gz
```

La réponse liste tous les fichiers écrits par l'archive :

```
{
  "files": [
    {
      "name": "app.py",
      "path": "workspace/src/app.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python"
    },
    {
      "name": "requirements.txt",
      "path": "workspace/src/requirements.txt",
      "type": "FILE",
      "size_bytes": "17",
      "mime_type": "text/plain"
    }
  ]
}
```

#### Importer des fichiers volumineux avec une session avec reprise

Pour les charges utiles volumineuses ou lorsque vous importez des données sur une connexion peu fiable, utilisez une session avec reprise au lieu d'envoyer l'intégralité du corps dans une seule requête. Une importation avec reprise divise le transfert en blocs qui peuvent être réessayés individuellement. Ainsi, en cas d'échec en cours de transfert, vous n'avez pas besoin de tout recommencer.

Commencez par lancer la session avec `uploadType=resumable`. Envoyez un corps vide et utilisez les en-têtes `X-Upload-Content-Type` et `X-Upload-Content-Length` pour déclarer le type de contenu et la taille totale de la charge utile que vous souhaitez importer :

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable HTTP/1.1
Host: generativelanguage.googleapis.com
X-Upload-Content-Type: application/octet-stream
X-Upload-Content-Length: 20971520
Content-Length: 0
x-goog-api-key: $GEMINI_API_KEY
```

La réponse contient l'URL de la session dans l'en-tête `Location`. Cette URL contient déjà un `upload_id`. La clé API n'est donc pas nécessaire :

```
HTTP/1.1 200 OK
Location: https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY
Content-Length: 0
```

Importez la charge utile à cette URL par blocs. Chaque bloc déclare sa plage d'octets et la taille totale avec un en-tête `Content-Range` :

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 0-10485759/20971520
Content-Length: 10485760

<10 MB binary payload>
```

Chaque bloc, à l'exception du dernier, renvoie `308 Resume Incomplete`. L'en-tête `Range` indique le nombre d'octets validés par le serveur, à partir duquel vous pouvez reprendre l'importation en cas d'échec d'un bloc :

```
HTTP/1.1 308 Resume Incomplete
Range: bytes=0-10485759
Content-Length: 0
```

Envoyez les autres blocs de la même manière :

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 10485760-20971519/20971520
Content-Length: 10485760

<remaining 10 MB binary payload>
```

Le dernier bloc termine l'importation et renvoie les métadonnées du fichier, dans la même enveloppe `files` qu'une importation en une seule fois :

```
{
  "files": [
    {
      "name": "large_dataset.bin",
      "path": "workspace/data/large_dataset.bin",
      "type": "FILE",
      "size_bytes": "20971520",
      "mime_type": "application/octet-stream"
    }
  ]
}
```

Les sessions réactivables fonctionnent également avec `extract` et `overwrite`. Définissez ces paramètres de requête sur la requête d'origine, et non sur les blocs individuels.

#### Protection contre l'écrasement

La valeur par défaut de `overwrite` est `false`. Si le chemin de destination existe déjà, la requête renvoie une erreur `409 Conflict` et rien n'est écrit :

```
{
  "error": {
    "message": "Requested entity already exists",
    "code": "aborted"
  }
}
```

Pour remplacer un fichier ou un répertoire existant, définissez `overwrite=true` (ou ajoutez `?overwrite=true` dans REST). Avec `extract=true`, la vérification des conflits s'applique à chaque fichier de l'archive. La requête échoue donc si un fichier cible existe.

### Télécharger l'instantané complet (obsolète)

Pour migrer le code existant vers l'API Environment Files :

- **Python** : remplacez les anciennes requêtes de téléchargement de fichiers par :

  ```
  archive = client.environments.files.download(
      environment="YOUR_ENVIRONMENT_ID",
      path="workspace",
  )
  with open("snapshot.tar", "wb") as f:
      f.write(archive)
  ```
- **JavaScript** : remplacez les anciennes requêtes de téléchargement de fichiers par :

  ```
  const bytes = await client.environments.files.download({
      environment: "YOUR_ENVIRONMENT_ID",
      path: "workspace",
  });
  fs.writeFileSync("snapshot.tar", Buffer.from(bytes));
  ```
- **REST** : remplacez `GET /v1beta/files/environment-$ENV_ID:download?alt=media` par :

  ```
  curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?alt=media" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -o snapshot.tar
  ```

## Tarifs et ressources

Chaque environnement s'exécute avec des allocations de ressources fixes :

| Ressource | Valeur |
| --- | --- |
| **Processeur** | 4 cœurs |
| **Mémoire** | 16 Go |

Le calcul de l'environnement (CPU, mémoire, exécution du bac à sable) n'est **pas facturé** pendant la période de preview. Pour en savoir plus sur les coûts des jetons d'agent, consultez la page [Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#pricing-for-agents).

## Limites

- **État de l'aperçu** : les environnements et les agents gérés sont en version bêta. Les fonctionnalités et les schémas peuvent changer.
- **Taille des sources intégrées** : les sources intégrées sont limitées à 1 Mo par fichier et à 2 Mo au total pour tous les fichiers.
- **Taille de la source** : les dépôts Git sont limités à 500 Mo et les dépôts Cloud Storage à 2 Go.
- **Démarrage de l'environnement** : le provisionnement d'un nouvel environnement prend environ cinq secondes. Les dépôts sources volumineux peuvent augmenter ce délai.
- **Expiration de l'environnement** : les environnements hors connexion inactifs sont conservés pendant sept jours avant d'expirer à l'aide du nettoyage automatique de la valeur TTL. Si vous transmettez un ID d'environnement expiré ou non valide, une erreur `404 Not Found` s'affiche.
- **Fichiers compatibles** : l'agent est actuellement limité à la lecture des fichiers texte et image. La prise en charge des fichiers binaires n'est pas encore disponible.
- **Pas de montage à partir de la racine** : vous ne pouvez pas définir la racine (`/`) comme cible lorsque vous ajoutez une source personnalisée. Vous devez toujours spécifier un sous-répertoire.

## Étape suivante

- [Présentation des agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr) : découvrez les concepts de base des agents gérés.
- [Guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr) : commencez à créer des conversations multitours et du streaming.
- [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr) : découvrez les fonctionnalités, les outils, la sélection de modèles et la tarification de l'agent par défaut.
- [Créer des agents personnalisés](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr) : définissez vos propres agents à l'aide de `AGENTS.md` et `SKILL.md`.
- [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fr) : appliquez des garde-fous de sécurité et exécutez des validations d'effets secondaires dans le bac à sable.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
