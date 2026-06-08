---
source_url: https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=hi
fetched_at: 2026-06-08T05:28:12.469089+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# दस्तावेज़ को समझना

Gemini मॉडल, PDF फ़ॉर्मैट में मौजूद दस्तावेज़ों को प्रोसेस कर सकते हैं. इसके लिए, वे दस्तावेज़ के पूरे कॉन्टेक्स्ट को समझने के लिए, नेटिव विज़न का इस्तेमाल करते हैं. यह सिर्फ़ टेक्स्ट निकालने से कहीं ज़्यादा है. इससे Gemini ये काम कर सकता है:

- टेक्स्ट, इमेज, डायग्राम, चार्ट, और टेबल के साथ-साथ कॉन्टेंट का विश्लेषण और व्याख्या करना. यह काम, 1, 000 पेजों तक के बड़े दस्तावेज़ों के लिए भी किया जा सकता है.
- जानकारी को [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=hi) फ़ॉर्मैट में निकालना.
- किसी दस्तावेज़ में मौजूद विज़ुअल और टेक्स्ट वाले एलिमेंट, दोनों के आधार पर खास जानकारी देना और सवालों के जवाब देना.
- दस्तावेज़ के कॉन्टेंट को ट्रांसक्रिप्ट करना.जैसे, एचटीएमएल में. साथ ही, लेआउट और फ़ॉर्मैटिंग को बनाए रखना, ताकि डाउनस्ट्रीम ऐप्लिकेशन में इसका इस्तेमाल किया जा सके.

आपके पास, PDF के अलावा दूसरे फ़ॉर्मैट वाले दस्तावेज़ों को भी उसी तरीके से पास करने का विकल्प है. हालांकि, Gemini उन्हें सामान्य टेक्स्ट के तौर पर देखेगा. इससे चार्ट या फ़ॉर्मैटिंग जैसे कॉन्टेक्स्ट नहीं दिखेंगे.

## पीडीएफ़ डेटा को इनलाइन पास करना

आपके पास अनुरोध में, पीडीएफ़ डेटा को इनलाइन पास करने का विकल्प है. यह छोटे दस्तावेज़ों या अस्थायी प्रोसेसिंग के लिए सबसे सही है. इसमें आपको बाद के अनुरोधों में फ़ाइल का रेफ़रंस देने की ज़रूरत नहीं होती. हमारा सुझाव है कि बड़े दस्तावेज़ों के लिए,
[Files API](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=hi#large-pdfs)
का इस्तेमाल करें. इससे अनुरोध की लेटेन्सी कम होगी और बैंडविड्थ का इस्तेमाल भी कम होगा. साथ ही, आपको कई बार होने वाले इंटरैक्शन में, इन दस्तावेज़ों का रेफ़रंस देना होगा.

यहां दिए गए उदाहरण में, पीडीएफ़ डेटा को इनलाइन पास करने का तरीका बताया गया है:

### Python

```
from google import genai
import base64

client = genai.Client()

with open('path/to/document.pdf', 'rb') as f:
    pdf_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {
            "type": "document",
            "data": base64.b64encode(pdf_bytes).decode('utf-8'),
            "mime_type": "application/pdf"
        },
        {"type": "text", "text": "Summarize this document"}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
    const pdfData = fs.readFileSync("path/to/document.pdf", {
        encoding: "base64"
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                data: pdfData,
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
PDF_PATH="path/to/document.pdf"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {
        "type": "document",
        "data": "'$(base64 $B64FLAGS $PDF_PATH)'",
        "mime_type": "application/pdf"
      },
      {"type": "text", "text": "Summarize this document"}
    ]
  }'
```

प्रोसेसिंग के लिए, स्थानीय तौर पर सेव की गई पीडीएफ़ फ़ाइल को भी अपलोड किया जा सकता है:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="file.pdf")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const uploadedFile = await ai.files.upload({
        file: "file.pdf",
        config: { mime_type: "application/pdf" }
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                uri: uploadedFile.uri,
                mime_type: uploadedFile.mime_type
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

## Files API का इस्तेमाल करके पीडीएफ़ अपलोड करना

हमारा सुझाव है कि बड़ी फ़ाइलों के लिए या एक ही दस्तावेज़ को कई अनुरोधों में फिर से इस्तेमाल करने के लिए, Files API का इस्तेमाल करें. इससे अनुरोध की लेटेन्सी कम होती है और बैंडविड्थ का इस्तेमाल भी कम होता है. ऐसा इसलिए, क्योंकि फ़ाइल अपलोड करने की प्रोसेस, मॉडल के अनुरोधों से अलग होती है.

### यूआरएल से बड़ी पीडीएफ़ फ़ाइलें

यूआरएल से बड़ी पीडीएफ़ फ़ाइलें अपलोड और प्रोसेस करने के लिए, File API का इस्तेमाल करें:

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://arxiv.org/pdf/2312.11805"

doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "uri": sample_doc.uri, "mime_type": sample_doc.mime_type},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

    const pdfBuffer = await fetch("https://arxiv.org/pdf/2312.11805")
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3.5-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### REST

```
PDF_PATH="https://arxiv.org/pdf/2312.11805"
DISPLAY_NAME="Gemini_paper"
PROMPT="Summarize this document"

# Download the PDF from the provided URL
wget -O "${DISPLAY_NAME}.pdf" "${PDF_PATH}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
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
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Create payload JSON file for safety
cat << EOF > payload.json
{
  "model": "gemini-3.5-flash",
  "input": [
    {"type": "text", "text": "${PROMPT}"},
    {"type": "document", "uri": "${file_uri}", "mime_type": "application/pdf"}
  ]
}
EOF

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -X POST \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm "${DISPLAY_NAME}.pdf"
rm payload.json
```

### स्थानीय तौर पर सेव की गई बड़ी पीडीएफ़ फ़ाइलें

### Python

```
from google import genai
import pathlib

client = genai.Client()

file_path = pathlib.Path('large_file.pdf')
sample_file = client.files.upload(
    file=file_path,
)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "uri": sample_file.uri, "mime_type": sample_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const file = await ai.files.upload({
        file: 'path-to-localfile.pdf',
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3.5-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### REST

```
PDF_PATH="path/to/large_file.pdf"
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME=TEXT
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -X POST \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "document", "uri": '$file_uri', "mime_type": "application/pdf"},
        {"type": "text", "text": "Can you add a few more lines to this poem?"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json
```

`[`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=hi)` को कॉल करके, यह पुष्टि की जा सकती है कि एपीआई ने अपलोड की गई फ़ाइल को सेव कर लिया है. साथ ही, इसका
मेटाडेटा भी पाया जा सकता है. सिर्फ़ `name` (और इसके साथ ही, `uri`) यूनीक होते हैं.

### Python

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.pdf')
fpath.write_text('hello')

file = client.files.upload(file='example.pdf')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
```

### REST

```
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl "https://generativelanguage.googleapis.com/v1beta/$name?key=$GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## एक से ज़्यादा पीडीएफ़ पास करना

Gemini API, एक ही अनुरोध में एक से ज़्यादा पीडीएफ़ दस्तावेज़ों (ज़्यादा से ज़्यादा 1,000 पेज) को प्रोसेस कर सकता है. हालांकि, इसके लिए ज़रूरी है कि दस्तावेज़ों और टेक्स्ट प्रॉम्प्ट का कुल साइज़, मॉडल के कॉन्टेक्स्ट विंडो में तय सीमा के अंदर हो.

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805"
doc_url_2 = "https://arxiv.org/pdf/2403.05530"

doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "uri": sample_pdf_1.uri, "mime_type": sample_pdf_1.mime_type},
        {"type": "document", "uri": sample_pdf_2.uri, "mime_type": sample_pdf_2.mime_type},
        {"type": "text", "text": prompt}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function uploadRemotePDF(url, displayName) {
    const pdfBuffer = await fetch(url)
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: displayName,
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    return file;
}

async function main() {
    const file1 = await uploadRemotePDF("https://arxiv.org/pdf/2312.11805", "PDF 1");
    const file2 = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2");

    const interaction = await ai.interactions.create({
        model: 'gemini-3.5-flash',
        input: [
            { type: "document", uri: file1.uri, mime_type: file1.mime_type },
            { type: "document", uri: file2.uri, mime_type: file2.mime_type },
            { type: "text", text: "What is the difference between each of the main benchmarks between these two papers? Output these in a table." }
        ],
    });

    console.log(interaction.output_text);
}

main();
```

### REST

```
DOC_URL_1="https://arxiv.org/pdf/2312.11805"
DOC_URL_2="https://arxiv.org/pdf/2403.05530"
DISPLAY_NAME_1="Gemini_paper"
DISPLAY_NAME_2="Gemini_1.5_paper"
PROMPT="What is the difference between each of the main benchmarks between these two papers? Output these in a table."

# Function to download and upload a PDF
upload_pdf() {
  local doc_url="$1"
  local display_name="$2"

  echo "Downloading ${display_name} from ${doc_url}..." >&2
  # Download the PDF
  wget -O "${display_name}.pdf" "${doc_url}" 2> /dev/null

  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c < "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}" >&2
  echo "NUM_BYTES: ${NUM_BYTES}" >&2

  local tmp_header_file="upload-header-${display_name}.tmp"

  # Initial resumable request
  # Using GEMINI_API_KEY instead of GOOGLE_API_KEY
  curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2> /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
  rm "${tmp_header_file}"

  echo "Upload URL for ${display_name}: ${upload_url}" >&2

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2> /dev/null > "file_info_${display_name}.json"

  local file_uri=$(jq -r ".file.uri" "file_info_${display_name}.json")
  echo "file_uri for ${display_name}: ${file_uri}" >&2

  # Clean up the downloaded PDF
  rm "${display_name}.pdf"

  echo "${file_uri}"
}

# Upload the first PDF
file_uri_1=$(upload_pdf "${DOC_URL_1}" "${DISPLAY_NAME_1}")

# Upload the second PDF
file_uri_2=$(upload_pdf "${DOC_URL_2}" "${DISPLAY_NAME_2}")

# Create payload JSON file for safety
cat << EOF > payload_multi.json
{
  "model": "gemini-3.5-flash",
  "input": [
    {"type": "document", "uri": "${file_uri_1}", "mime_type": "application/pdf"},
    {"type": "document", "uri": "${file_uri_2}", "mime_type": "application/pdf"},
    {"type": "text", "text": "${PROMPT}"}
  ]
}
EOF

# Now create an interaction using both files
# Using GEMINI_API_KEY instead of GOOGLE_API_KEY
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -X POST \
    -d @payload_multi.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm payload_multi.json
rm "file_info_${DISPLAY_NAME_1}.json"
rm "file_info_${DISPLAY_NAME_2}.json"
```

## तकनीकी जानकारी

Gemini, 50 एमबी या 1,000 पेजों तक की पीडीएफ़ फ़ाइलों के साथ काम करता है. यह सीमा, इनलाइन डेटा और Files API से अपलोड किए गए डेटा, दोनों पर लागू होती है. दस्तावेज़ का हर पेज, 258 टोकन के बराबर होता है.

मॉडल के [कॉन्टेक्स्ट विंडो](https://ai.google.dev/gemini-api/docs/long-context?hl=hi) के अलावा, किसी दस्तावेज़ में पिक्सल की संख्या की कोई खास सीमा नहीं होती. हालांकि, बड़े पेजों को ज़्यादा से ज़्यादा 3072 x 3072 रिज़ॉल्यूशन तक स्केल डाउन किया जाता है. इस दौरान, उनके ओरिजनल आसपेक्ट रेशियो को बनाए रखा जाता है. वहीं, छोटे पेजों को 768 x 768 पिक्सल तक स्केल अप किया जाता है. कम साइज़ वाले पेजों के लिए, बैंडविड्थ के अलावा कोई शुल्क कम नहीं किया जाता. वहीं, ज़्यादा रिज़ॉल्यूशन वाले पेजों के लिए, परफ़ॉर्मेंस में कोई सुधार नहीं किया जाता.

### Gemini 3 के मॉडल

Gemini 3 में, `media_resolution` पैरामीटर की मदद से, मल्टीमॉडल विज़न प्रोसेसिंग पर ज़्यादा कंट्रोल मिलता है. अब हर मीडिया पार्ट के लिए, रिज़ॉल्यूशन को कम, सामान्य या ज़्यादा पर सेट किया जा सकता है. इस सुविधा के जुड़ने के बाद, पीडीएफ़ दस्तावेज़ों की प्रोसेसिंग को अपडेट कर दिया गया है:

1. **नेटिव टेक्स्ट शामिल करना:** पीडीएफ़ में नेटिव तौर पर एम्बेड किए गए टेक्स्ट को निकालकर, मॉडल को उपलब्ध कराया जाता है.
2. **बिलिंग और टोकन की रिपोर्टिंग:**
   - पीडीएफ़ में मौजूद **नेटिव टेक्स्ट** से जनरेट होने वाले टोकन के लिए, **कोई शुल्क नहीं लिया जाता**.
   - एपीआई के जवाब के `usage_metadata` सेक्शन में, पीडीएफ़ पेजों को (इमेज के तौर पर) प्रोसेस करने से जनरेट होने वाले टोकन को अब `IMAGE` मोडैलिटी में गिना जाता है. पहले के कुछ वर्शन में, इन्हें `DOCUMENT` मोडैलिटी में गिना जाता था.

### दस्तावेज़ के टाइप

तकनीकी तौर पर, दस्तावेज़ को समझने के लिए, TXT, Markdown, HTML, XML वगैरह जैसे अन्य MIME टाइप पास किए जा सकते हैं. हालांकि, दस्तावेज़ का विज़न ***सिर्फ़ पीडीएफ़ को समझ पाता है***. अन्य टाइप को सिर्फ़ टेक्स्ट के तौर पर निकाला जाएगा. साथ ही, मॉडल उन फ़ाइलों के रेंडरिंग में दिखने वाले कॉन्टेंट की व्याख्या नहीं कर पाएगा. चार्ट, डायग्राम, एचटीएमएल टैग, Markdown फ़ॉर्मैटिंग वगैरह जैसे फ़ाइल टाइप से जुड़ी कोई भी जानकारी नहीं दिखेगी.

फ़ाइल इनपुट के अन्य तरीकों के बारे में जानने के लिए, [फ़ाइल इनपुट के तरीके](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=hi) से जुड़ा लेख पढ़ें.

### सबसे सही तरीके

सर्वोत्तम परिणामों के लिएः

- अपलोड करने से पहले, पेजों को सही ओरिएंटेशन में घुमाएं.
- धुंधले पेजों का इस्तेमाल न करें.
- अगर एक ही पेज का इस्तेमाल किया जा रहा है, तो टेक्स्ट प्रॉम्प्ट को पेज के बाद रखें.

## आगे क्या करना है

ज़्यादा जानने के लिए, ये लेख पढ़ें और वीडियो देखें:

- [फ़ाइल प्रॉम्प्ट करने की रणनीतियां](https://ai.google.dev/gemini-api/docs/interactions/files?hl=hi#prompt-guide): Gemini API, टेक्स्ट, इमेज, ऑडियो, और वीडियो डेटा के साथ प्रॉम्प्ट करने की सुविधा देता है. इसे मल्टीमॉडल प्रॉम्प्टिंग भी कहा जाता है.
- [सिस्टम के निर्देश](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=hi#system-instructions):
  सिस्टम के निर्देशों की मदद से, अपनी खास ज़रूरतों और इस्तेमाल के उदाहरणों के हिसाब से, मॉडल के व्यवहार को कंट्रोल किया जा सकता है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया."],[],[]]
