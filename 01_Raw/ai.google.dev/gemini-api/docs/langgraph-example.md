---
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example?hl=pl
fetched_at: 2026-11-02T07:19:25.527382+00:00
title: "Tworzenie agenta ReAct od podstaw za pomoc\u0105 Gemini i\u00a0LangGraph \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Tworzenie agenta ReAct od podstaw za pomocą Gemini i LangGraph

LangGraph to platforma do tworzenia aplikacji LLM ze stanem, dzięki czemu dobrze nadaje się do tworzenia agentów ReAct (Reasoning and Acting).

Agenci ReAct łączą rozumowanie LLM z wykonywaniem działań. Iteracyjnie myślą, używają narzędzi i reagują na obserwacje, aby osiągnąć cele użytkownika, dynamicznie dostosowując swoje podejście. Ten wzorzec, wprowadzony w artykule ["ReAct: Synergizing Reasoning and Acting
in Language Models"](https://arxiv.org/abs/2210.03629) (2023),
ma na celu odzwierciedlenie elastycznego rozwiązywania problemów przez ludzi w porównaniu ze sztywnymi przepływami pracy.

LangGraph oferuje gotowego agenta ReAct ([`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)),
który sprawdza się, gdy potrzebujesz większej kontroli i możliwości dostosowania implementacji ReAct. W tym przewodniku pokażemy uproszczoną wersję.

Modele LangGraph przedstawiają agentów jako grafy, używając 3 kluczowych komponentów:

- `State`: współdzielona struktura danych (zwykle `TypedDict` lub `Pydantic BaseModel`) reprezentująca bieżący zrzut aplikacji.
- `Nodes`: koduje logikę agentów. Otrzymują bieżący stan jako dane wejściowe, wykonują pewne obliczenia lub efekty uboczne i zwracają zaktualizowany stan, np. wywołania LLM lub wywołania narzędzi.
- `Edges`: definiuje następny węzeł `Node`, który ma zostać wykonany na podstawie bieżącego stanu `State`, co umożliwia stosowanie logiki warunkowej i stałych przejść.

Jeśli nie masz jeszcze klucza interfejsu API, możesz go uzyskać w [Google AI
Studio](https://aistudio.google.com/apikey?hl=pl).

```
pip install langgraph langchain-google-genai geopy requests
```

Ustaw klucz interfejsu API w zmiennej środowiskowej `GEMINI_API_KEY`.

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

Aby lepiej zrozumieć, jak zaimplementować agenta ReAct za pomocą LangGraph, w tym przewodniku omówimy praktyczny przykład. Utworzysz agenta, którego celem jest użycie narzędzia do sprawdzenia aktualnej pogody w określonej lokalizacji.

W przypadku tego agenta pogodowego `State` będzie przechowywać historię bieżącej rozmowy (jako listę wiadomości) oraz licznik (jako liczbę całkowitą) liczby wykonanych kroków.

LangGraph udostępnia funkcję pomocniczą `add_messages` do aktualizowania list wiadomości o stanie. Działa ona jako [reduktor](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers), który przyjmuje bieżącą listę oraz nowe wiadomości i zwraca połączoną listę. Obsługuje aktualizacje według identyfikatora wiadomości i domyślnie stosuje zachowanie „tylko dołączania” w przypadku nowych, nieprzeczytanych wiadomości.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

Następnie zdefiniuj narzędzie do sprawdzania pogody.

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

Teraz zainicjuj model i powiąż z nim narzędzia.

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

Ostatnim krokiem przed uruchomieniem agenta jest zdefiniowanie węzłów i krawędzi.
W tym przykładzie masz 2 węzły i 1 krawędź.

- Węzeł `call_tool`, który wykonuje metodę narzędzia. LangGraph ma gotowy węzeł
  o nazwie
  [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
- Węzeł `call_model`, który używa `model_with_tools` do wywołania modelu.
- Krawędź `should_continue`, która decyduje, czy wywołać narzędzie, czy model.

Liczba węzłów i krawędzi nie jest stała. Do grafu możesz dodać dowolną liczbę węzłów i krawędzi. Możesz na przykład dodać węzeł do dodawania uporządkowanych danych wyjściowych lub węzeł do samodzielnej weryfikacji/refleksji, aby sprawdzić dane wyjściowe modelu przed wywołaniem narzędzia lub modelu.

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

Gdy wszystkie komponenty agenta są gotowe, możesz je połączyć.

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

Graf możesz wizualizować za pomocą metody `draw_mermaid_png`.

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png?hl=pl)

Teraz uruchom agenta.

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Możesz kontynuować rozmowę, zapytać o pogodę w innym mieście lub poprosić o porównanie.

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-12 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-12 UTC."],[],[]]
