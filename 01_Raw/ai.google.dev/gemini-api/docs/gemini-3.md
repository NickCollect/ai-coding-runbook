---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=zh-TW
fetched_at: 2026-09-21T05:57:52.046072+00:00
title: "Gemini 3 \u958b\u767c\u4eba\u54e1\u6307\u5357 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)

提供意見

# Gemini 3 開發人員指南

Gemini 3 是我們至今最強大的模型系列，以最先進的推論技術為基礎。這項技術旨在運用代理工作流程、自主編碼和複雜的多模態工作，將任何想法化為現實。本指南將介紹 Gemini 3 模型系列的主要功能，以及如何充分發揮這些功能。

歡迎瀏覽 [Gemini 3 應用程式系列](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=zh-tw)，瞭解這款模型如何處理進階推論、自主程式設計和複雜的多模態工作。

只要編寫幾行程式碼，即可開始使用：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(
            InteractionsInput.of(
                "Find the race condition in this multi-threaded C++ snippet: [code here]"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## 認識 Gemini 3 系列

Gemini 3.1 Pro 最適合處理複雜工作，
需要廣泛的世界知識，以及跨模態的進階推論能力。

Gemini 3 Flash 是我們最新的第 3 系列模型，具備 Pro 級智慧，但速度和價格與 Flash 相同。

Nano Banana Pro (又稱 Gemini 3 Pro Image) 是 Google 最高品質的圖像生成模型，而 Nano Banana 2 (又稱 Gemini 3.1 Flash Image) 則具備高產量、高效率和低價位等優勢。

Gemini 3.1 Flash-Lite 是我們的主力模型，專為符合成本效益的模型和大量工作而打造。

所有 Gemini 3 模型目前皆為預先發布版。

| 模型 ID | 背景期間 (內 / 外) | 知識截點 | 定價 (輸入 / 輸出)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 100 萬次 / 6.4 萬次 | 2025 年 1 月 | $0.25 (文字、圖片、影片)、$0.50 (音訊) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128k / 32k | 2025 年 1 月 | $0.25 美元 (文字輸入) / $0.067 美元 (圖片輸出)\*\* |
| **gemini-3.1-pro-preview** | 100 萬次 / 6.4 萬次 | 2025 年 1 月 | $2 美元 / $12 美元 (少於 20 萬個權杖)   $4 美元 / $18 美元 (超過 20 萬個權杖) |
| **gemini-3-flash-preview** | 100 萬次 / 6.4 萬次 | 2025 年 1 月 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | 2025 年 1 月 | $2 (文字輸入) / $0.134 (圖片輸出)\*\* |

*\* 除非另有註明，否則價格以每 100 萬個權杖為單位。*
*\*\* 圖片價格會因解析度而異。詳情請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。*

如需詳細的限制、定價和其他資訊，請參閱[模型頁面](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw)。

## Gemini 3 的新 API 功能

Gemini 3 推出全新參數，讓開發人員進一步掌控延遲時間、成本和多模態準確度。

### 思考程度

Gemini 3 系列模型預設會使用動態思考功能，根據提示進行推論。您可以使用 `thinking_level` 參數，控制模型產生回覆前內部推論過程的**最大**深度。Gemini 3 會將這些層級視為思考的相對配額，而非嚴格的權杖保證。

如未指定 `thinking_level`，Gemini 3 會預設為 `high`。如果不需要複雜的推論，可以將模型的思考層級限制為 `low`，加快回應速度並降低延遲。

| 思考程度 | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 說明 |
| --- | --- | --- | --- | --- |
| **`minimal`** | 不支援 | 支援 (預設) | 支援 | 對於大多數查詢，這項設定與「不思考」相同。模型可能會以極少的思考時間處理複雜的程式碼編寫工作。將聊天或高處理量應用程式的延遲時間降到最低。請注意，`minimal` 無法保證思考功能已關閉。 |
| **`low`** | 支援 | 支援 | 支援 | 盡量縮短延遲時間並降低成本。最適合用於簡單的指令遵循、即時通訊或高處理量應用程式。 |
| **`medium`** | 支援 | 支援 | 支援 | 思考能力均衡，適合處理多數工作。 |
| **`high`** | 支援 (預設、動態) | 支援 (動態) | 支援 (預設、動態) | 盡可能深入推論。模型可能需要較長時間才能輸出第一個 (非思考) 輸出權杖，但輸出內容會經過更仔細的推論。 |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("How does AI work?"))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.LOW)
                .build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### 溫度

對於所有 Gemini 3 模型，我們強烈建議將溫度參數維持預設值 `1.0`。

先前的模型通常會調整溫度參數，以控制創意與確定性，但 Gemini 3 的推論能力已針對預設設定進行最佳化。變更溫度參數 (設為低於 1.0) 可能會導致異常行為，例如迴圈或效能降低，特別是在複雜的數學或推論任務。

### 想法簽名

Gemini 3 模型會使用思維簽章，在 API 呼叫之間維持推理脈絡。這些簽章是模型內部思考過程的加密表示法。

- **有狀態模式 (建議)**：在有狀態模式下使用 Interactions API (提供 `previous_interaction_id` 時)，伺服器會自動管理對話記錄和想法簽章。
- **無狀態模式**：如果手動管理對話記錄，後續要求必須包含附有簽章的思維方塊，才能驗證真偽。

詳情請參閱「[Thought Signatures](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)」頁面。

### 使用工具輸出結構化內容

Gemini 3 模型可讓您結合[結構化輸出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)與內建工具，包括[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)、[網址背景資訊](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)、[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)和[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)。

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("winner", Map.of("type", "string", "description", "The name of the winner."));
properties.put(
    "final_match_score", Map.of("type", "string", "description", "The final match score."));
properties.put(
    "scorers",
    Map.of(
        "type", "array",
        "items", Map.of("type", "string"),
        "description", "The name of the scorer."));

Map<String, Object> schema = new HashMap<>();
schema.put("type", "object");
schema.put("properties", properties);
schema.put("required", Arrays.asList("winner", "final_match_score", "scorers"));

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("Search for all details for the latest Euro."))
        .tools(Arrays.asList(GoogleSearch.builder().build(), URLContext.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    TextResponseFormat.builder()
                        .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                        .schema(schema)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### 圖像生成

Gemini 3.1 Flash Image 和 Gemini 3 Pro Image 可根據文字提示生成及編輯圖像。這項功能會運用推論能力「思考」提示詞，並擷取即時資料 (例如天氣預報或股票圖表)，然後使用 [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)建立基準，生成高擬真度的圖片。

**全新與改良功能：**

- **4K 和文字算繪：**生成清晰易讀的文字和圖表，最高可達 2K 和 4K 解析度。
- **以真實資訊為依據生成圖片：**使用 `google_search` 工具驗證事實，並根據真實世界資訊生成圖像。透過 Google *圖片*搜尋建立基準，適用於 Gemini 3.1 Flash Image。
- **對話式修圖：**只要提出變更要求 (例如「將背景改成日落」)，即可多輪編輯圖像。這個工作流程會使用**想法簽章**，在回合之間保留視覺情境。

如要進一步瞭解長寬比、編輯工作流程和設定選項，請參閱[圖片生成指南](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)。

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageResponseFormat;
import com.google.genai.gaos.models.interactions.ImageResponseFormatAspectRatio;
import com.google.genai.gaos.models.interactions.ImageResponseFormatImageSize;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.Optional;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-pro-image-preview"))
        .input(InteractionsInput.of("Generate an infographic of the current weather in Tokyo."))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    ImageResponseFormat.builder()
                        .aspectRatio(ImageResponseFormatAspectRatio.ONE_HUNDRED_AND_SIXTY_NINE)
                        .imageSize(ImageResponseFormatImageSize.FOUR_K)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

Optional<ImageContent> generatedImage = interaction.outputImage();
if (generatedImage.isPresent() && generatedImage.get().data().isPresent()) {
  byte[] imageBytes = Base64.getDecoder().decode(generatedImage.get().data().get());
  Files.write(Paths.get("weather_tokyo.png"), imageBytes);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**範例回應**

![東京天氣](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=zh-tw)

### 使用圖片執行程式碼

Gemini 3 Flash 可將視覺內容視為主動調查，而不只是靜態瀏覽。模型會結合推論和[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)功能，制定計畫，然後編寫及執行 Python 程式碼，逐步放大、裁剪、註解或以其他方式處理圖片，以便根據視覺內容提供答案。

**用途：**

- **縮放及檢查：**模型會隱含地偵測細節是否過小 (例如讀取遠處的儀表或序號)，並編寫程式碼來裁剪及重新檢查高解析度的區域。
- **視覺化數學和繪圖：**模型可使用程式碼執行多步驟計算 (例如加總收據上的項目，或從擷取的資料生成 Matplotlib 圖表)。
- **圖片註解：**模型可以直接在圖片上繪製箭頭、標示框或其他註解，回答「這個項目應該放在哪裡？」等空間問題。

如要啟用視覺化思考功能，請將「程式碼執行」設定為工具。如有需要，模型會自動使用程式碼來處理圖片。

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

URL url = new URL("https://goo.gle/instrument-img");
byte[] imageBytes;
try (InputStream is = url.openStream()) {
  imageBytes = is.readAllBytes();
}
String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .data(base64ImageData)
                        .build(),
                    TextContent.builder()
                        .text("Zoom into the expression pedals and tell me how many pedals are there?")
                        .build())))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep modelOutput = (ModelOutputStep) step;
    for (Content contentBlock : modelOutput.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println("Text: " + ((TextContent) contentBlock).text().orElse(""));
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().flatMap(args -> args.code()).ifPresent(code -> System.out.println("Code: " + code));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println("Output: " + resultStep.result().orElse(""));
  }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

如要進一步瞭解如何使用圖片執行程式碼，請參閱「[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw#images)」。

### 多模態函式回覆

[多模態函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#multimodal)
可讓使用者取得含有多模態物件的函式回應，
進而提升模型函式呼叫功能的運用效率。標準函式呼叫僅支援以文字為基礎的函式回應：

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.FunctionResultSubcontent;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> itemProp = new HashMap<>();
itemProp.put("type", "string");
itemProp.put("description", "The name or description of the item ordered (e.g., 'instrument').");

Map<String, Object> properties = new HashMap<>();
properties.put("item_name", itemProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("item_name"));

Function getImageTool =
    Function.builder()
        .name("get_image")
        .description("Retrieves the image file reference for a specific order item.")
        .parameters(parameters)
        .build();

CreateModelInteraction req1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "Use the get_image tool to show me the instrument I ordered last month."))
        .tools(Arrays.asList(getImageTool))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(req1)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction1.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  System.out.println("Tool Call: " + fcStep.name().orElse(""));

  URL url = new URL("https://goo.gle/instrument-img");
  byte[] imageBytes;
  try (InputStream is = url.openStream()) {
    imageBytes = is.readAllBytes();
  }
  String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

  List<FunctionResultSubcontent> subcontents = new ArrayList<>();
  subcontents.add(TextContent.builder().text("instrument.jpg").build());
  subcontents.add(
      ImageContent.builder()
          .mimeType(ImageContentMimeType.IMAGE_JPEG)
          .data(base64ImageData)
          .build());

  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(FunctionResultStepResultUnion.of(subcontents))
          .build();

  CreateModelInteraction req2 =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(getImageTool))
          .previousInteractionId(interaction1.id().orElse(""))
          .build();

  Interaction interaction2 =
      client.interactions.create(CreateInteractionRequestBody.of(req2)).interaction().get();
  System.out.println("Final model response: " + interaction2.outputText().orElse(""));
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### 結合使用內建工具和函式呼叫

Gemini 3 允許在同一個 API 呼叫中使用內建工具 (例如 Google 搜尋、網址內容和[更多](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)) 和自訂[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)工具，因此可執行更複雜的工作流程。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> cityProp = new HashMap<>();
cityProp.put("type", "string");
cityProp.put("description", "The city and state, e.g. Utqiaġvik, Alaska");

Map<String, Object> properties = new HashMap<>();
properties.put("city", cityProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("city"));

Function getWeather =
    Function.builder()
        .name("getWeather")
        .description("Gets the weather for a requested city.")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "What is the northernmost city in the United States? What's the weather like there today?"))
        .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(
              FunctionResultStepResultUnion.of(
                  "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"))
          .build();

  CreateModelInteraction finalRequest =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
          .previousInteractionId(interaction.id().orElse(""))
          .build();

  Interaction finalInteraction =
      client.interactions.create(CreateInteractionRequestBody.of(finalRequest)).interaction().get();
  System.out.println(finalInteraction.outputText().orElse(""));
}
```

## 從 Gemini 2.5 遷移

Gemini 3 是我們迄今最強大的模型系列，相較於 Gemini 2.5，效能有顯著提升。遷移時，請注意以下事項：

- **思考：**如果您先前使用複雜的提示工程 (例如思緒鏈) 強迫 Gemini 2.5 推理，請嘗試使用 `thinking_level: "high"` 和簡化提示的 Gemini 3。
- **溫度設定：**如果現有程式碼明確設定溫度參數 (尤其是將溫度設為低值，以取得確定性輸出內容)，建議您移除這個參數，並使用 Gemini 3 的預設值 1.0，以免在複雜工作上發生潛在的迴圈問題或效能下降。
- **PDF 和文件理解：**
  如果您依賴特定行為來剖析密集文件，請測試新的 `media_resolution_high` 設定，確保準確度不受影響。
- **詞元用量：**改用 Gemini 3 預設模型後，PDF 的詞元用量可能會**增加**，但影片的詞元用量會**減少**。如果預設解析度提高後，要求超出脈絡窗口，建議您明確降低媒體解析度。
- **影像分割：**Gemini 3 Pro 或 Gemini 3 Flash 不支援影像分割功能 (傳回物件的像素層級遮罩)。如要處理需要內建影像分割的工作負載，建議繼續使用 Gemini 2.5 Flash，並關閉思考功能。
- **電腦用途：**Gemini 3 Pro 和 Gemini 3 Flash 支援[電腦用途](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)。與 2.5 系列不同，您不必使用其他模型就能存取電腦使用工具。
- **工具支援**：Gemini 3 模型現在支援[結合內建工具和函式呼叫](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)。Gemini 3 模型現在也支援[地圖基礎](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)。

## OpenAI 相容性

如果使用者採用 [OpenAI 相容性層](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)，系統會自動將標準參數 (OpenAI 的 `reasoning_effort`) 對應至 Gemini (`thinking_level`) 的對等項目。

## 提示最佳做法

Gemini 3 是推論模型，因此提示方式有所不同。

- **明確的指令：**輸入提示時請簡潔扼要。Gemini 3 最適合直接且清楚的指令。如果使用舊版模型，系統可能會過度分析冗長或過於複雜的提示工程技術。
- **輸出詳細程度：**Gemini 3 預設會提供簡潔的回覆，偏好直接且有效率地回答問題。如果您的用途需要更具對話感或「健談」的角色，請務必在提示中明確引導模型 (例如「以友善健談的助理身分說明這件事」)。
- **脈絡管理：**處理大型資料集 (例如整本書、程式碼集或長篇影片) 時，請將具體指令或問題放在提示結尾的資料脈絡之後。在問題開頭使用「根據上述資訊...」等詞組，讓模型根據提供的資料進行推論。

如要進一步瞭解提示設計策略，請參閱[提示工程指南](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw)。

## 常見問題

1. **Gemini 3 的知識截點為何？**Gemini 3 模型可存取的知識截點為 2025 年 1 月。如需最新資訊，請使用[搜尋基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)工具。
2. **脈絡窗口的限制為何？**Gemini 3 模型支援 100 萬個詞元的輸入脈絡窗口，以及最多 64,000 個詞元的輸出。
3. **Gemini 3 是否提供免費方案？**Gemini 3 Flash
   `gemini-3-flash-preview` 在 Gemini API 中提供免費方案。您可以在 Google AI Studio 免付費試用 Gemini 3.1 Pro 和 3 Flash，但 Gemini API 的 `gemini-3.1-pro-preview` 沒有免付費方案。
4. **舊的 `thinking_budget` 程式碼是否仍可運作？**可以，`thinking_budget` 仍支援回溯相容性，但建議遷移至 `thinking_level`，以獲得更可預測的成效。請勿在同一項要求中同時使用這兩者。
5. **Gemini 3 是否支援 Batch API？**可以，Gemini 3 支援 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)。
6. **是否支援脈絡快取？**是，Gemini 3 支援[脈絡快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)。
7. **Gemini 3 支援哪些工具？**Gemini 3 支援 [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)、[利用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)、[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)、[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)和[網址背景資訊](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)。此外，這項功能也支援標準的[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)，可搭配自訂工具和[內建工具](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)使用。
8. **什麼是 `gemini-3.1-pro-preview-customtools`？**如果您使用 `gemini-3.1-pro-preview`，但模型忽略您的自訂工具，改用 bash 指令，請改用 `gemini-3.1-pro-preview-customtools` 模型。詳情請參閱 [這篇文章][customtools-model]。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-18 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-18 (世界標準時間)。"],[],[]]
