---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=de
fetched_at: 2026-05-25T05:17:41.508073+00:00
title: "Recherchergebnisse mit Gemini und LlamaIndex abrufen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Recherchergebnisse mit Gemini und LlamaIndex abrufen

LlamaIndex ist ein Framework zum Erstellen von Wissensagenten mit LLMs, die mit Ihren Daten verbunden sind. In diesem Beispiel erfahren Sie, wie Sie einen Multi-Agenten-Workflow für einen Research Agent erstellen. In LlamaIndex sind [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
die Bausteine von Agenten- und Multi-Agenten-Systemen.

Sie benötigen einen Gemini API-Schlüssel. Wenn Sie noch keinen haben, können Sie
[einen in Google AI Studio erstellen](https://aistudio.google.com/app/apikey?hl=de).
Installieren Sie zuerst alle erforderlichen LlamaIndex-Bibliotheken. LlamaIndex verwendet im Hintergrund das Paket `google-genai`.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## Gemini in LlamaIndex einrichten

Die Engine eines jeden LlamaIndex-Agenten ist ein LLM, das für die Schlussfolgerung und Textverarbeitung zuständig ist. In diesem Beispiel wird Gemini 3 Flash verwendet. [Achten Sie darauf, dass Sie Ihren API-Schlüssel als Umgebungsvariable festlegen.](https://ai.google.dev/gemini-api/docs/api-key?hl=de)

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## Build-Tools

Agenten verwenden Tools, um mit der Außenwelt zu interagieren, z. B. um im Web zu suchen oder Informationen zu speichern. [Tools in LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
können reguläre Python-Funktionen sein oder aus vorhandenen `ToolSpecs` importiert werden.
Gemini enthält ein integriertes Tool für die Verwendung der Google Suche, das hier verwendet wird.

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

Testen Sie nun die LLM-Instanz mit einer Abfrage, für die eine Suche erforderlich ist. In dieser Anleitung wird davon ausgegangen, dass eine Ereignisschleife ausgeführt wird (z. B. `python -m asyncio` oder Google Colab).

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

Der Research Agent verwendet Python-Funktionen als Tools. Es gibt viele Möglichkeiten, ein System zu erstellen, um diese Aufgabe auszuführen. In diesem Beispiel verwenden Sie Folgendes:

1. `search_web` verwendet Gemini mit der Google Suche, um im Web nach Informationen zum angegebenen Thema zu suchen.
2. `record_notes` speichert die im Web gefundenen Informationen im Status, damit sie von den anderen Tools verwendet werden können.
3. `write_report` schreibt den Bericht mit den Informationen, die vom `ResearchAgent` gefunden wurden.
4. `review_report` überprüft den Bericht und gibt Feedback.

Die Klasse `Context` übergibt den Status zwischen Agenten/Tools und jeder Agent hat Zugriff auf den aktuellen Status des Systems.

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

## Multi-Agenten-Assistent erstellen

Um ein Multi-Agenten-System zu erstellen, definieren Sie die Agenten und ihre Interaktionen.
Ihr System besteht aus drei Agenten:

1. Ein `ResearchAgent` sucht im Web nach Informationen zum angegebenen Thema.
2. Ein `WriteAgent` schreibt den Bericht mit den Informationen, die vom `ResearchAgent` gefunden wurden.
3. Ein `ReviewAgent` überprüft den Bericht und gibt Feedback.

In diesem Beispiel wird die Klasse `AgentWorkflow` verwendet, um ein Multi-Agenten-System zu erstellen, das diese Agenten in der richtigen Reihenfolge ausführt. Jeder Agent verwendet einen `system_prompt`, der ihm mitteilt, was er tun soll, und Vorschläge zur Zusammenarbeit mit den anderen Agenten enthält.

Optional können Sie Ihr Multi-Agenten-System unterstützen, indem Sie mit `can_handoff_to` angeben, mit welchen anderen Agenten es kommunizieren kann. Andernfalls versucht es, dies selbst herauszufinden.

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

Die Agenten sind definiert. Jetzt können Sie den `AgentWorkflow` erstellen und ausführen.

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

Während der Ausführung des Workflows können Sie Ereignisse, Tool-Aufrufe und Aktualisierungen an die Konsole streamen.

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

Nach Abschluss des Workflows können Sie die endgültige Ausgabe des Berichts sowie den endgültigen Überprüfungsstatus des Überprüfungsagenten ausgeben.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## Benutzerdefinierte Workflows

Der `AgentWorkflow` ist eine gute Möglichkeit, mit Multi-Agenten-Systemen zu beginnen. Was aber, wenn Sie mehr Kontrolle benötigen? Sie können einen Workflow von Grund auf neu erstellen. Hier sind einige Gründe, warum Sie einen eigenen Workflow erstellen sollten:

- **Mehr Kontrolle über den Prozess**: Sie können den genauen Pfad festlegen, den Ihre Agenten
  nehmen. Dazu gehört das Erstellen von Schleifen, das Treffen von Entscheidungen an bestimmten Punkten oder das parallele Arbeiten von Agenten an verschiedenen Aufgaben.
- **Komplexe Daten verwenden**: Gehen Sie über einfachen Text hinaus. Mit benutzerdefinierten Workflows können Sie für Ihre Eingaben und Ausgaben strukturiertere Daten wie JSON-Objekte oder benutzerdefinierte Klassen verwenden.
- **Mit verschiedenen Medien arbeiten**: Erstellen Sie Agenten, die
  nicht nur Text, sondern auch Bilder, Audio und Video verstehen und verarbeiten können.
- **Intelligenter planen**: Sie können einen Workflow entwerfen, der zuerst einen
  detaillierten Plan erstellt, bevor die Agenten mit der Arbeit beginnen. Dies ist nützlich für komplexe Aufgaben, die mehrere Schritte erfordern.
- **Selbstkorrektur aktivieren**: Erstellen Sie Agenten, die ihre eigene Arbeit überprüfen können. Wenn die Ausgabe nicht gut genug ist, kann der Agent es noch einmal versuchen und so eine Schleife zur Verbesserung erstellen, bis das Ergebnis perfekt ist.

Weitere Informationen zu LlamaIndex-Workflows finden Sie in der [LlamaIndex-Workflows
Dokumentation](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-19 (UTC)."],[],[]]
