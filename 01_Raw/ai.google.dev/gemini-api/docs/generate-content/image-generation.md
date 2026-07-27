---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=ko
fetched_at: 2026-07-27T04:39:04.635400+00:00
title: "Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Nano Banana 이미지 생성

프롬프트를 사용하여 완전한 기능을 갖춘 UI 완성 앱의 프로토타입을 제작하고 Nano Banana 2가 실제 도구, 데이터, Gemini 생태계와 통합된 모습을 확인하세요. 코드를 한 줄도 작성하지 않고 말입니다.

- [Nano Banana 2 앱 사용해 보기](https://aistudio.google.com/apps/bundled/pet_passport?hl=ko)
- 또는 프롬프트에서 직접 빌드할 수 있습니다.

- ![잡지](https://storage.googleapis.com/generativeai-downloads/images/magazine-2.jpg)
  ![런던](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/05-output.jpg)
  ![복원](https://storage.googleapis.com/generativeai-downloads/images/quetzal.png)
  ![banana](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/06-output.jpg)
  ![카페](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/02-a-photo-of-an-everyday-scene-at-a-busy-cafe-servin.jpg)
  ![기사](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/10-use-search-to-find-how-the-gemini-3-flash-launch-h.jpg)
  ![개](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/01-an-icon-representing-a-cute-dog-the-background-is-.jpg)
  ![아이소메트릭](https://storage.googleapis.com/generativeai-downloads/images/isometric-pool.jpg)
- ![잡지](https://storage.googleapis.com/generativeai-downloads/images/magazine-2.jpg)

  Nano Banana 2로 생성됨

  **프롬프트:** '유광 잡지 표지 사진. 미니멀한 파란색 표지에는 굵은 글씨로 Nano Banana라고 적혀 있습니다. 텍스트는 세리프 글꼴로 되어 있으며 뷰를 채웁니다. 다른 텍스트는 없습니다. 텍스트 앞에는 세련되고 미니멀한 드레스를 입은 사람의 인물 사진이 있습니다. 그녀는 초점인 숫자 2를 장난스럽게 들고 있습니다.
    
  바코드와 함께 문제 번호와 '2026년 2월' 날짜를 모서리에 넣습니다. 잡지는 디자이너 매장 내 오렌지색 회반죽 벽에 있는 선반에 있습니다.'

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=ko)에서 [전문적인 제품 사진](#4_product_mockups_commercial_photography) 만들기
- ![런던](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/05-output.jpg)

  Nano Banana Pro로 생성됨

  **프롬프트:** '런던의 가장 상징적인 랜드마크와 건축 요소를 보여주는 45도 각도로 위에서 내려다보는 구도의 아이소메트릭 미니어처 3D 만화 장면을 명확하게 표현해 줘. 사실적인 PBR 소재와 부드럽고 섬세한 질감, 부드럽고 사실적인 조명과 그림자를 사용해 줘. 현재 날씨 조건을 도시 환경에 직접 통합하여 몰입감 있는 분위기를 조성합니다. 부드러운 단색 배경을 사용하여 깨끗하고 미니멀한 구도를 사용합니다. 상단 중앙에 'London'이라는 제목을 큰 굵은 글씨로 배치하고 그 아래에 눈에 띄는 날씨 아이콘, 날짜 (작은 텍스트), 온도 (중간 텍스트)를 배치합니다. 모든 텍스트는 일관된 간격으로 가운데에 배치되어야 하며 건물의 상단과 미묘하게 겹칠 수 있습니다.'

  [검색 그라운딩](#use-with-grounding)에 대해 자세히 알아보고 [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=ko)에서 사용해 보세요.
- ![케트살](https://storage.googleapis.com/generativeai-downloads/images/quetzal.png)

  Nano Banana 2로 생성됨

  **프롬프트:** '이미지 검색을 사용하여 화려한 케찰새의 정확한 이미지를 찾아 줘. 자연스러운 위아래 그라데이션과 최소한의 구성으로 이 새의 아름다운 3:2 배경화면을 만들어 줘."

  Nano Banana 2를 사용하여 Google [이미지 검색](#image-search) 그라운딩을 사용합니다. [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=ko)에서 사용해 보기
- ![banana](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/06.jpg)

  Nano Banana Pro로 생성됨

  **프롬프트:** '바나나 향수 고급 광고에 이 로고를 넣어 줘. 로고가 병에 완벽하게 통합되어 있습니다.'

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=ko)에서 Nano Banana의 [높은 충실도 디테일 보존](#5_high-fidelity_detail_preservation)을 사용해 보세요.
- ![카페](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/02-a-photo-of-an-everyday-scene-at-a-busy-cafe-servin.jpg)

  Nano Banana Pro로 생성됨

  **프롬프트:** '아침 식사를 제공하는 번화한 카페의 일상적인 장면 사진. 앞쪽에는 파란색 머리의 애니메이션 남자가 있고, 한 사람은 연필 스케치, 다른 사람은 클레이 애니메이션 사람입니다.'

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=ko)의 Nano Banana로 다양한 [예술적 스타일](#3_style_transfer)을 실험해 보세요.
- ![기사](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/10-use-search-to-find-how-the-gemini-3-flash-launch-h.jpg)

  Nano Banana Pro로 생성됨

  **프롬프트:** '검색을 사용하여 Gemini 3 Flash 출시가 어떻게 받아들여졌는지 알아봐. 이 정보를 사용하여 제목이 있는 짧은 기사를 작성하세요. 디자인에 중점을 둔 광택 잡지에 표시된 기사의 사진을 반환해 줘. Gemini 3 Flash에 관한 기사를 보여주는 단일 페이지가 접혀 있는 사진입니다. 히어로 사진 1장 광고 제목은 세리프입니다.'

  [검색](#use-with-grounding)에서 [정확한 텍스트](#3_accurate_text_in_images)를 생성합니다. [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=ko)에서 Nano Banana 사용해 보기
- ![개](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/01-an-icon-representing-a-cute-dog-the-background-is-.jpg)

  Nano Banana Pro로 생성됨

  **프롬프트:** '귀여운 강아지를 나타내는 아이콘. 배경은 흰색입니다. 아이콘을 다채롭고 촉각적인 3D 스타일로 만들어 줘. 텍스트가 없습니다.'

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=ko)에서 Nano Banana로 [아이콘, 스티커, 애셋](#2_stylized_illustrations_stickers) 만들기
- ![아이소메트릭](https://storage.googleapis.com/generativeai-downloads/images/isometric-pool.jpg)

  Nano Banana 2로 생성됨

  **프롬프트:** '완벽한 등각 투영법으로 사진을 만들어 줘. 미니어처가 아니라 완벽한 등각 투영법으로 촬영된 사진입니다. 아름다운 현대식 정원의 사진입니다. 2 모양의 큰 수영장과 'Nano Banana 2'라는 단어가 있습니다.'

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=ko)에서 [사실적인 이미지 생성](#1_photorealistic_scenes)을 사용해 보세요.

**Nano Banana**는 Gemini의 기본 이미지 생성 기능의 이름입니다.
Gemini는 텍스트, 이미지, 동영상 또는 이들의 조합을 사용하여 대화형으로 이미지를 생성하고 처리할 수 있습니다. 이를 통해 전례 없이 세밀하게 제어하면서 시각적 요소를 만들고, 수정하고, 반복할 수 있습니다.

Nano Banana는 Gemini API에서 사용할 수 있는 4가지 고유한 모델을 의미합니다.

- **Nano Banana 2 Lite ([Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=ko))
  (`gemini-3.1-flash-lite-image`):** 속도와 비용이 주요 운영 제약 조건인 환경에서 속도와 확장성을 위해 설계된 가장 빠르고 저렴한 Gemini 이미지 모델입니다. 여러 참조 입력 또는 멀티턴 순차 편집에 최적화되어 있지 않습니다.
- **Nano Banana 2 ([Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=ko))
  (`gemini-3.1-flash-image`):** 모든 작업을 위한 가장 다재다능한 모델이자 일반적인 워크호스 모델입니다. 속도와 최첨단 4K 생성, 세계에 관한 지식, 안정적인 텍스트 렌더링의 균형을 맞춥니다. 여러 참고 이미지 처리 및 일관성에서 뛰어남
- **Nano Banana Pro ([Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=ko))
  (`gemini-3-pro-image`):** 가장 복잡한 시각적 작업을 위한 프리미엄 옵션으로, 최고 수준의 세계 지식, 고급 현지화, 정확한 브랜드 일관성, 정밀한 크리에이티브 컨트롤을 제공합니다.
- **Nano Banana ([Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ko))
  (`gemini-2.5-flash-image`):** Nano Banana 시리즈의 기존 선두 주자입니다.
  Nano Banana 2 Lite는 안정적인 성능을 제공하지만, 향상된 품질, 더 빠른 생성 속도, 더 낮은 API 가격을 경험하려면 Nano Banana 2 Lite로 전환하는 것이 좋습니다.

생성된 모든 이미지에는 [SynthID 워터마크](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ko)가 포함됩니다.

## 이미지 생성 (텍스트 이미지 변환)

### Python

```
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = ("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme")
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt =
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme";

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
  });
  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
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
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.1-flash-image",
      genai.Text("Create a picture of a nano banana dish in a " +
                 " fancy restaurant with a Gemini theme"),
  )

  for _, part := range result.Candidates[0].Content.Parts {
      if part.Text != "" {
          fmt.Println(part.Text)
      } else if part.InlineData != nil {
          imageBytes := part.InlineData.Data
          outputFilename := "gemini_generated_image.png"
          _ = os.WriteFile(outputFilename, imageBytes, 0644)
      }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class TextToImage {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme",
          config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("_01_generated_image.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class TextToImage {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme" }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("generated_image.png", imageBytes);
                Console.WriteLine("Image saved as generated_image.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }]
  }'
```

## 이미지 편집 (텍스트 및 이미지 간)

**참고**: 업로드하는 이미지에 대한 필요한 권리를 보유하고 있는지 확인하세요.
속이거나, 괴롭히거나, 피해를 입히는 동영상 또는 이미지를 비롯해 다른 사람의 권리를 침해하는 콘텐츠를 생성하면 안 됩니다. 이 생성형 AI 서비스의 사용에는 Google의 [금지된 사용 정책](https://policies.google.com/terms/generative-ai/use-policy?hl=ko)이 적용됩니다.

이미지를 제공하고 텍스트 프롬프트를 사용하여 요소를 추가, 삭제 또는 수정하거나, 스타일을 변경하거나, 색상 그레이딩을 조정합니다.

다음 예에서는 `base64`로 인코딩된 이미지를 업로드하는 방법을 보여줍니다.
여러 이미지, 더 큰 페이로드, 지원되는 MIME 유형은 [이미지 이해](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko) 페이지를 참고하세요.

### Python

```
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = (
    "Create a picture of my cat eating a nano-banana in a "
    "fancy restaurant under the Gemini constellation",
)

image = Image.open("/path/to/cat_image.png")

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt, image],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const imagePath = "path/to/cat_image.png";
  const imageData = fs.readFileSync(imagePath);
  const base64Image = imageData.toString("base64");

  const prompt = [
    { text: "Create a picture of my cat eating a nano-banana in a" +
            "fancy restaurant under the Gemini constellation" },
    {
      inlineData: {
        mimeType: "image/png",
        data: base64Image,
      },
    },
  ];

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
  });
  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
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
 "log"
 "os"
 "google.golang.org/genai"
)

func main() {

 ctx := context.Background()
 client, err := genai.NewClient(ctx, nil)
 if err != nil {
     log.Fatal(err)
 }

 imagePath := "/path/to/cat_image.png"
 imgData, _ := os.ReadFile(imagePath)

 parts := []*genai.Part{
   genai.NewPartFromText("Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation"),
   &genai.Part{
     InlineData: &genai.Blob{
       MIMEType: "image/png",
       Data:     imgData,
     },
   },
 }

 contents := []*genai.Content{
   genai.NewContentFromParts(parts, genai.RoleUser),
 }

 result, _ := client.Models.GenerateContent(
     ctx,
     "gemini-3.1-flash-image",
     contents,
 )

 for _, part := range result.Candidates[0].Content.Parts {
     if part.Text != "" {
         fmt.Println(part.Text)
     } else if part.InlineData != nil {
         imageBytes := part.InlineData.Data
         outputFilename := "gemini_generated_image.png"
         _ = os.WriteFile(outputFilename, imageBytes, 0644)
     }
 }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class TextAndImageToImage {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          Content.fromParts(
              Part.fromText("""
                  Create a picture of my cat eating a nano-banana in
                  a fancy restaurant under the Gemini constellation
                  """),
              Part.fromBytes(
                  Files.readAllBytes(
                      Path.of("src/main/resources/cat.jpg")),
                  "image/jpeg")),
          config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("gemini_generated_image.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class TextAndImageToImage {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation" },
            new Part
            {
                FileData = new FileData { FileUri = "file:///path/to/cat_image.png" }
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("gemini_generated_image.png", imageBytes);
                Console.WriteLine("Image saved as gemini_generated_image.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d "{
      \"contents\": [{
        \"parts\":[
            {\"text\": \"'Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation\"},
            {
              \"inline_data\": {
                \"mime_type\":\"image/jpeg\",
                \"data\": \"<BASE64_IMAGE_DATA>\"
              }
            }
        ]
      }]
    }"
```

### 멀티턴 이미지 수정

대화형으로 이미지를 계속 생성하고 수정하세요. 이미지를 반복하는 데는 채팅 또는 멀티턴 대화가 권장됩니다. 다음 예에서는 광합성에 관한 인포그래픽을 생성하는 프롬프트를 보여줍니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.1-flash-image",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        tools=[{"google_search": {}}]
    )
)

message = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader."

response = chat.send_message(message)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("photosynthesis.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.1-flash-image",
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      tools: [{googleSearch: {}}],
    },
  });
}

await main();

const message = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader."

let response = await chat.sendMessage({message});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("photosynthesis.png", buffer);
      console.log("Image saved as photosynthesis.png");
    }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Text, genai.Image},
    }
    chat := model.StartChat()

    message := "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader."

    resp, err := chat.SendMessage(ctx, genai.Text(message))
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("photosynthesis.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;
import com.google.genai.types.RetrievalConfig;
import com.google.genai.types.Tool;
import com.google.genai.types.ToolConfig;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class MultiturnImageEditing {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {

      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .tools(Tool.builder()
              .googleSearch(GoogleSearch.builder().build())
              .build())
          .build();

      Chat chat = client.chats.create("gemini-3.1-flash-image", config);

      GenerateContentResponse response = chat.sendMessage("""
          Create a vibrant infographic that explains photosynthesis
          as if it were a recipe for a plant's favorite food.
          Show the "ingredients" (sunlight, water, CO2)
          and the "finished dish" (sugar/energy).
          The style should be like a page from a colorful
          kids' cookbook, suitable for a 4th grader.
          """);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("photosynthesis.png"), blob.data().get());
          }
        }
      }
      // ...
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class MultiturnImageEditing {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            Tools = new List<Tool> { new Tool { GoogleSearch = new GoogleSearch() } }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("photosynthesis.png", imageBytes);
                Console.WriteLine("Image saved as photosynthesis.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {"text": "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plants favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids cookbook, suitable for a 4th grader."}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"]
    }
  }'
```

![광합성에 관한 AI 생성 인포그래픽](https://ai.google.dev/static/gemini-api/docs/images/infographic-eng.png?hl=ko)

광합성에 관한 AI 생성 인포그래픽

그런 다음 동일한 채팅을 사용하여 그래픽의 언어를 스페인어로 변경할 수 있습니다.

### Python

```
message = "Update this infographic to be in Spanish. Do not change any other elements of the image."
aspect_ratio = "16:9" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "2K" # "512", "1K", "2K", "4K"

response = chat.send_message(message,
    config=types.GenerateContentConfig(
        response_format={"image": {aspect_ratio: aspect_ratio,                 image_size: resolution}},
    ))

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("photosynthesis_spanish.png")
```

### JavaScript

```
const message = 'Update this infographic to be in Spanish. Do not change any other elements of the image.';
const aspectRatio = '16:9';
const resolution = '2K';

let response = await chat.sendMessage({
  message,
  config: {
    responseModalities: ['TEXT', 'IMAGE'],
    responseFormat: {
    image: {
      aspectRatio: aspectRatio,
      imageSize: resolution,
    }
  },
    tools: [{googleSearch: {}}],
  },
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("photosynthesis2.png", buffer);
      console.log("Image saved as photosynthesis2.png");
    }
}
```

### Go

```
message = "Update this infographic to be in Spanish. Do not change any other elements of the image."
aspect_ratio = "16:9" // "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "2K"     // "512", "1K", "2K", "4K"

model.GenerationConfig.ImageConfig = &pb.ImageConfig{
    AspectRatio: aspect_ratio,
    ImageSize:   resolution,
}

resp, err = chat.SendMessage(ctx, genai.Text(message))
if err != nil {
    log.Fatal(err)
}

for _, part := range resp.Candidates[0].Content.Parts {
    if txt, ok := part.(genai.Text); ok {
        fmt.Printf("%s", string(txt))
    } else if img, ok := part.(genai.ImageData); ok {
        err := os.WriteFile("photosynthesis_spanish.png", img.Data, 0644)
        if err != nil {
            log.Fatal(err)
        }
    }
}
```

### Java

```
String aspectRatio = "16:9"; // "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
String resolution = "2K"; // "512", "1K", "2K", "4K"

config = GenerateContentConfig.builder()
    .responseModalities("TEXT", "IMAGE")
    .imageConfig(ImageConfig.builder()
        .aspectRatio(aspectRatio)
        .imageSize(resolution)
        .build())
    .build();

response = chat.sendMessage(
    "Update this infographic to be in Spanish. " +
    "Do not change any other elements of the image.",
    config);

for (Part part : response.parts()) {
  if (part.text().isPresent()) {
    System.out.println(part.text().get());
  } else if (part.inlineData().isPresent()) {
    var blob = part.inlineData().get();
    if (blob.data().isPresent()) {
      Files.write(Paths.get("photosynthesis_spanish.png"), blob.data().get());
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class MultiturnImageEditingSpanish {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Update this infographic to be in Spanish. Do not change any other elements of the image." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "16:9",
                ImageSize = "2K"
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("photosynthesis_spanish.png", imageBytes);
                Console.WriteLine("Image saved as photosynthesis_spanish.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "Create a vibrant infographic that explains photosynthesis..."}]
      },
      {
        "role": "model",
        "parts": [{"inline_data": {"mime_type": "image/png", "data": "<PREVIOUS_IMAGE_DATA>"}}]
      },
      {
        "role": "user",
        "parts": [{"text": "Update this infographic to be in Spanish. Do not change any other elements of the image."}]
      }
    ],
    "tools": [{"google_search": {}}],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "responseFormat": {
    "image": {
        "aspectRatio": "16:9",
        "imageSize": "2K"
      }
  }
    }
  }'
```

![스페인어로 된 광합성의 AI 생성 인포그래픽](https://ai.google.dev/static/gemini-api/docs/images/infographic-spanish.png?hl=ko)

스페인어로 된 광합성 AI 생성 인포그래픽

## Gemini 3 이미지 모델의 새로운 기능

Gemini 3는 최첨단 이미지 생성 및 편집 모델을 제공합니다. Gemini 3.1 Flash Image는 속도와 대량 사용 사례에 최적화되어 있으며 Gemini 3 Pro Image는 전문적인 애셋 제작에 최적화되어 있습니다.
고급 추론을 통해 가장 어려운 워크플로를 처리하도록 설계되었으며, 복잡한 멀티턴 생성 및 수정 작업에 탁월합니다.

- **고해상도 출력**: 1K, 2K, 4K 시각적 요소를 생성하는 기능이 내장되어 있습니다.
  - **Gemini 3.1 Flash Image**에 더 작은 512 (0.5K) 해상도가 추가됩니다.
  - **Gemini 3.1 Flash Lite Image**는 1K 해상도만 지원합니다.
- **고급 텍스트 렌더링**: 인포그래픽, 메뉴, 다이어그램, 마케팅 애셋에 대해 읽기 쉽고 스타일이 지정된 텍스트를 생성할 수 있습니다.
- **Google 검색을 사용한 그라운딩**: 모델이 Google 검색을 도구로 사용하여 사실을 확인하고 실시간 데이터 (예: 현재 날씨 지도, 주식 차트, 최근 이벤트)를 기반으로 이미지를 생성할 수 있습니다.
  - **Gemini 3.1 Flash-Lite 이미지 모델에서 지원되지 않습니다.**
  - **Gemini 3.1 Flash Image**는 웹 검색과 함께 이미지용 Google 검색을 사용한 그라운딩을 통합합니다.
- **사고 모드**: 모델이 '사고' 과정을 활용하여 복잡한 프롬프트를 추론합니다. 최종 고화질 출력을 생성하기 전에 구도를 다듬기 위해 임시 '생각 이미지' (백엔드에 표시되지만 요금이 청구되지 않음)를 생성합니다.
- **최대 14개의 참고 이미지**: 이제 최대 14개의 참고 이미지를 혼합하여 최종 이미지를 생성할 수 있습니다.
- **새 가로세로 비율**: Gemini 3.1 Flash Lite Image에 `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` [가로세로 비율](#aspect_ratios_and_image_size)이 추가됩니다.

### 최대 14개의 참조 이미지 사용

Gemini 3 이미지 모델을 사용하면 최대 14개의 참조 이미지를 혼합할 수 있습니다. 이러한 14개의 이미지에는 다음이 포함될 수 있습니다.

| Gemini 3.1 Flash Lite 이미지 | Gemini 3.1 Flash Image | Gemini 3 Pro Image |
| --- | --- | --- |
| 최종 이미지에 포함할 충실도가 높은 객체의 이미지(최대 14개) | 최종 이미지에 포함할 충실도가 높은 객체의 이미지(최대 10개) | 최종 이미지에 포함할 충실도가 높은 객체의 이미지(최대 6개) |
| 해당 사항 없음 | 캐릭터 일관성을 유지하기 위한 캐릭터 이미지 최대 4개 | 캐릭터 일관성을 유지하기 위한 캐릭터 이미지 최대 5개 |
| 해당 사항 없음 | 해당 사항 없음 | 스타일 참조로 사용할 이미지 최대 3개 |

### Python

```
from google import genai
from google.genai import types
from PIL import Image

prompt = "An office group photo of these people, they are making funny faces."
aspect_ratio = "5:4" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "2K" # "512", "1K", "2K", "4K"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[
        prompt,
        Image.open('person1.png'),
        Image.open('person2.png'),
        Image.open('person3.png'),
        Image.open('person4.png'),
        Image.open('person5.png'),
    ],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        response_format={"image": {aspect_ratio: aspect_ratio,                 image_size: resolution}},
    )
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("office.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt =
      'An office group photo of these people, they are making funny faces.';
  const aspectRatio = '5:4';
  const resolution = '2K';

const contents = [
  { text: prompt },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile1,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile2,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile3,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile4,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile5,
    },
  }
];

const response = await ai.models.generateContent({
    model: 'gemini-3.1-flash-image',
    contents: contents,
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      responseFormat: {
    image: {
        aspectRatio: aspectRatio,
        imageSize: resolution,
      }
  },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
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
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Text, genai.Image},
        ImageConfig: &pb.ImageConfig{
            AspectRatio: "5:4",
            ImageSize:   "2K",
        },
    }

    img1, err := os.ReadFile("person1.png")
    if err != nil { log.Fatal(err) }
    img2, err := os.ReadFile("person2.png")
    if err != nil { log.Fatal(err) }
    img3, err := os.ReadFile("person3.png")
    if err != nil { log.Fatal(err) }
    img4, err := os.ReadFile("person4.png")
    if err != nil { log.Fatal(err) }
    img5, err := os.ReadFile("person5.png")
    if err != nil { log.Fatal(err) }

    parts := []genai.Part{
        genai.Text("An office group photo of these people, they are making funny faces."),
        genai.ImageData{MIMEType: "image/png", Data: img1},
        genai.ImageData{MIMEType: "image/png", Data: img2},
        genai.ImageData{MIMEType: "image/png", Data: img3},
        genai.ImageData{MIMEType: "image/png", Data: img4},
        genai.ImageData{MIMEType: "image/png", Data: img5},
    }

    resp, err := model.GenerateContent(ctx, parts...)
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("office.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class GroupPhoto {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .imageConfig(ImageConfig.builder()
              .aspectRatio("5:4")
              .imageSize("2K")
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          Content.fromParts(
              Part.fromText("An office group photo of these people, they are making funny faces."),
              Part.fromBytes(Files.readAllBytes(Path.of("person1.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person2.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person3.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person4.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person5.png")), "image/png")
          ), config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("office.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class GroupPhoto {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "An office group photo of these people, they are making funny faces." },
            new Part { FileData = new FileData { FileUri = "file:///person1.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person2.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person3.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person4.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person5.png" } }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "5:4",
                ImageSize = "2K"
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("office.png", imageBytes);
                Console.WriteLine("Image saved as office.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d "{
      \"contents\": [{
        \"parts\":[
            {\"text\": \"An office group photo of these people, they are making funny faces.\"},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_1>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_2>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_3>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_4>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_5>\"}}
        ]
      }],
      \"generationConfig\": {
        \"responseModalities\": [\"TEXT\", \"IMAGE\"],
        \"responseFormat\": {
        \"image\": {
          \"aspectRatio\": \"5:4\",
          \"imageSize\": \"2K\"
        }
      }
      }
    }"
```

![AI 생성 사무실 그룹 사진](https://ai.google.dev/static/gemini-api/docs/images/office-group-photo.jpeg?hl=ko)

AI 생성 사무실 단체 사진

### Google 검색을 사용하는 그라운딩

[Google 검색 도구](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)를 사용하여 날씨 예보, 주식 차트, 최근 이벤트와 같은 실시간 정보를 기반으로 이미지를 생성합니다.

이미지 생성과 함께 Google 검색으로 그라운딩을 사용하는 경우 이미지 기반 검색 결과는 생성 모델에 전달되지 않으며 대답에서 제외됩니다 ([이미지용 Google 검색으로 그라운딩](#image-search) 참고).

### Python

```
from google import genai
prompt = "Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day"
aspect_ratio = "16:9" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'],
        response_format={"image": {aspect_ratio: aspect_ratio,}},
        tools=[{"google_search": {}}]
    )
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("weather.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt = 'Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day';
  const aspectRatio = '16:9';
  const resolution = '2K';

const response = await ai.models.generateContent({
    model: 'gemini-3.1-flash-image',
    contents: prompt,
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      responseFormat: {
    image: {
        aspectRatio: aspectRatio,
        imageSize: resolution,
      }
  },
    tools: [{ googleSearch: {} }]
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
  }

}

main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class SearchGrounding {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .imageConfig(ImageConfig.builder()
              .aspectRatio("16:9")
              .build())
          .tools(Tool.builder()
              .googleSearch(GoogleSearch.builder().build())
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image", """
              Visualize the current weather forecast for the next 5 days
              in San Francisco as a clean, modern weather chart.
              Add a visual on what I should wear each day
              """,
          config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("weather.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class SearchGrounding {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day" }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "16:9"
            },
            Tools = new List<Tool> { new Tool { GoogleSearch = new GoogleSearch() } }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("weather.png", imageBytes);
                Console.WriteLine("Image saved as weather.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day"}]}],
    "tools": [{"google_search": {}}],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "responseFormat": {
    "image": {"aspectRatio": "16:9"}
  }
    }
  }'
```

![샌프란시스코의 5일간 날씨를 보여주는 AI 생성 차트](https://ai.google.dev/static/gemini-api/docs/images/weather-forecast.png?hl=ko)

샌프란시스코의 5일간 날씨를 보여주는 AI 생성 차트

응답에는 다음 필수 필드가 포함된 `groundingMetadata`이 포함됩니다.

- **`searchEntryPoint`**: 필수 검색어를 렌더링하는 HTML과 CSS가 포함되어 있습니다.
- **`groundingChunks`**: 생성된 이미지를 그라운딩하는 데 사용된 상위 3개 웹 소스를 반환합니다.

### 이미지용 Google 검색을 사용한 그라운딩 (3.1 Flash)

이미지에 대한 Google 검색을 사용한 그라운딩을 사용하면 모델이 Google 검색을 통해 검색된 웹 이미지를 이미지 생성의 시각적 컨텍스트로 사용할 수 있습니다. 이미지 검색은 기존의 Google 검색을 사용한 그라운딩 도구 내의 새로운 검색 유형으로, 표준 [웹 검색](#use-with-grounding)과 함께 작동합니다.

이미지 검색을 사용 설정하려면 API 요청에서 `googleSearch` 도구를 구성하고 `searchTypes` 객체 내에서 `imageSearch`을 지정합니다. 이미지 검색은 독립적으로 또는 웹 검색과 함께 사용할 수 있습니다.

이미지의 Google 검색을 통한 그라운딩은 사람을 검색하는 데 사용할 수 없습니다.

### Python

```
from google import genai
prompt = "A detailed painting of a Timareta butterfly resting on a flower"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        tools=[
            types.Tool(google_search=types.GoogleSearch(
                search_types=types.SearchTypes(
                    web_search=types.WebSearch(),
                    image_search=types.ImageSearch()
                )
            ))
        ]
    )
)

# Display grounding sources if available
if response.candidates and response.candidates[0].grounding_metadata and response.candidates[0].grounding_metadata.search_entry_point:
    display(HTML(response.candidates[0].grounding_metadata.search_entry_point.rendered_content))
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt = "A detailed painting of a Timareta butterfly resting on a flower";

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
    config: {
      responseModalities: ["IMAGE"],
      tools: [
        {
          googleSearch: {
            searchTypes: {
              webSearch: {},
              imageSearch: {}
            }
          }
        }
      ]
    }
  });

  // Display grounding sources if available
  if (response.candidates && response.candidates[0].groundingMetadata && response.candidates[0].groundingMetadata.searchEntryPoint) {
      console.log(response.candidates[0].groundingMetadata.searchEntryPoint.renderedContent);
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
  "log"

  "google.golang.org/genai"
  pb "google.golang.org/genai/schema"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
    log.Fatal(err)
  }
  defer client.Close()

  model := client.GenerativeModel("gemini-3.1-flash-image")
  model.Tools = []*pb.Tool{
    {
      GoogleSearch: &pb.GoogleSearch{
        SearchTypes: &pb.SearchTypes{
          WebSearch:   &pb.WebSearch{},
          ImageSearch: &pb.ImageSearch{},
        },
      },
    },
  }
  model.GenerationConfig = &pb.GenerationConfig{
    ResponseModalities: []pb.ResponseModality{genai.Image},
  }

  prompt := "A detailed painting of a Timareta butterfly resting on a flower"
  resp, err := model.GenerateContent(ctx, genai.Text(prompt))
  if err != nil {
    log.Fatal(err)
  }

  if resp.Candidates[0].GroundingMetadata != nil && resp.Candidates[0].GroundingMetadata.SearchEntryPoint != nil {
    fmt.Println(resp.Candidates[0].GroundingMetadata.SearchEntryPoint.RenderedContent)
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageSearch;
import com.google.genai.types.SearchTypes;
import com.google.genai.types.Tool;
import com.google.genai.types.WebSearch;

import java.io.IOException;

public class ImageSearchGrounding {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("IMAGE")
          .tools(Tool.builder()
              .googleSearch(GoogleSearch.builder()
                  .searchTypes(SearchTypes.builder()
                      .webSearch(WebSearch.builder().build())
                      .imageSearch(ImageSearch.builder().build())
                      .build())
                  .build())
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          "A detailed painting of a Timareta butterfly resting on a flower",
          config);

      if (response.candidates().isPresent() && !response.candidates().get().isEmpty()) {
        var candidate = response.candidates().get().get(0);
        if (candidate.groundingMetadata().isPresent() && candidate.groundingMetadata().get().searchEntryPoint().isPresent()) {
          System.out.println(candidate.groundingMetadata().get().searchEntryPoint().get().renderedContent().orElse(""));
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public class ImageSearchGrounding {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "A detailed painting of a Timareta butterfly resting on a flower" }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "IMAGE" },
            Tools = new List<Tool>
            {
                new Tool
                {
                    GoogleSearch = new GoogleSearch
                    {
                        SearchTypes = new SearchTypes
                        {
                            WebSearch = new WebSearch(),
                            ImageSearch = new ImageSearch()
                        }
                    }
                }
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        if (candidate.GroundingMetadata != null && candidate.GroundingMetadata.SearchEntryPoint != null) {
            Console.WriteLine(candidate.GroundingMetadata.SearchEntryPoint.RenderedContent);
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "A detailed painting of a Timareta butterfly resting on a flower"}]}],
    "tools": [{"google_search": {"searchTypes": {"webSearch": {}, "imageSearch": {}}}}],
    "generationConfig": {
      "responseModalities": ["IMAGE"]
    }
  }'
```

**디스플레이 요구사항**

Google 검색을 사용한 그라운딩 내에서 이미지 검색을 사용하는 경우 다음 조건을 준수해야 합니다.

- **소스 저작자 표시**: 사용자가 링크로 인식할 수 있는 방식으로 소스 이미지가 포함된 웹페이지 (이미지 파일 자체가 아닌 '포함 페이지')로 연결되는 링크를 제공해야 합니다.
- **직접 탐색**: 소스 이미지를 표시하는 경우 소스 이미지에서 소스 웹페이지로 연결되는 직접적인 단일 클릭 경로를 제공해야 합니다. 다중 클릭 경로 또는 중간 이미지 뷰어 사용을 포함하되 이에 국한되지 않고 최종 사용자의 소스 웹페이지 액세스를 지연하거나 추상화하는 기타 구현은 허용되지 않습니다.

**응답**

이미지 검색을 사용하는 그라운딩된 응답의 경우 API는 출력을 검증된 소스에 연결하는 명확한 저작자 표시와 메타데이터를 제공합니다. `groundingMetadata` 객체의 주요 필드는 다음과 같습니다.

- **`imageSearchQueries`**: 모델이 시각적 컨텍스트 (이미지 검색)에 사용하는 구체적인 질문입니다.
- **`groundingChunks`**: 가져온 결과의 소스 정보를 포함합니다.
  이미지 소스의 경우 새 이미지 청크 유형을 사용하여 리디렉션 URL로 반환됩니다. 이 청크에는 다음이 포함됩니다.

  - **`uri`**: 기여 분석을 위한 웹페이지 URL (방문 페이지)입니다.
  - **`image_uri`**: 직접 이미지 URL입니다.
- **`groundingSupports`**: 생성된 콘텐츠를 청크의 관련 인용 소스에 연결하는 구체적인 매핑을 제공합니다.
- **`searchEntryPoint`**: 검색 추천을 렌더링하기 위한 규정을 준수하는 HTML 및 CSS가 포함된 'Google 검색' 칩이 포함됩니다.

### 동영상 이미지 변환 생성 (3.1 Flash)

동영상-이미지 생성 기능을 사용하면 동영상의 컨텍스트를 멀티모달 참조로 사용하여 새로운 이미지를 생성할 수 있습니다. 이 기능은 고품질 동영상 썸네일, 영화 포스터, 요약 인포그래픽 또는 동영상 장면에서 영감을 받은 새로운 아트워크를 만드는 데 유용합니다.

생성 중에 모델은 컨텍스트의 동영상 프레임 (최대 모델의 입력 토큰 한도인 131,072개 토큰)을 분석하여 시각적 테마와 주요 이벤트를 추출한 다음, 텍스트 프롬프트와 함께 사용하여 출력 이미지를 합성합니다.

API 요청에 공개 [YouTube URL](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko#youtube)을 직접 전달하거나 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 사용하여 로컬 동영상 파일을 업로드할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Pass a public YouTube video URL as part of the contents
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[
        types.Part(
          file_data=types.FileData(file_uri="https://www.youtube.com/watch?v=UTdfxFyOQTI"),
          video_metadata=types.VideoMetadata(fps=0.5)
        ),
        "Generate a poster image that captures the key themes of this video."
    ],
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"]
    )
)

# Save the generated image part
for part in response.parts:
    if part.inline_data is not None:
        image = part.as_image()
        image.save("video_poster.png")
        print("Image saved as video_poster.png")
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
  const ai = new GoogleGenAI({});

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: [
      {
        fileData: {
          fileUri: "https://www.youtube.com/watch?v=UTdfxFyOQTI",
        },
        videoMetadata: {
          fps: 0.5
        }
      },
      { text: "Generate a poster image that captures the key themes of this video." }
    ],
    config: {
      responseModalities: ["TEXT", "IMAGE"]
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("video_poster.png", buffer);
      console.log("Image saved as video_poster.png");
    }
  }
}

main();
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    videoPart := genai.NewPartFromURI("https://www.youtube.com/watch?v=UTdfxFyOQTI", "video/mp4")
    videoPart.VideoMetadata = &genai.VideoMetadata{FPS: genai.Ptr(0.5)}

    parts := []*genai.Part{
        videoPart,
        genai.NewPartFromText("Generate a poster image that captures the key themes of this video."),
    }

    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.1-flash-image",
        contents,
        &genai.GenerateContentConfig{
            ResponseModalities: []string{"TEXT", "IMAGE"},
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range result.Candidates[0].Content.Parts {
        if part.InlineData != nil {
            imageBytes := part.InlineData.Data
            _ = os.WriteFile("video_poster.png", imageBytes, 0644)
            log.Println("Image saved as video_poster.png")
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.FileData;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.VideoMetadata;
import com.google.common.collect.ImmutableList;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class VideoToImage {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      Part videoPart = Part.builder()
          .fileData(FileData.builder()
              .fileUri("https://www.youtube.com/watch?v=UTdfxFyOQTI")
              .build())
          .videoMetadata(VideoMetadata.builder()
              .fps(0.5)
              .build())
          .build();

      Part textPart = Part.builder()
          .text("Generate a poster image that captures the key themes of this video.")
          .build();

      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          Content.builder()
              .role("user")
              .parts(ImmutableList.of(videoPart, textPart))
              .build(),
          config);

      for (Part part : response.parts()) {
        if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("video_poster.png"), blob.data().get());
            System.out.println("Image saved as video_poster.png");
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using Google.GenAI.Types;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class VideoToImage {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part
            {
                FileData = new FileData { FileUri = "https://www.youtube.com/watch?v=UTdfxFyOQTI" },
                VideoMetadata = new VideoMetadata { Fps = 0.5 }
            },
            new Part { Text = "Generate a poster image that captures the key themes of this video." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("video_poster.png", imageBytes);
                Console.WriteLine("Image saved as video_poster.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "https://www.youtube.com/watch?v=UTdfxFyOQTI"
          },
          "video_metadata": {
            "fps": 0.5
          }
        },
        {"text": "Generate a poster image that captures the key themes of this video."}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"]
    }
  }'
```

![YouTube 동영상에서 생성된 AI 인포그래픽](https://ai.google.dev/static/gemini-api/docs/images/youtube_infographics.png?hl=ko)

YouTube 동영상에서 생성된 AI 인포그래픽

### 최대 4K 해상도로 이미지 생성

Gemini 3 이미지 모델은 기본적으로 1K 이미지를 생성하지만 2K, 4K, 512 (0.5K) (Gemini 3.1 Flash Image만 해당) 이미지도 출력할 수 있습니다. 고해상도 애셋을 생성하려면 `generation_config`에서 `image_size`을 지정합니다.

대문자 'K'를 사용해야 합니다(예: 1K, 2K, 4K). `512` 값에 'K' 접미사가 사용되지 않습니다. 소문자 매개변수 (예: 1k)는 거부됩니다.

### Python

```
from google import genai
from google.genai import types

prompt = "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English."
aspect_ratio = "1:1" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "1K" # "512", "1K", "2K", "4K"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        response_format={"image": {aspect_ratio: aspect_ratio,                 image_size: resolution}},
    )
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("butterfly.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt =
      'Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English.';
  const aspectRatio = '1:1';
  const resolution = '1K';

  const response = await ai.models.generateContent({
    model: 'gemini-3.1-flash-image',
    contents: prompt,
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      responseFormat: {
    image: {
        aspectRatio: aspectRatio,
        imageSize: resolution,
      }
  },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
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
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Text, genai.Image},
        ImageConfig: &pb.ImageConfig{
            AspectRatio: "1:1",
            ImageSize:   "1K",
        },
    }

    prompt := "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English."
    resp, err := model.GenerateContent(ctx, genai.Text(prompt))
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("butterfly.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class HiRes {
    public static void main(String[] args) throws IOException {

      try (Client client = new Client()) {
        GenerateContentConfig config = GenerateContentConfig.builder()
            .responseModalities("TEXT", "IMAGE")
            .imageConfig(ImageConfig.builder()
                .aspectRatio("16:9")
                .imageSize("4K")
                .build())
            .build();

        GenerateContentResponse response = client.models.generateContent(
            "gemini-3.1-flash-image", """
              Da Vinci style anatomical sketch of a dissected Monarch butterfly.
              Detailed drawings of the head, wings, and legs on textured
              parchment with notes in English.
              """,
            config);

        for (Part part : response.parts()) {
          if (part.text().isPresent()) {
            System.out.println(part.text().get());
          } else if (part.inlineData().isPresent()) {
            var blob = part.inlineData().get();
            if (blob.data().isPresent()) {
              Files.write(Paths.get("butterfly.png"), blob.data().get());
            }
          }
        }
      }
    }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class HiRes {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "1:1",
                ImageSize = "1K"
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("butterfly.png", imageBytes);
                Console.WriteLine("Image saved as butterfly.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English."}]}],
    "tools": [{"google_search": {}}],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "responseFormat": {
    "image": {"aspectRatio": "1:1", "imageSize": "1K"}
  }
    }
  }'
```

다음은 이 프롬프트로 생성된 이미지의 예입니다.

![해부된 제왕나비의 다빈치 스타일 AI 생성 해부학적 스케치](https://ai.google.dev/static/gemini-api/docs/images/gemini3-4k-image.png?hl=ko)

해부된 제왕나비의 다빈치 스타일 AI 생성 해부학적 스케치

### 사고 과정

Gemini 3 이미지 모델은 복잡한 프롬프트에 추론 프로세스 ('사고')를 사용하는 사고 모델입니다. 이 기능은 기본적으로 사용 설정되어 있으며 API에서 사용 중지할 수 없습니다. 사고 과정에 대해 자세히 알아보려면 [Gemini 사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko) 가이드를 참고하세요.

모델은 구도와 논리를 테스트하기 위해 최대 2개의 임시 이미지를 생성합니다. Thinking 내의 마지막 이미지도 최종 렌더링된 이미지입니다.

최종 이미지가 생성된 이유를 확인할 수 있습니다.

### Python

```
for part in response.parts:
    if part.thought:
        if part.text:
            print(part.text)
        elif image:= part.as_image():
            image.show()
```

### JavaScript

```
for (const part of response.candidates[0].content.parts) {
  if (part.thought) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, 'base64');
      fs.writeFileSync('image.png', buffer);
      console.log('Image saved as image.png');
    }
  }
}
```

### 자바

```
for (Part part : response.parts()) {
  if (part.thought().orElse(false)) {
    if (part.text().isPresent()) {
      System.out.println(part.text().get());
    } else if (part.inlineData().isPresent()) {
      var blob = part.inlineData().get();
      if (blob.data().isPresent()) {
        Files.write(Paths.get("image.png"), blob.data().get());
        System.out.println("Image saved as image.png");
      }
    }
  }
}
```

### C#

```
foreach (var candidate in response.Candidates) {
    foreach (var part in candidate.Content.Parts) {
        if (part.Thought) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("image.png", imageBytes);
                Console.WriteLine("Image saved as image.png");
            }
        }
    }
}
```

#### 사고 수준 제어

Gemini 3.1 Flash Image 및 Gemini 3.1 Flash Lite Image를 사용하면 모델이 품질과 지연 시간의 균형을 맞추기 위해 사용하는 사고량을 제어할 수 있습니다. 기본 `thinkingLevel`은 `minimal`이고 지원되는 수준은 `minimal` 및 `high`입니다. `thinkingLevel`을 `minimal`로 설정하면 지연 시간이 가장 짧은 응답이 제공됩니다. 최소한의 사고는 모델이 전혀 사고하지 않는다는 의미가 아닙니다.

`includeThoughts` 불리언을 추가하여 모델에서 생성된 생각이 대답에 반환되는지 아니면 숨겨진 상태로 유지되는지 확인할 수 있습니다.

### Python

```
from google import genai

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents="A futuristic city built inside a giant glass bottle floating in space",
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        thinking_config=types.ThinkingConfig(
            thinking_level="High",
            include_thoughts=True
        ),
    )
)

for part in response.parts:
    if part.thought: # Skip outputting thoughts
      continue
    if part.text:
      display(Markdown(part.text))
    elif image:= part.as_image():
      image.show()
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: "A futuristic city built inside a giant glass bottle floating in space",
    config: {
      responseModalities: ["IMAGE"],
      thinkingConfig: {
        thinkingLevel: "High",
        includeThoughts: true
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.thought) { // Skip outputting thoughts
      continue;
    }
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
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
    "log"
    "os"

    "google.golang.org/genai"
    pb "google.golang.org/genai/schema"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Image},
        ThinkingConfig: &pb.ThinkingConfig{
            ThinkingLevel:   "High",
            IncludeThoughts: true,
        },
    }

    prompt := "A futuristic city built inside a giant glass bottle floating in space"
    resp, err := model.GenerateContent(ctx, genai.Text(prompt))
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if part.Thought { // Skip outputting thoughts
            continue
        }
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("image.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.ThinkingConfig;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class ThinkingLevels {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("IMAGE")
          .thinkingConfig(ThinkingConfig.builder()
              .thinkingLevel("High")
              .includeThoughts(true)
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          "A futuristic city built inside a giant glass bottle floating in space",
          config);

      for (Part part : response.parts()) {
        if (part.thought().orElse(false)) {
          // Skip outputting thoughts
          continue;
        }
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("image.png"), blob.data().get());
            System.out.println("Image saved as image.png");
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class ThinkingLevels {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "A futuristic city built inside a giant glass bottle floating in space" }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "IMAGE" },
            ThinkingConfig = new ThinkingConfig
            {
                ThinkingLevel = "High",
                IncludeThoughts = true
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Thought) {
                // Skip outputting thoughts
                continue;
            }
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("image.png", imageBytes);
                Console.WriteLine("Image saved as image.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "A futuristic city built inside a giant glass bottle floating in space"}]}],
    "generationConfig": {
      "responseModalities": ["IMAGE"],
      "thinkingConfig": {
        "thinkingLevel": "High",
        "includeThoughts": true
      }
    }
  }'
```

`includeThoughts`이 `true` 또는 `false`로 설정되었는지와 관계없이 생각 토큰은 청구됩니다. [생각 과정](#thinking-process)은 과정을 보든 보지 않든 기본적으로 항상 발생하기 때문입니다.

#### 생각 서명

생각 서명은 모델의 내부 사고 과정을 암호화한 표현으로, 멀티턴 상호작용에서 추론 컨텍스트를 유지하는 데 사용됩니다. 모든 응답에는 `thought_signature` 필드가 포함됩니다. 일반적으로 모델 응답에서 생각 서명을 수신하면 다음 턴에서 대화 기록을 보낼 때 수신한 그대로 다시 전달해야 합니다. 생각 서명을 순환하지 않으면 대답이 실패할 수 있습니다. 전반적인 서명에 관한 자세한 설명은 [사고 서명](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ko) 문서를 참고하세요.

생각 서명의 작동 방식은 다음과 같습니다.

- 대답에 포함된 이미지 `mimetype`이 있는 모든 `inline_data` 부분에는 서명이 있어야 합니다.
- 생각 바로 뒤에 (이미지 전) 시작 부분에 텍스트 부분이 있는 경우 첫 번째 텍스트 부분에도 서명이 있어야 합니다.
- 이미지(`mimetype`)가 포함된 `inline_data` 부분이 생각의 일부인 경우 서명이 없습니다.

다음 코드는 생각 서명이 포함된 위치의 예를 보여줍니다.

```
[
  {
    "inline_data": {
      "data": "<base64_image_data_0>",
      "mime_type": "image/png"
    },
    "thought": true // Thoughts don't have signatures
  },
  {
    "inline_data": {
      "data": "<base64_image_data_1>",
      "mime_type": "image/png"
    },
    "thought": true // Thoughts don't have signatures
  },
  {
    "inline_data": {
      "data": "<base64_image_data_2>",
      "mime_type": "image/png"
    },
    "thought": true // Thoughts don't have signatures
  },
  {
    "text": "Here is a step-by-step guide to baking macarons, presented in three separate images.\n\n### Step 1: Piping the Batter\n\nThe first step after making your macaron batter is to pipe it onto a baking sheet. This requires a steady hand to create uniform circles.\n\n",
    "thought_signature": "<Signature_A>" // The first non-thought part always has a signature
  },
  {
    "inline_data": {
      "data": "<base64_image_data_3>",
      "mime_type": "image/png"
    },
    "thought_signature": "<Signature_B>" // All image parts have a signatures
  },
  {
    "text": "\n\n### Step 2: Baking and Developing Feet\n\nOnce piped, the macarons are baked in the oven. A key sign of a successful bake is the development of \"feet\"—the ruffled edge at the base of each macaron shell.\n\n"
    // Follow-up text parts don't have signatures
  },
  {
    "inline_data": {
      "data": "<base64_image_data_4>",
      "mime_type": "image/png"
    },
    "thought_signature": "<Signature_C>" // All image parts have a signatures
  },
  {
    "text": "\n\n### Step 3: Assembling the Macaron\n\nThe final step is to pair the cooled macaron shells by size and sandwich them together with your desired filling, creating the classic macaron dessert.\n\n"
  },
  {
    "inline_data": {
      "data": "<base64_image_data_5>",
      "mime_type": "image/png"
    },
    "thought_signature": "<Signature_D>" // All image parts have a signatures
  }
]
```

## 기타 이미지 생성 모드

Gemini는 프롬프트 구조와 컨텍스트에 따라 다음과 같은 다른 이미지 상호작용 모드를 지원합니다.

- **텍스트 이미지 변환 및 텍스트(인터리브 처리):** 관련 텍스트와 함께 이미지를 출력합니다.
  - 프롬프트 예시: '파에야에 관한 그림이 있는 레시피를 생성해 줘.'
- **이미지 및 텍스트 이미지 변환 및 텍스트(인터리브 처리)**: 입력 이미지와 텍스트를 사용하여 관련 이미지와 텍스트를 새로 만듭니다.
  - 프롬프트 예시: (가구가 완비된 방의 이미지 포함) "내 공간에 어떤 색상의 소파가 어울릴까? 이미지를 업데이트해 줘."

## 일괄적으로 이미지 생성

이미지를 많이 생성해야 하는 경우 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)를 사용하면 됩니다. 최대 24시간의 처리 시간을 감수하는 대신 더 높은 [속도 제한](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko)을 이용할 수 있습니다.

[Batch API 이미지 생성 문서](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko#image-generation)와 [쿠크북](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=ko)에서 Batch API 이미지 예시와 코드를 확인하세요.

## 프롬프트 가이드 및 전략

이미지 생성의 기본 원칙은 다음과 같습니다.

> **장면을 설명하고 키워드만 나열하지 마세요.**
> 이 모델의 핵심 강점은 깊이 있는 언어 이해입니다. 설명적인 단락은 연결되지 않은 단어 목록보다 더 나은 일관된 이미지를 생성하는 경우가 거의 항상 있습니다.

### 이미지 생성 프롬프트

다음 전략을 사용하면 원하는 이미지를 정확하게 생성하는 효과적인 프롬프트를 만들 수 있습니다.

#### 사진

사실적인 이미지를 원한다면 사진 용어를 사용하세요. 카메라 각도, 렌즈 유형, 조명, 세부사항을 언급하여 모델이 사실적인 결과를 생성하도록 안내하세요.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 깊은 주름과 따뜻하고 의미심장한 미소를 지은 일본인 도예가 노인의 클로즈업 사진 갓 유약을 바른 찻사발을 주의 깊게 살펴보고 있습니다. 배경은 햇빛이 가득한 그의 소박한 작업장입니다. 창문을 통해 비추는 부드러운 골든아워 빛이 점토의 섬세한 질감을 강조하며 장면을 비춥니다. 85mm 인물 사진 렌즈로 촬영하여 부드럽고 흐린 배경 (빛망울 효과)을 만들어 줘. 전반적인 분위기는 차분하고 능숙한 느낌이야. 세로 방향입니다. | 고령의 일본 도예가 |

#### 스타일이 지정된 삽화 및 스티커

스티커, 아이콘 또는 애셋을 만들려면 스타일을 명시하고 흰색 배경을 요청하세요.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 작은 대나무 모자를 쓰고 있는 행복한 레서판다의 카와이 스타일 스티커 녹색 대나무 잎을 먹고 있습니다. 디자인에는 굵고 깔끔한 윤곽선, 단순한 셀 셰이딩, 생생한 색상 팔레트가 사용됩니다. 배경은 흰색이어야 합니다. | 귀여운 레서판다 스티커 |

#### 이미지의 정확한 텍스트

Gemini는 텍스트 렌더링에 탁월합니다. 텍스트, 글꼴 스타일(설명), 전체 디자인을 명확하게 설명하세요. Gemini 3 Pro Image를 사용하여 전문적인 애셋을 제작하세요.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 'The Daily Grind'라는 커피숍의 현대적이고 미니멀한 로고를 만들어 줘. 텍스트는 깔끔하고 굵은 산세리프 글꼴이어야 합니다. 색 구성표가 흑백입니다. 로고를 원 안에 넣습니다. 커피 원두를 영리하게 사용하세요. | 커피숍 로고 |

#### 제품 모형 및 상업용 사진

전자상거래, 광고 또는 브랜딩을 위한 깔끔하고 전문적인 제품 사진을 만드는 데 적합합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 광택이 나는 콘크리트 표면에 놓인 무광택 검은색의 미니멀한 세라믹 커피 머그잔의 고해상도 스튜디오 조명 제품 사진입니다. 조명은 부드럽고 확산된 하이라이트를 만들고 강한 그림자를 제거하도록 설계된 3점 소프트박스 설정입니다. 카메라 각도는 깔끔한 라인을 보여주기 위해 약간 높은 45도 각도로 촬영되었습니다. 커피에서 피어오르는 김에 초점을 맞춘 매우 사실적인 이미지입니다. 정사각형 이미지 | 세라믹 커피 머그잔 제품 사진 |

#### 미니멀리스트 및 네거티브 스페이스 디자인

텍스트가 오버레이되는 웹사이트, 프레젠테이션 또는 마케팅 자료의 배경을 만드는 데 적합합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 프레임 오른쪽 하단에 섬세한 빨간색 단풍잎 하나가 배치된 미니멀한 구성입니다. 배경은 광활하고 비어 있는 미색 캔버스로, 텍스트를 위한 상당한 여백을 만듭니다. 왼쪽 상단에서 부드럽게 확산되는 조명 정사각형 이미지 | 빨간 단풍잎이 있는 미니멀한 디자인 |

#### 연속적인 아트 (만화 패널 / 스토리보드)

캐릭터 일관성 및 장면 설명을 기반으로 시각적 스토리텔링을 위한 패널을 만듭니다. 텍스트의 정확성과 스토리텔링 능력을 위해 이러한 프롬프트는 Gemini 3.1 Pro 및 Gemini 3.1 Flash Image와 함께 사용하는 것이 가장 좋습니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  흰색 안경을 쓴 남자   입력 이미지   **프롬프트:** 거친 누아르 아트 스타일로 대비가 높은 흑백 잉크를 사용해 3컷 만화를 만들어 줘. 캐릭터를 재미있는 장면 속에 넣어 줘. | 음울한 느와르 만화 패널 |

#### Google 검색을 사용하는 그라운딩

Google 검색을 사용하여 최근 또는 실시간 정보를 기반으로 이미지를 생성합니다.
이는 뉴스, 날씨, 기타 시간에 민감한 주제에 유용합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 어젯밤 챔피언스 리그에서 펼쳐진 아스널 경기의 간단하지만 세련된 그래픽을 만들어 줘. | 아스널 축구 점수 그래픽 |

### 이미지 수정 프롬프트

이 예시에서는 수정, 구성, 스타일 전송을 위해 텍스트 프롬프트와 함께 이미지를 제공하는 방법을 보여줍니다.

#### 요소 추가 및 삭제

이미지를 제공하고 변경사항을 설명하세요. 모델은 원본 이미지의 스타일, 조명, 원근법과 일치합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  솜털이 보송보송한 생강색 고양이의 사실적인 사진...   입력 이미지   **프롬프트:** 제공된 내 고양이 이미지를 사용하여 머리에 작은 니트 마법사 모자를 추가해 줘. 편안하게 앉아 있는 것처럼 보이게 하고 사진의 부드러운 조명과 일치하도록 합니다. | 마법사 모자를 쓴 고양이 |

#### 인페인팅 (시맨틱 마스킹)

대화형으로 '마스크'를 정의하여 이미지의 특정 부분을 수정하고 나머지는 그대로 둡니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  조명이 잘 들어오는 현대적인 거실의 와이드 샷...   입력 이미지   **프롬프트:** 제공된 거실 이미지를 사용하여 파란색 소파만 빈티지한 갈색 가죽 체스터필드 소파로 변경해 줘. 소파의 베개와 조명을 비롯한 나머지 방은 변경하지 않습니다. | 갈색 가죽 소파가 있는 거실 |

#### 스타일 전이

이미지를 제공하고 모델에 다른 예술적 스타일로 콘텐츠를 재현해 달라고 요청합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  번화한 도시 거리의 포토리얼리스틱 고해상도 사진...   입력 이미지   **프롬프트:** 제공된 밤의 현대 도시 거리 사진을 빈센트 반 고흐의 '별이 빛나는 밤'의 예술적 스타일로 변환해 줘. 건물과 자동차의 원래 구성을 유지하되, 회전하는 임파스토 붓놀림과 깊은 파란색과 밝은 노란색의 극적인 팔레트로 모든 요소를 렌더링합니다. | 별이 빛나는 밤 스타일의 도시 거리 |

#### 고급 합성: 여러 이미지 결합

여러 이미지를 컨텍스트로 제공하여 새로운 합성 장면을 만듭니다. 제품 모형이나 창의적인 콜라주에 적합합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  파란색 꽃무늬 여름 드레스를 전문적으로 촬영한 사진...   입력 1: 드레스   머리를 묶은 여성의 전신 사진...   입력 2: 모델   **프롬프트:** 전문적인 이커머스 패션 사진을 만들어 줘. 첫 번째 이미지의 파란색 꽃무늬 드레스를 가져와 두 번째 이미지의 여성이 입도록 해 줘. 드레스를 입은 여성의 사실적인 전신 이미지를 생성해 줘. 조명과 그림자는 야외 환경에 맞게 조정해 줘. | 패션 전자상거래 샷 |

#### 충실도 높은 세부정보 보존

수정 중에 얼굴이나 로고와 같은 중요한 세부정보가 유지되도록 하려면 수정 요청과 함께 세부정보를 자세히 설명하세요.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  갈색 머리에 파란 눈을 가진 여성의 전문적인 프로필 사진...   입력 1: 여성   'G'와 'A' 글자가 있는 심플하고 모던한 로고...   입력 2: 로고   **프롬프트:** 갈색 머리, 파란 눈, 무표정한 여자의 첫 번째 이미지를 가져와 줘. 두 번째 이미지의 로고를 검은색 티셔츠에 추가해 줘. 여성의 얼굴과 특징은 완전히 변경되지 않아야 합니다. 로고는 셔츠의 주름을 따라 천에 자연스럽게 인쇄된 것처럼 보여야 합니다. | 티셔츠에 로고가 있는 여성 |

#### 생동감 불어넣기

러프 스케치나 그림을 업로드하고 모델에 완성된 이미지로 다듬어 달라고 요청하세요.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  자동차 스케치   자동차의 대략적인 스케치   **프롬프트:** 이 대략적인 미래형 자동차 연필 스케치를 쇼룸에 있는 완성된 컨셉 자동차의 세련된 사진으로 바꿔 줘. 스케치의 세련된 선과 로우 프로필은 유지하되 메탈릭 블루 페인트와 네온 림 조명을 추가합니다. | 컨셉트카의 세련된 사진 |

#### 캐릭터 일관성: 360도 뷰

다양한 각도를 반복적으로 요청하여 캐릭터의 360도 뷰를 생성할 수 있습니다. 최상의 결과를 얻으려면 일관성을 유지하기 위해 이전에 생성된 이미지를 후속 프롬프트에 포함하세요. 복잡한 포즈의 경우 원하는 포즈의 참고 이미지를 포함합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지:**  흰색 안경을 쓴 남자의 원본 입력   원본 이미지   **프롬프트:** 흰색 배경에 오른쪽을 바라보는 옆모습의 이 남성 스튜디오 인물 사진 | 오른쪽을 바라보는 흰색 안경을 쓴 남자의 출력   흰색 안경을 쓰고 오른쪽을 바라보는 남성   앞을 바라보는 흰색 안경을 쓴 남성의 출력   흰색 안경을 쓰고 앞을 바라보는 남성 |

### 권장사항

결과를 좋음에서 우수함으로 끌어올리려면 이러한 전문적인 전략을 워크플로에 통합하세요.

- **매우 구체적으로 작성:** 세부정보를 많이 제공할수록 더 나은 결과를 얻을 수 있습니다. '판타지 갑옷' 대신 '은박 무늬가 새겨진 화려한 엘프 판금 갑옷, 높은 칼라와 매 날개 모양의 어깨 보호대를 갖추고 있다'라고 설명해 보세요.
- **컨텍스트와 의도 제공:** 이미지의 *목적*을 설명합니다. 컨텍스트에 대한 모델의 이해가 최종 출력에 영향을 미칩니다. 예를 들어 '고급 미니멀리즘 스킨케어 브랜드를 위한 로고를 만들어 줘'가 '로고를 만들어 줘'보다 더 효과적입니다.
- **반복 및 개선:** 첫 번째 시도에서 완벽한 이미지를 기대하지 마세요. 모델의 대화형 특성을 사용하여 약간의 변경사항을 적용합니다. '좋은데 조명을 좀 더 따뜻하게 해 줘' 또는 '다른 건 그대로 두고 캐릭터의 표정을 더 심각하게 바꿔 줘'와 같은 프롬프트로 후속 조치를 취합니다.
- **단계별 안내 사용:** 요소가 많은 복잡한 장면의 경우 프롬프트를 단계로 나눕니다. '먼저 새벽의 고요하고 안개 낀 숲의 배경을 만들어 줘. 그런 다음 전경에 이끼로 덮인 고대 돌 제단을 추가하고
  마지막으로 제단 위에 빛나는 검 하나를 놓아'
- **'시맨틱 네거티브 프롬프트' 사용:** '차가 없다'고 말하는 대신, 원하는 장면을 긍정적으로 묘사하세요.'교통의 흔적조차 없는 텅 빈, 황량한 거리'
- **카메라 제어:** 사진 및 영화 언어를 사용하여 구도를 제어합니다. `wide-angle shot`, `macro shot`, `low-angle
  perspective`와 같은 용어

## 제한사항

- 최상의 성능을 위해 다음 언어를 사용하세요. EN, ar-EG, de-DE, es-MX, fr-FR, hi-IN, id-ID, it-IT, ja-JP, ko-KR, pt-BR, ru-RU, ua-UA, vi-VN, zh-CN
- 이미지 생성은 오디오 입력을 지원하지 않습니다. 동영상 입력은 Gemini 3.1 Flash Image에서만 지원됩니다.
- 모델이 사용자가 명시적으로 요청한 정확한 수의 이미지 출력을 따르지 않을 수 있습니다.
- `gemini-2.5-flash-image`는 최대 3개의 이미지를 입력으로 사용할 때 가장 잘 작동하며, `gemini-3-pro-image`는 충실도가 높은 이미지 5개와 최대 14개의 이미지를 지원합니다. `gemini-3.1-flash-image`는 단일 워크플로에서 최대 4자의 문자 유사성과 최대 10개의 객체 충실도를 지원합니다.
- 이미지에 대한 텍스트를 생성할 때 먼저 텍스트를 생성한 다음 텍스트와 함께 이미지를 요청하면 Gemini가 가장 잘 작동합니다.
- `gemini-3.1-flash-image` 현재 Google 검색을 사용한 그라운딩은 웹 검색에서 실제 사람의 이미지를 사용하는 것을 지원하지 않습니다.
- 생성된 모든 이미지에는 [SynthID 워터마크](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ko)가 포함됩니다.

## 선택적 구성

선택적으로 `generate_content` 호출의 `config` 필드에서 모델 출력의 응답 모달리티와 가로세로 비율을 구성할 수 있습니다.

### 출력 유형

모델은 기본적으로 텍스트 및 이미지 응답(즉, `response_modalities=['Text', 'Image']`)을 반환합니다. `response_modalities=['Image']`을 사용하여 텍스트 없이 이미지만 반환하도록 응답을 구성할 수 있습니다.

### Python

```
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
```

### 자바스크립트

```
const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
    config: {
        responseModalities: ['Image']
    }
  });
```

### Go

```
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.1-flash-image",
    genai.Text("Create a picture of a nano banana dish in a " +
                " fancy restaurant with a Gemini theme"),
    &genai.GenerateContentConfig{
        ResponseModalities: "Image",
    },
  )
```

### Java

```
response = client.models.generateContent(
    "gemini-3.1-flash-image",
    prompt,
    GenerateContentConfig.builder()
        .responseModalities("IMAGE")
        .build());
```

### C#

```
var response = await client.Models.GenerateContentAsync(
    model: "gemini-3.1-flash-image",
    contents: new List<Part> { new Part { Text = prompt } },
    config: new GenerateContentConfig
    {
        ResponseModalities = new List<string> { "IMAGE" }
    }
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["Image"]
    }
  }'
```

### 가로세로 비율 및 이미지 크기

모델은 기본적으로 출력 이미지 크기를 입력 이미지 크기에 맞추거나 1:1 정사각형을 생성합니다.
다음과 같이 응답 요청의 `response_format` 아래에 있는 `aspect_ratio` 필드를 사용하여 출력 이미지의 가로세로 비율을 제어할 수 있습니다.

### Python

```
# For gemini-2.5-flash-image
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_format={"image": {aspect_ratio: "16:9",}}
    )
)

# For gemini-3.1-flash-image and gemini-3-pro-image
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_format={"image": {aspect_ratio: "16:9",                 image_size: "2K",}}
    )
)
```

### 자바스크립트

```
// For gemini-2.5-flash-image
const response = await ai.models.generateContent({
    model: "gemini-2.5-flash-image",
    contents: prompt,
    config: {
      responseFormat: {
    image: {
        aspectRatio: "16:9",
      }
  },
    }
  });

// For gemini-3.1-flash-image and gemini-3-pro-image
const response_gemini3 = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
    config: {
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "2K",
      }
  },
    }
  });
```

### Go

```
// For gemini-2.5-flash-image
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-2.5-flash-image",
    genai.Text("Create a picture of a nano banana dish in a " +
                " fancy restaurant with a Gemini theme"),
    &genai.GenerateContentConfig{
        ImageConfig: &genai.ImageConfig{
          AspectRatio: "16:9",
        },
    }
  )

// For gemini-3.1-flash-image and gemini-3-pro-image
result_gemini3, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.1-flash-image",
    genai.Text("Create a picture of a nano banana dish in a " +
                " fancy restaurant with a Gemini theme"),
    &genai.GenerateContentConfig{
        ImageConfig: &genai.ImageConfig{
          AspectRatio: "16:9",
          ImageSize: "2K",
        },
    }
  )
```

### Java

```
// For gemini-2.5-flash-image
response = client.models.generateContent(
    "gemini-2.5-flash-image",
    prompt,
    GenerateContentConfig.builder()
        .imageConfig(ImageConfig.builder()
            .aspectRatio("16:9")
            .build())
        .build());

// For gemini-3.1-flash-image and gemini-3-pro-image
response_gemini3 = client.models.generateContent(
    "gemini-3.1-flash-image",
    prompt,
    GenerateContentConfig.builder()
        .imageConfig(ImageConfig.builder()
            .aspectRatio("16:9")
            .imageSize("2K")
            .build())
        .build());
```

### C#

```
// For gemini-2.5-flash-image
var response = await client.Models.GenerateContentAsync(
    model: "gemini-2.5-flash-image",
    contents: new List<Part> { new Part { Text = prompt } },
    config: new GenerateContentConfig
    {
        ImageConfig = new ImageConfig
        {
            AspectRatio = "16:9"
        }
    }
);

// For gemini-3.1-flash-image and gemini-3-pro-image
var response_gemini3 = await client.Models.GenerateContentAsync(
    model: "gemini-3.1-flash-image",
    contents: new List<Part> { new Part { Text = prompt } },
    config: new GenerateContentConfig
    {
        ImageConfig = new ImageConfig
        {
            AspectRatio = "16:9",
            ImageSize = "2K"
        }
    }
);
```

### REST

```
# For gemini-2.5-flash-image
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }],
    "generationConfig": {
      "responseFormat": {
    "image": {
        "aspectRatio": "16:9"
      }
  }
    }
  }'

# For gemini-3-pro-image
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }],
    "generationConfig": {
      "responseFormat": {
    "image": {
        "aspectRatio": "16:9",
        "imageSize": "2K"
      }
  }
    }
  }'
```

사용 가능한 다양한 비율과 생성된 이미지의 크기는 다음 표에 나와 있습니다.

### 3.1 Flash 이미지

| 가로세로 비율 | 512 해상도 | 토큰 500개 | 1K 해상도 | 토큰 1,000개 | 2K 해상도 | 토큰 2,000개 | 4K 해상도 | 4,000토큰 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1:1** | 512x512 | 747 | 1024x1024 | 1120 | 2048x2048 | 1680 | 4096x4096 | 2520 |
| **1:4** | 256x1024 | 747 | 512x2048 | 1120 | 1024x4096 | 1680 | 2048x8192 | 2520 |
| **1:8** | 192x1536 | 747 | 384x3072 | 1120 | 768x6144 | 1680 | 1536x12288 | 2520 |
| **2:3** | 424x632 | 747 | 848x1264 | 1120 | 1696x2528 | 1680 | 3392x5056 | 2520 |
| **3:2** | 632x424 | 747 | 1264x848 | 1120 | 2528x1696 | 1680 | 5056x3392 | 2520 |
| **3:4** | 448x600 | 747 | 896x1200 | 1120 | 1792x2400 | 1680 | 3584x4800 | 2520 |
| **4:1** | 1024x256 | 747 | 2048x512 | 1120 | 4096x1024 | 1680 | 8192x2048 | 2520 |
| **4:3** | 600x448 | 747 | 1200x896 | 1120 | 2400x1792 | 1680 | 4800x3584 | 2520 |
| **4:5** | 464x576 | 747 | 928x1152 | 1120 | 1856x2304 | 1680 | 3712x4608 | 2520 |
| **5:4** | 576x464 | 747 | 1152x928 | 1120 | 2304x1856 | 1680 | 4608x3712 | 2520 |
| **8:1** | 1536x192 | 747 | 3072x384 | 1120 | 6144x768 | 1680 | 12288x1536 | 2520 |
| **9:16** | 384x688 | 747 | 768x1376 | 1120 | 1536x2752 | 1680 | 3072x5504 | 2520 |
| **16:9** | 688x384 | 747 | 1376x768 | 1120 | 2752x1536 | 1680 | 5504x3072 | 2520 |
| **21:9** | 792x168 | 747 | 1584x672 | 1120 | 3168x1344 | 1680 | 6336x2688 | 2520 |

### 3.1 Flash Lite 이미지

| 가로세로 비율 | 512 해상도 | 토큰 500개 | 1K 해상도 | 토큰 1,000개 |
| --- | --- | --- | --- | --- |
| **1:1** | 512x512 | 747 | 1024x1024 | 1120 |
| **1:4** | 256x1024 | 747 | 512x2048 | 1120 |
| **1:8** | 192x1536 | 747 | 384x3072 | 1120 |
| **2:3** | 424x632 | 747 | 848x1264 | 1120 |
| **3:2** | 632x424 | 747 | 1264x848 | 1120 |
| **3:4** | 448x600 | 747 | 896x1200 | 1120 |
| **4:1** | 1024x256 | 747 | 2048x512 | 1120 |
| **4:3** | 600x448 | 747 | 1200x896 | 1120 |
| **4:5** | 464x576 | 747 | 928x1152 | 1120 |
| **5:4** | 576x464 | 747 | 1152x928 | 1120 |
| **8:1** | 1536x192 | 747 | 3072x384 | 1120 |
| **9:16** | 384x688 | 747 | 768x1376 | 1120 |
| **16:9** | 688x384 | 747 | 1376x768 | 1120 |
| **21:9** | 792x168 | 747 | 1584x672 | 1120 |

### 3.1 Pro 이미지

| 가로세로 비율 | 1K 해상도 | 토큰 1,000개 | 2K 해상도 | 토큰 2,000개 | 4K 해상도 | 4,000토큰 |
| --- | --- | --- | --- | --- | --- | --- |
| **1:1** | 1024x1024 | 1120 | 2048x2048 | 1120 | 4096x4096 | 2000 |
| **2:3** | 848x1264 | 1120 | 1696x2528 | 1120 | 3392x5056 | 2000 |
| **3:2** | 1264x848 | 1120 | 2528x1696 | 1120 | 5056x3392 | 2000 |
| **3:4** | 896x1200 | 1120 | 1792x2400 | 1120 | 3584x4800 | 2000 |
| **4:3** | 1200x896 | 1120 | 2400x1792 | 1120 | 4800x3584 | 2000 |
| **4:5** | 928x1152 | 1120 | 1856x2304 | 1120 | 3712x4608 | 2000 |
| **5:4** | 1152x928 | 1120 | 2304x1856 | 1120 | 4608x3712 | 2000 |
| **9:16** | 768x1376 | 1120 | 1536x2752 | 1120 | 3072x5504 | 2000 |
| **16:9** | 1376x768 | 1120 | 2752x1536 | 1120 | 5504x3072 | 2000 |
| **21:9** | 1584x672 | 1120 | 3168x1344 | 1120 | 6336x2688 | 2000 |

### Gemini 2.5 Flash Image

| 가로세로 비율 | 해상도 | 토큰 |
| --- | --- | --- |
| 1:1 | 1024x1024 | 1290 |
| 2:3 | 832x1248 | 1290 |
| 3:2 | 1248x832 | 1290 |
| 3:4 | 864x1184 | 1290 |
| 4:3 | 1184x864 | 1290 |
| 4:5 | 896x1152 | 1290 |
| 5:4 | 1152x896 | 1290 |
| 9:16 | 768x1344 | 1290 |
| 16:9 | 1344x768 | 1290 |
| 21:9 | 1536x672 | 1290 |

## 모델 선택

특정 사용 사례에 가장 적합한 모델을 선택합니다.

- **Gemini 3.1 Flash Image (Nano Banana 2)**는 비용과 지연 시간의 균형을 맞추는 최고의 전반적인 성능과 인텔리전스를 갖춘 이미지 생성 모델입니다. 자세한 내용은 모델 [가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#gemini-3.1-flash-image) 및 [기능](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=ko) 페이지를 참고하세요.
- **Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite)**는 이미지 생성 제품군의 효율성 전문가로 설계되어 지연 시간이 매우 짧고 비용 효율적인 이미지 생성 및 편집을 제공합니다.
  자세한 내용은 모델 [가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#gemini-3.1-flash-lite-image) 및 [기능](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=ko) 페이지를 참고하세요.
- **Gemini 3 Pro Image (Nano Banana Pro)**는 전문적인 애셋 제작과 복잡한 안내를 위해 설계되었습니다. 이 모델은 Google 검색을 사용한 실제 그라운딩, 생성 전에 구성을 개선하는 기본 '생각' 프로세스를 특징으로 하며 최대 4K 해상도의 이미지를 생성할 수 있습니다. 자세한 내용은 모델 [가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#gemini-3-pro-image) 및 [기능](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=ko) 페이지를 참고하세요.
- **Gemini 2.5 Flash Image (Nano Banana)**는 속도와 효율성을 위해 설계되었습니다. 이 모델은 대량의 낮은 지연 시간 태스크에 최적화되어 있으며 1024px 해상도로 이미지를 생성합니다. 자세한 내용은 모델 [가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#gemini-2.5-flash-image) 및 [기능](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ko) 페이지를 참고하세요.

### Imagen을 사용해야 하는 경우

Gemini의 기본 제공 이미지 생성 기능 사용 외에도 Gemini API를 통해 Google의 특화된 이미지 생성 모델인 [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ko)에도 액세스할 수 있습니다. 폐쇄일 전에 마이그레이션하세요.

## 다음 단계

- [쿡북 가이드](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_Started_Nano_Banana.ipynb?hl=ko)에서 더 많은 예와 코드 샘플을 확인하세요.
- [Veo 가이드](https://ai.google.dev/gemini-api/docs/video?hl=ko)에서 Gemini API로 동영상을 생성하는 방법을 알아보세요.
- Gemini 모델에 대해 자세히 알아보려면 [Gemini 모델](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko)을 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-16(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-16(UTC)"],[],[]]
