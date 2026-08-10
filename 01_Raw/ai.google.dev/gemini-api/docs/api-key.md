---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=he
fetched_at: 2026-08-10T03:14:23.305916+00:00
title: "\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1\u05de\u05e4\u05ea\u05d7\u05d5\u05ea API \u05e9\u05dc Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שימוש במפתחות API של Gemini

כדי להשתמש ב-Gemini API, צריך לאמת את הבקשות. אפשר לבצע אימות באמצעות מפתח API רגיל או מפתח API להרשאה.

[איך יוצרים מפתח Gemini API או צופים בו](https://aistudio.google.com/apikey?hl=he)

## סוגי מפתחות API: רגיל לעומת הרשאה

מפתחות API מספקים גישה ל-Gemini API, אבל מאפייני האבטחה שלהם שונים. אנחנו מעבירים את Gemini API ממפתחות API רגילים למפתחות הרשאה כדי לשפר את האבטחה:

- **מפתחות API רגילים**: משייכים בקשות לפרויקט בענן ב-Google Cloud לצורכי חיוב ומכסה. מפתחות רגילים לא מזהים את היישות שקוראת ל-API, ולכן הם לא יכולים לתמוך בהרשאות ובבקרת גישה ברמת פירוט גבוהה.
- **מפתחות הרשאה (auth)**: מקושרים ישירות לחשבון שירות של Google Cloud. כשמשתמשים במפתח הרשאה, הבקשות מעובדות תחת הזהות של חשבון השירות המקושר, וכך מתאפשרת שליטה מדויקת בגישה. כברירת מחדל, מפתחות הרשאה מוגבלים ל-Generative Language API ‏(Gemini API) ומספקים אכיפה מהירה של מפתחות שנחשפו, שמפסיקה במהירות את השימוש במפתחות שנחשפו שזוהו על ידי המערכות שלנו.

כדי להבטיח שימוש מאובטח, Gemini API יעבור ממפתחות רגילים למפתחות אימות:

- **ברירת המחדל של מפתחות אימות**: כל מפתחות ה-API החדשים שנוצרים ב-Google AI Studio נוצרים אוטומטית כמפתחות אימות.
- **דחייה של מפתחות ללא הגבלות**: Gemini API דוחה בקשות מ**מפתחות רגילים ללא הגבלות**. מפתחות API רגילים שהוחלו עליהם הגבלות מפורשות ממשיכים לפעול. ההגבלה הזו מונעת שימוש לא מורשה במפתחות שאולי שותפו באופן ציבורי או מקושרים לשירותים אחרים.
- **בספטמבר 2026**: Gemini API ידחה בקשות מ**מפתחות רגילים**. כדי למנוע שיבושים בשירות, חשוב [לעבור למפתחות אימות](#migrate-to-auth-key) לפני התאריך הזה. חשוב להעביר את המינוי למפתחות אימות לפני ספטמבר 2026.

## ניהול מפתחות API ב-Google AI Studio

אתם יכולים לנהל את הפרויקטים והמפתחות שלכם ישירות ב-[Google AI Studio](https://aistudio.google.com/apikey?hl=he).

### פרויקטים ב-Google Cloud

כל מפתח Gemini API משויך ל[פרויקט בענן של Google](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=he).
בפרויקטים ב-Google Cloud מנהלים את החיוב, את שותפי העריכה ואת ההרשאות. ‫Google AI Studio מספק ממשק קל משקל לגישה לפרויקטים האלה.

- **פרויקט ברירת מחדל**: אם אתם משתמשים חדשים, Google AI Studio יוצר באופן אוטומטי פרויקט בענן ב-Google Cloud ומפתח API שמוגדרים כברירת מחדל אחרי שאתם מאשרים את התנאים וההגבלות. כדי לשנות את שם הפרויקט, עוברים לתצוגה **Projects** במרכז הבקרה.
- **פרויקטים קיימים**: אם כבר יש לכם חשבון Google Cloud, ‏ AI Studio לא יוצר פרויקט ברירת מחדל. במקום זאת, צריך לייבא את הפרויקטים הקיימים.

### ייבוא פרויקטים

כברירת מחדל, לא כל הפרויקטים שלכם ב-Google Cloud מוצגים ב-Google AI Studio. צריך לייבא את הפרויקטים שרוצים להשתמש בהם:

1. עוברים אל [Google AI Studio](https://aistudio.google.com?hl=he).
2. פותחים את **לוח הבקרה** בחלונית הימנית ובוחרים באפשרות **פרויקטים**.
3. לוחצים על הלחצן **ייבוא פרויקטים**.
4. מחפשים את פרויקט הענן ב-Google Cloud שרוצים לייבא ובוחרים אותו, ואז לוחצים על **ייבוא**.
5. אחרי הייבוא, עוברים לדף **מפתחות API** במרכז הבקרה כדי ליצור מפתח בפרויקט הזה.

### פתרון בעיות בהרשאות ליצירת מפתחות

אם הלחצן **Create API key** לא זמין ומוצגת ההודעה:
*"You do not have permission to create a key in this project"*, סימן שאין לכם את הרשאות ה-IAM הנדרשות.

מבקשים מהאדמין של פרויקט בענן או הארגון ב-Google Cloud להקצות לכם תפקיד שמכיל את ההרשאות הבאות (למשל, עורך פרויקט):

- ‫`resourcemanager.projects.get`: מאפשר ל-AI Studio לאמת את הפרויקט.
- ‫`apikeys.keys.create`: מאפשר יצירת מפתחות.
- ‫`serviceusage.services.enable`: מוודא שממשק Generative Language API מופעל.
- `iam.serviceAccounts.create`: חובה כדי ליצור את חשבון השירות המקושר.
- ‫`iam.serviceAccountApiKeyBindings.create`: קושר את חשבון השירות למפתח ה-API.

אם אין לכם אפשרות לקבל הרשאת אדמין, אתם יכולים ליצור פרויקט חדש ב-Google Cloud שלא משויך לארגון כדי ליצור את המפתחות.

## הגדרת הסביבה

אחרי שיש לכם מפתח, אתם צריכים להגדיר את הסביבה כך שהמפתח ישמש את האפליקציות שלכם בצורה מאובטחת.

### אפשרות 1: שימוש במשתני סביבה (מומלץ)

מגדירים את משתנה הסביבה `GEMINI_API_KEY` או `GOOGLE_API_KEY`. ספריות הלקוח של Gemini API מזהות את המשתנים האלה ומשתמשות בהם באופן אוטומטי. אם שניהם מוגדרים, `GOOGLE_API_KEY` מקבל עדיפות.

בוחרים את מערכת ההפעלה כדי להגדיר את המשתנה:

### ‫Linux/macOS – Bash

בודקים אם יש לכם קובץ הגדרות bash:

```
~/.bashrc
```

אם לא, יוצרים חשבון ופותחים אותו:

```
touch ~/.bashrc && open ~/.bashrc
```

מוסיפים את פקודת הייצוא בסוף הקובץ:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

שומרים את הקובץ ומחילים את השינויים:

```
source ~/.bashrc
```

### ‫macOS – Zsh

בודקים אם יש לכם קובץ הגדרות zsh:

```
~/.zshrc
```

אם לא, יוצרים חשבון ופותחים אותו:

```
touch ~/.zshrc && open ~/.zshrc
```

מוסיפים את פקודת הייצוא:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

שומרים את הקובץ ומחילים את השינויים:

```
source ~/.zshrc
```

### Windows

1. בסרגל החיפוש של Windows, מחפשים את האפשרות 'משתני סביבה'.
2. בתיבת הדו-שיח System Properties (מאפייני מערכת), לוחצים על **Environment Variables** (משתני סביבה).
3. בקטע **משתנים בהגדרת המשתמש** או **משתני מערכת**, לוחצים על **חדש...**.
4. מגדירים את שם המשתנה כ-`GEMINI_API_KEY` ואת הערך כמפתח ה-API.
5. כדי לשמור את קיצור הדרך, לחץ על **אישור**. פותחים סשן טרמינל חדש כדי לטעון את המשתנה.

### אפשרות 2: ציון מפורש של מפתח ה-API בקוד

אפשר להעביר את מפתח ה-API באופן מפורש כשמאתחלים את הלקוח. כדאי לעשות את זה רק אם אי אפשר להשתמש במשתני סביבה.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
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
    "google.golang.org/genai/interactions"
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

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.6-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.6-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## אבטחה וניהול סודות

מפתח ה-API של Gemini הוא כמו סיסמה. אם פרטי הכניסה נחשפו, אנשים אחרים יכולים לנצל את המכסה של הפרויקט, לגרום לחיובים לא צפויים ולגשת למשאבים פרטיים.

### כללי אבטחה קריטיים

- **שומרים על סודיות המפתחות**: אף פעם אל תכניסו מפתחות API למערכות בקרת מקור כמו Git.
- **לעולם אל תחשפו מפתחות בצד הלקוח בסביבת ייצור**: אל תקודדו מפתחות API ישירות באפליקציות אינטרנט או באפליקציות לנייד. משתמשים יכולים לחלץ מפתחות שנאספים בקוד בצד הלקוח. כדי לאבטח אפליקציות בצד הלקוח, מריצים שרת proxy בקצה העורפי כדי לבצע את הקריאות בפועל ל-API.

### שיטות מומלצות לניהול סודות

- **משתני סביבה**: קריאת מפתחות ממשתני סביבה במקום מקובצי תצורה.
- ‫**Secret Manager**: בסביבת ייצור, מומלץ לאחסן את המפתחות במאגר סודי מאובטח כמו [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=he).
- **התראות על חיוב**: אפשר להגדיר התראות על חיוב ב-Google Cloud Console כדי לקבל הודעה אם יש עלייה חדה בשימוש או בעלויות.

### רשימת משימות לתגובה לדליפת נתונים

אם אתם חושדים שמפתח ה-API שלכם דלף:

1. **יצירת מפתח חדש**: יוצרים מפתח חלופי ב-Google AI Studio או ב-Cloud Console.
2. **מעדכנים את האפליקציה**: פורסים את הקוד באמצעות המפתח החדש.
3. **משביתים או מוחקים את המפתח שנפרץ**: אחרי שהמפתח החדש מאומת, משביתים את המפתח שנפרץ במסוף Cloud. כדי למנוע השבתה של האפליקציה, אל תמחקו את המפתח הישן עד שהמפתח החדש יהיה פעיל לגמרי.
4. **בדיקת השימוש**: כדי לזהות פעילות לא מורשית, בודקים את יומני החיוב ואת השימוש ב-API במסוף Google Cloud.

## הגבלת הגישה למפתחות והגנה עליהם

הוספת הגבלות למפתחות ה-API מצמצמת את הנזק הפוטנציאלי אם מפתח נפרץ.

### החלת הגבלות על מקור הבקשה

הגבלות על מקורות מגבילות את כתובות ה-IP, האתרים או האפליקציות שיכולים להשתמש במפתח.

1. נכנסים אל [הדף Credentials במסוף Google Cloud](https://console.cloud.google.com/apis/credentials?hl=he).
2. בוחרים את הפרויקט ולוחצים על השם של מפתח ה-API שרוצים להגביל.
3. בקטע **Application restrictions**, בוחרים באפשרות **IP addresses** (או בסוג ההגבלה המתאים לסביבה שלכם).
4. מציינים את כתובות ה-IP או את טווחי כתובות ה-IP המותרים ולוחצים על **שמירה**.

### אבטחה של מפתחות API רגילים ללא הגבלות

כדי להמשיך להשתמש ב-Gemini API, צריך לאבטח את כל המפתחות הלא מוגבלים.

#### שיטה א': הגבלת המפתח ל-Gemini API בלבד (AI Studio)

אם אתם משתמשים במפתח רק ל-Gemini API, אתם יכולים לאבטח אותו ישירות ב-AI Studio:

1. בדף **API Keys** ב-[Google AI Studio](https://aistudio.google.com/api-keys?hl=he), מאתרים מפתחות שמסומנים בתווית **Unrestricted**.
2. מעבירים את העכבר מעל התווית ולוחצים על **הוספת הגבלות** בתיבת הדו-שיח.
3. בוחרים באפשרות **הגבלה ל-Gemini API בלבד**.
4. לוחצים על **הגבלת המפתח** כדי לאשר.

#### שיטה ב': הגבלת המפתח לשירותים אחרים (מסוף Google Cloud)

אם המפתח משותף עם ממשקי Google API אחרים (לא מומלץ), צריך להגביל אותו במסוף Cloud. **הערה: בקשות ל-Gemini API באמצעות המפתח הזה ייכשלו אחרי החלת ההגבלות האלה.**

1. נכנסים אל [הדף Credentials במסוף Google Cloud](https://console.cloud.google.com/apis/credentials?hl=he).
2. בוחרים את הפרויקט ואת מפתח ה-API.
3. בקטע **API restrictions** (הגבלות על ממשקי API), משתמשים בתפריט הנפתח **Select API restrictions** (בחירת הגבלות על ממשקי API) כדי לבחור את ממשקי ה-API שאליהם המפתח הזה יוכל לגשת. לא בוחרים באפשרות **Generative Language API**.
4. לוחצים על **שמירה**. כדי להמשיך להשתמש ב-Gemini API, צריך ליצור מפתח נפרד ומוגבל ב-AI Studio.

### חסימה של מפתחות לא פעילים

החל מ-7 במאי 2026, Gemini API יחסום מפתחות API ללא הגבלות שלא נעשה בהם שימוש במשך תקופה ארוכה. המפתחות האלה מופיעים עם התג **חסום** ב-AI Studio. כדי להמשיך, צריך ליצור מפתח חדש או להשתמש במפתח קיים עם הגבלות.

## מעבר למפתח אימות

כדי ליצור מפתח API חדש לאימות ולעדכן את האפליקציות:

1. עוברים אל [דף מפתחות ה-API של AI Studio](https://aistudio.google.com/api-keys?hl=he).
2. בודקים את העמודה **סוג המפתח** כדי לזהות מפתחות שמופיעים כ**רגילים**.
3. לוחצים על **Create API key** (יצירת מפתח API) כדי ליצור מפתח חדש. כל המפתחות החדשים שנוצרים ב-AI Studio נוצרים אוטומטית כמפתחות אימות.
4. מעתיקים את מפתח ה-API החדש לאימות.
5. מעדכנים את קוד האפליקציה, את משתני הסביבה ואת כל הגדרות הפריסה כך שישתמשו במפתח ה-API החדש לאימות.
6. בודקים את האפליקציה כדי לוודא שהיא פועלת בצורה תקינה עם המפתח החדש.
7. אחרי האימות, מוחקים או מבטלים את מפתח התעבורה הישן כדי למנוע שימוש לרעה.

## מגבלות

ב-Google AI Studio יש את המגבלות הבאות על ניהול פרויקטים ומפתחות:

- אפשר ליצור עד 10 פרויקטים בכל פעם מדף **Projects** ב-Google AI Studio.
- בדפים **API keys** ו-**Projects** מוצגים עד 100 מפתחות ו-50 פרויקטים.
- מוצגים רק מפתחות API שלא הוגבלו או שהוגבלו ספציפית ל-Generative Language API ‏ (Gemini API).

לניהול מתקדם של פרויקטים או לשינוי מפתחות עם הגבלות אחרות, אפשר להשתמש ב[דף פרטי הכניסה במסוף Google Cloud](https://console.cloud.google.com/apis/credentials?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
