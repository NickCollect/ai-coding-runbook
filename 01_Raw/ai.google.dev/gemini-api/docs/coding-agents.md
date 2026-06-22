---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=he
fetched_at: 2026-06-22T06:32:37.951513+00:00
title: "\u05d4\u05d2\u05d3\u05e8\u05ea \u05e2\u05d5\u05d6\u05e8 \u05ea\u05db\u05e0\u05d5\u05ea \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Gemini MCP \u05d5-Skills \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# הגדרת עוזר תכנות באמצעות Gemini MCP ו-Skills

עוזרים מבוססי-AI לכתיבת קוד הם כלים יעילים, אבל יש להם מגבלות – נתוני האימון שלהם מוגבלים לתאריך מסוים, ולכן הם לא כוללים תכונות ושינויים חדשים בממשקי API. ללא גישה למסמכים ספציפיים ל-Gemini, יכול להיות שהסוכנים יציעו דפוסים כלליים במקום גישות אופטימליות.

כדי שהעוזר האישי לתכנות יהיה מעודכן ב-Gemini API המתפתח ובשימוש המומלץ בו, מומלץ להגדיר את **Gemini Docs MCP** ולשפר את הסביבה באמצעות **Gemini API Skills**. אפשר להשתמש בכל אחד מהכלים האלה בנפרד, אבל הם נועדו לעבוד יחד כדי לספק כיסוי מלא.

## חיבור Gemini Docs MCP

‫Gemini מארח שרת Model Context Protocol‏ (MCP) ציבורי בכתובת `https://gemini-api-docs-mcp.dev`. חיבור סוכן התכנות לשרת הזה מבטיח שלכל השאילתות תהיה גישה לממשקי ה-API העדכניים, לעדכוני הקוד ולדוגמאות אופטימליות להגדרות.

כדי להתקין את השרת, מריצים את הפקודה הבאה בטרמינל של הסוכן או בשורש הפרויקט:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

השרת הזה מוסיף פונקציה `search_documentation` שהסוכן יכול להשתמש בה כדי לאחזר הגדרות API ודפוסי שילוב בזמן אמת מקובצי התיעוד הרשמיים של Gemini.

## הוספת מיומנויות פיתוח API

הכישורים מספקים **כללים ושיטות מומלצות מובנים** (כמו אכיפה של גרסאות ה-SDK והמודל הנכונות) ישירות בהקשר של העוזר הדיגיטלי. היכולת פועלת יחד עם שירות ה-MCP של Gemini Docs: אם התקנתם את שניהם, היכולת משתמשת בשירות ה-MCP לתיעוד, אבל גם אם לא התקנתם את ה-MCP, היא תאחזר את `llms.txt` מ-`ai.google.dev` כחלופה.

כדי להתקין את המיומנויות האלה, אפשר להשתמש באחד מהכלים הנתמכים הבאים. הוראות ההתקנה של שניהם מופיעות מתחת לכל מודול מיומנות:

- ‫**[skills.sh](https://skills.sh)**: מומלץ. התקן הפתוח להתנהגויות ניידות של סוכנים.
- ‫**[Context7](https://context7.com)**: נתמך עבור משתמשים שכבר משתמשים במערכת האקולוגית של Context7.

### gemini-api-dev

מיומנות בסיסית לפיתוח ב-Gemini למטרות כלליות. במאמר הזה מפורטות שיטות מומלצות וקישורים למסמכים בנושאים הבאים:

- ניתוב הנחיות למודלים עדכניים (לדוגמה, Gemini 3.1 Pro/Flash) והימנעות ממודלים שיצאו משימוש
- כתיבת הנחיות מולטי-מודאליות, שימוש בפונקציות, פלט מובנה ודפוסי שילוב נפוצים

#### התקנה באמצעות skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### הטמעה באמצעות Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

מיומנות בפיתוח אפליקציות AI בממשק שיחה בזמן אמת באמצעות Gemini Live API. במאמר הזה מפורטות שיטות מומלצות וקישורים למסמכים בנושאים הבאים:

- חיבורי WebSocket לסטרימינג עם השהיה נמוכה
- סטרימינג של אודיו, וידאו וטקסט
- זיהוי פעילות קולית ותמיכה בהתפרצות לשיחה

#### התקנה באמצעות skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### הטמעה באמצעות Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

מיומנות בפיתוח אפליקציות באמצעות [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he). ‫Interactions API הוא ממשק מאוחד לאינטראקציה עם מודלים וסוכנים של Gemini, שמיועד לאפליקציות שמבוססות על סוכנים. המיומנות הזו כוללת:

- יצירת טקסט, שיחה עם זיכרון וסטרימינג
- בקשה להפעלת פונקציה, פלט מובנה ויצירת תמונות
- ביצוע ברקע וסוכני Deep Research
- ניהול מצב השיחה בצד השרת
- דפוסי SDK ב-Python וב-TypeScript

#### התקנה באמצעות skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### הטמעה באמצעות Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## אימות התקנה

אחרי ההתקנה, צריך לוודא שעוזר התכנות יכול להתחבר לשרת ה-MCP של Gemini Docs ולהשתמש במיומנויות שהתקנתם.

### 1. אימות התנהגות הנציג

הדרך הכי אמינה לאמת היא לשאול את הנציג שאלה טכנית לגבי Gemini API.

**הנחיה:** "איך משתמשים בשמירת מטמון של הקשר עם Gemini API?"

הגדרה מוצלחת תאפשר לכם:

- **מספקים קוד מדויק**: מפנים לשיטות ספציפיות של Gemini כמו `cacheContent` או `cachedContents.create` מנקודות הקצה העדכניות.
- **שימוש בכלי MCP**: צריך להראות שהוא מחובר ל**שרת ה-MCP של Gemini Docs** או שהוא משתמש בכלי `search_documentation` כדי לאחזר נתונים.
- **הפעלת מיומנויות שנטענו**: הצגת אינדיקטור של 'שימוש במיומנות: gemini-api-dev' (אם מסתמכים על wrapper משני).

### 2. אימות המניפסטים והכלים

אם הסוכן נותן תשובה כללית או גנרית, משתמשים בפקודות הספציפיות Discovery או Status עבור הסביבה שלכם כדי לוודא שה-Docs MCP או המיומנות נטענו לזיכרון.

| סביבה | אימות MCP | אימות כישורים |
| --- | --- | --- |
| **Claude Code** | מקלידים `/mcp` בטרמינל כדי לראות את השרתים הפעילים ואת כלי `search_documentation`. | מקלידים `/skills` במסוף כדי לראות רשימה של כל קובצי המניפסט הפעילים. |
| **Cursor** | עוברים אל **הגדרות > תכונות > MCP**. מוודאים שהשרת מחובר. | פותחים את **ההגדרות > כללים**. מוודאים שהמיומנות מופיעה בקטע 'הסוכן מחליט'. |
| **Antigravity** | בודקים את סטטוס ה-MCP בסרגל הצד **התאמות אישיות > חיבורים**. | מקלידים `/skills list` או מסמנים את סרגל הצד **התאמות אישיות > כללים**. |
| ‫**Gemini CLI** | מריצים את `gemini mcp list` או משתמשים ב-`/mcp list`. | מריצים את הפקודה `gemini skills list` או משתמשים בפקודה דרך שורת הפקודות `/skills` במהלך הפגישה. |
| **Copilot** | מקלידים `@gemini /mcp` כדי לראות רשימה של מחברים פעילים לנתונים. | מקלידים `@gemini /skills` (או `/skills`) כדי לראות את התוספים הפעילים. |

## פתרון בעיות

אם הסוכן שלכם מספק רק מידע כללי או לא מזהה שיטות ספציפיות ל-Gemini, כדאי לבדוק את הדברים הבאים:

### הסוכן לא זיהה את המיומנות

רוב הסוכנים מוסיפים לאינדקס את הכישורים רק בהפעלה.

**תיקון:** מפעילים מחדש את סביבת הפיתוח המשולבת (IDE) (Cursor/VS Code) או יוצאים מהסוכן מבוסס-הטרמינל (Claude Code) ופותחים אותו מחדש.

### סכסוך גלובלי לעומת סכסוך מקומי

אם התקנתם באמצעות הדגל `--global`, יכול להיות שהסוכן מתעלם ממנו לטובת כללים ספציפיים לפרויקט.

**פתרון:** נסו להתקין את היכולת ישירות בתיקיית הבסיס של הפרויקט בלי הדגל global:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## משאבים

- [מיומנויות של Gemini API ב-GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he)
- [מדריך למתחילים](https://ai.google.dev/gemini-api/docs/quickstart?hl=he)
- [ספריות](https://ai.google.dev/gemini-api/docs/libraries?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-19 (שעון UTC)."],[],[]]
