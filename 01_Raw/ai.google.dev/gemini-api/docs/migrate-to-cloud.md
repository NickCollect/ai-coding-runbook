---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=ja
fetched_at: 2026-10-26T05:46:16.816316+00:00
title: "Gemini Developer API \u3068 Gemini \u30d7\u30e9\u30c3\u30c8\u30d5\u30a9\u30fc\u30e0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini Developer API と Gemini プラットフォーム

Gemini を使用して生成 AI ソリューションを開発する場合、Google は [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=ja) と [Gemini プラットフォーム API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ja) の 2 つの API プロダクトを提供しています。

Gemini Developer API は、Gemini を活用したアプリケーションの構築、本番環境への移行、スケーリングを最速で実現します。特定のエンタープライズ コントロールが必要な場合を除き、ほとんどのデベロッパーは Gemini Developer API を使用する必要があります。

Gemini プラットフォームは、Google Cloud を基盤とする生成 AI アプリケーションの構築とデプロイのための、エンタープライズ対応の機能とサービスの包括的なエコシステムを提供します。

最近、これらのサービス間の移行を簡素化しました。Gemini Developer API と Gemini プラットフォーム API の両方に、統合された [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ja) と [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) を介してアクセスできるようになりました。

## コードの比較: Interactions API（推奨）

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) は、Gemini モデルとエージェントを使用して構築する場合に推奨される方法です。次の例では、Gemini Developer API と Gemini プラットフォーム間のテキスト生成を比較しています。

### Python

`google-genai` ライブラリ（`>= 2.3.0`）を介して、Gemini Developer API と Gemini プラットフォーム サービスの両方にアクセスできます。`google-genai` のインストール方法については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja) ページをご覧ください。

### Gemini Developer API

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### Gemini プラットフォーム API

```
from google import genai

client = genai.Client(
    enterprise=True, project="your-project-id", location="global"
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### JavaScript と TypeScript

`@google/genai` ライブラリ（`>= 2.3.0`）を介して、Gemini Developer API と Gemini プラットフォーム サービスの両方にアクセスできます。`@google/genai` のインストール方法については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja) ページをご覧ください。

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### Gemini プラットフォーム API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  enterprise: true,
  project: "your_project",
  location: "global",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

## コードの比較: generateContent API

新しいプロジェクトには Interactions API をおすすめしますが、`generateContent` API も引き続きサポートされます。

### Python

Gemini Developer API と Gemini プラットフォーム サービスの両方に、`google-genai` ライブラリからアクセスできます。`google-genai` のインストール手順については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)のページをご覧ください。

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini プラットフォーム API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript と TypeScript

`@google/genai` ライブラリを介して、Gemini Developer API と Gemini プラットフォーム サービスの両方にアクセスできます。`@google/genai` のインストール手順については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)のページをご覧ください。

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini プラットフォーム API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

`google.golang.org/genai` ライブラリを介して、Gemini Developer API と Gemini プラットフォーム サービスの両方にアクセスできます。`google.golang.org/genai` のインストール手順については、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)のページをご覧ください。

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
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini プラットフォーム API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google Cloud project
const project = "your-project"

// A Google Cloud location like "us-central1"
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
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### その他のユースケースとプラットフォーム

他のプラットフォームとユースケースについては、[Gemini Developer API ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)と [Gemini プラットフォーム ドキュメント](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ja)のユースケース固有のガイドをご覧ください。

## 移行に関する考慮事項

移行すると、次のようになります。

- 認証には Google Cloud サービス アカウントを使用する必要があります。詳細については、[Gemini プラットフォームのドキュメント](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ja)をご覧ください。
- 既存の Google Cloud プロジェクト（API キーの生成に使用したプロジェクト）を使用することも、[新しい Google Cloud プロジェクトを作成](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ja)することもできます。
- サポート対象の地域は、Gemini Developer API と Gemini プラットフォーム API で異なる場合があります。プレビュー期間中、[Gemini プラットフォームの Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=ja) は `global` エンドポイント（`location="global"`）のみをサポートします。[Google Cloud の生成 AI でサポート対象の地域](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=ja)のリストをご覧ください。
- Google AI Studio で作成したモデルは、Gemini プラットフォームで再トレーニングする必要があります。

Gemini Developer API で Gemini API キーを使用する必要がなくなった場合は、セキュリティのベスト プラクティスに従ってキーを削除します。

API キーを削除するには:

1. [Google Cloud API 認証情報](https://console.cloud.google.com/apis/credentials?hl=ja)ページを開きます。
2. 削除する API キーを見つけて、[**操作**] アイコンをクリックします。
3. [**API キーを削除**] を選択します。
4. [**認証情報の削除**] モーダルで、[**削除**] を選択します。

   API キーの削除が反映されるまでには数分かかることがあります。削除が反映されると、以降その API キーを使ったトラフィックはすべて拒否されます。

## 次のステップ

- [Gemini プラットフォームの Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=ja) デベロッパー ガイドをご覧ください。
- Gemini プラットフォームの生成 AI ソリューションの詳細については、[Gemini プラットフォームの生成 AI の概要](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-08 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-08 UTC。"],[],[]]
