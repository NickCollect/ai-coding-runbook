---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=zh-TW
fetched_at: 2026-07-20T04:45:48.589977+00:00
title: "\u4f7f\u7528 Gemini \u548c CrewAI \u5206\u6790\u9867\u5ba2\u670d\u52d9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini 和 CrewAI 分析顧客服務

[CrewAI](https://docs.crewai.com/introduction) 是一個框架，可自動化調度管理自主 AI 代理，讓這些代理互相合作，達成複雜目標。您可以指定角色、目標和背景故事來定義代理，然後為這些代理定義工作。

這個範例說明如何建構多代理程式系統，分析客戶服務資料以找出問題，並使用 Gemini 3 Flash 提出流程改善建議，然後生成一份報告，供營運長 (COO) 閱讀。

本指南將說明如何建立 AI 代理「團隊」，執行下列工作：

1. 擷取及分析客戶服務資料 (本範例中為模擬資料)。
2. 找出重複發生的問題和程序瓶頸。
3. 建議可行的改善措施。
4. 將調查結果彙整成簡明扼要的報告，方便營運長閱讀。

您需要 Gemini API 金鑰。如果還沒有金鑰，可以[在 Google AI Studio 取得](https://aistudio.google.com/apikey?hl=zh-tw)。

```
pip install "crewai[tools]"
```

將 Gemini API 金鑰設為名為 `GEMINI_API_KEY` 的環境變數，然後將 CrewAI 設定為使用 Gemini 模型。

```
import os
from crewai import LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model='gemini/gemini-3.5-flash',
    api_key=gemini_api_key,
    temperature=1.0  # Use the Gemini 3 recommended temperature
)
```

## 定義元件

使用**工具**、**代理**、**工作**和 **Crew** 本身，建構 CrewAI 應用程式。以下各節將說明這些元件。

### 工具

工具是代理可用的功能，可與外部世界互動或執行特定動作。您可以在這裡定義預留位置工具，模擬擷取客戶服務資料。在實際應用程式中，您會連線至資料庫、API 或檔案系統。如要進一步瞭解工具，請參閱 [CrewAI 工具指南](https://docs.crewai.com/concepts/tools)。

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

### 代理

代理是團隊中的個別 AI 工作者，每個代理程式都有特定的 `role`、`goal`、`backstory`、指派的 `llm` 和選用的 `tools`。如要進一步瞭解代理程式，請參閱 [CrewAI 代理程式指南](https://docs.crewai.com/concepts/agents)。

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

### 工作

工作會定義代理的具體指派事項。每項工作都有 `description`、`expected_output`，並指派給 `agent`。工作預設會依序執行，並包含先前工作的脈絡資訊。如要進一步瞭解工作，請參閱 [CrewAI 工作指南](https://docs.crewai.com/concepts/tasks)。

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

### 工作人員

`Crew` 會將代理和工作整合在一起，定義工作流程程序 (例如「循序」)。

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## Run the crew

最後，使用任何必要輸入內容啟動團隊執行作業。

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

指令碼現在會執行。`Data Analyst` 會使用這項工具，`Process
Optimizer` 會分析結果，`Report Writer` 則會編譯最終報告，然後將報告列印到控制台。`verbose=True`設定會顯示每位代理程式的詳細思考過程和動作。

如要進一步瞭解 CrewAI，請參閱 [CrewAI 簡介](https://docs.crewai.com/introduction)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-10 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-10 (世界標準時間)。"],[],[]]
