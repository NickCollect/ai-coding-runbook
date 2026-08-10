---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=fr
fetched_at: 2026-08-10T03:10:11.390035+00:00
title: "Gemini avec r\u00e9flexion \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Gemini avec réflexion

Les [modèles des séries Gemini 3 et 2.5](https://ai.google.dev/gemini-api/docs/models?hl=fr) utilisent un
"processus de réflexion" interne qui améliore considérablement leurs capacités de raisonnement et de planification en plusieurs étapes,
ce qui les rend très efficaces pour les tâches complexes telles que
le codage, les mathématiques avancées et l'analyse de données.

Ce guide vous explique comment utiliser les capacités de réflexion de Gemini à l'aide de l'API Gemini.

## Générer du contenu avec réflexion

Lancer une requête avec un modèle de réflexion est semblable à n'importe quelle autre requête de génération de contenu. La principale différence réside dans la spécification de l'un des
[modèles compatibles avec la réflexion](#supported-models) dans le `model` champ, comme
illustré dans l'exemple de [génération de texte](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#text-input) suivant :

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.6-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Résumés des réflexions

Les résumés des réflexions sont des versions résumées des réflexions brutes du modèle et offrent des insights sur le processus de raisonnement interne du modèle. Notez que les niveaux et les budgets de réflexion s'appliquent aux réflexions brutes du modèle, et non aux résumés des réflexions.

Vous pouvez activer les résumés des réflexions en définissant `includeThoughts` sur `true` dans la configuration de votre requête. Vous pouvez ensuite accéder au résumé en parcourant les `parts` du paramètre `response` et en cochant le booléen `thought`.

Voici un exemple qui montre comment activer et récupérer les résumés des réflexions sans streaming, ce qui renvoie un seul résumé final des réflexions avec la réponse :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Voici un exemple d'utilisation de la réflexion avec le streaming, qui renvoie des résumés progressifs et incrémentiels lors de la génération :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.6-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Contrôler la réflexion

Les modèles Gemini s'engagent dans une réflexion dynamique par défaut, en ajustant automatiquement l'effort de raisonnement en fonction de la complexité de la requête de l'utilisateur.
Toutefois, si vous avez des contraintes de latence spécifiques ou si vous avez besoin que le modèle s'engage dans un raisonnement plus approfondi que d'habitude, vous pouvez éventuellement utiliser des paramètres pour contrôler le comportement de la réflexion.

### Niveaux de réflexion (Gemini 3)

Le paramètre `thinkingLevel`, recommandé pour les modèles Gemini 3 et versions ultérieures, vous permet de contrôler le comportement de raisonnement.

Le tableau suivant détaille les paramètres `thinkingLevel` pour chaque type de modèle :

| Niveau de réflexion | Gemini 3.6 et 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 et 3.1 Flash-Lite | Image Gemini 3.1 Flash-Lite | Gemini 3 Flash | Description |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Compatible | Non compatible | Compatible (par défaut) | Compatible (par défaut) | Compatible | Correspond au paramètre "pas de réflexion" pour la plupart des requêtes. Notez que `minimal` ne garantit pas que la réflexion est désactivée. Le modèle peut raisonner de manière très minimale pour les tâches complexes. |
| **`low`** | Compatible | Compatible | Compatible | Non compatible | Compatible | Réduit la latence et les coûts. |
| **`medium`** | Compatible (par défaut) | Compatible | Compatible | Non compatible | Compatible | Réflexion équilibrée pour la plupart des tâches. |
| **`high`** | Compatible (dynamique) | Compatible (par défaut, dynamique) | Compatible (dynamique) | Compatible (dynamique) | Compatible (par défaut, dynamique) | Maximise la profondeur du raisonnement. Le modèle peut mettre beaucoup plus de temps à atteindre un premier jeton de sortie (sans réflexion), mais la sortie sera plus soigneusement raisonnée. |

L'exemple suivant montre comment définir le niveau de réflexion.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Vous ne pouvez pas désactiver la réflexion pour Gemini 3.1 Pro. Gemini 3 Flash et Flash-Lite
ne sont pas non plus compatibles avec la désactivation complète de la réflexion.
Si vous ne spécifiez pas de niveau de réflexion, Gemini utilise le niveau de réflexion par défaut des modèles Gemini 3 (par exemple, `"high"` pour Gemini 3.1 Pro et `"medium"` pour Gemini 3.5 Flash).

Les modèles de la série Gemini 2.5 ne sont pas compatibles avec `thinkingLevel`. Utilisez plutôt `thinkingBudget`.

### Budgets de réflexion

Le paramètre `thinkingBudget`, introduit avec la série Gemini 2.5, guide le modèle sur le nombre spécifique de jetons de réflexion à utiliser pour le raisonnement.

Vous trouverez ci-dessous les détails de configuration de `thinkingBudget` pour chaque type de modèle.
Vous pouvez désactiver la réflexion en définissant `thinkingBudget` sur 0.
Si vous définissez le `thinkingBudget` sur -1, vous activez la **réflexion dynamique**, ce qui signifie que le modèle ajuste le budget en fonction de la complexité de la requête.

| Modèle | Paramètre par défaut (le budget de réflexion n'est pas défini) | Plage | Désactiver la réflexion | Activer la réflexion dynamique |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Réflexion dynamique | `128` à `32768` | N/A : Impossible de désactiver la réflexion | `thinkingBudget = -1` (par défaut) |
| **2.5 Flash** | Réflexion dynamique | `0` à `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (par défaut) |
| **2.5 Flash Preview** | Réflexion dynamique | `0` à `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (par défaut) |
| **2.5 Flash Lite** | Le modèle ne réfléchit pas | `512` à `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | Le modèle ne réfléchit pas | `512` à `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | Réflexion dynamique | `0` à `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (par défaut) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Réflexion dynamique | `0` à `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (par défaut) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

En fonction du prompt, le modèle peut dépasser ou ne pas atteindre le budget de jetons.

## Signatures de réflexion

L'API Gemini est sans état. Le modèle traite donc chaque requête d'API indépendamment et n'a pas accès au contexte de réflexion des tours précédents dans les interactions multitours.

Pour permettre de maintenir le contexte de réflexion dans les interactions multitours, Gemini renvoie des signatures de réflexion, qui sont des représentations chiffrées du processus de réflexion interne du modèle.

- **Les modèles Gemini 2.5** renvoient des signatures de réflexion lorsque la réflexion est activée et
  que la requête inclut [un appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#thinking),
  en particulier [des déclarations de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#step-2).
- **Les modèles Gemini 3** peuvent renvoyer des signatures de réflexion pour tous les types de [parties](https://ai.google.dev/api/caching?hl=fr#Part).
  Nous vous recommandons de toujours renvoyer toutes les signatures telles qu'elles ont été reçues, mais cela est *obligatoire* pour les signatures d'appel de fonction. Pour en savoir plus, consultez la
  [page Signatures de réflexion](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=fr).

Les autres limites d'utilisation à prendre en compte avec l'appel de fonction incluent les suivantes :

- Les signatures sont renvoyées par le modèle dans d'autres parties de la réponse, par exemple des parties d'appel de fonction ou de texte.
  [Renvoyez la réponse complète](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#step-4)
  avec toutes les parties au modèle lors des tours suivants.
- Ne concaténez pas les parties avec des signatures.
- Ne fusionnez pas une partie avec une signature avec une autre partie sans signature.

## Tarifs

Lorsque la réflexion est activée, le prix de la réponse correspond à la somme des jetons de sortie et des jetons de réflexion. Vous pouvez obtenir le nombre total de jetons de réflexion générés à partir du champ `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Les modèles de réflexion génèrent des réflexions complètes pour améliorer la qualité de la réponse finale, puis génèrent des [résumés](#summaries) pour fournir des insights sur le processus de réflexion. La tarification est donc basée sur les jetons de réflexion complets que le modèle doit générer pour créer un résumé, même si seul le résumé est généré par l'API.

Pour en savoir plus sur les jetons, consultez le [guide](https://ai.google.dev/gemini-api/docs/tokens?hl=fr)
Comptage des jetons.

## Bonnes pratiques

Cette section fournit quelques conseils pour utiliser efficacement les modèles de réflexion.
Comme toujours, vous obtiendrez les meilleurs résultats en suivant nos [conseils et bonnes pratiques pour la rédaction de requêtes](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr).

### Débogage et orientation

- **Examiner le raisonnement** : lorsque vous n'obtenez pas la réponse attendue des
  modèles de réflexion, il peut être utile d'analyser attentivement les résumés des réflexions de Gemini.
  Vous pouvez voir comment il a décomposé la tâche et est parvenu à sa conclusion, et utiliser ces informations pour corriger les résultats.
- **Fournir des conseils dans le raisonnement** : si vous espérez obtenir une sortie particulièrement longue, vous pouvez fournir des conseils dans votre prompt afin de limiter la
  [réflexion](#set-budget) utilisée par le modèle. Vous réservez ainsi une plus grande partie de la sortie de jeton pour votre réponse.

### Complexité des tâches

- **Tâches simples (la réflexion peut être désactivée)** : pour les requêtes simples qui ne nécessitent pas de raisonnement complexe, telles que la récupération ou la classification de faits, la réflexion n'est pas nécessaire. Exemples :
  - "Où DeepMind a-t-il été fondé ?"
  - "Cet e-mail demande-t-il une réunion ou fournit-il simplement des informations ?"
- **Tâches moyennes (par défaut/certaine réflexion)** : de nombreuses requêtes courantes bénéficient d'un traitement étape par étape ou d'une compréhension plus approfondie. Gemini peut utiliser de manière flexible la capacité de réflexion pour des tâches telles que :
  - Comparer la photosynthèse et la croissance.
  - Comparer les voitures électriques et les voitures hybrides.
- **Tâches difficiles (capacité de réflexion maximale)** : pour les défis vraiment complexes, tels que la résolution de problèmes mathématiques complexes ou les tâches de codage, nous vous recommandons de définir un budget de réflexion élevé. Ces types de tâches nécessitent que le modèle utilise toutes ses capacités de raisonnement et de planification, ce qui implique souvent de nombreuses étapes internes avant de fournir une réponse. Exemples :
  - Résolvez le problème 1 de l'AIME 2025 : trouvez la somme de toutes les bases entières b > 9 pour
    lesquelles 17b est un diviseur de 97b.
  - Écrivez du code Python pour une application Web qui visualise les données boursières en temps réel, y compris l'authentification des utilisateurs. Rendez-le aussi efficace que possible.

## Modèles, outils et fonctionnalités compatibles

Les fonctionnalités de réflexion sont compatibles avec tous les modèles des séries 3 et 2.5.
Vous trouverez toutes les fonctionnalités des modèles sur la
[page de présentation des modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr).

Les modèles de réflexion fonctionnent avec tous les outils et fonctionnalités de Gemini. Cela permet aux modèles d'interagir avec des systèmes externes, d'exécuter du code ou d'accéder à des informations en temps réel, en intégrant les résultats dans leur raisonnement et leur réponse finale.

Vous pouvez essayer des exemples d'utilisation d'outils avec des modèles de réflexion dans le [recueil de recettes de réflexion][Colab].

## Étape suivante

- La couverture de la réflexion est disponible dans notre [guide de compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
