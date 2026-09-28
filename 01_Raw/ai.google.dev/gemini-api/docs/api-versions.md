---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=fr
fetched_at: 2026-09-28T06:21:56.907310+00:00
title: "Pr\u00e9sentation des versions de l'API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Documentation de référence de l'API](https://ai.google.dev/api?hl=fr)

Envoyer des commentaires

# Présentation des versions de l'API

Ce document présente les principales différences entre les versions `v1` et `v1beta` de l'API Gemini.

- **v1** : version stable de l'API. Les fonctionnalités de la version stable sont entièrement prises en charge pendant toute la durée de vie de la version majeure. En cas de modifications destructives, une nouvelle version majeure de l'API sera créée et la version existante sera obsolète après un délai raisonnable.
  Des modifications non destructives peuvent être apportées à l'API sans modifier la version majeure. L'**API Interactions** et ses principales fonctionnalités sont généralement disponibles dans `v1`.
- **v1beta** : cette version inclut des fonctionnalités et des capacités préliminaires en cours de développement. Bien que les fonctionnalités de `v1beta` puissent être modifiées à mesure que nous les affinons en fonction des commentaires, elles vous permettent d'essayer de nouvelles fonctionnalités avant qu'elles ne soient promues à la version stable.

## Compatibilité des fonctionnalités

Le tableau suivant détaille la disponibilité des fonctionnalités dans `v1` (disponibilité générale) et `v1beta` (bêta). Les outils et les fonctionnalités principales de l'API s'appliquent à l'API Interactions et à `generateContent`, sauf indication contraire :

| Fonctionnalité | v1 | v1beta |
| --- | --- | --- |
| **Fonctionnalités principales de l'API** |  |  |
| [API Interactions](https://ai.google.dev/gemini-api/docs/get-started?hl=fr) |  |  |
| [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) |  |  |
| [Sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr) |  |  |
| [Réflexion / Raisonnement](https://ai.google.dev/gemini-api/docs/thinking?hl=fr) |  |  |
| [Instructions système](https://ai.google.dev/gemini-api/docs/system-instructions?hl=fr) |  |  |
| [Sortie audio (configuration vocale)](https://ai.google.dev/gemini-api/docs/audio?hl=fr) |  |  |
| [Niveau de service (Priorité / Flex)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr) |  |  |
| **Outils** |  |  |
| [Outil d'exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) |  |  |
| [Ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) |  |  |
| [Ancrage Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr) |  |  |
| [Outil de contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) |  |  |
| [Outil de recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr) |  |  |
| [Outil d'utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr) |  |  |
| [Outil Serveurs MCP](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#mcp) |  |  |
| **API en temps réel** |  |  |
| [API Live (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=fr) |  |  |
| [API Live Music](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=fr) |  |  |
| [Jetons éphémères (API Live)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=fr) |  |  |
| **API de la plate-forme** |  |  |
| [API Models](https://ai.google.dev/gemini-api/docs/models?hl=fr) |  |  |
| [Route du service Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) |  |  |
| [Route de stockage de la recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr) |  |  |
| [API Agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr) |  |  |
| [API Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=fr) |  |  |
| [Mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) |  |  |

- : compatible

## Configurer la version de l'API dans un SDK

Les SDK de l'API Gemini sont définis par défaut sur `v1beta`, mais vous pouvez spécifier explicitement les versions en définissant la version de l'API, comme indiqué dans l'exemple de code suivant :

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            APIVersion: "v1",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.6-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works"),
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
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
  }'
```

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
