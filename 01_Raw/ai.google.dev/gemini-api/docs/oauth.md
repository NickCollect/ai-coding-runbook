---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=hi
fetched_at: 2026-08-24T02:19:57.936540+00:00
title: "OAuth \u0915\u094d\u0935\u093f\u0915\u0938\u094d\u091f\u093e\u0930\u094d\u091f \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u092a\u0941\u0937\u094d\u091f\u093f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# OAuth क्विकस्टार्ट की मदद से पुष्टि करना

Gemini API से पुष्टि करने का सबसे आसान तरीका है कि एपीआई
कुंजी को कॉन्फ़िगर किया जाए. इसके बारे में, [Gemini API का इस्तेमाल शुरू करने की
गाइड](https://ai.google.dev/gemini-api/docs/get-started?hl=hi) में बताया गया है. अगर आपको ऐक्सेस कंट्रोल के लिए ज़्यादा पाबंदियां लगानी हैं, तो OAuth का इस्तेमाल किया जा सकता है. इस गाइड की मदद से, OAuth की मदद से पुष्टि करने की सुविधा सेट अप की जा सकती है.

इस गाइड में, पुष्टि करने के लिए आसान तरीका बताया गया है. यह तरीका, टेस्ट एनवायरमेंट के लिए सही है. [[प्रोडक्शन एनवायरमेंट के लिए, अपने ऐप्लिकेशन के हिसाब से ऐक्सेस क्रेडेंशियल चुनने से पहले, पुष्टि करने और अनुमति देने के बारे में जानें.](https://developers.google.com/workspace/guides/auth-overview?hl=hi)](https://developers.google.com/workspace/guides/create-credentials?hl=hi#choose_the_access_credential_that_is_right_for_you)

## मकसद

- OAuth के लिए अपना क्लाउड प्रोजेक्ट सेट अप करना
- ऐप्लिकेशन-डिफ़ॉल्ट-क्रेडेंशियल सेट अप करना
- `gcloud auth` का इस्तेमाल करने के बजाय, अपने प्रोग्राम में क्रेडेंशियल मैनेज करना

## ज़रूरी शर्तें

क्विकस्टार्ट को चलाने के लिए, आपके पास ये चीज़ें होनी चाहिए:

- [एक Google Cloud प्रोजेक्ट](https://developers.google.com/workspace/guides/create-project?hl=hi)
- [gcloud सीएलआई का लोकल इंस्टॉलेशन](https://cloud.google.com/sdk/docs/install?hl=hi)

## अपना क्लाउड प्रोजेक्ट सेट अप करना

इस क्विकस्टार्ट को पूरा करने के लिए, आपको सबसे पहले अपना क्लाउड प्रोजेक्ट सेट अप करना होगा.

### 1. एपीआई चालू करना

Google के एपीआई का इस्तेमाल करने से पहले, आपको उन्हें Google Cloud प्रोजेक्ट में चालू करना होगा.

- Google Cloud Console में, Google Generative Language API चालू करें.

  [एपीआई चालू करें](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=hi)

### 2. उस स्क्रीन को कॉन्फ़िगर करना जहां OAuth को सहमति दी जाती है

इसके बाद, प्रोजेक्ट की उस स्क्रीन को कॉन्फ़िगर करें जहां OAuth को सहमति दी जाती है. साथ ही, खुद को टेस्ट यूज़र के तौर पर जोड़ें. अगर आपने अपने क्लाउड प्रोजेक्ट के लिए यह चरण पहले ही पूरा कर लिया है, तो अगले सेक्शन पर जाएं.

1. Google Cloud Console में, **मेन्यू** > **Google Auth प्लैटफ़ॉर्म** > **खास जानकारी** पर जाएं.

   [Google Auth प्लैटफ़ॉर्म पर जाएं](https://console.developers.google.com/auth/overview?hl=hi)
2. प्रोजेक्ट कॉन्फ़िगरेशन फ़ॉर्म भरें और **ऑडियंस** सेक्शन में, उपयोगकर्ता का टाइप **एक्सटर्नल** पर सेट करें.
3. फ़ॉर्म का बाकी हिस्सा भरें, उपयोगकर्ता के डेटा से जुड़ी नीति की शर्तें स्वीकार करें, और फिर **बनाएं** पर क्लिक करें.
4. फ़िलहाल, स्कोप जोड़ने के चरण को छोड़ा जा सकता है. इसके बाद, **सेव करें और जारी रखें** पर क्लिक करें. भविष्य में, जब आप अपने Google Workspace संगठन के बाहर इस्तेमाल के लिए कोई ऐप्लिकेशन बनाते हैं, तो आपको अनुमति के उन स्कोप को जोड़ना और उनकी पुष्टि करनी होगी जिनकी आपके ऐप्लिकेशन को ज़रूरत है.
5. टेस्ट यूज़र जोड़ना:

   1. Google Auth प्लैटफ़ॉर्म के
      [ऑडियंस पेज](https://console.developers.google.com/auth/audience?hl=hi) पर जाएं.
   2. **टेस्ट यूज़र** में जाकर, **उपयोगकर्ता जोड़ें** पर क्लिक करें.
   3. अपना ईमेल पता और अनुमति वाले अन्य टेस्ट यूज़र के ईमेल पते डालें. इसके बाद, **सेव करें** पर क्लिक करें.

### 3. डेस्कटॉप ऐप्लिकेशन के लिए क्रेडेंशियल को अनुमति देना

एंड यूज़र के तौर पर पुष्टि करने और अपने ऐप्लिकेशन में उपयोगकर्ता के डेटा को ऐक्सेस करने के लिए, आपको एक या उससे ज़्यादा OAuth 2.0 क्लाइंट आईडी बनाने होंगे. क्लाइंट आईडी का इस्तेमाल, Google के OAuth सर्वर पर किसी एक ऐप्लिकेशन की पहचान करने के लिए किया जाता है. अगर आपका ऐप्लिकेशन एक से ज़्यादा प्लैटफ़ॉर्म पर चलता है, तो आपको हर प्लैटफ़ॉर्म के लिए अलग-अलग क्लाइंट आईडी बनाना होगा.

1. Google Cloud Console में, **मेन्यू** > **Google Auth प्लैटफ़ॉर्म** > **क्लाइंट** पर जाएं.

   [क्रेडेंशियल पर जाएं](https://console.developers.google.com/auth/clients?hl=hi)
2. **क्लाइंट बनाएं** पर क्लिक करें.
3. **ऐप्लिकेशन का टाइप** > **डेस्कटॉप ऐप्लिकेशन** पर क्लिक करें.
4. **नाम** फ़ील्ड में, क्रेडेंशियल के लिए कोई नाम डालें. यह नाम सिर्फ़ Google Cloud Console में दिखता है.
5. **बनाएं** पर क्लिक करें. OAuth क्लाइंट बनाया गया स्क्रीन दिखती है. इसमें, आपका नया क्लाइंट आईडी और क्लाइंट सीक्रेट दिखता है.
6. **ठीक है** पर क्लिक करें. नया बनाया गया क्रेडेंशियल, **OAuth 2.0 क्लाइंट आईडी** में दिखता है.
7. JSON फ़ाइल सेव करने के लिए, डाउनलोड बटन पर क्लिक करें. यह
   `client_secret_<identifier>.json` के तौर पर सेव होगी. इसका नाम बदलकर `client_secret.json`
   करें और इसे अपनी वर्किंग डायरेक्ट्री में ले जाएं.

## ऐप्लिकेशन डिफ़ॉल्ट क्रेडेंशियल सेट अप करना

`client_secret.json` फ़ाइल को इस्तेमाल किए जा सकने वाले क्रेडेंशियल में बदलने के लिए, इसका पाथ, `gcloud auth application-default login` कमांड के `--client-id-file` आर्ग्युमेंट में पास करें.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

इस ट्यूटोरियल में, प्रोजेक्ट को सेट अप करने का आसान तरीका बताया गया है. इससे **"Google ने इस ऐप्लिकेशन की पुष्टि नहीं की है."** डायलॉग दिखता है. यह सामान्य है, **"जारी रखें"** को चुनें.

इससे, नतीजा देने वाला टोकन, जानी-मानी जगह पर सेव हो जाता है. इसलिए, इसे `gcloud` या क्लाइंट लाइब्रेरी से ऐक्सेस किया जा सकता है.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

ऐप्लिकेशन डिफ़ॉल्ट क्रेडेंशियल (एडीसी) सेट करने के बाद, ज़्यादातर भाषाओं में क्लाइंट लाइब्रेरी को इन्हें ढूंढने के लिए, बहुत कम या किसी भी मदद की ज़रूरत नहीं होती.

### Curl

यह काम कर रहा है या नहीं, यह टेस्ट करने का सबसे तेज़ तरीका है कि curl का इस्तेमाल करके, REST API को ऐक्सेस किया जाए:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

Python में, क्लाइंट लाइब्रेरी को इन्हें अपने-आप ढूंढ लेना चाहिए:

```
pip install google-genai
```

इसे टेस्ट करने के लिए, यह स्क्रिप्ट इस्तेमाल की जा सकती है:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## अगले चरण

अगर यह काम कर रहा है, तो अपने टेक्स्ट डेटा पर
[सिमैंटिक रिट्रीवल आज़माया जा सकता है](https://ai.google.dev/docs/semantic_retriever?hl=hi).

## क्रेडेंशियल खुद मैनेज करना [Python]

कई मामलों में, आपके पास क्लाइंट आईडी (`client_secret.json`) से ऐक्सेस टोकन बनाने के लिए, `gcloud` कमांड उपलब्ध नहीं होगा. Google, कई भाषाओं में लाइब्रेरी उपलब्ध कराता है, ताकि आपके ऐप्लिकेशन में इस प्रोसेस को मैनेज किया जा सके. इस सेक्शन में, Python में इस प्रोसेस के बारे में बताया गया है. [Drive API के दस्तावेज़ में, अन्य भाषाओं के लिए भी इस तरह की प्रोसेस के उदाहरण उपलब्ध हैं](https://developers.google.com/drive/api/quickstart/python?hl=hi)

### 1. ज़रूरी लाइब्रेरी इंस्टॉल करना

Python के लिए Google क्लाइंट लाइब्रेरी और Gemini क्लाइंट लाइब्रेरी इंस्टॉल करें.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. क्रेडेंशियल मैनेजर लिखना

अनुमति वाली स्क्रीन पर बार-बार क्लिक करने से बचने के लिए, अपनी वर्किंग डायरेक्ट्री में `load_creds.py` नाम की एक फ़ाइल बनाएं. यह `token.json` फ़ाइल को कैश करती है, ताकि इसे बाद में फिर से इस्तेमाल किया जा सके या इसकी समयसीमा खत्म होने पर इसे रीफ़्रेश किया जा सके.

`client_secret.json` फ़ाइल को `genai.configure` के साथ इस्तेमाल किए जा सकने वाले टोकन में बदलने के लिए, इस कोड का इस्तेमाल करें:

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

### 3. अपना प्रोग्राम लिखना

अब `script.py` बनाएं:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. प्रोग्राम चलाना

अपनी वर्किंग डायरेक्ट्री में, सैंपल चलाएं:

```
python script.py
```

स्क्रिप्ट को पहली बार चलाने पर, यह ब्राउज़र विंडो खोलती है और आपसे ऐक्सेस की अनुमति देने के लिए कहती है.

1. अगर आपने अपने Google खाते में साइन इन नहीं किया है, तो आपसे साइन इन करने के लिए कहा जाता है. अगर आपने एक से ज़्यादा खातों में साइन इन किया है, तो **प्रोजेक्ट को कॉन्फ़िगर करते समय, पक्का करें कि आपने वही खाता चुना हो जिसे "टेस्ट खाता" के तौर पर सेट किया है.**
2. अनुमति की जानकारी, फ़ाइल सिस्टम में सेव होती है. इसलिए, सैंपल कोड को अगली बार चलाने पर, आपसे अनुमति के लिए नहीं कहा जाता.

आपने पुष्टि करने की सुविधा को सेट अप कर लिया है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-01 (UTC) को अपडेट किया गया."],[],[]]
