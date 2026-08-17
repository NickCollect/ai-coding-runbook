---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=ar
fetched_at: 2026-08-17T02:23:24.228133+00:00
title: "\u0627\u0644\u0645\u0635\u0627\u062f\u0642\u0629 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0627\u0644\u062a\u0634\u063a\u064a\u0644 \u0627\u0644\u0633\u0631\u064a\u0639 \u0644\u0628\u0631\u0648\u062a\u0648\u0643\u0648\u0644 OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# المصادقة باستخدام التشغيل السريع لبروتوكول OAuth

أسهل طريقة للمصادقة على Gemini API هي إعداد مفتاح واجهة برمجة التطبيقات
، كما هو موضّح في دليل البدء في [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=ar). إذا كنت بحاجة إلى عناصر تحكّم أكثر صرامة في الوصول، يمكنك استخدام بروتوكول OAuth بدلاً من ذلك. سيساعدك هذا الدليل في إعداد المصادقة باستخدام بروتوكول OAuth.

يستخدم هذا الدليل طريقة مصادقة مبسطة مناسبة لبيئة الاختبار. بالنسبة إلى بيئة التشغيل الفعلي، يمكنك التعرّف
على
[المصادقة والتفويض](https://developers.google.com/workspace/guides/auth-overview?hl=ar)
قبل
[اختيار بيانات اعتماد الوصول](https://developers.google.com/workspace/guides/create-credentials?hl=ar#choose_the_access_credential_that_is_right_for_you)
المناسبة لتطبيقك.

## الأهداف

- إعداد مشروعك على السحابة الإلكترونية لاستخدام بروتوكول OAuth
- إعداد بيانات الاعتماد التلقائية للتطبيق
- إدارة بيانات الاعتماد في برنامجك بدلاً من استخدام `gcloud auth`

## المتطلبات الأساسية

لتشغيل هذا التشغيل السريع، تحتاج إلى:

- [مشروع على Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=ar)
- [تثبيت محلي لـ gcloud CLI](https://cloud.google.com/sdk/docs/install?hl=ar)

## إعداد مشروعك على السحابة الإلكترونية

لإكمال هذا التشغيل السريع، عليك أولاً إعداد مشروعك على السحابة الإلكترونية.

### 1. تفعيل واجهة برمجة التطبيقات

قبل استخدام واجهات برمجة التطبيقات من Google، عليك تفعيلها في مشروع على Google Cloud.

- في Google Cloud Console، فعِّل Google Generative Language API.

  [تفعيل واجهة برمجة التطبيقات](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=ar)

### 2. إعداد شاشة طلب الموافقة المتعلّقة ببروتوكول OAuth

بعد ذلك، اضبط شاشة طلب الموافقة المتعلّقة ببروتوكول OAuth في المشروع وأضِف نفسك كمستخدم اختبار. إذا سبق لك إكمال هذه الخطوة لمشروعك على السحابة الإلكترونية، انتقِل إلى القسم التالي.

1. في Google Cloud Console، انتقِل إلى **القائمة** > **منصة Google للمصادقة** > **نظرة عامة**.

   [الانتقال إلى منصة Google للمصادقة](https://console.developers.google.com/auth/overview?hl=ar)
2. أكمِل نموذج إعداد المشروع واضبط نوع المستخدم على **خارجي** في قسم **الجمهور**.
3. أكمِل باقي النموذج، واقبل بنود "سياسة بيانات المستخدم"، ثم انقر على **إنشاء**.
4. في الوقت الحالي، يمكنك تخطّي إضافة النطاقات والنقر على **حفظ ومتابعة**. في المستقبل، عند إنشاء تطبيق لاستخدامه خارج مؤسسة Google Workspace، يجب إضافة نطاقات التفويض التي يتطلبها تطبيقك وإثبات ملكيتها.
5. إضافة مستخدمين للاختبار:

   1. انتقِل إلى صفحة
      [الجمهور](https://console.developers.google.com/auth/audience?hl=ar) في
      منصة Google للمصادقة.
   2. ضمن **مستخدمو الاختبار** ، انقر على **إضافة مستخدمين**.
   3. أدخِل عنوان بريدك الإلكتروني وأي مستخدمين آخرين للاختبار تم منحهم الإذن، ثم انقر على **حفظ**.

### 3. السماح ببيانات اعتماد لتطبيق على الكمبيوتر

للمصادقة كمستخدم نهائي والوصول إلى بيانات المستخدم في تطبيقك، عليك إنشاء معرّف عميل واحد أو أكثر لبروتوكول OAuth 2.0. يُستخدم معرّف العميل لتعريف تطبيق واحد لخوادم OAuth من Google. إذا كان تطبيقك يعمل على منصات متعددة، عليك إنشاء معرّف عميل منفصل لكل منصة.

1. في Google Cloud Console، انتقِل إلى **القائمة** > **منصة Google للمصادقة** > **العملاء**.

   [الانتقال إلى بيانات الاعتماد](https://console.developers.google.com/auth/clients?hl=ar)
2. انقر على **إنشاء عميل**.
3. انقر على **نوع التطبيق** > **تطبيق على الكمبيوتر**.
4. في حقل **الاسم** ، اكتب اسمًا لبيانات الاعتماد. لا يظهر هذا الاسم إلا في Google Cloud Console.
5. انقر على **إنشاء**. تظهر شاشة عميل OAuth الذي تم إنشاؤه، وتعرض معرّف العميل الجديد وسر العميل.
6. انقر على **حسنًا**. تظهر بيانات الاعتماد التي تم إنشاؤها حديثًا ضمن **معرّفات عميل OAuth 2.0.**
7. انقر على زر التنزيل لحفظ ملف JSON. سيتم حفظه باسم
   `client_secret_<identifier>.json`، وعليك إعادة تسميته إلى `client_secret.json`
   ونقله إلى دليل العمل.

## إعداد بيانات الاعتماد التلقائية للتطبيق

لتحويل ملف `client_secret.json` إلى بيانات اعتماد قابلة للاستخدام، مرِّر موقعه إلى وسيطة `--client-id-file` في الأمر `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

يؤدي إعداد المشروع المبسّط في هذا البرنامج التعليمي إلى ظهور مربّع حوار **"لم تثبت Google
ملكية هذا التطبيق"**. هذا أمر طبيعي، لذا اختَر **"متابعة"**.

يؤدي ذلك إلى وضع الرمز المميّز الناتج في موقع معروف ليتمكّن `gcloud` أو مكتبات البرامج من الوصول إليه.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

بعد إعداد "بيانات الاعتماد التلقائية للتطبيق" (ADC)، تحتاج مكتبات البرامج في معظم اللغات إلى مساعدة قليلة أو لا تحتاج إلى أي مساعدة للعثور عليها.

### Curl

أسرع طريقة لاختبار ما إذا كان ذلك يعمل هي استخدامه للوصول إلى REST API باستخدام curl:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

في Python، يجب أن تعثر مكتبات البرامج عليها تلقائيًا:

```
pip install google-genai
```

قد يكون النص البرمجي الأدنى للاختبار على النحو التالي:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## الخطوات التالية

إذا كان ذلك يعمل، فأنت مستعد لتجربة
[الاسترجاع الدلالي على بياناتك النصية](https://ai.google.dev/docs/semantic_retriever?hl=ar).

## إدارة بيانات الاعتماد بنفسك [Python]

في حالات كثيرة، لن يكون الأمر `gcloud` متاحًا لك لإنشاء رمز الوصول المميّز من معرّف العميل (`client_secret.json`). توفّر Google مكتبات بلغات عديدة تتيح لك إدارة هذه العملية داخل تطبيقك. يوضّح هذا القسم العملية في Python. تتوفّر أمثلة مكافئة لهذا النوع
من الإجراءات بلغات أخرى في
[مستندات Drive API](https://developers.google.com/drive/api/quickstart/python?hl=ar)

### 1. تثبيت المكتبات الضرورية

ثبِّت مكتبة عميل Google لـ Python ومكتبة عميل Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. كتابة مدير بيانات الاعتماد

لتقليل عدد المرات التي عليك فيها النقر على شاشات التفويض، أنشِئ ملفًا باسم `load_creds.py` في دليل العمل لتخزين ملف `token.json` مؤقتًا يمكنه إعادة استخدامه لاحقًا أو إعادة تحميله إذا انتهت صلاحيته.

ابدأ بالرمز التالي لتحويل ملف `client_secret.json` إلى رمز مميّز قابل للاستخدام مع `genai.configure`:

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

### 3. كتابة برنامجك

الآن، أنشِئ `script.py`:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. تشغيل برنامجك

في دليل العمل، شغِّل النموذج:

```
python script.py
```

في المرة الأولى التي تشغِّل فيها النص البرمجي، ستُفتح نافذة متصفّح ويُطلب منك السماح بالوصول.

1. إذا لم تكن مسجِّلاً الدخول إلى حساب Google، سيُطلب منك هذا. إذا كنت مسجِّلاً الدخول إلى حسابات متعددة، **احرص على اختيار الحساب الذي ضبطته على أنّه "حساب اختبار" عند إعداد مشروعك.**
2. يتم تخزين معلومات التفويض في نظام الملفات، لذا لن يُطلب منك منح التفويض في المرة التالية التي تشغِّل فيها رمزًا نموذجيًا.

لقد أعددت المصادقة بنجاح.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-01 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-01 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
