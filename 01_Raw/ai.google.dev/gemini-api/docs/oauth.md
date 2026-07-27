---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=he
fetched_at: 2026-07-27T04:44:57.967263+00:00
title: "\u05d0\u05d9\u05de\u05d5\u05ea \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea \u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05de\u05ea\u05d7\u05d9\u05dc\u05d9\u05dd \u05e9\u05dc OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# אימות באמצעות מדריך למתחילים של OAuth

הדרך הכי קלה לבצע אימות ל-Gemini API היא להגדיר מפתח API, כמו שמתואר ב[מדריך לתחילת העבודה עם Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=he). אם אתם צריכים אמצעי בקרה מחמירים יותר על הגישה, אתם יכולים להשתמש ב-OAuth במקום זאת. המדריך הזה יעזור לכם להגדיר אימות באמצעות OAuth.

במדריך הזה נשתמש בגישה פשוטה לאימות, שמתאימה לסביבת בדיקה. בסביבת ייצור, מומלץ לקרוא על [אימות והרשאה](https://developers.google.com/workspace/guides/auth-overview?hl=he) לפני [שבוחרים את פרטי הגישה](https://developers.google.com/workspace/guides/create-credentials?hl=he#choose_the_access_credential_that_is_right_for_you) שמתאימים לאפליקציה שלכם.

## מטרות

- הגדרת פרויקט בענן ל-OAuth
- הגדרה של Application Default Credentials
- ניהול פרטי הכניסה בתוכנית במקום שימוש ב-`gcloud auth`

## דרישות מוקדמות

כדי להפעיל את המדריך למתחילים הזה, אתם צריכים:

- [פרויקט ב-Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=he)
- [התקנה מקומית של ה-CLI של gcloud](https://cloud.google.com/sdk/docs/install?hl=he)

## הגדרת הפרויקט בענן

כדי להשלים את המדריך למתחילים הזה, קודם צריך להגדיר את פרויקט הענן.

### 1. הפעלת ה-API

לפני שאתם משתמשים בממשקי Google API, אתם צריכים להפעיל אותם בפרויקט ב-Google Cloud.

- במסוף Google Cloud, מפעילים את Google Generative Language API.

  [להפעלת ה-API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=he)

### 2. מגדירים את מסך ההסכמה של OAuth

בשלב הבא מגדירים את מסך ההסכמה ל-OAuth של הפרויקט ומוסיפים את עצמכם כמשתמש לבדיקה. אם כבר ביצעתם את השלב הזה בפרויקט בענן שלכם, אתם יכולים לדלג לקטע הבא.

1. במסוף Google Cloud, לוחצים על **תפריט** > **פלטפורמת אימות של Google** > **סקירה כללית**.

   [מעבר לפלטפורמת האימות של Google](https://console.developers.google.com/auth/overview?hl=he)
2. ממלאים את טופס הגדרת הפרויקט ומגדירים את סוג המשתמש ל**External** (חיצוני) בקטע **Audience** (קהל).
3. ממלאים את שאר השדות בטופס, מאשרים את התנאים של המדיניות בנושא נתוני משתמשים ולוחצים על **יצירה**.
4. כרגע אתם יכולים לדלג על הוספת היקפי הרשאות וללחוץ על **שמירה והמשך**. בעתיד, כשתיצרו אפליקציה לשימוש מחוץ לארגון שלכם ב-Google Workspace, תצטרכו להוסיף ולאמת את היקפי ההרשאות שהאפליקציה דורשת.
5. הוספת משתמשי בדיקה:

   1. עוברים אל [דף הקהל](https://console.developers.google.com/auth/audience?hl=he) של פלטפורמת אימות Google.
   2. בקטע **משתמשי בדיקה**, לוחצים על **הוספת משתמשים**.
   3. מזינים את כתובת האימייל שלכם ושל משתמשים מורשים אחרים לבדיקה, ואז לוחצים על **שמירה**.

### 3. מאשרים את פרטי הכניסה של האפליקציה למחשב

כדי לבצע אימות כמשתמש קצה ולגשת לנתוני משתמשים באפליקציה, צריך ליצור מזהה לקוח אחד או יותר ב-OAuth 2.0. מזהה הלקוח משמש לזיהוי של אפליקציה אחת בשרתי OAuth של Google. אם האפליקציה פועלת בכמה פלטפורמות, צריך ליצור מזהה לקוח נפרד לכל פלטפורמה.

1. במסוף Google Cloud, לוחצים על **תפריט** > **פלטפורמת האימות של Google** > **לקוחות**.

   [לדף Credentials](https://console.developers.google.com/auth/clients?hl=he)
2. לוחצים על **Create Client**.
3. לוחצים על **Application type** > **Desktop app**.
4. בשדה **Name**, מקלידים שם לפרטי הכניסה. השם הזה מוצג רק במסוף Google Cloud.
5. לוחצים על **יצירה**. מופיע מסך עם לקוח OAuth שנוצר, שבו מוצגים מזהה הלקוח וסוד הלקוח החדשים.
6. לוחצים על **אישור**. פרטי הכניסה החדשים שנוצרו מופיעים בקטע **מזהי לקוח OAuth 2.0**.
7. לוחצים על לחצן ההורדה כדי לשמור את קובץ ה-JSON. הוא יישמר בשם `client_secret_<identifier>.json`. משנים את השם שלו ל-`client_secret.json` ומעבירים אותו לספריית העבודה.

## הגדרת Application Default Credentials

כדי להמיר את הקובץ `client_secret.json` לפרטי כניסה שניתן להשתמש בהם, מעבירים את המיקום שלו לארגומנט `--client-id-file` של הפקודה `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

ההגדרה הפשוטה של הפרויקט במדריך הזה מפעילה את תיבת הדו-שיח **"Google לא אימתה את האפליקציה הזו"**. זה מצב תקין, לוחצים על **"המשך"**.

הפעולה הזו מציבה את האסימון שמתקבל במיקום מוכר, כך שניתן לגשת אליו באמצעות `gcloud` או ספריות הלקוח.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

אחרי שמגדירים את Application Default Credentials‏ (ADC), ספריות הלקוח ברוב השפות לא צריכות עזרה כדי למצוא אותן, או שהן צריכות עזרה מינימלית.

### Curl

הדרך הכי מהירה לבדוק שהיא פועלת היא להשתמש בה כדי לגשת ל-REST API באמצעות curl:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

ב-Python, ספריות הלקוח אמורות למצוא את פרטי הכניסה באופן אוטומטי:

```
pip install google-genai
```

סקריפט מינימלי לבדיקה יכול להיות:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## השלבים הבאים

אם זה עובד, אפשר לנסות [אחזור סמנטי של נתוני הטקסט](https://ai.google.dev/docs/semantic_retriever?hl=he).

## ניהול פרטי הכניסה באופן עצמאי [Python]

במקרים רבים, הפקודה `gcloud` לא תהיה זמינה ליצירת אסימון הגישה ממזהה הלקוח (`client_secret.json`). Google מספקת ספריות בשפות רבות כדי לאפשר לכם לנהל את התהליך הזה בתוך האפליקציה. בקטע הזה מוצג התהליך ב-Python. דוגמאות מקבילות לסוג הזה של הליך, בשפות אחרות, זמינות ב[מסמכי התיעוד של Drive API](https://developers.google.com/drive/api/quickstart/python?hl=he).

### 1. התקנת הספריות הנדרשות

מתקינים את ספריית הלקוח של Google ל-Python ואת ספריית הלקוח של Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. כתיבה של מנהל פרטי הכניסה

כדי לצמצם את מספר הפעמים שצריך ללחוץ על מסכי ההרשאה, יוצרים קובץ בשם `load_creds.py` בספריית העבודה כדי לשמור במטמון קובץ `token.json` שאפשר לעשות בו שימוש חוזר בהמשך, או לרענן אותו אם הוא פג.

מתחילים עם הקוד הבא כדי להמיר את הקובץ `client_secret.json` לטוקן שאפשר להשתמש בו עם `genai.configure`:

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. כתיבת התוכנית

עכשיו יוצרים את `script.py`:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. הפעלת התוכנית

בספריית העבודה, מריצים את הדוגמה:

```
python script.py
```

בפעם הראשונה שמריצים את הסקריפט, נפתח חלון דפדפן ומופיעה בקשה לאשר גישה.

1. אם לא התחברתם לחשבון Google שלכם, תתבקשו להיכנס אליו. אם אתם מחוברים לכמה חשבונות, **חשוב לבחור את החשבון שהגדרתם כ'חשבון בדיקה' כשאתם מגדירים את הפרויקט.**
2. פרטי ההרשאה מאוחסנים במערכת הקבצים, כך שבפעם הבאה שתריצו את הקוד לדוגמה, לא תתבקשו להעניק הרשאה.

הגדרת האימות בוצעה בהצלחה.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-01 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-01 (שעון UTC)."],[],[]]
