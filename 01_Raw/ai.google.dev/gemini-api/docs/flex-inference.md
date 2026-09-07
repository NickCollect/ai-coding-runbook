---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=fr
fetched_at: 2026-09-07T05:37:56.389148+00:00
title: "Inf\u00e9rence flexible \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Inférence flexible

L'API Gemini Flex est un niveau d'inférence qui offre une réduction des coûts de 50% par rapport aux tarifs standards, en échange d'une latence variable et d'une disponibilité optimale. Elle est conçue pour les charges de travail tolérantes à la latence qui nécessitent un traitement synchrone, mais qui n'ont pas besoin des performances en temps réel de l'API standard.

## Utiliser Flex

Pour utiliser le niveau Flex, spécifiez `service_tier` comme `flex` dans votre requête. Par défaut, les requêtes utilisent le niveau standard si ce champ est omis.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.6-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Fonctionnement de l'inférence Flex

L'inférence Gemini Flex comble le fossé entre l'API standard et le délai de traitement de 24 heures
de l'[API par lot](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr). Elle utilise une capacité de calcul "réductible" en dehors des heures de pointe pour fournir une solution économique pour les tâches en arrière-plan et les workflows séquentiels.

| Fonctionnalité | Flex | Priorité | Standard | Lot |
| --- | --- | --- | --- | --- |
| **Tarifs** | 50% de remise | 75 à 100% de plus que le tarif standard | Plein tarif | 50% de remise |
| **Latence** | Minutes (1 à 15 minutes cibles) | Faible (secondes) | Secondes à minutes | Jusqu'à 24 heures |
| **Fiabilité** | Optimisation limitée (réductible) | Élevée (non réductible) | Élevée / Moyenne-élevée | Élevée (pour le débit) |
| **Interface** | Synchrone | Synchrone | Synchrone | Asynchrone |

### Principaux avantages

- **Rentabilité** : économies substantielles pour les évaluations hors production, les agents en arrière-plan et l'enrichissement des données.
- **Faible friction** : il vous suffit d'ajouter un seul paramètre à vos requêtes existantes.
- **Workflows synchrones** : idéal pour les chaînes d'API séquentielles où la requête suivante dépend du résultat de la précédente, ce qui la rend plus flexible que Batch pour les workflows agentiques.

### Cas d'utilisation

- **Évaluations hors connexion** : exécution de tests de régression ou de classements « LLM-as-a-judge ».
- **Agents en arrière-plan** : tâches séquentielles telles que les mises à jour CRM, la création de profils ou la modération de contenu où quelques minutes de délai sont acceptables.
- **Recherche avec budget limité** : expériences universitaires nécessitant un volume de jetons élevé avec un budget limité.

### Limites de débit

Le trafic d'inférence Flex est comptabilisé dans vos [limites de débit](https://aistudio.google.com/rate-limit?hl=fr) générales. Il n'offre pas
de limites de débit étendues comme l'[API par lot](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr).

### Capacité réductible

Le trafic Flex est traité avec une priorité inférieure. En cas de pic de trafic standard, les requêtes Flex peuvent être préemptées ou supprimées pour garantir la capacité des utilisateurs prioritaires. Si vous recherchez une inférence prioritaire, consultez la section
[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)

### Codes d'erreur

Lorsque la capacité Flex n'est pas disponible ou que le système est saturé, l'API renvoie des codes d'erreur standards :

- **503 Service indisponible** : le système a atteint sa capacité maximale.
- **429 Trop de requêtes** : limites de débit ou épuisement des ressources.

### Responsabilité du client

- **Aucune reprise en cas d'échec côté serveur** : pour éviter les frais imprévus, le système ne
  met pas automatiquement à niveau une requête Flex vers le niveau standard si la capacité Flex est
  pleine.
- **Nouvelles tentatives** : vous devez implémenter votre propre logique de nouvelle tentative côté client avec
  un intervalle exponentiel entre les tentatives.
- **Délais avant expiration** : étant donné que les requêtes Flex peuvent être mises en file d'attente, nous vous recommandons
  d'augmenter les délais avant expiration côté client à 10 minutes ou plus pour éviter une fermeture prématurée
  de la connexion.

## Ajuster les fenêtres de délai avant expiration

Vous pouvez configurer des délais avant expiration par requête pour l'API REST et les bibliothèques clientes.
Assurez-vous toujours que votre délai avant expiration côté client couvre la fenêtre de patience du serveur prévue (par exemple, 600 secondes ou plus pour les files d'attente Flex). Les SDK attendent des valeurs de délai avant expiration en millisecondes.

### Délais avant expiration par requête

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## Implémenter des nouvelles tentatives

Étant donné que Flex est réductible et échoue avec des erreurs 503, voici un exemple d'implémentation facultative d'une logique de nouvelle tentative pour continuer avec les requêtes ayant échoué :

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.6-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.6-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.6-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## Tarifs

[L'inférence Flex est facturée à 50% de l'API standard](https://ai.google.dev/gemini-api/docs/pricing?hl=fr)
et facturée par jeton.

## Modèles compatibles

Les modèles suivants sont compatibles avec l'inférence Flex :

| Modèle | Inférence Flex |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fr) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fr) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) | ✔️ |
| [Preview Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fr) | ✔️ |

## Étape suivante

- [Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr) pour une latence ultra-faible.
- [Jetons](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) : consultez la documentation sur les jetons.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
