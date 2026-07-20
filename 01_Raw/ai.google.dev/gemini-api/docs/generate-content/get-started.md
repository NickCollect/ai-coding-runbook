---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr
fetched_at: 2026-07-20T04:47:23.488362+00:00
title: "Premiers pas \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Premiers pas

Ce guide vous aidera à commencer à utiliser l'ancienne API **generateContent**. Pour les nouveaux projets et applications, nous vous recommandons vivement d'utiliser la nouvelle **API Interactions**, qui constitue le moyen le plus simple et le plus efficace de créer des applications avec les modèles et les agents Gemini.

Ce guide de démarrage rapide vous explique comment installer nos
[bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr) et effectuer votre première requête, diffuser
des réponses, créer des conversations multitours et utiliser des outils à l'aide de la méthode
`generateContent` standard.

## Obtenir une clé API

Pour utiliser l'API Gemini, vous devez disposer d'une clé API afin d'authentifier vos requêtes, d'appliquer des limites de sécurité et de suivre l'utilisation de votre compte.

- Google AI Studio crée automatiquement un projet et une clé API pour les nouveaux utilisateurs.
  Vous pouvez la copier depuis la page [Clés API](https://aistudio.google.com/api-keys?hl=fr).
- Si vous avez besoin d'une nouvelle clé, cliquez sur **Créer une clé API** dans AI Studio, puis suivez les instructions de la boîte de dialogue pour ajouter une nouvelle paire clé-projet.

[Créer une clé API Gemini](https://aistudio.google.com/apikey?hl=fr)

Définissez votre clé en tant que variable d'environnement :

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Passer à l'offre payante

Le passage à l'offre payante augmente vos limites de débit et nécessite la configuration de la facturation Cloud.

- Cliquez sur **Configurer la facturation** sur les pages Clés API
   ou
  [Projets](https://aistudio.google.com/projects?hl=fr) d'AI Studio.
- Suivez les instructions de la boîte de dialogue Facturation Cloud pour créer ou associer un compte de facturation, ajouter un mode de paiement et prépayer un minimum de 10 $ (ou l'équivalent dans votre devise) en crédits payants.
- Consultez votre utilisation de l'API dans [Google AI Studio](https://aistudio.google.com/usage?hl=fr)
  sous **Tableau de bord** > **Utilisation**.

Pour en savoir plus, consultez la page [Facturation](https://ai.google.dev/gemini-api/docs/billing?hl=fr).

## Installer le SDK Google GenAI

### Python

Si vous utilisez [Python 3.9 ou une version ultérieure](https://www.python.org/downloads/), installez le
[`google-genai` package](https://pypi.org/project/google-genai/)
à l'aide de la commande
[pip suivante](https://packaging.python.org/en/latest/tutorials/installing-packages/) :

```
pip install -q -U google-genai
```

### JavaScript

Si vous utilisez [Node.js v18 ou une version ultérieure](https://nodejs.org/en/download/package-manager),
installez le
[SDK Google Gen AI pour TypeScript et JavaScript](https://www.npmjs.com/package/@google/genai)
à l'aide de la commande
[npm suivante](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) :

```
npm install @google/genai
```

## Générer du texte

Utilisez la méthode `models.generate_content` pour
[générer une réponse textuelle](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Réponses dynamiques

Par défaut, le modèle ne renvoie une réponse qu'une fois l'ensemble du processus de génération terminé. Pour une expérience plus rapide et interactive, vous pouvez
[diffuser les blocs de réponse](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#stream) au fur et à mesure qu'ils
sont générés.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Conversations multitours

Pour les conversations multitours, les SDK fournissent un assistant `chats` avec état afin de
créer une expérience de chat [multitours](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#chat)
qui gère automatiquement l’historique des conversations.

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Utiliser des outils

Étendez les capacités du modèle en
[ancrant les réponses avec la recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)
pour accéder à du contenu Web en temps réel. Le modèle décide automatiquement quand effectuer une recherche, exécute les requêtes et synthétise une réponse.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

L'API Gemini est également compatible avec d'autres outils intégrés :

- **[Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr)**:
  permet au modèle d'écrire et d'exécuter du code Python pour résoudre des problèmes mathématiques complexes.
- **[Contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)** : vous permet d'
  ancrer les réponses dans des URL de pages Web spécifiques que vous fournissez.
- **[Recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr)** : vous permet d'
  importer des fichiers et d'ancrer les réponses dans leur contenu à l'aide de la recherche sémantique.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr)** : vous permet d'
  ancrer les réponses dans des données de localisation et de rechercher des lieux, des itinéraires et des
  cartes.
- **[Utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr)** : permet au
  modèle d'interagir avec un écran d'ordinateur virtuel, un clavier et une souris pour
  effectuer des tâches.

## Appeler des fonctions personnalisées

Utilisez l'**[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)** pour connecter
des modèles à vos outils et API personnalisés. Le modèle détermine quand appeler votre fonction et renvoie un `functionCall` dans la réponse pour que votre application l'exécute.

Cet exemple déclare une fonction de température factice et vérifie si le modèle souhaite l'appeler.

### Python

```
from google import genai
from google.genai import types

weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## Étape suivante

Maintenant que vous avez commencé à utiliser l'API Gemini, consultez les guides suivants pour créer des applications plus avancées :

- [Génération de texte](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr)
- [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr)
- [Compréhension des images](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr)
- [Raisonnement](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)
- [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
- [Ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr)
- [Contexte long](https://ai.google.dev/gemini-api/docs/long-context?hl=fr)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/08 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/08 (UTC)."],[],[]]
