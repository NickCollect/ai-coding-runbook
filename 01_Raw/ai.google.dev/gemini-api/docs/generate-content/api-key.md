---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-key?hl=he
fetched_at: 2026-11-02T07:10:07.860602+00:00
title: "\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1\u05de\u05e4\u05ea\u05d7\u05d5\u05ea API \u05e9\u05dc Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# שימוש במפתחות API של Gemini

כדי להשתמש ב-Gemini API, אתם צריכים לאמת את הבקשות שלכם. אתם יכולים לבצע אימות באמצעות מפתח API רגיל או מפתח API להרשאה.

[יצירה או הצגה של מפתח Gemini API](https://aistudio.google.com/apikey?hl=he)

## סוגי מפתחות API: רגיל לעומת הרשאה

מפתחות API מספקים גישה ל-Gemini API, אבל מאפייני האבטחה שלהם שונים. כדי לשפר את האבטחה, Gemini API עובר ממפתחות API רגילים למפתחות הרשאה:

- **מפתחות API רגילים**: משייכים בקשות לפרויקט ב-Google Cloud לצורכי חיוב ומכסה. מפתחות רגילים לא מזהים את הגורם שקורא ל-API, ולכן הם לא תומכים ברמת פירוט גבוהה של הרשאות ובקרת גישה.
- **מפתחות הרשאה (auth)**: מקושרים ישירות לחשבון שירות ב-Google Cloud. כשמשתמשים במפתח הרשאה, הבקשות מעובדות בזהות של חשבון השירות המקושר, וכך אפשר להגדיר בקרת גישה ברמה מפורטת. כברירת מחדל, מפתחות הרשאה מוגבלים ל-Generative Language API (‏Gemini API) ומספקים אכיפה מהירה של מפתחות שדלפו, כדי להפסיק במהירות את השימוש במפתחות שדלפו וזוהו על ידי המערכות שלנו.

כדי להבטיח שימוש מאובטח, Gemini API יעבור ממפתחות רגילים למפתחות אימות:

- **מפתחות אימות כברירת מחדל**: החל מ-28 במאי 2026, כל מפתחות ה-API החדשים שנוצרים ב-Google AI Studio נוצרים באופן אוטומטי כמפתחות אימות.
- **דחיית מפתחות לא מוגבלים**: Gemini API דוחה בקשות מ**מפתחות רגילים לא מוגבלים**. מפתחות API רגילים שהוחלו עליהם הגבלות מפורשות ממשיכים לפעול. ההגבלה הזו מונעת שימוש לא מורשה במפתחות ששותפו באופן ציבורי או קושרו לשירותים אחרים.

## ניהול מפתחות API ב-Google AI Studio

אתם יכולים לנהל את הפרויקטים והמפתחות ישירות ב-[Google AI Studio](https://aistudio.google.com/apikey?hl=he).

### פרויקטים ב-Google Cloud

כל מפתח Gemini API משויך ל[פרויקט ב-Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=he).
בפרויקטים ב-Google Cloud מנהלים את החיוב, את שותפי העריכה ואת ההרשאות. ב-Google AI Studio יש ממשק פשוט שמאפשר לגשת לפרויקטים האלה.

- **פרויקט ברירת מחדל**: אם אתם משתמשים חדשים, אחרי שתאשרו את התנאים וההגבלות, מערכת Google AI Studio תיצור באופן אוטומטי פרויקט בענן ב-Google Cloud ומפתח API שיוגדרו כברירת מחדל. כדי לשנות את שם הפרויקט, עוברים לתצוגה **Projects** בלוח הבקרה.
- **פרויקטים קיימים**: אם כבר יש לכם חשבון Google Cloud, מערכת AI Studio לא יוצרת פרויקט כברירת מחדל. במקום זאת, צריך לייבא את הפרויקטים הקיימים.

### ייבוא פרויקטים

כברירת מחדל, ב-Google AI Studio לא מוצגים כל הפרויקטים שלכם ב-Google Cloud. צריך לייבא את הפרויקטים שרוצים להשתמש בהם:

1. עוברים אל [Google AI Studio](https://aistudio.google.com?hl=he).
2. פותחים את **לוח הבקרה** מהחלונית הימנית ובוחרים באפשרות **פרויקטים**.
3. לוחצים על הכפתור **ייבוא פרויקטים**.
4. מחפשים את פרויקט הענן ב-Google Cloud שרוצים לייבא, בוחרים אותו ולוחצים על **Import**.
5. אחרי הייבוא, נכנסים לדף **מפתחות API** במרכז הבקרה כדי ליצור מפתח בפרויקט הזה.

### פתרון בעיות בהרשאות ליצירת מפתחות

אם הלחצן **Create API key** לא זמין ומוצגת ההודעה *"You do not have permission to create a key in this project"*, סימן שאין לכם את הרשאות ה-IAM הנדרשות.

מבקשים מהאדמין של פרויקט בענן או מנהל חשבון ארגוני ב-Google Cloud להקצות לכם תפקיד שכולל את ההרשאות הבאות (למשל, עריכת פרויקטים):

- ‫`resourcemanager.projects.get`: מאפשר ל-AI Studio לאמת את הפרויקט.
- ‫`apikeys.keys.create`: מאפשרת ליצור מפתחות.
- ‫`serviceusage.services.enable`: מוודא ש-Generative Language API מופעל.
- ‫`iam.serviceAccounts.create`: נדרש כדי ליצור את חשבון השירות המקושר.
- ‫`iam.serviceAccountApiKeyBindings.create`: מקשר את חשבון השירות למפתח ה-API.

אם אתם לא יכולים לקבל הרשאת אדמין, אתם יכולים ליצור פרויקט חדש ב-Google Cloud שלא משויך לארגון כדי ליצור את המפתחות.

### מפתחות לא ידועים בדף "שימוש"

ב[דף Usage](https://aistudio.google.com/usage?hl=he) ב-Google AI Studio, בקשות שלא תואמות למפתח API עם שם בפרויקט מקובצות בקטע **(unknown keys)**. הנתונים כוללים מפתחות שנמחקו לפני יותר מ-30 יום, מפתחות ללא שם מוצג ובקשות שבוצעו באמצעות פרטי כניסה אחרים, כמו OAuth.

## יצירת מפתחות במסוף Google Cloud

ב-Google AI Studio מוצגים רק מפתחות ללא הגבלה או מפתחות שמוגבלים ל-Gemini API. אם אתם לא יכולים להשתמש ב-AI Studio, או אם אתם רוצים לנהל את כל מפתחות ה-API במקום אחד, פועלים לפי ההוראות במאמר העזרה של Cloud בנושא [יצירת מפתח API](https://cloud.google.com/docs/authentication/api-keys?hl=he#create). כדי ליצור מפתח API ל-Gemini, צריך לקשר אותו ל[חשבון שירות](https://cloud.google.com/iam/docs/service-account-overview?hl=he).

## הגדרת הסביבה

אחרי שיש לכם מפתח, אתם צריכים להגדיר את הסביבה כך שתשתמש בו בצורה מאובטחת באפליקציות.

### שימוש במשתני סביבה (מומלץ)

מגדירים את משתנה הסביבה `GEMINI_API_KEY` או `GOOGLE_API_KEY`. ספריות הלקוח של Gemini API מזהות את המשתנים האלה ומשתמשות בהם באופן אוטומטי. אם שתיהן מוגדרות, המדיניות `GOOGLE_API_KEY` מקבלת עדיפות.

בוחרים את מערכת ההפעלה כדי להגדיר את המשתנה:

### ‫Linux/macOS – Bash

בודקים אם יש לכם קובץ תצורה של bash:

```
~/.bashrc
```

אם לא, יוצרים קובץ כזה ופותחים אותו:

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

### macOS – Zsh

בודקים אם יש קובץ תצורה של zsh:

```
~/.zshrc
```

אם לא, יוצרים קובץ כזה ופותחים אותו:

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

1. מחפשים את האפשרות Environment Variables (משתני סביבה) בסרגל החיפוש של Windows.
2. בתיבת הדו-שיח System Properties, לוחצים על **Environment Variables**.
3. בקטע **User variables** או **System variables**, לוחצים על **New...‎**.
4. מגדירים את שם המשתנה כ-`GEMINI_API_KEY` ואת הערך כמפתח ה-API שלכם.
5. כדי לשמור את קיצור הדרך, לחץ על **אישור**. פותחים סשן חדש בטרמינל כדי לטעון את המשתנה.

### לספק את מפתח ה-API באופן מפורש בקוד

אפשר להעביר את מפתח ה-API באופן מפורש כשמפעילים את הלקוח. עשו זאת רק אם אתם לא יכולים להשתמש במשתני סביבה.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
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
        "gemini-3.8-flash",
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
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"       -H 'Content-Type: application/json'       -H "x-goog-api-key: YOUR_API_KEY"       -X POST       -d '{
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

## אבטחה וניהול סודות

התייחסו למפתח Gemini API כמו לסיסמה. אם המפתח ייחשף, אנשים אחרים יוכלו לנצל את המכסה של הפרויקט, לגרום לחיובים לא צפויים ולגשת למשאבים פרטיים.

### כללי אבטחה קריטיים

- **שמירה על סודיות המפתחות**: אף פעם אל תכניסו מפתחות API למערכות בקרת מקור כמו Git.
- **אף פעם אל תחשפו מפתחות בצד הלקוח בסביבת הייצור**: אל תטמיעו מפתחות API ישירות באפליקציות לאינטרנט או לנייד. משתמשים יכולים לחלץ מפתחות שקומפלו בקוד בצד הלקוח. כדי לאבטח אפליקציות בצד הלקוח, צריך להפעיל שרת proxy לקצה העורפי שיבצע את הקריאות ל-API בפועל.

### שיטות מומלצות לניהול סודות

- **משתני סביבה**: קריאת מפתחות ממשתני סביבה במקום מקובצי תצורה.
- ‫**Secret Manager**: בסביבת הייצור, כדאי לאחסן את המפתחות במאגר סודי מאובטח כמו [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=he).
- **התראות חיוב**: הגדירו התראות חיוב במסוף Google Cloud כדי לקבל התראה אם יש עלייה חדה בשימוש או בעלויות.

### רשימת משימות לטיפול בדליפה

אם אתם חושדים שמפתח ה-API שלכם דלף:

1. **ליצור מפתח חדש**: יוצרים מפתח חלופי ב-Google AI Studio או במסוף Cloud.
2. **עדכון האפליקציה**: פורסים את הקוד באמצעות המפתח החדש.
3. **השבתה או מחיקה של המפתח שנחשף**: אחרי שמאמתים את המפתח החדש, משביתים את המפתח שנחשף במסוף Cloud. כדי למנוע השבתה של האפליקציה, אל תמחקו את המפתח הישן עד שהמפתח החדש יהיה פעיל לגמרי.
4. **ביקורת על השימוש**: בודקים את יומני החיוב ואת השימוש ב-API במסוף Google Cloud כדי לזהות פעילות לא מורשית.

## הגבלה ואבטחה של המפתחות

הוספת הגבלות למפתחות ה-API מצמצמת את הנזק הפוטנציאלי במקרה שהמפתח נחשף.

### החלת הגבלות על מקור הבקשה

הגבלות על מקורות מגבילות את כתובות ה-IP, האתרים או האפליקציות שיכולים להשתמש במפתח.

1. נכנסים ל[דף פרטי הכניסה במסוף Google Cloud](https://console.cloud.google.com/apis/credentials?hl=he).
2. בוחרים את הפרויקט ולוחצים על השם של מפתח ה-API שרוצים להגביל.
3. בקטע **Application restrictions**, בוחרים באפשרות **כתובות IP** (או בסוג ההגבלה שמתאים לסביבה שלכם).
4. מציינים את כתובות ה-IP או את טווחי הכתובות המותרים ולוחצים על **שמירה**.

### אבטחת מפתחות API רגילים ללא הגבלה

כדי להמשיך להשתמש ב-Gemini API, צריך לאבטח את כל המפתחות הלא מוגבלים.

#### להגביל את המפתח ל-Gemini API רק דרך AI Studio

אם אתם משתמשים במפתח רק ל-Gemini API, אתם יכולים לאבטח אותו ישירות ב-AI Studio:

1. בדף **מפתחות API** ב-[Google AI Studio](https://aistudio.google.com/api-keys?hl=he), מאתרים את המפתחות שמסומנים בתווית **Unrestricted**.
2. מעבירים את העכבר מעל התווית ולוחצים על **הוספת הגבלות** בתיבת הדו-שיח.
3. בוחרים באפשרות **Restrict to Gemini API only**.
4. לוחצים על **הגבלת המפתח** כדי לאשר.

#### הגבלת המפתח לשירותים אחרים באמצעות מסוף Google Cloud

אם המפתח משותף עם ממשקי Google API אחרים (לא מומלץ), צריך להגביל אותו במסוף Cloud. **הערה: אחרי שמחילים את ההגבלות האלה, בקשות ל-Gemini API באמצעות המפתח הזה ייכשלו.**

1. נכנסים ל[דף פרטי הכניסה במסוף Google Cloud](https://console.cloud.google.com/apis/credentials?hl=he).
2. בוחרים את הפרויקט ואת מפתח ה-API.
3. בקטע **API restrictions**, בוחרים באפשרות **Restrict key**.
4. בתפריט הנפתח, בוחרים את ממשקי ה-API שאליהם רוצים לתת גישה באמצעות המפתח הזה. אל תבחרו באפשרות **Generative Language API**.
5. לוחצים על **שמירה**. כדי להמשיך להשתמש ב-Gemini API, צריך ליצור מפתח נפרד ומוגבל ב-AI Studio.

### מפתחות רדומים חסומים

החל מ-7 במאי 2026, Gemini API חוסם מפתחות API לא מוגבלים שלא היו בשימוש במשך תקופה ארוכה. המפתחות האלה מוצגים עם התג **Blocked** ב-AI Studio. כדי להמשיך, צריך ליצור מפתח חדש או להשתמש במפתח קיים עם הגבלות.

## מעבר למפתח אימות

כדי ליצור מפתח API חדש לאימות ולעדכן את האפליקציות:

1. עוברים אל [דף מפתחות ה-API ב-AI Studio](https://aistudio.google.com/api-keys?hl=he).
2. בודקים את העמודה **סוג המפתח** כדי לזהות מפתחות שרשומים כ**רגילים**.
3. כדי ליצור מפתח API חדש, לוחצים על **Create API key**. כל המפתחות החדשים שנוצרים ב-AI Studio נוצרים באופן אוטומטי כמפתחות אימות.
4. מעתיקים את מפתח ה-API החדש לאימות.
5. מעדכנים את קוד האפליקציה, את משתני הסביבה ואת כל הגדרות הפריסה כדי להשתמש במפתח ה-API החדש לאימות.
6. בודקים את האפליקציה כדי לוודא שהיא פועלת כמו שצריך עם המפתח החדש.
7. אחרי האימות, מחקו או בטלו את מפתח התנועה הישן כדי למנוע שימוש לרעה.

## מגבלות

ב-Google AI Studio יש את המגבלות הבאות על ניהול פרויקטים ומפתחות:

- אתם יכולים ליצור עד 10 פרויקטים בו-זמנית בדף **Projects** ב-Google AI Studio.
- בדפים **מפתחות API** ו-**Projects** מוצגים עד 100 מפתחות ו-50 פרויקטים.
- מוצגים רק מפתחות API ללא הגבלה או מפתחות שמוגבלים ספציפית ל-Generative Language API (Gemini API).

כדי לנהל פרויקטים בצורה מתקדמת או לשנות מפתחות עם הגבלות אחרות, צריך להשתמש ב[דף פרטי הכניסה במסוף Google Cloud](https://console.cloud.google.com/apis/credentials?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-10-27 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-10-27 (שעון UTC)."],[],[]]
