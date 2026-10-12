---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=ar
fetched_at: 2026-10-12T07:10:14.424743+00:00
title: "\u062a\u062d\u0644\u064a\u0644 \u062f\u0639\u0645 \u0627\u0644\u0639\u0645\u0644\u0627\u0621 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini \u0648CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تحليل دعم العملاء باستخدام Gemini وCrewAI

‫[CrewAI](https://docs.crewai.com/introduction) هو إطار عمل لتنظيم
وكلاء الذكاء الاصطناعي المستقلين الذين يتعاونون لتحقيق أهداف معقّدة. يتيح لك
تحديد الوكلاء من خلال تحديد الأدوار والأهداف والقصص الخلفية، ثم تحديد المهام
لهم.

يوضّح هذا المثال كيفية إنشاء نظام متعدّد الوكلاء لتحليل بيانات دعم العملاء بهدف تحديد المشاكل واقتراح تحسينات على العمليات باستخدام Gemini 3 Flash، ما يؤدي إلى إنشاء تقرير مخصّص ليقرأه رئيس العمليات (COO).

سيوضّح لك الدليل كيفية إنشاء "طاقم عمل" من وكلاء الذكاء الاصطناعي الذين يمكنهم تنفيذ المهام التالية:

1. جلب بيانات دعم العملاء وتحليلها (محاكاة في هذا المثال)
2. تحديد المشاكل المتكرّرة والاختناقات في العمليات
3. اقتراح تحسينات قابلة للتنفيذ
4. تجميع النتائج في تقرير موجز مناسب لرئيس العمليات

تحتاج إلى مفتاح Gemini API. إذا لم يكن لديك مفتاح، يمكنك [الحصول عليه في
Google AI Studio](https://aistudio.google.com/apikey?hl=ar).

```
pip install "crewai[tools]"
```

عليك ضبط مفتاح Gemini API كمتغيّر بيئة باسم `GEMINI_API_KEY`، ثم ضبط CrewAI لاستخدام نموذج Gemini.

```
import os
from crewai import LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model='gemini/gemini-3.6-flash',
    api_key=gemini_api_key,
    temperature=1.0  # Use the Gemini 3 recommended temperature
)
```

## تحديد المكوّنات

يمكنك إنشاء تطبيقات CrewAI باستخدام **الأدوات** و**الوكلاء** و**المهام** و
**طاقم العمل** نفسه. توضّح الأقسام التالية كل مكوّن من هذه المكوّنات.

### الأدوات

الأدوات هي إمكانات يمكن للوكلاء استخدامها للتفاعل مع العالم الخارجي أو تنفيذ إجراءات معيّنة. هنا، يمكنك تحديد أداة عنصر نائب لمحاكاة جلب بيانات دعم العملاء. في تطبيق حقيقي، يمكنك الاتصال بقاعدة بيانات أو واجهة برمجة تطبيقات أو نظام ملفات. لمزيد من المعلومات عن الأدوات، يُرجى الاطّلاع على دليل أدوات [CrewAI](https://docs.crewai.com/concepts/tools).

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

### الوكلاء

الوكلاء هم العاملون الفرديون في مجال الذكاء الاصطناعي في طاقم عملك. لكل وكيل
معيّن`role` و`goal` و`backstory` و`llm` معيّن و`tools` اختيارية. لمزيد من
المعلومات عن الوكلاء، يُرجى الاطّلاع على دليل[وكلاء CrewAI](https://docs.crewai.com/concepts/agents).

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

### مهام Google

تحدّد المهام التعيينات المحدّدة للوكلاء. لكل مهمة
`description` و`expected_output` ويتم تعيينها إلى `agent`. يتم تنفيذ المهام بالتسلسل تلقائيًا وتتضمّن سياق المهمة السابقة. لمزيد من
المعلومات عن المهام، يُرجى الاطّلاع على دليل مهام [CrewAI
guide](https://docs.crewai.com/concepts/tasks).

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

### طاقم العمل

يجمع `Crew` بين الوكلاء والمهام، ويحدّد سير عمل العملية
(مثل "متسلسل").

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## تشغيل طاقم العمل

أخيرًا، يمكنك بدء تنفيذ طاقم العمل باستخدام أي مدخلات ضرورية.

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

سيتم الآن تنفيذ النص البرمجي. سيستخدم `Data Analyst` الأداة، وسيحلّل `Process
Optimizer` النتائج، وسيجمع `Report Writer`
التقرير النهائي، الذي تتم طباعته بعد ذلك في وحدة التحكّم. سيؤدي الإعداد `verbose=True` إلى عرض عملية التفكير والإجراءات التفصيلية لكل وكيل.

لمزيد من المعلومات عن CrewAI، يُرجى الاطّلاع على [مقدّمة عن CrewAI](https://docs.crewai.com/introduction).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
