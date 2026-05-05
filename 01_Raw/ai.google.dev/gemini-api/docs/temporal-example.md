---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=es-419
fetched_at: 2026-05-05T19:49:10.274781+00:00
title: "Agente de IA duradero con Gemini y Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agente de IA duradero con Gemini y Temporal

En este instructivo, se explica cómo compilar un
[bucle de agente de estilo ReAct](https://arxiv.org/abs/2210.03629) que usa la
API de Gemini para el razonamiento y [Temporal](https://temporal.io/) para la durabilidad.
El código fuente completo de este instructivo está disponible en
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

El agente puede llamar a herramientas, como buscar alertas meteorológicas o geolocalizar una dirección IP, y se repetirá hasta que tenga suficiente información para responder.

Lo que diferencia a este agente de una demostración típica es la **durabilidad**. Temporal conserva cada llamada a LLM, cada invocación de herramienta y cada paso del bucle de agente. Si el proceso falla, la red se cae o se agota el tiempo de espera de una API, Temporal vuelve a intentarlo automáticamente y se reanuda desde el último paso completado. No se pierde el historial de conversaciones ni se repiten de forma incorrecta las llamadas a herramientas.

## Arquitectura

La arquitectura consta de tres partes:

- **Flujo de trabajo:** Es el bucle de agente que organiza la lógica de ejecución.
- **Actividades:** Son unidades de trabajo individuales (llamadas a LLM, llamadas a herramientas) que Temporal hace duraderas.
- **Trabajador:** Es el proceso que ejecuta los flujos de trabajo y las actividades.

En este ejemplo, colocarás las tres partes en un solo archivo (`durable_agent_worker.py`). En una implementación real, las separarías para permitir varias ventajas de implementación y escalabilidad. Colocarás el código que proporciona una instrucción al agente en un segundo archivo (`start_workflow.py`).

## Requisitos previos

Para completar esta guía, necesitarás lo siguiente:

- Una clave de API de Gemini. Puedes crear una gratis en
  [Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).
- [Python](https://www.python.org/downloads/) versión 3.10 o posterior.
- La [CLI de Temporal](https://docs.temporal.io/cli) para ejecutar un servidor de desarrollo
  local.

## Configuración

Antes de comenzar, asegúrate de tener un
[servidor de desarrollo de Temporal](https://docs.temporal.io/cli#start-dev-server)
ejecutándose de forma local:

```
temporal server start-dev
```

Luego, instala las dependencias requeridas:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Crea un archivo `.env` en el directorio de tu proyecto con tu clave de API de Gemini. Puedes
obtener una clave de API en
[Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Implementación

En el resto de este instructivo, se explica `durable_agent_worker.py` de principio a fin, y se compila el agente paso a paso. Crea el archivo y sigue los pasos.

### Importaciones y configuración de sandbox

Comienza con las importaciones que se deben definir por adelantado. El bloque `workflow.unsafe.imports_passed_through()` le indica al sandbox de flujo de trabajo de Temporal que permita el paso de ciertos módulos sin restricciones. Esto es necesario porque varias bibliotecas (en particular, `httpx`, que subclases `urllib.request.Request`) usan patrones que el sandbox bloquearía de otro modo.

```
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    import pydantic_core  # noqa: F401
    import annotated_types  # noqa: F401

    import httpx
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
```

### Instrucciones del sistema

A continuación, define la personalidad del agente. Las instrucciones del sistema le indican al modelo cómo debe comportarse. Se le indica a este agente que responda en haikus cuando no se necesiten herramientas.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Definiciones de herramientas

Ahora define las herramientas que puede usar el agente. Cada herramienta es una función asíncrona con una cadena de documentación descriptiva. Las herramientas que toman parámetros usan un modelo Pydantic como su único argumento. Esta es una práctica recomendada de Temporal que mantiene estables las firmas de actividad a medida que agregas campos opcionales con el tiempo.

```
import json

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class GetWeatherAlertsRequest(BaseModel):
    """Request model for getting weather alerts."""

    state: str = Field(description="Two-letter US state code (e.g. CA, NY)")

async def get_weather_alerts(request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        request: The request object containing:
            - state: Two-letter US state code (e.g. CA, NY)
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=5.0)
        response.raise_for_status()
        return json.dumps(response.json())
```

A continuación, define las herramientas para la geolocalización de direcciones IP:

```
class GetLocationRequest(BaseModel):
    """Request model for getting location info from an IP address."""

    ipaddress: str = Field(description="An IP address")

async def get_ip_address() -> str:
    """Get the public IP address of the current machine."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://icanhazip.com")
        response.raise_for_status()
        return response.text.strip()

async def get_location_info(request: GetLocationRequest) -> str:
    """Get the location information for an IP address including city, state, and country.

    Args:
        request: The request object containing:
            - ipaddress: An IP address to look up
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{request.ipaddress}")
        response.raise_for_status()
        result = response.json()
        return f"{result['city']}, {result['regionName']}, {result['country']}"
```

### Registro de herramientas

A continuación, crea un registro que asigne nombres de herramientas a funciones de controlador. La función
`get_tools()` genera objetos `FunctionDeclaration` compatibles con Gemini
a partir de los objetos invocables con `FunctionDeclaration.from_callable_with_api_option()`.

```
from typing import Any, Awaitable, Callable

ToolHandler = Callable[..., Awaitable[Any]]

def get_handler(tool_name: str) -> ToolHandler:
    """Get the handler function for a given tool name."""
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    raise ValueError(f"Unknown tool name: {tool_name}")

def get_tools() -> types.Tool:
    """Get the Tool object containing all available function declarations.

    Uses FunctionDeclaration.from_callable_with_api_option() from the Google GenAI SDK
    to generate tool definitions from the handler functions.
    """
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_weather_alerts, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_location_info, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_ip_address, api_option="GEMINI_API"
            ),
        ]
    )
```

### Actividad de LLM

Ahora define la actividad que llama a la API de Gemini. Las clases de datos `GeminiChatRequest` y `GeminiChatResponse` definen el contrato.

Inhabilitarás la llamada a función automática para que la invocación de LLM y la invocación de herramienta se controlen como tareas separadas, lo que aportará más durabilidad a tu agente. También inhabilitarás los reintentos integrados del SDK (`attempts=1`), ya que Temporal controla los reintentos de forma duradera.

```
import os
from dataclasses import dataclass

from temporalio import activity

@dataclass
class GeminiChatRequest:
    """Request parameters for a Gemini chat completion."""

    model: str
    system_instruction: str
    contents: list[types.Content]
    tools: list[types.Tool]

@dataclass
class GeminiChatResponse:
    """Response from a Gemini chat completion."""

    text: str | None
    function_calls: list[dict[str, Any]]
    raw_parts: list[types.Part]

@activity.defn
async def generate_content(request: GeminiChatRequest) -> GeminiChatResponse:
    """Execute a Gemini chat completion with tool support."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    config = types.GenerateContentConfig(
        system_instruction=request.system_instruction,
        tools=request.tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    response = await client.aio.models.generate_content(
        model=request.model,
        contents=request.contents,
        config=config,
    )

    function_calls = []
    raw_parts = []
    text_parts = []

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            raw_parts.append(part)
            if part.function_call:
                function_calls.append(
                    {
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args) if part.function_call.args else {},
                    }
                )
            elif part.text:
                text_parts.append(part.text)

    text = "".join(text_parts) if text_parts and not function_calls else None

    return GeminiChatResponse(
        text=text,
        function_calls=function_calls,
        raw_parts=raw_parts,
    )
```

### Actividad de herramienta dinámica

A continuación, define la actividad que ejecuta herramientas. Esto usa la función de actividad dinámica de Temporal: el controlador de herramientas (un objeto invocable) se obtiene del registro de herramientas a través de la función `get_handler`. Esto permite definir diferentes agentes con solo proporcionar un conjunto diferente de herramientas e instrucciones del sistema. El flujo de trabajo que implementa el bucle de agente no requiere cambios.

La actividad inspecciona la firma del controlador para determinar cómo pasar argumentos. Si el controlador espera un modelo Pydantic, controla el formato de salida anidado
que produce Gemini (por ejemplo, `{"request": {"state": "CA"}}` en lugar
de un `{"state": "CA"}` plano).

```
import inspect
from collections.abc import Sequence

from temporalio.common import RawValue

@activity.defn(dynamic=True)
async def dynamic_tool_activity(args: Sequence[RawValue]) -> dict:
    """Execute a tool dynamically based on the activity name."""
    tool_name = activity.info().activity_type
    tool_args = activity.payload_converter().from_payload(args[0].payload, dict)
    activity.logger.info(f"Running dynamic tool '{tool_name}' with args: {tool_args}")

    handler = get_handler(tool_name)

    if not inspect.iscoroutinefunction(handler):
        raise TypeError("Tool handler must be async (awaitable).")

    sig = inspect.signature(handler)
    params = list(sig.parameters.values())

    if len(params) == 0:
        result = await handler()
    else:
        param = params[0]
        param_name = param.name
        ann = param.annotation

        if isinstance(ann, type) and issubclass(ann, BaseModel):
            nested_args = tool_args.get(param_name, tool_args)
            result = await handler(ann(**nested_args))
        else:
            result = await handler(**tool_args)

    activity.logger.info(f"Tool '{tool_name}' result: {result}")
    return result
```

### El flujo de trabajo del bucle de agente

Ahora tienes todas las piezas para terminar de compilar el agente. La clase `AgentWorkflow` implementa un flujo de trabajo que contiene el bucle de agente. Dentro de ese bucle, se invoca el LLM a través de la actividad (lo que lo hace duradero), se inspecciona el resultado y, si el LLM eligió una herramienta, se invoca a través de `dynamic_tool_activity`.

En este agente simple de estilo ReAct, una vez que el LLM decide no usar una herramienta, el bucle se considera completo y se muestra el resultado final del LLM.

```
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Agentic loop workflow that uses Gemini for LLM calls and executes tools."""

    @workflow.run
    async def run(self, input: str) -> str:
        contents: list[types.Content] = [
            types.Content(role="user", parts=[types.Part.from_text(text=input)])
        ]

        tools = [get_tools()]

        while True:
            result = await workflow.execute_activity(
                generate_content,
                GeminiChatRequest(
                    model="gemini-3-flash-preview",
                    system_instruction=SYSTEM_INSTRUCTIONS,
                    contents=contents,
                    tools=tools,
                ),
                start_to_close_timeout=timedelta(seconds=60),
            )

            if result.function_calls:
                # Sending the complete raw_parts here ensures Gemini 3 thought
                # signatures are propagated correctly.
                contents.append(types.Content(role="model", parts=result.raw_parts))

                for function_call in result.function_calls:
                    tool_result = await self._handle_function_call(function_call)

                    contents.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call["name"],
                                    response={"result": tool_result},
                                )
                            ],
                        )
                    )
            else:
                return result.text
            # Leave this in place. You will un-comment it during a durability
            # test later on.
            # await asyncio.sleep(10)

    async def _handle_function_call(self, function_call: dict) -> str:
        """Execute a tool via dynamic activity and return the result."""
        tool_name = function_call["name"]
        tool_args = function_call.get("args", {})

        result = await workflow.execute_activity(
            tool_name,
            tool_args,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return result
```

El bucle de agente es completamente duradero. Si el trabajador del agente falla después de varias iteraciones a través del bucle, Temporal retomará exactamente donde lo dejó sin necesidad de volver a invocar las invocaciones de LLM o las llamadas a herramientas ya ejecutadas.

### Inicio del trabajador

Por último, conecta todo. Si bien el código implementa la lógica empresarial necesaria de una manera que hace que parezca que se ejecuta en un solo proceso, el uso de Temporal lo convierte en un sistema controlado por eventos (específicamente, de origen de eventos) en el que la comunicación entre el flujo de trabajo y las actividades se realiza a través de la mensajería que proporciona Temporal.

El trabajador de Temporal se conecta al servicio de Temporal y actúa como un programador para las tareas de flujo de trabajo y actividad. El trabajador registra el flujo de trabajo y ambas actividades, y luego comienza a escuchar las tareas.

```
import asyncio
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter
from temporalio.envconfig import ClientConfig
from temporalio.worker import Worker

async def main():
    config = ClientConfig.load_client_connect_config()
    config.setdefault("target_host", "localhost:7233")
    client = await Client.connect(
        **config,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="gemini-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            generate_content,
            dynamic_tool_activity,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
```

## La secuencia de comandos del cliente

Crea la secuencia de comandos del cliente (`start_workflow.py`). Envía una consulta y espera el resultado. Ten en cuenta que se conecta a la misma lista de tareas en cola a la que se hace referencia en el trabajador del agente. La secuencia de comandos `start_workflow` envía una tarea de flujo de trabajo con la instrucción del usuario a esa lista de tareas en cola, lo que inicia la ejecución del agente.

```
import asyncio
import sys
import uuid

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Tell me about recursion"

    result = await client.execute_workflow(
        "AgentWorkflow",
        query,
        id=f"gemini-agent-id-{uuid.uuid4()}",
        task_queue="gemini-agent-python-task-queue",
    )
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Ejecuta el agente

Si aún no lo hiciste, inicia el servidor de desarrollo de Temporal:

```
temporal server start-dev
```

En una ventana de terminal nueva, inicia el trabajador del agente:

```
python -m durable_agent_worker
```

En una tercera ventana de terminal, envía una consulta a tu agente:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Observa el resultado en la terminal de `durable_agent_worker` que muestra las acciones que ocurren en cada iteración del bucle de agente. El LLM puede satisfacer la solicitud del usuario invocando una serie de herramientas a su disposición. Puedes ver los pasos que se ejecutaron a través de la IU de Temporal en `http://localhost:8233/namespaces/default/workflows`.

Prueba algunas instrucciones diferentes para ver el razonamiento del agente y las herramientas de llamada:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

La última instrucción no requiere ninguna herramienta, por lo que el agente responde en un haiku basado en `SYSTEM_INSTRUCTIONS`.

## Prueba la durabilidad (opcional)

La compilación en Temporal garantiza que tu agente sobreviva a las fallas sin problemas. Puedes probar esto con dos experimentos distintos.

### Simula una interrupción de la red

En esta prueba, inhabilitarás temporalmente la conexión a Internet de tu computadora, enviarás un flujo de trabajo, observarás cómo Temporal vuelve a intentarlo automáticamente y, luego, restablecerás la red para ver cómo se recupera.

1. Desconecta tu máquina de Internet (por ejemplo, desactiva la red Wi-Fi).
2. Envía un flujo de trabajo:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Consulta la IU de Temporal (`http://localhost:8233`). Verás que la actividad de LLM falla y que Temporal administra automáticamente los reintentos en segundo plano.
4. Vuelve a conectarte a Internet.
5. El siguiente reintento automático llegará correctamente a la API de Gemini y tu terminal imprimirá el resultado final.

### Sobrevive a una falla del trabajador

En esta prueba, finalizas el trabajador a mitad de la ejecución y lo reinicias. Temporal reproduce el historial del flujo de trabajo (origen de eventos) y se reanuda desde la última actividad completada. No se repiten las invocaciones de LLM ni las llamadas a herramientas ya completadas.

1. Para darte tiempo de finalizar el Worker, abre `durable_agent_worker.py` y quita temporalmente la marca de comentario de `await asyncio.sleep(10)` dentro del bucle `run` de `AgentWorkflow`.
2. Reinicia el trabajador:

   ```
   python -m durable_agent_worker
   ```
3. Envía una consulta que active varias herramientas:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Finaliza el proceso de trabajador en cualquier momento antes de que se complete (`Ctrl-C` en la terminal del trabajador o con `kill %1` si se ejecuta en segundo plano).
5. Reinicia el trabajador:

   ```
   python -m durable_agent_worker
   ```

Temporal reproduce el historial del flujo de trabajo. Las llamadas a LLM y las invocaciones de herramientas que ya se completaron **no** se vuelven a ejecutar. Sus resultados se reproducen instantáneamente desde el historial (el registro de eventos). El flujo de trabajo finaliza correctamente.

## Más recursos

- [Documentación de Temporal](https://docs.temporal.io/)
- [SDK de Python de Temporal](https://docs.temporal.io/develop/python)
- [SDK de Google GenAI](https://googleapis.github.io/python-genai/)
- [Código fuente de este instructivo](https://github.com/temporal-community/durable-react-agent-gemini)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
