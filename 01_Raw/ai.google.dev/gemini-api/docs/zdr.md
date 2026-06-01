---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=he
fetched_at: 2026-06-01T06:05:38.352293+00:00
title: "\u05e9\u05de\u05d9\u05e8\u05ea \u05e0\u05ea\u05d5\u05e0\u05d9\u05dd \u05d0\u05e4\u05e1\u05d9\u05ea \u05d1-Gemini Developer API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שמירת נתונים אפסית ב-Gemini Developer API

בדף הזה מפורטים פרטים על מה שנקרא בדרך כלל 'שמירת נתונים אפסית' ב-Gemini Developer API.

## הגבלת אימון

כפי שמפורט [בתנאים ובהגבלות של Gemini API](https://ai.google.dev/gemini-api/terms?hl=he), כשמשתמשים בשירותים בתשלום, Google לא משתמשת בהנחיות (כולל הוראות מערכת משויכות, תוכן במטמון וקבצים כמו תמונות, סרטונים או מסמכים) או בתשובות כדי לשפר את המוצרים שלה. הגדרת השירותים בתשלום מופיעה [כאן](https://ai.google.dev/gemini-api/terms?hl=he#paid-services).

## שמירת נתוני לקוחות והשגת מצב של אפס שמירת נתונים

בדרך כלל, נתוני הלקוחות נשמרים לפרקי זמן מוגבלים בתרחישים ובתנאים הבאים. כדי להגיע למצב של אפס שמירת נתונים, הלקוחות צריכים לבצע פעולות ספציפיות או להימנע משימוש בתכונות ספציפיות בכל אחד מהתחומים הבאים:

- **רישום ביומן של הנחיות לצורך מעקב אחר שימוש לרעה**: כפי שמתואר [בתנאים והגבלות הנוספים למתן שירות של Gemini API](https://ai.google.dev/gemini-api/terms?hl=he), בשירותים בתשלום, Google רושמת ביומן את ההנחיות והתשובות למשך זמן מוגבל, אך ורק לצורך זיהוי הפרות של [המדיניות בנושא שימוש אסור](https://policies.google.com/terms/generative-ai/use-policy?hl=he). כשהבקשה שלכם ל-ZDR עבור פרויקט מסוים מאושרת, כל תוכן המשתמשים (ההנחיות והתשובות) והמטא-נתונים שניתן לזהות (כמו כתובות IP ומזהי חשבון Google) נמחקים לפני הרישום ביומן. הרשומה שמתקבלת מסומנת כרשומה שעברה סניטציה, והיא לא מכילה מידע מזהה של משתמש. כך נשמרת התאימות עם פלטפורמת הסוכנים של Gemini Enterprise, שבה לא מתבצע שימור נתונים.
- **עיגון באמצעות חיפוש Google**: כמו שמתואר [בתנאים הנוספים של Gemini API](https://ai.google.dev/gemini-api/terms?hl=he#grounding-with-google-search),‏ Google שומרת הנחיות, מידע הקשרי ותוצאות שנוצרו למשך שלושים (30) ימים לצורך יצירת תוצאות מעוגנות והצעות לחיפוש.
  יכול להיות שנשתמש במידע השמור הזה לצורך ניפוי באגים ובדיקות של מערכות שתומכות בהארקה. **אם משתמשים ב-עיגון באמצעות חיפוש Google, אי אפשר להשבית את השמירה של המידע הזה.**
- **עיגון בעזרת מפות Google**: כפי שמפורט [בתנאים ובהגבלות הנוספים של Gemini API](https://ai.google.dev/gemini-api/terms?hl=he),‏ Google מאחסנת הנחיות, מידע הקשרי ותוצאות שנוצרו למשך שלושים (30) ימים לצורך יצירת תוצאות מבוססות. אפשר להשתמש במידע הזה רק לצורך הנדסת אמינות, למשל לצורך ניפוי באגים במקרה של בעיות בשירות.
  **אם משתמשים ב-עיגון בעזרת מפות Google, אין אפשרות להשבית את האחסון של המידע הזה.**
- ‫**Interactions API**: ‏Interactions API מנהל את המצב הפעיל של שיחה כדי לאפשר שיחות מרובות תורות. **כברירת מחדל, ה-API של האינטראקציות מאפשר אחסון של מצב**. כדי להבטיח שלא יישארו עקבות של נתונים, צריך להגדיר במפורש את הפרמטר `store` לערך `false` בבקשות ה-API כדי לבטל את ההסכמה לשמירת מצב ברירת המחדל.
- ‫**Live API**: ממשק API עם שמירת מצב שמאפשר התחברות מחדש בזמן אמת על ידי שמירת מצב השיחה. כדי להשיג אפס שמירת נתונים, **אל תגדירו את SessionResumptionConfig**. אם נוצר כינוי לסשן, מצב השיחה (כולל טקסט, אודיו ווידאו) נשמר למשך עד 24 שעות.
- ‫**File API Storage**: File API מאפשר למשתמשים להעלות נכסים גדולים.
  הקבצים מאוחסנים במצב לא פעיל עד שהמשתמש מוחק אותם או עד שתוקף שלהם פג.
  השימוש ב-File API לא תלוי ברישום ביומן של ZDR. כדי לוודא שלא נשארים נתונים, המשתמשים צריכים למחוק את הקבצים באופן ידני.
- **שמירת הקשר במטמון באופן מפורש**: המשתמשים יכולים לשמור במטמון באופן ידני מערכי נתונים גדולים (למשל, סרטונים ארוכים או ספריות מסמכים) באמצעות השדה `cached_content`. היומנים של הבקשות האלה פועלים לפי מדיניות ההשמטה של ZDR, אבל ההקשר ששמור במטמון מאוחסן עם `ttl` או `expire_time` שהוגדרו על ידי המשתמש. כדי להשיג טביעת רגל של אפס נתונים, אל תשתמשו בתכונה cached\_content.
- **שמירה במטמון בזיכרון באופן מרומז**: כברירת מחדל, מודלים של Gemini שומרים נתונים במטמון בזיכרון כדי להפחית את זמן האחזור ואת העלות למפתחים. הנתונים האלה נמצאים רק ב-RAM (לא במצב מנוחה), מבודדים ברמת הפרויקט, ויש להם TTL של 24 שעות.
  **הפעולה הזו לא מהווה הפרה של מדיניות אפס שמירת נתונים.**

## המאמרים הבאים

- [מידע על המדיניות בנושא שימוש אסור ב-AI גנרטיבי](https://policies.google.com/terms/generative-ai/use-policy?hl=he)
- קוראים את [התנאים וההגבלות הנוספים של Gemini API](https://ai.google.dev/gemini-api/terms?hl=he).
- אם אתם צריכים אמצעי בקרה של ZDR ברמה הארגונית בשירות עצמי, כדאי לעיין [במדריך בנושא שמירת נתונים אפסית בפלטפורמת הסוכנים של Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-28 (שעון UTC)."],[],[]]
