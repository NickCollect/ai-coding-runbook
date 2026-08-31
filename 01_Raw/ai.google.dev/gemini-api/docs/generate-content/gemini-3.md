---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=fr
fetched_at: 2026-08-31T06:36:15.813075+00:00
title: "Guide du d\u00e9veloppeur Gemini\u00a03 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)

Envoyer des commentaires

# Guide du développeur Gemini 3

Gemini 3 est notre famille de modèles la plus intelligente à ce jour. Elle repose sur une technologie de raisonnement de pointe. Il est conçu pour donner vie à toutes vos idées en maîtrisant les workflows agentifs, le codage autonome et les tâches multimodales complexes.
Ce guide présente les principales fonctionnalités de la famille de modèles Gemini 3 et explique comment en tirer le meilleur parti.

[Essayer Gemini 3.1 Pro (preview)](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=fr)
[Essayer Gemini 3 Flash (preview)](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=fr)
[Essayer Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=fr)
[Essayer Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=fr)

Découvrez notre [collection d'applications Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=fr) pour voir comment le modèle gère le raisonnement avancé, le codage autonome et les tâches multimodales complexes.

Commencez avec quelques lignes de code :

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Découvrez la gamme Gemini 3

Gemini 3.1 Pro est idéal pour les tâches complexes qui nécessitent une vaste connaissance du monde et un raisonnement avancé dans plusieurs modalités.

Gemini 3 Flash est notre dernier modèle de la série 3. Il offre une intelligence de niveau Pro avec la rapidité et le prix de Flash.

Nano Banana Pro (également appelé Gemini 3 Pro Image) est notre modèle de génération d'images de la plus haute qualité. Nano Banana 2 (également appelé Gemini 3.1 Flash Image) est son équivalent à prix plus abordable, qui permet de générer des images en grand volume et de manière très efficace.

Gemini 3.1 Flash-Lite est notre modèle de référence, conçu pour l'efficacité et les tâches à haut volume.

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
| **`minimal`** | Not supported | Accepté (par défaut) | Compatible | Correspond au paramètre "Sans réflexion" pour la plupart des requêtes. Le modèle peut réfléchir de manière très minimale pour les tâches de codage complexes. Minimise la latence pour les applications de chat ou à haut débit. Notez que `minimal` ne garantit pas que la réflexion est désactivée. |
| **`low`** | Compatible | Compatible | Compatible | Minimise la latence et les coûts. Convient mieux aux applications de suivi d'instructions simples, de chat ou à haut débit. |
| **`medium`** | Compatible | Compatible | Compatible | Réflexion équilibrée pour la plupart des tâches. |
| **`high`** | Compatible (par défaut, dynamique) | Compatible (dynamique) | Compatible (par défaut, dynamique) | Maximise la profondeur du raisonnement. Le modèle peut mettre beaucoup plus de temps à générer le premier jeton de sortie (autre que le jeton de réflexion), mais la sortie sera plus soigneusement raisonnée. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Résolution des contenus multimédias

Gemini 3 introduit un contrôle précis du traitement multimodal de la vision à l'aide du paramètre `media_resolution`. Les résolutions plus élevées améliorent la capacité du modèle à lire du texte fin ou à identifier de petits détails, mais augmentent l'utilisation de jetons et la latence.
Le paramètre `media_resolution` détermine le **nombre maximal de jetons alloués par image ou frame vidéo en entrée**.

Vous pouvez désormais définir la résolution sur `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` ou `media_resolution_ultra_high` pour chaque partie de contenu multimédia ou de manière globale (via `generation_config`, la résolution globale n'est pas disponible pour l'ultra haute définition). Si aucune valeur n'est spécifiée, le modèle utilise les valeurs par défaut optimales en fonction du type de support.

**Paramètres recommandés**

| Type de support | Réglage recommandé | Nombre maximal de jetons | Conseils d'utilisation |
| --- | --- | --- | --- |
| **Images** | `media_resolution_high` | 1120 | Recommandé pour la plupart des tâches d'analyse d'images afin de garantir une qualité maximale. |
| **PDF** | `media_resolution_medium` | 560 | Idéal pour la compréhension des documents. La qualité atteint généralement son maximum à `medium`. Augmenter la valeur à `high` améliore rarement les résultats de l'OCR pour les documents standards. |
| **Vidéo** (général) | `media_resolution_low` (ou `media_resolution_medium`) | 70 (par frame) | **Remarque** : Pour les vidéos, les paramètres `low` et `medium` sont traités de manière identique (70 jetons) afin d'optimiser l'utilisation du contexte. Cela suffit pour la plupart des tâches de reconnaissance et de description d'actions. |
| **Vidéo** (avec beaucoup de texte) | `media_resolution_high` | 280 (par frame) | Obligatoire uniquement lorsque le cas d'utilisation implique la lecture de texte dense (OCR) ou de petits détails dans les images vidéo. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Température

Pour tous les modèles Gemini 3, nous vous recommandons vivement de conserver la valeur par défaut du paramètre de température, à savoir `1.0`.

Alors que les modèles précédents bénéficiaient souvent d'un réglage de la température pour contrôler la créativité par rapport au déterminisme, les capacités de raisonnement de Gemini 3 sont optimisées pour le paramètre par défaut. Si vous modifiez la température (en la définissant sur une valeur inférieure à 1,0), vous risquez d'obtenir un comportement inattendu, comme une boucle ou une dégradation des performances, en particulier pour les tâches mathématiques ou de raisonnement complexes.

### Signatures de réflexion

Gemini 3 utilise des [signatures de pensée](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=fr) pour maintenir le contexte de raisonnement lors des appels d'API. Ces signatures sont des représentations chiffrées du processus de réflexion interne du modèle. Pour vous assurer que le modèle conserve ses capacités de raisonnement, vous devez renvoyer ces signatures au modèle dans votre requête exactement telles qu'elles ont été reçues :

- **Appel de fonction (strict)** : l'API applique une validation stricte au "tour actuel". Si des signatures sont manquantes, une erreur 400 sera générée.
- **Texte/Chat** : la validation n'est pas strictement appliquée, mais l'omission des signatures dégradera la qualité du raisonnement et des réponses du modèle.
- **Génération/Modification d'images (strict)** : l'API applique une validation stricte à toutes les parties du modèle, y compris à `thoughtSignature`. Si des signatures sont manquantes, une erreur 400 sera générée.

#### Appel de fonction (validation stricte)

Lorsque Gemini génère un `functionCall`, il s'appuie sur le `thoughtSignature` pour traiter correctement la sortie de l'outil au tour suivant. Le "tour actuel" inclut toutes les étapes du modèle (`functionCall`) et de l'utilisateur (`functionResponse`) qui se sont produites depuis le dernier message `text` **Utilisateur** standard.

- **Appel de fonction unique** : la partie `functionCall` contient une signature. Vous devez le renvoyer.
- **Appels de fonction parallèles** : seule la première partie `functionCall` de la liste contient la signature. Vous devez retourner les pièces dans l'ordre exact dans lequel vous les avez reçues.
- **Multiples étapes (séquentielles)** : si le modèle appelle un outil, reçoit un résultat et appelle *un autre* outil (au cours du même tour), **les deux** appels de fonction ont des signatures. Vous devez renvoyer **toutes** les signatures accumulées dans l'historique.

#### Texte et streaming

Pour la génération de texte ou de chat standard, la présence d'une signature n'est pas garantie.

- **Non-Streaming** : la partie finale du contenu de la réponse peut contenir un `thoughtSignature`, mais ce n'est pas toujours le cas. Si vous en recevez un, renvoyez-le pour maintenir des performances optimales.
- **Streaming** : si une signature est générée, elle peut arriver dans un bloc final contenant une partie de texte vide. Assurez-vous que votre analyseur de flux recherche les signatures même si le champ de texte est vide.

#### Génération et modification d'images

Pour `gemini-3-pro-image-preview` et `gemini-3.1-flash-image-preview`, les signatures de pensée sont essentielles pour la Retouche conversationnelle. Lorsque vous demandez au modèle de modifier une image, il s'appuie sur le `thoughtSignature` du tour précédent pour comprendre la composition et la logique de l'image d'origine.

- **Modification** : les signatures sont garanties dans la première partie après les réflexions de la réponse (`text` ou `inlineData`) et dans chaque partie `inlineData` suivante. Vous devez renvoyer toutes ces signatures pour éviter les erreurs.

#### Exemples de code

#### Appel de fonction en plusieurs étapes (séquentiel)

L'utilisateur pose une question nécessitant deux étapes distinctes (vérifier le vol > réserver un taxi) en une seule fois.   
  
**Étape 1 : Le modèle appelle l'outil de vol.**  
Le modèle renvoie une signature `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Étape 2 : L'utilisateur envoie le résultat du vol**  
Nous devons renvoyer `<Sig_A>` pour que le modèle puisse poursuivre sa réflexion.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Étape 3 : Le modèle appelle l'outil Taxi**  
Le modèle se souvient du retard de vol grâce à `<Sig_A>` et décide maintenant de réserver un taxi. Il génère une *nouvelle* signature `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Étape 4 : L'utilisateur envoie le résultat de la course de taxi**  
Pour terminer le tour, vous devez renvoyer la chaîne complète : `<Sig_A>` ET `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Appel de fonction en parallèle

L'utilisateur demande : "Vérifie la météo à Paris et à Londres." Le modèle renvoie deux appels de fonction dans une seule réponse.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Texte/Raisonnement contextuel (sans validation)

L'utilisateur pose une question qui nécessite un raisonnement contextuel sans outils externes. Bien qu'elle ne soit pas strictement validée, l'inclusion de la signature aide le modèle à maintenir la chaîne de raisonnement pour les questions de suivi.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Génération et retouche d'images

Pour la génération d'images, les signatures sont strictement validées. Elles s'affichent sur la **première partie** (texte ou image) et sur **toutes les parties d'image suivantes**. Tous doivent être renvoyés au prochain tour.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Migrer depuis d'autres modèles

Si vous transférez une trace de conversation depuis un autre modèle (par exemple, Gemini 2.5) ou si vous injectez un appel de fonction personnalisé qui n'a pas été généré par Gemini 3, vous n'aurez pas de signature valide.

Pour contourner la validation stricte dans ces scénarios spécifiques, renseignez le champ avec cette chaîne fictive spécifique : `"thoughtSignature": "context_engineering_is_the_way
to_go"`.

### Sorties structurées avec des outils

Les modèles Gemini 3 vous permettent de combiner les [sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr) avec des outils intégrés, y compris l'[ancrage avec la Recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr), le [contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr), l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) et l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
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
  }
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
- **Retouche conversationnelle** : modification d'images multitour en demandant simplement les modifications souhaitées (par exemple, "Remplace l'arrière-plan par un coucher de soleil"). Ce workflow s'appuie sur les **signatures de pensée** pour préserver le contexte visuel entre les tours de parole.

Pour en savoir plus sur les formats, les workflows de modification et les options de configuration, consultez le [guide de génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**Exemple de réponse**

![Météo Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=fr)

### Exécution de code avec des images

Gemini 3 Flash peut traiter la vision comme une investigation active, et pas seulement comme un coup d'œil statique. En combinant le raisonnement à l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr), le modèle élabore un plan, puis écrit et exécute du code Python pour faire un zoom avant, recadrer, annoter ou manipuler des images étape par étape afin d'ancrer visuellement ses réponses.

**Cas d'utilisation** :

- **Zoom et inspection** : le modèle détecte implicitement lorsque les détails sont trop petits (par exemple, la lecture d'un indicateur ou d'un numéro de série éloignés) et écrit du code pour recadrer et réexaminer la zone à une résolution plus élevée.
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

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
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

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Pour en savoir plus sur l'exécution de code avec des images, consultez [Exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr#images).

### Réponses de fonction multimodales

L'[appel de fonction multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#multimodal) permet aux utilisateurs d'obtenir des réponses de fonction contenant des objets multimodaux, ce qui améliore l'utilisation des capacités d'appel de fonction du modèle. L'appel de fonction standard n'accepte que les réponses de fonction textuelles :

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Combiner les outils intégrés et l'appel de fonction

Gemini 3 permet d'utiliser des outils intégrés (comme la recherche Google, le contexte d'URL et [plus encore](https://ai.google.dev/gemini-api/docs/tools?hl=fr)) et des outils d'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) personnalisés dans le même appel d'API, ce qui permet des workflows plus complexes. Pour en savoir plus, consultez la page [Combinaisons d'outils](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: Type.OBJECT,
        properties: {
            location: {
                type: Type.STRING,
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

## Migrer depuis Gemini 2.5

Gemini 3 est notre famille de modèles la plus performante à ce jour. Elle offre une amélioration progressive par rapport à Gemini 2.5. Lorsque vous migrez, tenez compte des points suivants :

- **Raisonnement** : si vous utilisiez auparavant le prompt engineering complexe (comme la chaîne de pensée) pour forcer Gemini 2.5 à raisonner, essayez Gemini 3 avec `thinking_level: "high"` et des prompts simplifiés.
- **Paramètres de température** : si votre code existant définit explicitement la température (en particulier sur des valeurs basses pour des résultats déterministes), nous vous recommandons de supprimer ce paramètre et d'utiliser la valeur par défaut de Gemini 3 (1.0) pour éviter d'éventuels problèmes de boucle ou une dégradation des performances pour les tâches complexes.
- **Compréhension des PDF et des documents** : si vous vous êtes appuyé sur un comportement spécifique pour l'analyse des documents denses, testez le nouveau paramètre `media_resolution_high` pour vous assurer de la précision continue.
- **Consommation de jetons** : la migration vers les paramètres par défaut de Gemini 3 peut **augmenter** l'utilisation de jetons pour les PDF, mais la **diminuer** pour les vidéos. Si les requêtes dépassent désormais la fenêtre de contexte en raison de résolutions par défaut plus élevées, nous vous recommandons de réduire explicitement la résolution du contenu multimédia.
- **Segmentation d'images** : les fonctionnalités de segmentation d'images (qui renvoient des masques au niveau des pixels pour les objets) ne sont pas disponibles dans Gemini 3 Pro ni Gemini 3 Flash. Pour les charges de travail nécessitant une segmentation d'image native, nous vous recommandons de continuer à utiliser Gemini 2.5 Flash avec la fonctionnalité de réflexion désactivée.
- **Utilisation de l'ordinateur** : Gemini 3 Pro et Gemini 3 Flash sont compatibles avec l'[utilisation de l'ordinateur](https://ai.google.dev/gemini-api/docs/computer-use?hl=fr). Contrairement à la série 2.5, vous n'avez pas besoin d'utiliser un modèle distinct pour accéder à l'outil Utilisation de l'ordinateur.
- **Compatibilité avec les outils** : [la combinaison d'outils intégrés et de l'appel de fonction](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr) est désormais compatible avec les modèles Gemini 3. L'[ancrage Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr) est désormais également compatible avec les modèles Gemini 3.
- **Nombre de candidats** : les modèles Gemini 3 ne sont pas compatibles avec `candidateCount > 1`.
  Si vous définissez ce paramètre sur une valeur supérieure à `1`, une erreur 400 sera renvoyée.

## Compatibilité avec OpenAI

Pour les utilisateurs qui utilisent la [couche de compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr), les paramètres standards (`reasoning_effort` d'OpenAI) sont automatiquement mappés sur les équivalents Gemini (`thinking_level`).

## Bonnes pratiques concernant les prompts

Gemini 3 est un modèle de raisonnement, ce qui modifie la façon dont vous devez formuler vos requêtes.

- **Instructions précises** : soyez concis dans vos requêtes. Gemini 3 répond mieux aux instructions directes et claires. Il peut suranalyser les techniques de prompt engineering verbeuses ou trop complexes utilisées pour les anciens modèles.
- **Niveau de détail des réponses** : par défaut, Gemini 3 est moins bavard et préfère fournir des réponses directes et efficaces. Si votre cas d'utilisation nécessite une personnalité plus conversationnelle ou "bavarde", vous devez orienter explicitement le modèle dans la requête (par exemple, "Explique cela comme un assistant amical et bavard").
- **Gestion du contexte** : lorsque vous travaillez avec de grands ensembles de données (par exemple, des livres entiers, des bases de code ou de longues vidéos), placez vos instructions ou questions spécifiques à la fin de la requête, après le contexte des données. Ancrez le raisonnement du modèle aux données fournies en commençant votre question par une expression telle que "Sur la base des informations ci-dessus…".

Pour en savoir plus sur les stratégies de conception de requêtes, consultez le [guide sur l'ingénierie des requêtes](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr).

## Questions fréquentes

1. **Quelle est la date limite des connaissances pour Gemini 3 ?** Les modèles Gemini 3 ont une limite de connaissances fixée à janvier 2025. Pour obtenir des informations plus récentes, utilisez l'outil [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=fr).
2. **Quelles sont les limites de la fenêtre de contexte ?** Les modèles Gemini 3 sont compatibles avec une fenêtre de contexte d'entrée d'un million de jetons et une sortie de 64 000 jetons maximum.
3. **Existe-t-il un forfait sans frais pour Gemini 3 ?** Gemini 3 Flash`gemini-3-flash-preview` et 3.1 Flash-Lite`gemini-3.1-flash-lite` disposent de niveaux sans frais dans l'API Gemini. Vous pouvez essayer Gemini 3.1 Pro et 3 Flash sans frais dans Google AI Studio, mais aucun niveau sans frais n'est disponible pour `gemini-3.1-pro-preview` dans l'API Gemini.
4. **Mon ancien code `thinking_budget` fonctionnera-t-il toujours ?** Oui, `thinking_budget` est toujours compatible pour des raisons de rétrocompatibilité, mais nous vous recommandons de migrer vers `thinking_level` pour des performances plus prévisibles. Ne les utilisez pas tous les deux dans la même requête.
5. **Gemini 3 est-il compatible avec l'API Batch ?** Oui, Gemini 3 est compatible avec l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr).
6. **La mise en cache du contexte est-elle prise en charge ?** Oui, la [mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) est compatible avec Gemini 3.
7. **Quels outils sont compatibles avec Gemini 3 ?** Gemini 3 est compatible avec la [recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr), l'[ancrage avec Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr), la [recherche de fichiers](https://ai.google.dev/gemini-api/docs/file-search?hl=fr), l'[exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) et le [contexte de l'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr). Il est également compatible avec l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) standard pour vos propres outils personnalisés, [en plus des outils intégrés](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).
8. **Qu'est-ce que `gemini-3.1-pro-preview-customtools` ?** Si vous utilisez `gemini-3.1-pro-preview` et que le modèle ignore vos outils personnalisés au profit des commandes Bash, essayez plutôt le modèle `gemini-3.1-pro-preview-customtools`. [En savoir plus](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr#gemini-31-pro-preview-customtools)

## Étapes suivantes

- Premiers pas avec le [cookbook Gemini 3](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=fr#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Consultez le guide Cookbook dédié aux [niveaux de réflexion](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=fr#gemini3) et découvrez comment migrer du budget de réflexion vers les niveaux de réflexion.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/08/26 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/08/26 (UTC)."],[],[]]
