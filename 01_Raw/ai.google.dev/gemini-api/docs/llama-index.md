---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=hi
fetched_at: 2026-05-11T05:04:41.779844+00:00
title: "Gemini \u0914\u0930 LlamaIndex \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0930\u093f\u0938\u0930\u094d\u091a \u090f\u091c\u0947\u0902\u091f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini और LlamaIndex की मदद से रिसर्च एजेंट

LlamaIndex, एक ऐसा फ़्रेमवर्क है जिसकी मदद से, एलएलएम का इस्तेमाल करके नॉलेज एजेंट बनाए जा सकते हैं. ये एलएलएम, आपके डेटा से कनेक्ट होते हैं. इस उदाहरण में, रिसर्च एजेंट के लिए मल्टी-एजेंट वर्कफ़्लो बनाने का तरीका बताया गया है. LlamaIndex में, [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
एजेंट और मल्टी-एजेंट सिस्टम के बिल्डिंग ब्लॉक होते हैं.

आपके पास Gemini API पासकोड होना चाहिए. अगर आपके पास पहले से कोई Gemini Pro 1.5 का ऐक्सेस नहीं है, तो [Google AI Studio में जाकर इसका ऐक्सेस पाएं](https://aistudio.google.com/app/apikey?hl=hi).
सबसे पहले, LlamaIndex की सभी ज़रूरी लाइब्रेरी इंस्टॉल करें. LlamaIndex, बैकग्राउंड में `google-genai` पैकेज का इस्तेमाल करता है.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## LlamaIndex में Gemini को सेट अप करना

LlamaIndex के किसी भी एजेंट का इंजन, एक एलएलएम होता है. यह एलएलएम, तर्क करने और टेक्स्ट को प्रोसेस करने का काम करता है. इस उदाहरण में Gemini 3 Flash का इस्तेमाल किया गया है. पक्का करें कि आपने [अपने एपीआई पासकोड को एनवायरमेंट वैरिएबल के तौर पर सेट किया हो](https://ai.google.dev/gemini-api/docs/api-key?hl=hi).

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3-flash-preview")
```

## बिल्ड टूल

एजेंट, बाहरी दुनिया से इंटरैक्ट करने के लिए टूल का इस्तेमाल करते हैं. जैसे, वेब पर खोजना या जानकारी सेव करना. [LlamaIndex में मौजूद टूल](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/), सामान्य Python फ़ंक्शन हो सकते हैं या पहले से मौजूद `ToolSpecs` से इंपोर्ट किए जा सकते हैं.
Gemini में Google Search का इस्तेमाल करने के लिए, पहले से मौजूद टूल होता है. इसका इस्तेमाल यहां किया जाता है.

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3-flash-preview",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

अब एलएलएम इंस्टेंस को ऐसी क्वेरी के साथ टेस्ट करें जिसके लिए खोज करने की ज़रूरत होती है. इस गाइड में यह माना गया है कि इवेंट लूप चल रहा है. जैसे, `python -m asyncio` या Google Colab.

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

रिसर्च एजेंट, Python फ़ंक्शन को टूल के तौर पर इस्तेमाल करेगा. इस काम को पूरा करने के लिए, सिस्टम बनाने के कई तरीके हैं. इस उदाहरण में, इनका इस्तेमाल किया जाएगा:

1. `search_web` दिए गए विषय के बारे में जानकारी खोजने के लिए, Google Search के साथ Gemini का इस्तेमाल करता है.
2. `record_notes` वेब पर मिली रिसर्च को सेव करता है, ताकि दूसरे टूल इसका इस्तेमाल कर सकें.
3. `write_report`, `ResearchAgent` से मिली जानकारी का इस्तेमाल करके रिपोर्ट लिखता है
4. `review_report` रिपोर्ट की समीक्षा करता है और सुझाव/राय देता है या शिकायत करता है.

`Context` क्लास, एजेंट/टूल के बीच स्टेट पास करती है. साथ ही, हर एजेंट के पास सिस्टम की मौजूदा स्थिति का ऐक्सेस होगा.

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

## मल्टी-एजेंट असिस्टेंट बनाना

मल्टी-एजेंट सिस्टम बनाने के लिए, एजेंट और उनके इंटरैक्शन तय किए जाते हैं.
आपके सिस्टम में तीन एजेंट होंगे:

1. `ResearchAgent` दिए गए विषय के बारे में जानकारी खोजने के लिए, वेब पर खोज करता है.
2. `WriteAgent`, `ResearchAgent` से मिली जानकारी का इस्तेमाल करके रिपोर्ट लिखता है.
3. `ReviewAgent` रिपोर्ट की समीक्षा करता है और सुझाव या राय देता है.

इस उदाहरण में, `AgentWorkflow` क्लास का इस्तेमाल करके एक मल्टी-एजेंट सिस्टम बनाया गया है. यह सिस्टम, इन एजेंट को क्रम से लागू करेगा. हर एजेंट एक `system_prompt` लेता है, जो उसे बताता है कि उसे क्या करना चाहिए. साथ ही, यह भी बताता है कि उसे अन्य एजेंट के साथ कैसे काम करना चाहिए.

आपके पास यह तय करने का विकल्प होता है कि मल्टी-एजेंट सिस्टम, `can_handoff_to` का इस्तेमाल करके किन अन्य एजेंट से बातचीत कर सकता है. अगर ऐसा नहीं किया जाता है, तो सिस्टम खुद ही इसका पता लगाने की कोशिश करेगा.

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

एजेंट तय कर लिए गए हैं. अब `AgentWorkflow` बनाया जा सकता है और उसे चलाया जा सकता है.

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

वर्कफ़्लो के लागू होने के दौरान, इवेंट, टूल कॉल, और अपडेट को कंसोल पर स्ट्रीम किया जा सकता है.

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

वर्कफ़्लो पूरा होने के बाद, रिपोर्ट का फ़ाइनल आउटपुट प्रिंट किया जा सकता है. साथ ही, समीक्षा करने वाले एजेंट से समीक्षा की फ़ाइनल स्थिति भी प्रिंट की जा सकती है.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## कस्टम वर्कफ़्लो की मदद से, ज़्यादा काम करें

मल्टी-एजेंट सिस्टम का इस्तेमाल शुरू करने के लिए, `AgentWorkflow` एक बेहतरीन तरीका है. हालांकि, अगर आपको ज़्यादा कंट्रोल की ज़रूरत हो, तो क्या करें? आपके पास नए सिरे से वर्कफ़्लो बनाने का विकल्प होता है. यहां कुछ ऐसी वजहें बताई गई हैं जिनकी वजह से, आपको अपना वर्कफ़्लो बनाने की ज़रूरत पड़ सकती है:

- **प्रक्रिया पर ज़्यादा कंट्रोल**: आपके पास यह तय करने का विकल्प होता है कि आपके एजेंट किस तरीके से काम करेंगे. इसमें लूप बनाना, कुछ पॉइंट पर फ़ैसले लेना या एजेंटों को अलग-अलग टास्क पर एक साथ काम करने के लिए कहना शामिल है.
- **जटिल डेटा का इस्तेमाल करें**: सिर्फ़ सामान्य टेक्स्ट का इस्तेमाल न करें. कस्टम वर्कफ़्लो की मदद से, इनपुट और आउटपुट के लिए ज़्यादा स्ट्रक्चर्ड डेटा इस्तेमाल किया जा सकता है. जैसे, JSON ऑब्जेक्ट या कस्टम क्लास.
- **अलग-अलग मीडिया फ़ॉर्मैट के साथ काम करना**: ऐसे एजेंट बनाएं जो न सिर्फ़ टेक्स्ट को समझ सकें और उसे प्रोसेस कर सकें, बल्कि इमेज, ऑडियो, और वीडियो को भी समझ सकें और उन्हें प्रोसेस कर सकें.
- **बेहतर प्लानिंग**: ऐसा वर्कफ़्लो डिज़ाइन किया जा सकता है जो एजेंटों के काम शुरू करने से पहले, एक विस्तृत प्लान तैयार करे. यह मुश्किल टास्क के लिए मददगार है. ऐसे टास्क में कई चरण शामिल होते हैं.
- **खुद से सुधार करने की सुविधा चालू करें**: ऐसे एजेंट बनाएं जो अपने काम की समीक्षा कर सकें. अगर आउटपुट उम्मीद के मुताबिक नहीं है, तो एजेंट फिर से कोशिश कर सकता है. इससे, नतीजे को बेहतर बनाने की प्रोसेस तब तक चलती रहती है, जब तक नतीजा सही नहीं हो जाता.

LlamaIndex Workflows के बारे में ज़्यादा जानने के लिए, [LlamaIndex Workflows का दस्तावेज़](https://docs.llamaindex.ai/en/stable/module_guides/workflow/) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया."],[],[]]
