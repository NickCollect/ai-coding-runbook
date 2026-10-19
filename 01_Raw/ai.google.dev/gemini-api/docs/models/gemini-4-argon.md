---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ja
fetched_at: 2026-10-19T05:44:31.700134+00:00
title: "Gemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini 4 Argon

Gemini 4 Argon（`gemini-4-argon`）は、複雑なソフトウェア エンジニアリング、高度な数学的および科学的問題の解決、自律型の多段階エージェント、最大 100 万トークンの長いデコード向けに構築された、Google のフラッグシップ推論モデルです。

[Google AI Studio で試す](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

## ドキュメント

機能、API の変更、移行ガイダンスの詳細については、[最新モデル](https://ai.google.dev/gemini-api/docs/latest-model?hl=ja)のページをご覧ください。

## gemini-4-argon

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | `gemini-4-argon` |
| saveサポートされるデータタイプ | **入力**  テキスト、画像、動画、音声、PDF  **出力**  テキスト |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **コンテキスト ウィンドウ（入力トークンと出力トークンの上限を統合）**  1,048,576  **最大出力**  65,536（デフォルトの同期）/ 最大 1,048,576（[長いデコード](https://ai.google.dev/gemini-api/docs/long-decode?hl=ja)を使用） |
| handyman機能 | **[エージェントによる動画の理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#agentic-video-understanding)**  サポート対象（デフォルトは `static`）  **[音声生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)**  サポート対象外  **[キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**  サポート対象（暗黙的のみ）  注: 明示的なキャッシュ保存はサポートされていません。  **[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)**  サポート対象  **[コンピュータ使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**  サポート対象（プレビュー）  **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**  サポート対象  **[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**  サポート対象  **[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**  サポート対象  **[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)**  サポート対象外  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)**  サポート対象外  **[検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)**  サポート対象  **[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)**  サポート対象  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)**  サポート対象（低、中、高）  **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**  サポート対象 |
| speed使用オプション | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**  サポート対象  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)**  サポート対象  **[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)**  サポート対象 |
| 123 バージョン | 詳細については、[モデル バージョンのパターン](https://ai.google.dev/gemini-api/docs/models?hl=ja#model-versions)をご覧ください。  - 安定版: `gemini-4-argon` |
| calendar\_month最終更新 | 2026 年 10 月 |
| id\_cardモデルカード | [モデルカード](https://deepmind.google/models/model-cards/gemini-4-argon/?hl=ja) |

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-14 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-14 UTC。"],[],[]]
