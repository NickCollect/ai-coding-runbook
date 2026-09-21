---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=es-419
fetched_at: 2026-09-21T05:49:35.635478+00:00
title: "Rob\u00f3tica con transmisi\u00f3n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Robótica con transmisión

El extremo del modelo `gemini-robotics-er-2-streaming-preview` expone un extremo de transmisión dedicado que se integra con la [API de Live](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=es-419), lo que permite la interacción bidireccional en tiempo real entre tu aplicación y el robot. Esto lo hace adecuado para agentes que necesitan ciclos de retroalimentación rápidos y respuestas reactivas al entorno.

[Probar en Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=es-419)
[Clonar apps de ejemplo desde GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## Casos de uso

- **Coordinación de varios robots**: Varios robots que comunican el estado de las tareas y delegan subtareas a través de una sesión compartida.
- **Supervisión continua**: Robots que observan una escena y activan acciones cuando ocurren eventos específicos, como un contenedor que alcanza un nivel de llenado.
- **Almacén y logística**: Agentes de selección y empaque que verifican los artículos visualmente, hacen un seguimiento del progreso del empaque y se recuperan de los errores.

## Especificaciones técnicas

En la siguiente tabla, se describen las especificaciones técnicas de la API de Live:

| Categoría | Detalles |
| --- | --- |
| Modalidades de entrada | Audio (audio PCM sin procesar de 16 bits, 16 kHz, little-endian), imágenes (JPEG <= 1 FPS), texto |
| Modalidades de salida | Texto |
| Protocolo | Conexión de WebSocket con estado (WSS) |

## Crea una configuración de agente

Cada agente robótico creado en la API de Live sigue tres pasos:

1. **Declara las capacidades del robot como herramientas.** Cada acción que puede realizar el robot (navegar, agarrar, hablar) se convierte en una declaración de función con un nombre, una descripción y un esquema de parámetros. Las acciones físicas deben usar `"behavior": "BLOCKING"` para que el modelo espere a que el robot termine antes de elegir el siguiente paso.
2. **Transmite entrada multimodal en una sesión persistente.** Abre una sesión de `live.connect` y mantenla abierta durante toda la tarea. Envía fotogramas de video, audio o texto a medida que llegan de los sensores del robot.
3. **Controla las llamadas a herramientas en un bucle de recepción.** Cada vez que el modelo selecciona una acción, envía un mensaje `tool_call`. Tu bucle de recepción ejecuta la función en tu SDK de robot y envía un `tool_response`. La sesión permanece abierta y el modelo elige la siguiente acción según el resultado.

En las siguientes secciones, se muestra cómo aplicar estos pasos a tres patrones comunes: un bucle de agente de referencia, la supervisión proactiva de escenas con una señal de monitoreo de funcionamiento y el enrutamiento del habla a través de TTS como herramienta.

## Cómo coordinar un robot a través de llamadas a funciones

En el siguiente ejemplo, se muestran los tres pasos conectados en una sola secuencia de comandos de Python.

Paso 1: Definiciones de herramientas: Declara las capacidades del robot como declaraciones de funciones. La función `navigate` usa `"behavior": "BLOCKING"` para que el modelo espere a que el robot llegue al punto de referencia antes de llamar a otra herramienta.
Agrega más declaraciones de funciones en la misma lista para exponer capacidades adicionales del robot.

El paso 2, Input helpers, muestra tres funciones que transmiten diferentes entradas de modalidad a la sesión: `send_text` para comandos, `send_image` para fotogramas de la cámara con una instrucción de texto opcional y `send_audio` para audio PCM sin procesar de un micrófono.

El paso 3, el bucle de recepción, se ejecuta de forma simultánea y controla dos tipos de mensajes: mensajes `server_content` (la salida de texto del modelo) y mensajes `tool_call` (el modelo solicita una acción del robot). Cuando llega una llamada a la herramienta, el bucle llama a `execute_tool`, un código auxiliar que reemplazas por tu SDK de robot real, y, luego, envía un `tool_response` para que el modelo pueda seleccionar la siguiente acción.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

El bucle de recepción permanece activo después de cada respuesta de la herramienta. El modelo construye y revisa un plan a largo plazo sin que tengas que codificar toda la secuencia de acciones por adelantado.

## Razonamiento espacio-temporal proactivo

La API de Live transmite video, pero los fotogramas de video por sí solos no activan un nuevo turno de razonamiento. Los fotogramas de video deben estar acompañados de una instrucción de texto o audio para activar una respuesta del modelo. Consulta las [capacidades de la API en vivo](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=es-419) para obtener más detalles.

Para habilitar el razonamiento proactivo, implementa un **latido**: Envía periódicamente el fotograma de la cámara más reciente seguido de una instrucción de texto breve que obligue al modelo a inspeccionar la escena y tomar una decisión explícita. La entrada de video está limitada a un fotograma por segundo.

### Implementa el latido

La corrutina de latido se ejecuta como una tarea `asyncio` separada en la misma sesión.
Se orienta de forma oportunista a una cadencia de 1 Hz (que coincide con el límite de frecuencia de entrada de video) mientras espera que se complete cada turno (`er_turn_done`) para evitar interrumpir el razonamiento en curso:

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### Actualiza el bucle de recepción

Para indicar cuándo el modelo completó su turno, actualiza tu `receive_loop` para establecer `er_turn_done`:

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## Salida de audio a través de TTS externo

Gemini Robotics ER 2 devuelve texto. Tu aplicación enruta las respuestas completadas a un proveedor de TTS independiente (como [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419)) a través de una devolución de llamada insertada.
Esto mantiene la latencia del habla, la selección de voz y el comportamiento de interrupción bajo tu control, y te permite intercambiar back-ends de TTS sin cambiar la lógica del agente.

También puedes declarar el TTS como una herramienta para que el modelo trate "decir algo" de la misma manera que "mover el brazo". Agrega la siguiente declaración de función a tu lista de `tools` de la primera sección:

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

Al encapsular el TTS en una declaración de función, el modelo controla el habla a través de la misma ruta de llamada a herramienta que cualquier otra acción del robot. Tu aplicación completa la llamada con una devolución de llamada insertada.

## Ejemplos en GitHub

Para ver ejemplos de trabajo completos, incluidas la demostración de búsqueda de bocadillos del robot Spot y el saludo de paneo e inclinación de Tinybot, consulta los [ejemplos de la API de Robotics Live](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## ¿Qué sigue?

- [Comprensión de video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=es-419): Búsqueda de momentos y clasificación del progreso.
- [Organización de tareas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=es-419): Tareas a largo plazo sin transmisión.
- [Descripción general de la API de Live](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=es-419): Documentación completa de la API de Live

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-16 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-16 (UTC)"],[],[]]
