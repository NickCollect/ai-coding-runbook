---
source_url: https://ai.google.dev/gemini-api/docs/interactions/webhooks?hl=it
fetched_at: 2026-06-08T05:30:22.759655+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Webhook

I webhook consentono all'API Gemini di inviare notifiche in tempo reale al tuo server
al termine delle operazioni asincrone o di lunga durata (LRO). In questo modo non è più necessario eseguire il polling dell'API per gli aggiornamenti di stato, riducendo la latenza e il sovraccarico.

I webhook sono disponibili per operazioni come i job [batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it),
le [interazioni](https://ai.google.dev/gemini-api/docs/interactions?hl=it) e la [generazione di video](https://ai.google.dev/gemini-api/docs/video?hl=it).

## Come funziona

Anziché eseguire il polling di `GET /operations` ripetutamente per verificare se un job è terminato,
puoi configurare i webhook dell'API Gemini per inviare una richiesta POST HTTP al tuo
URL listener immediatamente dopo l'attivazione di un evento.

L'API Gemini supporta due modi per configurare i webhook:

- [**Webhook statici**](#static-webhooks): endpoint a livello di progetto configurati
  con l'[API WebhookService](https://ai.google.dev/api?hl=it). Ideale per integrazioni globali (ad es. notifica di Slack, sincronizzazione di un database e così via).
- [**Webhook dinamici**](#dynamic-webhooks): override a livello di richiesta che passano un
  URL webhook nel payload di configurazione di una chiamata di lavoro specifica. Ideale per
  indirizzare job specifici a endpoint dedicati.

## Webhook statici

I webhook statici vengono registrati per un intero [progetto](https://ai.google.dev/gemini-api/docs/api-key?hl=it#google-cloud-projects) e vengono attivati per qualsiasi evento corrispondente.

### Crea un webhook

Puoi creare endpoint utilizzando l'SDK o l'API REST.

**IMPORTANTE**: quando crei un webhook, l'API restituisce un **segreto di firma**
**solo una volta**. Devi memorizzarlo in modo sicuro (ad es. nelle variabili di ambiente)
per verificare le firme in un secondo momento. Se perdi il secret di firma, dovrai
[ruotarlo](#rotate-signing-secret).

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

Per informazioni dettagliate sulla configurazione del server per la ricezione dei dati, consulta la sezione
[Gestire le richieste webhook](#handle-webhook-requests).

### Recuperare un webhook

Recupera i dettagli di un webhook specifico in base al nome della risorsa.

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

### Elenco webhook

Elenca tutti i webhook configurati per il progetto corrente, con paginazione facoltativa.

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

### Aggiorna un webhook

Aggiorna le proprietà di un webhook esistente, ad esempio il nome visualizzato, l'URI di destinazione o
gli eventi a cui è stato eseguito l'abbonamento.

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

### Eliminare un webhook

Rimuovi un endpoint webhook dal progetto. In questo modo, le future distribuzioni di eventi
a quell'endpoint vengono interrotte.

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

### Ruotare un secret di firma

Ruota il secret di firma per un webhook. Puoi configurare se i segreti attivi in precedenza
vengono revocati immediatamente o dopo un periodo di tolleranza di 24 ore.

**IMPORTANTE**: il nuovo segreto di firma viene restituito **solo una volta** al momento della rotazione. Archivialo in modo sicuro prima di aggiornare la logica di verifica.

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

### Gestire le richieste webhook su un server

Quando si verifica un evento a cui hai eseguito la registrazione, il tuo URL webhook riceverà
una richiesta POST HTTP. L'endpoint deve rispondere con un codice di stato 2xx
entro pochi secondi per evitare un nuovo tentativo. Per garantire la consegna, l'API Gemini
ritenta automaticamente le richieste non riuscite per 24 ore utilizzando il backoff esponenziale.

Gemini segue rigorosamente la specifica [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) per le intestazioni di sicurezza. Verifica il payload sul tuo server utilizzando le firme delle intestazioni firmate e la chiave segreta di firma statica memorizzata. Per informazioni sul payload, consulta la sezione [Webhook envelope](#webhook-envelope).

Ecco un esempio che utilizza Flask per il listener HTTP:

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

## Webhook dinamici

I webhook dinamici ti consentono di associare un endpoint webhook a una **configurazione di richiesta specifica**, ideale per le code di orchestrazione degli agenti. Gli webhook dinamici utilizzano
firme JWKS con chiavi pubbliche asimmetriche anziché segreti simmetrici.

### Inviare una richiesta dinamica

Aggiungi un `webhook_config` quando attivi un job asincrono (ad es. la creazione di un
batch).

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
  -H "Api-Revision: 2026-05-20" \
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

### Verifica delle firme dinamiche (JWKS)

Le richieste webhook dinamiche emettono una firma JSON Web Token (JWT). Il tuo listener
deve estrarre la firma e verificarla utilizzando gli [endpoint del certificato pubblico di Google](https://www.googleapis.com/oauth2/v3/certs).

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

## Busta del webhook

Per evitare la congestione della larghezza di banda, i webhook Gemini utilizzano un modello di **payload sottile** per
trasferire i dati.
Le consegne inviano uno snapshot contenente i dettagli dello stato e i puntatori ai risultati, anziché il file di output non elaborato.

Ecco un esempio di formato del payload:

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

## Riferimento al catalogo degli eventi

Per i job di supporto vengono attivati i seguenti eventi:

| Tipo di evento | Trigger | Elemento payload (`data`) |
| --- | --- | --- |
| `batch.succeeded` | Elaborazione completata correttamente. | `id`, `output_file_uri` |
| `batch.cancelled` | Richiesta annullata dall'utente | `id` |
| `batch.expired` | Il batch non è stato elaborato (completato) nell'arco di 24 ore | `id` |
| `batch.failed` | Job batch non riuscito (errore di sistema o di convalida). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Chiamata di funzione, l'utente deve fare qualcosa | `id` |
| `interaction.completed` | LRO nell'API Interactions riuscita | `id` |
| `interaction.failed` | LRO nell'API Interactions non riuscita (errore di sistema o di convalida). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | LRO nell'API Interactions annullata | `id` |
| `video.generated` | LRO di generazione video completata. | `id`, `output_file_uri`, `file_name` |

## Best practice

Per garantire un funzionamento affidabile e scalabile:

- **Controllo rigoroso della protezione dal replay**: tutte le richieste includono un'intestazione `webhook-timestamp`. Convalida sempre questo timestamp nel livello di configurazione del server per
  rifiutare i payload più vecchi di **5 minuti** (per mitigare gli attacchi di replay).
- **Elabora in modo asincrono**: rispondi con `2xx OK` immediatamente dopo il rilevamento di una firma valida e metti in coda internamente le operazioni di analisi. Tempi di attesa prolungati
  attiveranno un ciclo di nuovi tentativi di pubblicazione.
- **Gestione della deduplicazione**: i webhook standard vengono inviati "almeno una volta". Utilizza l'intestazione
  `webhook-id` coerente per gestire i potenziali duplicati nei flussi con congestione
  più elevata.

## Passaggi successivi

- [API Batch](https://ai.google.dev/gemini-api/docs/batch?hl=it): utilizza i webhook per automatizzare gli endpoint ad alto volume.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-28 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-28 UTC."],[],[]]
