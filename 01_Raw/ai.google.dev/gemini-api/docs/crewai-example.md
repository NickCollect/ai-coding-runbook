---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=id
fetched_at: 2026-05-05T19:46:16.925175+00:00
title: "Analisis dukungan pelanggan dengan Gemini dan CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Analisis dukungan pelanggan dengan Gemini dan CrewAI

[CrewAI](https://docs.crewai.com/introduction) adalah framework untuk mengatur
agen AI otonom yang berkolaborasi untuk mencapai sasaran yang kompleks. Framework ini memungkinkan Anda
menentukan agen dengan menentukan peran, sasaran, dan latar belakang, lalu menentukan tugas
untuk agen tersebut.

Contoh ini menunjukkan cara membuat sistem multi-agen untuk menganalisis data dukungan pelanggan guna mengidentifikasi masalah dan mengusulkan peningkatan proses menggunakan Gemini 3 Flash, yang menghasilkan laporan yang ditujukan untuk dibaca oleh Chief Operating Officer (COO).

Panduan ini akan menunjukkan cara membuat "kru" agen AI yang dapat melakukan tugas berikut:

1. Mengambil dan menganalisis data dukungan pelanggan (disimulasikan dalam contoh ini).
2. Mengidentifikasi masalah berulang dan hambatan proses.
3. Menyarankan peningkatan yang dapat ditindaklanjuti.
4. Mengumpulkan temuan ke dalam laporan ringkas yang sesuai untuk COO.

Anda memerlukan kunci Gemini API. Jika belum memilikinya, Anda bisa [mendapatkannya di
Google AI Studio](https://aistudio.google.com/app/apikey?hl=id).

```
pip install "crewai[tools]"
```

Tetapkan kunci Gemini API Anda sebagai variabel lingkungan bernama `GEMINI_API_KEY`, lalu konfigurasi CrewAI untuk menggunakan model Gemini.

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

## Menentukan komponen

Buat aplikasi CrewAI menggunakan **Alat**, **Agen**, **Tugas**, dan
**Kru** itu sendiri. Bagian berikut menjelaskan setiap komponen ini.

### Alat

Alat adalah kemampuan yang dapat digunakan agen untuk berinteraksi dengan dunia luar atau melakukan tindakan tertentu. Di sini, Anda menentukan alat placeholder untuk menyimulasikan pengambilan data dukungan pelanggan. Dalam aplikasi sebenarnya, Anda akan terhubung ke database, API, atau sistem file. Untuk mengetahui informasi selengkapnya tentang alat, lihat panduan alat [CrewAI](https://docs.crewai.com/concepts/tools).

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

### Agen

Agen adalah pekerja AI individual di kru Anda. Setiap agen memiliki `role`, `goal`, `backstory`, `llm` yang ditetapkan, dan `tools` opsional. Untuk mengetahui informasi selengkapnya tentang agen, lihat [panduan agen CrewAI](https://docs.crewai.com/concepts/agents).

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

### Tugas

Tugas menentukan penugasan spesifik untuk agen. Setiap tugas memiliki `description`, `expected_output`, dan ditetapkan ke `agent`. Tugas dijalankan secara berurutan secara default dan menyertakan konteks tugas sebelumnya. Untuk mengetahui informasi selengkapnya tentang tugas, lihat [panduan tugas CrewAI](https://docs.crewai.com/concepts/tasks).

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

`Crew` menggabungkan agen dan tugas, menentukan proses alur kerja (seperti "berurutan").

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## Menjalankan kru

Terakhir, mulai eksekusi kru dengan input yang diperlukan.

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

Skrip kini akan dijalankan. `Data Analyst` akan menggunakan alat, `Process
Optimizer` akan menganalisis temuan, dan `Report Writer` akan menyusun
laporan akhir, yang kemudian dicetak ke konsol. Setelan `verbose=True` akan menampilkan proses pemikiran dan tindakan mendetail dari setiap agen.

Untuk mempelajari CrewAI lebih lanjut, lihat [CrewAI
pengantar](https://docs.crewai.com/introduction).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
