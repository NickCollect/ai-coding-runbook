---
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example?hl=fr
fetched_at: 2026-05-05T13:16:29.068214+00:00
title: "Cr\u00e9er un agent ReAct \u00e0 partir de z\u00e9ro avec Gemini et LangGraph \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/recherche approfondie Gemini) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

- [Accueil](https://ai.google.dev/gemini-api/docs/Accueil)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Docs](https://ai.google.dev/gemini-api/docs/Docs)

Envoyer des commentaires

# Créer un agent ReAct à partir de zéro avec Gemini et LangGraph

LangGraph est un framework permettant de créer des applications LLM avec état. Il constitue donc un bon choix pour créer des agents ReAct (Reasoning and Acting).

Les agents ReAct combinent le raisonnement LLM et l'exécution d'actions. Ils réfléchissent de manière itérative, utilisent des outils et agissent en fonction des observations pour atteindre les objectifs des utilisateurs, en adaptant dynamiquement leur approche. Présenté dans ["ReAct : Synergizing Reasoning and Acting in Language Models"](https://ai.google.dev/gemini-api/docs/"ReAct : Synergizing Reasoning and Acting in Language Models") (2023), ce modèle tente d'imiter la résolution de problèmes flexible et semblable à celle des humains plutôt que des workflows rigides.

LangGraph propose un agent ReAct prédéfini ([`create_react_agent`](https://ai.google.dev/gemini-api/docs/`create_react_agent`)), qui est idéal lorsque vous avez besoin de plus de contrôle et de personnalisation pour vos implémentations ReAct. Ce guide vous en présente une version simplifiée.

LangGraph modélise les agents sous forme de graphiques à l'aide de trois composants clés :

- `State` : structure de données partagée (généralement `TypedDict` ou `Pydantic BaseModel`) représentant l'instantané actuel de l'application.
- `Nodes` : code la logique de vos agents. Ils reçoivent l'état actuel en entrée, effectuent un calcul ou un effet secondaire, et renvoient un état mis à jour, tel que des appels LLM ou des appels d'outils.
- `Edges` : définit le prochain `Node` à exécuter en fonction du `State` actuel, ce qui permet une logique conditionnelle et des transitions fixes.

Si vous ne disposez pas encore d'une clé API, vous pouvez en obtenir une auprès de [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio).

```
pip install langgraph langchain-google-genai geopy requests
```

Définissez votre clé API dans la variable d'environnement `GEMINI_API_KEY`.

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

Pour mieux comprendre comment implémenter un agent ReAct à l'aide de LangGraph, ce guide vous présentera un exemple pratique. Vous allez créer un agent dont l'objectif est d'utiliser un outil pour trouver la météo actuelle d'un lieu spécifié.

Pour cet agent météo, `State` conservera l'historique des conversations en cours (sous forme de liste de messages) et un compteur (sous forme d'entier) pour le nombre d'étapes effectuées, à des fins d'illustration.

LangGraph fournit une fonction d'assistance, `add_messages`, pour mettre à jour les listes de messages d'état. Elle fonctionne comme un [réducteur](https://ai.google.dev/gemini-api/docs/réducteur), en prenant la liste actuelle, plus les nouveaux messages, et en renvoyant une liste combinée. Il gère les mises à jour par ID de message et adopte par défaut un comportement "d'ajout uniquement" pour les nouveaux messages non lus.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

Définissez ensuite votre outil météo.

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

Initialisez maintenant le modèle et associez-y les outils.

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

La dernière étape avant de pouvoir exécuter votre agent consiste à définir vos nœuds et vos arêtes.
Dans cet exemple, vous avez deux nœuds et un bord.

- Nœud `call_tool` qui exécute la méthode de votre outil. LangGraph dispose d'un nœud prédéfini à cet effet, appelé [ToolNode](https://ai.google.dev/gemini-api/docs/ToolNode).
- Nœud `call_model` qui utilise `model_with_tools` pour appeler le modèle.
- `should_continue` edge qui décide s'il faut appeler l'outil ou le modèle.

Le nombre de nœuds et d'arêtes n'est pas fixe. Vous pouvez ajouter autant de nœuds et d'arêtes que vous le souhaitez à votre graphique. Par exemple, vous pouvez ajouter un nœud pour ajouter une sortie structurée ou un nœud d'auto-vérification/réflexion pour vérifier la sortie du modèle avant d'appeler l'outil ou le modèle.

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

Maintenant que tous les composants de l'agent sont prêts, vous pouvez les assembler.

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

Vous pouvez visualiser votre graphique à l'aide de la méthode `draw_mermaid_png`.

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png?hl=fr)

Exécutez maintenant l'agent.

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Vous pouvez à présent poursuivre votre conversation, demander la météo dans une autre ville ou demander une comparaison.

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0), et les échantillons de code sont régis par une licence [Apache 2.0](https://ai.google.dev/gemini-api/docs/Apache 2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://ai.google.dev/gemini-api/docs/Règles du site Google Developers). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?
