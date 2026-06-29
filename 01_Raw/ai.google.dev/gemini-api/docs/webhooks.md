---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=fr
fetched_at: 2026-06-29T05:38:23.060471+00:00
title: "Webhooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Webhooks

Les webhooks permettent à l'API Gemini d'envoyer des notifications en temps réel à votre serveur lorsque des opérations asynchrones ou de longue durée (LRO) sont terminées. Cela évite d'interroger l'API pour obtenir des mises à jour de l'état, ce qui réduit la latence et la surcharge.

Les Webhooks sont disponibles pour des opérations telles que les tâches [Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr), les [interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) et la [génération de vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr).

## Fonctionnement

Au lieu d'interroger `GET /operations` à plusieurs reprises pour vérifier si un job est terminé, vous pouvez configurer les Webhooks de l'API Gemini pour qu'ils envoient une requête HTTP POST à votre URL d'écouteur immédiatement après le déclenchement d'un événement.

L'API Gemini permet de configurer les webhooks de deux manières :

- [**Webhooks statiques**](#static-webhooks) : points de terminaison au niveau du projet configurés avec l'[API WebhookService](https://ai.google.dev/api?hl=fr) de Gemini. Idéal pour les intégrations mondiales (par exemple, envoyer une notification Slack, synchroniser une base de données, etc.).
- [**Webhooks dynamiques**](#dynamic-webhooks) : remplacements au niveau de la requête transmettant une URL de webhook dans la charge utile de configuration d'un appel de jobs spécifique. Idéal pour acheminer des tâches spécifiques vers des points de terminaison dédiés.

## Webhooks statiques

Les webhooks statiques sont enregistrés pour un [projet](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#google-cloud-projects) entier et se déclenchent pour tout événement correspondant.

### Créer un webhook

Vous pouvez créer des points de terminaison à l'aide du SDK ou de l'API REST.

**IMPORTANT** : Lorsque vous créez un webhook, l'API renvoie un **secret de signature**
**une seule fois**. Vous devez stocker cette clé de manière sécurisée (par exemple, dans vos variables d'environnement) pour valider les signatures ultérieurement. Si vous perdez le code secret de signature, vous devrez le [faire pivoter](#rotate-signing-secret).

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

# Store webhook.new_signing_secret securely
webhook_secret = webhook.new_signing_secret
print(f"Created webhook: {webhook.name}, {webhook.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  // Store webhook.signingSecret securely
  const webhookSecret = webhook.new_signing_secret;
  console.log(`Created webhook: ${webhook.name}, ${webhook.id}`);
}

createWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "name": "MyBatchWebhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

Pour savoir comment configurer votre serveur afin qu'il reçoive des données, consultez la section [Gérer les requêtes de webhook](#handle-webhook-requests).

### Obtenir un webhook

Récupérez les détails d'un webhook spécifique à l'aide de son nom de ressource.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.get(id="<your_webhook_id>")

print(f"Webhook: {webhook.name}")
print(f"URI: {webhook.uri}")
print(f"Events: {webhook.subscribed_events}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI(); // Assumes process.env.GEMINI_API_KEY is set

async function getWebhook() {
  const webhook = await client.webhooks.get("<your_webhook_id>");

  console.log(`Webhook: ${webhook.name}`);
  console.log(`URI: ${webhook.uri}`);
  console.log(`Events: ${webhook.subscribed_events}`);
}

getWebhook();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Lister les webhooks

Répertorie tous les Webhooks configurés pour le projet en cours, avec une pagination facultative.

### Python

```
from google import genai

client = genai.Client()

webhooks = client.webhooks.list()

for wh in webhooks:
    print(f"{wh.id}: {wh.name} -> {wh.uri}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function listWebhooks() {
  const webhooks = await client.webhooks.list();

  for (const wh of webhooks) {
    console.log(`${wh.id}: ${wh.name} -> ${wh.uri}`);
  }
}

listWebhooks();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Mettre à jour un webhook

Mettez à jour les propriétés d'un webhook existant, telles que le nom à afficher, l'URI cible ou les événements auxquels il est abonné.

### Python

```
from google import genai

client = genai.Client()

updated_webhook = client.webhooks.update(
    id="<your_webhook_id>",
    subscribed_events=["batch.succeeded", "batch.failed", "batch.cancelled"],
)

print(f"Updated webhook: {updated_webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function updateWebhook() {
  const updatedWebhook = await client.webhooks.update(
    "<your_webhook_id>",
    {
      subscribed_events: ["batch.succeeded", "batch.failed", "batch.cancelled"],
    }
  );

  console.log(`Updated webhook: ${updatedWebhook.name}`);
}

updateWebhook();
```

### REST

```
curl -X PATCH \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "subscribed_events": ["batch.succeeded", "batch.failed", "batch.cancelled"]
  }'
```

### Supprimer un webhook

Supprimez un point de terminaison de webhook du projet. Cela empêche les futurs événements d'être envoyés à ce point de terminaison.

### Python

```
from google import genai

client = genai.Client()

client.webhooks.delete(id="<your_webhook_id>")

print("Webhook deleted.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function deleteWebhook() {
  await client.webhooks.delete("<your_webhook_id>");

  console.log("Webhook deleted.");
}

deleteWebhook();
```

### REST

```
curl -X DELETE \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Effectuer une rotation d'un secret de signature

Faites tourner le secret de signature d'un webhook. Vous pouvez configurer la révocation des secrets précédemment actifs immédiatement ou après un délai de grâce de 24 heures.

**IMPORTANT** : Le nouveau secret de signature n'est renvoyé qu'**une seule fois** lors de la rotation. Stockez-le de manière sécurisée avant de mettre à jour votre logique de validation.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.webhooks.rotate_signing_secret(
    id="<your_webhook_id>",
    revocation_behavior="REVOKE_PREVIOUS_SECRETS_AFTER_H24",
)

# Store response.secret securely, then update your server's verification config
print("New signing secret generated. Update your server configuration.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function rotateSigningSecret() {
  const response = await client.webhooks.rotateSigningSecret(
    "<your_webhook_id>",
    {
      revocation_behavior: "REVOKE_PREVIOUS_SECRETS_AFTER_H24",
    }
  );

  // Store response.secret securely, then update your server's verification config
  console.log("New signing secret generated. Update your server configuration.");
}

rotateSigningSecret();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>/rotate_secret" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "revocation_behavior": "REVOKE_PREVIOUS_SECRETS_AFTER_H24"
  }'
```

### Gérer les requêtes webhook sur un serveur

Lorsqu'un événement auquel vous êtes abonné se produit, votre URL de webhook reçoit une requête HTTP POST. Votre point de terminaison doit répondre avec un code d'état 2xx dans un délai de quelques secondes pour éviter une nouvelle tentative. Pour garantir la diffusion, l'API Gemini relance automatiquement les requêtes ayant échoué pendant 24 heures à l'aide d'un intervalle exponentiel entre les tentatives.

Gemini suit scrupuleusement la spécification [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) pour les en-têtes de sécurité. Validez la charge utile sur votre serveur à l'aide des signatures d'en-tête signé et de votre secret de signature statique stocké. Pour en savoir plus sur la charge utile, consultez la section [Enveloppe du webhook](#webhook-envelope).

Voici un exemple utilisant Flask pour l'écouteur HTTP :

### Python

```
# pip install flask standardwebhooks
import os
from flask import Flask, request, jsonify
# Standard verification wrapper for Standard Webhook Headers
from standardwebhooks.webhooks import Webhook, WebhookVerificationError

app = Flask(__name__)

SIGNING_SECRET = os.environ.get('WEBHOOK_SIGNING_SECRET')

@app.route('/gemini-callback', methods=['POST'])
def gemini_callback():
    payload = request.get_data(as_text=True)
    headers = request.headers

    try:
        wh = Webhook(SIGNING_SECRET)
        event = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        return jsonify({"error": "Signature invalid"}), 400

    # Process thin payload contents
    if event.get("type") == "batch.succeeded":
        print(f"Batch completed! ID: {event['data']['id']}")
        if event["data"].get("output_file_uri"):
            # For batch jobs with input file
            print(f"Batch file: {event['data']['output_file_uri']}")
    elif event.get("type") == "interaction.completed":
        print(f"Interaction completed! ID: {event['data']['id']}")
    elif event.get("type") == "video.generated":
        print(f"Video generated! URI: {event['data']['output_file_uri']}")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=8000)
```

### JavaScript

```
// npm install standardwebhooks
import { Webhook } from "standardwebhooks";
import express from "express";

const app = express();
const client = new GoogleGenAI({ webhookSecret: process.env.WEBHOOK_SIGNING_SECRET });

// Don't use express.json() because signature verification needs the raw text body
app.use(express.text({ type: "application/json" }));

app.post("/gemini-callback", async (req, res) => {
  const payload = await req.text();
        const headers: Record<string, string> = {};
        req.headers.forEach((value, key) => {
            headers[key] = value;
        });

        try {
            const wh = new Webhook(process.env.WEBHOOK_SIGNING_SECRET);
            const event = wh.verify(payload, headers) as Record<string, any>;
    console.log(`Event type: ${event.type}, data: ${JSON.stringify(event.data)}`);

            // Process thin payload contents
            if (event.type === "batch.succeeded") {
                console.log(`Batch completed! ID: ${event.data.id}`);
                if (event.data.output_file_uri) {
                    // For batch jobs with input file
                    console.log(`Batch file: ${event.data.output_file_uri}`);
                }
            } else if (event.type === "interaction.completed") {
                console.log(`Interaction completed! ID: ${event.data.id}`);
            } else if (event.type === "video.generated") {
                console.log(`Video generated! URI: ${event.data.output_file_uri}`);
            }

            res.status(200).json({ status: "received" });
        } catch (e) {
            console.error("Webhook verification failed:", e);
            res.status(400).send("Invalid signature");
        }
});

app.listen(8000, () => {
  console.log("Webhook server is running on port 8000");
});
```

## Webhooks dynamiques

Les webhooks dynamiques vous permettent d'associer un point de terminaison de webhook à une **configuration de requête spécifique**, ce qui est idéal pour les files d'attente d'orchestration d'agents. Les Webhooks dynamiques utilisent des signatures JWKS à clé publique asymétrique au lieu de secrets symétriques.

### Envoyer une requête dynamique

Ajoutez un `webhook_config` lorsque vous déclenchez un job asynchrone (par exemple, lorsque vous créez un lot).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

response = client.interactions.create(
    model='gemini-3.5-flash',
    input='Tell me a short joke about programming.',
    background=True, # Required when webhook_config is specified
    webhook_config={
        'uris': ["https://my-api.com/gemini-webhook-dynamic"],
        'user_metadata': {"job_group": "nightly-eval", "priority": "high"}
    }
)

print(f"Interaction created! ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createInteractionWithWebhook() {
  const response = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Tell me a short joke about programming.",
    background: true, // Required when webhook_config is specified
    webhook_config: {
      uris: ["https://my-api.com/gemini-webhook-dynamic"],
      user_metadata: { job_group: "nightly-eval", priority: "high" },
    },
  });

  console.log(`Interaction created! ID: ${response.id}`);
  console.log(`Status: ${response.status}`);
}

createInteractionWithWebhook();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a short joke about programming.",
    "background": true,
    "webhook_config": {
      "uris": ["https://my-api.com/gemini-webhook-dynamic"],
      "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
    }
  }'
```

### Valider les signatures dynamiques (JWKS)

Les requêtes de webhook dynamiques émettent une signature JSON Web Token (JWT). Votre écouteur doit extraire la signature et la valider à l'aide des [points de terminaison du certificat public de Google](https://www.googleapis.com/oauth2/v3/certs).

### Python

```
import jwt
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Google public cert list endpoint
JWKS_URI = "https://generativelanguage.googleapis.com/.well-known/jwks.json"

def load_google_public_key(kid):
    response = requests.get(JWKS_URI).json()
    for key_item in response.get('keys', []):
        if key_item.get('kid') == kid:
            # Convert JWK to Cert wrapper
            return jwt.algorithms.RSAAlgorithm.from_jwk(key_item)
    return None

@app.route('/gemini-webhook-dynamic', methods=['POST'])
def dynamic_handler():
    payload = request.get_data(as_text=True)
    headers = request.headers

    token = headers.get('Webhook-Signature')
    if not token:
        return jsonify({"error": "No signature header"}), 400

    try:
        # Extract kid from JWT header
        unverified_headers = jwt.get_unverified_header(token)
        pub_key = load_google_public_key(unverified_headers.get('kid'))

        if not pub_key:
            return jsonify({"error": "Key cert not found"}), 400

        # Verify Signature against expected audience (e.g., your project client ID)
        event = jwt.decode(
            token,
            pub_key,
            algorithms=["RS256"],
            audience="your-configured-audience"
        )
    except Exception as e:
        return jsonify({"error": "Invalid Dynamic signature", "details": str(e)}), 400

    print("Verified Dynamic payload success.")
    return jsonify({"status": "received"}), 200
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import express from "express";
import jwt from "jsonwebtoken";
import jwksClient from "jwks-rsa";

const app = express();
app.use(express.text({ type: 'application/json' }));

const client = jwksClient({
  jwksUri: "https://generativelanguage.googleapis.com/.well-known/jwks.json"
});

function getKey(header, callback) {
  client.getSigningKey(header.kid, (err, key) => {
    const signingKey = key.getPublicKey();
    callback(null, signingKey);
  });
}

app.post('/gemini-webhook-dynamic', (req, res) => {
  const token = req.headers['webhook-signature'];

  if (!token) {
    return res.status(400).json({ error: "No signature header" });
  }

  jwt.verify(
    token,
    getKey,
    {
      algorithms: ["RS256"],
      audience: "your-configured-audience"
    },
    (err, decoded) => {
      if (err) {
        return res.status(400).json({ error: "Invalid Dynamic signature", details: err.message });
      }

      console.log("Verified Dynamic payload success.");
      res.status(200).json({ status: "received" });
    }
  );
});
```

## Enveloppe de webhook

Pour éviter la congestion de la bande passante, les Webhooks Gemini utilisent un modèle de **charge utile légère** pour fournir des données. Les livraisons envoient un instantané contenant des informations sur l'état et des pointeurs vers les résultats, plutôt que le fichier de sortie brut lui-même.

Voici un exemple de format de charge utile :

```
{
  "type": "batch.succeeded",
  "version": "v1",
  "timestamp": "2026-01-22T12:00:00Z",
  "data": {
    "id": "batch_123456",
    "output_file_uri": "gs://my-bucket/results.jsonl"
  }
}
```

## Documentation de référence sur le catalogue d'événements

Les événements suivants sont déclenchés pour les jobs associés :

| Type d'événement | Déclencheur | Élément de charge utile (`data`) |
| --- | --- | --- |
| `batch.succeeded` | Le traitement s'est terminé avec succès. | `id`, `output_file_uri` |
| `batch.cancelled` | Demande annulée par l'utilisateur | `id` |
| `batch.expired` | Le lot n'a pas été traité (terminé) dans un délai de 24 heures | `id` |
| `batch.failed` | Échec du job par lot (erreur système ou de validation). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Appel de fonction, l'utilisateur doit effectuer une action | `id` |
| `interaction.completed` | LRO réussi dans l'API Interactions | `id` |
| `interaction.failed` | Échec de l'opération de longue durée dans l'API Interactions (erreur système ou de validation). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | LRO annulée dans l'API Interactions | `id` |
| `video.generated` | La génération de la vidéo LRO est terminée. | `id`, `output_file_uri`, `file_name` |

## Bonnes pratiques

Pour garantir un fonctionnement fiable et évolutif :

- **Vérification stricte de la protection contre la relecture** : toutes les requêtes comportent un en-tête `webhook-timestamp`. Validez toujours ce code temporel au niveau de la configuration de votre serveur pour rejeter les charges utiles plus anciennes que **5 minutes** (afin d'atténuer les attaques par relecture).
- **Traitez de manière asynchrone** : répondez avec `2xx OK` immédiatement après la détection d'une signature valide et mettez en file d'attente les opérations d'analyse en interne. Si l'auditeur maintient le doigt appuyé pendant une longue période, un cycle de nouvelle tentative de livraison se déclenche.
- **Gestion de la déduplication** : les Webhooks standards sont de type "au moins une fois". Utilisez l'en-tête `webhook-id` cohérent pour gérer les doublons potentiels dans les flux à forte congestion.

## Étape suivante

- [API Batch](https://ai.google.dev/gemini-api/docs/batch?hl=fr) : utilisez des Webhooks pour automatiser les points de terminaison à volume élevé.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/22 (UTC)."],[],[]]
