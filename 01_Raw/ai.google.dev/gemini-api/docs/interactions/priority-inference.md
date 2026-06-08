---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=fr
fetched_at: 2026-06-08T05:31:15.037704+00:00
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

# Inférence de la priorité

L'API Gemini Priority est un niveau d'inférence premium conçu pour les charges de travail critiques qui nécessitent une latence plus faible et une fiabilité maximale, à un prix premium. Le trafic de niveau Priorité est prioritaire sur le trafic de niveau Standard et Flex.

L'inférence de priorité est disponible pour tous les points de terminaison de l'API Interactions.

## Utiliser la priorité

Pour utiliser le niveau de priorité, définissez le champ `service_tier` de votre requête sur `priority`. Si le champ est omis, le niveau par défaut est "standard".

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    print(interaction.output_text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      console.log(interaction.output_text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Fonctionnement de l'inférence prioritaire

L'inférence prioritaire achemine les requêtes vers des files d'attente de calcul de haute criticité, ce qui permet d'obtenir des performances rapides et prévisibles pour les applications destinées aux utilisateurs. Son mécanisme principal est une rétrogradation côté serveur vers un traitement standard pour le trafic qui dépasse les limites dynamiques, ce qui garantit la stabilité de l'application au lieu de faire échouer la requête.

| Fonctionnalité | Priorité | Standard | Flex | Lot |
| --- | --- | --- | --- | --- |
| **Tarifs** | 75 à 100% de plus que Standard | Plein tarif | 50% de remise | 50% de remise |
| **Latence** | Secondes | De secondes à minutes | Minutes (objectif de 1 à 15 min) | Jusqu'à 24 heures |
| **Fiabilité** | Élevé (non amovible) | Élevée / Moyenne-haute | Optimisation limitée (désactivable) | Élevée (pour le débit) |
| **Interface** | Synchrone | Synchrone | Synchrone | Asynchrone |

### Principaux avantages

- **Faible latence** : conçu pour des temps de réponse de l'ordre de la seconde pour les outils d'IA interactifs destinés aux utilisateurs.
- **Fiabilité élevée** : le trafic est traité avec la plus haute criticité et ne peut en aucun cas être abandonné.
- **Dégradation élégante** : les pics de trafic dépassant les limites dynamiques sont automatiquement rétrogradés au niveau Standard pour être traités au lieu d'échouer, ce qui évite les interruptions de service.
- **Friction réduite** : utilise la même méthode `create` synchrone que les niveaux Standard et Flex.

### Cas d'utilisation

Le traitement prioritaire est idéal pour les workflows critiques pour l'entreprise, où les performances et la fiabilité sont primordiales.

- **Applications d'IA interactives** : chatbots et copilotes du service client où les utilisateurs paient un supplément et s'attendent à des réponses rapides et cohérentes.
- **Moteurs de décision en temps réel** : systèmes nécessitant des résultats très fiables et à faible latence, comme le triage des tickets en direct ou la détection des fraudes.
- **Fonctionnalités Premium pour les clients** : pour les développeurs qui doivent garantir des objectifs de niveau de service (SLO) plus élevés pour les clients payants.

### Limites de débit

La consommation prioritaire possède ses propres limites de débit, même si la consommation est comptabilisée dans les [limites de débit du trafic interactif global](https://aistudio.google.com/rate-limit?hl=fr). Les limites de débit par défaut pour l'inférence prioritaire sont **0,3 fois la limite de débit standard pour le modèle / le niveau**.

### Logique de rétrogradation progressive

Si les limites de priorité sont dépassées en raison d'une congestion, les demandes excédentaires sont **automatiquement et correctement** rétrogradées vers un traitement standard au lieu d'échouer avec une erreur 503 ou 429. Les demandes rétrogradées sont facturées au tarif standard, et non au tarif premium Priority.

### Responsabilité du client

- **Surveillance des réponses** : les développeurs doivent surveiller l'en-tête `x-gemini-service-tier` dans la réponse de l'API pour détecter si les requêtes sont fréquemment rétrogradées à `standard`.
- **Nouvelles tentatives** : les clients doivent implémenter une logique de nouvelle tentative/un intervalle exponentiel entre les tentatives pour les erreurs standards, telles que `DEADLINE_EXCEEDED`.

## Tarifs

L'inférence prioritaire coûte 75 à 100% de plus que l'[API standard](https://ai.google.dev/gemini-api/docs/pricing?hl=fr) et est facturée par jeton.

## Modèles compatibles

Les modèles suivants sont compatibles avec l'inférence prioritaire :

| Modèle | Inférence de la priorité |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) | ✔️ |
| [Preview Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) | ✔️ |
| [Preview Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fr) | ✔️ |

## Étape suivante

- [Inférence flexible](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=fr) pour réduire les coûts.
- [Jetons](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=fr) : découvrez les jetons.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/28 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/28 (UTC)."],[],[]]
