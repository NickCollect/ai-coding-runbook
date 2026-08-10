---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/webhooks?hl=pt-BR
fetched_at: 2026-08-10T03:13:56.960791+00:00
title: "Webhooks \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Webhooks

Os webhooks permitem que a API Gemini envie notificações em tempo real para seu servidor quando operações assíncronas ou de longa duração (LROs, na sigla em inglês) forem concluídas. Isso substitui a necessidade de consultar a API para atualizações de status, reduzindo a latência e a sobrecarga.

Os webhooks estão disponíveis para operações como [jobs em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br),
[interações](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) e [geração de vídeo](https://ai.google.dev/gemini-api/docs/video?hl=pt-br).

## Como funciona

Em vez de consultar `GET /operations` repetidamente para verificar se um job foi concluído, você pode configurar os webhooks da API Gemini para enviar uma solicitação HTTP POST ao URL do listener imediatamente após um acionador de evento.

A API Gemini oferece duas maneiras de configurar webhooks:

- [**Webhooks estáticos**](#static-webhooks): endpoints no nível do projeto configurados
  com a API Gemini [WebhookService](https://ai.google.dev/api?hl=pt-br). Indicado para integrações globais (por exemplo, notificar o Slack, sincronizar um banco de dados etc.).
- [**Webhooks dinâmicos**](#dynamic-webhooks): substituições no nível da solicitação que transmitem um URL do webhook no payload de configuração de uma chamada de jobs específica. Ideal para rotear jobs específicos para endpoints dedicados.

## Webhooks estáticos

Os webhooks estáticos são registrados para um [projeto](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#google-cloud-projects) inteiro e acionados para qualquer evento
correspondente.

### Criar um webhook

É possível criar endpoints usando o SDK ou a API REST.

**IMPORTANTE**: ao criar um webhook, a API retorna um **secret de assinatura**
**apenas uma vez**. Você precisa armazenar isso com segurança (por exemplo, nas variáveis de ambiente) para verificar as assinaturas mais tarde. Se você perder o secret de assinatura, será necessário
[rotacioná-lo](#rotate-signing-secret).

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

Para detalhes sobre como configurar o servidor para receber dados, consulte a
[seção Processar solicitações de webhook](#handle-webhook-requests).

### Receber um webhook

Recupere detalhes sobre um webhook específico pelo nome do recurso.

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

### Listar webhooks

Liste todos os webhooks configurados para o projeto atual, com paginação opcional.

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

### Atualizar um webhook

Atualize as propriedades de um webhook atual, como o nome de exibição, o URI de destino ou os eventos inscritos.

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

### Excluir um webhook

Remova um endpoint de webhook do projeto. Isso interrompe as entregas de eventos futuras para esse endpoint.

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

### Rotacionar um secret de assinatura

Rotacione o secret de assinatura de um webhook. É possível configurar se os secrets ativos anteriormente serão revogados imediatamente ou após um período de carência de 24 horas.

**IMPORTANTE**: o novo secret de assinatura é retornado **apenas uma vez** no momento da rotação
time. Armazene-o com segurança antes de atualizar a lógica de verificação.

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

### Processar solicitações de webhook em um servidor

Quando um evento ao qual você está inscrito acontece, o URL do webhook recebe uma solicitação HTTP POST. O endpoint precisa responder com um código de status 2xx em alguns segundos para evitar uma nova tentativa. Para garantir a entrega, a API Gemini repete automaticamente as solicitações com falha por 24 horas usando a espera exponencial.

O Gemini segue rigorosamente a especificação de [webhooks padrão](https://github.com/standard-webhooks/standard-webhooks) para
cabeçalhos de segurança. Verifique o payload no servidor usando as assinaturas de cabeçalho assinadas e o secret de assinatura estático armazenado. Consulte a seção [Envelope de webhook](#webhook-envelope) para informações sobre o payload.

Confira um exemplo usando o Flask para o listener HTTP:

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
        print(f"Batch completed! ID: {event["data"]["id"]}")
        if event["data"].get("output_file_uri"):
            # For batch jobs with input file
            print(f"Batch file: {event["data"]["output_file_uri"]}")
    elif (event.type == "video.generated"):
        print(f"Video generated! URI: {event["data"]["output_file_uri"]}")

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

## Webhooks dinâmicos

Os webhooks dinâmicos permitem vincular um endpoint de webhook a uma **configuração de solicitação
específica**, ideal para filas de orquestração de agentes. Os webhooks dinâmicos aproveitam as assinaturas JWKS de chave pública assimétrica em vez de secrets simétricos.

### Enviar uma solicitação dinâmica

Adicione uma `webhook_config` ao acionar um job assíncrono (por exemplo, criar um lote).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

file_batch_job = client.batches.create(
    model="gemini-3.6-flash",
    src="files/uploaded_file_id",
    config={
        "display_name": "My Setup",
        "webhook_config": {
            "uris": ["https://my-api.com/gemini-webhook-dynamic"],
            "user_metadata":{"job_group": "nightly-eval", "priority": "high"}
        }
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createBatchWithWebhook() {
  const fileBatchJob = await client.batches.create({
    model: "gemini-3.6-flash",
    src: "files/uploaded_file_id",
    config: {
      displayName: "My Setup",
      webhookConfig: {
        uris: ["https://my-api.com/gemini-webhook-dynamic"],
        user_metadata: {"job_group": "nightly-eval", "priority": "high"}
      },
    },
  });
}
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.6-flash:batchCreate" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "src": "files/uploaded_file_id",
    "config": {
      "display_name": "My Setup",
      "webhook_config": {
        "uris": ["https://my-api.com/gemini-webhook-dynamic"],
        "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
      }
    }
  }'
```

### Verificar assinaturas dinâmicas (JWKS)

As solicitações de webhook dinâmico emitem uma assinatura JSON Web Token (JWT). O listener
precisa extrair a assinatura e verificá-la usando os endpoints de certificado público do [Google](https://www.googleapis.com/oauth2/v3/certs).

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

## Envelope de webhook

Para evitar o congestionamento da largura de banda, os webhooks do Gemini usam um modelo de **payload fino** para entregar dados. As entregas enviam um snapshot que contém detalhes de status e indicadores para resultados, em vez do próprio arquivo de saída bruto.

Confira um exemplo de formato de payload:

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

## Referência do catálogo de eventos

Os eventos a seguir são acionados para jobs de suporte:

| Tipo de evento | Gatilho | Item de payload (`data`) |
| --- | --- | --- |
| `batch.succeeded` | O processamento foi concluído. | `id`, `output_file_uri` |
| `batch.cancelled` | Solicitação cancelada pelo usuário | `id` |
| `batch.expired` | O lote não foi processado (concluído) em um período de 24 horas | `id` |
| `batch.failed` | Falha no job em lote (erro de sistema ou validação). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Chamada de função, o usuário precisa fazer algo | `id` |
| `interaction.completed` | LRO na API Interactions bem-sucedida | `id` |
| `interaction.failed` | LRO na API Interactions com falha (erro de sistema ou validação). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | LRO na API Interactions cancelada | `id` |
| `video.generated` | LRO de geração de vídeo concluída. | `id`, `output_file_uri`, `file_name` |

## Práticas recomendadas

Para garantir uma operação confiável e escalonável:

- **Verificação rigorosa de proteção contra repetição**: todas as solicitações têm um `webhook-timestamp`
  cabeçalho. Sempre valide esse carimbo de data/hora na camada de configuração do servidor para rejeitar payloads com mais de **5 minutos** (para atenuar ataques de repetição).
- **Processar de forma assíncrona**: responda com `2xx OK` imediatamente após a detecção de assinatura válida
  e coloque as operações de análise na fila internamente. Tempos de espera prolongados do listener vão acionar um ciclo de nova tentativa de entrega.
- **Processamento de desduplicação**: os webhooks padrão entregam "pelo menos uma vez". Use o cabeçalho `webhook-id` consistente para processar possíveis duplicados em fluxos de congestionamento mais altos.

## A seguir

- [API Batch](https://ai.google.dev/gemini-api/docs/batch?hl=pt-br): use webhooks para automatizar endpoints de alto volume.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
