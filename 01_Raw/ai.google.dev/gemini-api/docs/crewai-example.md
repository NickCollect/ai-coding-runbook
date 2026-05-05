---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=th
fetched_at: 2026-05-05T20:05:42.025012+00:00
title: "\u0e01\u0e32\u0e23\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e01\u0e32\u0e23\u0e2a\u0e19\u0e31\u0e1a\u0e2a\u0e19\u0e38\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e14\u0e49\u0e27\u0e22 Gemini \u0e41\u0e25\u0e30 CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การวิเคราะห์การสนับสนุนลูกค้าด้วย Gemini และ CrewAI

[CrewAI](https://docs.crewai.com/introduction) เป็นเฟรมเวิร์กสำหรับการจัดระเบียบ
AI Agent แบบอัตโนมัติที่ทำงานร่วมกันเพื่อให้บรรลุเป้าหมายที่ซับซ้อน โดยจะช่วยให้คุณ
กำหนด Agent ได้ด้วยการระบุบทบาท เป้าหมาย และเรื่องราวเบื้องหลัง จากนั้นจึงกำหนดงาน
สำหรับ Agent เหล่านั้น

ตัวอย่างนี้แสดงวิธีสร้างระบบหลายเอเจนต์เพื่อวิเคราะห์ข้อมูลการสนับสนุนลูกค้าเพื่อระบุปัญหาและเสนอการปรับปรุงกระบวนการโดยใช้ Gemini 3 Flash ซึ่งจะสร้างรายงานที่ออกแบบมาให้ประธานเจ้าหน้าที่ฝ่ายปฏิบัติการ (COO) อ่าน

คู่มือนี้จะแสดงวิธีสร้าง "ทีม" ของ AI Agent ที่สามารถทำงานต่อไปนี้ได้

1. ดึงและวิเคราะห์ข้อมูลการสนับสนุนลูกค้า (จำลองในตัวอย่างนี้)
2. ระบุปัญหาที่เกิดซ้ำและคอขวดของกระบวนการ
3. แนะนำการปรับปรุงที่นำไปใช้ได้จริง
4. รวบรวมผลการวิจัยเป็นรายงานที่กระชับซึ่งเหมาะสำหรับ COO

คุณต้องมีคีย์ Gemini API หากยังไม่มี คุณสามารถ[รับได้ใน
Google AI Studio](https://aistudio.google.com/app/apikey?hl=th)

```
pip install "crewai[tools]"
```

ตั้งค่าคีย์ Gemini API เป็นตัวแปรสภาพแวดล้อมชื่อ `GEMINI_API_KEY` จากนั้น
กำหนดค่า CrewAI ให้ใช้โมเดล Gemini

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

## กำหนดคอมโพเนนต์

สร้างแอปพลิเคชัน CrewAI โดยใช้**เครื่องมือ** **เอเจนต์** **งาน** และ**ทีม**เอง ส่วนต่อไปนี้จะอธิบายแต่ละองค์ประกอบเหล่านี้

### เครื่องมือ

เครื่องมือคือความสามารถที่เอเจนต์ใช้โต้ตอบกับโลกภายนอกหรือ
ดำเนินการบางอย่างได้ ในที่นี้ คุณจะกำหนดเครื่องมือตัวยึดตำแหน่งเพื่อจำลอง
การดึงข้อมูลการสนับสนุนลูกค้า ในแอปพลิเคชันจริง คุณจะต้องเชื่อมต่อกับฐานข้อมูล, API หรือระบบไฟล์ ดูข้อมูลเพิ่มเติมเกี่ยวกับเครื่องมือได้ที่[คู่มือเครื่องมือ CrewAI](https://docs.crewai.com/concepts/tools)

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

### ตัวแทน

เอเจนต์คือผู้ปฏิบัติงาน AI แต่ละคนในทีมของคุณ Agent แต่ละรายจะมี `role`, `goal`, `backstory`, `llm` ที่กำหนด และ `tools` ที่ไม่บังคับ ดูข้อมูลเพิ่มเติมเกี่ยวกับตัวแทนได้ที่[คู่มือตัวแทน CrewAI](https://docs.crewai.com/concepts/agents)

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

### งาน

งานจะกำหนดการมอบหมายที่เฉพาะเจาะจงสำหรับตัวแทน แต่ละงานจะมี`description` `expected_output` และมอบหมายให้`agent` โดยค่าเริ่มต้น ระบบจะเรียกใช้งานตามลำดับและรวมบริบทของงานก่อนหน้า ดูข้อมูลเพิ่มเติมเกี่ยวกับงานได้ที่[คู่มือเกี่ยวกับงานของ CrewAI](https://docs.crewai.com/concepts/tasks)

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

### ทีมงาน

`Crew`จะเชื่อมต่อ Agent และงานเข้าด้วยกันเพื่อกำหนดกระบวนการเวิร์กโฟลว์
(เช่น "ตามลำดับ")

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

สุดท้าย ให้เริ่มการทำงานของทีมด้วยข้อมูลที่จำเป็น

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

ตอนนี้สคริปต์จะทำงาน `Data Analyst` จะใช้เครื่องมือนี้ `Process
Optimizer` จะวิเคราะห์ผลลัพธ์ และ `Report Writer` จะรวบรวม
รายงานสุดท้าย ซึ่งจะพิมพ์ลงในคอนโซล `verbose=True` การตั้งค่า
จะแสดงกระบวนการคิดและการดำเนินการโดยละเอียดของเอเจนต์แต่ละราย

ดูข้อมูลเพิ่มเติมเกี่ยวกับ CrewAI ได้ที่[ข้อมูลเบื้องต้นเกี่ยวกับ CrewAI](https://docs.crewai.com/introduction)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
