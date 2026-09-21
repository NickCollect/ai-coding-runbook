---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=fr
fetched_at: 2026-09-21T05:51:28.572427+00:00
title: "Webhooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Webhooks

Les webhooks permettent à l'API Gemini d'envoyer des notifications en temps réel à votre serveur lorsque des opérations asynchrones ou de longue durée (LRO) sont terminées. Vous n'avez ainsi plus besoin d'interroger l'API pour obtenir des mises à jour de l'état, ce qui réduit la latence et la surcharge.

Les webhooks sont disponibles pour des opérations telles que les tâches [par lot](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr),
[les interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) et [la génération de vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr).

## Fonctionnement

Au lieu d'interroger `GET /operations` de manière répétée pour vérifier si une tâche est terminée, vous pouvez configurer les webhooks de l'API Gemini pour qu'ils envoient une requête HTTP POST à l'URL de votre écouteur immédiatement après le déclenchement d'un événement.

L'API Gemini permet de configurer les webhooks de deux manières :

- [**Webhooks statiques**](#static-webhooks) : points de terminaison au niveau du projet configurés
  avec l'API Gemini [WebhookService](https://ai.google.dev/api?hl=fr). Idéal pour les intégrations globales (par exemple, pour envoyer des notifications à Slack, synchroniser une base de données, etc.).
- [**Webhooks dynamiques**](#dynamic-webhooks) : remplacements au niveau de la requête qui transmettent une
  URL de webhook dans la charge utile de configuration d'un appel de tâches spécifique. Idéal pour acheminer des tâches spécifiques vers des points de terminaison dédiés.

## Webhooks statiques

Les webhooks statiques sont enregistrés pour l'ensemble d'un [projet](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#google-cloud-projects) et se déclenchent pour tout événement
correspondant.

### Créer un webhook

Vous pouvez créer des points de terminaison à l'aide du SDK ou de l'API REST.

**IMPORTANT** : Lorsque vous créez un webhook, l'API renvoie un **secret de signature**
**une seule fois**. Vous devez le stocker de manière sécurisée (par exemple, dans vos variables d'environnement) pour vérifier les signatures ultérieurement. Si vous perdez le secret de signature, vous devrez le
[faire pivoter](#rotate-signing-secret).

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookInput;
import com.google.genai.gaos.models.webhooks.WebhookSubscribedEvent;
import java.util.Arrays;

Client client = new Client();

WebhookInput input =
    WebhookInput.builder()
        .name("MyBatchWebhook")
        .subscribedEvents(
            Arrays.asList(
                WebhookSubscribedEvent.BATCH_SUCCEEDED, WebhookSubscribedEvent.BATCH_FAILED))
        .uri("https://my-api.com/gemini-callback")
        .build();

Webhook webhook = client.webhooks.create(input).webhook().get();

// Store webhook.newSigningSecret() securely
String webhookSecret = webhook.newSigningSecret().orElse("");
System.out.println(
    "Created webhook: " + webhook.name().orElse("") + ", " + webhook.id().orElse(""));
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

Pour savoir comment configurer votre serveur afin qu'il reçoive des données, consultez la
[section Gérer les requêtes de webhook](#handle-webhook-requests).

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import java.util.Collections;

Client client = new Client();

Webhook webhook = client.webhooks.get("<your_webhook_id>").webhook().get();

System.out.println("Webhook: " + webhook.name().orElse(""));
System.out.println("URI: " + webhook.uri().orElse(""));
System.out.println("Events: " + webhook.subscribedEvents().orElse(Collections.emptyList()));
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Répertorier les webhooks

Répertoriez tous les webhooks configurés pour le projet en cours, avec pagination facultative.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookListResponse;
import java.util.Collections;

Client client = new Client();

WebhookListResponse response =
    client.webhooks.listDirect().webhookListResponse().orElse(new WebhookListResponse());

for (Webhook wh : response.webhooks().orElse(Collections.emptyList())) {
  System.out.println(
      wh.id().orElse("") + ": " + wh.name().orElse("") + " -> " + wh.uri().orElse(""));
}
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookUpdate;
import com.google.genai.gaos.models.webhooks.WebhookUpdateSubscribedEvent;
import java.util.Arrays;

Client client = new Client();

WebhookUpdate updateBody =
    WebhookUpdate.builder()
        .subscribedEvents(
            Arrays.asList(
                WebhookUpdateSubscribedEvent.BATCH_SUCCEEDED,
                WebhookUpdateSubscribedEvent.BATCH_FAILED,
                WebhookUpdateSubscribedEvent.of("batch.cancelled")))
        .build();

Webhook updatedWebhook =
    client.webhooks
        .update()
        .id("<your_webhook_id>")
        .updateMask("subscribed_events")
        .body(updateBody)
        .call()
        .webhook()
        .get();

System.out.println("Updated webhook: " + updatedWebhook.name().orElse(""));
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

Supprimez un point de terminaison de webhook du projet. Les événements ne seront plus envoyés à ce point de terminaison.

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

### Java

```
import com.google.genai.Client;

Client client = new Client();

client.webhooks.delete("<your_webhook_id>");

System.out.println("Webhook deleted.");
```

### REST

```
curl -X DELETE \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Faire pivoter un secret de signature

Faites pivoter le secret de signature d'un webhook. Vous pouvez configurer si les secrets précédemment actifs sont révoqués immédiatement ou après un délai de grâce de 24 heures.

**IMPORTANT** : Le nouveau secret de signature n'est renvoyé qu'**une seule fois** au moment de la rotation
time. Stockez-le de manière sécurisée avant de mettre à jour votre logique de validation.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.RevocationBehavior;
import com.google.genai.gaos.models.webhooks.RotateSigningSecretRequest;
import com.google.genai.gaos.models.webhooks.WebhookRotateSigningSecretResponse;

Client client = new Client();

RotateSigningSecretRequest requestBody =
    RotateSigningSecretRequest.builder()
        .revocationBehavior(RevocationBehavior.REVOKE_PREVIOUS_SECRETS_AFTER_H24)
        .build();

WebhookRotateSigningSecretResponse response =
    client.webhooks
        .rotateSigningSecret()
        .id("<your_webhook_id>")
        .body(requestBody)
        .call()
        .webhookRotateSigningSecretResponse()
        .get();

// Store response.secret() securely, then update your server's verification config
String newSecret = response.secret().orElse("");
System.out.println("New signing secret generated. Update your server configuration.");
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

### Gérer les requêtes de webhook sur un serveur

Lorsqu'un événement auquel vous êtes abonné se produit, votre URL de webhook reçoit une requête HTTP POST. Votre point de terminaison doit répondre avec un code d'état 2xx dans les quelques secondes pour éviter une nouvelle tentative. Pour garantir la diffusion, l'API Gemini relance automatiquement les requêtes ayant échoué pendant 24 heures à l'aide d'un intervalle exponentiel entre les tentatives.

Gemini respecte strictement la spécification des [webhooks standards](https://github.com/standard-webhooks/standard-webhooks) pour
les en-têtes de sécurité. Vérifiez la charge utile sur votre serveur à l'aide des signatures d'en-tête signées et de votre secret de signature statique stocké. Pour obtenir des informations sur la charge utile, consultez la section [Enveloppe de webhook](#webhook-envelope).

Voici un exemple d'utilisation de Flask pour l'écouteur HTTP :

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

### Java

```
import com.sun.net.httpserver.HttpServer;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

String signingSecret = System.getenv("WEBHOOK_SIGNING_SECRET");

HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
server.createContext(
    "/gemini-callback",
    exchange -> {
      String payload =
          new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
      String msgId = exchange.getRequestHeaders().getFirst("webhook-id");
      String msgTimestamp = exchange.getRequestHeaders().getFirst("webhook-timestamp");
      String msgSignature = exchange.getRequestHeaders().getFirst("webhook-signature");

      try {
        String toSign = msgId + "." + msgTimestamp + "." + payload;
        Mac mac = Mac.getInstance("HmacSHA256");
        byte[] secretBytes =
            Base64.getDecoder().decode(signingSecret.replaceFirst("^whsec_", ""));
        mac.init(new SecretKeySpec(secretBytes, "HmacSHA256"));
        String expectedSig =
            "v1,"
                + Base64.getEncoder()
                    .encodeToString(mac.doFinal(toSign.getBytes(StandardCharsets.UTF_8)));

        if (msgSignature == null || !msgSignature.contains(expectedSig)) {
          byte[] resp = "{\"error\": \"Signature invalid\"}".getBytes(StandardCharsets.UTF_8);
          exchange.sendResponseHeaders(400, resp.length);
          try (OutputStream os = exchange.getResponseBody()) {
            os.write(resp);
          }
          return;
        }

        Matcher typeMatcher = Pattern.compile("\"type\"\\s*:\\s*\"([^\"]+)\"").matcher(payload);
        String type = typeMatcher.find() ? typeMatcher.group(1) : "";

        Matcher idMatcher = Pattern.compile("\"id\"\\s*:\\s*\"([^\"]+)\"").matcher(payload);
        String id = idMatcher.find() ? idMatcher.group(1) : "";

        Matcher uriMatcher =
            Pattern.compile("\"output_file_uri\"\\s*:\\s*\"([^\"]+)\"").matcher(payload);
        String outputFileUri = uriMatcher.find() ? uriMatcher.group(1) : "";

        if ("batch.succeeded".equals(type)) {
          System.out.println("Batch completed! ID: " + id);
          if (!outputFileUri.isEmpty()) {
            System.out.println("Batch file: " + outputFileUri);
          }
        } else if ("interaction.completed".equals(type)) {
          System.out.println("Interaction completed! ID: " + id);
        } else if ("video.generated".equals(type)) {
          System.out.println("Video generated! URI: " + outputFileUri);
        }

        byte[] resp = "{\"status\": \"received\"}".getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(200, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
      } catch (Exception e) {
        exchange.sendResponseHeaders(400, -1);
      }
    });
server.start();
```

## Webhooks dynamiques

Les webhooks dynamiques vous permettent de lier un point de terminaison de webhook à une **configuration de requête
spécifique**, ce qui est idéal pour les files d'attente d'orchestration d'agents. Les webhooks dynamiques utilisent des signatures JWKS de clé publique asymétriques au lieu de secrets symétriques.

### Envoyer une requête dynamique

Ajoutez un `webhook_config` lorsque vous déclenchez une tâche asynchrone (par exemple, lorsque vous créez un lot).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

response = client.interactions.create(
    model='gemini-3.8-flash',
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.WebhookConfig;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> userMetadata = new HashMap<>();
userMetadata.put("job_group", "nightly-eval");
userMetadata.put("priority", "high");

WebhookConfig webhookConfig =
    WebhookConfig.builder()
        .uris(Arrays.asList("https://my-api.com/gemini-webhook-dynamic"))
        .userMetadata(userMetadata)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Tell me a short joke about programming."))
        .background(true) // Required when webhookConfig is specified
        .webhookConfig(webhookConfig)
        .build();

Interaction response =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Interaction created! ID: " + response.id().orElse(""));
System.out.println(
    "Status: " + response.status().map(InteractionStatus::value).orElse(""));
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short joke about programming.",
    "background": true,
    "webhook_config": {
      "uris": ["https://my-api.com/gemini-webhook-dynamic"],
      "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
    }
  }'
```

### Vérifier les signatures dynamiques (JWKS)

Les requêtes de webhook dynamiques émettent une signature de jeton Web JSON (JWT). Votre écouteur
doit extraire la signature et la vérifier à l'aide des points de terminaison de certificat public de [Google](https://www.googleapis.com/oauth2/v3/certs).

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

### Java

```
import com.sun.net.httpserver.HttpServer;
import java.io.InputStream;
import java.io.OutputStream;
import java.math.BigInteger;
import java.net.InetSocketAddress;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.RSAPublicKeySpec;
import java.util.Base64;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

String jwksUri = "https://generativelanguage.googleapis.com/.well-known/jwks.json";

HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
server.createContext(
    "/gemini-webhook-dynamic",
    exchange -> {
      String token = exchange.getRequestHeaders().getFirst("Webhook-Signature");
      if (token == null || token.split("\\.").length != 3) {
        byte[] resp = "{\"error\": \"No signature header\"}".getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(400, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
        return;
      }

      try {
        String[] parts = token.split("\\.");
        String headerJson =
            new String(Base64.getUrlDecoder().decode(parts[0]), StandardCharsets.UTF_8);
        Matcher kidMatcher = Pattern.compile("\"kid\"\\s*:\\s*\"([^\"]+)\"").matcher(headerJson);
        String kid = kidMatcher.find() ? kidMatcher.group(1) : "";

        PublicKey pubKey = null;
        try (InputStream in = URI.create(jwksUri).toURL().openStream()) {
          String jwksJson = new String(in.readAllBytes(), StandardCharsets.UTF_8);
          Matcher keyBlockMatcher =
              Pattern.compile(
                      "\\{[^}]*\"kid\"\\s*:\\s*\"" + Pattern.quote(kid) + "\"[^}]*\\}")
                  .matcher(jwksJson);
          if (keyBlockMatcher.find()) {
            String keyBlock = keyBlockMatcher.group(0);
            Matcher nMatcher = Pattern.compile("\"n\"\\s*:\\s*\"([^\"]+)\"").matcher(keyBlock);
            Matcher eMatcher = Pattern.compile("\"e\"\\s*:\\s*\"([^\"]+)\"").matcher(keyBlock);
            if (nMatcher.find() && eMatcher.find()) {
              BigInteger n =
                  new BigInteger(1, Base64.getUrlDecoder().decode(nMatcher.group(1)));
              BigInteger e =
                  new BigInteger(1, Base64.getUrlDecoder().decode(eMatcher.group(1)));
              pubKey =
                  KeyFactory.getInstance("RSA").generatePublic(new RSAPublicKeySpec(n, e));
            }
          }
        }

        Signature sig = Signature.getInstance("SHA256withRSA");
        sig.initVerify(pubKey);
        sig.update((parts[0] + "." + parts[1]).getBytes(StandardCharsets.UTF_8));
        boolean verified = sig.verify(Base64.getUrlDecoder().decode(parts[2]));

        if (!verified) {
          throw new SecurityException("Signature verification failed");
        }

        System.out.println("Verified Dynamic payload success.");
        byte[] resp = "{\"status\": \"received\"}".getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(200, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
      } catch (Exception e) {
        byte[] resp =
            ("{\"error\": \"Invalid Dynamic signature\", \"details\": \""
                    + e.getMessage()
                    + "\"}")
                .getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(400, resp.length);
        try (OutputStream os = exchange.getResponseBody()) {
          os.write(resp);
        }
      }
    });
server.start();
```

## Enveloppe de webhook

Pour éviter la congestion de la bande passante, les webhooks Gemini utilisent un modèle de **charge utile légère** pour diffuser les données. Les diffusions envoient un instantané contenant des détails sur l'état et des pointeurs vers les résultats, plutôt que le fichier de sortie brut lui-même.

Voici un exemple de format de charge utile :

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

Les événements suivants sont déclenchés pour les tâches compatibles :

| Type d'événement | Déclencheur | Élément de charge utile (`data`) |
| --- | --- | --- |
| `batch.succeeded` | Traitement terminé. | `id`, `output_file_uri` |
| `batch.cancelled` | Requête annulée par l'utilisateur | `id` |
| `batch.expired` | Le lot n'a pas été traité (terminé) dans un délai de 24 heures | `id` |
| `batch.failed` | Échec de la tâche par lot (erreur système ou de validation). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Appel de fonction, l'utilisateur doit effectuer une action | `id` |
| `interaction.completed` | LRO dans l'API Interactions réussi | `id` |
| `interaction.failed` | Échec de la LRO dans l'API Interactions (erreur système ou de validation). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | LRO dans l'API Interactions annulée | `id` |
| `video.generated` | LRO de génération de vidéo terminée. | `id`, `output_file_uri`, `file_name` |

## Bonnes pratiques

Pour garantir un fonctionnement fiable et évolutif :

- **Vérification stricte de la protection contre la relecture** : toutes les requêtes comportent un en-tête `webhook-timestamp`. Validez toujours cet horodatage sur la couche de configuration de votre serveur pour refuser les charges utiles datant de plus de **5 minutes** (afin d'atténuer les attaques par relecture).
- **Traitement asynchrone** : répondez immédiatement avec `2xx OK` lors de la détection d'une signature valide, et mettez en file d'attente les opérations d'analyse en interne. Si les temps d'attente de l'écouteur sont prolongés, un cycle de nouvelles tentatives de diffusion sera déclenché.
- **Gestion de la déduplication** : les webhooks standards diffusent les données "au moins une fois". Utilisez l'en-tête `webhook-id` cohérent pour gérer les doublons potentiels dans les flux de congestion plus élevés.

## Étape suivante

- [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr) : utilisez des webhooks pour automatiser les points de terminaison à volume élevé.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/18 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/18 (UTC)."],[],[]]
