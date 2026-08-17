---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/files?hl=ja
fetched_at: 2026-08-17T02:26:30.474877+00:00
title: "Files API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Files API

Gemini は、テキスト、画像、音声など、さまざまな種類の入力データを同時に処理できます。

このガイドでは、Files API を使用してメディア ファイルを操作する方法について説明します。音声ファイル、画像、動画、ドキュメント、その他のサポートされているファイル形式の基本的な操作は同じです。

ファイル プロンプトのガイダンスについては、[ファイル プロンプト ガイド](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide)をご覧ください。

## ファイルをアップロード

Files API を使用してメディア ファイルをアップロードできます。リクエストの合計サイズ（ファイル、テキスト プロンプト、システム指示などを含む）が 100 MB を超える場合は、常に Files API を使用します。PDF ファイルの上限は 50 MB です。

次のコードは、ファイルをアップロードしてから、`generateContent` の呼び出しでそのファイルを使用します。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
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

resp, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", []*genai.Content{
  {
    Parts: []*genai.Part{
      genai.NewPartFromFile(*file),
      genai.NewPartFromText("Describe this audio clip"),
    },
  },
}, nil)

if err != nil {
    log.Fatal(err)
}

printResponse(resp)
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## ファイルのメタデータを取得する

`files.get` を呼び出すことで、API がアップロードされたファイルを正常に保存し、そのメタデータを取得したことを確認できます。

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

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await ai.files.get({ name: fileName });
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
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/files/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## アップロードされたファイルを一覧表示する

次のコードは、アップロードされたすべてのファイルのリストを取得します。

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

const ai = new GoogleGenAI({});

async function main() {
  const listResponse = await ai.files.list({ config: { pageSize: 10 } });
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

## アップロードしたファイルを削除する

ファイルは 48 時間後に自動的に削除されます。アップロードしたファイルを手動で削除することもできます。

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

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await ai.files.delete({ name: fileName });
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
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/files/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 使用状況情報

Files API を使用して、メディア ファイルをアップロードし、操作できます。Files API を使用すると、プロジェクトごとに最大 20 GB のファイルを保存できます。ファイルごとの最大サイズは 2 GB です。ファイルは 48 時間保存されます。この間、API を使用してファイルに関するメタデータを取得することはできますが、ファイルをダウンロードすることはできません。Files API は、Gemini API が利用可能なすべてのリージョンで無料で利用できます。

## ファイル プロンプト戦略

このセクションでは、Gemini API のプロンプトでメディア ファイルを使用するためのガイダンスとベスト プラクティスについて説明します。

プロンプトでさまざまな種類のデータを使用できるため、Gemini API で処理できるタスクの柔軟性が高まります。たとえば、おいしい食事の写真をモデルに送信し、その食事に関する短いブログ記事を作成するよう依頼できます。

|  |  |
| --- | --- |
| **プロンプト** | **レスポンス** |
| この写真に基づいて、魅力的な短いブログ投稿を書いてください。写真に写っている食事の説明と、私がミールプレップ（食事の作り置き）を始めた経緯について説明する必要があります。   クッキー | ミールプレップは、時間とお金の節約に役立ち、健康的な食事にもつながります。この食事は、事前に簡単に準備できる、健康的でおいしい食事の好例です。  この食事は、玄米、焼き野菜、鶏肉の照り焼きが特徴です。玄米は、持続的なエネルギーを供給する健康的で複合的な炭水化物です。焼き野菜は、1 日に必要なビタミンとミネラルを摂取するのに最適です。鶏肉の照り焼きは、おいしくてタンパク質が豊富なオプションです。  この食事は準備も簡単です。玄米を炊き、野菜をローストし、鶏肉の照り焼きを作ります。すべて調理したら、食事の準備用容器に分けて冷蔵庫に保管します。忙しい朝に、容器を持って出かけることができます。  健康的で美味しい食事を簡単に準備したいなら、この食事がおすすめです。栄養と風味がたっぷり詰まっており、満腹感と満足感が得られます。  健康的でおいしいミールプレップを楽しみましょう。 |

メディア ファイルを使用するプロンプトから目的の出力を取得できない場合は、目的の結果を得るために役立つ戦略がいくつかあります。以降のセクションでは、マルチモーダル入力を使用するプロンプトを改善するための設計アプローチとトラブルシューティングのヒントについて説明します。

マルチモーダル プロンプトは、次のベスト プラクティスに沿って改善できます。

- ### [プロンプト設計の基礎](#specific-instructions)

  - **指示を具体的にする**: 誤解を招かないように明確で簡潔な指示を記述します。
  - **プロンプトにいくつかの例を加える:** 現実的な数個の例を使用して実現したいことを示します。
  - **小さいステップに分ける**: 複雑なタスクを扱いやすい中間目標に分割して、プロセスに沿ってモデルを導きます。
  - **出力形式を指定する**: プロンプトで、必要とする形式（マークダウン、JSON、HTML など）で出力することを指示します。
  - **単一画像のプロンプトではまず画像を配置する**: Gemini は、画像とテキストの入力をどのような順序でも処理できますが、単一画像のプロンプトの場合は、対象の画像（または動画）をテキストのプロンプトよりも前に配置することでパフォーマンスが向上する可能性があります。ただし、その画像がテキストと複雑に絡み合っている場合は、最も自然に意味を捉えることができる順序を使用してください。
- ### [マルチモーダル プロンプトのトラブルシューティング](#troubleshooting)

  - **モデルが画像の該当箇所から情報を抽出していない場合:** プロンプトで画像のどの部分から情報を引き出してほしいかについてのヒントを出してください。
  - **モデルの出力内容が一般的すぎる（入力した画像 / 動画に十分対応していない）場合:** プロンプトの冒頭で、タスクの指示を出す前にモデルに画像や動画について説明するよう求めるか、画像の内容に言及するよう求めてみてください。
  - **失敗した部分のトラブルシューティングを行うには:** モデルの最初の理解度を測るために、モデルに画像の説明を求めるか、モデルに推論についての説明を求めます。
  - **プロンプトによりハルシネーションが生じたコンテンツが生成された場合:** 温度設定を下げるか、モデルに短い説明を求め、追加の詳細情報が推定されないようにしてみます。
  - **サンプリング パラメータのチューニング:** さまざまな Temperature 設定と Top-K 選択を試して、モデルの創造性を調整します。

### 指示を具体的にする

プロンプトは、明確かつ詳細である場合に最も良い結果が出ます。特定の出力を想定している場合は、必要な出力を確実に得られるように、その要件をプロンプトに含めることをおすすめします。

下に示す空港の発着表示板の画像の場合、「この画像について説明する」ようにモデルにリクエストすると、漠然とした説明が生成される可能性があります。モデルによって画像から時刻と都市が抽出されることを必要とする場合は、そのリクエストをプロンプトに直接追加します。

| プロンプト | モデルのレスポンス |
| --- | --- |
| この画像を説明してください。 | この画像は、空港の発着表示板を示しています。 |

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| 運行時刻表 この画像にある空港の発着表示板の時刻と都市を抽出してリストにしてください。 | - 10:50 モスクワ - 11:05 エディンバラ - 11:05 ロンドン - 11:10 ブカレスト - 11:30 キーウ - 11:35 ダブリン - 11:45 イースト ミッドランズ - 12:15 ソフィア - 12:30 ロンドン - 12:30 ニューカッスル - 12:40 サンクトペテルブルク - 12:40 ロンドン - 12:45 マンチェスター |

### 例をいくつか追加する

この Gemini モデルはさまざまな入力を受け付け、その入力を例として使用するとユーザーが必要とする出力を理解できます。こうした例を追加することでモデルがパターンを識別できるようになり、指定された画像と回答の関係を新しい例に適用できます。これは「少数ショット」学習とも呼ばれます。

下の例では、最初の出力が文章形式で記述されており、国（ブラジル）も含まれています。別の形式やスタイルで出力し、国ではなく都市のみを出力したいとします。プロンプトに少数ショットの例を追加すると、モデルを意図したとおりに応答するように誘導できます。

| **プロンプト** | **モデルのレスポンス** |
| --- | --- |
| 運行時刻表 ランドマークに一致する都市を特定してください。 | このランドマークは、ブラジルのリオデジャネイロにあるコルコバードのキリスト像です。 |

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| ランドマークに一致する都市を特定してください。 コロッセオ | 都市: ローマ、ランドマーク: コロッセオ。 |
| 紫禁城 | 都市: 北京、ランドマーク: 紫禁城 |
| 紫禁城 | 都市: リオデジャネイロ、ランドマーク: コルコバードのキリスト像 |

### 順を追って説明する

視覚的な理解と推論の両方を必要とするような複雑なタスクの場合は、タスクをより小さく、より簡単なステップに分割することが有効です。また、プロンプトの中でモデルに直接「順を追って考える」ように指示することも効果的な場合があります。

| プロンプト | モデルのレスポンス |
| --- | --- |
| トイレット ペーパーは、いつ使い切りますか？ | 間もなくです。あと 3 ロールしかありません。 |

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| 1. まず、この写真に写っているトイレット ペーパーのロールを数えてください。  2. 次に、標準的な人が 1 日に使用するトイレット ペーパーの量を定めます。  3. そのトイレット ペーパーがどのくらいの期間使用できるかを算出します。 | 1. この写真には、トイレット ペーパーのロールが 3 つ写っています。  2. 標準的な人は、1 日に約 20 枚のトイレット ペーパーを使用します。  3. 1 ロールに 200 枚入っているとすると、1 ロールで約 10 日間使用できます。したがって、3 ロールでは約 1 か月使用できます。 |

数学の問題や他の種類の言葉の問題は、モデルに順を追って考えることを求めるのに適しています。

| **プロンプト** | **レスポンス** |
| --- | --- |
| 数列の第 4 項は何ですか？ | -135 |

モデルからのレスポンスが正しくありません。これを改善するには、プロンプトに答える前に問題を解析するようにモデルに求める方法があります。

| **プロンプト** | **レスポンス** |
| --- | --- |
| まず、画像内の数式を解析します。  次に、数式に基づいて、「数列の第 4 項は何ですか？」に答えます。 | クリックして結果を拡大 $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. n = 4 を式に代入します。  $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. b(3) の値がわからないため、式に n = 3 を代入します。  $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. b(2) の値がわからないため、式に n = 2 を代入します。  $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. b(1) の値は 15 であるとわかっているため、それを式に代入します。  $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. b(2) の値がわかったので、それを b(3) の式に代入します。  $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. b(3) の値がわかったので、それを b(4) の式に代入します。  $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   したがって、数列の第 4 項は -405 です。 |

このモデルのレスポンスは正確ですが、レスポンスをさらに合理化するには、モデルに順を追って考えるように依頼します。

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| 数列の第 4 項は何ですか？順を追って考えてください。 | 最初の項は 15 です。  第 2 項は、b(1) × (-3) = 15 × (-3) = -45 です。  第 3 項は、b(2) × (-3) = -45 × (-3) = 135 です。  第 4 項は、b(3) × (-3) = 135 × (-3) = -405 です。 |

### 出力形式を指定する

よくある問題は、モデル出力を特定の形式（マークダウン、JSON、HTML など）にする必要があることです。特に、モデルの出力を下流のタスクで取り込む必要がある場合に発生します。プロンプトの中でモデルにそのように指示することで、その形式での出力を試みることができます。以下に 2 つの例を示します。

| プロンプト | モデルのレスポンス |
| --- | --- |
| この画像の表を解析してマークダウン形式に変換してください。 | | 科目 | ステータス | 時間 | 開始日 | 期限 |  | ------- | ------ | ---- | ---------- | ------ |  | 数学 | 完了 | 1.5 時間 | 2023 年 11 月 29 日 | 2023 年 12 月 1 日 |  | 地理 | 完了 | 30 分 | 2023 年 12 月 2 日 | 2023 年 12 月 4 日 |  | 物理 | 進行中 | 2 時間 | 2023 年 12 月 3 日 | 2023 年 12 月 5 日 |  | 生物 | 未開始 | 6 時間 | 2016 年 11 月 2 日 | 2023 年 12 月 6 日 | |

| **プロンプト** | **モデルのレスポンス** |
| --- | --- |
| 次の属性をすべてリストアップしてください。  材料、料理の種類、ベジタリアンかどうか、JSON 形式 | ```` ```json ````  `{`  `"ingredients": [`  `"rice",`  `"shrimp",`  `"clams",`  `"mussels",`  `"peas",`  `"tomatoes",`  `"onions",`  `"garlic",`  `"olive oil",`  `"paprika",`  `"salt",`  `"pepper"`  `],`  `"type of cuisine": "Spanish",`  `"vegetarian": false`  `}`  ```` ``` ```` |

### 単一画像のプロンプトではまず画像を配置する

Gemini は、プロンプト内の画像とテキストをどのような順序でも解釈できますが、テキスト プロンプトの前に画像を 1 つ配置するとより良い結果が得られる場合があります。以下の例では、それぞれのプロンプトにおいて、テキストの前に画像があることを確認できます。

### マルチモーダル プロンプトのトラブルシューティング

役に立つ回答が得られない場合は、プロンプトのトラブルシューティングが必要になることがあります。以下にいくつかの方法を示します。

#### モデルが画像の該当部分から情報を引き出していない場合

より具体的なレスポンスを得るには、プロンプトへのレスポンスに必要な情報を、画像のどの部分から引き出すかを指定します。

| プロンプト | モデルのレスポンス |
| --- | --- |
| このおむつは赤ちゃんに何日使えますか？ | おむつは、なくなるまで 198 日使用できます。 |

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| この紙おむつは、どのくらいで使い切りますか？  箱に記載されている体重から子どもの年齢を割り出し、箱に入っているおむつの総数を使用してください。  合計数を、子どもが 1 日あたりに使用するおむつの数で割ってください。 | 箱には 198 枚のおむつが入っています。箱には、おむつが 22～37 ポンドの子ども用であると書かれています。  この体重の範囲にある子どもの平均年齢は 1～2 歳であると考えられます。  通常、2 歳の子どもは 1 日あたり 6 枚のおむつを使用するため、おむつは約 33 日間（198÷6）使用できます。 |

#### モデル出力が漠然としすぎて、画像の入力に十分対応できない場合

モデルが画像に対するレスポンスを調整できるように、推論タスクを実行する前に、画像について説明するように求めてみます。

| プロンプト | モデルのレスポンス |
| --- | --- |
| これらの画像の共通点は何ですか？ | 4 枚の画像はいずれも風景写真のサンプルです。 |

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| まず、それぞれの画像の内容を詳しく説明してください。これらの画像の共通点は何ですか？ | 1 つ目の画像にはスーツケースに荷物を詰めている人物が写っています。2 つ目の画像にはショッピング モールの何もない廊下が写っています。3 つ目の画像にはトイレット ペーパーが写っています。4 つ目の画像には暗く荒れ狂う海が写っています。  これらの画像の共通点は、どれもリミナル スペースの例であるということです。リミナル スペースとは、他の 2 つの場所や状況の間にある場所や状況のことです。多くの場合、不確実性やあいまいさによって特徴付けられます。  1 つ目の画像は、自宅にいるときと旅行中の人物を写しています。2 つ目の画像は 2 つの店舗の間にある廊下が写されています。3 つ目の画像はトイレット ペーパーの画像で、バスルームの可能性もあります。トイレは、プライベートなスペースと共用スペースの間の過渡的なスペースです。そこは、外の世界に出入りするための準備をする場所です。  4 つ目の画像は、凪の状態と嵐の状態の間にある海を示しています。  リミナル スペースは刺激的でもあり、不安でもあります。新たな始まりの場所にもなれば、終わりの場所にもなります。内省の場所にもなれば、行動の場所にもなります。 |

また、画像の内容に言及するように明示的にモデルに指示することもできます。

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| これらの画像の共通点は何ですか？レスポンスでは、画像の内容を参考にしてください。 | 画像はすべて旅行に関連しています。1 つ目の画像にはスーツケースに荷物を詰めている人物が写っています。2 つ目の画像にはショッピング モールの何もない廊下が写っています。3 つ目の画像には積み重ねたトイレット ペーパーが写っています。4 つ目の画像には暗く荒れ狂う海が写っています。  これらの画像はすべて、人々が旅行するときに必要なもの、または使用するものであるため、すべて旅行に関連しています。1 つ目の画像には、スーツケースに荷物を詰めている人が写っています。これは、旅行に出かける人が行うことです。2 つ目の画像には、ショッピング モール内の何もない廊下が写っています。ショッピング モールは、旅行用品を購入するために訪れることが多い場所です。3 つ目の画像には、積み重ねたトイレット ペーパーが写っています。トイレット ペーパーは、人が旅行中によく使用するものです。4 つ目の画像には、暗い荒れ狂う海が写っています。これは、人が旅行中によく遭遇する場面です。 |

画像からクリエイティブな出力を得る場合も、同じアプローチが有効です。ウサギを使った次の例では、画像の特徴を含めるようにモデルに明示的に依頼すると、出力を改善できます。

| プロンプト | モデルのレスポンス |
| --- | --- |
| この画像について詩を書いてもらえますか？ | 柔らかくて茶色い小さなウサギ、 野原を飛び跳ね、上へ下へ。  耳はとても長く、しっぽはとても小さい、  君は一番かわいい生き物だ。  君は草をかじってる、とても青々としていて甘い、 私を見たらぴょんぴょん跳ねて逃げて行ったね。  でも私はいつも君の友だち。  小さなウサギさんが生きている限り。 |

| **更新されたプロンプト** | **改善されたレスポンス** |
| --- | --- |
| この画像について、叙述的で印象的な詩を書き、場所も含めてもらえますか？ | 草原にいる小さなウサギ、 長い耳、鋭い耳。 何を見ているの？ 遠くを見つめて。  それは海の青、 太陽に照らされて輝く海か？ それとも打ち寄せて響く波、 そのリズムに夢中なの？  小さいウサギさん、本当のことを教えてください、 君の心を捉えるものは？ 潮風、 それとも楽しいカモメの鳴き声かい？  きっと、あらゆる存在の壮大さだね、 とても大きくて小さな世界。 夢が広がる場所、 冒険の種がまかれる場所。  小さなウサギさん、どんな夢を見ているの？ 草の上に座って、とても穏やかに。 深い穴を掘りたいの？ それとも飛び跳ねられる大地にいたいの？  君の夢が何であれ、小さいウサギさん、 明るく輝く不思議さをなくさないでね。 夢と願望の中に、 君の創造を待っている世界があるから。 |

#### プロンプトの失敗した部分に対するトラブルシューティング

プロンプトが失敗したのは、モデルがそもそも**画像を理解**していなかったからなのか、それとも画像は理解していたものの、その後に正しい**推論の手順**を実行しなかったからなのかを判断することは困難です。このような理由を見極めるには、画像に何が写っているかを説明するようモデルに指示します。

次の例では、お茶と組み合わせると意外に思えるおやつ（ポップコーンなど）をモデルが返す場合に、まずトラブルシューティングを行い、画像にお茶が含まれていることをモデルが正しく認識しているかどうかを判断します。

| プロンプト | トラブルシューティング用のプロンプト |
| --- | --- |
| 1 分で作ることができるおやつで、これに合うものは何ですか？ | この画像にあるものを説明してください。 |

もう 1 つの方法は、モデルにその推論を説明してもらうことです。そうすることで、推論が破綻した部分を絞り込むことができます。

| プロンプト | トラブルシューティング用のプロンプト |
| --- | --- |
| 1 分で作ることができるおやつで、これに合うものは何ですか？ | 1 分で作ることができるおやつで、これに合うものは何ですか？理由を説明してください。 |

## 次のステップ

- [Google AI Studio](http://aistudio.google.com?hl=ja) を使用して、独自のマルチモーダル プロンプトを作成してみましょう。
- Gemini Files API を使用してメディア ファイルをアップロードし、プロンプトに含める方法については、[Vision](https://ai.google.dev/gemini-api/docs/vision?hl=ja)、[音声](https://ai.google.dev/gemini-api/docs/audio?hl=ja)、[ドキュメント処理](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)の各ガイドをご覧ください。
- サンプリング パラメータのチューニングなど、プロンプト設計に関するその他のガイダンスについては、[プロンプト戦略](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)のページをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
