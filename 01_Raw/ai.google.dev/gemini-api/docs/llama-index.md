---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=th
fetched_at: 2026-05-18T05:15:02.434646+00:00
title: "\u0e40\u0e2d\u0e40\u0e08\u0e19\u0e15\u0e4c\u0e01\u0e32\u0e23\u0e27\u0e34\u0e08\u0e31\u0e22\u0e14\u0e49\u0e27\u0e22 Gemini \u0e41\u0e25\u0e30 LlamaIndex \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เอเจนต์การวิจัยด้วย Gemini และ LlamaIndex

LlamaIndex เป็นเฟรมเวิร์กสำหรับการสร้าง Knowledge Agent โดยใช้ LLM ที่เชื่อมต่อกับ
ข้อมูลของคุณ ตัวอย่างนี้แสดงวิธีสร้างเวิร์กโฟลว์แบบหลาย Agent สำหรับ
Research Agent ใน LlamaIndex [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
เป็นองค์ประกอบที่ใช้สร้างสรรค์ของระบบ Agent และระบบ Multi-Agent

คุณต้องมีคีย์ Gemini API หากยังไม่มี คุณสามารถ
[รับได้ใน Google AI Studio](https://aistudio.google.com/app/apikey?hl=th)
ก่อนอื่น ให้ติดตั้งไลบรารี LlamaIndex ที่จำเป็นทั้งหมด LlamaIndex ใช้แพ็กเกจ `google-genai` เป็นส่วนประกอบพื้นฐานในการทำงาน

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## ตั้งค่า Gemini ใน LlamaIndex

เครื่องมือของเอเจนต์ LlamaIndex คือ LLM ที่จัดการการให้เหตุผลและการประมวลผลข้อความ
ตัวอย่างนี้ใช้ Gemini 3 Flash ตรวจสอบว่าคุณได้[ตั้งค่าคีย์ API เป็น
ตัวแปรสภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/api-key?hl=th)แล้ว

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3-flash-preview")
```

## เครื่องมือสร้าง

เอเจนต์ใช้เครื่องมือเพื่อโต้ตอบกับโลกภายนอก เช่น การค้นหาในเว็บหรือ
การจัดเก็บข้อมูล [เครื่องมือใน LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
อาจเป็นฟังก์ชัน Python ปกติ หรือนำเข้าจาก `ToolSpecs` ที่มีอยู่แล้วก็ได้
Gemini มาพร้อมเครื่องมือในตัวสำหรับใช้ Google Search ซึ่งใช้ในที่นี้

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

ตอนนี้ให้ทดสอบอินสแตนซ์ LLM ด้วยคำค้นหาที่ต้องใช้การค้นหา คู่มือนี้ถือว่ามีลูปเหตุการณ์ที่ทำงานอยู่ (เช่น `python -m asyncio` หรือ Google Colab)

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

Research Agent จะใช้ฟังก์ชัน Python เป็นเครื่องมือ การสร้างระบบเพื่อทำงานนี้ทำได้หลายวิธี ในตัวอย่างนี้ คุณ
จะใช้ข้อมูลต่อไปนี้

1. `search_web` ใช้ Gemini กับ Google Search เพื่อค้นหาข้อมูลในเว็บเกี่ยวกับหัวข้อที่ระบุ
2. `record_notes` จะบันทึกการวิจัยที่พบในเว็บไปยังสถานะเพื่อให้เครื่องมืออื่นๆ ใช้ได้
3. `write_report` เขียนรายงานโดยใช้ข้อมูลที่ `ResearchAgent` ค้นพบ
4. `review_report` จะตรวจสอบรายงานและให้ความคิดเห็น

`Context` คลาสจะส่งต่อสถานะระหว่าง Agent/เครื่องมือ และ Agent แต่ละตัวจะมีสิทธิ์เข้าถึงสถานะปัจจุบันของระบบ

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

## สร้างผู้ช่วยแบบหลายเอเจนต์

หากต้องการสร้างระบบแบบหลาย Agent คุณต้องกำหนด Agent และการโต้ตอบของ Agent
ระบบของคุณจะมีเอเจนต์ 3 รายดังนี้

1. `ResearchAgent` จะค้นหาข้อมูลในเว็บเกี่ยวกับหัวข้อที่ระบุ
2. `WriteAgent` เขียนรายงานโดยใช้ข้อมูลที่`ResearchAgent` ค้นพบ
3. `ReviewAgent` จะตรวจสอบรายงานและให้ความคิดเห็น

ตัวอย่างนี้ใช้คลาส `AgentWorkflow` เพื่อสร้างระบบแบบหลาย Agent ที่
จะเรียกใช้ Agent เหล่านี้ตามลำดับ Agent แต่ละตัวจะมี`system_prompt`ที่บอกว่าควรทำอะไร และแนะนำวิธีทำงานร่วมกับ Agent ตัวอื่นๆ

คุณยังช่วยระบบ Multi-Agent ได้ด้วยการระบุว่าเอเจนต์อื่นๆ ที่ระบบสามารถพูดคุยด้วยคือเอเจนต์ใดโดยใช้ `can_handoff_to` (หากไม่ระบุ ระบบจะพยายามค้นหาด้วยตัวเอง)

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

ตอนนี้คุณได้กำหนด Agent แล้ว จึงสร้าง `AgentWorkflow` และดำเนินการได้

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

ในระหว่างการดำเนินการเวิร์กโฟลว์ คุณสามารถสตรีมเหตุการณ์ การเรียกใช้เครื่องมือ และการอัปเดตไปยังคอนโซลได้

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

หลังจากเวิร์กโฟลว์เสร็จสมบูรณ์แล้ว คุณจะพิมพ์เอาต์พุตสุดท้ายของรายงานได้
รวมถึงสถานะการตรวจสอบขั้นสุดท้ายจากตัวแทนตรวจสอบ

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## ทำสิ่งต่างๆ ได้มากขึ้นด้วยเวิร์กโฟลว์ที่กำหนดเอง

`AgentWorkflow` เป็นวิธีที่ยอดเยี่ยมในการเริ่มต้นใช้งานระบบแบบหลาย Agent แต่จะเกิดอะไรขึ้นหากคุณต้องการควบคุมเพิ่มเติม คุณสร้างเวิร์กโฟลว์ได้ตั้งแต่ต้น ตัวอย่างเหตุผลที่คุณอาจต้องการสร้างเวิร์กโฟลว์ของคุณเองมีดังนี้

- **ควบคุมกระบวนการได้มากขึ้น**: คุณสามารถกำหนดเส้นทางที่แน่นอนที่ Agent
  ใช้ได้ ซึ่งรวมถึงการสร้างลูป การตัดสินใจในบางจุด หรือการให้เอเจนต์ทำงานแบบขนานในงานต่างๆ
- **ใช้ข้อมูลที่ซับซ้อน**: ใช้ข้อมูลที่มากกว่าข้อความธรรมดา เวิร์กโฟลว์ที่กำหนดเองช่วยให้คุณใช้ Structured Data ที่มีโครงสร้างมากขึ้น เช่น ออบเจ็กต์ JSON หรือคลาสที่กำหนดเอง สำหรับอินพุต และเอาต์พุต
- **ทำงานกับสื่อต่างๆ**: สร้าง Agent ที่เข้าใจและประมวลผลได้
  ไม่เพียงแต่ข้อความ แต่ยังรวมถึงรูปภาพ เสียง และวิดีโอ
- **การวางแผนที่ชาญฉลาดยิ่งขึ้น**: คุณสามารถออกแบบเวิร์กโฟลว์ที่สร้าง
  แผนโดยละเอียดก่อนที่ตัวแทนจะเริ่มทำงาน ซึ่งจะเป็นประโยชน์สำหรับงานที่ซับซ้อน
  ซึ่งต้องทำหลายขั้นตอน
- **เปิดใช้การแก้ไขด้วยตนเอง**: สร้างเอเจนต์ที่ตรวจสอบงานของตนเองได้ หาก
  เอาต์พุตยังไม่ดีพอ เอเจนต์จะลองอีกครั้งได้ ซึ่งจะสร้างลูปของ
  การปรับปรุงจนกว่าผลลัพธ์จะสมบูรณ์แบบ

ดูข้อมูลเพิ่มเติมเกี่ยวกับเวิร์กโฟลว์ LlamaIndex ได้ที่[เอกสารประกอบเกี่ยวกับเวิร์กโฟลว์ LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
