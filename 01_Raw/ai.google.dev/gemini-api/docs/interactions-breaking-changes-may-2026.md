---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=fr
fetched_at: 2026-09-07T05:41:07.508773+00:00
title: "Guide de migration des modifications destructives de l'API Interactions (mai\u00a02026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Guide de migration des modifications destructives de l'API Interactions (mai 2026)

L'API Interactions `v1beta` introduit des modifications incompatibles qui restructurent la forme de l'API pour prendre en charge de futures fonctionnalités telles que le pilotage en cours de vol et les appels d'outils asynchrones. Cette page explique ce qui change et fournit des exemples de code avant et après pour vous aider à migrer. Il existe deux catégories de modifications :

1. [**Schéma "Steps"**](#steps-schema) : un nouveau tableau `steps` remplace le tableau `outputs`, fournissant une chronologie structurée de chaque tour d'interaction.
2. [**Configuration du format de sortie**](#output-format-config) : un nouveau `response_format` polymorphe consolide tous les contrôles du format de sortie et supprime `response_mime_type`.

Suivez la procédure décrite dans [Migrer vers le nouveau schéma](#how-to-migrate) pour mettre à jour votre intégration.

## Modification principale : `outputs` vers `steps`

Le nouveau schéma remplace le tableau `outputs` par un tableau `steps`.

- **Ancien** : les réponses renvoyaient un tableau `outputs` plat contenant uniquement le contenu généré par le modèle.
- **Nouveau schéma** : les réponses renvoient un tableau `steps` contenant des étapes structurées avec des discriminateurs de type.

`POST /interactions` ne renvoie que les étapes de sortie. `GET /interactions/{id}` renvoie la chronologie complète des étapes, y compris l'étape initiale `user_input`.

### Entrée/Sortie de base (unaire)

#### Avant (ancienne version)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### Après (nouveau schéma)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### Appel de fonction

La structure de la requête reste inchangée, mais la réponse remplace le contenu `outputs` plat par des étapes structurées.

#### Avant (ancienne version)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling ${output.name} with ${JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### Après (nouveau schéma)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling ${step.name} with ${JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### Outils côté serveur

Les outils côté serveur (comme la recherche Google ou l'exécution de code) génèrent désormais des types d'étapes spécifiques dans le tableau `steps`. Alors que l'ancien schéma renvoyait ces opérations en tant que types de contenu spécifiques dans le tableau `outputs`, le nouveau schéma les déplace dans le tableau `steps`. Les exemples suivants utilisent la recherche Google.

#### Avant (ancienne version)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: ${output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: ${output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### Après (nouveau schéma)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result[0].search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: ${step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: ${step.result[0].search_suggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### Streaming

Le streaming expose de nouveaux types d'événements :

#### Nouveaux types d'événements

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Types d'événements obsolètes

Les anciens types d'événements suivants sont remplacés par les nouveaux événements listés ci-dessus :

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → remplacé par `interaction.in_progress`, `interaction.requires_action`, etc.

**Appels de fonction en streaming** : lorsque vous utilisez le streaming avec les appels de fonction, l'événement `step.start` fournit le nom de la fonction, et les événements `step.delta` transmettent les arguments sous forme de chaînes JSON partielles (à l'aide de `arguments_delta`). Vous devez cumuler ces deltas pour obtenir les arguments complets. Cela diffère des appels unaires où vous recevez l'objet d'appel de fonction complet en une seule fois.

#### Exemples

##### Avant (ancienne version)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### Après (nouveau schéma)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.event_type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.5-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.5-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### Historique des conversations sans état

Si vous gérez manuellement l'historique des conversations côté client (cas d'utilisation sans état), vous devez modifier la façon dont vous enchaînez les tours précédents.

- **Ancien** : les développeurs collectaient souvent le tableau `outputs` à partir des réponses et le renvoyaient dans le champ `input` au tour suivant.
- **Nouveau schéma** : vous devez maintenant collecter le tableau `steps` à partir de la réponse et le transmettre dans le champ `input` de la prochaine requête, en ajoutant votre nouveau tour d'utilisateur en tant qu'étape `user_input`.

## Modifications apportées à la configuration du format de sortie : `response_format`

La nouvelle API regroupe tous les contrôles de format de sortie dans un champ `response_format` polymorphe unifié. Cela centralise la configuration de la sortie au niveau supérieur et permet à `generation_config` de se concentrer sur le comportement du modèle (comme la température, top\_p et la réflexion).

### Principales modifications

- **L'API supprime `response_mime_type`.** Vous devez maintenant spécifier le type MIME par entrée de format dans `response_format`.
- **`response_format` est désormais un objet (ou un tableau) polymorphe.** Chaque entrée comporte un discriminant `type` (`text`, `audio`, `image`) et des champs spécifiques au type. Pour demander plusieurs modalités de sortie, transmettez un tableau d'entrées de format.
- **`image_config` passe de `generation_config` à `response_format`.**
  Vous pouvez désormais spécifier les paramètres de sortie des images, comme `aspect_ratio` et `image_size`, dans une entrée `response_format` avec `"type": "image"`.

### Sortie structurée (JSON)

Le nouveau schéma supprime le champ `response_mime_type`. Spécifiez plutôt le type MIME et le schéma JSON dans un objet `response_format` avec `"type": "text"`.

#### Avant (ancienne version)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### Après (nouveau schéma)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### Configuration des images

Le nouveau schéma supprime `image_config` de `generation_config`. Vous spécifiez désormais les paramètres de sortie d'image dans une entrée `response_format` avec `"type": "image"`.

#### Avant (ancienne version)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Après (nouveau schéma)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### Configuration audio

Le nouveau schéma remplace `response_modalities: ["audio"]` par une entrée `response_format` de `"type": "audio"`.

#### Avant (ancienne version)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    response_modalities: ['audio'],
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

#### Après (nouveau schéma)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    # response_modalities is removed — use response_format
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    // response_modalities is removed — use response_format
    response_format: {
        type: 'audio'
    },
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

Pour demander plusieurs modalités de sortie (par exemple, du texte et de l'audio ensemble), transmettez un tableau d'entrées de format à `response_format` au lieu d'un seul objet.

## Migrer vers le nouveau schéma

### Utilisateurs du SDK

Passez à la dernière version du SDK (Python ≥2.0.0, JavaScript ≥2.0.0). Le SDK vous inscrit automatiquement au nouveau schéma. Vous n'avez pas besoin de modifier le code, si ce n'est pour mettre à jour la façon dont vous lisez les réponses (voir les exemples ci-dessus). Notez que seul le nouveau schéma est compatible avec ces versions du SDK. Les anciennes versions du SDK (Python 1.x.x, JavaScript 1.x.x) continueront de fonctionner jusqu'à la suppression de l'ancien schéma le **8 juin 2026**.

### Utilisateurs de l'API REST

Ajoutez l'en-tête `Api-Revision: 2026-05-20` à vos requêtes pour activer le nouveau schéma dès maintenant. Après le **26 mai**, le nouveau schéma deviendra celui par défaut pour toutes les requêtes. Vous pouvez désactiver temporairement l'ancienne API avec `Api-Revision: 2026-05-07` jusqu'au **8 juin**, date à laquelle l'ancienne API sera définitivement supprimée.

### Chronologie

| Date | Phase | Utilisateurs du SDK | Utilisateurs de l'API REST |
| --- | --- | --- | --- |
| **7 mai** | Activer | Une nouvelle version du SDK est disponible (Python ≥2.0.0, JS ≥2.0.0). Passez à un forfait supérieur pour obtenir automatiquement le nouveau schéma. | Ajoutez l'en-tête `Api-Revision: 2026-05-20` pour activer cette fonctionnalité. L'ancienne version reste la version par défaut. |
| **26 mai** | Inversion par défaut | Aucune action n'est requise si vous avez déjà effectué la mise à niveau. Les anciens SDK (Python 1.x.x, JS 1.x.x) fonctionnent toujours, mais renvoient des réponses anciennes. | Le nouveau schéma est désormais celui par défaut. Envoyez l'en-tête `Api-Revision: 2026-05-07` pour ne plus recevoir de messages. |
| **8 juin** | Coucher du soleil | Les versions 1.x.x des SDK Python et JS ne fonctionneront plus pour les appels d'API Interactions. | L'ancien schéma a été supprimé pour l'API Interactions. En-tête `Api-Revision` ignoré. |

## Liste de contrôle de la migration

### Schéma des étapes (`steps`)

- Mettez à jour le code pour lire le contenu de la réponse à partir du tableau `steps` au lieu de `outputs`. [Voir des exemples](#basic-unary)
- Vérifiez que votre code gère les types d'étapes `user_input` et `model_output`. [Voir des exemples](#basic-unary)
- (Appel de fonction) Mettez à jour le code pour trouver les étapes `function_call` dans le tableau `steps`. [Voir des exemples](#function-calling)
- (Outils côté serveur) Mettez à jour le code pour gérer les étapes spécifiques aux outils (par exemple, `google_search_call`, `google_search_result`). [Consultez des exemples](#server-side-tools).
- (Historique sans état) Mettez à jour la gestion de l'historique pour transmettre le tableau `steps` dans le champ `input` de la prochaine requête. [En savoir plus](#stateless-history)
- (Streaming uniquement) Mettez à jour le client pour qu'il écoute les nouveaux types d'événements SSE (`interaction.created`, `step.delta`, etc.). [Voir des exemples](#streaming)

### Configuration du format de sortie (`response_format`)

- Remplacez `response_mime_type` par un champ `mime_type` dans `response_format`. [Voir des exemples](#structured-output)
- Encapsulez votre schéma JSON `response_format` existant dans un objet `{"type": "text", "schema": ...}`. [Voir des exemples](#structured-output)
- (Génération d'images) Déplacez `image_config` de `generation_config` vers une entrée `{"type": "image", ...}` dans `response_format`. [Voir des exemples](#image-config)
- (Génération de la parole) Remplacez `response_modalities=["audio"]` par une entrée `{"type": "audio"}` dans `response_format`. [Voir des exemples](#audio-config)
- (Multimodal) Convertissez `response_format` d'un seul objet en tableau lorsque vous demandez plusieurs modalités de sortie.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/07 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/07 (UTC)."],[],[]]
