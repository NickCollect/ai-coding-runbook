---
source_url: https://ai.google.dev/gemini-api/docs/interactions/webhooks?hl=pl
fetched_at: 2026-06-15T06:23:03.489132+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Webhooki

Webhooki umożliwiają interfejsowi Gemini API wysyłanie powiadomień w czasie rzeczywistym na Twój serwer po zakończeniu operacji asynchronicznych lub długotrwałych. Eliminuje to konieczność sondowania interfejsu API w celu uzyskania aktualizacji stanu, co zmniejsza opóźnienia i obciążenie.

Webhooki są dostępne w przypadku operacji takich jak [zadania wsadowe](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl),
[interakcje](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) i [generowanie filmów](https://ai.google.dev/gemini-api/docs/video?hl=pl).

## Jak to działa

Zamiast wielokrotnie sondować `GET /operations`, aby sprawdzić, czy zadanie zostało zakończone, możesz skonfigurować webhooki Gemini API tak, aby natychmiast po wywołaniu zdarzenia wysyłały żądanie HTTP POST na adres URL odbiornika.

Interfejs Gemini API obsługuje 2 sposoby konfigurowania webhooków:

- [**Webhooki statyczne**](#static-webhooks): punkty końcowe na poziomie projektu skonfigurowane
  za pomocą interfejsu Gemini [WebhookService API](https://ai.google.dev/api?hl=pl). Dobrze sprawdzają się w przypadku integracji globalnych (np. powiadamiania Slacka, synchronizowania bazy danych itp.).
- [**Webhooki dynamiczne**](#dynamic-webhooks): zastąpienia na poziomie żądania, które przekazują adres URL
  webhooka w ładunku konfiguracji konkretnego wywołania zadania. Idealne do kierowania konkretnych zadań do dedykowanych punktów końcowych.

## Webhooki statyczne

Webhooki statyczne są rejestrowane dla całego [projektu](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#google-cloud-projects) i są wywoływane w przypadku każdego pasującego
zdarzenia.

### Tworzenie webhooka

Punkty końcowe możesz tworzyć za pomocą pakietu SDK lub interfejsu API REST.

**WAŻNE**: podczas tworzenia webhooka interfejs API zwraca **obiekt tajny podpisywania**
**tylko raz**. Aby później weryfikować podpisy, musisz bezpiecznie przechowywać ten obiekt (np. w zmiennych środowiskowych). Jeśli utracisz obiekt tajny podpisywania, musisz go
[zmienić](#rotate-signing-secret).

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

Więcej informacji o konfigurowaniu serwera do odbierania danych znajdziesz w sekcji
[Obsługa żądań webhooków](#handle-webhook-requests).

### Pobieranie webhooka

Pobierz szczegóły konkretnego webhooka według jego nazwy zasobu.

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

### Wyświetlanie listy webhooków

Wyświetl listę wszystkich skonfigurowanych webhooków w bieżącym projekcie z opcjonalną paginacją.

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

### Aktualizowanie webhooka

Zaktualizuj właściwości istniejącego webhooka, takie jak nazwa wyświetlana, docelowy identyfikator URI lub subskrybowane zdarzenia.

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

### Usuwanie webhooka

Usuń punkt końcowy webhooka z projektu. Spowoduje to zatrzymanie dostarczania przyszłych zdarzeń do tego punktu końcowego.

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

### Rotacja obiektu tajnego podpisywania

Wykonaj rotację obiektu tajnego podpisywania dla webhooka. Możesz skonfigurować, czy wcześniej aktywne obiekty tajne mają zostać unieważnione natychmiast, czy po 24-godzinnym okresie przejściowym.

**WAŻNE**: nowy obiekt tajny podpisywania jest zwracany **tylko raz** w momencie rotacji
czasu. Zanim zaktualizujesz logikę weryfikacji, bezpiecznie go przechowuj.

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

### Obsługa żądań webhooków na serwerze

Gdy wystąpi zdarzenie, które subskrybujesz, Twój adres URL webhooka otrzyma żądanie HTTP POST. Aby uniknąć ponowienia, punkt końcowy musi odpowiedzieć kodem stanu 2xx w ciągu kilku sekund. Aby zapewnić dostarczenie, interfejs Gemini API automatycznie ponawia nieudane żądania przez 24 godziny, używając algorytmu wzrastający czas do ponowienia.

Gemini ściśle przestrzega specyfikacji [standardowych webhooków](https://github.com/standard-webhooks/standard-webhooks) w przypadku
nagłówków bezpieczeństwa. Zweryfikuj ładunek na serwerze za pomocą podpisów nagłówków podpisanych i przechowywanego statycznego obiektu tajnego podpisywania. Informacje o ładunku znajdziesz w sekcji dotyczącej [koperty webhooka](#webhook-envelope).

Oto przykład użycia Flask do odbiornika HTTP:

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

## Webhooki dynamiczne

Webhooki dynamiczne umożliwiają powiązanie punktu końcowego webhooka z **konkretną konfiguracją
żądania**, co jest idealne w przypadku kolejek orkiestracji agentów. Webhooki dynamiczne używają asymetrycznych podpisów JWKS klucza publicznego zamiast symetrycznych obiektów tajnych.

### Przesyłanie żądania dynamicznego

Podczas wywoływania zadania asynchronicznego (np. tworzenia zadania wsadowego) dodaj `webhook_config`.

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

### Weryfikowanie podpisów dynamicznych (JWKS)

Żądania webhooków dynamicznych emitują podpis tokena sieciowego JSON (JWT). Odbiornik
musi wyodrębnić podpis i zweryfikować go za pomocą [punktów końcowych certyfikatu publicznego Google](https://www.googleapis.com/oauth2/v3/certs).

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

## Koperta webhooka

Aby uniknąć przeciążenia przepustowości, webhooki Gemini używają modelu **cienki ładunek** do dostarczania danych. Dostawy wysyłają migawkę zawierającą szczegóły stanu i wskaźniki wyników, a nie sam plik wyjściowy.

Oto przykład formatu ładunku:

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

## Informacje o katalogu zdarzeń

W przypadku obsługiwanych zadań wywoływane są te zdarzenia:

| Typ zdarzenia | Wyzwalacz | Element ładunku (`data`) |
| --- | --- | --- |
| `batch.succeeded` | Przetwarzanie zostało zakończone. | `id`, `output_file_uri` |
| `batch.cancelled` | Użytkownik anulował żądanie | `id` |
| `batch.expired` | Zadanie wsadowe nie zostało przetworzone (zakończone) w ciągu 24 godzin | `id` |
| `batch.failed` | Nie udało się wykonać zadania wsadowego (błąd systemu lub weryfikacji). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Wywołanie funkcji, użytkownik musi coś zrobić | `id` |
| `interaction.completed` | Operacja LRO w interfejsie Interactions API zakończyła się powodzeniem | `id` |
| `interaction.failed` | Nie udało się wykonać operacji LRO w interfejsie Interactions API (błąd systemu lub weryfikacji). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | Operacja LRO w interfejsie Interactions API została anulowana | `id` |
| `video.generated` | Operacja LRO generowania filmu została zakończona. | `id`, `output_file_uri`, `file_name` |

## Sprawdzone metody

Aby zapewnić niezawodne i skalowalne działanie:

- **Ścisłe sprawdzanie ochrony przed powtórzeniem**: wszystkie żądania zawierają `webhook-timestamp`
  nagłówek. Zawsze sprawdzaj tę sygnaturę czasową w warstwie konfiguracji serwera, aby odrzucać ładunki starsze niż **5 minut** (aby ograniczyć ataki typu replay).
- **Przetwarzanie asynchroniczne**: natychmiast po wykryciu prawidłowego
  podpisu odpowiedz `2xx OK` i wewnętrznie umieść operacje analizowania w kolejce. Długie czasy wstrzymania odbiornika spowodują uruchomienie cyklu ponawiania dostarczania.
- **Obsługa deduplikacji**: standardowe webhooki dostarczają dane co najmniej raz. Aby obsługiwać potencjalne duplikaty w przepływach o większym natężeniu ruchu, użyj spójnego nagłówka `webhook-id`.

## Co dalej?

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=pl): używaj webhooków do automatyzowania punktów końcowych o dużej liczbie żądań.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-28 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-28 UTC."],[],[]]
