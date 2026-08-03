---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=pl
fetched_at: 2026-08-03T04:40:18.162587+00:00
title: "Agent badawczy z\u00a0Gemini i\u00a0LlamaIndex \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agent badawczy z Gemini i LlamaIndex

LlamaIndex to platforma do tworzenia agentów wiedzy przy użyciu dużych modeli językowych połączonych z Twoimi danymi. Ten przykład pokazuje, jak utworzyć przepływ pracy z wieloma agentami dla agenta badawczego. W LlamaIndex [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
są podstawowymi elementami systemów agentów i systemów wieloagentowych.

Potrzebujesz klucza interfejsu Gemini API. Jeśli jeszcze nie masz klucza, możesz go [uzyskać w Google AI Studio](https://aistudio.google.com/apikey?hl=pl).
Najpierw zainstaluj wszystkie wymagane biblioteki LlamaIndex. LlamaIndex korzysta z pakietu `google-genai`.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## Konfigurowanie Gemini w LlamaIndex

Silnikiem każdego agenta LlamaIndex jest model LLM, który zajmuje się rozumowaniem i przetwarzaniem tekstu. W tym przykładzie używamy Gemini 3 Flash. Upewnij się, że [klucz interfejsu API jest ustawiony jako zmienna środowiskowa](https://ai.google.dev/gemini-api/docs/api-key?hl=pl).

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## Narzędzia do kompilacji

Agenty korzystają z narzędzi do interakcji ze światem zewnętrznym, np. do wyszukiwania informacji w internecie lub przechowywania danych. [Narzędzia w LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
mogą być zwykłymi funkcjami Pythona lub importowane z wcześniej utworzonych `ToolSpecs`.
Gemini ma wbudowane narzędzie do korzystania z wyszukiwarki Google, które jest tutaj używane.

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

Teraz przetestuj instancję LLM za pomocą zapytania, które wymaga wyszukiwania. W tym przewodniku zakładamy, że pętla zdarzeń jest uruchomiona (np. `python -m asyncio` lub Google Colab).

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

Agent badawczy będzie używać funkcji Pythona jako narzędzi. Istnieje wiele sposobów na zbudowanie systemu, który będzie wykonywać to zadanie. W tym przykładzie użyjesz tych elementów:

1. `search_web` korzysta z Gemini z wyszukiwarką Google, aby wyszukiwać w internecie informacje na dany temat.
2. `record_notes` zapisuje wyniki wyszukiwania w internecie w stanie, aby inne narzędzia mogły z nich korzystać.
3. `write_report` tworzy raport na podstawie informacji znalezionych przez `ResearchAgent`
4. `review_report` sprawdza raport i przekazuje opinię.

Klasa `Context` przekazuje stan między agentami i narzędziami, a każdy agent ma dostęp do bieżącego stanu systemu.

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

## Tworzenie asystenta z wieloma agentami

Aby utworzyć system wieloagentowy, musisz zdefiniować agentów i ich interakcje.
System będzie miał 3 agenty:

1. `ResearchAgent` wyszukuje w internecie informacje na dany temat.
2. `WriteAgent` pisze raport na podstawie informacji znalezionych przez `ResearchAgent`.
3. `ReviewAgent` sprawdza raport i przekazuje opinię.

W tym przykładzie do utworzenia systemu z wieloma agentami, którzy będą wykonywani po kolei, użyto klasy `AgentWorkflow`. Każdy agent otrzymuje `system_prompt`, które informuje go, co ma robić, i sugeruje, jak współpracować z innymi agentami.

Opcjonalnie możesz pomóc systemowi wieloagentowemu, określając, z którymi innymi agentami może się komunikować, używając znaku `can_handoff_to` (w przeciwnym razie system spróbuje sam to ustalić).

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

Agenty zostały zdefiniowane. Teraz możesz utworzyć `AgentWorkflow` i ją uruchomić.

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

Podczas wykonywania przepływu pracy możesz przesyłać strumieniowo do konsoli zdarzenia, wywołania narzędzi i aktualizacje.

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

Po zakończeniu procesu możesz wydrukować ostateczną wersję raportu, a także ostateczny stan weryfikacji od agenta weryfikującego.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## Więcej możliwości dzięki niestandardowym przepływom pracy

`AgentWorkflow` to świetny sposób na rozpoczęcie pracy z systemami wieloagentowymi. A co, jeśli potrzebujesz większej kontroli? Możesz utworzyć proces od podstaw. Oto kilka powodów, dla których warto utworzyć własny przepływ pracy:

- **Większa kontrola nad procesem:** możesz określić dokładną ścieżkę, którą będą podążać Twoi agenci. Możesz na przykład tworzyć pętle, podejmować decyzje w określonych momentach lub zlecać agentom równoległe wykonywanie różnych zadań.
- **Używaj złożonych danych:** wyjdź poza zwykły tekst. Niestandardowe przepływy pracy umożliwiają używanie bardziej uporządkowanych danych, takich jak obiekty JSON lub klasy niestandardowe, jako danych wejściowych i wyjściowych.
- **Praca z różnymi mediami:** twórz agentów, którzy rozumieją i przetwarzają nie tylko tekst, ale też obrazy, dźwięk i wideo.
- **Inteligentniejsze planowanie:** możesz zaprojektować przepływ pracy, który najpierw tworzy szczegółowy plan, zanim agenci zaczną pracować. Jest to przydatne w przypadku złożonych zadań, które wymagają wykonania wielu czynności.
- **Włączanie autokorekty:** tworzenie agentów, którzy mogą sprawdzać własną pracę. Jeśli wynik nie jest wystarczająco dobry, agent może spróbować ponownie, tworząc pętlę ulepszeń, aż rezultat będzie idealny.

Więcej informacji o przepływach pracy LlamaIndex znajdziesz w [dokumentacji przepływów pracy LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-10 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-10 UTC."],[],[]]
