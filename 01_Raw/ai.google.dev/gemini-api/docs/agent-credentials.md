---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=hi
fetched_at: 2026-09-21T05:54:13.038612+00:00
title: "\u092e\u0948\u0928\u0947\u091c \u0915\u093f\u090f \u091c\u093e \u0930\u0939\u0947 \u090f\u091c\u0947\u0902\u091f \u092e\u0947\u0902 \u0915\u094d\u0930\u0947\u0921\u0947\u0902\u0936\u093f\u092f\u0932 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# मैनेज किए जा रहे एजेंट में क्रेडेंशियल

क्रेडेंशियल, सर्वर से मैनेज किए जाने वाले सीक्रेट होते हैं. इनकी मदद से, आपके एजेंट तीसरे पक्ष की सेवाओं तक पहुंच सकते हैं. हालांकि, इस दौरान सीक्रेट कभी भी एजेंट के एनवायरमेंट में नहीं जाता है. क्रेडेंशियल को एक बार सेव किया जाता है. इसके बाद, इसे आईडी के हिसाब से रेफ़रंस किया जाता है. साथ ही, इग्रेस प्रॉक्सी इसे अनुरोध के समय हल करके इंजेक्ट करती है.

सीक्रेट की वैल्यू सिर्फ़ लिखी जा सकती हैं. सेव होने के बाद, इन्हें किसी भी एंडपॉइंट से कभी वापस नहीं भेजा जाता. इसलिए, कोई ऐसा एजेंट जो सुरक्षा से समझौता करता है, उन टोकन को वापस नहीं पढ़ सकता जिनका वह इस्तेमाल कर रहा है.

क्रेडेंशियल का इस्तेमाल मुख्य रूप से, [`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi) पर नेटवर्क की अनुमति वाली सूची में किया जाता है. सबसे पहले, सीक्रेट सेव करें:

### Python

```
from google import genai

client = genai.Client()

credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});

console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

इसके बाद, इसे उस डोमेन से अटैच करें जिसकी पुष्टि की जाती है:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Triage the open issues in my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {"domain": "api.github.com", "credential": "github-production"},
                {"domain": "*"},
            ]
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Triage the open issues in my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ],
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Triage the open issues in my-org/my-repo.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                { "domain": "api.github.com", "credential": "github-production" },
                { "domain": "*" }
            ]
        }
    }
}'
```

अब एजेंट, `api.github.com` से पुष्टि किए गए अनुरोध करता है. साथ ही, टोकन कभी भी सैंडबॉक्स में मौजूद नहीं होता.

## क्रेडेंशियल के टाइप

हर क्रेडेंशियल में एक `type` होता है. इससे यह तय होता है कि क्रेडेंशियल किन फ़ील्ड को स्वीकार करता है और प्रॉक्सी इसे कैसे लागू करती है.

| टाइप | इस्तेमाल का उदाहरण | व्यवहार |
| --- | --- | --- |
| `bearer_token` | निजी ऐक्सेस टोकन, बॉट टोकन, स्टैटिक एपीआई कुंजियां | प्रॉक्सी, टोकन को अनुरोध के हेडर के तौर पर इंजेक्ट करता है. रीफ़्रेश करने का कोई लॉजिक नहीं है. |
| `oauth2` | OAuth ऐप्लिकेशन और उपयोगकर्ता के तौर पर काम करने वाले फ़्लो | प्रॉक्सी, रीफ़्रेश टोकन को ऐक्सेस टोकन के लिए बदलता है और खत्म होने पर उन्हें रीफ़्रेश करता है. |
| `environment_variable` | ऐसे क्लाइंट SDK टूल जो प्रोसेस एनवायरमेंट से सीक्रेट पढ़ते हैं | एजेंट के एनवायरमेंट को एक प्लेसहोल्डर मिलता है. प्रॉक्सी, आउटबाउंड अनुरोधों पर असली सीक्रेट की जगह दूसरा सीक्रेट इस्तेमाल करता है. |

## नेटवर्क की अनुमति वाली सूची में मौजूद क्रेडेंशियल का इस्तेमाल करना

अनुमति वाली सूची के नियम में `credential` जोड़ें. इसके बाद, प्रॉक्सी उस डोमेन के लिए किए गए हर आउटबाउंड अनुरोध की पुष्टि करती है. किसी एजेंट को निजी एपीआई, निजी डेटा सेव करने की जगह या निजी बकेट का ऐक्सेस देने का यह सबसे सही तरीका है.

एक ही अनुमति वाली सूची में, पुष्टि किए गए और पुष्टि नहीं किए गए नियमों को मिक्स किया जा सकता है:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Sync the open Jira issues into the tracking sheet in my repo.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app",
            }
        ],
        "network": {
            "allowlist": [
                {"domain": "github.com", "credential": "github-production"},
                {"domain": "api.atlassian.com", "credential": "jira-oauth"},
                {"domain": "*.googleapis.com"},
            ]
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Sync the open Jira issues into the tracking sheet in my repo.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app",
            },
        ],
        network: {
            allowlist: [
                { domain: "github.com", credential: "github-production" },
                { domain: "api.atlassian.com", credential: "jira-oauth" },
                { domain: "*.googleapis.com" },
            ],
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Sync the open Jira issues into the tracking sheet in my repo.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                { "domain": "github.com", "credential": "github-production" },
                { "domain": "api.atlassian.com", "credential": "jira-oauth" },
                { "domain": "*.googleapis.com" }
            ]
        }
    }
}'
```

प्रॉक्सी, हर अनुरोध के लिए क्रेडेंशियल को हल करता है. इसलिए, `oauth2` क्रेडेंशियल, अपने ऐक्सेस टोकन को पारदर्शी तरीके से रीफ़्रेश करता है. ऐक्सेस टोकन की समयसीमा खत्म होने पर, लंबे समय तक चलने वाला इंटरैक्शन नहीं रुकता.

### `credential` और `transform` को मिलाकर बनाई गई इमेज

अनुमति वाली सूची के नियमों में, इनलाइन [`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi#private-sources) ऑब्जेक्ट भी स्वीकार किया जाता है. यह ऑब्जेक्ट, नियम पर सीधे तौर पर हेडर सेट करता है. दोनों ही तरीके, वायर पर इग्रेस प्रॉक्सी लागू करते हैं. इसलिए, दोनों ही मामलों में हेडर वैल्यू, सैंडबॉक्स में कभी मौजूद नहीं होती. दोनों फ़ील्ड, एक ही नियम में दिख सकते हैं.

| नियम का कॉन्फ़िगरेशन | व्यवहार |
| --- | --- |
| सिर्फ़ `credential` | प्रॉक्सी, क्रेडेंशियल को हल करता है और डोमेन के हर अनुरोध पर उसका हेडर डालता है. |
| सिर्फ़ `transform` | स्टैटिक हेडर इंजेक्शन. आपने जो हेडर लिखे हैं उन्हें उसी तरह भेजा जाता है. |
| दोनों | सबसे पहले क्रेडेंशियल लागू होता है. इसके बाद, `transform` सबसे ऊपर मर्ज हो जाता है. अगर दोनों हेडर एक ही कुंजी सेट करते हैं, तो साफ़ तौर पर बताए गए `transform` हेडर को प्राथमिकता दी जाती है. |
| न तो सक्षम और न ही असक्षम | डोमेन को अनुमति है और कोई भी हेडर इंजेक्ट नहीं किया गया है. |

क्रेडेंशियल का इस्तेमाल तब किया जाता है, जब आपको किसी सीक्रेट को एक बार सेव करना हो और उसे अपने प्रोजेक्ट के हर एनवायरमेंट, एजेंट, और ट्रिगर से रेफ़रंस करना हो. साथ ही, जब आपको ऐक्सेस टोकन को रीफ़्रेश और रोटेट करने की सुविधा चाहिए हो. इनलाइन `transform` तब काम करता है, जब वैल्यू किसी एक कॉल से जुड़ी हो. उदाहरण के लिए, कोई ऐसा टोकन जिसे आपने इंटरैक्शन बनाने से ठीक पहले जनरेट किया हो.

इन दोनों को मिलाकर इस्तेमाल करना आम बात है. क्रेडेंशियल में पुष्टि करने वाला हेडर होता है. साथ ही, `transform` उसी अनुरोध में वह जानकारी जोड़ता है जो अपस्ट्रीम सेवा को चाहिए:

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

किसी सीक्रेट को इनलाइन `transform` से क्रेडेंशियल में ले जाने के लिए, उसे `POST /credentials` के साथ सेव करें. इसके बाद, `transform` में मौजूद auth हेडर को `"credential": "<id>"` से बदलें. साथ ही, `transform` ऑब्जेक्ट के बाकी हिस्से को वैसे ही छोड़ दें.

## एमसीपी सर्वर के साथ क्रेडेंशियल का इस्तेमाल करना

रिमोट एमसीपी सर्वर, एक ही `credential` फ़ील्ड का इस्तेमाल करते हैं. इसे `mcp_server` टूल पर सेट करें. इसके बाद, प्रॉक्सी उस सर्वर पर किए गए हर अनुरोध में पुष्टि करने वाला हेडर जोड़ देगा:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Create a new issue in my-org/my-repo",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "github",
        "url": "https://api.githubcopilot.com/mcp",
        "credential": "github-production",
    }],
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Create a new issue in my-org/my-repo",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "github",
        url: "https://api.githubcopilot.com/mcp",
        credential: "github-production",
    }],
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Create a new issue in my-org/my-repo",
    "environment": "remote",
    "tools": [
        {
            "type": "mcp_server",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp",
            "credential": "github-production"
        }
    ]
}'
```

`credential` और `headers`, अनुमति वाली सूची के लिए लागू होने वाले प्राथमिकता के नियम का पालन करते हैं.
क्रेडेंशियल पहले लागू होता है और `headers` सबसे ऊपर मर्ज होता है. इसलिए, अगर दोनों एक ही कुंजी सेट करते हैं, तो साफ़ तौर पर बताए गए हेडर को प्राथमिकता दी जाती है:

```
{
    "type": "mcp_server",
    "name": "jira",
    "url": "https://jira.atlassian.com/mcp",
    "credential": "jira-oauth",
    "headers": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

किसी सीक्रेट को इनलाइन `headers` से क्रेडेंशियल में ले जाने के लिए, उसे `POST /credentials` के साथ सेव करें. इसके बाद, `headers` में मौजूद पुष्टि करने की एंट्री को `credential` से बदलें.
अन्य हेडर को उनकी जगह पर ही रहने दें.

## क्रेडेंशियल को एनवायरमेंट वैरिएबल के तौर पर इस्तेमाल करना

कुछ क्लाइंट लाइब्रेरी, अनुरोध हेडर के तौर पर स्वीकार करने के बजाय, प्रोसेस एनवायरमेंट से सीक्रेट पढ़ती हैं. सॉकेट मोड और लॉन्ग-पोलिंग क्लाइंट, सामान्य तौर पर इस्तेमाल किए जाते हैं.

`environment_variable` में मौजूद किसी वैरिएबल के नाम से `environment.env` क्रेडेंशियल को बाइंड करें:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the sync script and check notifications.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": {"credential": "slack-bot-token"},
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the sync script and check notifications.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            SLACK_BOT_TOKEN: { credential: "slack-bot-token" },
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Run the sync script and check notifications.",
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": { "credential": "slack-bot-token" }
        }
    }
}'
```

`env`, लिटरल स्ट्रिंग और क्रेडेंशियल रेफ़रंस को साथ-साथ स्वीकार करता है. इस विकल्प का इस्तेमाल करके, कंटेनर में लिटरल स्ट्रिंग को सामान्य टेक्स्ट वैरिएबल के तौर पर इंजेक्ट किया जाता है.

क्रेडेंशियल रेफ़रंस नहीं है. इस वैरिएबल को प्लेसहोल्डर `__GEMINI_CRED_<credential-id>__` मिलता है. साथ ही, प्रॉक्सी सिर्फ़ उन आउटबाउंड अनुरोधों के लिए असली सीक्रेट को स्वैप करता है जो क्रेडेंशियल के `trusted_domains` में मौजूद किसी डोमेन पर जाते हैं. किसी दूसरे डोमेन के अनुरोध को अस्वीकार कर दिया जाता है. इसलिए, सीक्रेट कभी भी पेरीमीटर से बाहर नहीं जाता है और उसकी जगह पर प्लेसहोल्डर नहीं भेजा जाता है.

हर `environment_variable` क्रेडेंशियल पर `trusted_domains` सेट करें. यह एक कंट्रोल है, जिससे यह तय होता है कि सीक्रेट का इस्तेमाल कहां किया जा सकता है.

## क्रेडेंशियल बनाना

हर क्रिएट अनुरोध के लिए, `type` और उस टाइप के लिए ज़रूरी फ़ील्ड की ज़रूरत होती है.

REST को सीधे तौर पर कॉल करते समय, सभी फ़ील्ड के नाम snake\_case का इस्तेमाल करते हैं. camelCase फ़ील्ड भेजने पर, `400` दिखता है.

### बियरर टोकन

बेयरर टोकन क्रेडेंशियल के लिए सिर्फ़ `token` की ज़रूरत होती है:

### Python

```
credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

जवाब में सिर्फ़ मेटाडेटा मिलता है, टोकन कभी नहीं:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

डिफ़ॉल्ट रूप से, प्रॉक्सी `Authorization: Bearer <token>` भेजता है. किसी ऐसी सेवा को टारगेट करने के लिए `header_name` और `prefix` को बदलें जो कुछ और चाहती है:

### Python

```
credential = client.credentials.create(
    id="my-api-key",
    type="bearer_token",
    token="key_xxxxxxxxxxxx",
    header_name="x-goog-api-key",
    prefix="",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "my-api-key",
    type: "bearer_token",
    token: "key_xxxxxxxxxxxx",
    header_name: "x-goog-api-key",
    prefix: "",
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "my-api-key",
    "type": "bearer_token",
    "token": "key_xxxxxxxxxxxx",
    "header_name": "x-goog-api-key",
    "prefix": ""
}'
```

इस कॉन्फ़िगरेशन से, `x-goog-api-key: key_xxxxxxxxxxxx` हेडर जनरेट होता है.

इस टेबल में दिखाया गया है कि `header_name` और `prefix` को कैसे जोड़ा जाता है:

| कॉन्फ़िगरेशन | इंजेक्ट किया गया हेडर |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

OAuth2 क्रेडेंशियल के लिए `client_id`, `client_secret`, `refresh_token`, और `token_url` की ज़रूरत होती है. `scopes` फ़ील्ड की वैल्यू देना ज़रूरी नहीं है:

### Python

```
credential = client.credentials.create(
    id="jira-oauth",
    type="oauth2",
    client_id="my-client-id",
    client_secret="my-client-secret",
    token_url="https://auth.atlassian.com/oauth/token",
    refresh_token="rt_xxxxxxxxxxxxxxxxxxxx",
    scopes=["read:jira-work", "write:jira-work"],
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "jira-oauth",
    type: "oauth2",
    client_id: "my-client-id",
    client_secret: "my-client-secret",
    token_url: "https://auth.atlassian.com/oauth/token",
    refresh_token: "rt_xxxxxxxxxxxxxxxxxxxx",
    scopes: ["read:jira-work", "write:jira-work"],
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "jira-oauth",
    "type": "oauth2",
    "client_id": "my-client-id",
    "client_secret": "my-client-secret",
    "token_url": "https://auth.atlassian.com/oauth/token",
    "refresh_token": "rt_xxxxxxxxxxxxxxxxxxxx",
    "scopes": ["read:jira-work", "write:jira-work"]
}'
```

OAuth2 क्रेडेंशियल बनाने पर, `token_url` के साथ लाइव टोकन एक्सचेंज किया जाता है, ताकि यह पुष्टि की जा सके कि कॉन्फ़िगरेशन काम कर रहा है. क्रेडेंशियल सिर्फ़ तब सेव किया जाता है, जब प्रोवाइडर `access_token` वाला टोकन रिस्पॉन्स भेजता है. JSON और form-urlencoded, दोनों तरह के रिस्पॉन्स स्वीकार किए जाते हैं.

इसका मतलब है कि आपको खाता बनाते समय, एक मान्य और समयसीमा खत्म न हुआ रीफ़्रेश टोकन चाहिए. अगर सेवा देने वाली कंपनी, एक्सचेंज करने का अनुरोध अस्वीकार कर देती है, तो आपको गड़बड़ी का यह मैसेज दिखेगा:

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

स्टोर किए जाने के बाद, प्रॉक्सी ऐक्सेस टोकन की समयसीमा खत्म होने पर उन्हें रीफ़्रेश करता है. अगर सेवा देने वाली कंपनी, रीफ़्रेश टोकन को रोटेट करती है और रीफ़्रेश के दौरान नया टोकन देती है, तो नया टोकन, सेव किए गए टोकन की जगह अपने-आप ले लेता है.

### एनवायरमेंट वैरिएबल

`environment_variable` क्रेडेंशियल के लिए, `value` और `injection_location` की ज़रूरत होती है:

### Python

```
credential = client.credentials.create(
    id="slack-bot-token",
    type="environment_variable",
    value="xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains=["*.slack.com", "slack.com"],
    injection_location="header",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "slack-bot-token",
    type: "environment_variable",
    value: "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains: ["*.slack.com", "slack.com"],
    injection_location: "header",
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "slack-bot-token",
    "type": "environment_variable",
    "value": "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    "trusted_domains": ["*.slack.com", "slack.com"],
    "injection_location": "header"
}'
```

`injection_location` फ़ील्ड, प्रॉक्सी को यह बताता है कि आउटबाउंड अनुरोध में सीक्रेट को कहां बदलना है. यह `header`, `query` या `body` को स्वीकार करता है. अगर किसी सेवा के लिए एक से ज़्यादा की ज़रूरत होती है, तो इसे एक स्ट्रिंग या एक कलेक्शन के तौर पर स्वीकार किया जाता है:

```
"injection_location": ["header", "query"]
```

बदलाव सिर्फ़ उन जगहों पर होता है जिनकी जानकारी आपने दी है. अगर किसी अनुरोध में प्लेसहोल्डर को कहीं और रखा गया है, तो उसे आगे भेजने के बजाय अस्वीकार कर दिया जाता है.

क्रेडेंशियल को वैरिएबल के नाम से बाइंड करने के लिए, [क्रेडेंशियल को एनवायरमेंट वैरिएबल के तौर पर इस्तेमाल करना](#environment-variables) लेख पढ़ें.

### जनरेट किए गए आईडी

`id` फ़ील्ड ज़रूरी नहीं है. इसे हटा दें. इसके बाद, सेवा यूयूआईडी जनरेट करेगी:

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

जब आपको सभी इंटरैक्शन में इस्तेमाल करने के लिए, ऐसा रेफ़रंस चाहिए जिसे जल्दी बदला न जाए और जिसे आसानी से पढ़ा जा सके, तब अपना आईडी दें. आईडी, संसाधन के पाथ में दिखता है. इसलिए, हाइफ़न या अंडरस्कोर वाले छोटे अक्षरों और अंकों का इस्तेमाल करें.

## क्रेडेंशियल की सूची बनाना

अपने प्रोजेक्ट से जुड़े क्रेडेंशियल की सूची बनाएं. जवाब के बैच के साइज़ को कंट्रोल करने के लिए, पेज नंबर के पैरामीटर इस्तेमाल करें.

### Python

```
response = client.credentials.list(page_size=10)
for credential in response.credentials:
    print(f"Credential ID: {credential.id}, Type: {credential.type}")
```

### JavaScript

```
const response = await client.credentials.list({ page_size: 10 });
for (const credential of response.credentials) {
    console.log(`Credential ID: ${credential.id}, Type: ${credential.type}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials?page_size=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

जवाब में सिर्फ़ मेटाडेटा शामिल होता है:

```
{
  "credentials": [
    {
      "id": "github-production",
      "type": "bearer_token",
      "status": "active",
      "create_time": "2026-07-15T10:00:00.000000000Z",
      "update_time": "2026-07-15T10:00:00.000000000Z"
    },
    {
      "id": "jira-oauth",
      "type": "oauth2",
      "status": "active",
      "create_time": "2026-07-15T10:05:00.000000000Z",
      "update_time": "2026-07-15T10:05:00.000000000Z"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

अगला पेज फ़ेच करने के लिए, `next_page_token` को `page_token` के तौर पर पास करें. ज़्यादा नतीजे न होने पर, इस फ़ील्ड को शामिल नहीं किया जाता.

| पैरामीटर | टाइप | ब्यौरा |
| --- | --- | --- |
| `page_size` | पूर्णांक | हर पेज पर क्रेडेंशियल की ज़्यादा से ज़्यादा संख्या. |
| `page_token` | स्ट्रिंग | पिछले जवाब के `next_page_token` से मिला टोकन. |

## क्रेडेंशियल पाना

किसी क्रेडेंशियल का मेटाडेटा, उसकी आईडी के हिसाब से वापस पाएं.

### Python

```
credential = client.credentials.get(id="github-production")
print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### JavaScript

```
const credential = await client.credentials.get("github-production");
console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

जवाब कुछ ऐसा दिखता है:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

ऐसे क्रेडेंशियल का अनुरोध करने पर जो मौजूद नहीं है, `404` दिखता है:

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## क्रेडेंशियल बदलना

किसी सीक्रेट को बदलें. हालांकि, ऐसा करते समय, अनुमति वाली सूची के किसी नियम, टूल की परिभाषा या एनवायरमेंट वैरिएबल में कोई बदलाव न करें जो उसे रेफ़रंस करता है. अगले प्रॉक्सी रिज़ॉल्यूशन पर रोटेशन लागू होता है.

अनुरोध में `type` और वे फ़ील्ड शामिल होने चाहिए जिनमें आपको बदलाव करना है. जिन फ़ील्ड को नहीं बदला जाता उनकी मौजूदा वैल्यू बनी रहती हैं.

बियरर टोकन को रोटेट करना:

### Python

```
credential = client.credentials.update(
    id="github-production",
    type="bearer_token",
    token="ghp_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("github-production", {
    type: "bearer_token",
    token: "ghp_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "bearer_token",
    "token": "ghp_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

OAuth2 रीफ़्रेश टोकन को रोटेट करने का तरीका:

### Python

```
credential = client.credentials.update(
    id="jira-oauth",
    type="oauth2",
    refresh_token="rt_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("jira-oauth", {
    type: "oauth2",
    refresh_token: "rt_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/jira-oauth" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "oauth2",
    "refresh_token": "rt_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

जवाब में नया `update_time` दिखता है:

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

क्रेडेंशियल का `type`, क्रेडेंशियल बनाते समय तय किया जाता है. इसे बदलने के लिए, क्रेडेंशियल मिटाएं और नया क्रेडेंशियल बनाएं.

## क्रेडेंशियल मिटाना

जब किसी क्रेडेंशियल की ज़रूरत न हो, तो उसे और उससे जुड़े सेव किए गए सीक्रेट को मिटाएं.

### Python

```
client.credentials.delete(id="github-production")
```

### JavaScript

```
await client.credentials.delete("github-production");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

सही तरीके से मिटने पर, जवाब के तौर पर खाली ऑब्जेक्ट दिखता है:

```
{}
```

अगर अनुमति वाली सूची का कोई नियम, टूल या एनवायरमेंट वैरिएबल अब भी आईडी को रेफ़रंस कर रहा है, तो वह काम नहीं करेगा. इसलिए, उन्हें पहले अपडेट करें.

## फ़ील्ड रेफ़रंस

हर क्रेडेंशियल में मौजूद सामान्य फ़ील्ड:

| फ़ील्ड | प्रकार | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `id` | स्ट्रिंग | नहीं | यूनीक आइडेंटिफ़ायर. अगर इसे शामिल नहीं किया जाता है, तो इसे यूयूआईडी के तौर पर जनरेट किया जाता है. |
| `type` | स्ट्रिंग | हां | `bearer_token`, `oauth2`, `environment_variable` में से कोई एक. |
| `status` | स्ट्रिंग | रीड-ओनली | क्रेडेंशियल की मौजूदा स्थिति. |
| `create_time` | स्ट्रिंग | रीड-ओनली | आरएफ़सी 3339 फ़ॉर्मैट में बनाए जाने का टाइमस्टैंप. |
| `update_time` | स्ट्रिंग | रीड-ओनली | यह आखिरी अपडेट का आरएफ़सी 3339 टाइमस्टैंप है. |

`bearer_token` के लिए फ़ील्ड:

| फ़ील्ड | प्रकार | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `token` | स्ट्रिंग | हां | सिर्फ़ लिखने के लिए. टोकन की वैल्यू. |
| `header_name` | स्ट्रिंग | नहीं | इंजेक्ट किया जाने वाला हेडर. डिफ़ॉल्ट रूप से, यह `Authorization` पर सेट होता है. |
| `prefix` | स्ट्रिंग | नहीं | कीमत का प्रीफ़िक्स. डिफ़ॉल्ट रूप से, यह `Bearer` पर सेट होता है. किसी भी विकल्प को चुनने के लिए, `""` पर सेट करें. |

`oauth2` के लिए फ़ील्ड:

| फ़ील्ड | प्रकार | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `client_id` | स्ट्रिंग | हां | OAuth2 क्लाइंट आईडी. |
| `client_secret` | स्ट्रिंग | हां | सिर्फ़ लिखने के लिए. OAuth2 क्लाइंट सीक्रेट. |
| `refresh_token` | स्ट्रिंग | हां | सिर्फ़ लिखने के लिए. ऐक्सेस टोकन पाने के लिए इस्तेमाल किया गया रीफ़्रेश टोकन. |
| `token_url` | स्ट्रिंग | हां | टोकन सेवा देने वाली कंपनी का टोकन एंडपॉइंट. |
| `scopes` | ऐरे | नहीं | अनुरोध करने के लिए OAuth के दायरे. |

`environment_variable` के लिए फ़ील्ड:

| फ़ील्ड | प्रकार | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `value` | स्ट्रिंग | हां | सिर्फ़ लिखने के लिए. सीक्रेट वैल्यू. |
| `injection_location` | स्ट्रिंग या अरे | हां | सीक्रेट टोकन को कहां बदलना है. `header`, `query`, `body` में से एक या उससे ज़्यादा. |
| `trusted_domains` | ऐरे | नहीं | बदलाव करने के लिए, मंज़ूरी पा चुके डोमेन पैटर्न. |

## गड़बड़ियां

गड़बड़ियों के लिए, `message` और `code` के साथ JSON ऑब्जेक्ट मिलता है:

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| एचटीटीपी कोड स्थिति | `code` | वजह |
| --- | --- | --- |
| 400 | `invalid_request` | ज़रूरी फ़ील्ड मौजूद नहीं है, अज्ञात फ़ील्ड है, `type` काम नहीं करता या OAuth2 की पुष्टि नहीं हो पाई. |
| 404 | `not_found` | इस आईडी वाला कोई क्रेडेंशियल नहीं है. |
| 409 | `aborted` | उस आईडी वाला क्रेडेंशियल पहले से मौजूद है. |

जिन फ़ील्ड की पहचान नहीं हो पाती उन्हें अनदेखा करने के बजाय अस्वीकार कर दिया जाता है. साथ ही, गड़बड़ी के नाम में फ़ील्ड का नाम शामिल होता है:

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## आगे क्या करना है

- [एनवायरमेंट](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi): जानें कि एजेंट कोड कैसे चलाते हैं और फ़ाइलों को कैसे सेव करते हैं.
- [एजेंट की खास जानकारी](https://ai.google.dev/gemini-api/docs/agents?hl=hi): मैनेज किए जाने वाले एजेंट के मुख्य सिद्धांतों के बारे में जानें.
- [कस्टम एजेंट बनाना](https://ai.google.dev/gemini-api/docs/custom-agents?hl=hi): `AGENTS.md` और `SKILL.md` का इस्तेमाल करके, अपने एजेंट तय करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया."],[],[]]
