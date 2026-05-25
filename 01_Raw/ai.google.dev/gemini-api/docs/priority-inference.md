---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419
fetched_at: 2026-05-25T05:26:39.695130+00:00
title: "Inferencia de prioridad \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Inferencia de prioridad

La API de Gemini Priority es un nivel de inferencia premium diseñado para cargas de trabajo críticas para el negocio que requieren una latencia más baja y la mayor confiabilidad a un precio premium. El tráfico del nivel de prioridad tiene prioridad sobre el tráfico de la API estándar y del nivel Flex.

La inferencia de prioridad está disponible para los usuarios de [nivel 2 y nivel 3](https://ai.google.dev/gemini-api/docs/billing?hl=es-419#about-billing) en los extremos de la API de GenerateContent y la API de Interactions.

## Cómo usar la prioridad

Para usar el nivel de prioridad, establece el campo `service_tier` en `priority` en el cuerpo de la solicitud. El nivel predeterminado es estándar si se omite el campo.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.5-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Cómo funciona la inferencia de prioridad

El enrutamiento de inferencia de prioridad dirige las solicitudes a colas de procesamiento de alta criticidad, lo que ofrece un rendimiento rápido y predecible para las aplicaciones orientadas al usuario. Su mecanismo principal es una degradación correcta del servidor al procesamiento estándar para el tráfico que supera los límites dinámicos, lo que garantiza la estabilidad de la aplicación en lugar de rechazar la solicitud.

| Función | Prioridad | Estándar | Flexible | Lote |
| --- | --- | --- | --- | --- |
| **Precios** | Entre un 75% y un 100% más que el plan Estándar | Precio completo | 50% de descuento | 50% de descuento |
| **Latencia** | Segundos | De segundos a minutos | Minutos (objetivo de 1 a 15 min) | Hasta 24 horas |
| **Confiabilidad** | Alta (no se desprende) | Alta / media-alta | Mejor esfuerzo (descartable) | Alta (para la capacidad de procesamiento) |
| **Interfaz** | Síncrona | Síncrona | Síncrona | Asíncrono |

### Ventajas clave

- **Latencia baja**: Diseñada para tiempos de respuesta de segundos en herramientas de IA interactivas y orientadas al usuario.
- **Alta confiabilidad**: El tráfico se trata con la mayor criticidad y no se puede descartar.
- **Degradación elegante**: Los picos de tráfico que superan los límites dinámicos se degradan automáticamente al nivel Estándar para su procesamiento en lugar de fallar, lo que evita interrupciones del servicio.
- **Baja fricción**: Usa el mismo método `generateContent` síncrono que los niveles estándar y Flex.

### Casos de uso

El procesamiento prioritario es ideal para los flujos de trabajo fundamentales para la empresa en los que el rendimiento y la confiabilidad son primordiales.

- **Aplicaciones interactivas de IA**: Chatbots y copilotos de atención al cliente en los que los usuarios pagan una tarifa premium y esperan respuestas rápidas y coherentes.
- **Motores de decisiones en tiempo real**: Sistemas que requieren resultados altamente confiables y de baja latencia, como la clasificación de tickets en vivo o la detección de fraude.
- **Funciones para clientes premium**: Desarrolladores que necesitan garantizar objetivos de nivel de servicio (SLO) más altos para los clientes que pagan.

### Límites de frecuencia

El consumo de prioridad tiene sus propios límites de frecuencia, aunque el consumo se contabiliza para los [límites de frecuencia generales del tráfico interactivo](https://aistudio.google.com/rate-limit?hl=es-419). Los límites de frecuencia predeterminados para la inferencia de prioridad son **0.3 veces el límite de frecuencia estándar para el modelo o el nivel**.

### Lógica de cambio a una versión anterior correcta

Si se exceden los límites de prioridad debido a la congestión, las solicitudes de desbordamiento se **degradan de forma automática y correcta** al procesamiento estándar en lugar de fallar con un error 503 o 429. Las solicitudes degradadas se facturan a la tarifa estándar, no a la tarifa premium de prioridad.

### Responsabilidad del cliente

- **Supervisión de respuestas**: Los desarrolladores deben supervisar el encabezado `x-gemini-service-tier` en la respuesta de la API para detectar si las solicitudes se degradan con frecuencia a `standard`.
- **Reintentos**: Los clientes deben implementar una lógica de reintentos o una retirada exponencial para los errores estándar, como `DEADLINE_EXCEEDED`.

## Precios

La inferencia de prioridad tiene un precio entre un 75% y un 100% más alto que la [API estándar](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) y se factura por token.

## Modelos compatibles

Los siguientes modelos admiten la inferencia de prioridad:

| Modelo | Inferencia de prioridad |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=es-419) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=es-419) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ |

## ¿Qué sigue?

Obtén más información sobre otras opciones de [inferencia y optimización](https://ai.google.dev/gemini-api/docs/optimization?hl=es-419) de Gemini:

- [Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419) para una reducción del 50% en los costos
- [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419) para el procesamiento asíncrono en un plazo de 24 horas
- [Almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) para reducir los costos de los tokens de entrada

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-19 (UTC)"],[],[]]
