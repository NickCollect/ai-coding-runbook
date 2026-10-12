---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=he
fetched_at: 2026-10-12T06:53:08.000903+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# Hooks

ה-Hooks מאפשרים להריץ סקריפטים מותאמים אישית או בקשות HTTP חיצוניות ממש לפני שהסוכן מריץ קוד או משנה קבצים בארגז החול המרוחק שלו, או מיד אחרי. אפשר להשתמש ב-hooks כדי להרחיב את לולאת הסוכן באמצעות אמצעי הגנה אוטומטיים ותהליכי עבודה ברקע, כמו:

- **אכיפת אמצעי הגנה על בטיחות וגישה** לפני הפעלת פקודות shell בסיכון גבוה או קריאות קבצים מוגבלות.
- **אוטומציה של טרנספורמציות בצינור נתונים** מיד אחרי שהסוכן יוצר או משנה קבצים.
- **הזרמת טלמטריית ביקורת של הארגון** למערכות ניטור חיצוניות אחרי הפעלת הכלי.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
            },
        ],
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

String gateScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "cmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\n"
    + "if \"rm -rf\" in cmd:\n"
    + "    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\n"
    + "else:\n"
    + "    print(json.dumps({\"decision\": \"allow\"}))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/gate.py")
            .content(gateScript)
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run `rm -rf /tmp/forbidden` using code_execution."))
    .tools(List.of(CodeExecution.builder().build()))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    gateScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/gate.py"),
                Content: genai.Ptr(gateScript),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run `rm -rf /tmp/forbidden` using code_execution."),
            Tools:       []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})},
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## אירועים נתמכים במחזור החיים

ה-Hooks תומכים ב-2 אירועים בתוך ארגז החול:

| אירוע | מתי הוא מופעל | תיאור |
| --- | --- | --- |
| `pre_tool_execution` | רגע לפני הפעלת כלי | יכולים לאשר (`allow`) או לחסום (`deny`) את הכלי לפני שהוא מופעל. כשחוסמים את המודל, הוא רואה את הסיבה לדחייה ומתאים את עצמו. |
| `post_tool_execution` | מיד אחרי שכלי מסיים את הפעולה | מריץ משימות המשך כמו עיצוב קוד, הרצת בדיקות יחידה או רישום טלמטריה. אי אפשר לחסום פעולות שהושלמו או לבטל אותן. |

### `pre_tool_execution`

מופעל ממש לפני שכלי מבצע פעולה. הסקריפט קורא את פרטי הקריאה לכלי מ-`stdin` ומוציא את ה-JSON של ההחלטה (`allow` או `deny`) ל-`stdout`.

**מטען ייעודי (payload) של קלט (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**תשובת הפלט (`stdout`):**

כדי לאשר את קריאת הפונקציה:

```
{
  "decision": "allow"
}
```

כדי לחסום את הקריאה לכלי ולהחזיר משוב למודל:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

כש-Hook דוחה פקודה, הכלי מפסיק את הפעולה באופן מיידי. הנציג רואה תוצאת שגיאה שמכילה את סיבת הדחייה שלו בתוך התור הנוכחי. לאחר מכן המודל יכול לתקן את עצמו על ידי בחירת פקודה חלופית או הסבר למשתמש על החסימה.

אם הסקריפט מחזיר פלט של JSON לא מזוהה, טקסט פשוט או כל דבר אחר מלבד `{"decision": "deny"}`, סביבת זמן הריצה מתייחסת לתגובה כאל אישור (`allow`).

### `post_tool_execution`

מופעל מיד אחרי שכלי משלים את הפעולה. הסקריפט קורא את פרטי ההרצה ואת סטטוס השגיאה מ-`stdin`.

**מטען ייעודי (payload) של קלט (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

אם פקודת מעטפת מדפיסה שגיאות לשגיאה רגילה (`stderr`) או אם פעולה במערכת הקבצים נכשלת, מטען הייעודי (payload) כולל שדה `"error"` שמכיל את טקסט השגיאה. אם הפקודה מצליחה ללא שגיאות, השדה `"error"` לא מופיע בכלל.

**תשובת הפלט (`stdout`):**

```
{}
```

הסיבה לכך היא שוובינרים של אחרי הכלים מופעלים רק למשימות ברקע, כמו עיצוב קוד או רישום ביומן, ולכן זמן הריצה מתעלם מערכי החלטה שמוחזרים ב-`stdout`.

## גילוי הגדרות

סביבת זמן הריצה מגלה באופן אוטומטי הגדרות של ווים מ-`.agents/hooks.json` או מ-`/.agents/hooks.json` בתוך סביבת ארגז החול. אתם יכולים לספק את `hooks.json` לצד הסקריפטים המותאמים אישית שלכם באמצעות כל [מקור סביבה](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he#mount_from_a_source) נתמך:

- **Repository mount**: מאגר Git שמכיל את `.agents/hooks.json` לצד `AGENTS.md`.
- ‫**Cloud Storage ‏ (`gcs`)**: קטגוריית GCS שמכילה את `hooks.json` שהועתקו לסביבה.
- **מקורות מוטבעים**: מחרוזת JSON גולמית ותוכן סקריפט שמועברים ב-`environment.sources` כשקוראים ל-`client.interactions.create`.

### `hooks.json` schema

קובץ `hooks.json` מקבץ הגדרות של אירועים (`pre_tool_execution` או `post_tool_execution`) תחת שמות מותאמים אישית. אפשר להפעיל או להשבית כל קבוצה בנפרד:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### התחביר והכללים של כלי ההתאמה

כל קבוצת כללים ב-`hooks.json` מגדירה מתי ואיך מופעלים ה-handlers באמצעות המאפיינים `matcher` ו-`hooks`:

| שדה | סוג | תיאור |
| --- | --- | --- |
| `enabled` | `boolean` | אופציונלי. מגדירים את הערך `false` כדי להשבית את הקבוצה (`true` כברירת מחדל). |
| `matcher` | `string` | הכלי שבו מתבצעת ההתאמה של תבנית הביטוי הרגולרי לשמות של כלים בתוך המאגר. |
| `hooks` | `array` | רשימה מסודרת של הגדרות של רכיבי handler ‏ (`command` או `http`). רכיבי ה-handler מופעלים ברצף לפי סדר ההצהרה. |

#### איך מתבצעת הערכה של ביטויים רגולריים

כשהסוכן מפעיל כלי בתוך ארגז החול, זמן הריצה מעריך את שם מאגר התגים של הכלי בהשוואה לתבנית `matcher` באמצעות ביטויים רגולריים סטנדרטיים של RE2. אם הביטוי הרגולרי תואם לשם הכלי, כל הפונקציות במערך `hooks` מופעלות לפי הסדר. אם כמה קבוצות כללים תואמות לאותו כלי, כל מערכי ה-handler המתאימים מופעלים.

אפשר לטרגט כל שם של כלי מובנה למאגר תגים: הפעלת קוד (`code_execution`) או פעולות במערכת הקבצים (`view_file`,‏ `write_to_file`,‏ `replace_file_content`,‏ `list_dir` ו-`delete_file`).

#### ביטויים נפוצים של התאמה

- `"code_execution"`: התאמה מדויקת של מחרוזות לפקודות מעטפת ולהרצת סקריפטים.
- ‫`"write_to_file"`: התאמה מדויקת ליצירת קבצים במערכת הקבצים ולכתיבה לדיסק.
- ‫`"view_file|write_to_file"`: הפרדה באמצעות קו אנכי מאפשרת התאמה של כמה שמות ספציפיים של כלים בכלל אחד.
- ‫`".*_file"`: התאמה של תו כללי לחיפוש בביטוי רגולרי לכל כלי שמסתיים ב-`_file` (כמו `view_file`,‏ `write_to_file` או `delete_file`). זה כולל רק חלק מהכלים במערכת הקבצים, `replace_file_content` ו-`list_dir` לא מסתיימים ב-`_file`, לכן צריך לציין את השמות שלהם במפורש כשצריך אותם. ביטויים רגולריים רגילים של RE2 דורשים `.*`. תבניות globs פשוטות של מעטפת כמו `*_file` הן תחביר לא חוקי של ביטוי רגולרי, ולא יתאימו.
- ‫`".*"` או `"*"` או `""`: תבנית כללית שמיירטת כל קריאה לכלי בתוך הקונטיינר.

## סוגי תוכניות לטיפול

### Command hooks

ה-hooks של הפקודות מריצים פקודת Shell או סקריפט בתוך ארגז החול. הסקריפט מקבל את ה-JSON של האירוע ב-`stdin` ומוציא את ה-JSON של ההחלטה ב-`stdout`.

| שדה | סוג | תיאור |
| --- | --- | --- |
| `type` | `string` | חייב להיות `"command"`. |
| `command` | `string` | שורת פקודה להרצה בתוך ארגז החול (לדוגמה, `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | זמן קצוב לתפוגה בשניות. ברירת מחדל: `30`. |

### ווים של HTTP

ה-hooks של HTTP שולחים את ה-JSON של האירוע כבקשת POST לכתובת URL חיצונית של HTTPS ישירות מתוך רשת ארגז החול. שרת היעד מחזיר את ההחלטה שלו בגוף תגובת ה-HTTP באמצעות אותו פורמט JSON בדיוק (`{"decision": "allow"}` או `{"decision": "deny", "reason": "..."}`).

| שדה | סוג | תיאור |
| --- | --- | --- |
| `type` | `string` | חייב להיות `"http"`. |
| `url` | `string` | נקודת קצה (endpoint) חיצונית מסוג HTTPS שאליה יישלח המטען הייעודי (payload) של האירוע באמצעות POST. |
| `headers` | `object` | צמדי מפתח/ערך אופציונליים עבור כותרות בהתאמה אישית שלא מכילות מידע רגיש (כמו `{"X-Event-Source": "agent-sandbox"}`). לצורך אימות, אפשר להשתמש ב[פרטי כניסה](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=he) ברשימת ההיתרים של הרשת. |
| `timeout` | `integer` | זמן קצוב לתפוגה בשניות. ברירת מחדל: `30`. |

#### שרת proxy ליציאה ושינוי טוקן

ה-hooks של HTTP מופעלים ישירות מתוך מרחב השמות של רשת ארגז החול, ולכן בקשות יוצאות עוברות דרך פרוקסי היציאה השקוף. הארכיטקטורה הזו מספקת 2 יתרונות אבטחה חשובים:

- **הוספה לרשימת ההיתרים של הרשת:** צריך לאשר במפורש את נקודות הקצה של היעד ב`network.allowlist` של הסביבה. תעבורת נתונים של לולאת חזרה (`127.0.0.1` או `localhost`) נחסמת על ידי ה-proxy. צריך תמיד לכוון לנקודות קצה חיצוניות ברשימת ההיתרים.
- **החדרת פרטי כניסה:** אין צורך לאחסן מפתחות API או טוקנים סודיים של bearer בתוך `.agents/hooks.json` או להטמיע אותם במאגר התגים. אחסון הסוד פעם אחת כ[אישור גישה](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=he) והפניה אליו לפי מזהה מ-`network.allowlist` של הסביבה. ה-proxy של היציאה מיירט באופן אוטומטי את תנועת ה-HTTP של ה-hook היוצאת ומזריק את כותרת האימות האמיתית בחיבור לפני היציאה מהארגז. כללי `transform` מוטמעים מגדירים כותרות באותו אופן בנתונים שמועברים ברשת, ופרטי הכניסה הם אלה שצריך להשתמש בהם כשרוצים לעשות שימוש חוזר בסוד בכל הפרויקט ולעדכן אותו במקום אחד. [הגדרת הרשת](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he#network-configuration)

## איך זמן הריצה מטפל בהחלטות ובכשלים

- **המתנה סינכרונית:** הסוכן מושהה וממתין לסיום הפעולה של ה-hooks לפני שהוא ממשיך.
- **חסימת ההפעלה של הכלי:** אם ה-hook שלפני הכלי מחזיר `{"decision": "deny", "reason": "<your reason>"}`, סביבת זמן הריצה מבטלת מיד את הקריאה לכלי. המודל רואה את הסיבה לדחייה בהיסטוריית השיחות שלו, ומתאים את עצמו על ידי בחירת חלופה בטוחה או הסבר למשתמש על החסימה.
- **טיפול בקריסות של סקריפטים, בשגיאות HTTP ובפסק זמן:** אם סקריפט של פקודה קורס (סטטוס יציאה שאינו אפס), אם ווֹבּוּק HTTP מחזיר קוד סטטוס שאינו 2xx (למשל שגיאת שרת 4xx או 5xx), או אם פעולה מסוימת חורגת מהזמן הקצוב לתגובה או מחזירה JSON לא מזוהה, סביבת זמן הריצה מתייחסת לכך כאל אישור (`allow`). הביצוע של הכלי ממשיך כרגיל, כך שסקריפט פגום או שרת טלמטריה שלא ניתן להגיע אליו אף פעם לא גורמים לקיפאון של האפליקציה.

## תרחישים נפוצים לדוגמה

### שחזור רב-שלבי לשמירה על פרטיות הנתונים ועמידה בדרישות התאימות

כש-hook חוסם גישה למשאבים מוגבלים – כמו ספריות שמכילות פרטים אישיים מזהים (PII) או רשומות פיננסיות סודיות – אפשר להעביר את הערך `previous_interaction_id` בקריאה הבאה כדי להמשיך את התהליך באותה סביבה. הסוכן קורא את ההסבר לדחייה ומתאושש אוטומטית על ידי שליחת שאילתה לטבלאות ציבוריות מאושרות במקום זאת.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "view_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "view_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
""";

String checkPrivacyScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "path = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\n"
    + "if \"/private/\" in path:\n"
    + "    resp = {\n"
    + "        \"decision\": \"deny\",\n"
    + "        \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"\n"
    + "    }\n"
    + "else:\n"
    + "    resp = {\"decision\": \"allow\"}\n"
    + "print(json.dumps(resp))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/check_privacy.py")
            .content(checkPrivacyScript)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/private/employees.json")
            .content("{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/public/summary.json")
            .content("{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}")
            .build()
    ))
    .build();

// Step 1: Agent attempts to read confidential PII records and is intercepted
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction int1 = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println(int1.outputText().orElse(""));

// Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."))
    .environment(CreateAgentInteractionEnvironment.of(int1.environmentId().orElse("")))
    .previousInteractionId(int1.id().orElse(""))
    .build();

Interaction int2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println(int2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}`

    checkPrivacyScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))
if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential '/private/' records is blocked by PII compliance policy. Query approved '/public/' summary tables instead."
    }
else:
    resp = {"decision": "allow"}
print(json.dumps(resp))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/check_privacy.py"),
                Content: genai.Ptr(checkPrivacyScript),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/private/employees.json"),
                Content: genai.Ptr(`{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}`),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/public/summary.json"),
                Content: genai.Ptr(`{"department": "Engineering", "team_size": 42, "status": "active"}`),
            },
        },
    }

    // Step 1: Agent attempts to read confidential PII records and is intercepted
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    int1 := res1.Interaction
    if int1.OutputText != nil {
        fmt.Println(*int1.OutputText)
    }

    // Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*int1.EnvironmentID)),
            PreviousInteractionID: int1.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"view_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-09-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### רישום ביומן ביקורת וטלמטריה חיצוניים

שליחת אירועי ביקורת בזמן אמת מתוך ארגז החול לשרת חיצוני למעקב בכל פעם שמתבצעת קריאה או שינוי של קבצים.

- **התאמה של כמה כלים:** מכיוון שכלי ההתאמה משתמשים בביטוי רגולרי רגיל, אפשר לשלב כמה כלים בכלל אחד באמצעות קווים אנכיים (`view_file|write_to_file|replace_file_content`) או תווים כלליים (`.*_file`).
- **לא לכלול סודות בהגדרה:** מאחסנים את אסימון האימות כ[פרטי כניסה](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=he) ומתייחסים אליו לפי מזהה מתוך [הגדרת הרשת](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he#network-configuration) של הסביבה (`network.allowlist.credential`). שרת ה-proxy ליציאה מוסיף את אסימון ה-bearer האמיתי לבקשות יוצאות. בדוגמה הזו, הכותרת מוגדרת בשורה עם `transform`, שמוגן על ידי אותו שרת proxy ומתאים כשהאסימון שייך להגדרה הזו.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "view_file|write_to_file|replace_file_content",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "view_file|write_to_file|replace_file_content",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Define hook without secrets; the egress proxy injects headers dynamically
String hooksConfig = """
{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("telemetry.example.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer telemetry_secret_token_123"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("*").build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Define hook without secrets; the egress proxy injects headers dynamically
    hooksConfig := `{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "telemetry.example.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer telemetry_secret_token_123",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"view_file|write_to_file|replace_file_content\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## מגבלות

- **היקף הכלי Sandbox:** ה-Hooks מיירטים כלים מובנים בתוך ארגז החול: ביצוע קוד (`code_execution`) ופעולות במערכת הקבצים (`view_file`,‏ `write_to_file`,‏ `replace_file_content`,‏ `list_dir` ו-`delete_file`). הם לא מופעלים עבור קריאות לפונקציות מותאמות אישית (`function`) או כלים חיצוניים של Model Context Protocol‏ (`mcp_server`) שמטופלים מחוץ למאגר.
- **רשימות היתרים ברשת:** וובי HTTP פועלים בתוך רשת מאגר התגים. צריך לאפשר באופן מפורש כתובות URL לטירגוט ב-`network.allowlist` של הסביבה. כתובות לולאה חוזרת (`localhost`, ‏ `127.0.0.1`) חסומות על ידי השרת הפרוקסי.
- **אישור אוטומטי במקרה של שגיאות:** אם סקריפט של ווֹק קורס (סטטוס יציאה שאינו אפס), חלף הזמן הקצוב לתפוגה שלו או שהוא נכשל, סביבת זמן הריצה מתעדת את הכישלון ומאפשרת להמשך הקריאה לכלי. כך אפליקציות לא ייתקעו בגלל סקריפטים של כלי Linter שבורים או תהליכים תקועים.
- **הגנה על הגדרות ארגז החול (Sandbox):** מכיוון שה-Hooks מופעלים בתוך ארגז החול של הקונטיינר, סוכנים עם כלי כתיבה למערכת הקבצים או הרשאות להפעלת קוד מעטפת יכולים לשנות את `.agents/hooks.json` המקומי או סקריפטים בסביבות עבודה שניתן לכתוב בהן. אפשר להשתמש ב-container hooks כהנחיות מדיניות אוטומטיות וכאמצעי הגנה תפעוליים. אם נדרשת עמידות קפדנית בפני שינויים לא מורשים בהרצת מודלים לא מהימנים, צריך להגדיר מקורות של תצורות ממאגרים לקריאה בלבד.

## המאמרים הבאים

- [איך מגדירים ארגזי חול וסביבות מרחוק קבועים](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he)
- כדאי לעיין ביכולות ובכלים המובנים של [סוכן Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he).
- מידע נוסף על סשנים רב-שלביים ועל סטרימינג זמין [בסקירה הכללית על Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-07 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-07 (שעון UTC)."],[],[]]
