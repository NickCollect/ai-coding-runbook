---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=fr
fetched_at: 2026-06-29T05:28:54.219134+00:00
title: "Ancrage avec la recherche\u00a0Google \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Ancrage avec la recherche Google

L'ancrage avec la Recherche Google permet d'associer le modèle Gemini à des contenus Web en temps réel et fonctionne avec toutes les langues disponibles. Cela permet à Gemini de fournir des réponses plus précises et de citer des sources vérifiables au-delà de sa date limite de connaissances.

L'ancrage vous aide à créer des applications qui peuvent :

- **Améliorer la justesse factuelle** : réduisez les hallucinations du modèle en basant les réponses sur des informations réelles.
- **Accéder à des informations en temps réel** : répondez à des questions sur des événements et des sujets récents.
- **Fournir des citations** : renforcez la confiance des utilisateurs en indiquant les sources des affirmations du modèle.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
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

Pour en savoir plus, essayez le [notebook de l'outil de recherche](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=fr).

## Fonctionnement de l'ancrage avec la recherche Google

Lorsque vous activez l'outil `google_search`, le modèle gère automatiquement l'ensemble du workflow de recherche, de traitement et de citation des informations.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=fr)

1. **Invite de l'utilisateur** : votre application envoie l'invite d'un utilisateur à l'API Gemini avec l'outil `google_search` activé.
2. **Analyse de l'invite** : le modèle analyse l'invite et détermine si une recherche Google peut améliorer la réponse.
3. **Recherche Google** : si nécessaire, le modèle génère automatiquement une ou plusieurs requêtes de recherche et les exécute.
4. **Traitement des résultats de recherche** : le modèle traite les résultats de recherche, synthétise les informations et formule une réponse.
5. **Réponse ancrée** : l'API renvoie une réponse finale et conviviale qui est ancrée dans les résultats de recherche. Cette réponse inclut la réponse textuelle du modèle et `groundingMetadata` avec les requêtes de recherche, les résultats Web et les citations.

## Comprendre la réponse d'ancrage

Lorsqu'une réponse est correctement ancrée, elle inclut un champ `groundingMetadata`. Ces données structurées sont essentielles pour vérifier les affirmations et créer une expérience de citation enrichie dans votre application.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

L'API Gemini renvoie les informations suivantes avec `groundingMetadata` :

- `webSearchQueries` : tableau des requêtes de recherche utilisées. Cela est utile pour le débogage et la compréhension du processus de raisonnement du modèle.
- `searchEntryPoint` : contient le code HTML et CSS permettant d'afficher les suggestions de recherche requises. Les exigences d'utilisation complètes sont détaillées dans les [Conditions d'
  utilisation](https://ai.google.dev/gemini-api/terms?hl=fr#grounding-with-google-search).
- `groundingChunks` : tableau d'objets contenant les sources Web (`uri` et `title`).
- `groundingSupports` : tableau de blocs permettant de connecter la réponse `text` du modèle aux sources dans `groundingChunks`. Chaque bloc associe un `segment` de texte (défini par `startIndex` et `endIndex`) à un ou plusieurs `groundingChunkIndices`. Il s'agit de la clé pour créer des citations intégrées.

L'ancrage avec la recherche Google peut également être utilisé en combinaison avec l'outil de contexte d'[URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) pour ancrer les réponses à la fois dans les données Web publiques
et dans les URL spécifiques que vous fournissez.

## Attribuer des sources avec des citations intégrées

L'API renvoie des données de citation structurées, ce qui vous permet de contrôler entièrement la façon dont vous affichez les sources dans votre interface utilisateur. Vous pouvez utiliser les champs `groundingSupports` et `groundingChunks` pour lier directement les affirmations du modèle à leurs sources. Voici un schéma courant pour traiter les métadonnées afin de créer une réponse avec des citations intégrées cliquables.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

La nouvelle réponse avec des citations intégrées se présentera comme suit :

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Tarifs

Lorsque vous utilisez l'ancrage avec la recherche Google avec Gemini 3, votre projet est facturé pour chaque requête de recherche que le modèle décide d'exécuter. Si le modèle décide d'
exécuter plusieurs requêtes de recherche pour répondre à une seule invite (par exemple,
en recherchant `"UEFA Euro 2024 winner"` et `"Spain vs England Euro 2024 final
score"` dans le même appel d'API), cela compte comme deux utilisations facturables de l'outil
pour cette requête. À des fins de facturation, nous ignorons les requêtes de recherche Web vides lors du comptage des requêtes uniques. Ce modèle de facturation ne s'applique qu'aux modèles Gemini 3. Lorsque vous utilisez l'ancrage de recherche avec Gemini 2.5 ou des modèles plus anciens, votre projet est facturé par invite.

Pour en savoir plus sur les tarifs, consultez la page [Tarifs de l'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Modèles compatibles

Vous trouverez toutes les fonctionnalités sur la page de présentation du [modèle
vue d'ensemble](https://ai.google.dev/gemini-api/docs/models?hl=fr).

| Modèle | Ancrage avec la recherche Google |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Preview Gemini 3.1 Flash-Lite | ✔️ |
| Preview Gemini 3.1 Pro | ✔️ |
| Preview Gemini 3 Pro | ✔️ |
| Preview Gemini 3 Flash | ✔️ |
| Preview Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.0 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinaisons d'outils compatibles

Vous pouvez utiliser l'ancrage avec la recherche Google avec d'autres outils tels que
[l'exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) et
[le contexte d'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=fr) pour gérer des cas d'utilisation plus complexes.

Les modèles Gemini 3 sont compatibles avec la combinaison d'outils intégrés (tels que l'ancrage avec la recherche Google) et d'outils personnalisés (appels de fonction). Pour en savoir plus, consultez la
[page Combinaisons d'outils](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).

## Étape suivante

- [Essayez l'ancrage avec la recherche Google dans le livre de recettes de l'API Gemini.](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=fr)
- Découvrez d'autres outils disponibles, tels que les [appels de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr).
- [Découvrez comment augmenter les invites avec des URL spécifiques à l'aide de l'outil de contexte d'URL.](https://ai.google.dev/gemini-api/docs/url-context?hl=fr)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/23 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/23 (UTC)."],[],[]]
