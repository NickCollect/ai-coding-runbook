---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=ja
fetched_at: 2026-07-06T05:10:20.318431+00:00
title: "Gemini \u3068 CrewAI \u3092\u4f7f\u7528\u3057\u305f\u30ab\u30b9\u30bf\u30de\u30fc \u30b5\u30dd\u30fc\u30c8\u306e\u5206\u6790 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini と CrewAI を使用したカスタマー サポートの分析

[CrewAI](https://docs.crewai.com/introduction) は、連携して複雑な目標を達成する自律型 AI エージェントをオーケストレートするためのフレームワークです。ロール、目標、バックストーリーを指定してエージェントを定義し、タスクを定義できます。

この例では、Gemini 3 Flash を使用して、カスタマー サポート データを分析して問題を特定し、プロセス改善を提案するマルチエージェント システムを構築する方法を示します。このシステムは、最高執行責任者（COO）が読むことを想定したレポートを生成します。

このガイドでは、次のタスクを実行できる AI エージェントの「クルー」を作成する方法について説明します。

1. カスタマー サポート データを取得して分析します（この例ではシミュレートされています）。
2. 繰り返し発生する問題とプロセスのボトルネックを特定します。
3. 具体的な改善案を提案します。
4. 調査結果を COO に適した簡潔なレポートにまとめます。

Gemini API キーが必要です。キーがない場合は、[Google AI Studio で取得](https://aistudio.google.com/apikey?hl=ja)できます。

```
pip install "crewai[tools]"
```

Gemini API キーを `GEMINI_API_KEY` という名前の環境変数として設定し、Gemini モデルを使用するように CrewAI を構成します。

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

## コンポーネントを定義する

**ツール**、**エージェント**、**タスク**、**クルー**自体を使用して CrewAI アプリケーションを構築します。以降のセクションでは、これらの各コンポーネントについて説明します。

### ツール

ツールは、エージェントが外部とやり取りしたり、特定のアクションを実行したりするために使用できる機能です。ここでは、カスタマー サポート データの取得をシミュレートするプレースホルダ ツールを定義します。実際のアプリケーションでは、データベース、API、ファイル システムに接続します。ツールの詳細については、[CrewAI ツールガイド](https://docs.crewai.com/concepts/tools)をご覧ください。

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

### エージェント

エージェントは、クルー内の個々の AI ワーカーです。各エージェントには、特定の `role`、`goal`、`backstory`、割り当てられた `llm`、省略可能な `tools` があります。エージェントの詳細については、[CrewAI エージェントのガイド](https://docs.crewai.com/concepts/agents)をご覧ください。

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

### タスク

タスクは、エージェントの具体的な割り当てを定義します。各タスクには `description` と `expected_output` があり、`agent` に割り当てられます。タスクはデフォルトで順番に実行され、前のタスクのコンテキストが含まれます。タスクの詳細については、[CrewAI タスクガイド](https://docs.crewai.com/concepts/tasks)をご覧ください。

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

### Crew

`Crew` は、エージェントとタスクをまとめ、ワークフロー プロセス（「順次」など）を定義します。

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## クルーを実行する

最後に、必要な入力を使用してクルーの実行を開始します。

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

スクリプトが実行されます。`Data Analyst` はツールを使用し、`Process
Optimizer` は調査結果を分析し、`Report Writer` は最終レポートをコンパイルしてコンソールに出力します。`verbose=True` 設定では、各エージェントの詳細な思考プロセスとアクションが表示されます。

CrewAI の詳細については、[CrewAI の概要](https://docs.crewai.com/introduction)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-10 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-10 UTC。"],[],[]]
