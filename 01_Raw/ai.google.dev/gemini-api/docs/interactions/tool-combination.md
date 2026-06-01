---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=fr
fetched_at: 2026-06-01T05:59:02.244890+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Combiner les outils intégrés et l'appel de fonction

Gemini permet de combiner des [outils intégrés](https://ai.google.dev/gemini-api/docs/tools?hl=fr), tels que `google_search`, et l'[appel de fonction](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=fr) (également appelé *outils personnalisés*) dans une seule interaction en conservant et en exposant l'historique du contexte des appels d'outils. Les combinaisons d'outils intégrées et personnalisées permettent de créer des workflows complexes et agentiques où, par exemple, le modèle peut s'ancrer dans des données Web en temps réel avant d'appeler votre logique métier spécifique.

Voici un exemple qui permet des combinaisons d'outils intégrés et personnalisés avec `google_search` et une fonction personnalisée `getWeather` :

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

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

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
  "model": "gemini-3.5-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Fonctionnement

Les modèles Gemini 3 utilisent la *circulation du contexte des outils* pour permettre les combinaisons d'outils intégrés et personnalisés. La circulation du contexte des outils permet de préserver et d'exposer le contexte des outils intégrés, et de le partager avec les outils personnalisés lors de la même interaction.

### Activer la combinaison d'outils

- Incluez [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=fr#function-declarations), ainsi que les outils intégrés que vous souhaitez utiliser, pour déclencher le comportement de combinaison.

### Étapes de retour de l'API

Dans une réponse d'interaction, l'API renvoie des étapes distinctes pour les appels d'outils intégrés et les appels de fonctions (outils personnalisés) :

- **Étapes de l'outil intégré** : l'API les gère automatiquement, en préservant le contexte à chaque tour.
- **Étapes d'appel de fonction** : l'API renvoie des étapes `function_call` pour vos fonctions personnalisées. Vous exécutez la fonction et renvoyez le résultat.

### Champs essentiels dans les étapes renvoyées

Certains champs des étapes renvoyées sont essentiels pour maintenir le contexte de l'outil et permettre les combinaisons d'outils :

- **`id`** : se trouve dans les étapes `function_call` et `function_response`. Identifiant unique qui associe un appel à sa réponse.
- **`signature`** : disponible dans les étapes `thought`, ainsi que dans toutes les étapes d'appel d'outil (par exemple, `function_call`) et de résultat (par exemple, `function_response`) pour les modèles Gemini 3 et versions ultérieures. Ce contexte chiffré permet la **circulation du contexte de l'outil** lors des interactions.

**Gérer ces champs :**

- **Mode avec état (recommandé)** : lorsque vous utilisez `previous_interaction_id`, le serveur gère automatiquement les champs `id` et `signature`.
- **Mode sans état** : lorsque vous gérez manuellement l'historique des conversations, vous devez vous assurer de renvoyer les champs `id` et `signature` au modèle dans les requêtes suivantes pour valider l'authenticité et maintenir le contexte. Les SDK officiels gèrent cela automatiquement si vous renvoyez l'objet de réponse complet à l'historique.

### Données spécifiques à l'outil

Certains outils intégrés renvoient des arguments de données visibles par l'utilisateur, spécifiques au type d'outil.

| Outil | Arguments d'appel d'outil visibles par l'utilisateur (le cas échéant) | Réponse de l'outil visible par l'utilisateur (le cas échéant) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls`  URL à parcourir | `status` : état de l'exploration `retrieved_url` : URL explorées |
| **file\_search** | Aucun | Aucun |

## Jetons et tarifs

Notez que les parties d'appel d'outil intégrées dans les requêtes sont comptabilisées dans `prompt_token_count`. Étant donné que ces étapes intermédiaires de l'outil sont désormais visibles et vous sont renvoyées, elles font partie de l'historique des conversations. Cela ne s'applique qu'aux *requêtes*, et non aux *réponses*.

L'outil Recherche Google est une exception à cette règle. La recherche Google applique déjà son propre modèle de tarification au niveau des requêtes. Les jetons ne sont donc pas facturés deux fois (consultez la page [Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr)).

Pour en savoir plus, consultez la page [Jetons](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=fr).

## Limites

- Par défaut, le mode `validated` (le mode `auto` n'est pas pris en charge) est utilisé lorsque la circulation du contexte de l'outil est activée.
- Les outils intégrés tels que `google_search` s'appuient sur des informations de localisation et d'heure actuelle. Par conséquent, si votre `system_instruction` ou votre `function_declaration.description` comporte des informations de localisation et d'heure incohérentes, la fonctionnalité de combinaison d'outils risque de ne pas fonctionner correctement.

## Outils compatibles

La circulation standard du contexte d'outil s'applique aux outils côté serveur (intégrés).
L'exécution de code est également un outil côté serveur, mais elle dispose de sa propre solution intégrée pour la circulation du contexte. L'utilisation de l'ordinateur et l'appel de fonctions sont des outils côté client qui disposent également de solutions intégrées pour la circulation du contexte.

| Outil | Côté exécution | Compatibilité avec la circulation du contexte |
| --- | --- | --- |
| [La recherche Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=fr) | Côté serveur | Compatible |
| [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=fr) | Côté serveur | Compatible |
| [Contexte de l'URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=fr) | Côté serveur | Compatible |
| [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=fr) | Côté serveur | Compatible |
| [Exécution de code](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=fr) | Côté serveur | Pris en charge (intégré, utilise les étapes `code_execution` et `code_execution_result`) |
| [Utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=fr) | Côté client | Pris en charge (intégré, utilise les étapes `function_call` et `function_response`) |
| [Fonctions personnalisées](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=fr) | Côté client | Pris en charge (intégré, utilise les étapes `function_call` et `function_response`) |

## Étape suivante

- En savoir plus sur l'[appel de fonction](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=fr) dans l'API Gemini
- Découvrez les outils compatibles :
  - [La recherche Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=fr)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=fr)
  - [Contexte de l'URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=fr)
  - [Recherche de fichiers](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/28 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/28 (UTC)."],[],[]]
