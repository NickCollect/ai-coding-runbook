---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=hi
fetched_at: 2026-09-07T05:33:15.274152+00:00
title: "Gemini \u0914\u0930 CrewAI \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947, \u0917\u094d\u0930\u093e\u0939\u0915 \u0938\u0939\u093e\u092f\u0924\u093e \u0938\u0947 \u091c\u0941\u0921\u093c\u0947 \u0921\u0947\u091f\u093e \u0915\u093e \u0935\u093f\u0936\u094d\u0932\u0947\u0937\u0923 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini और CrewAI की मदद से, ग्राहक सहायता से जुड़े डेटा का विश्लेषण करना

[CrewAI](https://docs.crewai.com/introduction), अपने-आप काम करने वाले एआई एजेंट को व्यवस्थित करने के लिए एक फ़्रेमवर्क है. ये एजेंट, मुश्किल लक्ष्यों को हासिल करने के लिए साथ मिलकर काम करते हैं. इसकी मदद से, एजेंट को उनकी भूमिकाएं, लक्ष्य, और बैकस्टोरी के हिसाब से तय किया जा सकता है. इसके बाद, उनके लिए टास्क तय किए जा सकते हैं.

इस उदाहरण में, ग्राहक सहायता से जुड़े डेटा का विश्लेषण करने के लिए, कई एजेंट वाला सिस्टम बनाने का तरीका बताया गया है. इससे समस्याओं का पता लगाया जा सकता है और Gemini 3 Flash का इस्तेमाल करके, प्रोसेस को बेहतर बनाने के सुझाव दिए जा सकते हैं. साथ ही, इसमें एक ऐसी रिपोर्ट जनरेट करने का तरीका भी बताया गया है जिसे मुख्य परिचालन अधिकारी (सीओओ) पढ़ सके.

इस गाइड में, आपको एआई एजेंट की एक "क्रू" बनाने का तरीका बताया जाएगा. यह क्रू, ये काम कर सकता है:

1. ग्राहक सहायता से जुड़ा डेटा फ़ेच करना और उसका विश्लेषण करना. इस उदाहरण में, डेटा को सिम्युलेट किया गया है.
2. बार-बार होने वाली समस्याओं और प्रोसेस में आने वाली रुकावटों की पहचान करना.
3. कार्रवाई करने लायक सुझाव दो.
4. इन नतीजों को एक छोटी रिपोर्ट में शामिल करो, ताकि सीओओ को आसानी से समझ आ सके.

आपके पास Gemini API पासकोड होना चाहिए. अगर आपके पास पहले से कोई Gemini Pro 1.0 API कुंजी नहीं है, तो [Google AI Studio में जाकर इसे पाएं](https://aistudio.google.com/apikey?hl=hi).

```
pip install "crewai[tools]"
```

अपने Gemini API पासकोड को `GEMINI_API_KEY` नाम के एनवायरमेंट वैरिएबल के तौर पर सेट करें. इसके बाद, CrewAI को Gemini मॉडल का इस्तेमाल करने के लिए कॉन्फ़िगर करें.

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

## कॉम्पोनेंट तय करना

**टूल**, **एजेंट**, **टास्क**, और **क्रू** का इस्तेमाल करके, CrewAI ऐप्लिकेशन बनाएं. यहां दिए गए सेक्शन में, इन सभी कॉम्पोनेंट के बारे में बताया गया है.

### टूल

टूल, ऐसी सुविधाएं होती हैं जिनका इस्तेमाल एजेंट, बाहरी दुनिया से इंटरैक्ट करने या खास कार्रवाइयां करने के लिए कर सकते हैं. यहां, ग्राहक सहायता से जुड़ा डेटा फ़ेच करने का सिम्युलेट करने के लिए, प्लेसहोल्डर टूल तय किया जाता है. किसी असली ऐप्लिकेशन में, आपको डेटाबेस, एपीआई या फ़ाइल सिस्टम से कनेक्ट करना होगा. टूल के बारे में ज़्यादा जानकारी के लिए, [CrewAI टूल गाइड](https://docs.crewai.com/concepts/tools) देखें.

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

### एजेंट

एजेंट, आपकी क्रू में शामिल एआई वर्कर होते हैं. हर एजेंट के पास एक खास `role`, `goal`, `backstory`, असाइन किया गया `llm`, और वैकल्पिक `tools` होता है. एजेंट के बारे में ज़्यादा जानकारी के लिए, [CrewAI एजेंट गाइड](https://docs.crewai.com/concepts/agents) देखें.

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

टास्क से, एजेंट के लिए खास असाइनमेंट तय किए जाते हैं. हर टास्क में `description` और `expected_output` होता है. साथ ही, इसे `agent` को असाइन किया जाता है. टास्क डिफ़ॉल्ट रूप से क्रम से पूरे किए जाते हैं. इनमें पिछले टास्क का कॉन्टेक्स्ट शामिल होता है. टास्क के बारे में ज़्यादा जानकारी के लिए, [CrewAI टास्क गाइड](https://docs.crewai.com/concepts/tasks) देखें.

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

### क्रू

`Crew`, एजेंट और टास्क को एक साथ लाता है. साथ ही, वर्कफ़्लो प्रोसेस (जैसे कि "क्रमिक") तय करता है.

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## क्रू को मैनेज करना

आखिर में, ज़रूरी इनपुट के साथ क्रू के काम को शुरू करें.

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

अब स्क्रिप्ट चलेगी. `Data Analyst` टूल का इस्तेमाल करेगा, `Process
Optimizer` नतीजों का विश्लेषण करेगा, और `Report Writer` फ़ाइनल रिपोर्ट तैयार करेगा. इसके बाद, इसे कंसोल पर प्रिंट किया जाएगा. `verbose=True` सेटिंग से, हर एजेंट की सोच और कार्रवाइयों के बारे में पूरी जानकारी मिलेगी.

CrewAI के बारे में ज़्यादा जानने के लिए, [CrewAI का परिचय](https://docs.crewai.com/introduction) पढ़ें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-10 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-10 (UTC) को अपडेट किया गया."],[],[]]
