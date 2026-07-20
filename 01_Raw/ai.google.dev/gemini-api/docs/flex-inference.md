---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419
fetched_at: 2026-07-20T04:47:26.993742+00:00
title: "Inferencia flexible \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Inferencia flexible

La API de Gemini Flex es un nivel de inferencia que ofrece una reducción del 50% en el costo en comparación con las tarifas estándar, a cambio de una latencia variable y una disponibilidad de mejor esfuerzo. Está diseñada para cargas de trabajo tolerantes a la latencia que requieren procesamiento síncrono, pero no necesitan el rendimiento en tiempo real de la API estándar.

## Cómo usar Flex

Para usar el nivel Flex, especifica `service_tier` como `flex` en tu solicitud. De forma predeterminada, las solicitudes usan el nivel estándar si se omite este campo.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.5-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Cómo funciona la inferencia de Flex

La inferencia de Gemini Flex une la brecha entre la API estándar y el tiempo de respuesta de 24 horas
de la [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419). Utiliza la capacidad de procesamiento fuera de las horas pico y "desechable" para proporcionar una solución rentable para las tareas en segundo plano y los flujos de trabajo secuenciales.

| Función | Flexible | Prioridad | Estándar | Lote |
| --- | --- | --- | --- | --- |
| **Precios** | 50% de descuento | Entre un 75% y un 100% más que el nivel Estándar | Precio completo | 50% de descuento |
| **Latencia** | Minutos (objetivo de 1 a 15 min) | Baja (segundos) | De segundos a minutos | Hasta 24 horas |
| **Confiabilidad** | Mejor esfuerzo (desechable) | Alta (no desechable) | Alta / media alta | Alta (para la capacidad de procesamiento) |
| **Interfaz** | Síncrona | Síncrona | Síncrona | Asíncrona |

### Ventajas clave

- **Rentabilidad**: Ahorros significativos para las evaluaciones que no son de producción, los agentes en segundo plano y el enriquecimiento de datos
- **Baja fricción**: Simplemente agrega un solo parámetro a tus solicitudes existentes
- **Flujos de trabajo síncronos**: Ideal para cadenas de API secuenciales en las que la siguiente solicitud depende del resultado de la anterior, lo que la hace más flexible que el lote para los flujos de trabajo de agentes

### Casos de uso

- **Evaluaciones sin conexión**: Ejecución de pruebas de regresión o clasificaciones de "LLM como juez"
- **Agentes en segundo plano**: Tareas secuenciales como actualizaciones de CRM, creación de perfiles o moderación de contenido en las que se aceptan minutos de demora
- **Investigación con restricciones presupuestarias**: Experimentos académicos que requieren un gran volumen de tokens con un presupuesto limitado

### Límites de frecuencia

El tráfico de inferencia de Flex se incluye en los [límites de frecuencia](https://aistudio.google.com/rate-limit?hl=es-419) generales; no
ofrece límites de frecuencia extendidos como la [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419).

### Capacidad desechable

El tráfico de Flex se trata con una prioridad más baja. Si hay un aumento en el tráfico estándar, es posible que se interrumpan o se expulsen las solicitudes de Flex para garantizar la capacidad de los usuarios de alta prioridad. Si buscas inferencias de alta prioridad, consulta
[Inferencias de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)

### Códigos de error

Cuando la capacidad de Flex no está disponible o el sistema está congestionado, la API muestra códigos de error estándar:

- **503 Service Unavailable**: El sistema está al máximo de su capacidad.
- **429 Too Many Requests**: Límites de frecuencia o agotamiento de recursos.

### Responsabilidad del cliente

- **Sin fallback del servidor**: Para evitar cargos inesperados, el sistema no
  actualizará automáticamente una solicitud de Flex al nivel Estándar si la capacidad de Flex está
  llena.
- **Reintentos**: Debes implementar tu propia lógica de reintento del cliente con
  retirada exponencial.
- **Tiempos de espera**: Debido a que las solicitudes de Flex pueden estar en una cola, te recomendamos
  que aumentes los tiempos de espera del cliente a 10 minutos o más para evitar el cierre prematuro de la
  conexión.

## Ajusta los períodos de tiempo de espera

Puedes configurar tiempos de espera por solicitud para la API de REST y las bibliotecas cliente.
Siempre asegúrate de que el tiempo de espera del cliente cubra el período de paciencia del servidor deseado (p.ej., 600 s o más para las colas de espera de Flex). Los SDK esperan valores de tiempo de espera en milisegundos.

### Tiempos de espera por solicitud

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## Implementa reintentos

Debido a que Flex es desechable y falla con errores 503, aquí tienes un ejemplo de implementación opcional de la lógica de reintento para continuar con las solicitudes fallidas:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.5-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## Precios

La inferencia de Flex tiene un precio del 50% de la [API estándar](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419)
y se factura por token.

## Modelos compatibles

Los siguientes modelos admiten la inferencia de Flex:

| Modelo | Inferencia de Flex |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=es-419) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ |

## ¿Qué sigue?

- [Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419) para una latencia ultrabaja
- [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419): Comprende los tokens

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-06 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-06 (UTC)"],[],[]]
