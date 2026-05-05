---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=ja
fetched_at: 2026-05-05T20:49:14.118453+00:00
title: "Gemini API \u306e\u30af\u30a4\u30c3\u30af\u30b9\u30bf\u30fc\u30c8 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API のクイックスタート

このクイックスタートでは、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)
をインストールして最初の Gemini API リクエストを行う方法について説明します。

## 始める前に

Gemini API を使用するには API キーが必要です。API キーは無料で作成できます。

[Gemini API キーを作成する](https://aistudio.google.com/app/apikey?hl=ja)

## Google GenAI SDK をインストールする

### Python

[Python 3.9+](https://www.python.org/downloads/) 以降を使用して、次の
[pip コマンド](https://packaging.python.org/en/latest/tutorials/installing-packages/)で
[`google-genai` パッケージ](https://pypi.org/project/google-genai/)をインストールします。

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager) 以降を使用して、次の [npm コマンド](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)で [TypeScript と JavaScript 用の Google Gen AI SDK](https://www.npmjs.com/package/@google/genai) をインストールします。

```
npm install @google/genai
```

### Go

[go get コマンドを使用して、モジュール ディレクトリに
[google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai) をインストールします。](https://go.dev/doc/code)

```
go get google.golang.org/genai
```

### Java

Maven を使用している場合は、依存関係に次のものを追加して
[google-genai](https://github.com/googleapis/java-genai)をインストールできます。

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

[dotnet add コマンドを使用して、モジュール ディレクトリに
[googleapis/go-genai](https://googleapis.github.io/dotnet-genai/) をインストールします。](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add)

```
dotnet add package Google.GenAI
```

### Apps Script

1. 新しい Apps Script プロジェクトを作成するには、
   [script.new](https://script.google.com/u/0/home/projects/create?hl=ja) に移動します。
2. [**無題のプロジェクト**] をクリックします。
3. Apps Script プロジェクトの名前を **AI Studio** に変更して、[**名前を変更**] をクリックします。
4. [API キー](https://developers.google.com/apps-script/guides/properties?hl=ja#manage_script_properties_manually)を設定する
   1. 左側の [**プロジェクトの設定**] ![プロジェクト設定のアイコン](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg) をクリックします。
   2. [**スクリプト プロパティ**] で [**スクリプト プロパティを追加**] をクリックします。
   3. [**プロパティ**] にキー名 `GEMINI_API_KEY` を入力します。
   4. [**\*\*値\*\***] に API キーの値を入力します。
   5. [**スクリプト プロパティを保存**] をクリックします。
5. `Code.gs` ファイルの内容を次のコードに置き換えます。

## 最初のリクエストを送信する

Gemini 2.5 Flash モデルを使用して Gemini API にリクエストを送信する
[`generateContent`](https://ai.google.dev/api/generate-content?hl=ja#method:-models.generatecontent) メソッド
を使用する例を次に示します。

API キーを[環境変数 `GEMINI_API_KEY`として](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#set-api-env-var)設定すると、
Gemini API ライブラリを[使用するときにクライアントによって](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)自動的に取得されます。
[それ以外の場合は、クライアントを初期化するときに API キーを引数として渡す必要があります。](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#provide-api-key-explicitly)

Gemini API ドキュメントのすべてのコードサンプルでは、環境変数 `GEMINI_API_KEY` が設定されていることを前提としています。

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
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
)

func main() {
    ctx := context.Background()
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    // The client gets the API key from the environment variable `GOOGLE_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## 次のステップ

最初の API リクエストが完了したので、Gemini の動作を示す次のガイドをご覧ください。

- [テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja)
- [画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)
- [画像理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)
- [思考モード](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)
- [長いコンテキスト](https://ai.google.dev/gemini-api/docs/long-context?hl=ja)
- [エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
