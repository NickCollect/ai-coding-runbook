---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=he
fetched_at: 2026-05-05T20:50:08.483279+00:00
title: "\u05e0\u05d9\u05ea\u05d5\u05d7 \u05e9\u05dc \u05ea\u05de\u05d9\u05db\u05ea \u05dc\u05e7\u05d5\u05d7\u05d5\u05ea \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Gemini \u05d5-CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ניתוח של תמיכת לקוחות באמצעות Gemini ו-CrewAI

‫[CrewAI](https://docs.crewai.com/introduction) הוא פריימוורק לניהול סוכני AI אוטונומיים שמשתפים פעולה כדי להשיג יעדים מורכבים. הוא מאפשר להגדיר סוכנים על ידי ציון תפקידים, יעדים וסיפורי רקע, ולאחר מכן להגדיר להם משימות.

בדוגמה הזו נסביר איך לבנות מערכת מרובת סוכנים לניתוח נתונים של תמיכת לקוחות כדי לזהות בעיות ולהציע שיפורים בתהליכים באמצעות Gemini 3 Flash. המערכת יוצרת דוח שמיועד לקריאה על ידי מנהל תפעול ראשי (COO).

במדריך הזה נסביר איך ליצור 'צוות' של סוכני AI שיכולים לבצע את המשימות הבאות:

1. אחזור וניתוח של נתוני תמיכת לקוחות (סימולציה בדוגמה הזו).
2. זיהוי בעיות חוזרות וצווארי בקבוק בתהליך.
3. להציע שיפורים פרקטיים.
4. לרכז את הממצאים בדוח תמציתי שמתאים למנהל תפעול ראשי.

אתם צריכים מפתח Gemini API. אם עדיין אין לכם חשבון, אתם יכולים [ליצור חשבון ב-Google AI Studio](https://aistudio.google.com/app/apikey?hl=he).

```
pip install "crewai[tools]"
```

מגדירים את מפתח Gemini API כמשתנה סביבה בשם `GEMINI_API_KEY`, ואז מגדירים את CrewAI כך שישתמש במודל Gemini.

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

## הגדרת רכיבים

פיתוח אפליקציות CrewAI באמצעות **Tools**,‏ **Agents**,‏ **Tasks** ו-**Crew**. בקטעים הבאים מוסבר על כל אחד מהרכיבים האלה.

### כלים

כלים הם יכולות שסוכנים יכולים להשתמש בהן כדי ליצור אינטראקציה עם העולם החיצוני או לבצע פעולות ספציפיות. כאן מגדירים כלי placeholder כדי לדמות אחזור של נתוני תמיכת לקוחות. באפליקציה אמיתית, מתחברים למסד נתונים, ל-API או למערכת קבצים. מידע נוסף על כלים זמין [במדריך הכלים של CrewAI](https://docs.crewai.com/concepts/tools).

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

### סוכנים

סוכנים הם עובדי ה-AI האישיים בצוות. לכל סוכן יש `role`,‏ `goal`,‏ `backstory` ספציפיים, `llm` מוקצה ו`tools` אופציונלי. מידע נוסף על סוכנים זמין [במדריך לסוכני CrewAI](https://docs.crewai.com/concepts/agents).

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

### Tasks

המשימות מגדירות את המטלות הספציפיות של הסוכנים. לכל משימה יש `description`, ‏ `expected_output`, והיא מוקצית ל`agent`. כברירת מחדל, המשימות מופעלות ברצף וכוללות את ההקשר של המשימה הקודמת. מידע נוסף על משימות זמין ב[מדריך למשימות ב-CrewAI](https://docs.crewai.com/concepts/tasks).

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

### צוות ההפקה

`Crew` מאחד בין הסוכנים והמשימות, ומגדיר את תהליך העבודה (למשל, 'רציף').

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## הרצת הצוות

לבסוף, מפעילים את צוות הביצוע עם כל נתוני הקלט הנדרשים.

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

הסקריפט יופעל. ‫`Data Analyst` ישתמש בכלי, `Process
Optimizer` ינתח את הממצאים ו-`Report Writer` ירכז את הדוח הסופי, שיוצג במסוף. ההגדרה `verbose=True` תציג את תהליך החשיבה המפורט ואת הפעולות של כל סוכן.

מידע נוסף על CrewAI זמין ב[מבוא ל-CrewAI](https://docs.crewai.com/introduction).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
