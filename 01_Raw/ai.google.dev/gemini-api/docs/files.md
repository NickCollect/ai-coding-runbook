---
source_url: https://ai.google.dev/gemini-api/docs/files?hl=vi
fetched_at: 2026-06-29T05:29:59.007032+00:00
title: "API T\u1ec7p \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# API Tệp

Gemini có thể xử lý nhiều loại dữ liệu đầu vào, bao gồm văn bản, hình ảnh và âm thanh cùng một lúc.

Hướng dẫn này trình bày cách xử lý các tệp nội dung nghe nhìn bằng Files API. Các thao tác cơ bản đều giống nhau đối với tệp âm thanh, hình ảnh, video, tài liệu và các loại tệp được hỗ trợ khác.

Để biết hướng dẫn về câu lệnh cho tệp, hãy xem phần [Hướng dẫn về câu lệnh cho tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide).

## Tải tệp lên

Bạn có thể dùng Files API để tải một tệp đa phương tiện lên. Luôn sử dụng Files API khi tổng kích thước yêu cầu (bao gồm cả tệp, câu lệnh văn bản, hướng dẫn hệ thống, v.v.) lớn hơn 100 MB. Đối với tệp PDF, giới hạn là 50 MB.

Đoạn mã sau đây tải một tệp lên rồi dùng tệp đó trong một lệnh gọi đến `interactions.create`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": myfile.uri, "mime_type": myfile.mime_type}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this audio clip" },
      { type: "audio", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
defer client.Files.Delete(ctx, file.Name)

interaction, err := client.Interactions.Create(ctx, "gemini-3.5-flash", &genai.InteractionRequest{
    Input: []interface{}{
        genai.NewPartFromFile(*file),
        genai.NewPartFromText("Describe this audio clip"),
    },
}, nil)

if err != nil {
    log.Fatal(err)
}

// Print the model's text response
for _, step := range interaction.Steps {
    if step.Type == "model_output" {
        for _, part := range step.Content {
            if part.Type == "text" {
                fmt.Println(part.Text)
            }
        }
    }
}
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

# Now create an interaction using the Interactions API
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Lấy siêu dữ liệu cho một tệp

Bạn có thể xác minh rằng API đã lưu trữ thành công tệp được tải lên và nhận siêu dữ liệu của tệp đó bằng cách gọi `files.get`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await client.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}

gotFile, err := client.Files.Get(ctx, file.Name)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Got file:", gotFile.Name)
```

### REST

```
# file_info.json was created in the upload example
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## Liệt kê các tệp đã tải lên

Đoạn mã sau đây sẽ lấy danh sách tất cả các tệp đã tải lên:

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const listResponse = await client.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Go

```
for file, err := range client.Files.All(ctx) {
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(file.Name)
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Xoá tệp đã tải lên

Các tệp sẽ tự động bị xoá sau 48 giờ. Bạn cũng có thể xoá tệp đã tải lên theo cách thủ công:

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await client.files.delete({ name: fileName });
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
client.Files.Delete(ctx, file.Name)
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Thông tin về việc sử dụng

Bạn có thể dùng Files API để tải lên và tương tác với các tệp đa phương tiện. Files API cho phép bạn lưu trữ tối đa 20 GB tệp cho mỗi dự án, với kích thước tối đa cho mỗi tệp là 2 GB. Các tệp được lưu trữ trong 48 giờ. Trong thời gian đó, bạn có thể dùng API để lấy siêu dữ liệu về các tệp, nhưng không thể tải các tệp xuống.
Files API được cung cấp miễn phí ở mọi khu vực có Gemini API.

## Chiến lược nhắc nhở về tệp

Phần này cung cấp hướng dẫn và các phương pháp hay nhất để sử dụng tệp đa phương tiện với câu lệnh cho Gemini API.

Việc có thể sử dụng nhiều loại dữ liệu trong câu lệnh giúp bạn linh hoạt hơn về những nhiệm vụ mà bạn có thể giải quyết bằng Gemini API. Ví dụ: bạn có thể gửi cho mô hình một bức ảnh về một bữa ăn ngon và yêu cầu mô hình viết một bài đăng ngắn trên blog về bữa ăn đó.

|  |  |
| --- | --- |
| **Câu lệnh** | **Đáp** |
| Viết một bài đăng ngắn gọn và hấp dẫn trên blog dựa trên bức ảnh này. Nội dung đó phải có phần mô tả về bữa ăn trong ảnh và nói về hành trình chuẩn bị bữa ăn của tôi.   Bánh quy | Chuẩn bị sẵn bữa ăn là một cách hiệu quả để tiết kiệm thời gian và tiền bạc, đồng thời giúp bạn ăn uống lành mạnh hơn. Bữa ăn này là một ví dụ điển hình về bữa ăn lành mạnh và ngon miệng mà bạn có thể chuẩn bị trước.  Bữa ăn này có cơm gạo lứt, rau củ nướng và gà sốt teriyaki. Gạo lứt là một loại carbohydrate phức tạp và lành mạnh, giúp bạn có năng lượng bền bỉ. Rau củ nướng là một cách tuyệt vời để bổ sung vitamin và khoáng chất hằng ngày, còn món gà teriyaki là một lựa chọn ngon miệng và giàu protein.  Món ăn này cũng rất dễ chế biến. Bạn chỉ cần nấu gạo lứt, nướng rau và nấu món gà sốt teriyaki. Sau khi nấu xong, hãy chia thức ăn vào các hộp đựng và bảo quản trong tủ lạnh. Sau đó, bạn có thể lấy hộp đựng và đi làm vào những buổi sáng bận rộn!  Nếu bạn đang tìm một bữa ăn lành mạnh và ngon miệng có thể chuẩn bị trước, thì đây là một lựa chọn tuyệt vời. Món ăn này giàu dinh dưỡng và hương vị, chắc chắn sẽ giúp bạn cảm thấy no và hài lòng.  Chúc bạn chuẩn bị được những bữa ăn lành mạnh và ngon miệng! |

Nếu gặp khó khăn khi nhận được kết quả mong muốn từ những câu lệnh sử dụng tệp đa phương tiện, bạn có thể áp dụng một số chiến lược để đạt được kết quả mong muốn. Các phần sau đây cung cấp các phương pháp thiết kế và mẹo khắc phục sự cố để cải thiện câu lệnh sử dụng dữ liệu đầu vào đa phương thức.

Bạn có thể cải thiện câu lệnh đa phương thức bằng cách làm theo các phương pháp hay nhất sau:

- ### [Kiến thức cơ bản về thiết kế câu lệnh](#specific-instructions)

  - **Đưa ra chỉ dẫn cụ thể**: Soạn thảo chỉ dẫn rõ ràng và ngắn gọn để giảm thiểu khả năng hiểu sai.
  - **Thêm một vài ví dụ vào câu lệnh:** Sử dụng một vài ví dụ thực tế để minh hoạ những gì bạn muốn đạt được.
  - **Chia nhỏ thành từng bước**: Chia các việc phức tạp thành những mục tiêu phụ dễ quản lý, hướng dẫn mô hình thực hiện quy trình.
  - **Chỉ định định dạng đầu ra**: Trong câu lệnh, hãy yêu cầu đầu ra ở định dạng bạn muốn, chẳng hạn như Markdown, JSON, HTML, v.v.
  - **Đặt hình ảnh lên trước đối với câu lệnh có một hình ảnh**: Mặc dù Gemini có thể xử lý dữ liệu đầu vào là hình ảnh và văn bản theo bất kỳ thứ tự nào, nhưng đối với câu lệnh có một hình ảnh, Gemini có thể hoạt động hiệu quả hơn nếu hình ảnh (hoặc video) đó được đặt trước câu lệnh văn bản. Tuy nhiên, đối với những câu lệnh yêu cầu hình ảnh phải được xen kẽ với văn bản để có ý nghĩa, hãy sử dụng bất kỳ thứ tự nào tự nhiên nhất.
- ### [Khắc phục sự cố về câu lệnh đa phương thức](#troubleshooting)

  - **Nếu mô hình không lấy thông tin từ phần liên quan của hình ảnh:** Đưa ra gợi ý về những khía cạnh của hình ảnh mà bạn muốn câu lệnh lấy thông tin.
  - **Nếu đầu ra của mô hình quá chung chung (không đủ phù hợp với đầu vào là hình ảnh/video):** Khi bắt đầu câu lệnh, hãy thử yêu cầu mô hình mô tả(các) hình ảnh hoặc video trước khi đưa ra hướng dẫn về nhiệm vụ, hoặc thử yêu cầu mô hình tham khảo nội dung trong hình ảnh.
  - **Cách khắc phục sự cố về phần bị lỗi:** Yêu cầu mô hình mô tả hình ảnh hoặc giải thích lý do để đánh giá mức độ hiểu biết ban đầu của mô hình.
  - **Nếu câu lệnh của bạn tạo ra nội dung ảo:** Hãy thử giảm chế độ cài đặt nhiệt độ hoặc yêu cầu mô hình cung cấp nội dung mô tả ngắn hơn để mô hình ít có khả năng suy đoán thêm chi tiết.
  - **Điều chỉnh các tham số lấy mẫu:** Thử nghiệm với các chế độ cài đặt nhiệt độ và lựa chọn top-k khác nhau để điều chỉnh khả năng sáng tạo của mô hình.

### Đưa ra hướng dẫn cụ thể

Câu lệnh sẽ hiệu quả nhất khi rõ ràng và chi tiết. Nếu bạn có một kết quả cụ thể trong đầu, thì tốt hơn là bạn nên đưa yêu cầu đó vào câu lệnh để đảm bảo bạn nhận được kết quả mình muốn.

Đối với hình ảnh này về một bảng thông tin tại sân bay, nếu bạn chỉ yêu cầu mô hình "mô tả hình ảnh này", thì mô hình có thể tạo ra một nội dung mô tả chung chung. Nếu cần mô hình phân tích cú pháp thời gian và thành phố từ hình ảnh, bạn có thể đưa yêu cầu đó trực tiếp vào câu lệnh.

| Câu lệnh | Câu trả lời của mô hình |
| --- | --- |
| Mô tả hình ảnh này. | Hình ảnh cho thấy bảng thông tin chuyến bay hạ cánh và khởi hành tại sân bay. |

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| Lịch trình du lịch Phân tích thời gian và thành phố từ bảng thông tin tại sân bay xuất hiện trong hình ảnh này thành một danh sách. | - 10:50 Moscow - 11:05 Edinburgh - 11:05 London - 11:10 Bucharest - 11:30 Kiev - 11:35 Dublin - 11:45 Đông Midlands - 12:15 Sofia - 12:30 London - 12:30 Newcastle - 12:40 St Petersburg - 12:40 London - 12:45 Manchester |

### Thêm một vài ví dụ

Mô hình Gemini có thể chấp nhận nhiều dữ liệu đầu vào mà mô hình có thể dùng làm ví dụ để hiểu được kết quả bạn muốn. Việc thêm những ví dụ này có thể giúp mô hình xác định các mẫu và áp dụng mối quan hệ giữa hình ảnh và câu trả lời đã cho vào ví dụ mới. Đây cũng được gọi là học "từ một vài dữ liệu".

Trong ví dụ sau, kết quả ban đầu được viết dưới dạng câu và cũng chứa quốc gia (Brazil). Giả sử bạn muốn đầu ra ở một định dạng hoặc kiểu khác và bạn chỉ muốn thành phố chứ không phải quốc gia. Việc thêm một vài ví dụ vào câu lệnh có thể hướng dẫn mô hình trả lời theo cách bạn muốn.

| **Câu lệnh** | **Phản hồi của mô hình** |
| --- | --- |
| Lịch trình du lịch Xác định thành phố cùng với địa danh. | Địa danh này là tượng Chúa Kitô Cứu thế ở Rio de Janeiro, Brazil. |

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| Xác định thành phố cùng với địa danh. đấu trường La Mã | thành phố: Rome, địa danh: Đấu trường La Mã. |
| Tử Cấm Thành | thành phố: Bắc Kinh, địa danh: Tử Cấm Thành |
| tử cấm thành | thành phố: Rio de Janeiro, địa danh: Tượng Chúa Kitô Cứu thế |

### Phân tích từng bước

Đối với những tác vụ phức tạp như những tác vụ đòi hỏi cả khả năng hiểu biết bằng hình ảnh và khả năng suy luận, bạn nên chia tác vụ thành các bước nhỏ hơn và đơn giản hơn. Ngoài ra, bạn cũng có thể yêu cầu trực tiếp mô hình "suy nghĩ từng bước" trong câu lệnh của mình để đạt được hiệu quả.

| Câu lệnh | Câu trả lời của mô hình |
| --- | --- |
| Khi nào tôi sẽ hết giấy vệ sinh? | Bạn chỉ còn 3 lượt quay. |

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| 1. Trước tiên, hãy đếm xem có bao nhiêu cuộn giấy vệ sinh trong bức ảnh này. 2. Sau đó, hãy xác định lượng giấy vệ sinh mà một người thường dùng mỗi ngày. 3. Tính toán thời gian sử dụng hết số giấy vệ sinh này. | 1. Có 3 cuộn giấy vệ sinh trong bức ảnh này. 2. Một người thường dùng khoảng 20 tờ giấy vệ sinh mỗi ngày. 3. Nếu mỗi cuộn có 200 tờ, thì mỗi cuộn sẽ dùng được khoảng 10 ngày. Do đó, 3 cuộn giấy sẽ dùng được khoảng một tháng. |

Các bài toán hoặc những loại bài toán có lời văn khác là những lựa chọn phù hợp để yêu cầu mô hình suy nghĩ từng bước.

| **Câu lệnh** | **Đáp** |
| --- | --- |
| Số hạng thứ 4 trong dãy số này là bao nhiêu? | -135 |

Câu trả lời của mô hình không chính xác. Một số cách để cải thiện vấn đề này là yêu cầu mô hình phân tích vấn đề trước khi trả lời câu lệnh.

| **Câu lệnh** | **Đáp** |
| --- | --- |
| Trước tiên, hãy phân tích cú pháp công thức trong hình ảnh.  Sau đó, dựa vào công thức, hãy trả lời câu hỏi "số hạng thứ 4 trong dãy số là gì?". | *Nhấp để mở rộng kết quả* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Thay n = 4 vào công thức: $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. Chúng ta không biết giá trị của b(3), vì vậy hãy thay n = 3 vào công thức: $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. Chúng ta không biết giá trị của b(2), nên hãy thay n = 2 vào công thức: $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. Chúng ta biết giá trị của b(1) là 15, vì vậy hãy thay thế giá trị này vào công thức: $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. Giờ đây, khi đã biết giá trị của b(2), hãy thay thế giá trị đó vào công thức cho b(3): $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Giờ đây, khi đã biết giá trị của b(3), hãy thay thế giá trị đó vào công thức cho b(4): $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Do đó, số hạng thứ 4 trong dãy số là -405. |

Câu trả lời này của mô hình là chính xác. Để câu trả lời trở nên tinh gọn hơn nữa, bạn có thể yêu cầu mô hình suy nghĩ từng bước.

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| Số hạng thứ 4 trong dãy số này là bao nhiêu? Hãy suy nghĩ từng bước. | Số hạng đầu tiên là 15.  Số hạng thứ hai là b(1) \* (-3) = 15 \* (-3) = -45.  Số hạng thứ ba là b(2) \* (-3) = -45 \* (-3) = 135.  Số hạng thứ tư là b(3) \* (-3) = 135 \* (-3) = -405. |

### Chỉ định định dạng đầu ra

Một vấn đề thường gặp là nhu cầu về đầu ra của mô hình phải ở một định dạng nhất định (ví dụ: Markdown, JSON, HTML), đặc biệt nếu đầu ra của mô hình cần được một tác vụ hạ nguồn tiếp nhận. Bạn có thể thử tạo kết quả ở định dạng đó bằng cách hướng dẫn mô hình làm như vậy trong câu lệnh. Sau đây là hai ví dụ:

| Câu lệnh | Câu trả lời của mô hình |
| --- | --- |
| Phân tích bảng trong hình ảnh này thành định dạng Markdown | ```none | Môn học | Trạng thái | Thời gian | Ngày bắt đầu | Đến hạn | | ------- | ------ | ---- | ---------- | ------ | | Toán | Đã hoàn thành | 1,5 giờ | 29/11/2023 | 1/12/2023 | | Địa lý | Đã hoàn thành | 30 phút | 2/12/2023 | 4/12/2023 | | Vật lý | Đang thực hiện | 2 giờ | 3/12/2023 | 5/12/2023 | | Sinh học | Chưa bắt đầu | 6 giờ | 2/11/2016 | 6/12/2023 | ``` |

| **Câu lệnh** | **Phản hồi của mô hình** |
| --- | --- |
| Cung cấp danh sách tất cả các thuộc tính sau:  thành phần, loại món ăn, có phải là món chay hay không, ở định dạng JSON | ```json { "ingredients": [ "rice", "shrimp", "clams", "mussels", "peas", "tomatoes", "onions", "garlic", "olive oil", "paprika", "salt", "pepper" ], "type of cuisine": "Spanish", "vegetarian": false } ``` |

### Đặt hình ảnh lên trước cho câu lệnh một hình ảnh

Mặc dù Gemini có thể diễn giải hình ảnh và văn bản theo bất kỳ thứ tự nào trong câu lệnh, nhưng việc đặt một hình ảnh trước câu lệnh văn bản có thể mang lại kết quả tốt hơn.
Trong các mẫu sau, bạn sẽ nhận thấy hình ảnh xuất hiện trước văn bản trong mỗi câu lệnh.

### Khắc phục sự cố với câu lệnh đa phương thức

Bạn có thể cần khắc phục sự cố về câu lệnh nếu không nhận được phản hồi hữu ích. Bạn có thể thử một số chiến lược sau.

#### Nếu mô hình không lấy thông tin từ phần liên quan của hình ảnh

Để nhận được câu trả lời cụ thể hơn, bạn có thể chỉ ra những khía cạnh của hình ảnh mà bạn muốn câu lệnh lấy thông tin để đưa ra câu trả lời.

| Câu lệnh | Câu trả lời của mô hình |
| --- | --- |
| Những chiếc tã này sẽ dùng được bao nhiêu ngày cho một em bé? | Số tã này sẽ dùng được trong 198 ngày. |

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| Tôi có thể dùng hết số tã này trong bao lâu?  Dùng trọng lượng ghi trên hộp để xác định độ tuổi của trẻ và dùng tổng số tã trong hộp.  Chia tổng số tã cho số lượng tã mà trẻ dùng mỗi ngày. | Hộp này có 198 chiếc tã. Trên hộp ghi rằng tã dành cho trẻ nặng từ 10 đến 17 kg.  Trẻ em trung bình trong khoảng cân nặng này có thể từ 1 đến 2 tuổi.  Một đứa trẻ 2 tuổi thường dùng 6 chiếc tã mỗi ngày, do đó, số tã này sẽ dùng được khoảng 33 ngày (198/6). |

#### Nếu đầu ra của mô hình quá chung chung và không đủ phù hợp với dữ liệu đầu vào là hình ảnh

Để giúp mô hình điều chỉnh câu trả lời cho(các) hình ảnh, hãy thử yêu cầu mô hình mô tả hình ảnh trước khi thực hiện nhiệm vụ suy luận.

| Câu lệnh | Câu trả lời của mô hình |
| --- | --- |
| Điểm chung giữa những hình ảnh này là gì? | Cả 4 hình ảnh đều là ví dụ về ảnh phong cảnh. |

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| Trước tiên, hãy mô tả chi tiết nội dung trong từng hình ảnh. Điểm chung giữa những hình ảnh này là gì? | Hình ảnh đầu tiên cho thấy một người đang đóng gói hành lý vào vali. Hình ảnh thứ hai cho thấy một hành lang trống trong trung tâm mua sắm. Hình ảnh thứ ba cho thấy một cuộn giấy vệ sinh. Hình ảnh thứ tư cho thấy một vùng biển tối tăm và bão tố.  Điểm chung giữa những hình ảnh này là chúng đều là ví dụ về không gian trung gian. Không gian liminal là những nơi hoặc tình huống nằm giữa hai nơi hoặc tình huống khác. Chúng thường có đặc điểm là cảm giác không chắc chắn hoặc mơ hồ.  Hình ảnh đầu tiên cho thấy người ở giữa đang ở nhà và đang đi du lịch. Hình ảnh thứ hai cho thấy hành lang giữa hai cửa hàng. Hình ảnh thứ ba là giấy vệ sinh, có thể tượng trưng cho phòng tắm. Phòng tắm là không gian chuyển tiếp giữa khu vực riêng tư và khu vực công cộng. Đó là nơi chúng ta chuẩn bị bước vào hoặc rời khỏi thế giới bên ngoài.  Hình ảnh thứ tư cho thấy biển ở trạng thái giữa bình lặng và bão tố.  Không gian liminal có thể vừa thú vị vừa bất an. Chúng có thể là nơi bắt đầu hoặc kết thúc. Đó có thể là nơi để suy ngẫm hoặc nơi để hành động. |

Bạn cũng có thể thử yêu cầu mô hình tham khảo nội dung trong hình ảnh một cách rõ ràng.

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| Điểm chung giữa những hình ảnh này là gì? Tham khảo nội dung trong hình ảnh trong câu trả lời của bạn. | Tất cả hình ảnh đều liên quan đến du lịch. Hình ảnh đầu tiên cho thấy một người đang đóng gói hành lý vào vali, hình ảnh thứ hai cho thấy một hành lang trống trong trung tâm mua sắm, hình ảnh thứ ba cho thấy một chồng giấy vệ sinh và hình ảnh thứ tư cho thấy một vùng biển tối tăm và giông bão.  Tất cả những hình ảnh này đều liên quan đến du lịch vì chúng đều là những thứ mà mọi người cần hoặc sử dụng khi đi du lịch. Hình ảnh đầu tiên cho thấy một người đang đóng gói hành lý vào vali. Đây là việc mà mọi người thường làm khi đi du lịch. Hình ảnh thứ hai cho thấy một hành lang trống trong trung tâm mua sắm, đây là nơi mọi người thường đến để mua đồ cho chuyến đi của mình. Hình ảnh thứ ba cho thấy một chồng giấy vệ sinh. Đây là thứ mà mọi người thường dùng khi đi du lịch. Hình ảnh thứ tư cho thấy một vùng biển tối tăm và bão tố. Đây là điều mà mọi người thường gặp phải khi đi du lịch. |

Các mẹo tương tự cũng áp dụng cho kết quả sáng tạo từ hình ảnh. Trong ví dụ sau đây về chú thỏ, việc yêu cầu rõ ràng mô hình đưa các khía cạnh trong hình ảnh vào có thể cải thiện kết quả.

| Câu lệnh | Câu trả lời của mô hình |
| --- | --- |
| Bạn có thể viết cho tôi một bài thơ về hình ảnh này không? | Chú thỏ nhỏ, mềm mại và có màu nâu,  Nhảy qua cánh đồng, lên và xuống.  Tai dài, đuôi nhỏ,  Bạn là sinh vật đáng yêu nhất trong tất cả.  Bạn gặm cỏ, cỏ xanh và ngọt,  Và nhảy đi khi thấy tôi.  Nhưng tôi sẽ luôn là bạn của bạn,  Chú thỏ nhỏ, cho đến tận cùng. |

| **Câu lệnh mới** | **Cải thiện phản hồi** |
| --- | --- |
| Bạn có thể viết cho tôi một bài thơ giàu hình ảnh và kịch tính về thông tin về hình ảnh này, đồng thời cho biết vị trí không? | Chú thỏ nhỏ trên bãi cỏ xanh,  Đôi tai dài và thính.  Bạn thấy gì ở nơi đó,  Ở nơi xa xăm mà bạn đang nhìn chằm chằm?  Có phải là màu xanh dương của đại dương,  Lấp lánh dưới ánh mặt trời?  Hay tiếng sóng vỗ và gầm gừ,  Một nhịp điệu mà bạn yêu thích?  Thỏ con ơi, hãy nói thật cho ta hay,  Điều gì khiến con chú ý đến vậy?  Là làn gió mặn,  Hay tiếng hải âu kêu vang?  Có lẽ là do sự rộng lớn của tất cả,  Một thế giới vừa rộng lớn vừa nhỏ bé.  Một nơi mà những giấc mơ có thể bay bổng,  Và những cuộc phiêu lưu có thể nảy mầm.  Thỏ con ơi, ta tự hỏi giấc mơ của con là gì,  Khi con ngồi trên cỏ, thật thanh bình.  Bạn có khao khát khám phá biển sâu,  Hay ở trên đất liền, nơi bạn có thể nhảy?  Dù là gì đi chăng nữa, thỏ con ơi,  Hãy giữ cho ngọn lửa tò mò luôn cháy sáng.  Trong những ước mơ và khát vọng của bạn,  Có một thế giới đang chờ bạn sáng tạo. |

#### Khắc phục sự cố về phần nào của câu lệnh không hoạt động

Bạn khó có thể biết liệu một câu lệnh có thất bại là do mô hình không **hiểu được hình ảnh** ngay từ đầu hay là do mô hình hiểu được hình ảnh nhưng không thực hiện đúng **các bước suy luận** sau đó.
Để phân biệt những lý do đó, hãy yêu cầu mô hình mô tả nội dung trong hình ảnh.

Trong ví dụ sau, nếu mô hình phản hồi bằng một món ăn nhẹ có vẻ bất ngờ khi kết hợp với trà (ví dụ: bỏng ngô), trước tiên, bạn có thể khắc phục sự cố để xác định xem mô hình có nhận dạng chính xác rằng hình ảnh có chứa trà hay không.

| Câu lệnh | Lời nhắc để khắc phục sự cố |
| --- | --- |
| Tôi có thể làm món ăn nhẹ nào trong 1 phút để ăn kèm với món này? | Mô tả nội dung trong hình ảnh này. |

Một chiến lược khác là yêu cầu mô hình giải thích lý do. Điều này có thể giúp bạn thu hẹp phạm vi để xác định phần nào của quá trình suy luận bị lỗi (nếu có).

| Câu lệnh | Lời nhắc để khắc phục sự cố |
| --- | --- |
| Tôi có thể làm món ăn nhẹ nào trong 1 phút để ăn kèm với món này? | Tôi có thể làm món ăn nhẹ nào trong 1 phút để ăn kèm với món này? Vui lòng giải thích lý do. |

## Bước tiếp theo

- Hãy thử viết câu lệnh đa phương thức của riêng bạn bằng [Google AI Studio](http://aistudio.google.com?hl=vi).
- Để biết thông tin về cách sử dụng Gemini Files API để tải tệp đa phương tiện lên và đưa tệp đó vào câu lệnh, hãy xem hướng dẫn về [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=vi), [Xử lý âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi) và [Xử lý tài liệu](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi).
- Để biết thêm hướng dẫn về cách thiết kế câu lệnh, chẳng hạn như điều chỉnh các thông số lấy mẫu, hãy xem trang [Chiến lược tạo câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
