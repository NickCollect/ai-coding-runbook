---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=he
fetched_at: 2026-07-06T05:08:51.362173+00:00
title: "\u05e1\u05d5\u05db\u05df \u05de\u05d7\u05e7\u05e8 \u05e2\u05dd Gemini \u05d5-LlamaIndex \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# סוכן מחקר עם Gemini ו-LlamaIndex

‫LlamaIndex הוא פריימוורק לבניית סוכני ידע באמצעות מודלים גדולים של שפה (LLM) שמחוברים לנתונים שלכם. בדוגמה הזו מוסבר איך ליצור תהליך עבודה עם כמה סוכנים עבור סוכן מחקר. ב-LlamaIndex, ‏ [`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
הם אבני הבניין של סוכנים ומערכות מרובות סוכנים.

אתם צריכים מפתח Gemini API. אם עדיין אין לכם חשבון, אתם יכולים [ליצור חשבון ב-Google AI Studio](https://aistudio.google.com/apikey?hl=he).
קודם כול, מתקינים את כל הספריות הנדרשות של LlamaIndex. ‫LlamaIndex משתמש בחבילה `google-genai` מתחת לפני השטח.

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## הגדרת Gemini ב-LlamaIndex

המנוע של כל סוכן LlamaIndex הוא LLM שמטפל בהסקת מסקנות ובעיבוד טקסט. בדוגמה הזו נשתמש ב-Gemini 3 Flash. חשוב לוודא ש[הגדרתם את מפתח ה-API כמשתנה סביבה](https://ai.google.dev/gemini-api/docs/api-key?hl=he).

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.5-flash")
```

## כלי בנייה

סוכנים משתמשים בכלים כדי ליצור אינטראקציה עם העולם החיצוני, כמו חיפוש באינטרנט או אחסון מידע. [כלים ב-LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
יכולים להיות פונקציות רגילות של Python, או מיובאים מ-`ToolSpecs` קיימים.
‫Gemini כולל כלי מובנה לשימוש בחיפוש Google, שבו נעשה שימוש כאן.

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

עכשיו בודקים את מופע ה-LLM באמצעות שאילתה שדורשת חיפוש. במדריך הזה מניחים שקיים לולאת אירועים פעילה (כמו `python -m asyncio` או Google Colab).

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

הנציג למחקר ישתמש בפונקציות של Python ככלים. יש הרבה דרכים לבנות מערכת שתבצע את המשימה הזו. בדוגמה הזו, תשתמשו בנתונים הבאים:

1. ‫`search_web` משתמש ב-Gemini עם חיפוש Google כדי לחפש באינטרנט מידע על הנושא שצוין.
2. ‫`record_notes` שומר את המחקר שנמצא באינטרנט במצב, כדי שהכלים האחרים יוכלו להשתמש בו.
3. ‫`write_report` כותב את הדוח באמצעות המידע שנמצא על ידי `ResearchAgent`
4. ‫`review_report` בודק את הדוח ומספק משוב.

המחלקות `Context` מעבירות את המצב בין סוכנים/כלים, ולכל סוכן תהיה גישה למצב הנוכחי של המערכת.

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

## יצירת עוזר עם כמה סוכנים

כדי ליצור מערכת מרובת סוכנים, צריך להגדיר את הסוכנים ואת האינטראקציות שלהם.
במערכת יהיו שלושה סוכנים:

1. ‫`ResearchAgent` מחפש באינטרנט מידע על הנושא שצוין.
2. `WriteAgent` כותב את הדוח באמצעות המידע שנמצא על ידי `ResearchAgent`.
3. `ReviewAgent` בודק את הדוח ומספק משוב.

בדוגמה הזו נעשה שימוש במחלקה `AgentWorkflow` כדי ליצור מערכת מרובת סוכנים שתפעיל את הסוכנים האלה לפי הסדר. כל סוכן מקבל `system_prompt` שמסביר לו מה הוא צריך לעשות, ומציע לו איך לעבוד עם הסוכנים האחרים.

אפשר גם לציין אילו סוכנים אחרים יכולים לתקשר עם המערכת מרובת הסוכנים באמצעות `can_handoff_to` (אם לא תציינו, המערכת תנסה להבין את זה בעצמה).

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

הגדרתם את הסוכנים, ועכשיו אתם יכולים ליצור את `AgentWorkflow` ולהפעיל אותו.

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

במהלך ההרצה של תהליך העבודה, אפשר להזרים אירועים, קריאות לכלים ועדכונים אל המסוף.

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

אחרי שהתהליך מסתיים, אפשר להדפיס את הפלט הסופי של הדוח, וגם את מצב הבדיקה הסופי של סוכן הבדיקה.

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## רוצים להשתמש בתהליכי עבודה מותאמים אישית?

‫`AgentWorkflow` היא דרך מצוינת להתחיל לעבוד עם מערכות מרובות סוכנים. אבל מה קורה אם אתם צריכים יותר שליטה? אתם יכולים לבנות תהליך עבודה מאפס. כמה סיבות ליצירת תהליך עבודה משלכם:

- **יותר שליטה בתהליך**: אתם יכולים להחליט על הנתיב המדויק של הסוכנים שלכם. לדוגמה, ליצור לולאות, לקבל החלטות בנקודות מסוימות או להגדיר סוכנים שיעבדו במקביל על משימות שונות.
- **שימוש בנתונים מורכבים**: לא להשתמש רק בטקסט פשוט. תהליכי עבודה מותאמים אישית מאפשרים לכם להשתמש בנתונים מובְנים נוספים, כמו אובייקטים מסוג JSON או מחלקות מותאמות אישית, כקלט ופלט.
- **עבודה עם מדיה מסוגים שונים**: יצירת סוכנים שיכולים להבין ולעבד לא רק טקסט, אלא גם תמונות, אודיו וסרטונים.
- **תכנון חכם יותר**: אתם יכולים לעצב תהליך עבודה שקודם יוצר תוכנית מפורטת לפני שהסוכנים מתחילים לעבוד. התכונה הזו שימושית למשימות מורכבות שדורשות כמה שלבים.
- **הפעלת תיקון עצמי**: יצירת סוכנים שיכולים לבדוק את העבודה שלהם. אם הפלט לא מספיק טוב, הסוכן יכול לנסות שוב, וליצור לולאה של שיפורים עד שהתוצאה תהיה מושלמת.

מידע נוסף על LlamaIndex Workflows זמין ב[תיעוד של LlamaIndex Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-10 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-10 (שעון UTC)."],[],[]]
