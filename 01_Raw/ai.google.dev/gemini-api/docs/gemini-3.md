---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=fr
fetched_at: 2026-10-05T06:44:19.279332+00:00
title: "Guide du d\u00e9veloppeur Gemini\u00a03 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)

Envoyer des commentaires

# Guide du développeur Gemini 3

Gemini 3 est notre famille de modèles la plus intelligente à ce jour. Elle repose sur une technologie de raisonnement de pointe. Il est conçu pour donner vie à toutes vos idées en maîtrisant les workflows agentiques, le codage autonome et les tâches multimodales complexes.
Ce guide présente les principales fonctionnalités de la famille de modèles Gemini 3 et explique comment en tirer le meilleur parti.

Découvrez notre [collection d'applications Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=fr) pour voir comment le modèle gère le raisonnement avancé, le codage autonome et les tâches multimodales complexes.

Commencez avec quelques lignes de code :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(
            InteractionsInput.of(
                "Find the race condition in this multi-threaded C++ snippet: [code here]"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Find the race condition in this multi-threaded C++ snippet: [code here]"),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Découvrez la gamme Gemini 3

Gemini 3.1 Pro est idéal pour les tâches complexes qui nécessitent une vaste connaissance du monde et un raisonnement avancé dans plusieurs modalités.

Gemini 3 Flash est notre dernier modèle de la série 3. Il offre une intelligence de niveau Pro avec la rapidité et le prix de Flash.

Nano Banana Pro (également appelé Gemini 3 Pro Image) est notre modèle de génération d'images de la plus haute qualité. Nano Banana 2 (également appelé Gemini 3.1 Flash Image) est son équivalent à prix plus abordable, qui permet de générer des images en grand volume et de manière très efficace.

Gemini 3.1 Flash-Lite est notre modèle de référence conçu pour les tâches à haut volume et économiques.

Tous les modèles Gemini 3 sont actuellement en preview.

| ID du modèle | Fenêtre de contexte (entrée / sortie) | Date limite des connaissances | Tarification (entrée / sortie)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 M / 64 k | Janv. 2025 | 0,25 $ (texte, image, vidéo), 0,50 $ (audio) / 1,50 $ |
| **gemini-3.1-flash-image-preview** | 128 000 / 32 000 | Janv. 2025 | 0,25 $ (entrée de texte) / 0,067 $ (sortie d'image)\*\* |
| **gemini-3.1-pro-preview** | 1 M / 64 k | Janv. 2025 | 2 $ / 12 $ (<200 000 jetons)   4 $ / 18 $ (>200 000 jetons) |
| **gemini-3-flash-preview** | 1 M / 64 k | Janv. 2025 | 0,50 $ / 3 $ |
| **gemini-3-pro-image-preview** | 65 000 / 32 000 | Janv. 2025 | 2 $ (entrée de texte) / 0,134 $ (sortie d'image)\*\* |

*\* Sauf indication contraire, les tarifs s'entendent pour 1 million de jetons.*
*\*\* Le prix des images varie en fonction de leur résolution. Pour en savoir plus, consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).*

Pour en savoir plus sur les limites, les tarifs et d'autres informations, consultez la [page des modèles](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr).

## Nouvelles fonctionnalités de l'API dans Gemini 3

Gemini 3 introduit de nouveaux paramètres conçus pour offrir aux développeurs un meilleur contrôle de la latence, des coûts et de la fidélité multimodale.

### Niveau de réflexion

Les modèles de la famille Gemini 3 utilisent par défaut la pensée dynamique pour raisonner à partir des requêtes. Vous pouvez utiliser le paramètre `thinking_level`, qui contrôle la profondeur **maximale** du processus de raisonnement interne du modèle avant qu'il ne produise une réponse. Gemini 3 traite ces niveaux comme des allocations relatives pour la réflexion plutôt que comme des garanties strictes de jetons.

Si `thinking_level` n'est pas spécifié, Gemini 3 utilisera `high` par défaut. Pour obtenir des réponses plus rapides et à faible latence lorsque le raisonnement complexe n'est pas nécessaire, vous pouvez limiter le niveau de réflexion du modèle à `low`.

| Niveau de réflexion | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Description |
| --- | --- | --- | --- | --- |
| **`minimal`** | Not supported | Compatible (par défaut) | Compatible | Correspond au paramètre "Sans réflexion" pour la plupart des requêtes. Le modèle peut réfléchir de manière très minimale pour les tâches de codage complexes. Minimise la latence pour les applications de chat ou à haut débit. Notez que `minimal` ne garantit pas que la réflexion est désactivée. |
| **`low`** | Compatible | Compatible | Compatible | Minimise la latence et les coûts. Convient mieux aux applications de suivi d'instructions simples, de chat ou à haut débit. |
| **`medium`** | Compatible | Compatible | Compatible | Réflexion équilibrée pour la plupart des tâches. |
| **`high`** | Compatible (par défaut, dynamique) | Compatible (dynamique) | Compatible (par défaut, dynamique) | Maximise la profondeur du raisonnement. Le modèle peut mettre beaucoup plus de temps à générer le premier jeton de sortie (autre que le jeton de réflexion), mais la sortie sera plus soigneusement raisonnée. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("How does AI work?"))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.LOW)
                .build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("How does AI work?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
            },
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Température

Pour tous les modèles Gemini 3, nous vous recommandons vivement de conserver la valeur par défaut du paramètre de température, à savoir `1.0`.

Alors que les modèles précédents bénéficiaient souvent d'un réglage de la température pour contrôler la créativité par rapport au déterminisme, les capacités de raisonnement de Gemini 3 sont optimisées pour le paramètre par défaut. Si vous modifiez la température (en la définissant sur une valeur inférieure à 1,0), vous risquez d'obtenir un comportement inattendu, comme une boucle ou une dégradation des performances, en particulier pour les tâches mathématiques ou de raisonnement complexes.

### Signatures de réflexion

Les modèles Gemini 3 utilisent des signatures de pensée pour conserver le contexte de raisonnement lors des appels d'API. Ces signatures sont des représentations chiffrées du processus de réflexion interne du modèle.

- **Mode avec état (recommandé)** : lorsque vous utilisez l'API Interactions en mode avec état (en fournissant `previous_interaction_id`), le serveur gère automatiquement l'historique des conversations et les signatures de pensée.
- **Mode sans état** : si vous gérez manuellement l'historique des conversations, vous devez inclure des blocs de réflexion avec leurs signatures dans les requêtes suivantes pour valider l'authenticité.

Pour en savoir plus, consultez la page [Signatures de pensée](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).

### Sorties structurées avec des outils

Les modèles Gemini 3 vous permettent de combiner les [sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr) avec des outils intégrés, y compris l'[ancrage avec la Recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr), le [contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr), l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) et l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("winner", Map.of("type", "string", "description", "The name of the winner."));
properties.put(
    "final_match_score", Map.of("type", "string", "description", "The final match score."));
properties.put(
    "scorers",
    Map.of(
        "type", "array",
        "items", Map.of("type", "string"),
        "description", "The name of the scorer."));

Map<String, Object> schema = new HashMap<>();
schema.put("type", "object");
schema.put("properties", properties);
schema.put("required", Arrays.asList("winner", "final_match_score", "scorers"));

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("Search for all details for the latest Euro."))
        .tools(Arrays.asList(GoogleSearch.builder().build(), URLContext.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    TextResponseFormat.builder()
                        .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                        .schema(schema)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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

    schema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "winner": map[string]any{
                "type":        "string",
                "description": "The name of the winner.",
            },
            "final_match_score": map[string]any{
                "type":        "string",
                "description": "The final match score.",
            },
            "scorers": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "string"},
                "description": "The name of the scorer.",
            },
        },
        "required": []string{"winner", "final_match_score", "scorers"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Search for all details for the latest Euro."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
                interactions.NewTool(interactions.URLContext{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeType("application/json").ToPointer(),
                    Schema:   schema,
                }),
            )),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Génération d'images

Gemini 3.1 Flash Image et Gemini 3 Pro Image vous permettent de générer et de modifier des images à partir de requêtes textuelles. Il utilise le raisonnement pour "réfléchir" à une requête et peut récupérer des données en temps réel (comme des prévisions météo ou des graphiques boursiers) avant d'utiliser l'ancrage [Recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) pour générer des images haute fidélité.

**Nouvelles fonctionnalités et améliorations :**

- **Rendu 4K et de texte** : générez du texte et des schémas nets et lisibles avec des résolutions allant jusqu'à 2K et 4K.
- **Génération ancrée** : utilisez l'outil `google_search` pour vérifier les faits et générer des images basées sur des informations réelles. L'ancrage avec la recherche d'*images* Google est disponible pour Gemini 3.1 Flash Image.
- **Retouche conversationnelle** : retouche d'images multitour en demandant simplement les changements à effectuer (par exemple, "Remplace l'arrière-plan par un coucher de soleil"). Ce workflow s'appuie sur les **signatures de pensée** pour préserver le contexte visuel entre les tours de conversation.

Pour en savoir plus sur les formats, les workflows de modification et les options de configuration, consultez le [guide de génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageResponseFormat;
import com.google.genai.gaos.models.interactions.ImageResponseFormatAspectRatio;
import com.google.genai.gaos.models.interactions.ImageResponseFormatImageSize;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.Optional;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-pro-image-preview"))
        .input(InteractionsInput.of("Generate an infographic of the current weather in Tokyo."))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    ImageResponseFormat.builder()
                        .aspectRatio(ImageResponseFormatAspectRatio.ONE_HUNDRED_AND_SIXTY_NINE)
                        .imageSize(ImageResponseFormatImageSize.FOUR_K)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

Optional<ImageContent> generatedImage = interaction.outputImage();
if (generatedImage.isPresent() && generatedImage.get().data().isPresent()) {
  byte[] imageBytes = Base64.getDecoder().decode(generatedImage.get().data().get());
  Files.write(Paths.get("weather_tokyo.png"), imageBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

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
            Model: interactions.Model("gemini-3-pro-image-preview"),
            Input: interactions.NewInteractionsInput("Generate an infographic of the current weather in Tokyo."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.ImageResponseFormat{
                    AspectRatio: interactions.ImageResponseFormatAspectRatioOneHundredAndSixtyNine.ToPointer(),
                    ImageSize:   interactions.ImageResponseFormatImageSize("4K").ToPointer(),
                }),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if generatedImage := res.Interaction.GetOutputImage(); generatedImage != nil && generatedImage.Data != nil {
        imageBytes, err := base64.StdEncoding.DecodeString(*generatedImage.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("weather_tokyo.png", imageBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Exemple de réponse**

![Météo Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=fr)

### Exécution de code avec des images

Gemini 3 Flash peut traiter la vision comme une investigation active, et pas seulement comme un coup d'œil statique. En combinant le raisonnement à l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr), le modèle élabore un plan, puis écrit et exécute du code Python pour faire un zoom avant, recadrer, annoter ou manipuler des images étape par étape afin d'ancrer visuellement ses réponses.

**Cas d'utilisation** :

- **Zoom et inspection** : le modèle détecte implicitement lorsque les détails sont trop petits (par exemple, pour lire une jauge ou un numéro de série éloignés) et écrit du code pour recadrer et réexaminer la zone à une résolution plus élevée.
- **Calculs et graphiques visuels** : le modèle peut effectuer des calculs en plusieurs étapes à l'aide de code (par exemple, en additionnant les lignes d'un reçu ou en générant un graphique Matplotlib à partir de données extraites).
- **Annotation d'images** : le modèle peut dessiner des flèches, des cadres de sélection ou d'autres annotations directement sur les images pour répondre à des questions spatiales comme "Où cet élément doit-il être placé ?".

Pour activer la pensée visuelle, configurez l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) en tant qu'outil. Le modèle utilisera automatiquement du code pour manipuler les images si nécessaire.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

URL url = new URL("https://goo.gle/instrument-img");
byte[] imageBytes;
try (InputStream is = url.openStream()) {
  imageBytes = is.readAllBytes();
}
String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .data(base64ImageData)
                        .build(),
                    TextContent.builder()
                        .text("Zoom into the expression pedals and tell me how many pedals are there?")
                        .build())))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep modelOutput = (ModelOutputStep) step;
    for (Content contentBlock : modelOutput.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println("Text: " + ((TextContent) contentBlock).text().orElse(""));
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().flatMap(args -> args.code()).ifPresent(code -> System.out.println("Code: " + code));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println("Output: " + resultStep.result().orElse(""));
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
    "io"
    "log"
    "net/http"

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

    httpRes, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer httpRes.Body.Close()
    imageBytes, err := io.ReadAll(httpRes.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    Data:     genai.Ptr(base64ImageData),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Zoom into the expression pedals and tell me how many pedals are there?",
                }),
            }),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if modelOutput := step.ModelOutputStep; modelOutput != nil {
            for _, contentBlock := range modelOutput.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println("Text:", textContent.Text)
                }
            }
        } else if callStep := step.CodeExecutionCallStep; callStep != nil {
            if callStep.Arguments.Code != nil {
                fmt.Println("Code:", *callStep.Arguments.Code)
            }
        } else if resultStep := step.CodeExecutionResultStep; resultStep != nil {
            fmt.Println("Output:", resultStep.Result)
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Pour en savoir plus sur l'exécution de code avec des images, consultez [Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr#images).

### Réponses de fonction multimodales

L'[appel de fonction multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#multimodal) permet aux utilisateurs d'obtenir des réponses de fonction contenant des objets multimodaux, ce qui améliore l'utilisation des capacités d'appel de fonction du modèle. L'appel de fonction standard n'accepte que les réponses de fonction textuelles :

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.FunctionResultSubcontent;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> itemProp = new HashMap<>();
itemProp.put("type", "string");
itemProp.put("description", "The name or description of the item ordered (e.g., 'instrument').");

Map<String, Object> properties = new HashMap<>();
properties.put("item_name", itemProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("item_name"));

Function getImageTool =
    Function.builder()
        .name("get_image")
        .description("Retrieves the image file reference for a specific order item.")
        .parameters(parameters)
        .build();

CreateModelInteraction req1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "Use the get_image tool to show me the instrument I ordered last month."))
        .tools(Arrays.asList(getImageTool))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(req1)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction1.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  System.out.println("Tool Call: " + fcStep.name().orElse(""));

  URL url = new URL("https://goo.gle/instrument-img");
  byte[] imageBytes;
  try (InputStream is = url.openStream()) {
    imageBytes = is.readAllBytes();
  }
  String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

  List<FunctionResultSubcontent> subcontents = new ArrayList<>();
  subcontents.add(TextContent.builder().text("instrument.jpg").build());
  subcontents.add(
      ImageContent.builder()
          .mimeType(ImageContentMimeType.IMAGE_JPEG)
          .data(base64ImageData)
          .build());

  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(FunctionResultStepResultUnion.of(subcontents))
          .build();

  CreateModelInteraction req2 =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(getImageTool))
          .previousInteractionId(interaction1.id().orElse(""))
          .build();

  Interaction interaction2 =
      client.interactions.create(CreateInteractionRequestBody.of(req2)).interaction().get();
  System.out.println("Final model response: " + interaction2.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    getImageTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_image"),
        Description: genai.Ptr("Retrieves the image file reference for a specific order item."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "item_name": map[string]any{
                    "type":        "string",
                    "description": "The name or description of the item ordered (e.g., 'instrument').",
                },
            },
            "required": []string{"item_name"},
        },
    })

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("Use the get_image tool to show me the instrument I ordered last month."),
            Tools: []interactions.Tool{getImageTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res1.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            fmt.Println("Tool Call:", fcStep.Name)

            httpRes, err := http.Get("https://goo.gle/instrument-img")
            if err != nil {
                log.Fatal(err)
            }
            defer httpRes.Body.Close()
            imageBytes, err := io.ReadAll(httpRes.Body)
            if err != nil {
                log.Fatal(err)
            }
            base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                    interactions.NewFunctionResultSubcontent(interactions.TextContent{
                        Text: "instrument.jpg",
                    }),
                    interactions.NewFunctionResultSubcontent(interactions.ImageContent{
                        MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                        Data:     genai.Ptr(base64ImageData),
                    }),
                }),
            })

            res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res1.Interaction.ID,
                    Tools:                 []interactions.Tool{getImageTool},
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if res2.Interaction.OutputText != nil {
                fmt.Println("Final model response:", *res2.Interaction.OutputText)
            }
            break
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Combiner des outils intégrés et l'appel de fonction

Gemini 3 permet d'utiliser des outils intégrés (comme la recherche Google, le contexte d'URL et [plus encore](https://ai.google.dev/gemini-api/docs/tools?hl=fr)) et des outils d'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) personnalisés dans le même appel d'API, ce qui permet des workflows plus complexes.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> cityProp = new HashMap<>();
cityProp.put("type", "string");
cityProp.put("description", "The city and state, e.g. Utqiaġvik, Alaska");

Map<String, Object> properties = new HashMap<>();
properties.put("city", cityProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("city"));

Function getWeather =
    Function.builder()
        .name("getWeather")
        .description("Gets the weather for a requested city.")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "What is the northernmost city in the United States? What's the weather like there today?"))
        .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(
              FunctionResultStepResultUnion.of(
                  "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"))
          .build();

  CreateModelInteraction finalRequest =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
          .previousInteractionId(interaction.id().orElse(""))
          .build();

  Interaction finalInteraction =
      client.interactions.create(CreateInteractionRequestBody.of(finalRequest)).interaction().get();
  System.out.println(finalInteraction.outputText().orElse(""));
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

    getWeather := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("getWeather"),
        Description: genai.Ptr("Gets the weather for a requested city."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "city": map[string]any{
                    "type":        "string",
                    "description": "The city and state, e.g. Utqiaġvik, Alaska",
                },
            },
            "required": []string{"city"},
        },
    })

    tools := []interactions.Tool{
        interactions.NewTool(interactions.GoogleSearch{}),
        getWeather,
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("What is the northernmost city in the United States? What's the weather like there today?"),
            Tools: tools,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion(`{"response": "Very cold. 22 degrees Fahrenheit."}`),
            })

            finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res.Interaction.ID,
                    Tools:                 tools,
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if finalRes.Interaction.OutputText != nil {
                fmt.Println(*finalRes.Interaction.OutputText)
            }
            break
        }
    }
}
```

## Migration depuis Gemini 2.5

Gemini 3 est notre famille de modèles la plus performante à ce jour. Elle offre une amélioration progressive par rapport à Gemini 2.5. Lorsque vous migrez, tenez compte des points suivants :

- **Raisonnement** : si vous utilisiez auparavant le prompt engineering complexe (comme la chaîne de pensée) pour forcer Gemini 2.5 à raisonner, essayez Gemini 3 avec `thinking_level: "high"` et des prompts simplifiés.
- **Paramètres de température** : si votre code existant définit explicitement la température (en particulier sur des valeurs basses pour des résultats déterministes), nous vous recommandons de supprimer ce paramètre et d'utiliser la valeur par défaut de Gemini 3 (1.0) pour éviter d'éventuels problèmes de boucle ou une dégradation des performances pour les tâches complexes.
- **Compréhension des PDF et des documents** : si vous vous êtes appuyé sur un comportement spécifique pour l'analyse des documents denses, testez le nouveau paramètre `media_resolution_high` pour vous assurer de la précision continue.
- **Consommation de jetons** : la migration vers les paramètres par défaut de Gemini 3 peut **augmenter** l'utilisation de jetons pour les PDF, mais la **diminuer** pour les vidéos. Si les requêtes dépassent désormais la fenêtre de contexte en raison de résolutions par défaut plus élevées, nous vous recommandons de réduire explicitement la résolution du contenu multimédia.
- **Segmentation d'images** : les fonctionnalités de segmentation d'images (qui renvoient des masques au niveau des pixels pour les objets) ne sont pas disponibles dans Gemini 3 Pro ni Gemini 3 Flash. Pour les charges de travail nécessitant une segmentation d'image intégrée, nous vous recommandons de continuer à utiliser Gemini 2.5 Flash avec la fonctionnalité de réflexion désactivée.
- **Utilisation de l'ordinateur** : Gemini 3 Pro et Gemini 3 Flash sont compatibles avec l'[utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr). Contrairement à la série 2.5, vous n'avez pas besoin d'utiliser un modèle distinct pour accéder à l'outil Utilisation de l'ordinateur.
- **Compatibilité avec les outils** : [la combinaison d'outils intégrés et de l'appel de fonction](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr) est désormais compatible avec les modèles Gemini 3. L'[ancrage Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr) est désormais également compatible avec les modèles Gemini 3.

## Compatibilité avec OpenAI

Pour les utilisateurs qui utilisent la [couche de compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr), les paramètres standards (`reasoning_effort` d'OpenAI) sont automatiquement mappés sur les équivalents Gemini (`thinking_level`).

## Bonnes pratiques concernant les prompts

Gemini 3 est un modèle de raisonnement, ce qui modifie la façon dont vous devez formuler vos requêtes.

- **Instructions précises** : soyez concis dans vos requêtes. Gemini 3 répond mieux aux instructions directes et claires. Il peut suranalyser les techniques de prompt engineering verbeuses ou trop complexes utilisées pour les anciens modèles.
- **Niveau de détail des réponses** : par défaut, Gemini 3 est moins bavard et préfère fournir des réponses directes et efficaces. Si votre cas d'utilisation nécessite un persona plus conversationnel ou "bavard", vous devez orienter explicitement le modèle dans l'invite (par exemple, "Explique cela comme un assistant amical et bavard").
- **Gestion du contexte** : lorsque vous travaillez avec de grands ensembles de données (par exemple, des livres entiers, des bases de code ou de longues vidéos), placez vos instructions ou questions spécifiques à la fin de la requête, après le contexte des données. Ancrez le raisonnement du modèle aux données fournies en commençant votre question par une expression telle que "Sur la base des informations précédentes…".

Pour en savoir plus sur les stratégies de conception de requêtes, consultez le [guide sur l'ingénierie des requêtes](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr).

## Questions fréquentes

1. **Quelle est la date limite des connaissances pour Gemini 3 ?** Les modèles Gemini 3 ont une limite de connaissances fixée à janvier 2025. Pour obtenir des informations plus récentes, utilisez l'outil [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=fr).
2. **Quelles sont les limites de la fenêtre de contexte ?** Les modèles Gemini 3 sont compatibles avec une fenêtre de contexte d'entrée d'un million de jetons et une sortie de 64 000 jetons maximum.
3. **Existe-t-il un forfait sans frais pour Gemini 3 ?** Gemini 3 Flash
   `gemini-3-flash-preview` dispose d'un niveau sans frais dans l'API Gemini. Vous pouvez essayer Gemini 3.1 Pro et 3 Flash sans frais dans Google AI Studio, mais aucun niveau sans frais n'est disponible pour `gemini-3.1-pro-preview` dans l'API Gemini.
4. **Mon ancien code `thinking_budget` fonctionnera-t-il toujours ?** Oui, `thinking_budget` est toujours compatible pour des raisons de rétrocompatibilité, mais nous vous recommandons de migrer vers `thinking_level` pour des performances plus prévisibles. N'utilisez pas les deux dans la même requête.
5. **Gemini 3 est-il compatible avec l'API Batch ?** Oui, Gemini 3 est compatible avec l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr).
6. **La mise en cache du contexte est-elle prise en charge ?** Oui, la [mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) est compatible avec Gemini 3.
7. **Quels outils sont compatibles avec Gemini 3 ?** Gemini 3 est compatible avec la [recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr), l'[ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr), la [recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr), l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) et le [contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr). Il est également compatible avec l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) standard pour vos propres outils personnalisés, et en [combinaison avec les outils intégrés](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).
8. **Qu'est-ce que `gemini-3.1-pro-preview-customtools` ?** Si vous utilisez `gemini-3.1-pro-preview` et que le modèle ignore vos outils personnalisés au profit des commandes Bash, essayez plutôt le modèle `gemini-3.1-pro-preview-customtools`.
   Pour en savoir plus, [cliquez ici][customtools-model].

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
