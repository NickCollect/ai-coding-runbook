---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=he
fetched_at: 2026-08-17T02:17:50.044559+00:00
title: "\u05e9\u05d9\u05dc\u05d5\u05d1 \u05e9\u05dc \u05db\u05dc\u05d9\u05dd \u05de\u05d5\u05d1\u05e0\u05d9\u05dd \u05d5\u05e7\u05e8\u05d9\u05d0\u05d4 \u05dc\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d5\u05ea \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שילוב של כלים מובנים וקריאה לפונקציות

‫

‫Gemini מאפשר לשלב [כלים מובנים](https://ai.google.dev/gemini-api/docs/tools?hl=he), כמו `google_search`, ו[קריאות לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) (שנקראות גם *כלים מותאמים אישית*) ביצירה אחת, על ידי שמירה של היסטוריית ההקשר של קריאות לכלים וחשיפה שלה. שילובים מובנים ומותאמים אישית של כלים מאפשרים תהליכי עבודה מורכבים ודינמיים. לדוגמה, המודל יכול להסתמך על נתונים מהאינטרנט בזמן אמת לפני שהוא מפעיל את הלוגיקה העסקית הספציפית שלכם.

דוגמה שבה מופעלים שילובים מובנים ומותאמים אישית של כלים באמצעות `google_search` ופונקציה מותאמת אישית `getWeather`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.getGenerativeModel({
        model: "gemini-3.6-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.6-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## איך זה עובד

מודלים של Gemini 3 משתמשים ב*העברת הקשר של כלי* כדי לאפשר שילובים מובנים ושילובים בהתאמה אישית של כלים. הפצת ההקשר של כלי מאפשרת לשמור את ההקשר של כלים מובנים ולחשוף אותו, ולשתף אותו עם כלים בהתאמה אישית באותה שיחה, מתור לתור.

### הפעלת שילוב של כלים

- כדי להפעיל את העברת ההקשר של הכלי, צריך להגדיר את הדגל `include_server_side_tool_invocations` לערך `true`.
- כדי להפעיל את ההתנהגות המשולבת, צריך לכלול את [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#function-declarations), יחד עם הכלים המובנים שרוצים להשתמש בהם.
  - אם לא תכללו את `function_declarations`, עדיין תהיה השפעה של העברת ההקשר של הכלי על הכלים המובנים שכללתם, כל עוד הדגל מוגדר.

### חלקים שמוחזרים על ידי ה-API

בתשובה אחת, ה-API מחזיר את החלקים `toolCall` ו-`toolResponse` של קריאת הפונקציה המובנית. במקרה של קריאה לפונקציה (כלי בהתאמה אישית), ה-API מחזיר את `functionCall` החלק של הקריאה, והמשתמש מספק את החלק `functionResponse` בתור הבא.

- ‫`toolCall` ו-`toolResponse`: ה-API מחזיר את החלקים האלה כדי לשמור על ההקשר של הכלים שמופעלים בצד השרת, ועל התוצאה של ההרצה שלהם, לתור הבא.
- ‫`functionCall` ו-`functionResponse`: ה-API שולח את הקריאה לפונקציה למשתמש כדי למלא אותה, והמשתמש שולח את התוצאה בחזרה בתגובה לפונקציה (החלקים האלה הם סטנדרטיים לכל [הקריאות לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) ב-Gemini API, ולא ייחודיים לתכונה של שילוב כלים).
- ([כלי להרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) בלבד)
  ‫`executableCode` ו-`codeExecutionResult`:
  כשמשתמשים בכלי להרצת קוד, במקום `functionCall` ו-`functionResponse`, ה-API מחזיר `executableCode` (הקוד שנוצר על ידי המודל שאמור להיות מורץ) ו-`codeExecutionResult` (התוצאה של הקוד שניתן להרצה).

כדי לשמור על ההקשר ולאפשר שילוב של כלים, צריך להחזיר למודל את כל החלקים, כולל כל [השדות](#critical-fields) שהם מכילים, בכל תור.

### שדות קריטיים בחלקים שמוחזרים

[חלקים מסוימים שמוחזרים על ידי ה-API](#api-returns-parts) יכללו את השדות `id`,‏ `tool_type` ו-`thought_signature`. השדות האלה חשובים לשמירה על ההקשר של הכלי (ולכן חשובים לשילובים של כלים). צריך להחזיר את כל החלקים *כפי שמופיעים בתשובה* בבקשות הבאות.

- ‫`id`: מזהה ייחודי שממפה קריאה לתגובה שלה. הערך `id` **מוגדר בכל התשובות של קריאות לפונקציות**, ללא קשר להפצה של הקשר הכלי.
  *חובה* לספק את אותו `id` בתשובת הפונקציה שה-API מספק בקריאה לפונקציה. הכלים המובנים משתפים באופן אוטומטי את `id` בין קריאת הכלי לתגובה של הכלי.
  - מופיע בכל החלקים שקשורים לכלי: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- ‫`tool_type`: מזהה את הכלי הספציפי שבו נעשה שימוש; השם המילולי של הכלי המובנה
  או (לדוגמה, `URL_CONTEXT`) או הפונקציה (לדוגמה, `getWeather`).
  - נמצא בחלקים `toolCall` ו-`toolResponse`.
- ‫`thought_signature`: ההקשר המוצפן בפועל שמוטמע ב**כל חלק שמוחזר על ידי ה-API**. אי אפשר לשחזר את ההקשר בלי חתימות המחשבה. אם לא תחזירו את חתימות המחשבה לכל החלקים בכל תור, המודל יחזיר שגיאה.
  - נמצא ב*כל* החלקים.

### נתונים ספציפיים לכלי

חלק מהכלים המובנים מחזירים ארגומנטים של נתונים שגלויים למשתמשים, שספציפיים לסוג הכלי.

| כלי | User visible tool call args (if any) | תגובה של הכלי שגלויה למשתמש (אם יש) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` כתובות URL לבדיקה | ‫`urls_metadata` `retrieved_url`: כתובות URL שנבדקו `url_retrieval_status`: סטטוס הבדיקה |
| **FILE\_SEARCH** | ללא | ללא |

## דוגמה למבנה של בקשה לשילוב כלים

מבנה הבקשה הבא מציג את מבנה הבקשה של ההנחיה: "מהי העיר הכי צפונית בארצות הברית? What's the weather like there
today?". הוא משלב שלושה כלים: הכלים המובנים של Gemini‏ `google_search`
ו-`code_execution`, ופונקציה בהתאמה אישית `get_weather`.

```
{
  "model": "models/gemini-3.6-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## אסימונים ותמחור

שימו לב: החלקים `toolCall` ו-`toolResponse` בבקשות נספרים במסגרת `prompt_token_count`. השלבים האלה של כלי הביניים גלויים לכם עכשיו ומוחזרים לכם, ולכן הם חלק מהיסטוריית השיחה. זה קורה רק ב*בקשות*, ולא ב*תגובות*.

הכלי של חיפוש Google הוא חריג לכלל הזה. חיפוש Google כבר מחיל מודל תמחור משלו ברמת השאילתה, כך שלא מתבצע חיוב כפול על טוקנים (ראו את הדף [תמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he)).

מידע נוסף זמין בדף [אסימונים](https://ai.google.dev/gemini-api/docs/tokens?hl=he).

## מגבלות

- ברירת המחדל היא מצב `VALIDATED` (מצב `AUTO` לא אפשרי) כשהדגל `include_server_side_tool_invocations` מופעל
- כלים מובנים כמו `google_search` מסתמכים על מידע לגבי המיקום והשעה הנוכחית, ולכן אם יש סתירה במידע לגבי המיקום והשעה ב-`system_instruction` או ב-`function_declaration.description`, יכול להיות שהתכונה של שילוב כלים לא תפעל בצורה טובה.

## כלים נתמכים

הפצת ההקשר הרגילה של הכלי חלה על כלים בצד השרת (מוכללים).
הכלי Code Execution (הרצת קוד) הוא גם כלי בצד השרת, אבל יש לו פתרון מובנה משלו להעברת הקשר. השימוש במחשב והפעלת פונקציות הם כלים בצד הלקוח, ויש להם גם פתרונות מובנים להעברת הקשר.

| כלי | צד הביצוע | תמיכה בהעברת הקשר |
| --- | --- | --- |
| [חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) | צד השרת | כן |
| [מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he) | צד השרת | כן |
| [הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he) | צד השרת | כן |
| [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he) | צד השרת | כן |
| [Code Execution](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) | צד השרת | נתמך (מובנה, משתמש בחלקים `executableCode` ו-`codeExecutionResult`) |
| [שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he) | בצד הלקוח | נתמך (מובנה, משתמש בחלקים `functionCall` ו-`functionResponse`) |
| [פונקציות מותאמות אישית](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) | בצד הלקוח | נתמך (מובנה, משתמש בחלקים `functionCall` ו-`functionResponse`) |

## המאמרים הבאים

- מידע נוסף על [בקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) ב-Gemini API
- אפשר לעיין ברשימת הכלים הנתמכים:
  - [חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he)
  - [מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he)
  - [הקשר של כתובת ה-URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he)
  - [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
