---
source_url: https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=he
fetched_at: 2026-06-08T05:40:18.507012+00:00
title: "Gemini Deep Research Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# Gemini Deep Research Agent

סוכן Deep Research של Gemini מתכנן, מבצע ומסכם באופן אוטונומי משימות מחקר מרובות שלבים. הוא מבוסס על Gemini, ולכן הוא יכול לנווט בין מערכי מידע מורכבים כדי ליצור דוחות מפורטים עם ציטוטים. יכולות חדשות מאפשרות לכם לתכנן בשיתוף עם הסוכן, להתחבר לכלים חיצוניים באמצעות שרתי MCP, לכלול ויזואליזציות (כמו תרשימים וגרפים) ולספק מסמכים ישירות כקלט.

משימות מחקר כוללות חיפוש וקריאה חוזרים, והן יכולות להימשך כמה דקות. כדי להריץ את הסוכן באופן אסינכרוני ולבדוק אם יש תוצאות או עדכונים בסטרימינג, צריך להשתמש בהרצת רקע (הגדרה `background=true`). פרטים נוספים זמינים במאמר בנושא [טיפול במשימות ארוכות טווח](#long-running-tasks).

בדוגמה הבאה אפשר לראות איך מתחילים משימת מחקר ברקע ומבצעים סקר כדי לקבל את התוצאות.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.output_text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.output_text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## גרסאות נתמכות

סוכן Deep Research זמין בשתי גרסאות:

- ‫**Deep Research** (`deep-research-preview-04-2026`): מודל שנועד לפעול במהירות וביעילות, ומתאים במיוחד להזרמה חזרה לממשק משתמש של לקוח.
- ‫**Deep Research Max** (`deep-research-max-preview-04-2026`): מקיף ביותר לאיסוף וסינתוז אוטומטיים של הקשר.

## תכנון שיתופי

תכנון שיתופי מאפשר לכם לשלוט בכיוון המחקר לפני שהסוכן מתחיל לעבוד. כשהאפשרות הזו מופעלת, הנציג מחזיר תוכנית מחקר מוצעת במקום לבצע את המחקר באופן מיידי. לאחר מכן תוכלו לבדוק, לשנות או לאשר את התוכנית באמצעות אינטראקציות עוקבות.

### שלב 1: שליחת בקשה לתוכנית

מגדירים `collaborative_planning=True` באינטראקציה הראשונה. הסוכן
מחזיר תוכנית מחקר במקום דוח מלא.

### Python

```
from google import genai

client = genai.Client()

plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### שלב 2: שיפור התוכנית (אופציונלי)

כדי להמשיך את השיחה ולשפר את התוכנית, אפשר להשתמש ב-`previous_interaction_id`. מחזיקים את המקש `collaborative_planning=True` כדי להישאר במצב תכנון.

### Python

```
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### שלב 3: אישור וביצוע

מגדירים את הערך `collaborative_planning=False` (או משמיטים אותו) כדי לאשר את התוכנית ולהתחיל את המחקר.

### Python

```
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## הצגה חזותית

כשההגדרה `visualization` מוגדרת לערך `"auto"`, הסוכן יכול ליצור תרשימים, גרפים ורכיבים ויזואליים אחרים כדי לתמוך בממצאי המחקר שלו.
תמונות שנוצרו נכללות בשלבי התשובה ומוזרמות כדלתאות של `image`. כדי לקבל את התוצאות הטובות ביותר, כדאי לבקש באופן מפורש תמונות חזותיות בשאילתה – לדוגמה, "תכלול תרשימים שמציגים מגמות לאורך זמן" או "תייצר גרפיקה להשוואה של נתח השוק". ההגדרה `visualization` לערך `"auto"` מפעילה את היכולת, אבל הסוכן יוצר תמונות רק כשמבקשים זאת בהנחיה.

### Python

```
import base64

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## כלים נתמכים

‫Deep Research תומך בכמה כלים מובנים וחיצוניים. כברירת מחדל (כשלא מציינים פרמטר `tools`), לסוכן יש גישה לחיפוש Google, להקשר של כתובת האתר ולביצוע קוד. אתם יכולים לציין באופן מפורש כלים כדי להגביל או להרחיב את היכולות של הסוכן.

| כלי | הקלדת ערך | תיאור |
| --- | --- | --- |
| חיפוש Google | `google_search` | חיפוש באינטרנט הציבורי. מופעל כברירת מחדל. |
| ההקשר של כתובת ה-URL | `url_context` | לקרוא ולסכם את התוכן בדף אינטרנט. מופעל כברירת מחדל. |
| הרצת קוד | `code_execution` | להריץ קוד כדי לבצע חישובים וניתוח נתונים. מופעל כברירת מחדל. |
| שרת MCP | `mcp_server` | להתחבר לשרתי MCP מרוחקים כדי לגשת לכלי חיצוניים. |
| חיפוש קבצים | `file_search` | חיפוש במאגרי המסמכים שהועלו. |

### חיפוש Google

מפעילים במפורש את חיפוש Google ככלי היחיד:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### ההקשר של כתובת ה-URL

לתת לסוכן את היכולת לקרוא ולסכם דפי אינטרנט ספציפיים:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### הרצת קוד

ההרשאה לסוכן להריץ קוד לחישובים ולניתוח נתונים:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### שרתי MCP

מזינים את השרת `name` ואת `url` בהגדרות של הכלי. אפשר גם להעביר פרטי אימות ולהגביל את הכלים שהסוכן יכול להפעיל.

| שדה | סוג | נדרש | תיאור |
| --- | --- | --- | --- |
| `type` | `string` | כן | חייב להיות `"mcp_server"`. |
| `name` | `string` | לא | השם המוצג של שרת ה-MCP. |
| `url` | `string` | לא | כתובת ה-URL המלאה של נקודת הקצה של שרת ה-MCP. |
| `headers` | `object` | לא | צמדי מפתח/ערך שנשלחים ככותרות HTTP עם כל בקשה לשרת (לדוגמה, אסימוני אימות). |
| `allowed_tools` | `array` | לא | הגבלת הכלים שהסוכן יכול להשתמש בהם בשרת. |

#### שימוש בסיסי

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### חיפוש קבצים

כדי לתת לסוכן גישה לנתונים שלכם, משתמשים בכלי [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=he).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## הכוונה ועיצוב

אתם יכולים להנחות את הפלט של הסוכן על ידי מתן הוראות עיצוב ספציפיות בהנחיה. כך תוכלו לבנות דוחות עם חלקים ותתי-חלקים ספציפיים, לכלול טבלאות נתונים או להתאים את הטון לקהלים שונים (למשל, 'טכני', 'מנהלים', 'לא רשמי').

מגדירים במפורש את פורמט הפלט הרצוי בטקסט הקלט.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## קלטים מרובי מצבים

התכונה 'Deep Research' תומכת בקלט מולטי-מודאלי, כולל תמונות ומסמכים (קובצי PDF), ומאפשרת לסוכן לנתח תוכן חזותי ולבצע מחקר מבוסס-אינטרנט בהקשר של הקלט שסופק.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.output_text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.output_text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### הבנת מסמכים

להעביר מסמכים ישירות כקלט מרובה מצבים. הסוכן מנתח את המסמכים שסיפקתם ומבצע מחקר שמבוסס על התוכן שלהם.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## טיפול במשימות לטווח ארוך

‫Deep Research הוא תהליך רב-שלבי שכולל תכנון, חיפוש, קריאה וכתיבה. המחזור הזה בדרך כלל חורג ממגבלות הזמן הקצוב לתפוגה של קריאות API סינכרוניות.

הסוכנים חייבים להשתמש ב-`background=True`. ה-API מחזיר אובייקט `Interaction` חלקי באופן מיידי. אפשר להשתמש במאפיין `id` כדי לאחזר אינטראקציה לצורך בדיקה. מצב האינטראקציה ישתנה מ`in_progress` ל`completed` או ל`failed`.

### סטרימינג

התכונה Deep Research תומכת בהזרמת נתונים כדי לקבל עדכונים בזמן אמת על התקדמות המחקר, כולל סיכומי מחשבות, פלט טקסט ותמונות שנוצרו.
צריך להגדיר את `stream=True` ואת `background=True`. מדריך מקיף בנושא סטרימינג, כולל סוגי אירועים, סטרימינג של כלים ושיקולים, זמין במאמר [סטרימינג של אינטראקציות](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=he).

כדי לקבל שלבי ביניים של חשיבה רציונלית (מחשבות) ועדכוני התקדמות, צריך להפעיל **סיכומי חשיבה** על ידי הגדרת `thinking_summaries` לערך `"auto"` ב-`agent_config`. בלי זה, יכול להיות שהזרם יספק רק את התוצאות הסופיות.

#### סוגי אירועים במקור נתונים

| סוג אירוע | סוג הדלתא | תיאור |
| --- | --- | --- |
| `step.delta` | `thought` | שלב ביניים של הסוכן בתהליך החשיבה. |
| `step.delta` | `text` | חלק מפלט הטקסט הסופי. |
| `step.delta` | `image` | תמונה שנוצרה (בקידוד Base64). |

בדוגמה הבאה מתחילים משימת מחקר ומעבדים את הסטרימינג עם חיבור מחדש אוטומטי. הוא עוקב אחרי `interaction_id` ו-`last_event_id`, כך שאם החיבור ייפסק (לדוגמה, אחרי זמן קצוב לתפוגה של 600 שניות), אפשר יהיה להמשיך מהמקום שבו הוא נעצר.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## שאלות המשך ואינטראקציות

אחרי שהנציג או הנציגה ישלחו את הדוח הסופי, תוכלו להמשיך את השיחה באמצעות `previous_interaction_id`. כך תוכלו לבקש הבהרה, סיכום או פירוט של קטעים ספציפיים במחקר בלי להפעיל מחדש את כל המשימה.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## מתי כדאי להשתמש ב-Gemini Deep Research Agent

‫Deep Research הוא **סוכן**, ולא רק מודל. היא מתאימה במיוחד לעומסי עבודה שדורשים גישה של "אנליסט בקופסה" ולא צ'אט עם זמן אחזור נמוך.

| תכונה | מודלים רגילים של Gemini | Gemini Deep Research Agent |
| --- | --- | --- |
| **זמן אחזור** | שניות | דקות (אסינכרוני/ברקע) |
| **Process** | יצירה -> פלט | תכנון -> חיפוש -> קריאה -> חזרה על הפעולה -> פלט |
| **פלט** | טקסט שיחה, קוד, סיכומים קצרים | דוחות מפורטים, ניתוח ארוך, טבלאות השוואה |
| **מתאים במיוחד ל** | צ'אטבוטים, חילוץ, כתיבה יוצרת | ניתוח שוק, בדיקת נאותות, סקירת ספרות, ניתוח התחרות |

## הגדרת הסוכן

הפרמטר `agent_config` משמש לשליטה בהתנהגות של Deep Research.
מעבירים אותו כמילון עם השדות הבאים:

| שדה | סוג | ברירת מחדל | תיאור |
| --- | --- | --- | --- |
| `type` | `string` | חובה | חייב להיות `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | מגדירים את הערך `"auto"` כדי לקבל שלבי ביניים של חשיבה רציונלית במהלך השידור. כדי להשבית, מגדירים את הערך `"none"`. |
| `visualization` | `string` | `"auto"` | מגדירים את הערך `"auto"` כדי להפעיל תרשימים ותמונות שנוצרו על ידי סוכן. כדי להשבית, מגדירים את הערך `"off"`. |
| `collaborative_planning` | `boolean` | `false` | מגדירים את האפשרות `true` כדי להפעיל בדיקה של תוכנית המחקר בכמה שלבים לפני תחילת המחקר. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## זמינות ומחירים

אפשר לגשת לסוכן Deep Research של Gemini באמצעות Interactions API ב-Google AI Studio וב-Gemini API.

התמחור מבוסס על [מודל של תשלום לפי שימוש](https://ai.google.dev/gemini-api/docs/pricing?hl=he#pricing-for-agents), בהתאם למודלים הבסיסיים של Gemini ולכלים הספציפיים שבהם הסוכן משתמש. בניגוד לבקשות רגילות בצ'אט, שבהן בקשה מובילה לפלט אחד, משימת Deep Research היא תהליך עבודה של AI אקטיבי. בקשה אחת מפעילה לולאה אוטונומית של תכנון, חיפוש, קריאה והסקת מסקנות.

### עלויות משוערות

העלויות משתנות בהתאם לעומק המחקר הנדרש. הסוכן קובע באופן אוטונומי כמה קריאה וחיפוש נדרשים כדי לענות על ההנחיה.

- ‫**Deep Research** (`deep-research-preview-04-2026`): בשאילתה טיפוסית שדורשת ניתוח מתון, יכול להיות שהסוכן ישתמש בכ-80 שאילתות חיפוש, בכ-250,000 טוקנים של קלט (כ-50-70% במטמון) ובכ-60,000 טוקנים של פלט.
  - **סך הכול משוער:** כ-4 ש"ח עד 12 ש"ח לכל משימה
- ‫**Deep Research Max**‏ (`deep-research-max-preview-04-2026`): לניתוח מעמיק של הסביבה התחרותית או לבדיקת נאותות מקיפה, יכול להיות שהסוכן ישתמש בעד 160 שאילתות חיפוש, עד 900,000 טוקנים של קלט (כ-50-70% במטמון) ועד 80,000 טוקנים של פלט.
  - **סכום משוער כולל:** כ-3.00$עד 7.00$ לכל משימה

## שיקולי בטיחות

כדי לתת לסוכן גישה לאינטרנט ולקבצים הפרטיים שלכם, צריך לשקול היטב את סיכוני הבטיחות.

- **החדרת הנחיות באמצעות קבצים:** הסוכן קורא את התוכן של הקבצים שאתם מספקים. חשוב לוודא שהמסמכים שהועלו (קובצי PDF, קובצי טקסט) מגיעים ממקורות מהימנים. קובץ זדוני יכול להכיל טקסט מוסתר שנועד לתמרן את הפלט של הסוכן.
- **סיכונים שקשורים לתוכן באינטרנט:** הסוכן מחפש באינטרנט הציבורי. אנחנו מטמיעים מסנני בטיחות חזקים, אבל קיים סיכון שהסוכן ייתקל בדפי אינטרנט זדוניים ויעבד אותם. מומלץ לעיין ב`citations` שצוינו בתשובה כדי לאמת את המקורות.
- **העברת נתונים:** חשוב לנקוט משנה זהירות כשמבקשים מהסוכן לסכם נתונים פנימיים רגישים אם מאפשרים לו גם לגלוש באינטרנט.

## שיטות מומלצות

- **הנחיה לגבי נתונים לא ידועים:** הנחיה של הסוכן לגבי אופן הטיפול בנתונים חסרים.
  לדוגמה, אפשר להוסיף את ההנחיה *"אם נתונים ספציפיים לשנת 2025 לא זמינים,
  ציין במפורש שהם תחזיות או לא זמינים, במקום להעריך"*.
- **מספקים הקשר:** כדי שהמחקר של הסוכן יהיה מבוסס על מידע רלוונטי, כדאי לספק הנחיות או מידע רקע ישירות בהנחיית הקלט.
- **שימוש בתכנון שיתופי:** בשאילתות מורכבות, מומלץ להפעיל תכנון שיתופי כדי לבדוק ולשפר את תוכנית המחקר לפני הביצוע.
- ‫**Multimodal inputs:** Deep Research Agent supports multi-modal inputs.
  צריך להשתמש בזה בזהירות, כי זה מגדיל את העלויות ואת הסיכון לחריגה מחלון ההקשר.

## מגבלות

- **סטטוס בטא**: ממשק Interactions API נמצא בגרסת בטא ציבורית. יכול להיות שיהיו שינויים בתכונות ובסכימות.
- **כלים בהתאמה אישית:** נכון לעכשיו אי אפשר לספק כלים מותאמים אישית להפעלת פונקציות, אבל אפשר להשתמש בשרתי MCP (Model Context Protocol) מרוחקים עם סוכן המחקר המעמיק.
- **פלט מובנה:** כרגע, סוכן Deep Research לא תומך בפלט מובנה.
- **זמן המחקר המקסימלי:** לסוכן Deep Research יש זמן מחקר מקסימלי של 60 דקות. רוב המשימות אמורות להסתיים תוך 20 דקות.
- **דרישה לחנות:** כדי להפעיל את הנציג באמצעות `background=True`, צריך `store=True`.
- **חיפוש Google:** [חיפוש Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=he) מופעל כברירת מחדל, ויש [הגבלות ספציפיות](https://ai.google.dev/gemini-api/terms?hl=he#use-restrictions2) על התוצאות שמוצגות.

## המאמרים הבאים

- [מידע נוסף על Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he)
- [כך משתמשים בנתונים שלכם באמצעות הכלי 'חיפוש קבצים'](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-29 (שעון UTC)."],[],[]]
