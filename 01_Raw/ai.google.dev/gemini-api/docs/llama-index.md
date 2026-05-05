---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=fr
fetched_at: 2026-05-05T13:27:59.565060+00:00
title: "Agent de recherche avec Gemini et LlamaIndex \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/recherche approfondie Gemini) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

- [Accueil](https://ai.google.dev/gemini-api/docs/Accueil)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Docs](https://ai.google.dev/gemini-api/docs/Docs)

Envoyer des commentaires

# Agent de recherche avec Gemini et LlamaIndex

LlamaIndex est un framework permettant de créer des agents de connaissances à l'aide de LLM connectés à vos données. Cet exemple vous montre comment créer un workflow multi-agents pour un agent de recherche. Dans LlamaIndex, les [`Workflows`](https://ai.google.dev/gemini-api/docs/`Workflows`)
sont les éléments constitutifs des systèmes mono-agent et multi-agents.

Vous avez besoin d'une clé API Gemini. Si vous n'en avez pas encore, vous pouvez [en obtenir une dans Google AI Studio](https://ai.google.dev/gemini-api/docs/en obtenir une dans Google AI Studio).
Commencez par installer toutes les bibliothèques LlamaIndex requises. LlamaIndex utilise le package `google-genai` en arrière-plan.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## Configurer Gemini dans LlamaIndex

Le moteur de tout agent LlamaIndex est un LLM qui gère le raisonnement et le traitement du texte. Cet exemple utilise Gemini 3 Flash. Assurez-vous de [définir votre clé API en tant que variable d'environnement](https://ai.google.dev/gemini-api/docs/définir votre clé API en tant que variable d'environnement).

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3-flash-preview")
```

## Outils de compilation

Les agents utilisent des outils pour interagir avec le monde extérieur, comme effectuer des recherches sur le Web ou stocker des informations. Les [outils de LlamaIndex](https://ai.google.dev/gemini-api/docs/outils de LlamaIndex) peuvent être des fonctions Python standards ou être importés à partir de `ToolSpecs` préexistants.
Gemini est fourni avec un outil intégré pour utiliser la recherche Google, qui est utilisé ici.

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3-flash-preview",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

Testez maintenant l'instance LLM avec une requête nécessitant une recherche. Ce guide suppose qu'une boucle d'événements est en cours d'exécution (comme `python -m asyncio` ou Google Colab).

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

L'agent de recherche utilisera des fonctions Python comme outils. Il existe de nombreuses façons de créer un système pour effectuer cette tâche. Dans cet exemple, vous utiliserez les éléments suivants :

1. `search_web` utilise Gemini avec la recherche Google pour rechercher des informations sur le Web concernant le thème donné.
2. `record_notes` enregistre les recherches trouvées sur le Web dans l'état afin que les autres outils puissent les utiliser.
3. `write_report` rédige le rapport à l'aide des informations trouvées par `ResearchAgent`.
4. `review_report` examine le rapport et fournit des commentaires.

La classe `Context` transmet l'état entre les agents/outils, et chaque agent aura accès à l'état actuel du système.

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

## Créer un assistant multi-agents

Pour créer un système multi-agent, vous devez définir les agents et leurs interactions.
Votre système comportera trois agents :

1. Un `ResearchAgent` recherche des informations sur le Web concernant le sujet donné.
2. Un `WriteAgent` rédige le rapport à l'aide des informations trouvées par le `ResearchAgent`.
3. Un `ReviewAgent` examine le rapport et fournit des commentaires.

Cet exemple utilise la classe `AgentWorkflow` pour créer un système multi-agents qui exécutera ces agents dans l'ordre. Chaque agent prend un `system_prompt` qui lui indique ce qu'il doit faire et suggère comment travailler avec les autres agents.

Vous pouvez éventuellement aider votre système multi-agents en spécifiant les autres agents avec lesquels il peut communiquer à l'aide de `can_handoff_to` (sinon, il tentera de le déterminer lui-même).

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

Les agents sont définis. Vous pouvez maintenant créer le `AgentWorkflow` et l'exécuter.

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

Pendant l'exécution du workflow, vous pouvez diffuser des événements, des appels d'outils et des mises à jour vers la console.

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

Une fois le workflow terminé, vous pouvez imprimer le résultat final du rapport, ainsi que l'état final de l'examen par l'agent.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## Aller plus loin avec les workflows personnalisés

Le `AgentWorkflow` est un excellent moyen de se lancer dans les systèmes multi-agents. Mais que faire si vous avez besoin de plus de contrôle ? Vous pouvez créer un workflow de A à Z. Voici quelques raisons pour lesquelles vous pouvez créer votre propre workflow :

- **Meilleur contrôle du processus** : vous pouvez décider du chemin exact que vos agents doivent suivre. Cela inclut la création de boucles, la prise de décisions à certains moments ou le fait de faire travailler les agents en parallèle sur différentes tâches.
- **Utilisez des données complexes** : allez au-delà du texte brut. Les workflows personnalisés vous permettent d'utiliser des données plus structurées, comme des objets JSON ou des classes personnalisées, pour vos entrées et sorties.
- **Travailler avec différents types de contenus multimédias** : créez des agents capables de comprendre et de traiter non seulement du texte, mais aussi des images, du contenu audio et des vidéos.
- **Planification plus intelligente** : vous pouvez concevoir un workflow qui crée d'abord un plan détaillé avant que les agents ne commencent à travailler. Cela est utile pour les tâches complexes qui nécessitent plusieurs étapes.
- **Activer l'auto-correction** : créez des agents capables de vérifier leur propre travail. Si le résultat n'est pas satisfaisant, l'agent peut réessayer, créant ainsi une boucle d'amélioration jusqu'à ce que le résultat soit parfait.

Pour en savoir plus sur les workflows LlamaIndex, consultez la [documentation sur les workflows LlamaIndex](https://ai.google.dev/gemini-api/docs/documentation sur les workflows LlamaIndex).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0), et les échantillons de code sont régis par une licence [Apache 2.0](https://ai.google.dev/gemini-api/docs/Apache 2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://ai.google.dev/gemini-api/docs/Règles du site Google Developers). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?
