---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=fr
fetched_at: 2026-08-24T02:37:26.739769+00:00
title: "Gemini avec r\u00e9flexion \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Gemini avec réflexion

Les modèles des séries [Gemini 3 et 2.5](https://ai.google.dev/gemini-api/docs/models?hl=fr) utilisent un
"processus de réflexion" qui améliore considérablement leurs capacités de raisonnement et de planification en plusieurs étapes,
ce qui les rend très efficaces pour les tâches complexes telles que
la programmation, les mathématiques avancées et l'analyse de données.

Lorsque vous utilisez un modèle de réflexion, Gemini raisonne en interne avant de répondre. L'API Interactions met en évidence ce raisonnement via des étapes `thought` dédiées qui apparaissent de manière chronologique à côté des appels de fonction, des entrées utilisateur ou des sorties de modèle dans le tableau `steps`.

Chaque étape de réflexion contient deux champs :

| Champ | Obligatoire | Description |
| --- | --- | --- |
| `signature` | ✅ Oui | Représentation chiffrée de l'état de raisonnement interne du modèle. Toujours présent, même lorsque le modèle effectue un raisonnement minimal. |
| `summary` | ❌ Non | Tableau de contenu (texte et/ou images) résumant le raisonnement. Peut être vide en fonction de la [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=fr) config, du fait que le modèle a effectué suffisamment de raisonnement ou du type de contenu (par exemple, les latents d'image peuvent ne pas avoir de résumés de texte). |

## Interactions avec la réflexion

Lancer une interaction avec un modèle de réflexion est semblable à toute autre requête d'interaction. Spécifiez l'un des [modèles compatibles avec la réflexion](#thinking-levels) dans le `model` champ :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Résumés des réflexions

Les résumés des réflexions fournissent des insights sur le processus de raisonnement interne du modèle.
Par défaut, seule la sortie finale est renvoyée. Vous pouvez activer les résumés des réflexions avec `thinking_summaries` :

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Un bloc de réflexion peut contenir **uniquement une signature sans résumé** dans les cas suivants :

- Requêtes simples, où le modèle n'a pas suffisamment raisonné pour générer un résumé
- `thinking_summaries: "none"`, où les résumés sont explicitement désactivés
- Certains types de contenu de réflexion, tels que les images, peuvent ne pas avoir de résumés de texte

Votre code doit toujours gérer les blocs de réflexion où `summary` est vide ou absent.

## Streaming avec réflexion

Utilisez le streaming pour recevoir des résumés de réflexion incrémentiels lors de la génération.
Les blocs de réflexion sont fournis à l'aide d'événements envoyés par le serveur (SSE) avec deux types de delta distincts :

| Type de delta | Contient | Quand les données sont envoyées |
| --- | --- | --- |
| `thought_summary` | Contenu du résumé de texte ou d'image | Un ou plusieurs deltas avec un résumé incrémentiel |
| `thought_signature` | La signature cryptographique | le dernier delta avant `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

La réponse en streaming utilise des événements envoyés par le serveur (SSE) et se compose d'étapes et d'événements, par exemple :

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Contrôler la réflexion

Les modèles Gemini s'engagent dans une réflexion dynamique par défaut, en ajustant automatiquement la quantité d'efforts de raisonnement en fonction de la complexité de la requête. Vous pouvez contrôler ce comportement à l'aide du paramètre `thinking_level`.

| Modèle | Réflexion par défaut | Niveaux compatibles |
| --- | --- | --- |
| gemini-3.6-flash | Activé (moyen) | minimal, faible, moyen, élevé |
| gemini-3.5-flash-lite | Activé (minimal) | minimal, faible, moyen, élevé |
| gemini-3.1-pro-preview | Activé (élevé) | faible, moyen, élevé |
| gemini-3.1-flash-lite-image | Activé (minimal) | minimal, élevé |
| gemini-3-flash-preview | Activé (élevé) | minimal, faible, moyen, élevé |
| gemini-3-pro-preview | Activé (élevé) | faible, élevé |
| gemini-3.5-flash | Activé (moyen) | minimal, faible, moyen, élevé |
| gemini-2.5-pro | Activé | faible, moyen, élevé |
| gemini-2.5-flash | Activé | faible, moyen, élevé |
| gemini-2.5-flash-lite | Désactivé | faible, moyen, élevé |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Signatures de réflexion

Les signatures de réflexion sont des représentations chiffrées du raisonnement interne du modèle. Elles sont nécessaires pour maintenir la continuité du raisonnement dans les interactions multitours.

L'API Interactions simplifie considérablement la gestion des signatures de réflexion par rapport à l'API `generateContent`.

### Mode avec état (recommandé)

Par défaut, lorsque vous utilisez l'API Interactions en mode avec état (en définissant `store: true` et en transmettant le `previous_interaction_id` dans les tours suivants), le serveur gère automatiquement l'état de la conversation, y compris tous les blocs de réflexion et les signatures. Dans ce mode, vous n'avez rien à faire concernant les signatures. Elles sont entièrement gérées côté serveur.

### Mode sans état

Si vous gérez vous-même l'état de la conversation (mode sans état) et que vous transmettez l'historique complet des entrées et des sorties dans chaque requête :

- Vous **DEVEZ** toujours renvoyer tous les blocs `thought` exactement tels qu'ils ont été reçus du modèle.
- Vous **NE DEVEZ PAS** supprimer ni modifier les blocs de réflexion de l'historique, car ils contiennent les signatures requises pour que le modèle poursuive son raisonnement.
- Lorsque vous changez de modèle au cours d'une session, vous devez toujours renvoyer les blocs de réflexion du modèle précédent. Le backend gère la compatibilité.

## Tarifs

Lorsque la réflexion est activée, le prix de la réponse correspond à la somme des jetons de sortie et des jetons de réflexion. Vous pouvez obtenir le nombre total de jetons de réflexion générés à partir du champ `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Les modèles de réflexion génèrent des réflexions complètes pour améliorer la qualité de la réponse finale, puis génèrent des [résumés](#summaries) pour fournir des insights sur le processus de réflexion. La tarification est basée sur les jetons de réflexion complets que le modèle doit générer, même si seul le résumé est généré par l'API.

Pour en savoir plus sur les jetons, consultez le guide sur le [comptage des jetons](https://ai.google.dev/gemini-api/docs/tokens?hl=fr).

## Bonnes pratiques

Utilisez efficacement les modèles de réflexion en suivant ces consignes.

- **Examiner le raisonnement** : analysez les résumés des réflexions pour comprendre les échecs et améliorer les requêtes.
- **Contrôler le budget de réflexion** : demandez au modèle de moins réfléchir pour les sorties longues afin d'économiser des jetons.
- **Tâches simples** : utilisez une réflexion minimale ou faible pour la récupération ou la classification de faits (par exemple, « Où DeepMind a-t-il été fondé ? »).
- **Tâches modérées** : utilisez la réflexion par défaut pour comparer des concepts ou un raisonnement créatif (par exemple, comparer les voitures électriques et hybrides).
- **Tâches complexes** : utilisez une réflexion maximale pour la programmation avancée, les mathématiques ou la planification en plusieurs étapes (par exemple, résoudre des problèmes mathématiques AIME).

## Étape suivante

- [Génération de texte](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr) : réponses textuelles de base
- [Appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) : se connecter à des outils
- [Guide Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=fr) : fonctionnalités spécifiques au modèle

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
