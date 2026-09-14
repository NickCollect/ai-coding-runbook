---
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example?hl=de
fetched_at: 2026-09-14T05:45:49.569665+00:00
title: "ReAct-Agent mit Gemini und LangGraph von Grund auf erstellen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# ReAct-Agent mit Gemini und LangGraph von Grund auf erstellen

LangGraph ist ein Framework zum Erstellen zustandsorientierter LLM-Anwendungen und eignet sich daher gut für die Entwicklung von ReAct-Agents (Reasoning and Acting).

ReAct-Agents kombinieren LLM-Logik mit der Ausführung von Aktionen. Sie denken iterativ, verwenden Tools und reagieren auf Beobachtungen, um Nutzerziele zu erreichen, wobei sie ihren Ansatz dynamisch anpassen. Dieses Muster wurde 2023 in [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) eingeführt und versucht, die flexible Problemlösung von Menschen anstelle von starren Workflows nachzubilden.

LangGraph bietet einen vordefinierten ReAct-Agenten ([`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)), der sich besonders eignet, wenn Sie mehr Kontrolle und Anpassungsmöglichkeiten für Ihre ReAct-Implementierungen benötigen. In diesem Leitfaden wird eine vereinfachte Version beschrieben.

Bei LangGraph werden Agents als Graphen mit drei Hauptkomponenten modelliert:

- `State`: Gemeinsame Datenstruktur (in der Regel `TypedDict` oder `Pydantic BaseModel`), die den aktuellen Snapshot der Anwendung darstellt.
- `Nodes`: Codiert die Logik Ihrer Agents. Sie erhalten den aktuellen Status als Eingabe, führen eine Berechnung oder einen Nebeneffekt aus und geben einen aktualisierten Status zurück, z. B. LLM- oder Tool-Aufrufe.
- `Edges`: Definiert den nächsten `Node`, der auf Grundlage des aktuellen `State` ausgeführt werden soll. Dies ermöglicht bedingte Logik und feste Übergänge.

Wenn Sie noch keinen API-Schlüssel haben, können Sie einen in [Google AI Studio](https://aistudio.google.com/apikey?hl=de) abrufen.

```
pip install langgraph langchain-google-genai geopy requests
```

Legen Sie Ihren API-Schlüssel in der Umgebungsvariable `GEMINI_API_KEY` fest.

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

In diesem Leitfaden wird anhand eines praktischen Beispiels erläutert, wie Sie einen ReAct-Agenten mit LangGraph implementieren. Sie erstellen einen Agent, dessen Ziel es ist, mit einem Tool das aktuelle Wetter für einen bestimmten Ort zu ermitteln.

Für diesen Wetter-Agent wird der `State` zur Veranschaulichung den laufenden Unterhaltungsverlauf (als Liste von Nachrichten) und einen Zähler (als Ganzzahl) für die Anzahl der ausgeführten Schritte beibehalten.

LangGraph bietet die Hilfsfunktion `add_messages` zum Aktualisieren von Listen mit Statusmeldungen. Sie fungiert als [Reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers), der die aktuelle Liste und die neuen Nachrichten entgegennimmt und eine kombinierte Liste zurückgibt. Es verarbeitet Aktualisierungen anhand der Nachrichten-ID und verwendet standardmäßig das Verhalten „Nur anhängen“ für neue, noch nicht gesehene Nachrichten.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

Als Nächstes definieren Sie Ihr Wettertool.

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

Initialisieren Sie nun das Modell und binden Sie die Tools an das Modell.

```
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-3.6-flash",
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

Der letzte Schritt, bevor Sie Ihren Agent ausführen können, besteht darin, die Knoten und Kanten zu definieren.
In diesem Beispiel gibt es zwei Knoten und eine Kante.

- `call_tool`-Knoten, der die Tool-Methode ausführt. LangGraph hat einen vordefinierten Knoten dafür namens [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
- `call_model`-Knoten, der das Modell mit dem `model_with_tools` aufruft.
- `should_continue`-Kante, die entscheidet, ob das Tool oder das Modell aufgerufen wird.

Die Anzahl der Knoten und Kanten ist nicht festgelegt. Sie können Ihrem Diagramm beliebig viele Knoten und Kanten hinzufügen. Sie können beispielsweise einen Knoten zum Hinzufügen strukturierter Ausgaben oder einen Knoten zur Selbstüberprüfung/Reflexion hinzufügen, um die Modellausgabe zu prüfen, bevor Sie das Tool oder das Modell aufrufen.

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

Nachdem alle Agent-Komponenten fertig sind, können Sie sie jetzt zusammenfügen.

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

Mit der Methode `draw_mermaid_png` können Sie den Graphen visualisieren.

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png?hl=de)

Führen Sie den Agent jetzt aus.

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Sie können die Unterhaltung jetzt fortsetzen, nach dem Wetter in einer anderen Stadt fragen oder einen Vergleich anfordern.

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
