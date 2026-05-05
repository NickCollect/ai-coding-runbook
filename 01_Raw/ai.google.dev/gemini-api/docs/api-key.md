---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=he
fetched_at: 2026-05-05T20:50:32.168132+00:00
title: "\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1\u05de\u05e4\u05ea\u05d7\u05d5\u05ea API \u05e9\u05dc Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שימוש במפתחות API של Gemini

כדי להשתמש ב-Gemini API, אתם צריכים מפתח API. בדף הזה מוסבר איך ליצור ולנהל את המפתחות ב-Google AI Studio, ואיך להגדיר את הסביבה כדי להשתמש בהם בקוד.

[איך יוצרים מפתח Gemini API או צופים בו](https://aistudio.google.com/app/apikey?hl=he)

## מפתחות API

אתם יכולים ליצור ולנהל את כל מפתחות Gemini API מתוך הדף **מפתחות API** ב-[Google AI Studio](https://aistudio.google.com/app/apikey?hl=he).

אחרי שיש לכם מפתח API, יש לכם את האפשרויות הבאות להתחבר ל-Gemini API:

- [הגדרת מפתח ה-API כמשתנה סביבה](#set-api-env-var)
- [העברת מפתח ה-API באופן מפורש](#provide-api-key-explicitly)

לצורך בדיקה ראשונית, אפשר להגדיר מפתח API בהארדקוד, אבל זה צריך להיות זמני כי זה לא מאובטח. דוגמאות לקידוד קשיח של מפתח ה-API מופיעות בקטע [הוספה מפורשת של מפתח API](#provide-api-key-explicitly).

## פרויקטים ב-Google Cloud

[פרויקטים ב-Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=he) הם הבסיס לשימוש בשירותי Google Cloud (כמו Gemini API), לניהול החיוב ולשליטה בשותפי עריכה ובהרשאות. ‫Google AI Studio מספק ממשק קל משקל לפרויקטים שלכם ב-Google Cloud.

אם עדיין לא יצרתם פרויקטים, אתם צריכים ליצור פרויקט חדש או לייבא פרויקט מ-Google Cloud אל Google AI Studio. בדף **Projects** ב-Google AI Studio יוצגו כל המפתחות שיש להם הרשאה מספקת להשתמש ב-Gemini API. הוראות מפורטות זמינות בקטע [ייבוא פרויקטים](#import-projects).

### פרויקט ברירת מחדל

למשתמשים חדשים, אחרי אישור התנאים וההגבלות, Google AI Studio יוצר פרויקט ברירת מחדל ב-Google Cloud ומפתח API, כדי להקל על השימוש. כדי לשנות את השם של הפרויקט ב-Google AI Studio, עוברים לתצוגה **Projects** ב**מרכז הבקרה**, לוחצים על סמל ההגדרות (3 נקודות) לצד הפרויקט ובוחרים באפשרות **Rename project** (שינוי שם הפרויקט). למשתמשים קיימים או למשתמשים שכבר יש להם חשבונות Google Cloud לא נוצר פרויקט ברירת מחדל.

## ייבוא פרויקטים

כל מפתח Gemini API משויך לפרויקט בענן של Google. כברירת מחדל, לא כל הפרויקטים שלכם ב-Cloud מוצגים ב-Google AI Studio. כדי לייבא פרויקטים, צריך לחפש את השם או את מזהה הפרויקט בתיבת הדו-שיח **ייבוא פרויקטים**. כדי לראות רשימה מלאה של הפרויקטים שיש לכם גישה אליהם, נכנסים ל-Cloud Console.

אם עדיין לא ייבאתם פרויקטים, פועלים לפי השלבים הבאים כדי לייבא פרויקט של Google Cloud וליצור מפתח:

1. עוברים אל [Google AI Studio](https://aistudio.google.com?hl=he).
2. פותחים את **מרכז הבקרה** מהחלונית הימנית.
3. לוחצים על **פרויקטים**.
4. בדף **Projects** (פרויקטים), לוחצים על הלחצן **Import projects** (ייבוא פרויקטים).
5. מחפשים את פרויקט הענן ב-Google Cloud שרוצים לייבא, בוחרים אותו ולוחצים על הלחצן **ייבוא**.

אחרי שמייבאים פרויקט, עוברים לדף **API Keys** בתפריט **Dashboard** ויוצרים מפתח API בפרויקט שזה עתה ייבאתם.

## מגבלות

אלה המגבלות על ניהול מפתחות API ופרויקטים ב-Google Cloud ב-Google AI Studio.

- אפשר ליצור עד 10 פרויקטים בכל פעם בדף **Projects** ב-Google AI Studio.
- אתם יכולים לתת שמות לפרויקטים ולמפתחות ולשנות את השמות שלהם.
- בדפים **API keys** ו-**Projects** מוצגים עד 100 מפתחות ו-50 פרויקטים.
- מוצגים רק מפתחות API ללא הגבלות, או מפתחות API עם הגבלות על Generative Language API.

כדי לקבל גישה נוספת לניהול הפרויקטים, כולל שינוי מפתחות API והגבלת הגישה אליהם, אפשר להיכנס אל [דף פרטי הכניסה במסוף Google Cloud](https://console.cloud.google.com/apis/credentials?hl=he).
ב-Cloud Console, אפשר לבחור את הפרויקט, ללחוץ על מפתח API קיים ואז להגביל אותו ל-**Generative Language API**.

## הגדרת מפתח ה-API כמשתנה סביבה

אם מגדירים את משתנה הסביבה `GEMINI_API_KEY` או `GOOGLE_API_KEY`, מפתח ה-API יזוהה באופן אוטומטי על ידי הלקוח כשמשתמשים באחת מ[ספריות Gemini API](https://ai.google.dev/gemini-api/docs/libraries?hl=he). מומלץ להגדיר רק אחד מהמשתנים האלה, אבל אם מגדירים את שניהם, `GOOGLE_API_KEY` מקבל עדיפות.

אם אתם משתמשים ב-API בארכיטקטורת REST או ב-JavaScript בדפדפן, תצטרכו לציין את מפתח ה-API באופן מפורש.

כך מגדירים את מפתח ה-API באופן מקומי כמשתנה הסביבה `GEMINI_API_KEY` במערכות הפעלה שונות.

### ‫Linux/macOS – Bash

‫Bash היא הגדרה נפוצה של טרמינל ב-Linux וב-macOS. כדי לבדוק אם יש לכם קובץ תצורה בשבילו, מריצים את הפקודה הבאה:

```
~/.bashrc
```

אם התשובה היא "No such file or directory" (אין קובץ או ספרייה כאלה), צריך ליצור את הקובץ הזה ולפתוח אותו באמצעות הפעלת הפקודות הבאות, או להשתמש ב-`zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

בשלב הבא צריך להגדיר את מפתח ה-API על ידי הוספת פקודת הייצוא הבאה:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

אחרי ששומרים את הקובץ, מריצים את הפקודה הבאה כדי להחיל את השינויים:

```
source ~/.bashrc
```

### ‫macOS –‏ Zsh

‫Zsh היא הגדרה נפוצה של טרמינל ב-Linux וב-macOS. כדי לבדוק אם יש לכם קובץ תצורה בשבילו, מריצים את הפקודה הבאה:

```
~/.zshrc
```

אם התשובה היא "No such file or directory" (אין קובץ או ספרייה כאלה), צריך ליצור את הקובץ הזה ולפתוח אותו באמצעות הפעלת הפקודות הבאות, או להשתמש ב-`bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

בשלב הבא צריך להגדיר את מפתח ה-API על ידי הוספת פקודת הייצוא הבאה:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

אחרי ששומרים את הקובץ, מריצים את הפקודה הבאה כדי להחיל את השינויים:

```
source ~/.zshrc
```

### Windows

1. בסרגל החיפוש, מחפשים את האפשרות Environment Variables (משתני סביבה).
2. בוחרים באפשרות לשינוי **הגדרות המערכת**. יכול להיות שתתבקשו לאשר שאתם רוצים לבצע את הפעולה הזו.
3. בתיבת הדו-שיח של הגדרות המערכת, לוחצים על הלחצן **Environment
   Variables** (משתני סביבה).
4. בקטע **User variables** (משתני משתמש, עבור המשתמש הנוכחי) או **System variables** (משתני מערכת, חל על כל המשתמשים במחשב), לוחצים על **New...** (חדש...).
5. מציינים את שם המשתנה כ-`GEMINI_API_KEY`. מציינים את מפתח ה-API של Gemini כערך המשתנה.
6. לוחצים על **אישור** כדי להחיל את השינויים.
7. פותחים סשן טרמינל חדש (cmd או Powershell) כדי לקבל את המשתנה החדש.

## ציון מפתח ה-API באופן מפורש

במקרים מסוימים, כדאי לספק מפתח API באופן מפורש. לדוגמה:

- אתם מבצעים קריאה פשוטה ל-API ומעדיפים להגדיר את מפתח ה-API בתוך הקוד.
- אתם רוצים שליטה מפורשת בלי להסתמך על גילוי אוטומטי של משתני סביבה על ידי ספריות Gemini API
- אתם משתמשים בסביבה שבה משתני סביבה לא נתמכים (למשל, באינטרנט) או שאתם מבצעים קריאות REST.

בהמשך מפורטות דוגמאות לאופן שבו אפשר לספק מפתח API באופן מפורש:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## שמירה על אבטחת מפתח ה-API

התייחס למפתח ה-API של Gemini כמו לסיסמה. אם המפתח ייפרץ, אנשים אחרים יוכלו להשתמש במכסת הפרויקט, לחייב אתכם (אם החיוב מופעל) ולגשת לנתונים הפרטיים שלכם, כמו קבצים.

### כללי אבטחה קריטיים

- **שמירה על סודיות המפתחות**: מפתחות API של Gemini עשויים לגשת למידע אישי רגיש שהאפליקציה שלכם מסתמכת עליו.

  - **לעולם אל תבצעו קומיט של מפתחות API למערכת לניהול גרסאות.** אל תכניסו את מפתח ה-API למערכות בקרת גרסאות כמו Git.
  - **לעולם אל תחשפו מפתחות API בצד הלקוח.** לא להשתמש במפתח ה-API ישירות באפליקציות לאינטרנט או לנייד בסביבת ייצור. אפשר לחלץ מפתחות מקוד בצד הלקוח (כולל ספריות JavaScript/TypeScript וקריאות ל-REST).
- **הגבלת הגישה**: כדאי להגביל את השימוש במפתח API לכתובות IP ספציפיות, לגורמים מפנים מסוג HTTP או לאפליקציות ספציפיות ל-Android או ל-iOS, אם אפשר.
- **הגבלת השימוש**: מפעילים רק את ממשקי ה-API הנדרשים לכל מפתח.
- **ביצוע בדיקות שוטפות**: חשוב לבדוק את מפתחות ה-API באופן קבוע ולבצע רוטציה שלהם מדי פעם.

### שיטות מומלצות

- **שימוש בקריאות בצד השרת עם מפתחות API** הדרך הכי מאובטחת להשתמש במפתח API היא לשלוח קריאה ל-Gemini API מאפליקציה בצד השרת, שבה אפשר לשמור את המפתח בסודיות.
- **שימוש בטוקנים זמניים לגישה בצד הלקוח (Live API בלבד):** כדי לקבל גישה ישירה ל-Live API בצד הלקוח, אפשר להשתמש בטוקנים זמניים. הן מגיעות עם סיכוני אבטחה נמוכים יותר ויכולות להתאים לשימוש בסביבת הייצור. מידע נוסף זמין במדריך בנושא [טוקנים זמניים](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=he).
- **כדאי להוסיף הגבלות למפתח:** אפשר להגביל את ההרשאות של מפתח על ידי הוספה של [הגבלות על מפתחות API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=he#add-api-restrictions).
  כך מצמצמים את הנזק הפוטנציאלי אם המפתח ידלוף.

[במאמר הזה](https://support.google.com/googleapi/answer/6310037?hl=he) מפורטות שיטות מומלצות כלליות נוספות.

## פתרון בעיות ביצירת מפתח API

ב-Google AI Studio, יכול להיות שהלחצן **Create API key** לא יהיה זמין, ותופיע ההודעה: *You do not have permission to create a key in this project* (אין לך הרשאה ליצור מפתח בפרויקט הזה).

השגיאה הזו מתרחשת כשאין לכם את ההרשאות הנדרשות בפרויקט כדי ליצור מפתח חדש:

- ‫**`resourcemanager.projects.get`**: מאפשר ל-AI Studio לאמת את קיום הפרויקט.
- ‫**`apikeys.keys.create`**: מאפשר ליצור את מפתח ה-API עצמו.
- ‫**`serviceusage.services.enable`**: נדרש כדי לוודא ש-Gemini API פעיל בפרויקט.

כדי לתקן את ההרשאות, צריך לבקש מאדמין הפרויקט או מהאדמין של הארגון (אם הפרויקט שייך ל[ארגון](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=he)) להקצות לכם תפקיד עם ההרשאות שצוינו למעלה (כמו עריכה בפרויקט או תפקיד בהתאמה אישית).

אם אין לכם הרשאת אדמין בפרויקט, אתם יכולים ליצור פרויקט חדש שלא משויך לארגון כדי ליצור את המפתחות.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
