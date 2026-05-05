---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi
fetched_at: 2026-05-05T13:26:53.095287+00:00
title: "Ph\u01b0\u01a1ng th\u1ee9c nh\u1eadp t\u1ec7p \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/Tính năng Nghiên cứu chuyên sâu của Gemini) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

- [Trang chủ](https://ai.google.dev/gemini-api/docs/Trang chủ)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/Tài liệu)

Gửi ý kiến phản hồi

# Phương thức nhập tệp

Hướng dẫn này giải thích những cách để bạn có thể đưa các tệp đa phương tiện (chẳng hạn như hình ảnh, âm thanh, video và tài liệu) vào khi đưa ra yêu cầu cho Gemini API.
Các phương thức mới được hỗ trợ trong tất cả các điểm cuối của Gemini API, bao gồm cả Batch, Interactions và Live API.
Việc chọn phương thức phù hợp phụ thuộc vào kích thước tệp, nơi dữ liệu của bạn hiện được lưu trữ và tần suất bạn dự định sử dụng tệp.

Cách đơn giản nhất để đưa một tệp vào làm thông tin đầu vào là đọc một tệp cục bộ rồi đưa tệp đó vào một câu lệnh. Ví dụ sau đây cho biết cách đọc một tệp PDF cục bộ. Tệp PDF có giới hạn là 50 MB đối với phương thức này. Hãy xem [Bảng so sánh phương thức nhập](https://ai.google.dev/gemini-api/docs/Bảng so sánh phương thức nhập) để biết danh sách đầy đủ các loại và giới hạn nhập tệp.

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
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
        model: "gemini-3-flash-preview",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## So sánh phương thức nhập

Bảng sau đây so sánh từng phương thức nhập với giới hạn tệp và các trường hợp sử dụng hiệu quả nhất. Xin lưu ý rằng giới hạn kích thước tệp có thể thay đổi tuỳ thuộc vào loại tệp và mô hình/trình mã hoá từ được dùng để xử lý tệp.

| Phương thức | Phù hợp nhất cho | Kích thước tệp tối đa | Khả năng lưu trữ dài lâu |
| --- | --- | --- | --- |
| **Dữ liệu nội tuyến** | Thử nghiệm nhanh, tệp nhỏ, ứng dụng theo thời gian thực. | 100 MB cho mỗi yêu cầu/tải trọng   (**50 MB đối với tệp PDF**) | Không có (gửi kèm theo mọi yêu cầu) |
| **Tải tệp lên bằng API** | Tệp lớn, tệp được sử dụng nhiều lần. | 2 GB cho mỗi tệp,   tối đa 20 GB cho mỗi dự án | 48 giờ |
| **Đăng ký URI GCS của File API** | Các tệp lớn đã có trong Google Cloud Storage, các tệp được dùng nhiều lần. | 2 GB cho mỗi tệp, không có giới hạn về tổng dung lượng lưu trữ | Không có (tìm nạp theo yêu cầu). Một lần đăng ký có thể cấp quyền truy cập trong tối đa 30 ngày. |
| **URL bên ngoài** | Dữ liệu công khai hoặc dữ liệu trong các vùng lưu trữ đám mây (AWS, Azure, GCS) mà không cần tải lại. | 100 MB cho mỗi yêu cầu/tải trọng | Không có (tìm nạp theo yêu cầu) |

## Dữ liệu trong dòng

Đối với các tệp nhỏ hơn (dưới 100 MB hoặc 50 MB đối với tệp PDF), bạn có thể truyền dữ liệu trực tiếp trong tải trọng yêu cầu. Đây là phương thức đơn giản nhất để kiểm thử nhanh hoặc các ứng dụng xử lý dữ liệu tạm thời theo thời gian thực. Bạn có thể cung cấp dữ liệu dưới dạng chuỗi được mã hoá base64 hoặc bằng cách đọc trực tiếp các tệp cục bộ.

Để xem ví dụ về cách đọc từ một tệp cục bộ, hãy xem ví dụ ở đầu trang này.

### Tìm nạp từ URL

Bạn cũng có thể tìm nạp một tệp từ URL, chuyển đổi tệp đó thành byte và đưa tệp đó vào dữ liệu đầu vào.

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
  model="gemini-3-flash-preview",
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
        model: "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

File API được thiết kế cho các tệp lớn hơn (tối đa 2 GB) hoặc các tệp mà bạn dự định dùng trong nhiều yêu cầu.

### Tải tệp lên theo cách tiêu chuẩn

Tải một tệp cục bộ lên Gemini API. Các tệp được tải lên theo cách này sẽ được lưu trữ tạm thời (48 giờ) và được xử lý để mô hình có thể truy xuất hiệu quả.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

### Đăng ký tệp Google Cloud Storage

Nếu dữ liệu của bạn đã có trong Google Cloud Storage, bạn không cần tải xuống rồi tải lên lại. Bạn có thể đăng ký trực tiếp với File API.

1. Cấp quyền truy cập cho **Service Agent** vào từng bộ chứa

   1. Bật Gemini API trong dự án trên đám mây của bạn.
   2. Tạo tác nhân dịch vụ:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Cấp cho Gemini API Service Agent quyền** đọc các bộ chứa lưu trữ của bạn.

      Người dùng cần chỉ định `Storage Object Viewer`
      [vai trò IAM](https://ai.google.dev/gemini-api/docs/vai trò IAM)
      cho tác nhân dịch vụ này trên các vùng lưu trữ cụ thể mà họ dự định sử dụng.

   Theo mặc định, quyền truy cập này không hết hạn, nhưng bạn có thể thay đổi bất cứ lúc nào. Bạn cũng có thể dùng các lệnh [SDK IAM của Google Cloud Storage](https://ai.google.dev/gemini-api/docs/SDK IAM của Google Cloud Storage) để cấp quyền.
2. Xác thực dịch vụ của bạn

   **Điều kiện tiên quyết**

   - Bật API
   - Tạo một tài khoản dịch vụ/tác nhân có các quyền thích hợp.

   Trước tiên, bạn cần xác thực với tư cách là dịch vụ có quyền xem đối tượng lưu trữ. Cách thức này phụ thuộc vào môi trường mà mã quản lý tệp của bạn sẽ chạy.

   **Bên ngoài Google Cloud**

   Nếu mã của bạn đang chạy bên ngoài Google Cloud, chẳng hạn như trên máy tính, hãy tải thông tin đăng nhập tài khoản xuống từ Google Cloud Console theo các bước sau:

   1. Duyệt đến [bảng điều khiển Tài khoản dịch vụ](https://ai.google.dev/gemini-api/docs/bảng điều khiển Tài khoản dịch vụ)
   2. Chọn tài khoản dịch vụ có liên quan
   3. Chọn thẻ **Khoá** rồi chọn **Thêm khoá, Tạo khoá mới**
   4. Chọn loại khoá **JSON** và ghi lại vị trí tải tệp xuống trên máy của bạn.

   Để biết thêm thông tin chi tiết, hãy xem tài liệu chính thức của Google Cloud về [hoạt động quản lý khoá tài khoản dịch vụ](https://ai.google.dev/gemini-api/docs/hoạt động quản lý khoá tài khoản dịch vụ).

   Sau đó, hãy dùng các lệnh sau để xác thực. Các lệnh này giả định rằng tệp tài khoản dịch vụ của bạn nằm trong thư mục hiện tại, có tên là `service-account.json`.

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

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Trên Google Cloud**

   Nếu đang chạy trực tiếp trong Google Cloud, chẳng hạn như bằng cách sử dụng [các hàm Cloud Run](https://ai.google.dev/gemini-api/docs/các hàm Cloud Run) hoặc một [phiên bản Compute Engine](https://ai.google.dev/gemini-api/docs/phiên bản Compute Engine), bạn sẽ có thông tin đăng nhập ngầm nhưng cần xác thực lại để cấp các phạm vi thích hợp.

   ### Python

   Mã này giả định rằng dịch vụ đang chạy trong một môi trường mà [Thông tin xác thực mặc định của ứng dụng](https://ai.google.dev/gemini-api/docs/Thông tin xác thực mặc định của ứng dụng) có thể được tự động lấy, chẳng hạn như Cloud Run hoặc Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Mã này giả định rằng dịch vụ đang chạy trong một môi trường mà [Thông tin xác thực mặc định của ứng dụng](https://ai.google.dev/gemini-api/docs/Thông tin xác thực mặc định của ứng dụng) có thể được tự động lấy, chẳng hạn như Cloud Run hoặc Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   Đây là một lệnh tương tác. Đối với các dịch vụ như Compute Engine, bạn có thể đính kèm các phạm vi vào dịch vụ đang chạy ở cấp cấu hình. Hãy xem [tài liệu về dịch vụ do người dùng quản lý](https://ai.google.dev/gemini-api/docs/tài liệu về dịch vụ do người dùng quản lý) để biết ví dụ.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Đăng ký tệp (API Tệp)

   Sử dụng Files API để đăng ký tệp và tạo đường dẫn Files API có thể được dùng trực tiếp trong Gemini API.

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
       model="gemini-3-flash-preview",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## HTTP bên ngoài / URL đã ký

Bạn có thể truyền trực tiếp các URL HTTPS truy cập công khai hoặc URL được ký trước (tương thích với [URL được ký trước S3](https://ai.google.dev/gemini-api/docs/URL được ký trước S3) và SAS Azure) trong yêu cầu tạo. Gemini API sẽ tìm nạp nội dung một cách an toàn trong quá trình xử lý. Đây là lựa chọn lý tưởng cho những tệp có dung lượng tối đa 100 MB mà bạn không muốn tải lại lên.

Bạn có thể sử dụng URL công khai hoặc URL đã ký làm dữ liệu đầu vào bằng cách sử dụng các URL trong trường `file_uri`.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
    model: 'gemini-3-flash-preview',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent \
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

### Hỗ trợ tiếp cận

Xác minh rằng các URL bạn cung cấp không dẫn đến những trang yêu cầu đăng nhập hoặc có tường phí. Đối với cơ sở dữ liệu riêng tư, hãy đảm bảo rằng bạn tạo một URL đã ký với quyền truy cập và thời gian hết hạn chính xác.

### Kiểm tra an toàn

Hệ thống sẽ kiểm tra nội dung của URL để xác nhận rằng các URL đó đáp ứng các tiêu chuẩn về sự an toàn và chính sách (ví dụ: nội dung không bị loại trừ và có tường phí). Nếu URL bạn cung cấp không vượt qua bước kiểm tra này, bạn sẽ nhận được `url_retrieval_status` trong số `URL_RETRIEVAL_STATUS_UNSAFE`.

### Các loại nội dung được hỗ trợ

Danh sách các loại tệp được hỗ trợ và hạn chế này chỉ mang tính hướng dẫn ban đầu và chưa đầy đủ. Tập hợp các loại được hỗ trợ có hiệu quả có thể thay đổi và khác nhau tuỳ theo mô hình và phiên bản mã hoá từ cụ thể đang được sử dụng. Các loại không được hỗ trợ sẽ dẫn đến lỗi.
Ngoài ra, tính năng truy xuất nội dung cho các loại tệp này hiện chỉ hỗ trợ những URL có thể truy cập công khai.

#### Loại tệp văn bản

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Các loại tệp ứng dụng

- `application/json`
- `application/pdf`

#### Loại tệp hình ảnh

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Loại tệp video

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Các phương pháp hay nhất

- **Chọn phương thức phù hợp:** Sử dụng dữ liệu nội tuyến cho các tệp nhỏ, tạm thời.
  Sử dụng File API cho các tệp có kích thước lớn hoặc thường dùng. Sử dụng URL bên ngoài cho dữ liệu đã được lưu trữ trực tuyến.
- **Chỉ định loại MIME:** Luôn cung cấp loại MIME chính xác cho dữ liệu tệp để đảm bảo quá trình xử lý diễn ra đúng cách.
- **Xử lý lỗi:** Triển khai quy trình xử lý lỗi trong mã của bạn để quản lý các vấn đề tiềm ẩn như lỗi mạng, vấn đề về quyền truy cập vào tệp hoặc lỗi API.
- **Quản lý quyền GCS:** Khi sử dụng chế độ đăng ký GCS, chỉ cấp cho Gemini API Service Agent vai trò `Storage Object Viewer` cần thiết trên các bộ chứa cụ thể.
- **Bảo mật URL đã ký:** Đảm bảo URL đã ký có thời gian hết hạn thích hợp và quyền hạn hạn chế.

## Các điểm hạn chế

- Giới hạn kích thước tệp thay đổi tuỳ theo phương thức (xem [bảng so sánh](https://ai.google.dev/gemini-api/docs/bảng so sánh)) và loại tệp.
- Dữ liệu cùng dòng làm tăng kích thước tải trọng yêu cầu.
- Tệp tải lên qua File API chỉ là tạm thời và sẽ hết hạn sau 48 giờ.
- Việc tìm nạp URL bên ngoài bị giới hạn ở mức 100 MB cho mỗi tải trọng và hỗ trợ các loại nội dung cụ thể.
- Để đăng ký Google Cloud Storage, bạn cần thiết lập IAM và quản lý mã thông báo OAuth đúng cách.

## Bước tiếp theo

- Hãy thử viết câu lệnh đa phương thức của riêng bạn bằng [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio).
- Để biết thông tin về cách đưa tệp vào câu lệnh, hãy xem hướng dẫn về [Vision](https://ai.google.dev/gemini-api/docs/Vision), [Âm thanh](https://ai.google.dev/gemini-api/docs/Âm thanh) và [Xử lý tài liệu](https://ai.google.dev/gemini-api/docs/Xử lý tài liệu).
- Để biết thêm hướng dẫn về cách thiết kế câu lệnh, chẳng hạn như điều chỉnh các thông số lấy mẫu, hãy xem hướng dẫn [Chiến lược tạo câu lệnh](https://ai.google.dev/gemini-api/docs/Chiến lược tạo câu lệnh).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://ai.google.dev/gemini-api/docs/Giấy phép ghi nhận tác giả 4.0 của Creative Commons) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://ai.google.dev/gemini-api/docs/Giấy phép Apache 2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://ai.google.dev/gemini-api/docs/Chính sách trang web của Google Developers). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?
