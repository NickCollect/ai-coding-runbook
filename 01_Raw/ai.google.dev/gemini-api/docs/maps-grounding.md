---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr
fetched_at: 2026-08-10T03:22:49.340755+00:00
title: "Ancrage avec Google\u00a0Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Ancrage avec Google Maps

L'ancrage avec Google Maps associe les capacités génératives de Gemini aux données riches, factuelles et à jour de Google Maps. Cette fonctionnalité permet aux développeurs d'intégrer facilement des fonctionnalités de localisation dans leurs applications. Lorsqu'une requête utilisateur a un contexte lié aux données Maps, le modèle Gemini exploite Google Maps pour fournir des réponses factuellement exactes et récentes, pertinentes pour le lieu spécifié par l'utilisateur ou la zone géographique générale.

- **Réponses précises et géolocalisées** : exploitez les données complètes et actuelles de Google Maps pour les requêtes géographiques spécifiques.
- **Personnalisation améliorée** : adaptez les recommandations et les informations en fonction des lieux fournis par l'utilisateur.

## Premiers pas

Cet exemple montre comment intégrer l'ancrage avec Google Maps dans votre application pour fournir des réponses précises et géolocalisées aux requêtes des utilisateurs. La requête demande des recommandations locales avec une position utilisateur facultative, ce qui permet au modèle Gemini d'utiliser les données Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Fonctionnement de l'ancrage avec Google Maps

L'ancrage avec Google Maps intègre l'API Gemini à l'écosystème Google Geo en utilisant l'API Google Maps comme source d'ancrage. Lorsque la requête d'un utilisateur contient un contexte géographique, le modèle Gemini peut appeler l'outil d'ancrage avec Google Maps. Le modèle peut ensuite générer des réponses basées sur les données Google Maps pertinentes pour le lieu fourni.

Ce processus implique généralement les étapes suivantes :

1. **Requête utilisateur** : un utilisateur envoie une requête à votre application, qui peut inclure un contexte géographique (par exemple, "cafés à proximité" ou "musées à San Francisco").
2. **Appel d'outil** : le modèle Gemini, reconnaissant l'intention géographique, appelle l'outil d'ancrage avec Google Maps. Cet outil peut éventuellement être fourni avec la `latitude` et la `longitude` de l'utilisateur. L'outil est un outil de recherche textuelle et se comporte de la même manière que la recherche dans Maps. Les requêtes locales ("à proximité") utilisent les coordonnées, tandis que les requêtes spécifiques ou non locales sont peu susceptibles d'être influencées par le lieu explicite.
3. **Récupération des données** : le service d'ancrage avec Google Maps interroge Google Maps pour obtenir des informations pertinentes (par exemple, des lieux, des avis, des photos, des adresses, des horaires d'ouverture).
4. **Génération ancrée** : les données Maps récupérées sont utilisées pour informer la réponse du modèle Gemini, ce qui garantit l'exactitude et la pertinence des faits.
5. **Réponse et annotations** : le modèle renvoie une réponse textuelle avec des annotations intégrées renvoyant aux sources Google Maps, ce qui permet aux développeurs d'afficher des citations.

## Pourquoi et quand utiliser l'ancrage avec Google Maps

L'ancrage avec Google Maps est idéal pour les applications qui nécessitent des informations précises, à jour et spécifiques à un lieu. Il améliore l'expérience utilisateur en fournissant des contenus pertinents et personnalisés, basés sur la vaste base de données Google Maps de plus de 250 millions de lieux dans le monde.

Vous devez utiliser l'ancrage avec Google Maps lorsque votre application doit :

- fournir des réponses complètes et précises à des questions géographiques spécifiques ;
- créer des planificateurs de voyage conversationnels et des guides locaux ;
- recommander des points d'intérêt en fonction du lieu et des préférences de l'utilisateur, comme des restaurants ou des magasins ;
- créer des expériences géolocalisées pour les services sociaux, de vente au détail ou de livraison de nourriture.

L'ancrage avec Google Maps excelle dans les cas d'utilisation où la proximité et les données factuelles actuelles sont essentielles, par exemple pour trouver le "meilleur café à proximité" ou obtenir un itinéraire.

## Cas d'utilisation

L'ancrage avec Google Maps est compatible avec différents cas d'utilisation géolocalisés.

### Gérer les questions spécifiques à un lieu

Posez des questions détaillées sur un lieu spécifique pour obtenir des réponses basées sur les avis des utilisateurs Google et d'autres données Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Fournir une personnalisation basée sur la localisation

Obtenez des recommandations adaptées aux préférences d'un utilisateur et à une zone géographique spécifique.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Aider à la planification d'itinéraires

Générez des plans sur plusieurs jours avec des itinéraires et des informations sur différents lieux, parfaits pour les applications de voyage.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Conditions d'utilisation du service

Cette section décrit les conditions d'utilisation du service pour l'ancrage avec Google Maps.

### Informer l'utilisateur de l'utilisation des sources Google Maps

Pour chaque résultat ancré de Google Maps, vous recevrez des annotations de source sur les blocs de contenu de l'étape `model_output` qui prennent en charge chaque réponse. Les métadonnées suivantes sont renvoyées :

- URL de la source
- nom

Lorsque vous présentez des résultats de l'ancrage avec Google Maps, vous devez spécifier les sources Google Maps associées et informer vos utilisateurs des points suivants :

- Les sources Google Maps doivent suivre immédiatement le contenu généré qu'elles prennent en charge. Ce contenu généré est également appelé résultat ancré de Google Maps.
- Les sources Google Maps doivent être visibles en une seule interaction de l'utilisateur.

### Afficher les sources Google Maps avec des liens Google Maps

Pour chaque annotation de source, un aperçu du lien doit être généré en respectant les exigences suivantes :

- Attribuez chaque source à Google Maps en suivant les consignes d'attribution textuelle de Google Maps
  .
- Affichez le nom de la source fourni dans la réponse.
- Créez un lien vers la source à l'aide de l'`url` de l'annotation.

### Consignes d'attribution textuelle de Google Maps

Lorsque vous attribuez des sources à Google Maps dans du texte, suivez ces consignes :

- Ne modifiez en aucun cas le texte Google Maps :
  - Ne modifiez pas la casse de Google Maps.
  - N'insérez pas Google Maps sur plusieurs lignes.
  - Ne traduisez pas Google Maps dans une autre langue.
  - Empêchez les navigateurs de traduire Google Maps en utilisant l'attribut HTML translate="no".

Pour en savoir plus sur certains de nos fournisseurs de données Google Maps et leurs
conditions de licence, consultez les [mentions légales de Google Maps et Google Earth](https://www.google.com/help/legalnotices_maps/?hl=fr).

## Bonnes pratiques

- **Fournir la position de l'utilisateur** : pour obtenir les réponses les plus pertinentes et personnalisées, incluez toujours la `latitude` et la `longitude` dans la configuration de votre outil `google_maps` lorsque la position de l'utilisateur est connue.
- **Informer les utilisateurs finaux** : indiquez clairement à vos utilisateurs finaux que les données Google Maps sont utilisées pour répondre à leurs requêtes, en particulier lorsque l'outil est activé.
- **Désactiver lorsque ce n'est pas nécessaire** : l'ancrage avec Google Maps est désactivé par défaut. N'activez-le (`"tools": [{"type": "google_maps"}]`) que lorsqu'une requête a un
  contexte géographique clair, afin d'optimiser les performances et les coûts.

## Limites

- L'ancrage avec Google Maps n'est actuellement compatible qu'avec les requêtes et les réponses en anglais.
- L'outil peut ne pas être disponible dans toutes les régions.
- Les résultats peuvent varier en fonction de la précision de la localisation et des données Maps disponibles.
- **Couverture géographique** : l'ancrage avec Google Maps est disponible dans le monde entier.
- **État par défaut** : l'outil d'ancrage avec Google Maps est désactivé par défaut.
  Vous devez l'activer explicitement dans vos requêtes API.

## Tarifs et limites de débit

Les tarifs de l'ancrage avec Google Maps varient en fonction de la génération du modèle :

- **Modèles Gemini 3** : votre projet est facturé pour chaque **requête de recherche** que le modèle décide d'exécuter. Une seule **requête de recherche** (votre requête API au modèle) peut entraîner l'exécution de plusieurs requêtes de recherche par le modèle pour trouver les informations nécessaires. Chacune de ces requêtes est comptabilisée comme une utilisation facturable de l'outil.
- **Modèles Gemini 2.5 et versions antérieures** : votre projet est facturé par **requête de recherche**.
  Une requête n'est facturée que si la requête renvoie au moins un résultat ancré de Google Maps, quel que soit le nombre de requêtes de recherche individuelles que le modèle a effectuées en interne pour obtenir ce résultat.

Pour en savoir plus sur les tarifs, consultez la page [Tarifs de l'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Modèles compatibles

Les modèles suivants sont compatibles avec l'ancrage avec Google Maps :

| Modèle | Ancrage avec Google Maps |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fr) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fr) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr) | ✔️ |
| [Gemini 3.1 Pro (preview)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) | ✔️ |
| [Gemini 3 Flash (preview)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fr) | ✔️ |

## Combinaisons d'outils compatibles

Les modèles Gemini 3 sont compatibles avec la combinaison d'outils intégrés (comme l'ancrage avec Google Maps) et d'outils personnalisés (appel de fonction). Pour en savoir plus, consultez la
[page sur les combinaisons d'outils](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).

## Étape suivante

- Découvrez d'autres [outils disponibles](https://ai.google.dev/gemini-api/docs/tools?hl=fr).
- Pour en savoir plus sur les bonnes pratiques d'IA responsable et les filtres de sécurité de l'API Gemini, consultez [le guide des paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
