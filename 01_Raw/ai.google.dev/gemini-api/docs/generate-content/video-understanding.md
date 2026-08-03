---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=hi
fetched_at: 2026-08-03T04:31:15.139960+00:00
title: "\u0935\u0940\u0921\u093f\u092f\u094b \u0915\u0940 \u092c\u093e\u0930\u0940\u0915\u093c\u0940 \u0938\u0947 \u092a\u0939\u091a\u093e\u0928 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# वीडियो की बारीक़ी से पहचान करना

> वीडियो जनरेट करने के बारे में जानने के लिए, [Veo](https://ai.google.dev/gemini-api/docs/video?hl=hi) की गाइड देखें.

Gemini मॉडल, वीडियो प्रोसेस कर सकते हैं. इससे डेवलपर, वीडियो से जुड़े कई ऐसे काम कर सकते हैं जिनके लिए पहले, खास डोमेन के मॉडल की ज़रूरत होती थी.
Gemini की विज़न सुविधाओं में ये काम शामिल हैं: वीडियो के बारे में बताना, वीडियो को सेगमेंट में बांटना, वीडियो से जानकारी निकालना, वीडियो के कॉन्टेंट से जुड़े सवालों के जवाब देना, और वीडियो में मौजूद किसी खास टाइमस्टैंप के बारे में बताना.

Gemini को इन तरीकों से वीडियो इनपुट के तौर पर दिया जा सकता है:

| इनपुट विधि | सबसे बड़ा साइज़ | सुझाया गया इस्तेमाल |
| --- | --- | --- |
| [File API](#upload-video) | 20 जीबी (पैसे चुकाकर) / 2 जीबी (मुफ़्त) | बड़ी फ़ाइलें (100 एमबी से ज़्यादा), लंबे वीडियो (10 मिनट से ज़्यादा), दोबारा इस्तेमाल की जा सकने वाली फ़ाइलें. |
| [Cloud Storage रजिस्ट्रेशन](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi#registration) | हर फ़ाइल के लिए 2 जीबी (स्टोरेज की कोई सीमा नहीं) | बड़ी फ़ाइलें (100 एमबी से ज़्यादा), लंबे वीडियो (10 मिनट से ज़्यादा), लगातार इस्तेमाल की जा सकने वाली, दोबारा इस्तेमाल की जा सकने वाली फ़ाइलें. |
| [इनलाइन डेटा](#inline-video) | 100 एमबी से कम | छोटी फ़ाइलें (100 एमबी से कम), कम अवधि वाले वीडियो (एक मिनट से कम), एक बार इस्तेमाल किए जाने वाले इनपुट. |
| [YouTube के यूआरएल](#youtube) | लागू नहीं | YouTube के सार्वजनिक वीडियो. |

> **ध्यान दें:** ज़्यादातर मामलों में, [File API](#upload-video) का इस्तेमाल करने का सुझाव दिया जाता है. खास तौर पर, 100 एमबी से बड़ी फ़ाइलों के लिए या जब आपको एक ही फ़ाइल को कई अनुरोधों में दोबारा इस्तेमाल करना हो.

[फ़ाइल इनपुट के अन्य तरीकों के बारे में जानने के लिए, जैसे कि बाहरी यूआरएल या Google Cloud में सेव की गई फ़ाइलों का इस्तेमाल करना, फ़ाइल इनपुट के तरीके वाली गाइड देखें.](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi)

### वीडियो फ़ाइल अपलोड करना

यहां दिया गया कोड, एक सैंपल वीडियो डाउनलोड करता है. इसके बाद, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) का इस्तेमाल करके उसे अपलोड करता है.
वीडियो के प्रोसेस होने का इंतज़ार करता है. इसके बाद, अपलोड की गई फ़ाइल के रेफ़रंस का इस्तेमाल करके,
वीडियो की खास जानकारी देता है.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.6-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Files API का इस्तेमाल हमेशा तब करें, जब अनुरोध का कुल साइज़ (इसमें फ़ाइल, टेक्स्ट प्रॉम्प्ट, सिस्टम के निर्देश वगैरह शामिल हैं) 20 एमबी से ज़्यादा हो, वीडियो की अवधि ज़्यादा हो या अगर आपको एक ही वीडियो को कई प्रॉम्प्ट में इस्तेमाल करना हो.
File API, वीडियो फ़ाइल फ़ॉर्मैट को सीधे स्वीकार करता है.

मीडिया फ़ाइलों के साथ काम करने के बारे में ज़्यादा जानने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) देखें.

### वीडियो डेटा को इनलाइन पास करना

File API का इस्तेमाल करके वीडियो फ़ाइल अपलोड करने के बजाय, `generateContent` के अनुरोध में सीधे छोटे वीडियो पास किए जा सकते हैं. यह सुविधा, 20 एमबी से कम साइज़ वाले छोटे वीडियो के लिए सही है.

यहां, इनलाइन वीडियो डेटा देने का एक उदाहरण दिया गया है:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### YouTube के यूआरएल पास करना

YouTube के यूआरएल को, Gemini API में सीधे अपने अनुरोध के हिस्से के तौर पर इस तरह पास किया जा सकता है:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**सीमाएं:**

- मुफ़्त टियर के लिए, हर दिन YouTube के आठ घंटे से ज़्यादा के वीडियो अपलोड नहीं किए जा सकते.
- पैसे चुकाकर इस्तेमाल किए जाने वाले टियर के लिए, वीडियो की अवधि के हिसाब से कोई सीमा नहीं है.
- Gemini 2.5 से पहले के मॉडल के लिए, हर अनुरोध में सिर्फ़ एक वीडियो अपलोड किया जा सकता है. Gemini 2.5 और इसके बाद के मॉडल के लिए, हर अनुरोध में ज़्यादा से ज़्यादा 10 वीडियो अपलोड किए जा सकते हैं.
- सिर्फ़ सार्वजनिक वीडियो अपलोड किए जा सकते हैं. निजी या 'सबके लिए मौजूद नहीं' के तौर पर उपलब्ध वीडियो अपलोड नहीं किए जा सकते.

## लंबे वीडियो के लिए, कॉन्टेक्स्ट कैश मेमोरी में सेव करने की सुविधा का इस्तेमाल करना

अगर वीडियो 10 मिनट से ज़्यादा लंबा है या आपको एक ही वीडियो फ़ाइल के लिए कई अनुरोध करने हैं, तो लागत कम करने और इंतज़ार का समय कम करने के लिए, [कॉन्टेक्स्ट कैश मेमोरी में सेव करने की सुविधा](https://ai.google.dev/gemini-api/docs/caching?hl=hi) का इस्तेमाल करें. कॉन्टेक्स्ट कैश मेमोरी में सेव करने की सुविधा से, वीडियो को एक बार प्रोसेस किया जा सकता है. इसके बाद, टोकन को बाद की क्वेरी के लिए दोबारा इस्तेमाल किया जा सकता है. यह सुविधा, चैट सेशन या लंबी अवधि वाले कॉन्टेंट के बार-बार विश्लेषण के लिए सही है.

## कॉन्टेंट में मौजूद टाइमस्टैंप के बारे में बताना

`MM:SS` फ़ॉर्मैट वाले टाइमस्टैंप का इस्तेमाल करके, वीडियो में मौजूद किसी खास समय के बारे में सवाल पूछे जा सकते हैं.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## वीडियो से अहम जानकारी निकालना

Gemini मॉडल, वीडियो के कॉन्टेंट को समझने के लिए बेहतरीन सुविधाएं देते हैं. इसके लिए, ये मॉडल **ऑडियो और विज़ुअल**, दोनों तरह के स्ट्रीम से जानकारी प्रोसेस करते हैं. इससे, वीडियो में क्या हो रहा है, इसकी जानकारी जनरेट करने और वीडियो के कॉन्टेंट के बारे में सवालों के जवाब देने के साथ-साथ, कई तरह की अहम जानकारी निकाली जा सकती है.

विज़ुअल जानकारी के लिए, मॉडल **हर सेकंड एक फ़्रेम** (एफ़पीएस) की दर से वीडियो का सैंपल लेता है. सैंपल लेने की यह डिफ़ॉल्ट दर, ज़्यादातर कॉन्टेंट के लिए सही है. हालांकि, ध्यान दें कि तेज़ी से चलने वाले वीडियो या सीन में तेज़ी से बदलाव होने वाले वीडियो में, यह दर कुछ जानकारी छोड़ सकती है.
तेज़ी से चलने वाले ऐसे कॉन्टेंट के लिए, फ़्रेम रेट को अपने हिसाब से [सेट करें](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## वीडियो प्रोसेसिंग को पसंद के मुताबिक बनाना

Gemini API में, वीडियो प्रोसेसिंग को पसंद के मुताबिक बनाया जा सकता है. इसके लिए, क्लिप करने के इंटरवल सेट किए जा सकते हैं या फ़्रेम रेट के हिसाब से सैंपल लेने की सुविधा दी जा सकती है.

### क्लिप करने के इंटरवल सेट करना

`videoMetadata` में, वीडियो के शुरू और खत्म होने के ऑफ़सेट की जानकारी देकर, वीडियो को क्लिप किया जा सकता है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.6-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### फ़्रेम रेट को अपने हिसाब से सेट करना

`videoMetadata` में `fps` आर्ग्युमेंट पास करके, फ़्रेम रेट के हिसाब से सैंपल लेने की सुविधा को अपने हिसाब से सेट किया जा सकता है.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

डिफ़ॉल्ट रूप से, वीडियो से हर सेकंड एक फ़्रेम (एफ़पीएस) का सैंपल लिया जाता है. लंबे वीडियो के लिए, कम एफ़पीएस (< 1) सेट किया जा सकता है. यह सुविधा, खास तौर पर ऐसे वीडियो के लिए काम की है जिनमें ज़्यादातर स्थिर सीन होते हैं. जैसे, लेक्चर. ऐसे वीडियो के लिए ज़्यादा एफ़पीएस का इस्तेमाल करें जिनमें समय के हिसाब से बारीकी से विश्लेषण करने की ज़रूरत होती है. जैसे, तेज़ी से होने वाली कार्रवाई को समझना या तेज़ गति से होने वाली गतिविधि को ट्रैक करना.

## काम करने वाले वीडियो फ़ॉर्मैट

Gemini, इन वीडियो फ़ॉर्मैट के MIME टाइप के साथ काम करता है:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## वीडियो के बारे में तकनीकी जानकारी

- **काम करने वाले मॉडल और कॉन्टेक्स्ट**: सभी Gemini मॉडल, वीडियो डेटा को प्रोसेस कर सकते हैं.
  - 10 लाख कॉन्टेक्स्ट विंडो वाले मॉडल, डिफ़ॉल्ट मीडिया रिज़ॉल्यूशन पर एक घंटे तक के वीडियो या कम मीडिया रिज़ॉल्यूशन पर तीन घंटे तक के वीडियो प्रोसेस कर सकते हैं.
- **File API से प्रोसेसिंग**: File API का इस्तेमाल करने पर, वीडियो को हर सेकंड एक
  फ़्रेम (एफ़पीएस) पर सेव किया जाता है. साथ ही, ऑडियो को 1 केबीपीएस (सिंगल चैनल) पर प्रोसेस किया जाता है.
  हर सेकंड टाइमस्टैंप जोड़े जाते हैं.
  - इन्फ़रंस को बेहतर बनाने के लिए, आने वाले समय में इन दरों में बदलाव हो सकता है.
  - फ़्रेम रेट को अपने हिसाब से सेट करके, हर सेकंड एक फ़्रेम (एफ़पीएस) की दर को [बदला जा सकता है](#custom-frame-rate).
- **टोकन की गिनती**: वीडियो के हर सेकंड को इस तरह टोकन में बदला जाता है:
  - अलग-अलग फ़्रेम (हर सेकंड एक फ़्रेम की दर से सैंपल लिए गए):
    - अगर [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=hi#MediaResolution) को कम पर सेट किया जाता है, तो फ़्रेम को हर फ़्रेम के लिए 66 टोकन की दर से टोकन में बदला जाता है.
    - अन्य मामलों में, फ़्रेम को हर फ़्रेम के लिए 258 टोकन की दर से टोकन में बदला जाता है.
  - ऑडियो: हर सेकंड 32 टोकन.
  - इसमें मेटाडेटा भी शामिल होता है.
  - कुल: डिफ़ॉल्ट मीडिया रिज़ॉल्यूशन पर, वीडियो के हर सेकंड के लिए करीब 300 टोकन या कम मीडिया रिज़ॉल्यूशन पर, वीडियो के हर सेकंड के लिए 100 टोकन.
- **मीडिया रिज़ॉल्यूशन**: Gemini 3 में, मल्टीमॉडल
  विज़न प्रोसेसिंग पर ज़्यादा कंट्रोल मिलता है.`media_resolution` `media_resolution` पैरामीटर, **हर इनपुट इमेज या वीडियो फ़्रेम के लिए, टोकन की ज़्यादा से ज़्यादा संख्या तय करता है.**
  ज़्यादा रिज़ॉल्यूशन से, मॉडल को बारीक टेक्स्ट पढ़ने या छोटी-छोटी जानकारी की पहचान करने में मदद मिलती है. हालांकि, इससे टोकन का इस्तेमाल और इंतज़ार का समय बढ़ जाता है.

  पैरामीटर के बारे में ज़्यादा जानकारी और इससे टोकन
  की गिनती पर पड़ने वाले असर के बारे में जानने के लिए, [मीडिया रिज़ॉल्यूशन](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=hi) की गाइड देखें.
- **टाइमस्टैंप का फ़ॉर्मैट**: अपने प्रॉम्प्ट में, वीडियो में मौजूद किसी खास समय के बारे में बताने के लिए, `MM:SS` फ़ॉर्मैट का इस्तेमाल करें. जैसे, एक मिनट और 15 सेकंड के लिए `01:15`.
- **सबसे सही तरीके**:

  - सबसे अच्छे नतीजे पाने के लिए, हर प्रॉम्प्ट अनुरोध के लिए सिर्फ़ एक वीडियो का इस्तेमाल करें.
  - अगर टेक्स्ट और एक वीडियो को एक साथ इस्तेमाल किया जा रहा है, तो `contents` कलेक्शन में वीडियो वाले हिस्से के *बाद* टेक्स्ट प्रॉम्प्ट रखें.
  - ध्यान रखें कि हर सेकंड एक फ़्रेम की दर से सैंपल लेने की वजह से, तेज़ी से होने वाली कार्रवाई के क्रम में कुछ जानकारी छूट सकती है. अगर ज़रूरी हो, तो ऐसी क्लिप की स्पीड कम करें.

## आगे क्या करना है

इस गाइड में, वीडियो फ़ाइलें अपलोड करने और वीडियो इनपुट से टेक्स्ट आउटपुट जनरेट करने का तरीका बताया गया है. ज़्यादा जानने के लिए, ये लेख पढ़ें और वीडियो देखें:

- [सिस्टम के निर्देश](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#system-instructions):
  सिस्टम के निर्देशों से, अपनी
  ज़रूरतों और इस्तेमाल के मामलों के हिसाब से मॉडल के व्यवहार को कंट्रोल किया जा सकता है.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi): Gemini के साथ इस्तेमाल करने के लिए, फ़ाइलें अपलोड करने और मैनेज करने के बारे में ज़्यादा जानें.
- [फ़ाइल के साथ प्रॉम्प्ट करने की रणनीतियां](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide): Gemini API, टेक्स्ट, इमेज, ऑडियो, और वीडियो डेटा के साथ प्रॉम्प्ट करने की सुविधा देता है. इसे
  मल्टीमॉडल प्रॉम्प्टिंग भी कहा जाता है.
- [सुरक्षा से जुड़े दिशा-निर्देश](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=hi): कभी-कभी, जनरेटिव
  एआई मॉडल से ऐसे आउटपुट मिलते हैं जिनकी उम्मीद नहीं होती. जैसे, गलत, पक्षपाती या आपत्तिजनक आउटपुट. ऐसे आउटपुट से होने वाले नुकसान के जोखिम को कम करने के लिए, पोस्ट-प्रोसेसिंग और लोगों से आकलन कराना ज़रूरी है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
