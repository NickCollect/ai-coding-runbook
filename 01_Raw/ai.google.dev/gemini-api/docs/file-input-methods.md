---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi
fetched_at: 2026-10-26T05:56:55.089303+00:00
title: "\u092b\u093c\u093e\u0907\u0932 \u0907\u0928\u092a\u0941\u091f \u0915\u0930\u0928\u0947 \u0915\u0947 \u0924\u0930\u0940\u0915\u0947 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# फ़ाइल इनपुट करने के तरीके

इस गाइड में, Gemini API से अनुरोध करते समय इमेज, ऑडियो, वीडियो, और दस्तावेज़ जैसी मीडिया फ़ाइलें शामिल करने के अलग-अलग तरीके बताए गए हैं.
नए तरीके, Gemini API के सभी एंडपॉइंट में काम करते हैं. इनमें बैच, इंटरैक्शन, और Live API शामिल हैं.
सही तरीका चुनने के लिए, इन बातों का ध्यान रखें: आपकी फ़ाइल का साइज़, आपका डेटा कहां सेव है, और आपको फ़ाइल का इस्तेमाल कितनी बार करना है.

किसी फ़ाइल को इनपुट के तौर पर शामिल करने का सबसे आसान तरीका यह है कि किसी स्थानीय फ़ाइल को पढ़ा जाए और उसे प्रॉम्प्ट में शामिल किया जाए. यहां दिए गए उदाहरण में, किसी स्थानीय PDF फ़ाइल को पढ़ने का तरीका बताया गया है. इस तरीके से अपलोड किए जाने वाले PDF का साइज़ 50 एमबी से ज़्यादा नहीं होना चाहिए. फ़ाइल इनपुट टाइप और सीमाओं की पूरी सूची देखने के लिए, [इनपुट मेथड की तुलना करने वाली टेबल](#method-comparison) देखें.

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("my_local_file.pdf"));
String base64Pdf = Base64.getEncoder().encodeToString(pdfBytes);

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    pdfBytes, err := os.ReadFile("my_local_file.pdf")
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(pdfBytes)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## इनपुट के तरीकों की तुलना

यहां दी गई टेबल में, हर इनपुट तरीके की तुलना फ़ाइल की सीमाओं और इस्तेमाल के सबसे सही तरीकों से की गई है. ध्यान दें कि फ़ाइल का साइज़, फ़ाइल टाइप और फ़ाइल को प्रोसेस करने के लिए इस्तेमाल किए गए मॉडल या टोकनाइज़र के हिसाब से अलग-अलग हो सकता है.

| तरीका | इन स्थितियों में बेहतर है | अधिकतम फ़ाइल आकार | परसिस्टेंस |
| --- | --- | --- | --- |
| **इनलाइन डेटा** | तेज़ी से टेस्टिंग, छोटी फ़ाइलें, रीयल-टाइम ऐप्लिकेशन. | हर अनुरोध या पेलोड के लिए 100 एमबी   (**PDF के लिए 50 एमबी**) | कोई नहीं (हर अनुरोध के साथ भेजी जाती है) |
| **File API की मदद से अपलोड करना** | बड़ी फ़ाइलें और वे फ़ाइलें जिनका इस्तेमाल कई बार किया गया है. | हर फ़ाइल का साइज़ 2 जीबी और हर प्रोजेक्ट के लिए   फ़ाइलों का कुल साइज़ 20 जीबी तक हो सकता है | 48 घंटे |
| **File API GCS यूआरआई रजिस्ट्रेशन** | Google Cloud Storage में पहले से मौजूद बड़ी फ़ाइलें और वे फ़ाइलें जिनका इस्तेमाल कई बार किया गया है. | हर फ़ाइल के लिए 2 जीबी, स्टोरेज की कोई सीमा नहीं | कोई नहीं (हर अनुरोध के हिसाब से फ़ेच किया जाता है). एक बार रजिस्टर करने पर, 30 दिनों तक ऐक्सेस मिल सकता है. |
| **बाहरी यूआरएल** | सार्वजनिक डेटा या क्लाउड बकेट (AWS, Azure, GCS) में मौजूद डेटा को फिर से अपलोड किए बिना. | हर फ़ाइल का साइज़ 15 एमबी से ज़्यादा नहीं होना चाहिए | कोई नहीं (हर अनुरोध के हिसाब से फ़ेच किया जाता है) |

## इनलाइन डेटा

छोटी फ़ाइलों (100 एमबी से कम या PDF के लिए 50 एमबी) के लिए, डेटा को सीधे तौर पर अनुरोध के पेलोड में पास किया जा सकता है. यह तरीका, तुरंत किए जाने वाले टेस्ट या रीयल-टाइम में कुछ समय के लिए उपलब्ध डेटा को मैनेज करने वाले ऐप्लिकेशन के लिए सबसे आसान है. डेटा को base64 एन्कोड की गई स्ट्रिंग के तौर पर उपलब्ध कराया जा सकता है. इसके अलावा, सीधे तौर पर स्थानीय फ़ाइलों को पढ़कर भी डेटा उपलब्ध कराया जा सकता है.

किसी स्थानीय फ़ाइल से पढ़ने के उदाहरण के लिए, इस पेज की शुरुआत में दिया गया उदाहरण देखें.

### किसी यूआरएल से फ़ेच करना

किसी यूआरएल से फ़ाइल फ़ेच की जा सकती है. साथ ही, उसे बाइट में बदलकर इनपुट में शामिल किया जा सकता है.

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

String docUrl = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf";
HttpClient httpClient = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(docUrl)).build();
byte[] docData = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();
String base64Pdf = Base64.getEncoder().encodeToString(docData);

String prompt = "Summarize this document";

Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    docURL := "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
    resp, err := http.Get(docURL)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    docData, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(docData)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.8-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

File API को बड़ी फ़ाइलों (2 जीबी तक) या उन फ़ाइलों के लिए डिज़ाइन किया गया है जिनका इस्तेमाल आपको कई अनुरोधों में करना है.

### फ़ाइल अपलोड करने का स्टैंडर्ड तरीका

Gemini API में कोई स्थानीय फ़ाइल अपलोड करें. इस तरह अपलोड की गई फ़ाइलों को कुछ समय के लिए (48 घंटे) सेव किया जाता है. साथ ही, मॉडल के ज़रिए उन्हें आसानी से ऐक्सेस करने के लिए प्रोसेस किया जाता है.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File docFile =
    client.files.upload(
        new java.io.File("path/to/your/sample.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .uri(docFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(docFile.mimeType().orElse("application/pdf")))
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    docFile, err := client.Files.UploadFromPath(ctx, "path/to/your/sample.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(docFile.URI),
                    MimeType: interactions.DocumentContentMimeType(docFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Google Cloud Storage की फ़ाइलें रजिस्टर करना

अगर आपका डेटा पहले से ही Google Cloud Storage में है, तो आपको उसे डाउनलोड करके फिर से अपलोड करने की ज़रूरत नहीं है. इसे सीधे तौर पर File API के साथ रजिस्टर किया जा सकता है.

1. हर बकेट के लिए, **सर्विस एजेंट** को ऐक्सेस दें

   1. अपने Google Cloud प्रोजेक्ट में Gemini API चालू करें.
   2. सर्विस एजेंट बनाएं:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. Gemini API सेवा एजेंट को, आपके स्टोरेज बकेट पढ़ने की **अनुमतियां दें**.

      उपयोगकर्ता को इस सर्विस एजेंट को, उन स्टोरेज बकेट के लिए `Storage Object Viewer`
      [IAM भूमिका](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=hi#storage.objectViewer)
      असाइन करनी होगी जिनका इस्तेमाल करना है.

   डिफ़ॉल्ट रूप से, यह ऐक्सेस कभी खत्म नहीं होता. हालांकि, इसे किसी भी समय बदला जा सकता है. अनुमतियां देने के लिए, [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=hi) कमांड का भी इस्तेमाल किया जा सकता है.
2. अपनी सेवा की पुष्टि करना

   **ज़रूरी शर्तें**

   - एपीआई चालू करना
   - ज़रूरी अनुमतियों के साथ कोई सेवा खाता या एजेंट बनाएं.

   सबसे पहले, आपको उस सेवा के तौर पर पुष्टि करनी होगी जिसके पास स्टोरेज ऑब्जेक्ट व्यूअर की अनुमतियां हैं. यह इस बात पर निर्भर करता है कि आपकी फ़ाइल मैनेजमेंट का कोड किस एनवायरमेंट में चलेगा.

   **Google Cloud के बाहर**

   अगर आपका कोड Google Cloud के बाहर से चल रहा है, जैसे कि आपका डेस्कटॉप, तो Google Cloud Console से खाते के क्रेडेंशियल डाउनलोड करें. इसके लिए, यह तरीका अपनाएं:

   1. [Service Account console](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=hi) पर जाएं
   2. काम का सेवा खाता चुनें
   3. **कुंजियां** टैब को चुनें. इसके बाद, **कुंजी जोड़ें, नई कुंजी बनाएं** को चुनें
   4. **JSON** कुंजी टाइप चुनें. साथ ही, यह नोट करें कि फ़ाइल आपके डिवाइस पर कहां डाउनलोड हुई है.

   ज़्यादा जानकारी के लिए, [सेवा खाते की कुंजी के मैनेजमेंट](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=hi) के बारे में Google Cloud का आधिकारिक दस्तावेज़ देखें.

   इसके बाद, पुष्टि करने के लिए इन कमांड का इस्तेमाल करें. इन कमांड में यह माना जाता है कि आपकी सेवा खाते की फ़ाइल, मौजूदा डायरेक्ट्री में है और उसका नाम `service-account.json` है.

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

   अगर Google Cloud में सीधे तौर पर कोई काम किया जा रहा है, जैसे कि [Cloud Run फ़ंक्शन](https://cloud.google.com/functions?hl=hi) या [Compute Engine इंस्टेंस](https://cloud.google.com/products/compute?hl=hi) का इस्तेमाल करके, तो आपके पास इंप्लिसिट क्रेडेंशियल होंगे. हालांकि, आपको सही स्कोप देने के लिए फिर से पुष्टि करनी होगी.

   ### Python

   इस कोड के लिए ज़रूरी है कि सेवा ऐसे एनवायरमेंट में चल रही हो जहां [ऐप्लिकेशन के डिफ़ॉल्ट क्रेडेंशियल](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=hi) अपने-आप मिल सकते हैं. जैसे, Cloud Run या Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   इस कोड के लिए ज़रूरी है कि सेवा ऐसे एनवायरमेंट में चल रही हो जहां [ऐप्लिकेशन के डिफ़ॉल्ट क्रेडेंशियल](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=hi) अपने-आप मिल सकते हैं. जैसे, Cloud Run या Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.List;

List<String> gcsReadScopes =
    Arrays.asList(
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/cloud-platform");

String serviceAccountFile = "service-account.json";

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream(serviceAccountFile))
        .createScoped(gcsReadScopes);
```

### ऐप पर जाएं

```
package main

import (
    "log"

    "google.golang.org/genai"
)

func main() {
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    _ = cc.Credentials
}
```

### सीएलआई

यह एक इंटरैक्टिव कमांड है. Compute Engine जैसी सेवाओं के लिए, कॉन्फ़िगरेशन लेवल पर चल रही सेवा से स्कोप अटैच किए जा सकते हैं. उदाहरण के लिए, [उपयोगकर्ता के मैनेज किए गए सेवा दस्तावेज़](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=hi#using) देखें.

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. फ़ाइल रजिस्टर करना (Files API)
   फ़ाइलों को रजिस्टर करने के लिए, Files API का इस्तेमाल करें. साथ ही, Files API का ऐसा पाथ जनरेट करें जिसका इस्तेमाल Gemini API में सीधे तौर पर किया जा सकता है.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.8-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.8-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.RegisterFilesResponse;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream("service-account.json"))
        .createScoped(
            Arrays.asList(
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/cloud-platform"));

Client client = Client.builder().credentials(credentials).build();

RegisterFilesResponse registeredGcsFiles =
    client.files.registerFiles(
        credentials,
        Arrays.asList("gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"),
        null);

String prompt = "Summarize this file.";

for (File f : registeredGcsFiles.files().orElse(Collections.emptyList())) {
  System.out.println(f.name().orElse(""));

  Content textContent = TextContent.builder().text(prompt).build();
  Content docContent =
      DocumentContent.builder()
          .uri(f.uri().orElse(""))
          .mimeType(DocumentContentMimeType.of(f.mimeType().orElse("application/pdf")))
          .build();

  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(InteractionsInput.ofContent(Arrays.asList(textContent, docContent)))
          .build();

  Interaction interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
  System.out.println(interaction.outputText().orElse(""));
}
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    client, err := genai.NewClient(ctx, cc)
    if err != nil {
        log.Fatal(err)
    }

    registeredGcsFiles, err := client.Files.RegisterFiles(
        ctx,
        []string{"gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"},
        cc.Credentials,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this file."

    for _, f := range registeredGcsFiles.Files {
        fmt.Println(f.Name)
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput([]interactions.Content{
                    interactions.NewContent(interactions.TextContent{
                        Text: prompt,
                    }),
                    interactions.NewContent(interactions.DocumentContent{
                        URI:      genai.Ptr(f.URI),
                        MimeType: interactions.DocumentContentMimeType(f.MIMEType).ToPointer(),
                    }),
                }),
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        if res.Interaction.OutputText != nil {
            fmt.Println(*res.Interaction.OutputText)
        }
    }
}
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

## एक्सटर्नल एचटीटीपी / सीमित ऐक्सेस देने वाले यूआरएल

आपके पास सार्वजनिक तौर पर ऐक्सेस किए जा सकने वाले एचटीटीपीएस यूआरएल या पहले से हस्ताक्षर किए गए यूआरएल को सीधे अपने अनुरोध में पास करने का विकल्प होता है. Gemini API, प्रोसेसिंग के दौरान कॉन्टेंट को सुरक्षित तरीके से फ़ेच करेगा.
यह उन फ़ाइलों के लिए सबसे सही है जिन्हें आपको फिर से अपलोड नहीं करना है. हर फ़ाइल का साइज़ 15 एमबी तक हो सकता है. बड़ी फ़ाइलों के लिए, [File API](#file-api) का इस्तेमाल करें.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.8-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### सुलभता

पुष्टि करें कि आपके दिए गए यूआरएल, ऐसे पेजों पर रीडायरेक्ट न करते हों जहां लॉगिन करने की ज़रूरत हो या जिन पर पेवॉल लागू हो. निजी डेटाबेस के लिए, पक्का करें कि आपने सही ऐक्सेस अनुमतियों और समयसीमा खत्म होने की तारीख के साथ हस्ताक्षर किया गया यूआरएल बनाया हो.

### सुरक्षा जांच

सिस्टम, यूआरएल पर मौजूद कॉन्टेंट की जांच करता है, ताकि यह पुष्टि की जा सके कि वह सुरक्षा और नीति के मानकों के मुताबिक है. अगर यूआरएल इस जांच में पास नहीं होता है, तो आपको `url_retrieval_status` का `URL_RETRIEVAL_STATUS_UNSAFE` मिलेगा.

### इस्तेमाल किए जा सकने वाले कॉन्टेंट टाइप

यहां दिए गए फ़ाइल टाइप और सीमाओं के बारे में शुरुआती जानकारी दी गई है. यह पूरी जानकारी नहीं है. सपोर्ट किए गए टाइप का सेट बदल सकता है. साथ ही, यह इस्तेमाल किए जा रहे मॉडल और टोकनाइज़र के वर्शन के हिसाब से अलग-अलग हो सकता है. काम न करने वाले टाइप की वजह से गड़बड़ी होगी.
इसके अलावा, इन फ़ाइल टाइप के लिए कॉन्टेंट सिर्फ़ उन यूआरएल से वापस पाया जा सकता है जिन्हें सार्वजनिक तौर पर ऐक्सेस किया जा सकता है.

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

- **सही तरीका चुनें:** कम समय के लिए इस्तेमाल की जाने वाली छोटी फ़ाइलों के लिए, इनलाइन डेटा का इस्तेमाल करें.
  बड़ी या अक्सर इस्तेमाल की जाने वाली फ़ाइलों के लिए, File API का इस्तेमाल करें. पहले से ऑनलाइन होस्ट किए गए डेटा के लिए, बाहरी यूआरएल का इस्तेमाल करें.
- **MIME टाइप तय करें:** फ़ाइल के डेटा को सही तरीके से प्रोसेस करने के लिए, हमेशा सही MIME टाइप दें.
- **गड़बड़ियों को ठीक करना:** अपने कोड में गड़बड़ी ठीक करने की सुविधा लागू करें, ताकि नेटवर्क फ़ेल होने, फ़ाइल ऐक्सेस करने में आने वाली समस्याओं या एपीआई से जुड़ी गड़बड़ियों जैसी संभावित समस्याओं को मैनेज किया जा सके.

## सीमाएं

- फ़ाइल के साइज़ की सीमाएं, अपलोड करने के तरीके ([तुलना करने वाली टेबल](#method-comparison) देखें) और फ़ाइल टाइप के हिसाब से अलग-अलग होती हैं.
- इनलाइन डेटा से, अनुरोध के पेलोड का साइज़ बढ़ जाता है.
- File API के ज़रिए अपलोड की गई फ़ाइलें कुछ समय के लिए उपलब्ध होती हैं. ये 48 घंटे बाद मिट जाती हैं.
- बाहरी यूआरएल से फ़ेच की गई हर फ़ाइल का साइज़ 15 एमबी से ज़्यादा नहीं होना चाहिए. साथ ही, यह कुछ खास तरह के कॉन्टेंट के साथ काम करता है.

## आगे क्या करना है

- [Google AI Studio](http://aistudio.google.com/?hl=hi) का इस्तेमाल करके, मल्टीमॉडल प्रॉम्प्ट लिखने की कोशिश करें.
- अपने प्रॉम्प्ट में फ़ाइलें शामिल करने के बारे में जानकारी पाने के लिए, [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=hi), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=hi), और [Document processing](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi) गाइड देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-07 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-07 (UTC) को अपडेट किया गया."],[],[]]
