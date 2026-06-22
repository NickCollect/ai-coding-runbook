---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=ja
fetched_at: 2026-06-22T06:33:09.540140+00:00
title: "Gemini Developer API \u3068 Gemini Enterprise Agent Platform \u306e\u6bd4\u8f03 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini Developer API と Gemini Enterprise Agent Platform の比較

Gemini を使用して生成 AI ソリューションを開発する場合、Google は [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=ja) と [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ja) の 2 つの API プロダクトを提供しています。

Gemini Developer API は、Gemini を活用したアプリケーションの構築、本番環境への移行、スケーリングを迅速に行うための手段です。特定のエンタープライズ コントロールが必要な場合を除き、ほとんどのデベロッパーは Gemini デベロッパー API を使用する必要があります。

Gemini Enterprise Agent Platform は、Google Cloud Platform を基盤とする生成 AI アプリケーションの構築とデプロイのための、エンタープライズ対応の機能とサービスの包括的なエコシステムを提供します。

Google は最近、これらのサービス間の移行を簡素化しました。Gemini Developer API と Gemini Enterprise Agent Platform API の両方に、統合された [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ja) を介してアクセスできるようになりました。

## コードの比較

このページでは、テキスト生成用の Gemini Developer API と Gemini Enterprise Agent Platform のクイックスタートのコードを並べて比較しています。

### Python

Gemini Developer API と Gemini Enterprise Agent Platform の両方のサービスには、`google-genai` ライブラリを介してアクセスできます。`google-genai` のインストール手順については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)のページをご覧ください。

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript と TypeScript

`@google/genai` ライブラリを介して、Gemini Developer API と Gemini Enterprise Agent Platform の両方のサービスにアクセスできます。`@google/genai` のインストール手順については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)のページをご覧ください。

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

`google.golang.org/genai` ライブラリを介して、Gemini Developer API と Gemini Enterprise Agent Platform の両方のサービスにアクセスできます。`google.golang.org/genai` のインストール手順については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)のページをご覧ください。

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### その他のユースケースとプラットフォーム

他のプラットフォームとユースケースについては、[Gemini Developer API ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)と [Gemini Enterprise Agent Platform ドキュメント](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ja)のユースケース固有のガイドをご覧ください。

## 移行に関する考慮事項

移行すると、次のようになります。

- 認証には Google Cloud サービス アカウントを使用する必要があります。詳細については、[Gemini Enterprise Agent Platform のドキュメント](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ja)をご覧ください。
- 既存の Google Cloud プロジェクト（API キーの生成に使用したプロジェクト）を使用することも、[新しい Google Cloud プロジェクトを作成](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ja)することもできます。
- サポートされているリージョンは、Gemini Developer API と Gemini Enterprise Agent Platform API で異なる場合があります。[Google Cloud の生成 AI でサポートされているリージョン](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=ja)のリストをご覧ください。
- Google AI Studio で作成したモデルは、Gemini Enterprise Agent Platform で再トレーニングする必要があります。

Gemini Developer API で Gemini API キーを使用する必要がなくなった場合は、セキュリティのベスト プラクティスに従ってキーを削除します。

API キーを削除するには:

1. [Google Cloud API 認証情報](https://console.cloud.google.com/apis/credentials?hl=ja)ページを開きます。
2. 削除する API キーを見つけて、[**操作**] アイコンをクリックします。
3. [**API キーを削除**] を選択します。
4. [**認証情報の削除**] モーダルで、[**削除**] を選択します。

   API キーの削除が反映されるまでには数分かかることがあります。削除が反映されると、以降その API キーを使ったトラフィックはすべて拒否されます。

## 次のステップ

- Gemini Enterprise Agent Platform の生成 AI ソリューションの詳細については、[Gemini Enterprise Agent Platform の生成 AI の概要](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-18 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-18 UTC。"],[],[]]
