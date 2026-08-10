---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/flex-inference?hl=fr
fetched_at: 2026-08-10T03:23:30.977146+00:00
title: "Inf\u00e9rence flexible \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Inférence flexible

Description : Découvrez comment optimiser les coûts avec le niveau d'inférence Flex

L'API Gemini Flex est un niveau d'inférence qui offre une réduction des coûts de 50% par rapport aux tarifs standards, en échange d'une latence variable et d'une disponibilité optimale. Elle est conçue pour les charges de travail tolérantes à la latence qui nécessitent un traitement synchrone, mais qui n'ont pas besoin des performances en temps réel de l'API standard.

## Utiliser Flex

Pour utiliser le niveau Flex, spécifiez `service_tier` comme `flex` dans le corps de la requête. Par défaut, les requêtes utilisent le niveau standard si ce champ est omis.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3.6-flash",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## Fonctionnement de l'inférence Flex

L'inférence Gemini Flex comble le fossé entre l'API standard et le délai de traitement de 24 heures
de l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr). Elle utilise une capacité de calcul "détachable" en dehors des heures de pointe pour fournir une solution économique pour les tâches en arrière-plan et les workflows séquentiels.

| Fonctionnalité | Flex | Priorité | Standard | Lot |
| --- | --- | --- | --- | --- |
| **Tarifs** | 50% de remise | 75 à 100% de plus que le niveau Standard | Plein tarif | 50% de remise |
| **Latence** | Minutes (cible de 1 à 15 minutes) | Faible (secondes) | Secondes à minutes | Jusqu'à 24 heures |
| **Fiabilité** | Optimisation limitée (détachable) | Élevée (non détachable) | Élevée / Moyenne haute | Élevée (pour le débit) |
| **Interface** | Synchrone | Synchrone | Synchrone | Asynchrone |

### Principaux avantages

- **Rentabilité** : économies substantielles pour les évaluations hors production, les agents en arrière-plan et l'enrichissement des données.
- **Faible friction** : pas besoin de gérer les objets par lot, les ID de tâche ni l'interrogation. Il vous suffit d'ajouter un seul paramètre à vos requêtes existantes.
- **Workflows synchrones** : idéal pour les chaînes d'API séquentielles où la requête suivante dépend du résultat de la précédente, ce qui la rend plus flexible que Batch pour les workflows agentiques.

### Cas d'utilisation

- **Évaluations hors connexion** : exécution de tests de régression ou de classements « LLM-as-a-judge ».
- **Agents en arrière-plan** : tâches séquentielles telles que les mises à jour CRM, la création de profils ou la modération de contenu où quelques minutes de délai sont acceptables.
- **Recherche avec budget limité** : expériences universitaires nécessitant un volume de jetons élevé avec un budget limité.

### Limites de débit

Le trafic d'inférence Flex est comptabilisé dans vos [limites de débit](https://aistudio.google.com/rate-limit?hl=fr) générales. Il n'offre pas
de limites de débit étendues comme l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr).

### Capacité détachable

Le trafic Flex est traité avec une priorité inférieure. En cas de pic de trafic standard, les requêtes Flex peuvent être préemptées ou supprimées pour garantir la capacité des utilisateurs prioritaires. Si vous recherchez une inférence prioritaire, consultez la section
[Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr)

### Codes d'erreur

Lorsque la capacité Flex n'est pas disponible ou que le système est saturé, l'API renvoie des codes d'erreur standards :

- **503 Service indisponible** : le système a atteint sa capacité maximale.
- **429 Trop de requêtes** : limites de débit ou épuisement des ressources.

### Responsabilité du client

- **Aucune reprise en cas d'échec côté serveur** : pour éviter les frais inattendus, le système ne
  met pas automatiquement à niveau une requête Flex vers le niveau Standard si la capacité Flex est
  pleine.
- **Nouvelles tentatives** : vous devez implémenter votre propre logique de nouvelle tentative côté client avec
  un intervalle exponentiel entre les tentatives.
- **Délais avant expiration** : étant donné que les requêtes Flex peuvent se trouver dans une file d'attente, nous vous recommandons
  d’augmenter les délais avant expiration côté client à 10 minutes ou plus pour éviter une
  fermeture prématurée de la connexion.

## Ajuster les fenêtres de délai avant expiration

Vous pouvez configurer des délais avant expiration par requête pour l'API REST et les bibliothèques clientes, et des délais avant expiration globaux uniquement lorsque vous utilisez les bibliothèques clientes.

Assurez-vous toujours que votre délai avant expiration côté client couvre la fenêtre de patience du serveur prévue (par exemple, 600 secondes ou plus pour les files d'attente Flex). Les SDK attendent des valeurs de délai avant expiration en millisecondes.

### Délais avant expiration par requête

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3.6-flash",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3.6-flash",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3.6-flash",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
     }
 }

 await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3.6-flash",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3.6-flash",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

Lorsque vous effectuez des appels REST, vous pouvez contrôler les délais avant expiration à l'aide d'une combinaison d'en-têtes HTTP et d'options `curl` :

- **En-tête `X-Server-Timeout` (délai avant expiration côté serveur)** : cet en-tête suggère une durée de délai avant expiration préférée (600 secondes par défaut) au serveur d'API Gemini. Le serveur tentera de respecter cette valeur, mais cela n'est pas garanti. La valeur doit être exprimée en secondes.
- **`--max-time` dans `curl` (délai avant expiration côté client)** : l'option `curl --max-time
  <seconds>` définit une limite stricte sur le temps total (en secondes) pendant lequel `curl`
  attendra la fin de l'opération. Il s'agit d'une protection côté client.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### Délais avant expiration globaux

Si vous souhaitez que tous les appels d'API effectués via une instance `genai.Client` spécifique (bibliothèques clientes uniquement) aient un délai avant expiration par défaut, vous pouvez le configurer lors de l'initialisation du client à l'aide de `http_options` et `genai.types.HttpOptions`.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.6-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.6-flash",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.6-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.6-flash",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
    }
}

await main();
```

### Go

```
 package main

 import (
     "context"
     "fmt"
     "log"
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3.6-flash")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
```

## Implémenter des nouvelles tentatives

Étant donné que Flex est détachable et échoue avec des erreurs 503, voici un exemple d'implémentation facultative d'une logique de nouvelle tentative pour poursuivre les requêtes ayant échoué :

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.6-flash",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3.6-flash",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3.6-flash",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
 }

 await main();
```

### Go

```
 package main

 import (
     "context"
     "fmt"
     "log"
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3.6-flash"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
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
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) | ✔️ |
| [Preview Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr) | ✔️ |
| [Preview Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=fr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fr) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=fr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fr) | ✔️ |

## Étape suivante

Découvrez les autres options d' [inférence et d'optimisation](https://ai.google.dev/gemini-api/docs/optimization?hl=fr) de Gemini :

- [Inférence prioritaire](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fr) pour une latence ultra-faible.
- [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr) pour le traitement asynchrone sous 24 heures.
- [Mise en cache de contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) pour réduire les coûts des jetons d'entrée.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
