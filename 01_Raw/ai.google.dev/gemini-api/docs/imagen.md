---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=ja
fetched_at: 2026-10-26T05:48:00.965356+00:00
title: "Imagen \u3092\u4f7f\u7528\u3057\u3066\u753b\u50cf\u3092\u751f\u6210\u3059\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)

フィードバックを送信

# Imagen を使用して画像を生成する

Imagen は Google の以前の画像生成モデルです。この機能は現在シャットダウンされており、Gemini API では利用できなくなっています。

## Nano Banana に移行する

画像生成用の Nano Banana に移行します。

- **モデル名**: Imagen モデル名の代わりに `gemini-2.5-flash-image`（または `gemini-3.1-flash-image` などの Nano Banana 2 モデル）を使用します。
- **メソッド**: `client.models.generate_images` ではなく `client.models.generate_content` を使用します。
- **レスポンスの処理**: Nano Banana は、特定の画像レスポンス オブジェクトではなく、画像データを含むコンテンツ部分を返します。

詳細と例については、[画像生成ガイド](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-18 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-18 UTC。"],[],[]]
