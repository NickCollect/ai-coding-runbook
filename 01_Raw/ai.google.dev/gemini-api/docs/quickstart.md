---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-TW
fetched_at: 2026-05-11T05:05:52.576492+00:00
title: "Gemini API \u5feb\u901f\u5165\u9580\u5c0e\u89bd\u8ab2\u7a0b \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini API 快速入門導覽課程

本快速入門導覽課程說明如何安裝[程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)，並發出第一個 Gemini API 要求。

## 事前準備

使用 Gemini API 時需要 API 金鑰，您可以免費建立金鑰，然後開始使用。

[建立 Gemini API 金鑰](https://aistudio.google.com/app/apikey?hl=zh-tw)

## 安裝 Google GenAI SDK

### Python

使用 [Python 3.9 以上版本](https://www.python.org/downloads/)，透過下列 [pip 指令](https://packaging.python.org/en/latest/tutorials/installing-packages/)安裝 [`google-genai` 套件](https://pypi.org/project/google-genai/)：

```
pip install -q -U google-genai
```

### JavaScript

使用 [Node.js v18 以上版本](https://nodejs.org/en/download/package-manager)，透過下列 [npm 指令](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)安裝 [Google Gen AI SDK for TypeScript and JavaScript](https://www.npmjs.com/package/@google/genai)：

```
npm install @google/genai
```

### Go

在模組目錄中，使用 [go get 指令](https://go.dev/doc/code)安裝 [google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai)：

```
go get google.golang.org/genai
```

### Java

如果您使用 Maven，可以將下列項目新增至依附元件，安裝 [google-genai](https://github.com/googleapis/java-genai)：

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

使用 [dotnet add 指令](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add)，在模組目錄中安裝 [googleapis/go-genai](https://googleapis.github.io/dotnet-genai/)

```
dotnet add package Google.GenAI
```

### Apps Script

1. 如要建立新的 Apps Script 專案，請前往 [script.new](https://script.google.com/u/0/home/projects/create?hl=zh-tw)。
2. 按一下「未命名的專案」。
3. 將 Apps Script 專案重新命名為「AI Studio」，然後按一下「重新命名」。
4. 設定 [API 金鑰](https://developers.google.com/apps-script/guides/properties?hl=zh-tw#manage_script_properties_manually)
   1. 按一下左側的「專案設定」圖示 ![專案設定圖示](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg)。
   2. 在「指令碼屬性」下方，按一下「新增指令碼屬性」。
   3. 在「Property」(屬性) 中輸入金鑰名稱：`GEMINI_API_KEY`。
   4. 在「Value」(值) 部分輸入 API 金鑰的值。
   5. 按一下「儲存指令碼屬性」。
5. 將 `Code.gs` 檔案內容替換成下列程式碼：

## 發出第一項要求

以下範例使用 [`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-tw#method:-models.generatecontent) 方法，透過 Gemini 2.5 Flash 模型傳送要求至 Gemini API。

如果您[將 API 金鑰設為](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#set-api-env-var)環境變數 `GEMINI_API_KEY`，使用 [Gemini API 程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)時，用戶端會自動擷取該金鑰。否則，您需要在初始化用戶端時[傳遞 API 金鑰](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#provide-api-key-explicitly)做為引數。

請注意，Gemini API 文件中的所有程式碼範例，都假設您已設定環境變數 `GEMINI_API_KEY`。

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

## 後續步驟

您已發出第一項 API 要求，現在不妨參考下列指南，瞭解 Gemini 的實際運作方式：

- [生成文字](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw)
- [圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)
- [圖像解讀](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-tw)
- [思考型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)
- [函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)
- [長篇脈絡資訊](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw)
- [嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-07 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-07 (世界標準時間)。"],[],[]]
