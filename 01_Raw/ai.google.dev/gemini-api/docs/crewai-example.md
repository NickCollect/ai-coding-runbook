---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=pl
fetched_at: 2026-05-05T13:26:34.213212+00:00
title: "Analiza obs\u0142ugi klienta za pomoc\u0105 Gemini i CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

- [Strona główna](https://ai.google.dev/gemini-api/docs/Strona główna)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/Dokumenty)

Prześlij opinię

# Analiza obsługi klienta za pomocą Gemini i CrewAI

[CrewAI](https://ai.google.dev/gemini-api/docs/CrewAI) to platforma do koordynowania autonomicznych agentów AI, którzy współpracują ze sobą, aby osiągać złożone cele. Umożliwia ona definiowanie agentów przez określanie ról, celów i historii, a następnie definiowanie dla nich zadań.

Ten przykład pokazuje, jak utworzyć system wielu agentów do analizowania danych obsługi klienta w celu identyfikowania problemów i proponowania ulepszeń procesów przy użyciu Gemini 3 Flash. System generuje raport przeznaczony dla dyrektora operacyjnego.

Z tego przewodnika dowiesz się, jak utworzyć „zespół” agentów AI, którzy mogą wykonywać te zadania:

1. Pobieranie i analizowanie danych obsługi klienta (symulowane w tym przykładzie).
2. Identyfikuj powtarzające się problemy i wąskie gardła w procesie.
3. sugerować praktyczne ulepszenia,
4. Zbierz wyniki w zwięzłym raporcie odpowiednim dla dyrektora operacyjnego.

Potrzebujesz klucza interfejsu Gemini API. Jeśli jeszcze go nie masz, możesz [uzyskać go w Google AI Studio](https://ai.google.dev/gemini-api/docs/uzyskać go w Google AI Studio).

```
pip install "crewai[tools]"
```

Ustaw klucz interfejsu Gemini API jako zmienną środowiskową o nazwie `GEMINI_API_KEY`, a następnie skonfiguruj CrewAI tak, aby używał modelu Gemini.

```
import os
from crewai import LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model='gemini/gemini-3-flash-preview',
    api_key=gemini_api_key,
    temperature=1.0  # Use the Gemini 3 recommended temperature
)
```

## Definiowanie komponentów

Twórz aplikacje CrewAI za pomocą **narzędzi**, **agentów**, **zadań** i samej **ekipy**. W sekcjach poniżej znajdziesz opis każdego z tych komponentów.

### Narzędzia

Narzędzia to funkcje, których agenci mogą używać do interakcji ze światem zewnętrznym lub wykonywania określonych działań. W tym miejscu definiujesz narzędzie zastępcze, które symuluje pobieranie danych obsługi klienta. W prawdziwej aplikacji połączysz się z bazą danych, interfejsem API lub systemem plików. Więcej informacji o narzędziach znajdziesz w [przewodniku po narzędziach CrewAI](https://ai.google.dev/gemini-api/docs/przewodniku po narzędziach CrewAI).

```
from crewai.tools import BaseTool

# Placeholder tool for fetching customer support data
class CustomerSupportDataTool(BaseTool):
    name: str = "Customer Support Data Fetcher"
    description: str = (
      "Fetches recent customer support interactions, tickets, and feedback. "
      "Returns a summary string.")

    def _run(self, argument: str) -> str:
        # In a real scenario, this would query a database or API.
        # For this example, return simulated data.
        print(f"--- Fetching data for query: {argument} ---")
        return (
            """Recent Support Data Summary:
- 50 tickets related to 'login issues'. High resolution time (avg 48h).
- 30 tickets about 'billing discrepancies'. Mostly resolved within 12h.
- 20 tickets on 'feature requests'. Often closed without resolution.
- Frequent feedback mentions 'confusing user interface' for password reset.
- High volume of calls related to 'account verification process'.
- Sentiment analysis shows growing frustration with 'login issues' resolution time.
- Support agent notes indicate difficulty reproducing 'login issues'."""
        )

support_data_tool = CustomerSupportDataTool()
```

### Agenty

Agenci to poszczególne instancje robocze AI w Twoim zespole. Każdy agent ma określony `role`, `goal`, `backstory`, przypisany `llm` i opcjonalny `tools`. Więcej informacji o agentach znajdziesz w [przewodniku po agentach CrewAI](https://ai.google.dev/gemini-api/docs/przewodniku po agentach CrewAI).

```
from crewai import Agent

# Agent 1: Data analyst
data_analyst = Agent(
    role='Customer Support Data Analyst',
    goal='Analyze customer support data to identify trends, recurring issues, and key pain points.',
    backstory=(
        """You are an expert data analyst specializing in customer support operations.
        Your strength lies in identifying patterns and quantifying problems from raw support data."""
    ),
    verbose=True,
    allow_delegation=False,  # This agent focuses on its specific task
    tools=[support_data_tool],  # Assign the data fetching tool
    llm=gemini_llm  # Use the configured Gemini LLM
)

# Agent 2: Process optimizer
process_optimizer = Agent(
    role='Process Optimization Specialist',
    goal='Identify bottlenecks and inefficiencies in current support processes based on the data analysis. Propose actionable improvements.',
    backstory=(
        """You are a specialist in optimizing business processes, particularly in customer support.
        You excel at pinpointing root causes of delays and inefficiencies and suggesting concrete solutions."""
    ),
    verbose=True,
    allow_delegation=False,
    # No tools needed, this agent relies on the context provided by data_analyst.
    llm=gemini_llm
)

# Agent 3: Report writer
report_writer = Agent(
    role='Executive Report Writer',
    goal='Compile the analysis and improvement suggestions into a concise, clear, and actionable report for the COO.',
    backstory=(
        """You are a skilled writer adept at creating executive summaries and reports.
        You focus on clarity, conciseness, and highlighting the most critical information and recommendations for senior leadership."""
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)
```

### Lista zadań

Zadania określają konkretne przypisania dla agentów. Każde zadanie ma `description`, `expected_output` i jest przypisane do `agent`. Zadania są domyślnie wykonywane sekwencyjnie i uwzględniają kontekst poprzedniego zadania. Więcej informacji o zadaniach znajdziesz w [przewodniku po zadaniach CrewAI](https://ai.google.dev/gemini-api/docs/przewodniku po zadaniach CrewAI).

```
from crewai import Task

# Task 1: Analyze data
analysis_task = Task(
    description=(
        """Fetch and analyze the latest customer support interaction data (tickets, feedback, call logs)
        focusing on the last quarter. Identify the top 3-5 recurring issues, quantify their frequency
        and impact (e.g., resolution time, customer sentiment). Use the Customer Support Data Fetcher tool."""
    ),
    expected_output=(
        """A summary report detailing the key findings from the customer support data analysis, including:
- Top 3-5 recurring issues with frequency.
- Average resolution times for these issues.
- Key customer pain points mentioned in feedback.
- Any notable trends in sentiment or support agent observations."""
    ),
    agent=data_analyst  # Assign task to the data_analyst agent
)

# Task 2: Identify bottlenecks and suggest improvements
optimization_task = Task(
    description=(
        """Based on the data analysis report provided by the Data Analyst, identify the primary bottlenecks
        in the support processes contributing to the identified issues (especially the top recurring ones).
        Propose 2-3 concrete, actionable process improvements to address these bottlenecks.
        Consider potential impact and ease of implementation."""
    ),
    expected_output=(
        """A concise list identifying the main process bottlenecks (e.g., lack of documentation for agents,
        complex escalation path, UI issues) linked to the key problems.
A list of 2-3 specific, actionable recommendations for process improvement
(e.g., update agent knowledge base, simplify password reset UI, implement proactive monitoring)."""
    ),
    agent=process_optimizer  # Assign task to the process_optimizer agent
    # This task implicitly uses the output of analysis_task as context
)

# Task 3: Compile COO report
report_task = Task(
    description=(
        """Compile the findings from the Data Analyst and the recommendations from the Process Optimization Specialist
        into a single, concise executive report for the COO. The report should clearly state:
1. The most critical customer support issues identified (with brief data points).
2. The key process bottlenecks causing these issues.
3. The recommended process improvements.
Ensure the report is easy to understand, focuses on actionable insights, and is formatted professionally."""
    ),
    expected_output=(
        """A well-structured executive report (max 1 page) summarizing the critical support issues,
        underlying process bottlenecks, and clear, actionable recommendations for the COO.
        Use clear headings and bullet points."""
    ),
    agent=report_writer  # Assign task to the report_writer agent
)
```

### Ekipa

Element `Crew` łączy agenty i zadania, definiując proces przepływu pracy (np. „sekwencyjny”).

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## Uruchamianie ekipy

Na koniec uruchom wykonanie przez grupę, podając niezbędne dane wejściowe.

```
# Start the crew's work
print("--- Starting Customer Support Analysis Crew ---")
# The 'inputs' dictionary provides initial context if needed by the first task.
# In this case, the tool simulates data fetching regardless of the input.
result = support_analysis_crew.kickoff(inputs={'data_query': 'last quarter support data'})

print("--- Crew Execution Finished ---")
print("--- Final Report for COO ---")
print(result)
```

Skrypt zostanie uruchomiony. `Data Analyst` używa narzędzia, `Process
Optimizer` analizuje wyniki, a `Report Writer` kompiluje raport końcowy, który jest następnie drukowany w konsoli. Ustawienie `verbose=True` wyświetli szczegółowy proces myślowy i działania każdego agenta.

Więcej informacji o CrewAI znajdziesz we [wprowadzeniu do CrewAI](https://ai.google.dev/gemini-api/docs/wprowadzeniu do CrewAI).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://ai.google.dev/gemini-api/docs/licencją Creative Commons – uznanie autorstwa 4.0), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://ai.google.dev/gemini-api/docs/licencji Apache 2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://ai.google.dev/gemini-api/docs/zasady dotyczące witryny Google Developers). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?
