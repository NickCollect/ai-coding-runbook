---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=ja
fetched_at: 2026-07-20T04:44:46.784551+00:00
title: "Gemini API \u3067\u306e\u52d5\u753b\u751f\u6210 \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API での動画生成

Gemini API には、動画を生成するための 2 つのモデル（[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ja) と [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=ja)）があります。それぞれ異なるワークフロー向けに設計されています。

動画生成のデフォルト モデルとして Gemini Omni Flash を使用します。優れた動画のコヒーレンス、マルチ入力推論（テキスト、画像、音声、動画の入力を同時にサポート）、キャラクターの一貫性、事実の正確性、マルチターンの会話型編集（要素の置換や視点の変更など）を実現します。シーン拡張、最終フレーム制御、レガシー パイプラインとの統合などの特定の機能が必要な場合は、Veo 3.1 を使用します。

## Gemini Omni Flash

Gemini Omni Flash は、動画生成と会話型動画編集のための高速なマルチモーダル モデルです。テキスト プロンプトや画像を短い動画にすばやく変換することに優れており、Interactions API を使用して複数のターンで結果を絞り込むことができます。

[Gemini Omni Flash を使ってみる →](https://ai.google.dev/gemini-api/docs/omni?hl=ja)

## Veo 3.1

Veo 3.1 は、ネイティブ音声を含む動画を生成するモデルです。`generateContent` API を通じて、動画拡張、フレーム固有の生成、画像ベースの方向などの機能をサポートしています。

[Veo 3.1 を使ってみる →](https://ai.google.dev/gemini-api/docs/veo?hl=ja)

## 動画理解

新しい動画を生成するのではなく、既存の動画コンテンツを取り込んで分析する必要がある場合は、[動画理解ガイド](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-30 UTC。"],[],[]]
