---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pt-BR
fetched_at: 2026-08-17T02:31:37.035141+00:00
title: "Tokens tempor\u00e1rios \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Tokens temporários

Os tokens temporários são tokens de autenticação de curta duração para acessar a API Gemini
usando [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Eles foram projetados para aumentar a segurança quando
você se conecta diretamente de um dispositivo do usuário à API (uma
[implementação cliente-servidor](https://ai.google.dev/gemini-api/docs/live?hl=pt-br#implementation-approach)
). Assim como as chaves de API padrão, os tokens temporários podem ser extraídos de aplicativos do lado do cliente, como navegadores da Web ou apps para dispositivos móveis. No entanto, como os tokens temporários expiram rapidamente e podem ser restritos, eles reduzem significativamente os riscos de segurança em um ambiente de produção. Use-os ao acessar a API Live diretamente de aplicativos do lado do cliente para aumentar a segurança da chave de API.

## Como os tokens temporários funcionam

Confira como os tokens temporários funcionam de modo geral:

1. O cliente (por exemplo, um app da Web) é autenticado com o back-end.
2. O back-end solicita um token temporário do serviço de provisionamento da API Gemini.
3. A API Gemini emite um token de curta duração.
4. O back-end envia o token ao cliente para conexões WebSocket com a API Live. Para fazer isso, troque a chave de API por um token temporário.
5. O cliente usa o token como se fosse uma chave de API.

![Visão geral dos tokens temporários](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=pt-br)

Isso aumenta a segurança porque, mesmo que seja extraído, o token é de curta duração, ao contrário de uma chave de API de longa duração implantada no lado do cliente. Como o cliente envia dados diretamente ao Gemini, isso também melhora a latência e evita que os back-ends precisem fazer proxy dos dados em tempo real.

## Criar um token temporário

Confira um exemplo simplificado de como receber um token temporário do Gemini.
Por padrão, você terá 1 minuto para iniciar novas sessões da API Live usando o token dessa solicitação (`newSessionExpireTime`) e 30 minutos para enviar mensagens por essa conexão (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
    },
  });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

Para restrições de valor `expireTime`, padrões e outras especificações de campo, consulte a
[referência da API](https://ai.google.dev/api/live?hl=pt-br#ephemeral-auth-tokens).
No período `expireTime`, você precisará de
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=pt-br#session-resumption) para
reconectar a chamada a cada 10 minutos. Isso pode ser feito com o mesmo token, mesmo
que `uses: 1`.

Também é possível bloquear um token temporário em um conjunto de configurações. Isso pode ser útil para melhorar ainda mais a segurança do aplicativo e manter as instruções do sistema no lado do servidor.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.1-flash-live-preview",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

Também é possível bloquear um subconjunto de campos. Consulte a [documentação do SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
para mais informações.

## Conectar-se à API Live com um token temporário

Depois de ter um token temporário, use-o como se fosse uma chave de API. No entanto, ele só funciona para a API Live e apenas com a versão `v1beta` da API.

O uso de tokens temporários só agrega valor ao implantar aplicativos
que seguem a abordagem de implementação [cliente-servidor](https://ai.google.dev/gemini-api/docs/live?hl=pt-br#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Consulte [Introdução à API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br) para mais exemplos.

## Práticas recomendadas

- Defina uma duração de expiração curta usando o parâmetro `expire_time`.
- Os tokens expiram, exigindo a reinicialização do processo de provisionamento.
- Verifique a autenticação segura do seu back-end. Os tokens temporários só serão tão seguros quanto o método de autenticação do back-end.
- Em geral, evite usar tokens temporários para conexões de back-end para Gemini, já que esse caminho normalmente é considerado seguro.

## Limitações

No momento, os tokens temporários só são compatíveis com a [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).

## A seguir

- Leia a referência da API Live [sobre tokens temporários](https://ai.google.dev/api/live?hl=pt-br#ephemeral-auth-tokens)
  para mais informações.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
