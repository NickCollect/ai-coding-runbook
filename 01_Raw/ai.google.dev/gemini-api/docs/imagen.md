---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=vi
fetched_at: 2026-07-27T04:48:15.408081+00:00
title: "T\u1ea1o h\u00ecnh \u1ea3nh b\u1eb1ng Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo hình ảnh bằng Imagen

Imagen là mô hình tạo ảnh có độ trung thực cao của Google, có khả năng tạo ra hình ảnh chân thực và chất lượng cao từ câu lệnh văn bản. Tất cả hình ảnh được tạo đều có hình mờ SynthID. Để tìm hiểu thêm về các biến thể của mô hình Imagen hiện có, hãy xem phần [Các phiên bản mô hình](#model-versions).

## Di chuyển sang Nano Banana

Các mô hình Imagen sẽ ngừng hoạt động từ ngày 17 tháng 8 năm 2026. Bạn nên chuyển sang dùng Nano Banana để đáp ứng nhu cầu tạo hình ảnh.

Quá trình di chuyển bao gồm những thay đổi sau:

- **Tên mô hình**: Sử dụng `gemini-2.5-flash-image` thay vì tên mô hình Imagen.
- **Phương thức**: Sử dụng `client.models.generate_content` thay vì `client.models.generate_images`.
- **Xử lý phản hồi**: Nano Banana trả về các phần nội dung (có thể bao gồm dữ liệu hình ảnh) thay vì một đối tượng phản hồi hình ảnh cụ thể.

Hãy xem [Hướng dẫn tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) để biết thêm thông tin chi tiết và ví dụ.

## Tạo hình ảnh bằng các mô hình Imagen

Ví dụ này minh hoạ cách tạo hình ảnh bằng [mô hình Imagen](https://deepmind.google/technologies/imagen/?hl=vi):

### Python

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 4,
    )
)
for generated_image in response.generated_images:
  generated_image.image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const response = await ai.models.generateImages({
    model: 'imagen-4.0-generate-001',
    prompt: 'Robot holding a red skateboard',
    config: {
      numberOfImages: 4,
    },
  });

  let idx = 1;
  for (const generatedImage of response.generatedImages) {
    let imgBytes = generatedImage.image.imageBytes;
    const buffer = Buffer.from(imgBytes, "base64");
    fs.writeFileSync(`imagen-${idx}.png`, buffer);
    idx++;
  }
}

main();
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

  config := &genai.GenerateImagesConfig{
      NumberOfImages: 4,
  }

  response, _ := client.Models.GenerateImages(
      ctx,
      "imagen-4.0-generate-001",
      "Robot holding a red skateboard",
      config,
  )

  for n, image := range response.GeneratedImages {
      fname := fmt.Sprintf("imagen-%d.png", n)
          _ = os.WriteFile(fname, image.Image.ImageBytes, 0644)
  }
}
```

### REST

```
curl -X POST \
    "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "instances": [
          {
            "prompt": "Robot holding a red skateboard"
          }
        ],
        "parameters": {
          "sampleCount": 4
        }
      }'
```

![Hình ảnh do AI tạo về một rô-bốt đang cầm ván trượt màu đỏ](https://ai.google.dev/static/gemini-api/docs/images/robot-skateboard.png?hl=vi)

Hình ảnh do AI tạo về một robot đang cầm ván trượt màu đỏ

### Cấu hình Imagen

Hiện tại, Imagen chỉ hỗ trợ câu lệnh bằng tiếng Anh và các thông số sau:

- `numberOfImages`: Số lượng hình ảnh cần tạo, từ 1 đến 4 (bao gồm cả 1 và 4).
  Giá trị mặc định là 4.
- `imageSize`: Kích thước của hình ảnh được tạo. Tính năng này chỉ được hỗ trợ cho các mô hình Chuẩn và Siêu. Giá trị được hỗ trợ là `1K` và `2K`.
  Giá trị mặc định là `1K`.
- `aspectRatio`: Thay đổi tỷ lệ khung hình của hình ảnh được tạo. Các giá trị được hỗ trợ là `"1:1"`, `"3:4"`, `"4:3"`, `"9:16"` và `"16:9"`. Giá trị mặc định là `"1:1"`.
- `personGeneration`: Cho phép mô hình tạo hình ảnh về con người. Sau đây là các giá trị được hỗ trợ:

  - `"dont_allow"`: Chặn việc tạo hình ảnh có người.
  - `"allow_adult"`: Tạo hình ảnh về người lớn, nhưng không tạo hình ảnh về trẻ em. Đây là tuỳ chọn mặc định
  - `"allow_all"`: Tạo hình ảnh có cả người lớn và trẻ em.

## Hướng dẫn về câu lệnh cho Imagen

Phần này trong hướng dẫn về Imagen cho bạn biết cách sửa đổi câu lệnh chuyển văn bản thành hình ảnh có thể tạo ra nhiều kết quả, cùng với ví dụ về những hình ảnh bạn có thể tạo.

### Kiến thức cơ bản về cách viết câu lệnh

Câu lệnh hiệu quả là câu lệnh có tính mô tả và rõ ràng, đồng thời sử dụng các từ khoá và đối tượng sửa đổi có ý nghĩa. Bắt đầu bằng cách nghĩ đến **chủ thể**, **bối cảnh** và **phong cách**.

![Câu lệnh có chủ đề, bối cảnh và phong cách được nhấn mạnh](https://ai.google.dev/static/gemini-api/docs/images/imagen/style-subject-context.png?hl=vi)

Văn bản trong hình ảnh: Một *bản phác thảo* (**phong cách**) về một *toà nhà chung cư hiện đại* (**đối tượng**) được bao quanh bởi *các toà nhà chọc trời* (**bối cảnh và nền**).

1. **Chủ thể**: Điều đầu tiên bạn cần nghĩ đến khi đưa ra câu lệnh là *chủ thể*: đối tượng, người, động vật hoặc cảnh vật mà bạn muốn tạo hình ảnh.
2. **Bối cảnh và nền:** *Nền hoặc bối cảnh* mà chủ thể sẽ được đặt vào cũng quan trọng không kém. Hãy thử đặt chủ thể của bạn vào nhiều phông nền. Ví dụ: một phòng chụp hình có phông nền trắng, ngoài trời hoặc môi trường trong nhà.
3. **Phong cách:** Cuối cùng, hãy thêm phong cách hình ảnh mà bạn muốn. *Phong cách* có thể là phong cách chung (tranh vẽ, ảnh chụp, bản phác thảo) hoặc phong cách rất cụ thể (tranh vẽ bằng phấn màu, bản vẽ bằng than, hình ảnh 3D đẳng cự). Bạn cũng có thể kết hợp các kiểu.

Sau khi viết phiên bản đầu tiên của câu lệnh, hãy tinh chỉnh câu lệnh bằng cách thêm nhiều chi tiết hơn cho đến khi bạn nhận được hình ảnh mà mình muốn. Việc lặp lại là rất quan trọng.
Bắt đầu bằng cách xác định ý tưởng cốt lõi, sau đó tinh chỉnh và mở rộng ý tưởng cốt lõi đó cho đến khi hình ảnh được tạo gần với tầm nhìn của bạn.

|  |  |  |
| --- | --- | --- |
| photorealistic sample image 1   Câu lệnh: Một công viên vào mùa xuân bên cạnh một hồ nước | photorealistic sample image 2   Câu lệnh: Một công viên vào mùa xuân bên cạnh một hồ nước, **mặt trời lặn bên kia hồ, giờ vàng** | hình ảnh mẫu giống thật 3   Câu lệnh: Một công viên vào mùa xuân bên cạnh một hồ nước, ***mặt trời lặn trên hồ, giờ vàng, hoa dại màu đỏ*** |

Các mô hình Imagen có thể biến ý tưởng của bạn thành hình ảnh chi tiết, cho dù câu lệnh của bạn ngắn hay dài và chi tiết. Tinh chỉnh ý tưởng của bạn thông qua việc đưa ra câu lệnh lặp đi lặp lại, thêm chi tiết cho đến khi bạn đạt được kết quả hoàn hảo.

|  |  |
| --- | --- |
| Câu lệnh ngắn giúp bạn tạo hình ảnh một cách nhanh chóng.  Ví dụ về câu lệnh ngắn cho Imagen 4   Câu lệnh: ảnh cận cảnh một phụ nữ ở độ tuổi 20, ảnh đường phố, ảnh tĩnh trong phim, tông màu cam ấm dịu | Câu lệnh dài hơn cho phép bạn thêm thông tin chi tiết cụ thể và tạo hình ảnh.  Ví dụ về câu lệnh dài cho Imagen 4   Câu lệnh: bức ảnh quyến rũ về một phụ nữ ở độ tuổi 20 sử dụng phong cách chụp ảnh đường phố. Hình ảnh phải trông như một cảnh phim tĩnh với tông màu cam nhạt ấm áp. |

Lời khuyên bổ sung về cách viết câu lệnh cho Imagen:

- **Sử dụng ngôn từ mô tả**: Sử dụng các tính từ và trạng từ chi tiết để mô tả rõ ràng cho Imagen.
- **Cung cấp bối cảnh**: Nếu cần, hãy cung cấp thông tin cơ bản để hỗ trợ AI hiểu rõ hơn.
- **Tham khảo các nghệ sĩ hoặc phong cách cụ thể**: Nếu bạn có một phong cách thẩm mỹ cụ thể, thì việc tham khảo các nghệ sĩ hoặc trào lưu nghệ thuật cụ thể có thể hữu ích.
- **Sử dụng các công cụ thiết kế câu lệnh**: Cân nhắc việc khám phá các công cụ hoặc tài nguyên thiết kế câu lệnh để giúp bạn tinh chỉnh câu lệnh và đạt được kết quả tối ưu.
- **Cải thiện các chi tiết trên khuôn mặt trong ảnh cá nhân và ảnh nhóm**: Chỉ định các chi tiết trên khuôn mặt làm tiêu điểm của bức ảnh (ví dụ: sử dụng từ "chân dung" trong câu lệnh).

### Tạo văn bản trong hình ảnh

Các mô hình Imagen có thể thêm văn bản vào hình ảnh, mở ra nhiều khả năng sáng tạo hơn trong việc tạo hình ảnh. Hãy tham khảo hướng dẫn sau để khai thác tối đa tính năng này:

- **Lặp lại một cách tự tin**: Bạn có thể phải tạo lại hình ảnh cho đến khi đạt được kết quả mong muốn. Tính năng tích hợp văn bản của Imagen vẫn đang phát triển và đôi khi bạn cần thử nhiều lần để có kết quả tốt nhất.
- **Ngắn gọn**: Giới hạn văn bản ở mức 25 ký tự trở xuống để tạo hình ảnh tối ưu.
- **Nhiều cụm từ**: Thử nghiệm với hai hoặc ba cụm từ riêng biệt để cung cấp thêm thông tin. Tránh dùng quá 3 cụm từ để có bố cục rõ ràng hơn.

  ![Ví dụ về văn bản do Imagen 4 tạo](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_generate-text.png?hl=vi)

  Câu lệnh: Một áp phích có văn bản "Summerland" (Vùng đất mùa hè) bằng phông chữ in đậm làm tiêu đề, bên dưới văn bản này là khẩu hiệu "Mùa hè chưa bao giờ tuyệt vời đến thế"
- **Vị trí theo hướng dẫn**: Mặc dù Imagen có thể cố gắng đặt văn bản theo chỉ dẫn, nhưng đôi khi sẽ có sự khác biệt. Tính năng này liên tục được cải thiện.
- **Kiểu phông chữ truyền cảm hứng**: Chỉ định một kiểu phông chữ chung để ảnh hưởng một cách tinh tế đến các lựa chọn của Imagen. Đừng dựa vào việc sao chép phông chữ một cách chính xác, mà hãy mong đợi những cách diễn giải sáng tạo.
- **Cỡ chữ**: Chỉ định cỡ chữ hoặc chỉ số chung về kích thước (ví dụ: *nhỏ*, *vừa*, *lớn*) để ảnh hưởng đến quá trình tạo cỡ chữ.

### Tham số hoá câu lệnh

Để kiểm soát kết quả đầu ra tốt hơn, bạn có thể thấy việc tham số hoá dữ liệu đầu vào thành Imagen là hữu ích. Ví dụ: giả sử bạn muốn khách hàng có thể tạo biểu trưng cho doanh nghiệp của họ và bạn muốn đảm bảo rằng biểu trưng luôn được tạo trên nền có màu đơn sắc. Bạn cũng muốn giới hạn các lựa chọn mà khách hàng có thể chọn trong trình đơn.

Trong ví dụ này, bạn có thể tạo một câu lệnh có tham số tương tự như sau:

```
A {logo_style} logo for a {company_area} company on a solid color background. Include the text {company_name}.
```

Trong giao diện người dùng tuỳ chỉnh, khách hàng có thể nhập các tham số bằng một trình đơn và giá trị mà họ chọn sẽ điền vào câu lệnh mà Imagen nhận được.

Ví dụ:

1. Câu lệnh: `A minimalist logo for a health care company on a solid color background. Include the text Journey.`

   ![Ví dụ 1 về tham số hoá câu lệnh của Imagen 4](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_healthcare.png?hl=vi)
2. Câu lệnh: `A modern logo for a software company on a solid color background. Include the text Silo.`

   ![Ví dụ 2 về việc tham số hoá câu lệnh cho Imagen 4](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_software.png?hl=vi)
3. Câu lệnh: `A traditional logo for a baking company on a solid color background. Include the text Seed.`

   ![Ví dụ 3 về tham số hoá câu lệnh của Imagen 4](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_baking.png?hl=vi)

### Kỹ thuật viết câu lệnh nâng cao

Hãy sử dụng các ví dụ sau để tạo câu lệnh cụ thể hơn dựa trên các thuộc tính như nội dung mô tả về nhiếp ảnh, hình dạng và chất liệu, các phong trào nghệ thuật trong lịch sử và các đối tượng sửa đổi chất lượng hình ảnh.

#### Nhiếp ảnh

- Câu lệnh bao gồm: *"Một bức ảnh về..."*

Để sử dụng kiểu này, hãy bắt đầu bằng cách dùng các từ khoá cho Imagen biết rõ rằng bạn đang tìm kiếm một bức ảnh. Bắt đầu câu lệnh bằng *"Một bức ảnh về. . ."*. Ví dụ:

|  |  |  |
| --- | --- | --- |
| photorealistic sample image 1   Câu lệnh: **Ảnh chụp** hạt cà phê trong bếp trên bề mặt gỗ | photorealistic sample image 2   Câu lệnh: **Ảnh chụp** một thanh sô cô la trên mặt bếp | hình ảnh mẫu giống thật 3   Câu lệnh: **Ảnh chụp** một toà nhà hiện đại có nước ở phía sau |

Nguồn hình ảnh: Mỗi hình ảnh được tạo bằng câu lệnh văn bản tương ứng với mô hình Imagen 4.

##### Đối tượng sửa đổi nhiếp ảnh

Trong các ví dụ sau, bạn có thể thấy một số tham số và giá trị sửa đổi dành riêng cho nhiếp ảnh. Bạn có thể kết hợp nhiều đối tượng sửa đổi để kiểm soát chính xác hơn.

1. **Khoảng cách chụp của camera** – *Cận cảnh, chụp từ xa*

   |  |  |
   | --- | --- |
   | ảnh mẫu chụp cận cảnh bằng camera   Câu lệnh: Ảnh **cận cảnh** hạt cà phê | hình ảnh mẫu của camera ở chế độ thu phóng   Câu lệnh: Ảnh **thu nhỏ** của một túi nhỏ đựng  hạt cà phê trong một căn bếp bừa bộn |
2. **Vị trí camera** – *trên không, từ dưới lên*

   |  |  |
   | --- | --- |
   | ảnh mẫu chụp từ trên không   Câu lệnh: **ảnh chụp từ trên không** về một thành phố đô thị có nhiều nhà cao tầng | hình ảnh mẫu về góc nhìn từ bên dưới   Câu lệnh: Ảnh chụp tán rừng với bầu trời xanh **từ dưới lên** |
3. **Ánh sáng** – *tự nhiên, kịch tính, ấm áp, lạnh*

   |  |  |
   | --- | --- |
   | hình ảnh mẫu ánh sáng tự nhiên   Câu lệnh: ảnh chụp trong studio về một chiếc ghế bành hiện đại, **ánh sáng tự nhiên** | hình ảnh mẫu ánh sáng kịch tính   Câu lệnh: ảnh chụp trong phòng thu về một chiếc ghế bành hiện đại, **ánh sáng kịch tính** |
4. **Chế độ cài đặt camera** *– làm mờ chuyển động, tiêu điểm mềm, hiệu ứng bokeh, chân dung*

   |  |  |
   | --- | --- |
   | hình ảnh mẫu làm mờ chuyển động   Câu lệnh: ảnh chụp một thành phố có các toà nhà chọc trời từ bên trong một chiếc ô tô với **hiệu ứng làm mờ chuyển động** | hình ảnh mẫu tiêu điểm mềm   Câu lệnh: **ảnh chụp tiêu điểm mềm** một cây cầu trong thành phố vào ban đêm |
5. **Loại ống kính** – *35 mm, 50 mm, mắt cá, góc rộng, macro*

   |  |  |
   | --- | --- |
   | hình ảnh mẫu chụp bằng ống kính macro   Câu lệnh: ảnh chụp một chiếc lá, **ống kính macro** | hình ảnh mẫu chụp bằng ống kính mắt cá   Câu lệnh: nhiếp ảnh đường phố, thành phố New York, **ống kính mắt cá** |
6. **Loại phim** – *đen trắng, polaroid*

   |  |  |
   | --- | --- |
   | hình ảnh mẫu về ảnh polaroid   Câu lệnh: **ảnh chân dung chụp bằng máy polaroid** của một chú chó đeo kính râm | ảnh mẫu đen trắng   Câu lệnh: **ảnh đen trắng** về một chú chó đeo kính râm |

Nguồn hình ảnh: Mỗi hình ảnh được tạo bằng câu lệnh văn bản tương ứng với mô hình Imagen 4.

### Hình minh hoạ và nghệ thuật

- Câu lệnh có: *"Một painting về..."*, *"Một sketch của..."*

Phong cách nghệ thuật đa dạng từ phong cách đơn sắc như phác hoạ bằng bút chì, đến nghệ thuật số siêu thực. Ví dụ: các hình ảnh sau đây sử dụng cùng một câu lệnh nhưng có các kiểu khác nhau:

*"Một [art style or creation technique] về chiếc xe sedan điện thể thao góc cạnh với các toà nhà chọc trời ở phía sau"*

|  |  |  |
| --- | --- | --- |
| hình ảnh mẫu về tác phẩm nghệ thuật   Câu lệnh: **Bản vẽ kỹ thuật bằng bút chì** về một... | hình ảnh mẫu về tác phẩm nghệ thuật   Câu lệnh: Một **bức vẽ bằng chì than** về một... | hình ảnh mẫu về tác phẩm nghệ thuật   Câu lệnh: **Bức vẽ bằng bút chì màu** về một... |

|  |  |  |
| --- | --- | --- |
| hình ảnh mẫu về tác phẩm nghệ thuật   Câu lệnh: Một **bức tranh vẽ bằng phấn màu** về một... | hình ảnh mẫu về tác phẩm nghệ thuật   Câu lệnh: **Tranh kỹ thuật số** về một... | hình ảnh mẫu về tác phẩm nghệ thuật   Câu lệnh: Một **bức áp phích theo phong cách art deco** về một... |

Nguồn hình ảnh: Mỗi hình ảnh được tạo bằng câu lệnh văn bản tương ứng với mô hình Imagen 2.

##### Hình dạng và chất liệu

- Câu lệnh có: *"...làm bằng..."*, *"...có hình dạng..."*

Một trong những điểm mạnh của công nghệ này là bạn có thể tạo ra những hình ảnh mà nếu không có công nghệ này thì bạn khó hoặc không thể tạo được. Ví dụ: bạn có thể tạo lại biểu trưng công ty bằng nhiều chất liệu và kết cấu.

|  |  |  |
| --- | --- | --- |
| shapes and materials example image 1   Câu lệnh: một chiếc túi du lịch **làm bằng** phô mai | hình ảnh ví dụ 2 về hình dạng và chất liệu   Câu lệnh: ống neon **có hình dạng** của một con chim | hình ảnh ví dụ 3 về hình dạng và vật liệu   Câu lệnh: một chiếc ghế bành **làm bằng giấy**, ảnh chụp trong phòng chụp ảnh, phong cách origami |

Nguồn hình ảnh: Mỗi hình ảnh được tạo bằng câu lệnh văn bản tương ứng với mô hình Imagen 4.

#### Tài liệu tham khảo về nghệ thuật trong lịch sử

- Câu lệnh có chứa: *"...theo phong cách của..."*

Một số phong cách đã trở thành biểu tượng qua nhiều năm. Sau đây là một số ý tưởng về phong cách hội hoạ hoặc nghệ thuật trong lịch sử mà bạn có thể thử.

*"Tạo hình ảnh theo phong cách của [art period or movement]
: một trang trại gió"*

|  |  |  |
| --- | --- | --- |
| hình ảnh ví dụ về trường phái ấn tượng   Câu lệnh: tạo một hình ảnh **theo phong cách *hội hoạ trường phái ấn tượng***: một trang trại gió | hình ảnh ví dụ về thời Phục hưng   Câu lệnh: tạo một hình ảnh **theo phong cách *tranh thời Phục hưng***: một trang trại gió | hình ảnh ví dụ về nghệ thuật đại chúng   Tạo hình ảnh: tạo một hình ảnh **theo phong cách *nghệ thuật đại chúng***: một trang trại điện gió |

Nguồn hình ảnh: Mỗi hình ảnh được tạo bằng câu lệnh văn bản tương ứng với mô hình Imagen 4.

#### Các tham số sửa đổi chất lượng hình ảnh

Một số từ khoá có thể cho mô hình biết rằng bạn đang tìm kiếm một thành phần chất lượng cao. Sau đây là một số ví dụ về hệ số điều chỉnh chất lượng:

- **Đối tượng sửa đổi chung** – *chất lượng cao, đẹp, cách điệu*
- **Ảnh** – *4K, HDR, ảnh chụp trong phòng chụp*
- **Nghệ thuật, Hình minh hoạ** – *do chuyên gia tạo ra, chi tiết*

Sau đây là một vài ví dụ về câu lệnh không có công cụ sửa đổi chất lượng và câu lệnh tương tự có công cụ sửa đổi chất lượng.

|  |  |
| --- | --- |
| ví dụ về hình ảnh bắp không có đối tượng sửa đổi   Câu lệnh (không có bộ sửa đổi chất lượng): ảnh chụp một cây ngô | hình ảnh mẫu về bắp có đối tượng sửa đổi   Câu lệnh (có bộ sửa đổi chất lượng): **Ảnh 4K HDR tuyệt đẹp**   về một cây ngô **do một   nhiếp ảnh gia chuyên nghiệp chụp** |

Nguồn hình ảnh: Mỗi hình ảnh được tạo bằng câu lệnh văn bản tương ứng với mô hình Imagen 4.

#### Tỷ lệ khung hình

Tính năng tạo hình ảnh của Imagen cho phép bạn đặt 5 tỷ lệ khung hình riêng biệt cho hình ảnh.

1. **Vuông** (1:1, mặc định) – Ảnh vuông tiêu chuẩn. Tỷ lệ khung hình này thường được dùng cho bài đăng trên mạng xã hội.
2. **Toàn màn hình** (4:3) – Tỷ lệ khung hình này thường được dùng trong nội dung nghe nhìn hoặc phim.
   Đây cũng là kích thước của hầu hết các TV cũ (không phải màn hình rộng) và máy ảnh định dạng trung bình. Tỷ lệ này chụp được nhiều cảnh hơn theo chiều ngang (so với tỷ lệ 1:1), khiến đây trở thành tỷ lệ khung hình ưu tiên cho nhiếp ảnh.

   |  |  |
   | --- | --- |
   | ví dụ về tỷ lệ khung hình   Câu lệnh: cận cảnh ngón tay của một nhạc sĩ đang chơi đàn piano, phim đen trắng, cổ điển (tỷ lệ khung hình 4:3) | ví dụ về tỷ lệ khung hình   Câu lệnh: Bức ảnh chuyên nghiệp chụp khoai tây chiên trong phòng thu cho một nhà hàng cao cấp, theo phong cách của một tạp chí ẩm thực (tỷ lệ khung hình 4:3) |
3. **Toàn màn hình dọc** (3:4) – Đây là tỷ lệ khung hình toàn màn hình được xoay 90 độ. Điều này cho phép bạn chụp cảnh theo chiều dọc nhiều hơn so với tỷ lệ khung hình 1:1.

   |  |  |
   | --- | --- |
   | ví dụ về tỷ lệ khung hình   Câu lệnh: một người phụ nữ đang đi bộ đường dài, cận cảnh đôi ủng của cô ấy phản chiếu trong một vũng nước, những ngọn núi lớn ở phía sau, theo phong cách của một quảng cáo, góc quay ấn tượng (tỷ lệ khung hình 3:4) | ví dụ về tỷ lệ khung hình   Câu lệnh: ảnh chụp từ trên không về một dòng sông chảy qua một thung lũng huyền bí (tỷ lệ khung hình 3:4) |
4. **Màn hình rộng** (16:9) – Tỷ lệ này đã thay thế tỷ lệ 4:3 và hiện là tỷ lệ khung hình phổ biến nhất cho TV, màn hình và màn hình điện thoại di động (chế độ ngang).
   Hãy sử dụng tỷ lệ khung hình này khi bạn muốn chụp nhiều cảnh nền hơn (ví dụ: cảnh quan thiên nhiên).

   ![ví dụ về tỷ lệ khung hình](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_16-9_man.png?hl=vi)

   Câu lệnh: một người đàn ông mặc quần áo toàn màu trắng đang ngồi trên bãi biển, cận cảnh, ánh sáng khung giờ vàng (tỷ lệ khung hình 16:9)
5. **Dọc** (9:16) – Tỷ lệ này là tỷ lệ màn hình rộng nhưng được xoay. Đây là một tỷ lệ khung hình tương đối mới và được các ứng dụng video ngắn (ví dụ: YouTube Shorts) ưa chuộng. Sử dụng chế độ này cho các đối tượng cao có hướng dọc mạnh mẽ, chẳng hạn như toà nhà, cây, thác nước hoặc các đối tượng tương tự khác.

   ![ví dụ về tỷ lệ khung hình](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_9-16_skyscraper.png?hl=vi)

   Câu lệnh: hình ảnh kỹ thuật số của một toà nhà chọc trời đồ sộ, hiện đại, hùng vĩ, hoành tráng với cảnh hoàng hôn tuyệt đẹp ở phía sau (tỷ lệ khung hình 9:16)

#### Hình ảnh chân thực

Các phiên bản khác nhau của mô hình tạo hình ảnh có thể cung cấp cả đầu ra mang tính nghệ thuật và chân thực như ảnh chụp. Hãy sử dụng những từ ngữ sau trong câu lệnh để tạo ra kết quả chân thực hơn, dựa trên chủ đề mà bạn muốn tạo.

| Trường hợp sử dụng | Loại ống kính | Tiêu cự | Thông tin chi tiết bổ sung |
| --- | --- | --- | --- |
| Người (ảnh chân dung) | Prime, zoom | 24-35mm | phim đen trắng, phim noir, độ sâu trường ảnh, hai tông màu (nêu 2 màu) |
| Thực phẩm, côn trùng, thực vật (vật thể, tĩnh vật) | Macro | 60-105mm | Độ chi tiết cao, lấy nét chính xác, ánh sáng được kiểm soát |
| Thể thao, động vật hoang dã (chuyển động) | Thu phóng bằng ống kính chụp xa | 100-400mm | Tốc độ màn trập nhanh, theo dõi hành động hoặc chuyển động |
| Thiên văn học, phong cảnh (góc rộng) | Ống kính góc rộng | 10-24mm | Thời gian phơi sáng lâu, tiêu cự sắc nét, phơi sáng lâu, nước hoặc mây mịn |

##### Chân dung

| Trường hợp sử dụng | Loại ống kính | Tiêu cự | Thông tin chi tiết bổ sung |
| --- | --- | --- | --- |
| Người (ảnh chân dung) | Prime, zoom | 24-35mm | phim đen trắng, phim noir, độ sâu trường ảnh, hai tông màu (nêu 2 màu) |

Dựa vào một số từ khoá trong bảng, Imagen có thể tạo ra những bức chân dung sau:

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về ảnh chân dung | ví dụ về ảnh chân dung | ví dụ về ảnh chân dung | ví dụ về ảnh chân dung |

Câu lệnh: *Một phụ nữ, ảnh chân dung 35 mm, tông màu kép xanh dương và xám*  
Mô hình: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về ảnh chân dung | ví dụ về ảnh chân dung | ví dụ về ảnh chân dung | ví dụ về ảnh chân dung |

Câu lệnh: *Một phụ nữ, ảnh chân dung 35 mm, phim noir*  
Người mẫu: `imagen-4.0-generate-001`

##### Đồ vật

| Trường hợp sử dụng | Loại ống kính | Tiêu cự | Thông tin chi tiết bổ sung |
| --- | --- | --- | --- |
| Thực phẩm, côn trùng, thực vật (vật thể, tĩnh vật) | Macro | 60-105mm | Độ chi tiết cao, lấy nét chính xác, ánh sáng được kiểm soát |

Bằng cách sử dụng một số từ khoá trong bảng, Imagen có thể tạo các hình ảnh đối tượng sau:

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về chụp ảnh vật thể | ví dụ về chụp ảnh vật thể | ví dụ về chụp ảnh vật thể | ví dụ về chụp ảnh vật thể |

Câu lệnh: *lá của cây cầu nguyện, ống kính macro, 60mm*  
Mô hình: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về chụp ảnh vật thể | ví dụ về chụp ảnh vật thể | ví dụ về chụp ảnh vật thể | ví dụ về chụp ảnh vật thể |

Câu lệnh: *một đĩa mì ống, ống kính macro 100 mm*  
Mô hình: `imagen-4.0-generate-001`

##### Chuyển động

| Trường hợp sử dụng | Loại ống kính | Tiêu cự | Thông tin chi tiết bổ sung |
| --- | --- | --- | --- |
| Thể thao, động vật hoang dã (chuyển động) | Thu phóng bằng ống kính chụp xa | 100-400mm | Tốc độ màn trập nhanh, theo dõi hành động hoặc chuyển động |

Bằng cách sử dụng một số từ khoá trong bảng, Imagen có thể tạo ra những hình ảnh chuyển động sau:

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về ảnh chuyển động | ví dụ về ảnh chuyển động | ví dụ về ảnh chuyển động | ví dụ về ảnh chuyển động |

Câu lệnh: *một pha tiếp bóng thành công, tốc độ màn trập nhanh, theo dõi chuyển động*  
Mô hình: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về ảnh chuyển động | ví dụ về ảnh chuyển động | ví dụ về ảnh chuyển động | ví dụ về ảnh chuyển động |

Câu lệnh: *Một chú hươu đang chạy trong rừng, tốc độ màn trập nhanh, theo dõi chuyển động*  
Mô hình: `imagen-4.0-generate-001`

##### Ống kính góc rộng

| Trường hợp sử dụng | Loại ống kính | Tiêu cự | Thông tin chi tiết bổ sung |
| --- | --- | --- | --- |
| Thiên văn học, phong cảnh (góc rộng) | Ống kính góc rộng | 10-24mm | Thời gian phơi sáng lâu, tiêu cự sắc nét, phơi sáng lâu, nước hoặc mây mịn |

Bằng cách sử dụng một số từ khoá trong bảng, Imagen có thể tạo ra những hình ảnh góc rộng sau đây:

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về ảnh góc rộng | ví dụ về ảnh góc rộng | ví dụ về ảnh góc rộng | ví dụ về ảnh góc rộng |

Câu lệnh: *một dãy núi rộng lớn, phong cảnh góc rộng 10 mm*  
Mô hình: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| ví dụ về ảnh góc rộng | ví dụ về ảnh góc rộng | ví dụ về ảnh góc rộng | ví dụ về ảnh góc rộng |

Câu lệnh: *một bức ảnh về mặt trăng, ảnh thiên văn, góc rộng 10 mm*  
Mô hình: `imagen-4.0-generate-001`

## Phiên bản mô hình

### Imagen 4 (Không dùng nữa)

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `imagen-4.0-generate-001`  `imagen-4.0-ultra-generate-001`  `imagen-4.0-fast-generate-001` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản  **Đầu ra**  Hình ảnh |
| token\_autoGiới hạn mã thông báo[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | **Giới hạn mã thông báo đầu vào**  480 token (văn bản)  **Hình ảnh đầu ra**  1 đến 4 (Ultra/Standard/Fast) |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 6 năm 2025 |

### Imagen 3

Mô hình Imagen 3 đã [tắt](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-16 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-16 UTC."],[],[]]
