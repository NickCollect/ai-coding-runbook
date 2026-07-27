---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=ko
fetched_at: 2026-07-27T04:44:26.273235+00:00
title: "Gemini \ubc0f LlamaIndex\ub97c \uc0ac\uc6a9\ud55c \uc5f0\uad6c \uc5d0\uc774\uc804\ud2b8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini 및 LlamaIndex를 사용한 연구 에이전트

LlamaIndex는 데이터에 연결된 LLM을 사용하여 지식 에이전트를 빌드하는 프레임워크입니다. 이 예시에서는 리서치 에이전트를 위한 멀티 에이전트 워크플로를 빌드하는 방법을 보여줍니다. LlamaIndex에서 [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
는 에이전트 및 멀티 에이전트 시스템의 구성요소입니다.

Gemini API 키가 필요합니다. 아직 키가 없다면 [Google AI Studio에서 키를 가져오세요](https://aistudio.google.com/apikey?hl=ko).
먼저 필요한 모든 LlamaIndex 라이브러리를 설치합니다. LlamaIndex는 내부적으로 `google-genai` 패키지를 사용합니다.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## LlamaIndex에서 Gemini 설정

모든 LlamaIndex 에이전트의 엔진은 추론 및 텍스트 처리를 처리하는 LLM입니다. 이 예에서는 Gemini 3 Flash를 사용합니다. [API 키를 환경 변수로 설정](https://ai.google.dev/gemini-api/docs/api-key?hl=ko)해야 합니다.

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## 빌드 도구

에이전트는 도구를 사용하여 웹 검색이나 정보 저장과 같은 외부 세계와 상호작용합니다. [LlamaIndex의 도구](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)는 일반 Python 함수일 수도 있고 기존 `ToolSpecs`에서 가져올 수도 있습니다.
Gemini에는 Google 검색을 사용하는 기본 제공 도구가 함께 제공되며, 여기서는 이 도구를 사용합니다.

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

이제 검색이 필요한 질문으로 LLM 인스턴스를 테스트합니다. 이 가이드에서는 실행 중인 이벤트 루프 (예: `python -m asyncio` 또는 Google Colab)를 가정합니다.

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

리서치 에이전트는 Python 함수를 도구로 사용합니다. 이 작업을 실행하는 시스템을 구축하는 방법은 다양합니다. 이 예시에서는 다음을 사용합니다.

1. `search_web`는 Gemini와 Google 검색을 사용하여 지정된 주제에 관한 정보를 웹에서 검색합니다.
2. `record_notes`는 다른 도구에서 사용할 수 있도록 웹에서 찾은 연구를 상태에 저장합니다.
3. `write_report`은 `ResearchAgent`에서 찾은 정보를 사용하여 보고서를 작성합니다.
4. `review_report`가 보고서를 검토하고 의견을 제공합니다.

`Context` 클래스는 에이전트/도구 간에 상태를 전달하며 각 에이전트는 시스템의 현재 상태에 액세스할 수 있습니다.

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

## 멀티 에이전트 어시스턴트 빌드

멀티 에이전트 시스템을 빌드하려면 에이전트와 에이전트의 상호작용을 정의해야 합니다.
시스템에는 다음 세 가지 에이전트가 있습니다.

1. `ResearchAgent`가 주어진 주제에 관한 정보를 웹에서 검색합니다.
2. `WriteAgent`은 `ResearchAgent`에서 찾은 정보를 사용하여 보고서를 작성합니다.
3. `ReviewAgent`가 보고서를 검토하고 의견을 제공합니다.

이 예에서는 `AgentWorkflow` 클래스를 사용하여 이러한 에이전트를 순서대로 실행하는 멀티 에이전트 시스템을 만듭니다. 각 에이전트는 해야 할 일을 알려주고 다른 에이전트와 협력하는 방법을 제안하는 `system_prompt`를 사용합니다.

원하는 경우 `can_handoff_to`를 사용하여 멀티 에이전트 시스템이 대화할 수 있는 다른 에이전트를 지정하여 멀티 에이전트 시스템을 지원할 수 있습니다. 지정하지 않으면 멀티 에이전트 시스템이 자체적으로 이를 파악하려고 시도합니다.

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

에이전트가 정의되었으므로 이제 `AgentWorkflow`을 만들고 실행할 수 있습니다.

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

워크플로를 실행하는 동안 이벤트, 도구 호출, 업데이트를 콘솔로 스트리밍할 수 있습니다.

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

워크플로가 완료되면 보고서의 최종 출력과 검토 에이전트의 최종 검토 상태를 인쇄할 수 있습니다.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## 맞춤 워크플로로 더 많은 작업 수행

`AgentWorkflow`는 멀티 에이전트 시스템을 시작하기에 좋은 방법입니다. 하지만 더 많은 제어가 필요한 경우 어떻게 해야 할까요? 처음부터 워크플로를 빌드할 수 있습니다. 자체 워크플로를 빌드해야 하는 몇 가지 이유는 다음과 같습니다.

- **프로세스에 대한 더 많은 제어**: 에이전트가 따를 정확한 경로를 결정할 수 있습니다. 여기에는 루프 생성, 특정 시점에서 결정 내리기, 에이전트가 서로 다른 작업을 병렬로 수행하도록 하는 것이 포함됩니다.
- **복잡한 데이터 사용**: 일반 텍스트를 넘어섭니다. 맞춤 워크플로를 사용하면 입력 및 출력에 JSON 객체나 맞춤 클래스와 같은 구조화된 데이터를 더 많이 사용할 수 있습니다.
- **다양한 미디어 작업**: 텍스트뿐만 아니라 이미지, 오디오, 동영상도 이해하고 처리할 수 있는 에이전트를 빌드합니다.
- **더 스마트한 계획**: 에이전트가 작업을 시작하기 전에 먼저 세부 계획을 만드는 워크플로를 설계할 수 있습니다. 이는 여러 단계가 필요한 복잡한 작업에 유용합니다.
- **자기 수정 사용 설정**: 자체 작업을 검토할 수 있는 에이전트를 만듭니다. 출력이 충분하지 않으면 에이전트가 다시 시도하여 결과가 완벽해질 때까지 개선을 반복할 수 있습니다.

LlamaIndex Workflows에 대해 자세히 알아보려면 [LlamaIndex Workflows 문서](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-10(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-10(UTC)"],[],[]]
