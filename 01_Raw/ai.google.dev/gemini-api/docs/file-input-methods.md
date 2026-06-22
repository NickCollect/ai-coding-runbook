---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi
fetched_at: 2026-06-22T06:25:00.539703+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# फ़ाइल इनपुट करने के तरीके

इस गाइड में, Gemini API से अनुरोध करते समय इमेज, ऑडियो, वीडियो, और दस्तावेज़ जैसी मीडिया फ़ाइलें शामिल करने के अलग-अलग तरीके बताए गए हैं.
नए तरीके, Gemini API के सभी एंडपॉइंट पर काम करते हैं. इनमें बैच, इंटरैक्शन, और Live API शामिल हैं.
सही तरीका चुनने के लिए, आपको यह देखना होगा कि आपकी फ़ाइल का साइज़ कितना है, आपका डेटा फ़िलहाल कहां सेव है, और आपको फ़ाइल का इस्तेमाल कितनी बार करना है.

किसी फ़ाइल को इनपुट के तौर पर शामिल करने का सबसे आसान तरीका यह है कि किसी लोकल फ़ाइल को पढ़ा जाए और उसे प्रॉम्प्ट में शामिल किया जाए. यहां दिए गए उदाहरण में, किसी स्थानीय PDF फ़ाइल को पढ़ने का तरीका बताया गया है. इस तरीके से अपलोड किए जाने वाले PDF का साइज़ 50 एमबी से ज़्यादा नहीं होना चाहिए. फ़ाइल इनपुट टाइप और सीमाओं की पूरी सूची देखने के लिए, [इनपुट मेथड की तुलना करने वाली टेबल](#method-comparison) देखें.

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## इनपुट के तरीकों की तुलना

यहां दी गई टेबल में, हर इनपुट तरीके की तुलना फ़ाइल की सीमाओं और सबसे सही इस्तेमाल के उदाहरणों से की गई है. ध्यान दें कि फ़ाइल का साइज़, फ़ाइल टाइप और फ़ाइल को प्रोसेस करने के लिए इस्तेमाल किए गए मॉडल/टोकनाइज़र के हिसाब से अलग-अलग हो सकता है.

| तरीका | इन स्थितियों में बेहतर है | अधिकतम फ़ाइल आकार | परसिस्टेंस |
| --- | --- | --- | --- |
| **इनलाइन डेटा** | तेज़ी से टेस्टिंग, छोटी फ़ाइलें, रीयल-टाइम ऐप्लिकेशन. | हर अनुरोध/पेलोड के लिए 100 एमबी   (**PDF के लिए 50 एमबी**) | कोई नहीं (हर अनुरोध के साथ भेजा जाता है) |
| **File API की मदद से अपलोड करना** | बड़ी फ़ाइलें, एक से ज़्यादा बार इस्तेमाल की गई फ़ाइलें. | हर फ़ाइल का साइज़ 2 जीबी और हर प्रोजेक्ट के लिए 20 जीबी तक | 48 घंटे |
| **File API GCS यूआरआई रजिस्ट्रेशन** | Google Cloud Storage में पहले से मौजूद बड़ी फ़ाइलें और वे फ़ाइलें जिनका इस्तेमाल कई बार किया गया है. | हर फ़ाइल के लिए 2 जीबी, स्टोरेज की कोई सीमा नहीं | कोई नहीं (हर अनुरोध के हिसाब से फ़ेच किया जाता है). एक बार रजिस्टर करने पर, 30 दिनों तक ऐक्सेस मिल सकता है. |
| **बाहरी यूआरएल** | सार्वजनिक डेटा या क्लाउड बकेट (AWS, Azure, GCS) में मौजूद डेटा को फिर से अपलोड किए बिना. | हर अनुरोध/पे लोड के लिए 100 एमबी | कोई नहीं (हर अनुरोध के हिसाब से फ़ेच किया जाता है) |

## इनलाइन डेटा

छोटी फ़ाइलों (100 एमबी से कम या PDF के लिए 50 एमबी) के लिए, डेटा को सीधे तौर पर अनुरोध के पेलोड में पास किया जा सकता है. यह तुरंत टेस्ट करने या रीयल-टाइम में कुछ समय के लिए उपलब्ध डेटा को मैनेज करने वाले ऐप्लिकेशन के लिए सबसे आसान तरीका है. डेटा को base64 एन्कोड की गई स्ट्रिंग के तौर पर उपलब्ध कराया जा सकता है. इसके अलावा, सीधे तौर पर स्थानीय फ़ाइलों को पढ़कर भी डेटा उपलब्ध कराया जा सकता है.

किसी स्थानीय फ़ाइल से पढ़ने के उदाहरण के लिए, इस पेज की शुरुआत में दिया गया उदाहरण देखें.

### किसी यूआरएल से फ़ेच करना

किसी यूआरएल से फ़ाइल फ़ेच की जा सकती है. साथ ही, उसे बाइट में बदलकर इनपुट में शामिल किया जा सकता है.

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl);
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Gemini File API

File API को बड़ी फ़ाइलों (2 जीबी तक) या उन फ़ाइलों के लिए डिज़ाइन किया गया है जिनका इस्तेमाल आपको कई अनुरोधों में करना है.

### फ़ाइल अपलोड करने की स्टैंडर्ड सुविधा

Gemini API में कोई लोकल फ़ाइल अपलोड करें. इस तरीके से अपलोड की गई फ़ाइलों को कुछ समय के लिए (48 घंटे) सेव किया जाता है. साथ ही, मॉडल के ज़रिए उन्हें आसानी से ऐक्सेस करने के लिए प्रोसेस किया जाता है.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[prompt, audio_file]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### Google Cloud Storage की फ़ाइलें रजिस्टर करना

अगर आपका डेटा पहले से ही Google Cloud Storage में है, तो आपको उसे डाउनलोड करके फिर से अपलोड करने की ज़रूरत नहीं है. इसे सीधे तौर पर File API के साथ रजिस्टर किया जा सकता है.

1. हर बकेट के लिए, **सर्विस एजेंट** को ऐक्सेस दें

   1. अपने Google Cloud प्रोजेक्ट में Gemini API चालू करें.
   2. सर्विस एजेंट बनाएं:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Gemini API सेवा एजेंट को, आपके स्टोरेज बकेट पढ़ने की अनुमतियां दें**.

      उपयोगकर्ता को उन स्टोरेज बकेट के लिए, इस सेवा एजेंट को `Storage Object Viewer`
      [IAM भूमिका](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=hi#storage.objectViewer)
      असाइन करनी होगी जिनका उसे इस्तेमाल करना है.

   डिफ़ॉल्ट रूप से, यह ऐक्सेस कभी खत्म नहीं होता. हालांकि, इसे किसी भी समय बदला जा सकता है. अनुमतियां देने के लिए, [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=hi) की कमांड का भी इस्तेमाल किया जा सकता है.
2. अपनी सेवा की पुष्टि करना

   **ज़रूरी शर्तें**

   - एपीआई चालू करना
   - ज़रूरी अनुमतियों के साथ सेवा खाता/एजेंट बनाएं.

   सबसे पहले, आपको उस सेवा के तौर पर पुष्टि करनी होगी जिसके पास स्टोरेज ऑब्जेक्ट व्यूअर की अनुमतियां हैं. यह इस बात पर निर्भर करता है कि आपका फ़ाइल मैनेजमेंट कोड किस एनवायरमेंट में चलेगा.

   **Google Cloud के बाहर**

   अगर आपका कोड Google Cloud के बाहर से चल रहा है, जैसे कि आपका डेस्कटॉप, तो Google Cloud Console से खाते के क्रेडेंशियल डाउनलोड करें. इसके लिए, यह तरीका अपनाएं:

   1. [Service Account console](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=hi) पर जाएं
   2. काम का सेवा खाता चुनें
   3. **कुंजियां** टैब को चुनें. इसके बाद, **कुंजी जोड़ें, नई कुंजी बनाएं** को चुनें
   4. **JSON** फ़ाइल फ़ॉर्मैट वाली कुंजी चुनें. साथ ही, यह नोट करें कि आपके डिवाइस पर फ़ाइल कहां डाउनलोड हुई है.

   ज़्यादा जानकारी के लिए, [सेवा खाते की कुंजी के मैनेजमेंट](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=hi) के बारे में Google Cloud का आधिकारिक दस्तावेज़ देखें.

   इसके बाद, पुष्टि करने के लिए इन कमांड का इस्तेमाल करें. इन कमांड में यह माना गया है कि आपकी सेवा खाते की फ़ाइल, मौजूदा डायरेक्ट्री में है और उसका नाम `service-account.json` है.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### सीएलआई

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Google Cloud पर**

   अगर Google Cloud में सीधे तौर पर कोई काम किया जा रहा है, जैसे कि [Cloud Run फ़ंक्शन](https://cloud.google.com/functions?hl=hi) या [Compute Engine इंस्टेंस](https://cloud.google.com/products/compute?hl=hi) का इस्तेमाल करके, तो आपके पास इंप्लिसिट क्रेडेंशियल होंगे. हालांकि, सही स्कोप देने के लिए आपको फिर से पुष्टि करनी होगी.

   ### Python

   इस कोड के लिए ज़रूरी है कि सेवा ऐसे एनवायरमेंट में चल रही हो जहां [ऐप्लिकेशन के डिफ़ॉल्ट क्रेडेंशियल](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=hi) अपने-आप मिल सकते हों. जैसे, Cloud Run या Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   इस कोड के लिए ज़रूरी है कि सेवा ऐसे एनवायरमेंट में चल रही हो जहां [ऐप्लिकेशन के डिफ़ॉल्ट क्रेडेंशियल](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=hi) अपने-आप मिल सकते हों. जैसे, Cloud Run या Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### सीएलआई

   यह एक इंटरैक्टिव कमांड है. Compute Engine जैसी सेवाओं के लिए, कॉन्फ़िगरेशन लेवल पर चल रही सेवा से स्कोप अटैच किए जा सकते हैं. उदाहरण के लिए, [उपयोगकर्ता के मैनेज किए गए सेवा दस्तावेज़](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=hi#using) देखें.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. फ़ाइल रजिस्टर करना (Files API)

   फ़ाइलों को रजिस्टर करने के लिए, Files API का इस्तेमाल करें. साथ ही, Files API का ऐसा पाथ जनरेट करें जिसका इस्तेमाल Gemini API में सीधे तौर पर किया जा सके.

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3.5-flash",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
   ```

   ### सीएलआई

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## एक्सटर्नल एचटीटीपी / सीमित ऐक्सेस वाले यूआरएल

जनरेट करने के अनुरोध में, सार्वजनिक तौर पर ऐक्सेस किए जा सकने वाले एचटीटीपीएस यूआरएल या पहले से हस्ताक्षर किए गए यूआरएल ([S3 Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) और Azure SAS के साथ काम करने वाले) सीधे तौर पर पास किए जा सकते हैं. Gemini API, प्रोसेसिंग के दौरान कॉन्टेंट को सुरक्षित तरीके से फ़ेच करेगा. यह 100 एमबी तक की उन फ़ाइलों के लिए सबसे सही है जिन्हें आपको फिर से अपलोड नहीं करना है.

`file_uri` फ़ील्ड में यूआरएल का इस्तेमाल करके, सार्वजनिक या हस्ताक्षर किए गए यूआरएल को इनपुट के तौर पर इस्तेमाल किया जा सकता है.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### सुलभता

पुष्टि करें कि आपके दिए गए यूआरएल, ऐसे पेजों पर न ले जाते हों जिन्हें ऐक्सेस करने के लिए लॉगिन करने की ज़रूरत हो या जिन पर paywall लागू हो. निजी डेटाबेस के लिए, पक्का करें कि आपने सही ऐक्सेस अनुमतियों और समयसीमा के साथ हस्ताक्षर किया गया यूआरएल बनाया हो.

### सुरक्षा जांच

सिस्टम, यूआरएल पर कॉन्टेंट मॉडरेशन की जांच करता है.इससे यह पुष्टि की जाती है कि यूआरएल, सुरक्षा और नीति के मानकों के मुताबिक है. जैसे, ऑप्ट आउट न किया गया और पेवॉल वाला कॉन्टेंट. अगर आपके दिए गए यूआरएल की जांच नहीं हो पाती है, तो आपको `url_retrieval_status` में से `URL_RETRIEVAL_STATUS_UNSAFE` मिलेगा.

### इस्तेमाल किए जा सकने वाले कॉन्टेंट टाइप

यहां दिए गए फ़ाइल टाइप और सीमाओं के बारे में शुरुआती जानकारी दी गई है. इसमें पूरी जानकारी शामिल नहीं है. सपोर्ट किए गए टाइप का सेट बदल सकता है. साथ ही, यह इस्तेमाल किए जा रहे मॉडल और टोकनाइज़र के वर्शन के हिसाब से अलग-अलग हो सकता है. काम न करने वाले टाइप की वजह से गड़बड़ी होगी.
इसके अलावा, फ़िलहाल इन फ़ाइल टाइप के लिए कॉन्टेंट सिर्फ़ ऐसे यूआरएल से वापस पाया जा सकता है जिन्हें सार्वजनिक तौर पर ऐक्सेस किया जा सकता है.

#### टेक्स्ट फ़ाइल के टाइप

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### ऐप्लिकेशन फ़ाइल के टाइप

- `application/json`
- `application/pdf`

#### इमेज फ़ाइल के टाइप

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### वीडियो फ़ाइल के टाइप

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## सबसे सही तरीके

- **सही तरीका चुनें:** छोटी और कुछ समय के लिए इस्तेमाल की जाने वाली फ़ाइलों के लिए, इनलाइन डेटा का इस्तेमाल करें.
  बड़ी या अक्सर इस्तेमाल की जाने वाली फ़ाइलों के लिए, फ़ाइल एपीआई का इस्तेमाल करें. पहले से ऑनलाइन होस्ट किए गए डेटा के लिए, बाहरी यूआरएल का इस्तेमाल करें.
- **MIME टाइप तय करें:** फ़ाइल के डेटा को सही तरीके से प्रोसेस करने के लिए, हमेशा सही MIME टाइप दें.
- **गड़बड़ियों को ठीक करना:** अपने कोड में गड़बड़ी ठीक करने की सुविधा लागू करें, ताकि नेटवर्क फ़ेल होने, फ़ाइल ऐक्सेस करने में आने वाली समस्याओं या एपीआई से जुड़ी गड़बड़ियों जैसी संभावित समस्याओं को मैनेज किया जा सके.
- **GCS की अनुमतियां मैनेज करें:** GCS रजिस्ट्रेशन का इस्तेमाल करते समय, Gemini API सेवा एजेंट को सिर्फ़ ज़रूरी `Storage Object Viewer` भूमिका दें. ऐसा सिर्फ़ चुनिंदा बकेट के लिए करें.
- **हस्ताक्षर किए गए यूआरएल की सुरक्षा:** पक्का करें कि हस्ताक्षर किए गए यूआरएल की समयसीमा खत्म होने का समय सही हो और उनके लिए अनुमतियां सीमित हों.

## सीमाएं

- फ़ाइल के साइज़ की सीमाएं, अपलोड करने के तरीके ([तुलना करने वाली टेबल](#method-comparison) देखें) और फ़ाइल टाइप के हिसाब से अलग-अलग होती हैं.
- इनलाइन डेटा से, अनुरोध के पेलोड का साइज़ बढ़ जाता है.
- फ़ाइल एपीआई के ज़रिए अपलोड की गई फ़ाइलें कुछ समय के लिए होती हैं. ये 48 घंटे बाद मिट जाती हैं.
- बाहरी यूआरएल से डेटा फ़ेच करने की सुविधा, हर पेलोड के लिए 100 एमबी तक सीमित है. साथ ही, यह सुविधा कुछ खास कॉन्टेंट टाइप के साथ काम करती है.
- Google Cloud Storage के रजिस्ट्रेशन के लिए, IAM को सही तरीके से सेटअप करना और OAuth टोकन को मैनेज करना ज़रूरी है.

## आगे क्या करना है

- [Google AI Studio](http://aistudio.google.com/?hl=hi) का इस्तेमाल करके, मल्टीमॉडल प्रॉम्प्ट लिखने की कोशिश करें.
- अपने प्रॉम्प्ट में फ़ाइलें शामिल करने के बारे में जानकारी पाने के लिए, [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=hi), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=hi), और [Document processing](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi) से जुड़ी गाइड देखें.
- प्रॉम्प्ट डिज़ाइन करने के बारे में ज़्यादा जानकारी के लिए, [प्रॉम्प्ट से जुड़ी रणनीतियां](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=hi) गाइड देखें. इसमें सैंपलिंग पैरामीटर को ट्यून करने के बारे में भी बताया गया है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया."],[],[]]
