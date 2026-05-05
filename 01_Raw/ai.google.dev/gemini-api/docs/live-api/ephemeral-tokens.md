---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=es-419
fetched_at: 2026-05-05T20:02:30.480269+00:00
title: "Ephemeral tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Ephemeral tokens

Los tokens efímeros son tokens de autenticación de corta duración para acceder a la API de Gemini a través de [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Están diseñadas para mejorar la seguridad cuando te conectas directamente desde el dispositivo de un usuario a la API (una implementación de [cliente a servidor](https://ai.google.dev/gemini-api/docs/live?hl=es-419#implementation-approach)). Al igual que las claves de API estándar, los tokens efímeros se pueden extraer de aplicaciones del cliente, como navegadores web o aplicaciones para dispositivos móviles. Sin embargo, debido a que los tokens efímeros vencen rápidamente y se pueden restringir, reducen significativamente los riesgos de seguridad en un entorno de producción. Debes usarlos cuando accedas a la API de Live directamente desde aplicaciones del cliente para mejorar la seguridad de la clave de API.

## Cómo funcionan los tokens efímeros

A continuación, se explica cómo funcionan los tokens efímeros a nivel general:

1. Tu cliente (p.ej., una app web) se autentica con tu backend.
2. Tu backend solicita un token efímero al servicio de aprovisionamiento de la API de Gemini.
3. La API de Gemini emite un token de corta duración.
4. Tu backend envía el token al cliente para las conexiones de WebSocket a la API de Live. Para ello, reemplaza tu clave de API por un token efímero.
5. Luego, el cliente usa el token como si fuera una clave de API.

![Descripción general de los tokens efímeros](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=es-419)

Esto mejora la seguridad, ya que, incluso si se extrae, el token es de corta duración, a diferencia de una clave de API de larga duración implementada del lado del cliente. Dado que el cliente envía datos directamente a Gemini, esto también mejora la latencia y evita que tus back-ends necesiten proxy para los datos en tiempo real.

## Crea un token efímero

A continuación, se muestra un ejemplo simplificado de cómo obtener un token efímero de Gemini.
De forma predeterminada, tendrás 1 minuto para iniciar nuevas sesiones de la API de Live con el token de esta solicitud (`newSessionExpireTime`) y 30 minutos para enviar mensajes a través de esa conexión (`expireTime`).

### Python

```
import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

  const token: AuthToken = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

Para conocer las restricciones, los valores predeterminados y otras especificaciones del campo `expireTime`, consulta la [referencia de la API](https://ai.google.dev/api/live?hl=es-419#ephemeral-auth-tokens).
Dentro del período `expireTime`, deberás [`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=es-419#session-resumption) para volver a conectar la llamada cada 10 minutos (esto se puede hacer con el mismo token incluso si `uses: 1`).

También es posible bloquear un token efímero para un conjunto de configuraciones. Esto puede ser útil para mejorar aún más la seguridad de tu aplicación y mantener las instrucciones del sistema en el servidor.

### Python

```
client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
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
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

También puedes bloquear un subconjunto de campos. Consulta la [documentación del SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields) para obtener más información.

## Conéctate a la API de Live con un token efímero

Una vez que tengas un token efímero, úsalo como si fuera una clave de API (pero recuerda que solo funciona para la API en vivo y solo con la versión `v1alpha` de la API).

El uso de tokens efímeros solo agrega valor cuando se implementan aplicaciones que siguen el enfoque de [implementación de cliente a servidor](https://ai.google.dev/gemini-api/docs/live?hl=es-419#implementation-approach).

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

Consulta [Comienza a usar la API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419) para obtener más ejemplos.

## Prácticas recomendadas

- Establece una duración de vencimiento corta con el parámetro `expire_time`.
- Los tokens vencen, por lo que se debe volver a iniciar el proceso de aprovisionamiento.
- Verifica la autenticación segura para tu propio backend. Los tokens efímeros solo serán tan seguros como tu método de autenticación de backend.
- En general, evita usar tokens efímeros para las conexiones del backend a Gemini, ya que esta ruta suele considerarse segura.

## Limitaciones

Por el momento, los tokens efímeros solo son compatibles con la [API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419).

## ¿Qué sigue?

- Lee la [referencia](https://ai.google.dev/api/live?hl=es-419#ephemeral-auth-tokens) de la API de Live sobre los tokens efímeros para obtener más información.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
