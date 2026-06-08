---
source_url: https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-TW
fetched_at: 2026-06-08T05:36:48.021834+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Files API

Gemini 可同時處理各種輸入資料，包括文字、圖片和音訊。

本指南說明如何使用 Files API 處理媒體檔案。音訊檔案、圖片、影片、文件和其他支援的檔案類型，基本操作都相同。

如需檔案提示詞指南，請參閱「[檔案提示詞指南](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-tw#prompt-guide)」一節。

## 上傳檔案

您可以使用 Files API 上傳媒體檔案。如果要求總大小 (包括檔案、文字提示、系統指令等) 超過 100 MB，請務必使用 Files API。如果是 PDF 檔案，上限為 50 MB。

下列程式碼會上傳檔案，然後在呼叫 `interactions.create` 時使用該檔案。

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
    -H "Api-Revision: 2026-05-20" \
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

## 取得檔案的中繼資料

您可以呼叫 `files.get`，確認 API 是否已成功儲存上傳的檔案並取得其
中繼資料。

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

## 列出上傳的檔案

下列程式碼會取得所有已上傳檔案的清單：

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

## 刪除上傳的檔案

檔案會在 48 小時後自動刪除。你也可以手動刪除上傳的檔案：

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

## 使用資訊

您可以使用 Files API 上傳媒體檔案並與之互動。透過 Files API，每個專案最多可儲存 20 GB 的檔案，每個檔案的大小上限為 2 GB。檔案會儲存 48 小時。在這段期間，您可以使用 API 取得檔案的中繼資料，但無法下載檔案。在 Gemini API 支援的所有地區，都能免付費使用 Files API。

## 檔案提示策略

本節提供使用 Gemini API 提示搭配媒體檔案的指南和最佳做法。

提示中可使用的資料類型越多，您就能越靈活地運用 Gemini API 處理各種工作。例如，你可以向模型傳送美味餐點的相片，並請模型撰寫有關該餐點的短篇網誌。

|  |  |
| --- | --- |
| **提示** | **回應** |
| 根據這張相片撰寫簡短有趣的網誌文章。文章應包含相片中餐點的說明，並談談我準備餐點的過程。   Cookie | 事先備餐是節省時間和金錢的好方法，也有助於健康飲食。這道餐點就是健康美味的絕佳例子，而且可以事先備妥。  這道餐點包含糙米、烤蔬菜和照燒雞肉。糙米是健康且複雜的碳水化合物，可提供持久的能量。烤蔬菜是攝取每日維生素和礦物質的絕佳方式，照燒雞肉則美味又富含蛋白質。  這道餐點的準備方式也很簡單。只要煮好糙米飯、烤蔬菜，以及烹調照燒雞肉，所有食材煮熟後， 將餐點分裝到備餐容器中，然後放入冰箱。 這樣就能在忙碌的早晨直接拿了就走！  如果你想找一道健康美味的料理，而且可以事先準備，這道料理就是絕佳選擇。這道料理營養豐富、風味十足，保證能讓你吃得飽足又滿足。  祝你餐點準備順利，吃得健康又美味！ |

如果使用媒體檔案的提示無法產生所需輸出內容，可以嘗試一些策略，協助您取得想要的結果。以下各節提供設計方法和疑難排解提示，協助您改善使用多模態輸入內容的提示。

如要改善多模態提示，請參考下列最佳做法：

- ### [提示設計基礎知識](#specific-instructions)

  - **提供明確的指示**：清楚簡潔地說明指示，盡量避免誤解。
  - **在提示中加入幾個範例：**使用實際的少量樣本範例，說明您想達成的目標。
  - **逐步分解**：將複雜工作拆解成容易處理的子目標，引導模型完成程序。
  - **指定輸出格式**：在提示中要求輸出內容採用所需格式，例如 Markdown、JSON、HTML 等。
  - **單一圖片提示詞請先放上圖片**：Gemini 可以處理任何順序的圖片和文字輸入內容，但如果提示詞只包含一張圖片，將圖片 (或影片) 放在文字提示詞前面，或許能獲得更佳的結果。不過，如果提示詞需要圖片和文字高度交錯才能有意義，請使用最自然的順序。
- ### [排解多模態提示詞問題](#troubleshooting)

  - **如果模型未從圖片的相關部分提取資訊：**請提供提示，說明要從圖片的哪些部分提取資訊。
  - **如果模型輸出內容過於一般 (不夠符合輸入的圖片/影片)：** 在提示開頭，先要求模型描述圖片或影片，再提供工作指令，或要求模型參考圖片內容。
  - **如要排解哪個部分發生錯誤：**要求模型描述圖片或說明推論過程，評估模型初步理解的內容。
  - **如果提示詞導致模型生成幻覺內容：**請嘗試調低溫度參數設定，或要求模型提供較短的說明，這樣模型就不太可能推斷出額外的詳細資料。
  - **調整取樣參數：**實驗不同的溫度參數設定和 Top-K 選項，調整模型的創意程度。

### 指令應明確具體

提示越清楚詳細，生成結果就越符合需求。如果您有特定輸出內容，建議在提示中加入該要求，確保取得所需輸出內容。

以這張機場看板圖片為例，如果只要求模型「描述這張圖片」，模型可能會生成一般描述。如要讓模型從圖片中剖析時間和城市，可以直接在提示中加入這項要求。

| 提示詞 | 模型回應 |
| --- | --- |
| 描述這張圖片。 | 圖片：機場抵達和起飛時刻資訊看板。 |

| **更新提示** | **提升回應速度** |
| --- | --- |
| 旅行時刻表 Parse the time and city from the airport board shown in this image into a list. | - 莫斯科 10:50 - 11:05 愛丁堡 - 11:05 倫敦 - 11:10 布加勒斯特 - 基輔時間 11:30 - 11:35 都柏林 - 11:45 東密德蘭 - 12:15 索非亞 - 倫敦時間 12:30 - 12:30 新堡 - 12:40 聖彼得堡 - 12:40 倫敦 - 12:45 曼徹斯特 |

### 新增幾個範例

Gemini 模型可接受多項輸入內容，並將其做為範例，瞭解您想要的輸出內容。加入這些範例有助於模型找出模式，並將指定圖片和回覆之間的關係套用至新範例。這也稱為「少量樣本」學習。

在以下範例中，初始輸出內容是以句子形式撰寫，且包含國家/地區 (巴西)。假設您希望輸出內容採用不同格式或風格，而且只要城市名稱，不要國家/地區名稱。在提示中加入少樣本範例，可引導模型以您期望的方式回覆。

| **提示** | **模型回覆** |
| --- | --- |
| 旅行時刻表 判斷地標所在的城市。 | 地標是巴西里約熱內盧的救世基督像。 |

| **更新提示** | **提升回應速度** |
| --- | --- |
| 判斷地標所在的城市。 羅馬競技場 | 城市：羅馬，地標：羅馬競技場。 |
| 紫禁城 | 城市：北京，地標：紫禁城 |
| forbidden-city | 城市：里約熱內盧，地標：救世基督像 |

### 逐步分解

對於需要視覺理解和推論的複雜任務，將任務拆解成更簡單、更直接的步驟會很有幫助。或者，在提示詞中直接要求模型「逐步思考」也可能有效。

| 提示詞 | 模型回應 |
| --- | --- |
| 我何時會用完衛生紙？ | 不久後，你只剩下 3 卷底片。 |

| **更新提示** | **提升回應速度** |
| --- | --- |
| 1. 首先，請計算這張圖片中有多少捲衛生紙。 2. 接著，判斷一般人每天使用的衛生紙量。 3. 計算這些捲筒衛生紙可以使用多久。 | 1. 這張圖片中有 3 卷衛生紙。 2. 一般人每天約使用 20 張衛生紙。 3. 如果每捲有 200 張，則每捲約可使用 10 天，因此 3 捲約可使用一個月。 |

數學問題或其他類型的文字題很適合要求模型逐步思考。

| **提示** | **回應** |
| --- | --- |
| 這個數列的第 4 項為何？ | -135 |

模型回覆的內容不正確。如要改善這點，可以要求模型先剖析問題，再回答提示。

| **提示** | **回應** |
| --- | --- |
| 請先剖析圖片中的公式。  然後根據公式回答「這個數列的第 4 個項是什麼？」。 | *按一下即可展開結果* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. 將 n = 4 代入公式： $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. 我們不知道 b(3) 的值，因此將 n = 3 代入公式： $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. 我們不知道 b(2) 的值，因此將 n = 2 代入公式： $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. 我們知道 b(1) 的值為 15，因此將其代入公式： $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. 現在我們知道 b(2) 的值，因此可以代入 b(3) 的公式： $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. 現在我們知道 b(3) 的值，請將其代入 b(4) 的公式： $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   因此，這個數列的第 4 項是 -405。 |

這個模型回覆正確無誤，現在為了讓回覆更精簡，你可以要求模型逐步思考。

| **更新提示** | **提升回應速度** |
| --- | --- |
| 這個數列的第 4 項為何？請逐步思考。 | 第一個項是 15。  第二項是 b(1) \* (-3) = 15 \* (-3) = -45。  第三個項是 b(2) \* (-3) = -45 \* (-3) = 135。  第四個項是 b(3) \* (-3) = 135 \* (-3) = -405。 |

### 指定輸出格式

常見的問題是需要模型輸出特定格式的內容 (例如 Markdown、JSON、HTML)，尤其是當下游工作需要擷取模型輸出內容時。您可以在提示詞中指示模型以該格式輸出內容。以下是兩個範例：

| 提示詞 | 模型回應 |
| --- | --- |
| 將這張圖片中的表格剖析為 Markdown 格式 | ```none | Subject | Status | Time | Start date | Due on | | ------- | ------ | ---- | ---------- | ------ | | Math | Done | 1.5 hrs | 11/29/2023 | 12/1/2023 | | Geography | Done | 30 min | 12/2/2023 | 12/4/2023 | | Physics | In progress | 2 hrs | 12/3/2023 | 12/5/2023 | | Biology | Not started | 6 hrs | 11/2/2016 | 12/6/2023 | ``` |

| **提示** | **模型回覆** |
| --- | --- |
| 提供下列所有屬性的清單：  食材、菜餚類型、是否為素食，以 JSON 格式提供 | ```json { "ingredients": [ "rice", "shrimp", "clams", "mussels", "peas", "tomatoes", "onions", "garlic", "olive oil", "paprika", "salt", "pepper" ], "type of cuisine": "Spanish", "vegetarian": false } ``` |

### 單張圖片提示請先輸入圖片

雖然 Gemini 可以解讀提示中的圖片和文字，但將單一圖片放在文字提示之前，可能會產生更出色的結果。在下列範例中，你會發現每個提示中的圖片都放在文字之前。

### 排解多模態提示問題

如果沒有獲得實用回覆，可能需要排解提示問題。你可以嘗試下列幾種策略。

#### 如果模型未從圖片的相關部分擷取資訊

如要取得更具體的答覆，可以指出提示要從圖片的哪些方面汲取資訊，以利生成回覆。

| 提示詞 | 模型回應 |
| --- | --- |
| 這些尿布夠寶寶用幾天？ | 這些尿布可使用 198 天。 |

| **更新提示** | **提升回應速度** |
| --- | --- |
| 這些尿布可以用多久？  根據包裝盒上顯示的體重判斷孩子的年齡，並使用包裝盒中的尿布總數。  將總數除以孩子每天使用的尿布數量。 | 包裝內含 198 片尿布，包裝上標示適用於體重 22 至 37 磅的兒童。  這個體重範圍的兒童平均年齡可能介於 1 到 2 歲。  2 歲幼童通常每天會用掉 6 片尿布，因此 198 片尿布大約可用 33 天 (198/6)。 |

#### 如果模型輸出內容過於一般，不夠符合圖片輸入內容

為協助模型根據圖片調整回覆內容，請先要求模型描述圖片，再執行推論工作。

| 提示詞 | 模型回應 |
| --- | --- |
| 這些圖片有什麼共通點？ | 這四張圖片都是風景攝影的例子。 |

| **更新提示** | **提升回應速度** |
| --- | --- |
| 首先，請詳細描述每張圖片的內容。這些圖片的共同點是什麼？ | 第一張圖片：一個人正在打包行李箱。第二張圖片：購物中心空蕩蕩的走廊。第三張圖片：一捲衛生紙。第四張圖片：狂風暴雨中的大海。  這些圖片的共同點是，它們都是過渡空間的例子。過渡空間是指介於兩個空間或情境之間的地方或情境，通常帶有不確定或模糊的感覺。  第一張圖片顯示該名人士在家中和旅行之間。第二張圖片顯示兩間商店之間的走廊。第三張圖片是衛生紙，代表浴室。浴室是私人和公共領域之間的過渡空間，我們會在浴室準備進入或離開外部世界。  第四張圖片顯示介於平靜和暴風雨之間的海洋。  過渡空間既令人興奮又令人不安，可能是新開始或結束的地方，也可能是反思或行動的地方。 |

你也可以明確要求模型參照圖片內容。

| **更新提示** | **提升回應速度** |
| --- | --- |
| 這些圖片有什麼共通點？請在回覆中說明圖片內容。 | 所有圖片都與旅遊相關。第一張圖片顯示有人正在打包行李箱，第二張圖片顯示購物中心空蕩蕩的走廊，第三張圖片顯示一疊衛生紙，第四張圖片顯示陰暗且暴風雨的海面。  這些圖片都與旅遊相關，因為都是人們旅遊時需要或使用的物品。第一張圖片顯示有人在打包行李箱，這是人們旅遊時會做的事。第二張圖片顯示購物中心空蕩蕩的走廊，人們經常會到購物中心購買旅遊用品。第三張圖片顯示一疊衛生紙，這是人們旅遊時經常使用的物品。第四張圖片顯示暴風雨中的大海，這是人們旅遊時經常會遇到的情況。 |

這些訣竅也適用於圖片的創意輸出內容。在以下兔子範例中，明確要求模型納入圖片中的元素，可提升輸出內容品質。

| 提示詞 | 模型回應 |
| --- | --- |
| 可以幫我寫一首關於這張圖片的詩嗎？ | 小兔兔，毛茸茸，棕色身，  在田野間跳躍，上上下下。  耳朵長長，尾巴短短，  你是最可愛的生物。  你啃食青草，青翠又香甜，  一見到我就跳開。  但直到最後，我都會是你的朋友，  小兔子。 |

| **更新提示** | **提升回應速度** |
| --- | --- |
| 請根據這張圖片撰寫一首描述性強烈且充滿戲劇性的詩，並加入地點資訊。 | 綠地上的小兔，  耳朵又長又尖。  你望向遠方，  看到什麼？  是海洋的藍色，  在陽光下閃閃發光？  還是海浪拍打的轟隆聲，  你喜愛的節奏？  小兔，請告訴我，  是什麼吸引了你的目光？  是鹹鹹的海風，  還是海鷗的叫聲？  或許是這一切的浩瀚，  一個如此巨大又渺小的世界。  夢想在此漫遊，  冒險在此萌芽。  小兔子，我好奇你夢見了什麼，  你坐在草地上，如此寧靜。  你是否渴望探索深海，  還是想留在陸地上跳躍？  無論如何，小兔子，  請讓好奇心持續閃耀。  因為在你的夢想和抱負中，  存在著一個等待你創造的世界。 |

#### 排解提示的哪個部分失敗

很難判斷提示失敗的原因是模型一開始就**不瞭解圖片**，還是瞭解圖片但後續**推理步驟**有誤。如要釐清原因，請要求模型描述圖像內容。

在下列範例中，如果模型回應的點心與茶飲搭配起來似乎很奇怪 (例如爆米花)，您可以先進行疑難排解，判斷模型是否正確辨識出圖片含有茶飲。

| 提示詞 | 提示排解問題 |
| --- | --- |
| 有什麼零食可以在 1 分鐘內完成，而且很適合搭配這道料理？ | 描述這張圖片的內容。 |

另一種策略是要求模型說明推論過程，這有助於縮小推論過程的範圍，找出問題所在。

| 提示詞 | 提示排解問題 |
| --- | --- |
| 有什麼零食可以在 1 分鐘內完成，而且很適合搭配這道料理？ | 有什麼點心可以在 1 分鐘內做好，而且很適合搭配這道菜？請說明原因。 |

## 後續步驟

- 使用 [Google AI Studio](http://aistudio.google.com?hl=zh-tw) 撰寫自己的多模態提示。
- 如要瞭解如何使用 Gemini Files API 上傳媒體檔案並加入提示，請參閱[Vision](https://ai.google.dev/gemini-api/docs/interactions/vision?hl=zh-tw)、[音訊](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=zh-tw)和[文件處理](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=zh-tw)指南。
- 如需提示設計的更多指引 (例如微調取樣參數)，請參閱「[提示策略](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw)」頁面。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-02 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-02 (世界標準時間)。"],[],[]]
