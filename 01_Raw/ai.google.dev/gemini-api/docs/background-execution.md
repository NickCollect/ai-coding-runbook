---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=fr
fetched_at: 2026-08-24T02:28:37.140762+00:00
title: "Ex\u00e9cution en arri\u00e8re-plan \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Exécution en arrière-plan

Pour les tâches de longue durée, telles que la recherche approfondie, le raisonnement complexe ou les exécutions d'agents en plusieurs étapes, les délais d'expiration des connexions peuvent interrompre les requêtes HTTP standards (qui se ferment généralement après 60 secondes). L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) fournit une **exécution en arrière-plan** pour exécuter ces tâches de manière asynchrone.

Pour que l'interaction s'exécute jusqu'à ce qu'elle termine la tâche sur le serveur, définissez `"background": true` lors de la création de l'interaction. L'API renvoie immédiatement un ID d'interaction, que les applications clientes peuvent utiliser pour interroger l'état, diffuser la progression ou se reconnecter à un flux déconnecté.

L'exécution en arrière-plan est compatible avec les modèles Gemini standards (tels que `gemini-3.6-flash` et `gemini-3.1-pro-preview`) et les agents gérés (tels que `antigravity-preview-05-2026`).

## Créer une interaction en arrière-plan

Pour démarrer une interaction en arrière-plan, définissez le paramètre `background` sur `true` lors de la création de la ressource.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## Fonctionnement de l'exécution en arrière-plan

Lorsque vous créez une interaction en arrière-plan, la tâche s'exécute de manière asynchrone sur le serveur. L'interaction passe par différents états d'exécution :

- `in_progress` : le serveur exécute activement l'interaction (par exemple, en exécutant du code ou en effectuant des recherches).
- `requires_action` : l'interaction est mise en pause et attend une entrée du client (par exemple, la confirmation de l'exécution d'un outil ou la réponse à une question).
- `completed` : l'interaction s'est terminée correctement et la sortie est disponible.
- `failed` : une erreur s'est produite lors de l'exécution (par exemple, un échec d'outil ou des limites de débit).
- `cancelled` : une requête client a arrêté l'exécution.

### Cas d'utilisation

Utilisez l'exécution en arrière-plan pour :

- **Exécutions d'agents** : tâches nécessitant l'exécution de code, la navigation sur le Web ou l'orchestration de sous-agents (telles que `antigravity-preview-05-2026`).
- **Recherche approfondie** : exécutions utilisant `deep-research-preview-04-2026` ou `deep-research-max-preview-04-2026`, qui prennent plusieurs minutes.
- **Raisonnement long** : tâches dans lesquelles les étapes de réflexion du modèle dépassent les limites de connexion HTTP standards.

## Récupérer les résultats

Obtenez les résultats d'une interaction en arrière-plan à l'aide de **l'interrogation** ou du **streaming**.

### Modèle d'interrogation (non bloquant)

L'interrogation vérifie régulièrement l'état de l'interaction à l'aide de requêtes GET non bloquantes jusqu'à ce qu'elle atteigne un état final.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### Modèle de streaming

Si une interruption du réseau déconnecte un flux, le streaming peut reprendre à partir du dernier événement reçu. Chaque delta contient un `event_id` unique dans sa charge utile. Le fait de transmettre cet ID en tant que `last_event_id` reprend le flux à partir de cet événement.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Conversations multitours

Les interactions suivantes peuvent être enchaînées à une conversation en arrière-plan à l'aide de `previous_interaction_id`, sous réserve des contraintes suivantes :

1. **Les exécutions actives sont bloquées** : l'enchaînement d'une interaction suivante à une interaction dont l'état est `in_progress` renvoie une erreur `400 Bad Request`. Attendez que l'interaction atteigne l'état `completed` avant de démarrer la suivante.
2. **Paramètre d'environnement pour les agents gérés** : lorsque vous enchaînez des interactions pour des agents gérés (tels que `antigravity-preview-05-2026`), les requêtes doivent inclure à la fois `previous_interaction_id` et `environment`.

Les exemples suivants montrent comment enchaîner des interactions :

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## Annulation et suppression

Contrôlez les exécutions en cours et gérez le stockage à l'aide des requêtes d'annulation et de suppression :

- **Annuler (`POST /interactions/{id}/cancel`)** : arrête la tâche en cours d'exécution. L'état passe à `cancelled`. Les actions de nettoyage sur le serveur peuvent entraîner un léger délai avant que l'état ne soit mis à jour dans les requêtes GET.
- **Supprimer (`DELETE /interactions/{id}`)** : supprime les enregistrements d'interaction du serveur. Les requêtes GET suivantes renvoient une erreur `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Étapes suivantes

- Consultez la [présentation de l'API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) pour comprendre la gestion des sessions et des états.
- Consultez le guide [Interactions de streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=fr) pour en savoir plus sur les mises à jour des événements en temps réel.
- Découvrez le [guide de démarrage rapide Agents gérés](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr) pour créer des agents multitours avec état.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/30 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/30 (UTC)."],[],[]]
