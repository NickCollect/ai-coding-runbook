---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=he
fetched_at: 2026-07-27T04:48:47.091031+00:00
title: "\u05d0\u05e1\u05d8\u05e8\u05d8\u05d2\u05d9\u05d5\u05ea \u05dc\u05e2\u05d9\u05e6\u05d5\u05d1 \u05d4\u05e0\u05d7\u05d9\u05d5\u05ea \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# אסטרטגיות לעיצוב הנחיות

*עיצוב פרומפטים* הוא תהליך של יצירת פרומפטים, או בקשות בשפה טבעית, שמניבים תשובות מדויקות ואיכותיות ממודל שפה.

בדף הזה מוסברים מושגים בסיסיים, אסטרטגיות ושיטות מומלצות שיעזרו לכם להתחיל לכתוב הנחיות כדי להפיק את המרב ממודלים של Gemini AI.

## מדריכים לכתיבת הנחיות בנושאים ספציפיים

רוצים ללמוד עוד אסטרטגיות ספציפיות לכתיבת הנחיות? כדאי לעיין במדריכים הנוספים שלנו לכתיבת הנחיות בנושאים הבאים:

- [יצירת הנחיות עם קובצי מדיה](https://ai.google.dev/gemini-api/docs/files?hl=he#prompt-guide)
- הנחיות ליצירת תמונות באמצעות [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=he#imagen-prompt-guide) ו[יצירת תמונות מקוריות ב-Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=he#prompt-guide)
- [יצירת סרטונים באמצעות הנחיות](https://ai.google.dev/gemini-api/docs/video?hl=he#prompt-guide)

דוגמאות נוספות להנחיות מופיעות ב[גלריית ההנחיות](https://ai.google.dev/gemini-api/prompts?hl=he), שנועדה להציג באופן אינטראקטיבי רבים מהמושגים שמופיעים במדריך הזה.

## הוראות ברורות וספציפיות

דרך יעילה ונוחה להתאים אישית את התנהגות המודל היא לספק לו הוראות ברורות וספציפיות. ההוראות יכולות להיות בצורת שאלה, משימות מפורטות או מורכבות כמו מיפוי של חוויית המשתמש והלך הרוח שלו.

### קלט

קלט הוא הטקסט הנדרש בהנחיה שרוצים שהמודל יספק לו תשובה. קלט יכול להיות שאלה שהמודל עונה עליה (קלט של שאלה), משימה שהמודל מבצע (קלט של משימה), ישות שהמודל פועל עליה (קלט של ישות) או קלט חלקי שהמודל משלים או ממשיך (קלט של השלמה).

| **סוג הקלט** | **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- | --- |
| שאלה | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| משימה | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| ישות | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### השלמה חלקית של קלט

מודלים גנרטיביים של שפה פועלים כמו כלי מתקדם להשלמה אוטומטית. כשמספקים תוכן חלקי, המודל יכול לספק את שאר התוכן או את מה שהוא חושב שהוא המשך של התוכן הזה כתשובה. כשעושים את זה, אם כוללים דוגמאות או הקשר, המודל יכול להתחשב בהם.

בדוגמה הבאה מופיעה הנחיה עם הוראה וקלט של ישות:

|  |
| --- |
| **הנחיה:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **תשובה:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

המודל פעל לפי ההנחיה, אבל לפעמים קשה לכתוב את ההוראות בשפה טבעית, והמודל צריך לפרש אותן.
לדוגמה, התפריט של מסעדה יכול להכיל הרבה פריטים. כדי להקטין את הגודל של תגובת ה-JSON, כדאי להשמיט את הפריטים שלא הוזמנו. במקרה כזה, אפשר לתת דוגמה וקידומת לתשובה ולתת למודל להשלים אותה:

|  |
| --- |
| **הנחיה:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **תשובה:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

שימו לב שהמילה cheeseburger לא נכללה בפלט כי היא לא הייתה חלק מההזמנה.

אפשר לציין את הפורמט של אובייקטים פשוטים של תגובות JSON באמצעות הנחיות, אבל מומלץ להשתמש בתכונה [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) של Gemini API כשמציינים סכימת JSON מורכבת יותר לתגובה.

### מגבלות

מציינים מגבלות לגבי קריאת ההנחיה או יצירת תשובה. אפשר להגיד למודל מה לעשות ומה לא לעשות. לדוגמה, אפשר לציין בהנחיה מגבלה לגבי אורך הסיכום:

|  |
| --- |
| **הנחיה:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **תשובה:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### פורמט התשובה

אתם יכולים לתת הוראות שמציינות את פורמט התשובה. לדוגמה,
אתם יכולים לבקש שהתשובה תהיה בפורמט של טבלה, רשימה עם תבליטים, הצגה עצמית קצרה, מילות מפתח, משפט או פסקה. ההוראה הבאה למערכת מורה למודל להיות יותר שיחתי בתשובה שלו:

|  |
| --- |
| **הוראות מערכת**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **הנחיה**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **תשובה:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### עיצוב התשובות באמצעות אסטרטגיית ההשלמה

[אסטרטגיית ההשלמה](#completion) יכולה לעזור גם בעיצוב התשובה.
בדוגמה הבאה, המודל מתבקש ליצור טיוטה של חיבור:

|  |
| --- |
| **הנחיה:**    ``` Create an outline for an essay about hummingbirds. ```  **תשובה:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

בהנחיה לא צוין פורמט לתוכן, והמודל בחר פורמט בשבילכם. כדי שהמודל יחזיר תוכן בפורמט ספציפי, אפשר להוסיף טקסט שמייצג את תחילת התוכן ולתת למודל להשלים אותו על סמך התבנית שהתחלתם.

|  |
| --- |
| **הנחיה:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **תשובה:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## הנחיות ישירות (Zero-shot) לעומת הנחיות עם כמה דוגמאות (Few-shot)

אתם יכולים לכלול בהנחיה דוגמאות שמראות למודל איך נראית תשובה נכונה. המודל מנסה לזהות דפוסים וקשרים בדוגמאות ומיישם אותם כשהוא יוצר תשובה. הנחיות שמכילות כמה דוגמאות נקראות הנחיות *עם כמה דוגמאות*, והנחיות שלא מכילות דוגמאות נקראות הנחיות *ללא דוגמאות*. הנחיות עם כמה דוגמאות משמשות בדרך כלל כדי להסדיר את הפורמט, הניסוח, ההיקף או הדפוס הכללי של תשובות המודל. כדאי להשתמש בדוגמאות ספציפיות ומגוונות כדי לעזור למודל לצמצם את המיקוד שלו וליצור תוצאות מדויקות יותר.

מומלץ תמיד לכלול בדחיפות דוגמאות של few-shot. דחיפות ללא דוגמאות של few-shot צפויות להיות פחות יעילות. למעשה, אפשר להסיר את ההוראות מהדחיפה אם הדוגמאות מבהירות מספיק את המשימה.

ההנחיה הבאה היא הנחיית zero-shot שבה המודל מתבקש לבחור את ההסבר הטוב ביותר.

|  |
| --- |
| **הנחיה:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **תשובה:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

אם תרצו שהמודל יפיק תשובות תמציתיות, תוכלו לכלול בהנחיה דוגמאות שמראות שהתשובות צריכות להיות תמציתיות.

ההנחיה הבאה מספקת שתי דוגמאות שבהן מוצגת העדפה להסברים קצרים יותר. בתגובה, אפשר לראות שהדוגמאות הנחו את המודל לבחור בהסבר הקצר יותר (`Explanation2`) ולא בהסבר הארוך יותר (`Explanation1`) כמו שהוא עשה קודם.

|  |
| --- |
| **הנחיה:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **תשובה:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### מספר הדוגמאות האופטימלי

מודלים כמו Gemini יכולים לזהות דפוסים באמצעות כמה דוגמאות, אבל יכול להיות שתצטרכו להתנסות במספר הדוגמאות שאתם מספקים בהנחיה כדי לקבל את התוצאות הכי טובות. יחד עם זאת, אם תכללו יותר מדי דוגמאות, יכול להיות שהמודל יתחיל [להתאים יתר על המידה](https://developers.google.com/machine-learning/glossary?hl=he#overfitting) את התשובה לדוגמאות.

### עיצוב עקבי

כדי למנוע תשובות בפורמטים לא רצויים, חשוב לוודא שהמבנה והפורמט של הדוגמאות עם ההסברים הזהים. אחת המטרות העיקריות של הוספת דוגמאות בשיטת ה-few-shot בהנחיות היא להראות למודל את פורמט התשובה. לכן, חשוב לוודא שהפורמט עקבי בכל הדוגמאות, ובמיוחד לשים לב לתגי XML, לרווחים, למעברי שורה ולמפרידי הדוגמאות.

## הוספת הקשר

אתם יכולים לכלול בהנחיה הוראות ומידע שהמודל צריך כדי לפתור בעיה, במקום להניח שלמודל יש את כל המידע הנדרש. המידע ההקשרי הזה עוזר למודל להבין את האילוצים והפרטים של מה שאתם מבקשים ממנו לעשות.

בדוגמה הבאה, המודל מתבקש לספק הנחיות לפתרון בעיות בנתב:

|  |
| --- |
| **הנחיה:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **תשובה:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

התשובה נראית כמו מידע כללי לפתרון בעיות שלא ספציפי לנתב או לסטטוס של נוריות ה-LED.

כדי להתאים אישית את התשובה לנתב הספציפי, אפשר להוסיף להנחיה את מדריך פתרון הבעיות של הנתב כהקשר שאליו כדאי להתייחס כשמספקים תשובה.

|  |
| --- |
| **הנחיה:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **תשובה:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## פירוק ההנחיות לרכיבים

בתרחישי שימוש שבהם נדרשות הנחיות מורכבות, אפשר לפשט את המודל על ידי פירוק הדברים לרכיבים פשוטים יותר.

1. **פירוט ההוראות:** במקום לכתוב הרבה הוראות בהנחיה אחת, כדאי ליצור הנחיה אחת לכל הוראה. אתם יכולים לבחור איזו הנחיה לעבד על סמך הקלט של המשתמש.
2. **שרשור הנחיות:** למשימות מורכבות שכוללות כמה שלבים עוקבים,
   אפשר להפוך כל שלב להנחיה ולשרשר את ההנחיות ברצף. בשרשרת הרציפה הזו של הנחיות, הפלט של הנחיה אחת ברצף הופך לקלט של ההנחיה הבאה. הפלט של ההנחיה האחרונה ברצף
   הוא הפלט הסופי.
3. **תשובות מצטברות:** צבירה היא מצב שבו רוצים לבצע משימות מקבילות שונות בחלקים שונים של הנתונים, ולצבור את התוצאות כדי ליצור את הפלט הסופי. לדוגמה, אפשר להנחות את המודל לבצע פעולה אחת בחלק הראשון של הנתונים, לבצע פעולה אחרת בשאר הנתונים ולצבור את התוצאות.

## ניסוי עם פרמטרים של מודל

כל קריאה ששולחים למודל כוללת ערכי פרמטרים שקובעים איך המודל יוצר תגובה. המודל יכול ליצור תוצאות שונות עבור ערכי פרמטרים שונים. כדאי להתנסות עם ערכי פרמטרים שונים כדי לקבל את הערכים הכי טובים למשימה. הפרמטרים שזמינים למודלים שונים עשויים להיות שונים. הפרמטרים הנפוצים ביותר הם:

1. ‫**Max output tokens:** מציין את המספר המקסימלי של טוקנים שאפשר ליצור בתשובה. כל טוקן הוא בערך באורך של ארבעה תווים. ‫100 טוקנים מקבילים בערך ל-60-80 מילים.
2. **טמפרטורה:** הטמפרטורה שולטת במידת האקראיות בבחירת האסימון. רמת האקראיות משמשת לדגימה במהלך תהליך יצירת תשובות, שמתרחש כשמחילים את `topP` ואת `topK`. טמפרטורות נמוכות טובות להנחיות שדורשות תשובה יותר דטרמיניסטית או פחות פתוחה, ואילו טמפרטורות גבוהות יכולות להוביל לתוצאות יותר מגוונות או יצירתיות. רמת אקראיות של 0 היא דטרמיניסטית, כלומר תמיד נבחרת התגובה עם ההסתברות הכי גבוהה.
3. ‫**`topK`:** הפרמטר `topK` משנה את האופן שבו המודל בוחר טוקנים לפלט. ערך של `topK`‏ 1 מציין שהאסימון שנבחר הוא האסימון הסביר ביותר מבין כל האסימונים באוצר המילים של המודל (נקרא גם פענוח חמדני), ואילו ערך של `topK`‏ 3 מציין שהאסימון הבא נבחר מבין 3 האסימונים הסבירים ביותר באמצעות הטמפרטורה. בכל שלב של בחירת טוקנים, מתבצעת דגימה של `topK` הטוקנים עם ההסתברויות הכי גבוהות. לאחר מכן, הטוקנים מסוננים עוד יותר על סמך `topP`, והטוקן הסופי נבחר באמצעות דגימה של הטמפרטורה.
4. ‫**`topP`:** הפרמטר `topP` משנה את האופן שבו המודל בוחר טוקנים לפלט. הטוקנים נבחרים מהסבירות הגבוהה ביותר לסבירות הנמוכה ביותר עד שסכום ההסתברויות שלהם שווה לערך `topP`. לדוגמה, אם ההסתברות של הטוקנים A,‏ B,‏
   ו-C היא 0.3,‏ 0.2 ו-0.1, והערך של `topP` הוא 0.5,
   אז המודל יבחר ב-A או ב-B כטוקן הבא באמצעות רמת האקראיות, ויפסול את C כמועמד. ערך ברירת המחדל של `topP` הוא 0.95.
5. ‫**`stop_sequences`:** הגדרת רצף עצירה כדי להנחות את המודל להפסיק ליצור תוכן. רצף עצירה יכול להיות כל רצף של תווים. כדאי להימנע משימוש ברצף של תווים שעשויים להופיע בתוכן שנוצר.

## אסטרטגיות לחידוד הנחיות

לפעמים צריך לבצע כמה איטרציות של עיצוב הנחיה כדי לקבל באופן עקבי את התשובה שמחפשים. בקטע הזה מפורטות כמה פעולות שאפשר לנסות כשמשפרים את ההנחיות:

1. **שימוש בניסוחים שונים:** שימוש במילים או בניסוחים שונים בהנחיות לרוב יוביל לתשובות שונות מהמודל, גם אם המשמעות של ההנחיות זהה. אם לא קיבלתם את התוצאות שציפיתם להן מההנחיה, נסו לנסח אותה מחדש.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **מעבר למשימה דומה:** אם לא הצלחתם לגרום למודל לפעול לפי ההוראות שנתתם לו למשימה מסוימת, נסו לתת לו הוראות למשימה דומה שתשיג את אותה תוצאה.

   ההנחיה הזו אומרת למודל לסווג ספר באמצעות קטגוריות מוגדרות מראש:

   |  |
   | --- |
   | **הנחיה:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **תשובה:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   התשובה נכונה, אבל המודל לא נשאר בגבולות האפשרויות. אתם רוצים שהמודל ישיב רק עם אחת מהאפשרויות ולא עם משפט מלא. במקרה כזה, אפשר לנסח מחדש את ההוראות כשאלה אמריקאית ולבקש מהמודל לבחור אפשרות.

   |  |
   | --- |
   | **הנחיה:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **תשובה:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **שינוי הסדר של התוכן בהנחיה:** לפעמים הסדר של התוכן בהנחיה משפיע על התשובה. כדאי לנסות לשנות את סדר התוכן ולראות איך זה משפיע על התשובה.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## תשובות חלופיות

תשובת גיבוי היא תשובה שמוחזרת על ידי המודל אם ההנחיה או התשובה מפעילות מסנן בטיחות. דוגמה לתשובה חלופית: "אני לא יכול לעזור בזה, כי אני רק מודל שפה".

אם המודל מגיב בתשובה חלופית, נסו להגדיל את רמת האקראיות.

## הארקה והרצת קוד

‫Gemini יכול להשתמש בכלים כדי להימנע מהזיות בתרחישים שבהם הוא עלול לתת תשובות שגויות.

[עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) מחבר את מודל Gemini לתוכן מהאינטרנט שמתעדכן בזמן אמת, וכדאי להפעיל אותו בכל פעם שהמודל עשוי להזדקק למידע על עובדות לא מוכרות או עדכניות.

[כלי הרצת הקוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) של Gemini מאפשר למודל ליצור ולהריץ קוד Python, וצריך להפעיל אותו בכל פעם שהמודל צריך לבצע פעולות אריתמטיות, ספירה או חישובים.

## Gemini 3

[מודלים של Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-3) מיועדים להסקת מסקנות מתקדמת ולביצוע הוראות. הם מגיבים בצורה הטובה ביותר להנחיות ישירות ומובנות היטב, שמגדירות בבירור את המשימה ואת כל המגבלות. כדי לקבל תוצאות אופטימליות עם Gemini 3, מומלץ לפעול לפי השיטות הבאות:

### עקרונות חשובים לכתיבת הנחיות

- **היו מדויקים וישירים:** ציינו את המטרה שלכם בצורה ברורה ותמציתית. מומלץ להימנע משפה מיותרת או משכנעת מדי.
- **שימוש במבנה עקבי:** כדאי להשתמש בתווים ברורים להפרדה בין חלקים שונים בהנחיה. תגים בסגנון XML (לדוגמה, `<context>`, `<task>`) או כותרות ב-Markdown. בוחרים פורמט אחד ומשתמשים בו באופן עקבי בהנחיה אחת.
- **הגדרת פרמטרים:** הסבירו במפורש כל מונח או פרמטר מעורפל.
- **שליטה ברמת הפירוט של הפלט:** כברירת מחדל, מודלים של Gemini 3 מספקים תשובות ישירות ויעילות. אם אתם צריכים תשובה יותר מפורטת או כזו שמתנהלת כמו שיחה, אתם צריכים לציין את זה במפורש בהוראות.
- **טיפול עקבי בקלט מולטימודאלי:** כשמשתמשים בטקסט, בתמונות, באודיו או בסרטונים, צריך להתייחס אליהם כאל קלט מאותו סוג. חשוב לוודא שההוראות מתייחסות בבירור לכל מודאליות לפי הצורך.
- **תעדוף הוראות קריטיות:** כדאי להוסיף את ההגבלות ההתנהגותיות החשובות, את הגדרות התפקיד (פרסונה) ואת הדרישות לגבי פורמט הפלט בהוראות המערכת או בתחילת ההנחיה למשתמש.
- **מבנה להקשרים ארוכים:** כשמספקים כמויות גדולות של הקשר (למשל, מסמכים, קוד), צריך לספק את כל ההקשר קודם. ממקמים את ההוראות או השאלות הספציפיות *בסוף* ההנחיה.
- **הקשר של נקודת העוגן:** אחרי בלוק גדול של נתונים, כדאי להשתמש במשפט מעבר ברור כדי לקשר בין ההקשר לבין השאילתה, למשל "בהתבסס על המידע שלמעלה...".

### אסטרטגיות של Gemini 3 Flash

- **דיוק של היום הנוכחי:** מוסיפים את הסעיף הבא להוראות המערכת כדי לעזור למודל לשים לב שהיום הנוכחי הוא בשנת 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **דיוק של מועד סיום הידע:** מוסיפים את הסעיף הבא להוראות המערכת כדי שהמודל יהיה מודע למועד סיום הידע שלו:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **ביצועי ההארקה:** כדי לשפר את היכולת של המודל להארקת התשובות בהקשר שסופק, מוסיפים את הסעיף הבא להוראות המערכת (עם עריכות לפי הצורך):

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### שיפור היכולות של הסקת מסקנות ותכנון

מודלים מסדרות Gemini 2.5 ו-3 יוצרים באופן אוטומטי טקסט פנימי של 'חשיבה' כדי לשפר את ביצועי החשיבה הרציונלית. לכן, בדרך כלל אין צורך שהמודל יציג את שלבי החשיבה הרציונלית בתשובה עצמה. לבעיות שדורשות חשיבה רציונלית מורכבת, בקשות פשוטות כמו 'תחשוב טוב לפני שתענה' יכולות לשפר את הביצועים, אבל הן כרוכות בשימוש נוסף בטוקנים של חשיבה.

פרטים נוספים זמינים במאמר בנושא [התהליך של Gemini לחשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he).

### דוגמאות להנחיות מובנות

שימוש בתגים או ב-Markdown עוזר למודל להבחין בין הוראות, הקשר ומשימות.

**דוגמה לפורמט XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**דוגמה לשימוש ב-Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### דוגמה לתבנית שמשלבת שיטות מומלצות

התבנית הזו כוללת את העקרונות המרכזיים לכתיבת הנחיות ל-Gemini 3. חשוב תמיד לחזור על התהליך ולשנות את ההגדרות בהתאם לתרחיש השימוש הספציפי שלכם.

**הוראה למערכת:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**הנחיה למשתמש:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Agentic workflows

בתהליכי עבודה מורכבים של סוכנים, לעיתים קרובות נדרשות הוראות ספציפיות כדי לשלוט באופן שבו המודל מסיק מסקנות, מתכנן ומבצע משימות. למרות ש-Gemini מספק ביצועים כלליים טובים, כדי להשתמש בסוכנים מורכבים צריך לעיתים קרובות להגדיר את האיזון בין עלות החישוב (זמן האחזור והטוקנים) לבין דיוק המשימה.

כשמעצבים הנחיות לסוכנים, כדאי להתייחס למאפייני ההתנהגות הבאים שאפשר להגדיר בסוכן:

### חשיבה רציונלית ואסטרטגיה

הגדרה של אופן החשיבה והתכנון של המודל לפני שהוא מבצע פעולה.

- **פירוק לוגי:** מגדיר את רמת הניתוח של האילוצים, הדרישות המוקדמות וסדר הפעולות.
- **אבחון בעיות**: קובע את עומק הניתוח בזיהוי הסיבות לבעיות ואת השימוש של המודל בהיסק אבדוקטיבי. ההגדרה הזו קובעת אם המודל יקבל את התשובה הכי ברורה או יחפש הסברים מורכבים ופחות סבירים.
- **מידע מקיף:** איזון בין ניתוח של כל המדיניות והמסמכים הזמינים לבין מתן עדיפות ליעילות ולמהירות.

### ביצוע ואמינות

הגדרות לגבי האופן שבו הסוכן פועל באופן אוטונומי ומטפל בבעיות.

- **יכולת הסתגלות:** איך המודל מגיב לנתונים חדשים. ההגדרה הזו קובעת אם המודל צריך לדבוק בתוכנית הראשונית שלו או לשנות אותה באופן מיידי כשהתצפיות סותרות את ההנחות.
- **התמדה ושחזור:** המידה שבה המודל מנסה לתקן שגיאות בעצמו. התמדה גבוהה מגדילה את שיעורי ההצלחה, אבל עלולה להגדיל את עלויות הטוקן או ליצור לולאות.
- **הערכת סיכונים:** הלוגיקה להערכת ההשלכות. ההבדלה בין פעולות חקר בסיכון נמוך (קריאות) לבין שינויים במצב בסיכון גבוה (כתיבות) נעשית באופן מפורש.

### אינטראקציה ופלט

הגדרות לגבי אופן התקשורת של הסוכן עם המשתמש ופורמט התוצאות.

- **טיפול בדו-משמעות ובהרשאות:** ההגדרה הזו קובעת מתי המודל יכול להניח הנחות ומתי הוא צריך להשהות את הביצוע כדי לבקש מהמשתמש הבהרה או הרשאה.
- **רמת הפירוט:** קובעת את נפח הטקסט שנוצר לצד קריאות הכלים. ההגדרה הזו קובעת אם המודל יסביר למשתמש את הפעולות שלו או יישאר שקט במהלך הביצוע.
- **דיוק ושלמות:** רמת הדיוק הנדרשת של הפלט. מציינים אם המודל צריך לפתור כל מקרה קצה ולספק נתונים מדויקים, או אם אפשר להשתמש בהערכות גסות.

### תבנית הוראות למערכת

ההוראה הבאה למערכת היא דוגמה שנבדקה על ידי חוקרים כדי לשפר את הביצועים במדדים של סוכנים שבהם המודל צריך לפעול לפי מערכת מורכבת של כללים ולקיים אינטראקציה עם משתמש. ההנחיה מעודדת את הסוכן לפעול כמתכנן וכמנמק חזק, אוכפת התנהגויות ספציפיות בממדים שמפורטים למעלה ומחייבת את המודל לתכנן מראש לפני ביצוע פעולה כלשהי.

אפשר להתאים את התבנית הזו למגבלות של תרחיש השימוש הספציפי שלכם.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## השלבים הבאים

- עכשיו, אחרי שהבנתם יותר טוב איך לכתוב הנחיות, אתם יכולים לנסות לכתוב הנחיות משלכם באמצעות [Google AI Studio](http://aistudio.google.com?hl=he).
- [מידע נוסף על הנחיות ל-multimodal](https://ai.google.dev/gemini-api/docs/files?hl=he#prompt-guide)
- כדי לקבל מידע על הנחיות ליצירת תמונות, אפשר לעיין במדריכים להנחיות של [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=he#prompt-guide) ושל [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=he#imagen-prompt-guide).
- מידע על הנחיות ליצירת סרטונים זמין ב[מדריך לכתיבת הנחיות של Veo](https://ai.google.dev/gemini-api/docs/video?hl=he#prompt-guide).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-10 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-10 (שעון UTC)."],[],[]]
