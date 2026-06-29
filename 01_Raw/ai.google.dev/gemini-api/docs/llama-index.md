---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=es-419
fetched_at: 2026-06-29T05:30:49.675015+00:00
title: "Agente de investigaci\u00f3n con Gemini y LlamaIndex \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agente de investigación con Gemini y LlamaIndex

LlamaIndex es un framework para compilar agentes de conocimiento con LLM conectados a tus datos. En este ejemplo, se muestra cómo compilar un flujo de trabajo multiagente para un agente de investigación. En LlamaIndex, los [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/) son los componentes básicos de los sistemas de agentes y multiagente.

Necesitas una clave de la API de Gemini. Si aún no tienes una, puedes [obtener una en Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).
Primero, instala todas las bibliotecas requeridas de LlamaIndex. LlamaIndex usa el paquete `google-genai` de forma interna.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## Configura Gemini en LlamaIndex

El motor de cualquier agente de LlamaIndex es un LLM que controla el razonamiento y el procesamiento de texto. En este ejemplo, se usa Gemini 3 Flash. Asegúrate de [configurar tu clave de API como una variable de entorno](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419).

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## Herramientas de compilación

Los agentes usan herramientas para interactuar con el mundo exterior, como buscar en la Web o almacenar información. Las [herramientas en LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/) pueden ser funciones regulares de Python o importarse desde `ToolSpecs` preexistentes.
Gemini incluye una herramienta integrada para usar la Búsqueda de Google, que se usa aquí.

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3.5-flash",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

Ahora, prueba la instancia del LLM con una búsqueda que requiera buscar. En esta guía, se supone que hay un bucle de eventos en ejecución (como `python -m asyncio` o Google Colab).

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

El agente de investigación usará funciones de Python como herramientas. Existen muchas formas de crear un sistema para realizar esta tarea. En este ejemplo, usarás lo siguiente:

1. `search_web` usa Gemini con la Búsqueda de Google para buscar información en la Web sobre el tema determinado.
2. `record_notes` guarda la investigación que se encuentra en la Web en el estado para que las otras herramientas puedan usarla.
3. `write_report` escribe el informe con la información que encontró `ResearchAgent`
4. `review_report` revisa el informe y proporciona comentarios.

La clase `Context` pasa el estado entre los agentes o las herramientas, y cada agente tendrá acceso al estado actual del sistema.

```
from llama_index.core.workflow import Context

async def search_web(ctx: Context, query: str) -> str:
    """Useful for searching the web about a specific query or topic"""
    response = await llm_with_search.acomplete(f"""Please research given this query or topic,
    and return the result\n<query_or_topic>{query}</query_or_topic>""")
    return response

async def record_notes(ctx: Context, notes: str, notes_title: str) -> str:
    """Useful for recording notes on a given topic."""
    current_state = await ctx.store.get("state")
    if "research_notes" not in current_state:
        current_state["research_notes"] = {}
    current_state["research_notes"][notes_title] = notes
    await ctx.store.set("state", current_state)
    return "Notes recorded."

async def write_report(ctx: Context, report_content: str) -> str:
    """Useful for writing a report on a given topic."""
    current_state = await ctx.store.get("state")
    current_state["report_content"] = report_content
    await ctx.store.set("state", current_state)
    return "Report written."

async def review_report(ctx: Context, review: str) -> str:
    """Useful for reviewing a report and providing feedback."""
    current_state = await ctx.store.get("state")
    current_state["review"] = review
    await ctx.store.set("state", current_state)
    return "Report reviewed."
```

## Crea un asistente multiagente

Para crear un sistema multiagente, debes definir los agentes y sus interacciones.
Tu sistema tendrá tres agentes:

1. Un `ResearchAgent` busca información en la Web sobre el tema determinado.
2. Un `WriteAgent` escribe el informe con la información que encontró el `ResearchAgent`.
3. Un `ReviewAgent` revisa el informe y proporciona comentarios.

En este ejemplo, se usa la clase `AgentWorkflow` para crear un sistema multiagente que ejecutará estos agentes en orden. Cada agente toma un `system_prompt` que le indica lo que debe hacer y sugiere cómo trabajar con los demás agentes.

De manera opcional, puedes ayudar a tu sistema multiagente especificando con qué otros agentes puede comunicarse usando `can_handoff_to` (si no lo haces, intentará averiguarlo por su cuenta).

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)
from llama_index.core.agent.workflow import FunctionAgent, ReActAgent

research_agent = FunctionAgent(
    name="ResearchAgent",
    description="Useful for searching the web for information on a given topic and recording notes on the topic.",
    system_prompt=(
        "You are the ResearchAgent that can search the web for information on a given topic and record notes on the topic. "
        "Once notes are recorded and you are satisfied, you should hand off control to the WriteAgent to write a report on the topic."
    ),
    llm=llm,
    tools=[search_web, record_notes],
    can_handoff_to=["WriteAgent"],
)

write_agent = FunctionAgent(
    name="WriteAgent",
    description="Useful for writing a report on a given topic.",
    system_prompt=(
        "You are the WriteAgent that can write a report on a given topic. "
        "Your report should be in a markdown format. The content should be grounded in the research notes. "
        "Once the report is written, you should get feedback at least once from the ReviewAgent."
    ),
    llm=llm,
    tools=[write_report],
    can_handoff_to=["ReviewAgent", "ResearchAgent"],
)

review_agent = FunctionAgent(
    name="ReviewAgent",
    description="Useful for reviewing a report and providing feedback.",
    system_prompt=(
        "You are the ReviewAgent that can review a report and provide feedback. "
        "Your feedback should either approve the current report or request changes for the WriteAgent to implement."
    ),
    llm=llm,
    tools=[review_report],
    can_handoff_to=["ResearchAgent","WriteAgent"],
)
```

Los agentes ya están definidos, por lo que ahora puedes crear el `AgentWorkflow` y ejecutarlo.

```
from llama_index.core.agent.workflow import AgentWorkflow

agent_workflow = AgentWorkflow(
    agents=[research_agent, write_agent, review_agent],
    root_agent=research_agent.name,
    initial_state={
        "research_notes": {},
        "report_content": "Not written yet.",
        "review": "Review required.",
    },
)
```

Durante la ejecución del flujo de trabajo, puedes transmitir eventos, llamadas a herramientas y actualizaciones a la consola.

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)

research_topic = """Write me a report on the history of the web.
Briefly describe the history of the world wide web, including
the development of the internet and the development of the web,
including 21st century developments"""

handler = agent_workflow.run(
    user_msg=research_topic
)

current_agent = None
current_tool_calls = ""
async for event in handler.stream_events():
    if (
        hasattr(event, "current_agent_name")
        and event.current_agent_name != current_agent
    ):
        current_agent = event.current_agent_name
        print(f"\n{'='*50}")
        print(f"🤖 Agent: {current_agent}")
        print(f"{'='*50}\n")
    elif isinstance(event, AgentOutput):
        if event.response.content:
            print("📤 Output:", event.response.content)
        if event.tool_calls:
            print(
                "🛠️  Planning to use tools:",
                [call.tool_name for call in event.tool_calls],
            )
    elif isinstance(event, ToolCallResult):
        print(f"🔧 Tool Result ({event.tool_name}):")
        print(f"  Arguments: {event.tool_kwargs}")
        print(f"  Output: {event.tool_output}")
    elif isinstance(event, ToolCall):
        print(f"🔨 Calling Tool: {event.tool_name}")
        print(f"  With arguments: {event.tool_kwargs}")
```

Una vez que se complete el flujo de trabajo, podrás imprimir el resultado final del informe, así como el estado de revisión final del agente de revisión.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## Llega más lejos con los flujos de trabajo personalizados

El `AgentWorkflow` es una excelente manera de comenzar a usar los sistemas multiagente. Pero ¿qué sucede si necesitas más control? Puedes crear un flujo de trabajo desde cero. Estos son
algunos motivos por los que quizás quieras compilar tu propio flujo de trabajo:

- **Más control sobre el proceso**: Puedes decidir la ruta exacta que tomarán tus agentes. Esto incluye crear bucles, tomar decisiones en ciertos puntos o hacer que los agentes trabajen en paralelo en diferentes tareas.
- **Usa datos complejos**: Ve más allá del texto simple. Los flujos de trabajo personalizados te permiten usar datos más estructurados, como objetos JSON o clases personalizadas, para tus entradas y salidas.
- **Trabaja con diferentes medios**: Crea agentes que puedan comprender y procesar no solo texto, sino también imágenes, audio y video.
- **Planificación más inteligente**: Puedes diseñar un flujo de trabajo que primero cree un plan detallado antes de que los agentes comiencen a trabajar. Esto es útil para tareas complejas que requieren varios pasos.
- **Habilita la autocorrección**: Crea agentes que puedan revisar su propio trabajo. Si el resultado no es lo suficientemente bueno, el agente puede volver a intentarlo y crear un ciclo de mejora hasta que el resultado sea perfecto.

Para obtener más información sobre los flujos de trabajo de LlamaIndex, consulta la [documentación de flujos de trabajo de LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-10 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-10 (UTC)"],[],[]]
