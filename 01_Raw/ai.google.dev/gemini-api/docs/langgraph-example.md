---
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example?hl=es-419
fetched_at: 2026-05-05T20:03:37.813676+00:00
title: "Agente ReAct desde cero con Gemini y LangGraph \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agente ReAct desde cero con Gemini y LangGraph

LangGraph es un framework para compilar aplicaciones de LLM con estado, lo que lo convierte en una buena opción para crear agentes de ReAct (razonamiento y acción).

Los agentes de ReAct combinan el razonamiento del LLM con la ejecución de acciones. Piensan de forma iterativa, usan herramientas y actúan en función de las observaciones para lograr los objetivos del usuario, y adaptan su enfoque de forma dinámica. Presentado en ["ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/abs/2210.03629) (2023), este patrón intenta imitar la resolución de problemas flexible y similar a la humana en lugar de flujos de trabajo rígidos.

LangGraph ofrece un agente de ReAct compilado previamente ([`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)),
que resulta útil cuando necesitas más control y personalización para tus implementaciones de ReAct. En esta guía, se muestra una versión simplificada.

LangGraph modela los agentes como gráficos con tres componentes clave:

- `State`: Estructura de datos compartida (por lo general, `TypedDict` o `Pydantic BaseModel`) que representa la instantánea actual de la aplicación.
- `Nodes`: Codifica la lógica de tus agentes. Reciben el estado actual como entrada, realizan algún cálculo o efecto secundario, y devuelven un estado actualizado, como llamadas a LLM o llamadas a herramientas.
- `Edges`: Define el siguiente `Node` que se ejecutará en función del `State` actual, lo que permite la lógica condicional y las transiciones fijas.

Si aún no tienes una clave de API, puedes obtenerla en [Google AI Studio](https://aistudio.google.com/app/apikey?hl=es-419).

```
pip install langgraph langchain-google-genai geopy requests
```

Establece tu clave de API en la variable de entorno `GEMINI_API_KEY`.

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

Para comprender mejor cómo implementar un agente de ReAct con LangGraph, esta guía te mostrará un ejemplo práctico. Crearás un agente cuyo objetivo es usar una herramienta para encontrar el clima actual de una ubicación específica.

En este agente meteorológico, el `State` mantendrá el historial de conversación en curso (como una lista de mensajes) y un contador (como un número entero) para la cantidad de pasos realizados, con fines ilustrativos.

LangGraph proporciona una función auxiliar, `add_messages`, para actualizar las listas de mensajes de estado. Funciona como un [reductor](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers), ya que toma la lista actual, más los mensajes nuevos, y devuelve una lista combinada. Maneja las actualizaciones por ID de mensaje y, de forma predeterminada, tiene un comportamiento de "solo agregar" para los mensajes nuevos y no vistos.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

A continuación, define tu herramienta del clima.

```
from langchain_core.tools import tool
from geopy.geocoders import Nominatim
from pydantic import BaseModel, Field
import requests

geolocator = Nominatim(user_agent="weather-app")

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """Retrieves the weather using Open-Meteo API.

    Takes a given location (city) and a date (yyyy-mm-dd).

    Returns:
        A dict with the time and temperature for each hour.
    """
    # Note that Colab may experience rate limiting on this service. If this
    # happens, use a machine to which you have exclusive access.
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return dict(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}

tools = [get_weather_forecast]
```

Ahora, inicializa el modelo y vincula las herramientas a él.

```
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-3-flash-preview",
    temperature=1.0,
    max_retries=2,
    google_api_key=api_key,
)

# Bind tools to the model
model = llm.bind_tools([get_weather_forecast])

# Test the model with tools
res=model.invoke(f"What is the weather in Berlin on {datetime.today()}?")

print(res)
```

El último paso antes de ejecutar tu agente es definir los nodos y los bordes.
En este ejemplo, tienes dos nodos y una arista.

- Nodo `call_tool` que ejecuta el método de tu herramienta. LangGraph tiene un nodo prediseñado para esto llamado [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
- Nodo `call_model` que usa `model_with_tools` para llamar al modelo.
- Borde `should_continue` que decide si se debe llamar a la herramienta o al modelo.

La cantidad de nodos y aristas no es fija. Puedes agregar tantos nodos y aristas como quieras a tu gráfico. Por ejemplo, podrías agregar un nodo para agregar una salida estructurada o un nodo de autoverificación o reflexión para verificar la salida del modelo antes de llamar a la herramienta o al modelo.

```
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # This returns a list, which combines with the existing messages state
    # using the add_messages reducer.
    return {"messages": [response]}

# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"
```

Con todos los componentes del agente listos, ahora puedes ensamblarlos.

```
from langgraph.graph import StateGraph, END

# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add the nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return,
    # and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()
```

Puedes visualizar tu gráfico con el método `draw_mermaid_png`.

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png?hl=es-419)

Ahora, ejecuta el agente.

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Ahora puedes continuar con tu conversación, preguntar el clima en otra ciudad o solicitar una comparación.

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
