---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=ar
fetched_at: 2026-07-20T04:49:04.334711+00:00
title: "\u0648\u0643\u064a\u0644 \u0627\u0644\u0628\u062d\u062b \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini \u0648LlamaIndex \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# وكيل البحث باستخدام Gemini وLlamaIndex

‫LlamaIndex هو إطار عمل لإنشاء وكلاء معرفة باستخدام نماذج لغوية كبيرة مرتبطة ببياناتك. يوضّح لك هذا المثال كيفية إنشاء سير عمل يتضمّن عدّة وكلاء
لوكلاء البحث. في LlamaIndex، تشكّل [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
المكوّنات الأساسية للوكلاء والأنظمة المتعددة الوكلاء.

يجب أن يكون لديك مفتاح Gemini API. إذا لم يكن لديك حساب، يمكنك
[إنشاء حساب في Google AI Studio](https://aistudio.google.com/apikey?hl=ar).
أولاً، ثبِّت جميع مكتبات LlamaIndex المطلوبة. تستخدم LlamaIndex حزمة `google-genai` في الخلفية.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## إعداد Gemini في LlamaIndex

محرك أي وكيل LlamaIndex هو نموذج لغوي كبير (LLM) يتعامل مع الاستدلال ومعالجة النصوص. يستخدم هذا المثال Gemini 3 Flash. تأكَّد من [ضبط مفتاح واجهة برمجة التطبيقات كمتغيّر بيئة](https://ai.google.dev/gemini-api/docs/api-key?hl=ar).

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## أدوات الإنشاء

تستخدم البرامج الآلية الأدوات للتفاعل مع العالم الخارجي، مثل البحث على الويب أو تخزين المعلومات. يمكن أن تكون [الأدوات في LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
عبارة عن دوال Python عادية، أو يمكن استيرادها من `ToolSpecs` حالي.
يتضمّن Gemini أداة مدمجة لاستخدام "بحث Google"، وهي الأداة المستخدَمة هنا.

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3.5-flash",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

اختبِر الآن مثيل النموذج اللغوي الكبير باستخدام طلب بحث يتطلّب البحث. يفترض هذا الدليل
حلقة أحداث نشطة (مثل `python -m asyncio` أو Google Colab).

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

سيستخدم "وكيل البحث" دوال Python كأدوات. هناك العديد من الطرق التي يمكنك اتّباعها لإنشاء نظام ينفّذ هذه المهمة. في هذا المثال، ستستخدم ما يلي:

1. تستخدم `search_web` Gemini مع "بحث Google" للبحث على الويب عن معلومات حول الموضوع المحدّد.
2. تحفظ `record_notes` الأبحاث التي تم العثور عليها على الويب في الحالة حتى تتمكّن الأدوات الأخرى من استخدامها.
3. تكتب `write_report` التقرير باستخدام المعلومات التي عثر عليها `ResearchAgent`
4. `review_report` يراجع التقرير ويقدّم ملاحظات.

تمرِّر فئة `Context` الحالة بين الوكلاء/الأدوات، وسيتمكّن كل وكيل من الوصول إلى الحالة الحالية للنظام.

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

## إنشاء مساعد متعدد الوكلاء

لإنشاء نظام متعدد الوكلاء، عليك تحديد الوكلاء وتفاعلاتهم.
سيتضمّن نظامك ثلاثة وكلاء:

1. تجري أداة `ResearchAgent` عمليات بحث على الويب للعثور على معلومات حول الموضوع المحدّد.
2. يكتب `WriteAgent` التقرير باستخدام المعلومات التي يعثر عليها `ResearchAgent`.
3. `ReviewAgent` يراجع التقرير ويقدّم ملاحظات.

يستخدم هذا المثال الفئة `AgentWorkflow` لإنشاء نظام متعدد الوكلاء سيتم تنفيذه بالترتيب. يتلقّى كل وكيل `system_prompt` يخبره بما يجب أن يفعله، ويقترح عليه كيفية العمل مع الوكلاء الآخرين.

يمكنك اختياريًا مساعدة نظامك المتعدد الوكلاء من خلال تحديد الوكلاء الآخرين الذين يمكنه التحدث إليهم باستخدام `can_handoff_to` (إذا لم تفعل ذلك، سيحاول النظام تحديد ذلك بنفسه).

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

تم تحديد الوكلاء، ويمكنك الآن إنشاء `AgentWorkflow` وتشغيله.

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

أثناء تنفيذ سير العمل، يمكنك بث الأحداث واستدعاءات الأدوات والتحديثات إلى وحدة التحكّم.

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

بعد اكتمال سير العمل، يمكنك طباعة الناتج النهائي للتقرير، بالإضافة إلى حالة المراجعة النهائية من وكيل المراجعة.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## الاستفادة من ميزات إضافية مع مهام سير العمل المخصّصة

تُعدّ `AgentWorkflow` طريقة رائعة للبدء باستخدام الأنظمة المتعدّدة الوكلاء. ولكن ماذا لو كنت بحاجة إلى المزيد من التحكّم؟ يمكنك إنشاء سير عمل من البداية. في ما يلي بعض الأسباب التي قد تدفعك إلى إنشاء سير عمل خاص بك:

- **التحكّم بشكل أكبر في العملية**: يمكنك تحديد المسار الدقيق الذي تتّبعه برامجك. ويشمل ذلك إنشاء حلقات أو اتّخاذ قرارات في نقاط معيّنة أو جعل الوكلاء يعملون بالتوازي على مهام مختلفة.
- **استخدام بيانات معقّدة**: يمكنك استخدام بيانات أكثر من النص العادي. تتيح لك سير العمل المخصّصة استخدام المزيد من البيانات المنظَّمة، مثل عناصر JSON أو الفئات المخصّصة، للإدخالات والمخرجات.
- **التعامل مع وسائط مختلفة**: يمكنك إنشاء وكلاء يمكنهم فهم النصوص والصور والمحتوى الصوتي والفيديوهات ومعالجتها.
- **تخطيط أكثر ذكاءً**: يمكنك تصميم سير عمل ينشئ أولاً خطة تفصيلية قبل أن يبدأ الموظفون العمل. ويفيد هذا في المهام المعقّدة التي تتطلّب عدّة خطوات.
- **تفعيل ميزة "التصحيح الذاتي"**: يمكنك إنشاء وكلاء يمكنهم مراجعة عملهم. إذا لم تكن النتيجة جيدة بما فيه الكفاية، يمكن للوكيل المحاولة مرة أخرى، ما يؤدي إلى إنشاء حلقة من التحسينات إلى أن تصبح النتيجة مثالية.

لمزيد من المعلومات حول LlamaIndex Workflows، اطّلِع على [مستندات LlamaIndex Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-10 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-10 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
