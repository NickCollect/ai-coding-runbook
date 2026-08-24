---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=fr
fetched_at: 2026-08-24T02:25:57.302418+00:00
title: "URLs de contexte \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# URLs de contexte

L'outil de contexte d'URL vous permet de fournir un contexte supplémentaire aux modèles sous la
forme d'URL. En incluant des URL dans votre requête, le modèle accédera
au contenu de ces pages (à condition qu'il ne s'agisse pas d'un type d'URL listé dans la
[section "Limites"](#limitations)) pour informer
et améliorer sa réponse.

L'outil de contexte d'URL est utile pour les tâches suivantes, par exemple :

- **Extraire des données** : extrayez des informations spécifiques telles que des prix, des noms ou des conclusions
  clés à partir de plusieurs URL.
- **Comparer des documents** : analysez plusieurs rapports, articles ou PDF pour
  identifier les différences et suivre les tendances.
- **Synthétiser et créer du contenu** : combinez des informations provenant de plusieurs URL sources pour générer des résumés, des articles de blog ou des rapports précis.
- **Analyser du code et des documents** : pointez vers un dépôt GitHub ou une documentation technique pour expliquer du code, générer des instructions de configuration ou répondre à des questions.

L'exemple suivant montre comment comparer deux recettes provenant de différents sites Web.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Fonctionnement

L'outil Contexte de l'URL utilise un processus d'extraction en deux étapes pour équilibrer la vitesse, le coût et l'accès aux données récentes. Lorsque vous fournissez une URL, l'outil tente d'abord d'extraire le contenu d'un cache d'index interne. Il s'agit d'un cache hautement optimisé. Si une URL n'est pas disponible dans l'index (par exemple, s'il s'agit d'une page très récente), l'outil revient automatiquement à une extraction en direct.
Il accède directement à l'URL pour récupérer son contenu en temps réel.

## Combinaison avec d'autres outils

Vous pouvez combiner l'outil de contexte d'URL avec d'autres outils pour créer des workflows plus puissants.

[Les modèles Gemini 3](#supported-models) sont compatibles avec la combinaison d'outils intégrés
(comme le Contexte de l'URL) et d'outils personnalisés (appel de fonction). Pour en savoir plus, consultez la
[page sur les combinaisons d'outils](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).

### Ancrage avec la recherche

Lorsque le contexte d'URL et
[l'ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/grounding?hl=fr) sont activés,
le modèle peut utiliser ses fonctionnalités de recherche pour trouver
des informations pertinentes en ligne, puis utiliser l'outil de contexte d'URL pour mieux
comprendre les pages qu'il trouve. Cette approche est efficace pour les invites qui nécessitent à la fois une recherche étendue et une analyse approfondie de pages spécifiques.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Comprendre la réponse

Lorsque le modèle utilise l'outil de contexte d'URL, sa réponse textuelle inclut des annotations `url_citation` intégrées dans le bloc de contenu textuel. Chaque annotation associe un segment du texte de la réponse (via `start_index` et `end_index`) à l'URL source à partir de laquelle il a été dérivé. Il s'agit du principal moyen d'afficher des citations dans votre
application. Pour savoir comment les extraire, consultez le [main example above](#get-started).

La réponse inclut également une étape `url_context_result` avec des métadonnées sur chaque tentative d'extraction d'URL (état, URL extraite). Cela est principalement utile pour le débogage.

### Contrôles de sécurité

Le système effectue un contrôle de modération du contenu sur les URL pour vérifier qu'elles respectent les normes de sécurité. Si une URL échoue à ce contrôle, l'étape correspondante
`url_context_result` affiche un `status` de `"unsafe"`.

### Nombre de jetons

Le contenu extrait des URL que vous spécifiez dans votre invite est comptabilisé dans les jetons d'entrée. Vous pouvez voir le nombre de jetons dans l'objet `usage` de l'interaction. Voici un exemple :

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

Le prix par jeton dépend du modèle utilisé. Pour en savoir plus, consultez la
[page sur les tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Modèles compatibles

| Modèle | Contexte de l'URL |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fr) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fr) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) | ✔️ |
| [Preview Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fr) | ✔️ |

## Bonnes pratiques

- **Fournissez des URL spécifiques** : pour obtenir les meilleurs résultats, fournissez des URL directes vers le
  contenu que vous souhaitez que le modèle analyse. Le modèle ne récupérera le contenu que des URL que vous fournissez, et non celui des liens imbriqués.
- **Vérifiez l'accessibilité** : vérifiez que les URL que vous fournissez ne mènent pas à
  des pages qui nécessitent une connexion ou qui sont soumises à un paywall.
- **Utilisez l'URL complète** : fournissez l'URL complète, y compris le protocole
  (par exemple, https://www.google.com au lieu de google.com).

## Limites

- Limite de requêtes : l'outil peut traiter jusqu'à 20 URL par requête.
- Taille du contenu de l'URL : la taille maximale du contenu extrait d'une seule URL est de 34 Mo.
- Accessibilité publique : les URL doivent être accessibles au public sur le Web.
  Les adresses localhost (par exemple, localhost, 127.0.0.1), les réseaux privés et les services de tunneling (par exemple, ngrok, pinggy) ne sont pas acceptés.

### Types de contenu acceptés et non acceptés

L'outil peut extraire du contenu à partir d'URL avec les types de contenu suivants :

- Texte (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Image (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Les types de contenu suivants **ne sont pas** acceptés :

- Contenu soumis à un paywall
- Vidéos YouTube (pour savoir comment traiter les URL YouTube, consultez
  [Comprendre les vidéos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr#youtube))
- Fichiers Google Workspace tels que des documents ou des feuilles de calcul Google
- Fichiers audio et vidéo

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/31 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/31 (UTC)."],[],[]]
