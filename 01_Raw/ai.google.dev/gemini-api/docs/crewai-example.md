---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=tr
fetched_at: 2026-05-25T05:18:52.818299+00:00
title: "Gemini ve CrewAI ile m\u00fc\u015fteri deste\u011fi analizi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini ve CrewAI ile müşteri desteği analizi

[CrewAI](https://docs.crewai.com/introduction), karmaşık hedeflere ulaşmak için işbirliği yapan bağımsız yapay zeka aracılarını düzenlemeye yönelik bir çerçevedir. Rolleri, hedefleri ve geçmişleri belirterek aracıları tanımlamanıza ve ardından bunlar için görevler tanımlamanıza olanak tanır.

Bu örnekte, Gemini 3 Flash kullanarak sorunları belirlemek ve süreç iyileştirmeleri önermek için müşteri desteği verilerini analiz etmeye yönelik çoklu aracı sistemi oluşturma ve bir Operasyon Direktörü (COO) tarafından okunması amaçlanan bir rapor oluşturma işlemi gösterilmektedir.

Bu kılavuzda, aşağıdaki görevleri yapabilen bir "ekip" yapay zeka temsilcisi oluşturma adımları açıklanmaktadır:

1. Müşteri desteği verilerini getirme ve analiz etme (bu örnekte simüle edilmiştir).
2. Tekrarlanan sorunları ve süreçlerdeki darboğazları belirleyin.
3. Uygulanabilir iyileştirmeler önerin.
4. Bulguları, COO için uygun olan kısa bir raporda derleyin.

Gemini API anahtarına ihtiyacınız vardır. Henüz bir hesabınız yoksa [Google AI Studio'da hesap oluşturabilirsiniz](https://aistudio.google.com/app/apikey?hl=tr).

```
pip install "crewai[tools]"
```

Gemini API anahtarınızı `GEMINI_API_KEY` adlı bir ortam değişkeni olarak ayarlayın, ardından CrewAI'yı Gemini modelini kullanacak şekilde yapılandırın.

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

## Bileşenleri tanımlama

**Araçlar**, **Temsilciler**, **Görevler** ve **Ekip**'i kullanarak CrewAI uygulamaları oluşturun. Aşağıdaki bölümlerde bu bileşenlerin her biri açıklanmaktadır.

### Araçlar

Araçlar, temsilcilerin dış dünyayla etkileşim kurmak veya belirli işlemleri gerçekleştirmek için kullanabileceği özelliklerdir. Burada, müşteri desteği verilerini getirme işlemini simüle etmek için bir yer tutucu araç tanımlarsınız. Gerçek bir uygulamada, veritabanına, API'ye veya dosya sistemine bağlanırsınız. Araçlar hakkında daha fazla bilgi için [CrewAI araçları rehberine](https://docs.crewai.com/concepts/tools) bakın.

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

### Temsilciler

Ajanlar, ekibinizdeki bağımsız yapay zeka çalışanlarıdır. Her aracının belirli bir `role`, `goal`, `backstory`, atanmış `llm` ve isteğe bağlı `tools` vardır. Temsilciler hakkında daha fazla bilgi için [CrewAI temsilcileri rehberine](https://docs.crewai.com/concepts/agents) bakın.

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

### Görevler

Görevler, temsilcilerin belirli atamalarını tanımlar. Her görevin bir `description`, `expected_output` ve `agent` ataması vardır. Görevler varsayılan olarak sırayla çalıştırılır ve önceki görevin bağlamını içerir. Görevler hakkında daha fazla bilgi için [CrewAI görevleri rehberine](https://docs.crewai.com/concepts/tasks) bakın.

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

### Ekip

`Crew`, iş akışı sürecini ("sıralı" gibi) tanımlayarak aracıları ve görevleri bir araya getirir.

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

Son olarak, gerekli girişleri yaparak ekibin çalışmasını başlatın.

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

Komut dosyası artık yürütülecek. `Data Analyst` aracı kullanır, `Process
Optimizer` bulguları analiz eder ve `Report Writer` nihai raporu derler. Bu rapor daha sonra konsola yazdırılır. `verbose=True` ayarı, her aracının ayrıntılı düşünce sürecini ve işlemlerini gösterir.

CrewAI hakkında daha fazla bilgi edinmek için [CrewAI'ya
giriş](https://docs.crewai.com/introduction) bölümüne göz atın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
