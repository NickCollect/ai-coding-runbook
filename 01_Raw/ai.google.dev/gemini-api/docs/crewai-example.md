---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=ko
fetched_at: 2026-05-11T05:04:45.352900+00:00
title: "Gemini \ubc0f CrewAI\ub97c \uc0ac\uc6a9\ud55c \uace0\uac1d \uc9c0\uc6d0 \ubd84\uc11d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini 및 CrewAI를 사용한 고객 지원 분석

[CrewAI](https://docs.crewai.com/introduction)는 복잡한 목표를 달성하기 위해 협업하는
자율 AI 에이전트를 조정하기 위한 프레임워크입니다. 역할을 지정하고, 목표를 지정하고, 배경 스토리를 지정하여 에이전트를
정의한 다음 에이전트의 작업을
정의할 수 있습니다.

이 예에서는 Gemini 3 Flash를 사용하여 고객 지원 데이터를 분석하여 문제를 식별하고 프로세스 개선사항을 제안하는 다중 에이전트 시스템을 빌드하는 방법을 보여줍니다. 이 시스템은 최고 운영 책임자 (COO)가 읽을 보고서를 생성합니다.

이 가이드에서는 다음 작업을 실행할 수 있는 AI 에이전트 '크루'를 만드는 방법을 보여줍니다.

1. 고객 지원 데이터 가져오기 및 분석 (이 예에서 시뮬레이션됨)
2. 반복되는 문제 및 프로세스 병목 현상 식별
3. 실행 가능한 개선사항 제안
4. COO에게 적합한 간결한 보고서로 발견 항목 컴파일

Gemini API 키가 필요합니다. 아직 키가 없으면 [Google AI Studio에서
키를 가져올 수 있습니다](https://aistudio.google.com/app/apikey?hl=ko).

```
pip install "crewai[tools]"
```

Gemini API 키를 `GEMINI_API_KEY`라는 환경 변수로 설정한 다음 Gemini 모델을 사용하도록 CrewAI를 구성합니다.

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

## 구성요소 정의

**도구**, **에이전트**, **태스크**, 그리고
**크루** 자체를 사용하여 CrewAI 애플리케이션을 빌드합니다. 다음 섹션에서는 이러한 각 구성요소를 설명합니다.

### 도구

도구는 에이전트가 외부 세계와 상호작용하거나 특정 작업을 실행하는 데 사용할 수 있는 기능입니다. 여기서는 고객 지원 데이터 가져오기를 시뮬레이션하기 위해 자리표시자 도구를 정의합니다. 실제 애플리케이션에서는 데이터베이스, API 또는 파일 시스템에 연결합니다. 도구에 대한 자세한 내용은 [CrewAI
도구 가이드](https://docs.crewai.com/concepts/tools)를 참고하세요.

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

### 에이전트

에이전트는 크루의 개별 AI 작업자입니다. 각 에이전트에는 특정 `role`, `goal`, `backstory`, 할당된 `llm`, 선택적 `tools`가 있습니다. 에이전트에 대한 자세한 내용은 [CrewAI 에이전트
가이드](https://docs.crewai.com/concepts/agents)를 참고하세요.

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

### 작업

작업은 에이전트의 특정 할당을 정의합니다. 각 작업에는 `description`, `expected_output`이 있으며 `agent`에 할당됩니다. 작업은 기본적으로 순차적으로 실행되며 이전 작업의 컨텍스트를 포함합니다. 작업에 대한 자세한 내용은 [CrewAI 작업
가이드](https://docs.crewai.com/concepts/tasks)를 참고하세요.

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

### 크루

`Crew`는 에이전트와 작업을 함께 가져와 워크플로 프로세스(예: '순차')를 정의합니다.

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## 크루 실행

마지막으로 필요한 입력으로 크루 실행을 시작합니다.

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

이제 스크립트가 실행됩니다. `Data Analyst`는 도구를 사용하고, `Process
Optimizer`는 발견 항목을 분석하고, `Report Writer`는
최종 보고서를 컴파일한 후 콘솔에 출력합니다. `verbose=True` 설정을 사용하면 각 에이전트의 세부적인 사고 과정과 작업이 표시됩니다.

CrewAI에 대한 자세한 내용은 [CrewAI
소개](https://docs.crewai.com/introduction)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
