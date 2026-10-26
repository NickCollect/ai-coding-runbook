---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=es-419
fetched_at: 2026-10-26T05:49:27.683167+00:00
title: "Decodificaci\u00f3n larga \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Decodificación larga

La decodificación larga permite que Gemini 4 Argon genere más allá del límite de salida de una sola solicitud para tareas de razonamiento profundo, hasta la ventana de contexto unificada de 1 millón de tokens (1,048,576 tokens compartidos entre la entrada, el pensamiento y la salida).

Cambiar solo el ID del modelo no habilita la decodificación larga. Sin configuración adicional, la salida se detiene en 64,000 tokens para las llamadas de transmisión y en 32,000 tokens para las llamadas que no son de transmisión. La forma más rápida de activar la decodificación larga es actualizar el SDK de IA generativa de Google y establecer `max_output_tokens` en un valor superior a 65,536. En esta guía, se explica cómo funciona la decodificación de Long, cuándo usarla y cómo activarla con `generateContent`.

## Cómo funciona la decodificación de duración

Una sola solicitud de transmisión o del SDK genera hasta 64,000 tokens, y una solicitud de REST sin transmisión genera hasta 32,000 tokens. Cuando una respuesta necesita más tokens, el modelo la genera en varios saltos de solicitud y respuesta, y cada uno continúa desde donde se detuvo el salto anterior.

- **Límite unificado de tokens de entrada y salida:** La entrada, el pensamiento, las llamadas a funciones y la respuesta final comparten una ventana de 1 millón de tokens. La salida puede usar hasta 1,048,576 tokens menos los de entrada.
- **Límite en cada salto:** Un salto devuelve hasta 65,536 tokens de salida. Las solicitudes de REST sin transmisión devuelven hasta 32,768.
- **Un indicador de continuación:** Si el modelo alcanza el límite y le quedan tokens, la respuesta termina con `finish_reason: CONTINUATION` y un `continuation_token`.
- **El próximo salto:** El cliente vuelve a enviar la misma solicitud con el token. El modelo continúa desde donde se detuvo.
- **Un total para todos los saltos:** `max_output_tokens` establece el total de tokens de razonamiento y de salida para todos los saltos en conjunto.
- **Una señal de detención:** Cuando el modelo usa todo `max_output_tokens`, la respuesta termina con `finish_reason: MAX_TOKENS`.

En problemas difíciles, un salto puede gastar todos sus tokens en el pensamiento interno y devolver un texto vacío con un `continuation_token`. Esto es normal, y la respuesta final llega en saltos posteriores.

## Límites de salida predeterminados

Sin la decodificación larga, una sola solicitud se detiene en estos límites por solicitud:

- **Solicitudes de transmisión y solicitudes que no son de transmisión a través del SDK de IA generativa de Google (`generate_content`):** Se establecen de forma predeterminada en 64 000 tokens de salida.
- **Llamadas de REST directas que no son de transmisión (`generateContent`):** El valor predeterminado es 32,000 tokens de salida. Si se configura `max_output_tokens` en un valor superior a 32,768 en una llamada REST que no es de transmisión sin un `continuation_token`, se devuelve un error `400`.

| Cómo llamas al modelo | Límite de salida sin decodificación larga | Decodificación prolongada al inicio | Qué hacer |
| --- | --- | --- | --- |
| SDK de IA generativa de Google, versión más reciente | 64 K | Sí, el SDK continúa por ti | Establece `max_output_tokens`. |
| SDK de IA generativa de Google, versión anterior, sin transmisión | 64 K | No | Actualiza el SDK. |
| REST `streamGenerateContent` | 64 K | Sí, con tu propio bucle | Escribe un bucle. Consulta la [opción 2](#option-2-loop). |
| REST `generateContent` | 32,000 | Sí, con tu propio bucle | Escribe un bucle. Consulta la [opción 2](#option-2-loop). |

## Cuándo usar la decodificación larga

La mayoría de las solicitudes se completan dentro del límite de una sola solicitud (64 000 tokens para las llamadas de transmisión y del SDK, o 32 000 tokens para las llamadas de REST que no son de transmisión). Usa la decodificación larga cuando una respuesta necesite más tokens de razonamiento y de salida combinados de los que permite una sola solicitud. Aumentar `max_output_tokens` le da al modelo un límite más alto para razonar sobre problemas difíciles, en lugar de hacer que las respuestas estándar sean más largas.

| Carga de trabajo | ¿Quieres usar la decodificación larga? | Por qué |
| --- | --- | --- |
| Matemáticas, ciencias, investigación y pruebas formales complejas | Sí | El modelo puede usar más de 64,000 tokens para explorar y verificar su razonamiento. |
| Las tareas de programación y de agentes más difíciles | Sí | Algunas tareas necesitan más de 64,000 tokens de razonamiento y código en una sola respuesta. La mayoría de las tareas de programación y de agentes finalizan con menos de 64,000 tokens. |
| Arneses de evaluación que se detienen en el límite de salida | Sí | La decodificación larga evita que se corten las respuestas cuando el modelo dedica una solicitud completa de 64,000 o 32,000 tokens al pensamiento. |
| Chat, preguntas y respuestas, resumen, clasificación y extracción | No | Estas tareas se completan con menos de 32,000 tokens. |
| Solicitudes de una longitud fija, como "escribe un libro de 700,000 palabras" | No | El modelo no sigue los objetivos de longitud. |
| Agentes que llaman a herramientas en muchos turnos cortos | No | Cada turno es corto. Las salidas grandes en cada turno llenan rápidamente la ventana unificada de entrada y salida de 1M. |
| Instrucciones cerca del límite de entrada de 1 millón | No | La salida solo puede usar 1 millón menos tu entrada. |
| Solicitudes sensibles a la latencia | No | La decodificación larga puede ejecutarse durante varios minutos. |

Establecer un valor alto de `max_output_tokens` le da al modelo espacio para pensar más tiempo en problemas difíciles, pero el modelo sigue decidiendo cuánto escribir. Para controlar cuánto esfuerzo de razonamiento usa el modelo, establece [`thinking_level`](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=es-419).

## Activa la decodificación larga

Puedes ejecutar la decodificación larga automáticamente con el SDK de IA generativa de Google (opción 1, recomendada para la mayoría de las apps) o escribir tu propio bucle de continuación (opción 2). Ambas opciones admiten la ventana de contexto completa de 1 millón de tokens.

|  | Opción 1: SDK de Google GenAI (recomendado) | Opción 2: Tu propio bucle de transmisión | Opción 2: Tu propio bucle que no es de transmisión |
| --- | --- | --- | --- |
| **Quién inicia cada salto** | El SDK Tú estableces `max_output_tokens`. | Tu código, en cada punto de control o después de una transmisión interrumpida | Tu código, cada 32,000 tokens |
| **Tokens por solicitud** | 64 K por salto | 64 K por transmisión, con un punto de control cada 5 K tokens después de 32 K | 32,000 por solicitud |
| **Límite de tiempo por solicitud** | 20 minutos | 20 minutos | 20 minutos |
| **Almacenamiento** | No hay almacenamiento en el servidor | No hay almacenamiento en el servidor | No hay almacenamiento en el servidor |
| **Ideal para** | La mayoría de las aplicaciones | Llamadores de REST y arneses personalizados que transmiten | Arneses de evaluación simples |

El `continuation_token` encriptado transporta el estado del modelo entre solicitudes, por lo que no se almacena nada en el servidor.

### Opción 1: Usa el SDK de Google GenAI (recomendado)

En el SDK de GenAI de Google más reciente, `automatic_continuation` está habilitado de forma predeterminada para las llamadas de transmisión y las que no son de transmisión, por lo que no es necesario que lo configures. Cuando configuras `max_output_tokens` por encima del límite por solicitud, el SDK ejecuta automáticamente los saltos de continuación y devuelve una respuesta combinada.

1. Actualiza el SDK.

   ### Python

   ```
   pip install -U "google-genai>=2.30.1"
   ```

   ### JavaScript

   ```
   npm install "@google/genai@>=2.29.1"
   ```
2. Establece `max_output_tokens` en un valor mayor que 65,536.

   ### Python

   ```
   from google import genai
   from google.genai import types

   client = genai.Client()  # Reads GEMINI_API_KEY

   response = client.models.generate_content(
       model="gemini-4-argon",
       contents="Write a complete, rigorous proof of the prime number theorem.",
       config=types.GenerateContentConfig(
           max_output_tokens=262_144,  # Total thinking and output for all hops
           thinking_config=types.ThinkingConfig(thinking_level="high"),
           automatic_continuation=True,  # Default. Shown for clarity.
       ),
   )

   print(response.text)
   print("Finish reason:", response.candidates[0].finish_reason)
   print("Prompt size:", response.usage_metadata.initial_prompt_token_count)
   print("Billed tokens:", response.usage_metadata.total_token_count)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI, ThinkingLevel } from "@google/genai";

   const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY

   const response = await ai.models.generateContent({
     model: "gemini-4-argon",
     contents: "Write a complete, rigorous proof of the prime number theorem.",
     config: {
       maxOutputTokens: 262144, // Total thinking and output for all hops
       thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
       automaticContinuation: true, // Default. Shown for clarity.
     },
   });

   console.log(response.text);
   console.log("Finish reason:", response.candidates?.[0]?.finishReason);
   console.log("Prompt size:", response.usageMetadata?.initialPromptTokenCount);
   console.log("Billed tokens:", response.usageMetadata?.totalTokenCount);
   ```

Recuerda estos puntos:

- **Transmisión:** `generate_content_stream` (Python) y `generateContentStream` (JavaScript) también continúan para ti. Si una transmisión se interrumpe después de un punto de control, el SDK se reanuda desde ese punto de control.
- **Tiempos de espera:** Los tiempos de espera y los reintentos se aplican a cada salto, no a la ejecución completa.
- **Control manual:** Para ejecutar el bucle por tu cuenta, establece `automatic_continuation=False` (Python) o `automaticContinuation: false` (JavaScript). Luego, sigue la opción 2.
- **Uso:** Los campos de uso muestran la suma de todos los saltos. Para obtener el tamaño de tu instrucción, lee `initial_prompt_token_count`. Consulta [Recuento de tokens](#count-tokens).

### Opción 2: Escribe tu propio bucle

Escribe tu propio bucle si llamas a REST directamente, usas un lenguaje sin el SDK más reciente o necesitas un control total. También puedes consultar nuestras implementaciones del SDK de IA generativa de Google en [Python](https://github.com/googleapis/python-genai/blob/v2.30.1/google/genai/models.py#L6111) y [JavaScript/TypeScript](https://github.com/googleapis/js-genai/blob/v2.29.1/src/models.ts#L88) como referencia.

Siga estas reglas:

1. **Enviar la misma solicitud en cada salto** Envía los atributos originales `contents`, `system_instruction`, `tools` y `generation_config`. Mantén `max_output_tokens` igual.
2. **No agregues resultados parciales a `contents`.** El `continuation_token` contiene el estado del modelo, incluido su proceso de pensamiento.
3. **Envía solo el token más reciente.** Cada token contiene todo el progreso anterior.
4. **Continúa mientras `finish_reason` es `CONTINUATION`.** Se detiene por cualquier otro motivo de finalización.
5. **Une las partes después del último salto.** Combina las partes de todos los saltos en un turno de modelo para el historial de conversaciones.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()  # Reads GEMINI_API_KEY
PROMPT = "Write a complete, rigorous proof of the prime number theorem."
parts = []
token = None

while True:
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents=PROMPT,  # The original contents on every request
        config=types.GenerateContentConfig(
            max_output_tokens=262_144,  # The same total on every request
            thinking_config=types.ThinkingConfig(thinking_level="high"),
            automatic_continuation=False,  # You run the loop
            continuation_token=token,
        ),
    )
    candidate = response.candidates[0]
    if candidate.content and candidate.content.parts:
        parts.extend(candidate.content.parts)
    token = candidate.continuation_token
    if candidate.finish_reason != types.FinishReason.CONTINUATION or not token:
        break

print("".join(p.text for p in parts if p.text and not p.thought))
print("Finish reason:", candidate.finish_reason)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
const PROMPT = "Write a complete, rigorous proof of the prime number theorem.";
const parts = [];
let token = undefined;
let candidate = undefined;

while (true) {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: PROMPT, // The original contents on every request
    config: {
      maxOutputTokens: 262144, // The same total on every request
      thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
      automaticContinuation: false, // You run the loop
      continuationToken: token,
    },
  });
  candidate = response.candidates?.[0];
  if (candidate?.content?.parts) {
    parts.push(...candidate.content.parts);
  }
  token = candidate?.continuationToken;
  if (candidate?.finishReason !== "CONTINUATION" || !token) {
    break;
  }
}

console.log(parts.filter((p) => p.text && !p.thought).map((p) => p.text).join(""));
console.log("Finish reason:", candidate?.finishReason);
```

### REST

```
# Hop 1: send the request with max_output_tokens.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    }
  }'

# Hop 2: if finishReason is CONTINUATION, send the same request plus the token.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    },
    "continuationToken": "TOKEN_FROM_HOP_1"
  }'
```

Un salto dedicado por completo a la reflexión devuelve un `text` vacío con `finishReason: "CONTINUATION"`. Trata esto como un progreso normal y solicita el próximo salto:

```
{
  "candidates": [{
    "content": {"role": "model", "parts": [{"text": ""}]},
    "finishReason": "CONTINUATION",
    "continuationToken": "CiQ4ZmQ3..."
  }],
  "usageMetadata": {
    "promptTokenCount": 142,
    "candidatesTokenCount": 0,
    "thoughtsTokenCount": 32768,
    "totalTokenCount": 32910
  }
}
```

Los **bucles de transmisión** necesitan una regla más. Después de los primeros 32,768 tokens, la transmisión envía un token de punto de control cada 5,000 tokens. Mantén los fragmentos nuevos en una lista pendiente. Cuando un fragmento tenga un `continuation_token`, mueve los fragmentos pendientes a tu resultado confirmado y guarda el token. Si se interrumpe la transmisión, descarta los fragmentos pendientes y reanuda la transmisión desde el último token. Si la transmisión se interrumpe antes del primer punto de control, vuelve a enviar la solicitud original.

## Conjunto `max_output_tokens`

`max_output_tokens` establece el límite combinado para el pensamiento y la salida en todos los saltos. Disminuirlo no hace que el modelo piense de forma más concisa, sino que corta la respuesta antes.

| Tu carga de trabajo | Recomendada `max_output_tokens` |
| --- | --- |
| Apps existentes con un límite inferior a 32,000 | Aumenta el valor a 32,768. |
| Tareas de programación y de agentes extensas | Comienza en 65,536. |
| Matemáticas, ciencia, investigación y demostraciones difíciles | Valores de prueba desde 262,144 hasta 1,048,576 menos tus tokens de entrada. |

Para usar menos tokens, disminuye `thinking_level`. Usa `high` para las tareas de razonamiento más difíciles. Usa `medium` (la opción predeterminada) para la mayoría de las tareas de programación y de agentes. Usa `low` para tareas menos complejas.

## Cómo controlar solicitudes de larga duración

Como Gemini 4 Argon piensa más tiempo que los modelos Gemini 3.x en problemas difíciles, debes aumentar los tiempos de espera de tus clientes para que las solicitudes largas no se desconecten antes de tiempo.

- **Llamadas que no son de transmisión:** El servidor cierra la conexión después de 10 minutos.
- **Llamadas de transmisión:** El servidor cierra la transmisión después de 20 minutos.
- **Tiempos de espera del cliente:** Establece el tiempo de espera de lectura de HTTP en 20 minutos. Un tiempo de espera de 3 o 5 minutos detiene la solicitud antes de tiempo.

En Python, establece el tiempo de espera en el cliente en milisegundos:

```
client = genai.Client(http_options=types.HttpOptions(timeout=1_200_000))  # 20 minutes
```

En el caso de los trabajos que son sondeados por tu cliente, la API de Interactions ejecuta una decodificación prolongada en el servidor. Consulta [Ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419).

## Reanudar cuando el modelo use todos los tokens de salida

Cuando una respuesta termina con `MAX_TOKENS`, aún incluye un `continuation_token`. Tienes dos opciones:

- **Continuar:** Envía la misma solicitud con el token y un `max_output_tokens` más alto. El valor debe ser superior a los tokens que se usaron hasta el momento. De lo contrario, la API devuelve un error 400.
- **Vuelve a empezar:** Envía la solicitud original con un valor de `max_output_tokens` más alto y sin token. Pagas por ambas ejecuciones.

## Cuenta tokens

Con la continuación automática, `usage_metadata` informa los totales de todos los saltos. El SDK suma todos los campos de recuento: `prompt_token_count`, `cached_content_token_count`, `candidates_token_count`, `thoughts_token_count` y `total_token_count`.

`prompt_token_count` suma los tokens de entrada de cada salto. Cada salto envía tu instrucción y todo lo que se generó hasta el momento de vuelta al modelo como entrada, por lo que los mismos tokens se vuelven a contar en cada salto posterior. Por ejemplo, con el SDK de IA generativa de Google, una instrucción de 1,000 tokens que produce 200,000 tokens de razonamiento y resultado requiere cuatro saltos:

| Hop | Entrada enviada al modelo | Tokens de entrada |
| --- | --- | --- |
| 1 | Instrucción | 1,000 |
| 2 | Instrucción + salto 1 | 66,536 |
| 3 | Instrucción + saltos 1 y 2 | 132,072 |
| 4 | Instrucción + saltos 1 a 3 | 197,608 |
| **Total** |  | **397,216** |

`prompt_token_count` informa sobre 397,000 tokens (con entradas de saltos repetidos que se descuentan automáticamente en un 95% por el almacenamiento en caché implícito), y `total_token_count` informa sobre 597,000 tokens, aunque el tamaño real del contexto es de solo unos 201,000 tokens: la instrucción de 1,000 tokens más 200,000 tokens de pensamiento y salida. Un bucle REST que no es de transmisión usa 32 000 saltos, por lo que se necesitan siete saltos para la misma salida y se registran 695,128 tokens de entrada.

| Cómo llamas al modelo | Qué muestra `usage_metadata` | Por costo | Para el tamaño de la instrucción |
| --- | --- | --- | --- |
| SDK de IA generativa de Google, continuación automática (opción predeterminada) | Totales en todos los saltos | Lee los campos de uso tal como están. | Lee `usage_metadata.initial_prompt_token_count` (Python) o `usageMetadata.initialPromptTokenCount` (JavaScript). |
| SDK con `automatic_continuation=False` o REST | Un salto por respuesta | Agrega cada campo en los diferentes saltos. | Lee `prompt_token_count` desde el primer salto. |

`prompt_token_count` y `total_token_count` son la suma de cada salto, no el tamaño de tu contexto. No los uses para decidir cuándo resumir o recortar tu historial de conversaciones (compactación del contexto) ni para aplicar un límite de contexto. Para estimar el tamaño del contexto, agrega el tamaño de tu instrucción de la tabla a `candidates_token_count` y `thoughts_token_count`.

Actualiza el framework del agente, la herramienta de evaluación o el proxy antes de ejecutar la decodificación larga:

- **Agentes y herramientas de evaluación:** Si tu código compacta el contexto o detiene una ejecución en un límite de tokens, usa `initial_prompt_token_count` (o el `prompt_token_count` del primer salto en REST) en lugar del `prompt_token_count` sumado. Las respuestas que finalizan en un salto informan el mismo valor en ambos campos, por lo que las pruebas cortas no muestran el problema.
- **Proxies y puertas de enlace que llaman a REST:** Cada respuesta de REST informa solo su propio salto. Suma cada campo en los saltos para el costo y mantén el `promptTokenCount` del primer salto como el tamaño de la instrucción. De lo contrario, tus usuarios verán números diferentes de los que ven los usuarios del SDK para la misma solicitud.
- **Registros y respuestas serializadas:** El SDK calcula `initial_prompt_token_count` en el cliente. No se encuentra en la respuesta de REST ni en el resultado JSON del SDK, como `model_dump()`. Guárdalo como un valor independiente si lo necesitas más adelante.

Si transmites en tu propio bucle, `usage_metadata` es acumulativo dentro de cada transmisión. Conserva solo el último valor de cada transmisión y, luego, suma los valores en los saltos.

## Comprende la facturación

Pagas por cada token en cada salto, incluidos los saltos que solo contienen pensamiento.

- **Descuento por almacenamiento en caché:** El almacenamiento en caché implícito descuenta la entrada repetida en cada salto en un 95%. La entrada almacenada en caché cuesta USD 0.10 por cada millón de tokens en lugar de USD 2.00 durante el período de lanzamiento.
- **Vencimiento de la caché:** La caché vence después de 15 a 20 minutos sin uso. Una pausa larga entre saltos vuelve a cobrar la tarifa de entrada completa.
- **Saltos fallidos sin transmisión:** Solo pagas cuando se completa una respuesta. Una solicitud con errores o descartada cuesta $0.
- **Transmisiones descartadas:** Una transmisión que se descarta antes de los 32,000 tokens cuesta $0. Después de eso, pagas hasta el último token de punto de control, porque puedes reanudar desde allí.

## Solución de problemas

| Síntoma | Causa y solución |
| --- | --- |
| La salida se detiene en 64,000 o 32,000 con `CONTINUATION` | Al modelo le quedan tokens, pero nada continuó la solicitud. Actualiza el SDK o agrega un bucle. |
| La salida se detiene en 64 K o 32 K con `MAX_TOKENS` | `max_output_tokens` no está configurado o es demasiado bajo. Establece un valor superior a 65,536. |
| Texto vacío con `MAX_TOKENS` | El modelo usó todos los tokens en el pensamiento. Sube `max_output_tokens` o baja `thinking_level`. |
| 400: "El token de continuación ya usó tokens de salida…" | `max_output_tokens` no supera los tokens usados hasta el momento. Levántala. |
| Error para `thinking_level: "minimal"` o para `thinking_budget` con `thinking_level` | Gemini 4 Argon no admite `minimal`. Usa `low`, `medium` o `high`. Configura `thinking_level` o `thinking_budget`, pero no ambos. |
| Advertencia para `thinking_budget`, `temperature`, `top_p` o `top_k` | Gemini 4 Argon ignora o asigna estos campos. Usa `thinking_level` y quita los parámetros de muestreo. |
| La solicitud finaliza después de 3 o 5 minutos | El tiempo de espera del cliente es demasiado corto. Establécelo en 20 minutos. |
| La compactación de contexto comienza demasiado pronto | El harness lee la entrada sumada. Lee `initial_prompt_token_count` en su lugar. |

## Limitaciones

- **Extremo de compatibilidad con OpenAI:** La decodificación larga no está disponible. La salida se detiene en el límite por solicitud.
- **SDKs más antiguos:** Las versiones anteriores a las mínimas que se indican en la nota no continúan automáticamente.
- **Longitud:** El modelo no sigue los objetivos de longitud de tokens ni de recuento de palabras.

## Lista de tareas

- Actualiza el SDK de GenAI de Google a la versión mínima.
- Establece `max_output_tokens` en un valor mayor que 65,536.
- Usa `thinking_level` (`low`, `medium` o `high`), no `thinking_budget`.
- Establece los tiempos de espera de lectura de HTTP en 20 minutos.
- Usa `initial_prompt_token_count` para el tamaño y la compactación del contexto.
- Ejecuta una instrucción como prueba antes de una evaluación grande.

## Próximos pasos

- [Novedades de Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=es-419)
- [Pensamiento](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=es-419)
- [Recuento de tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-13 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-13 (UTC)"],[],[]]
