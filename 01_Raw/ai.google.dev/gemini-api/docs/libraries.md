---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=ja
fetched_at: 2026-05-05T20:41:23.912223+00:00
title: "Gemini API \u30e9\u30a4\u30d6\u30e9\u30ea \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API ライブラリ

Gemini API を使用して構築する場合は、**Google GenAI SDK** を使用することをおすすめします。
これらは、プロダクション
レディな公式ライブラリであり、多くの一般的な言語向けに開発、保守されています。[一般提供されており、Google の公式
ドキュメントとサンプルで広く使用されています。](https://ai.google.dev/gemini-api/docs/libraries?hl=ja#new-libraries)

Gemini API を初めて使用する場合は、[クイックスタート ガイド](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja)に沿って開始してください。

## 言語のサポートとインストール

Google GenAI SDK は、Python、JavaScript/TypeScript、Go、Java 言語で利用できます。各言語のライブラリは、パッケージ マネージャーを使用してインストールできます。詳細については、GitHub リポジトリをご覧ください。

### Python

- ライブラリ: [`google-genai`](https://pypi.org/project/google-genai)
- GitHub リポジトリ: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- インストール: `pip install google-genai`

### JavaScript

- ライブラリ: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- GitHub リポジトリ: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- インストール: `npm install @google/genai`

### Go

- ライブラリ: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- GitHub リポジトリ: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- インストール: `go get google.golang.org/genai`

### Java

- ライブラリ: `google-genai`
- GitHub リポジトリ: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- インストール: Maven を使用している場合は、次のものを依存関係に追加します。

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

- ライブラリ: `Google.GenAI`
- GitHub リポジトリ: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- インストール: `dotnet add package Google.GenAI`

## 一般提供

2025 年 5 月の時点で、Google GenAI SDK はサポートされているすべてのプラットフォームで一般提供（GA）に達しており、Gemini API にアクセスするための推奨ライブラリとなっています。
安定しており、本番環境での使用が完全にサポートされ、積極的にメンテナンスされています。
最新の機能にアクセスでき、Gemini と連携して最高のパフォーマンスを発揮します。

以前のライブラリを使用している場合は、移行して最新の機能にアクセスし、Gemini と連携して最高のパフォーマンスを得ることを強くおすすめします。詳細については、[以前のライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja#previous-sdks)のセクションをご覧ください。

## 以前のライブラリと移行

以前のライブラリを使用している場合は、新しいライブラリに
[移行することをおすすめします](https://ai.google.dev/gemini-api/docs/migrate?hl=ja)。

以前のライブラリでは、最近の機能（
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) や [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ja) など）にアクセスできず、
2025 年 11 月 30 日に非推奨となりました。

以前のライブラリのサポート状況はそれぞれ異なります。詳細については、次の表をご覧ください。

| 言語 | 以前のライブラリ | サポート状況 | 推奨ライブラリ |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | 積極的にメンテナンスされていない | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | 積極的にメンテナンスされていない | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | 積極的にメンテナンスされていない | `google.golang.org/genai` |
| **Dart と Flutter** | `google_generative_ai` | 積極的にメンテナンスされていない | [Genkit Dart](https://genkit.dev/docs/dart/get-started/) または [Firebase AI Logic](https://pub.dev/packages/firebase_ai) を使用する |
| **Swift** | `generative-ai-swift` | 積極的にメンテナンスされていない | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ja) を使用する |
| **Android** | `generative-ai-android` | 積極的にメンテナンスされていない | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ja) を使用する |

**Java デベロッパー向けの注:** Gemini API 用の Google 提供のレガシー Java SDK は存在しないため、以前の Google ライブラリからの移行は必要ありません。新しいライブラリから直接開始できます。
[[言語のサポートとインストール](#install)] セクションの

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
