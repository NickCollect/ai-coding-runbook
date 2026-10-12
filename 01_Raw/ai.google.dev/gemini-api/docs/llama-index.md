---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=zh-TW
fetched_at: 2026-10-12T07:05:36.879101+00:00
title: "\u4f7f\u7528 Gemini \u548c LlamaIndex \u5efa\u7acb\u7814\u7a76\u4ee3\u7406\u7a0b\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini 和 LlamaIndex 建立研究代理程式

LlamaIndex 是一個框架，可使用連結至您資料的 LLM 建構知識代理。本範例說明如何為研究代理建構多代理工作流程。在 LlamaIndex 中，[`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
是代理和多代理系統的建構區塊。

您需要 Gemini API 金鑰。如果還沒有金鑰，請[在 Google AI Studio 取得](https://aistudio.google.com/apikey?hl=zh-tw)。首先，請安裝所有必要的 LlamaIndex 程式庫。LlamaIndex 在內部使用 `google-genai` 套件。

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## 在 LlamaIndex 中設定 Gemini

任何 LlamaIndex 代理的引擎都是 LLM，負責處理推論和文字。本範例使用 Gemini 3 Flash。請務必[將 API 金鑰設為環境變數](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw)。

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.6-flash")
```

## 建立工具

代理會使用工具與外界互動，例如搜尋網路或儲存資訊。[LlamaIndex 中的工具](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)可以是常見的 Python 函式，也可以從預先存在的 `ToolSpecs` 匯入。Gemini 內建 Google 搜尋工具，因此可直接使用。

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3.6-flash",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

現在，請使用需要搜尋的查詢測試 LLM 執行個體。本指南假設您已執行事件迴圈 (例如 `python -m asyncio` 或 Google Colab)。

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

研究代理會使用 Python 函式做為工具。您可以透過多種方式建構系統來執行這項工作。在本範例中，您將使用下列項目：

1. `search_web` 會使用 Gemini 和 Google 搜尋，在網路上搜尋指定主題的資訊。
2. `record_notes` 會將在網路上找到的研究內容儲存至狀態，供其他工具使用。
3. `write_report`使用 `ResearchAgent` 找到的資訊撰寫報表
4. `review_report` 審查報告並提供意見回饋。

`Context` 類別會在代理程式/工具之間傳遞狀態，且每個代理程式都能存取系統的目前狀態。

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

## 建立多代理助理

如要建構多代理系統，請定義代理及其互動。系統會有三位代理人：

1. `ResearchAgent` 會在網路上搜尋指定主題的相關資訊。
2. `WriteAgent` 會使用 `ResearchAgent` 找到的資訊撰寫報告。
3. `ReviewAgent` 會審查報告並提供意見回饋。

本例使用 `AgentWorkflow` 類別建立多代理系統，依序執行這些代理。每個代理程式都會取得 `system_prompt`，瞭解自己應執行的動作，以及如何與其他代理程式合作。

您可以選擇使用 `can_handoff_to` 指定多代理系統可與哪些其他代理程式通訊，藉此協助系統 (否則系統會自行判斷)。

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

定義代理後，您現在可以建立並執行 `AgentWorkflow`。

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

執行工作流程期間，您可以將事件、工具呼叫和更新串流至控制台。

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

工作流程完成後，您可以列印報告的最終輸出內容，以及審查代理人的最終審查狀態。

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## 使用自訂工作流程執行更多操作

`AgentWorkflow` 是開始使用多代理系統的絕佳方式。但如果需要更多控制權呢？您可以從頭開始建立工作流程。以下列舉幾個可能需要自行建構工作流程的原因：

- **更精確地控管程序**：您可以決定代理程式採取的確切路徑。包括建立迴圈、在特定時間點做出決策，或讓代理程式同時處理不同工作。
- **使用複雜資料**：不只是純文字，自訂工作流程可讓您使用更多結構化資料 (例如 JSON 物件或自訂類別) 做為輸入和輸出內容。
- **處理不同媒體**：建構可理解及處理文字、圖片、音訊和影片的代理程式。
- **更聰明的規劃**：您可以設計工作流程，讓代理程式先建立詳細計畫，再開始工作。這項功能適用於需要多個步驟的複雜工作。
- **啟用自我修正功能**：建立可自行審查工作的代理。如果輸出結果不夠好，代理程式可以再次嘗試，建立改良迴圈，直到結果完美為止。

如要進一步瞭解 LlamaIndex Workflows，請參閱 [LlamaIndex Workflows 說明文件](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-12 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-12 (世界標準時間)。"],[],[]]
