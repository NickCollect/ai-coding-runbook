---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-preview?hl=ja
fetched_at: 2026-11-02T07:17:48.860289+00:00
title: "Gemini Robotics ER 2 \u30d7\u30ec\u30d3\u30e5\u30fc\u7248 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini Robotics ER 2 プレビュー版

Gemini Robotics ER 2 は、テキスト、画像、動画、音声の入力を受け入れるロボット工学向けの視覚言語モデル（VLM）です。空間推論、動画理解、エージェント型コード実行、マルチステップ ツール オーケストレーション、マルチロボット調整をサポートしています。

[Google AI Studio で試す](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=ja)

## ドキュメント

機能と性能の詳細については、[ロボティクス](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ja)のページをご覧ください。

## gemini-robotics-er-2-preview

### Gemini Robotics ER 2 プレビュー

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | `gemini-robotics-er-2-preview` |
| saveサポートされるデータタイプ | **入力**  テキスト、画像、動画、音声  **出力**  テキスト |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  131,072  **出力トークンの上限**  65,536 |
| handyman機能 | **[音声生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)**  サポート対象外  **[キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**  サポート対象  **コード実行**  サポート対象  **[コンピュータ使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**  サポート対象  **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**  サポート対象  **[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**  サポート対象  **[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**  サポート対象  **[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)**  サポート対象外  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)**  サポート対象外  **[検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)**  サポート対象  **[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)**  サポート対象  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)**  サポート対象  **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**  サポート対象 |
| speed使用オプション | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**  サポート対象  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)**  サポート対象外  **[優先度推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)**  サポート対象外 |
| 123 バージョン | 詳細については、[モデル バージョン パターン](https://ai.google.dev/gemini-api/docs/models?hl=ja#model-versions)をご覧ください。  - プレビュー: `gemini-robotics-er-2-preview` |
| calendar\_month最終更新 | 2026 年 7 月 |
| id\_cardモデルカード | [モデルカード](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ja) |
| paid料金 | [料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#gemini-robotics-er-2) |

### Gemini Robotics ER 2 Streaming プレビュー

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | `gemini-robotics-er-2-streaming-preview` |
| saveサポートされるデータタイプ | **入力**  テキスト、画像、動画、音声  **出力**  テキスト |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  131,072  **出力トークンの上限**  65,536 |
| handyman機能 | **[音声生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)**  サポート対象外  **[キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**  サポート対象外  **コード実行**  サポート対象外  **[コンピュータ使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**  サポート対象外  **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**  サポート対象外  **[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**  サポート対象  **[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**  サポート対象外  **[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)**  サポート対象外  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)**  サポート対象  **[検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)**  サポート対象  **[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)**  サポート対象外  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)**  サポート対象  **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**  サポート対象外 |
| speed使用オプション | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**  サポート対象外  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)**  サポート対象外  **[優先度推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)**  サポート対象外 |
| 123 バージョン | 詳細については、[モデル バージョン パターン](https://ai.google.dev/gemini-api/docs/models?hl=ja#model-versions)をご覧ください。  - プレビュー: `gemini-robotics-er-2-streaming-preview` |
| calendar\_month最終更新 | 2026 年 7 月 |
| id\_cardモデルカード | [モデルカード](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ja) |
| paid料金 | [料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#gemini-robotics-er-2-streaming) |

### Gemini Robotics-ER 1.6 プレビュー版

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | `gemini-robotics-er-1.6-preview` |
| saveサポートされるデータタイプ | **入力**  テキスト、画像、動画、音声  **出力**  テキスト |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  131,072  **出力トークンの上限**  65,536 |
| handyman機能 | **[音声生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)**  サポート対象外  **[キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**  サポート対象  **コード実行**  サポート対象  **[コンピュータ使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**  サポート対象  **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**  サポート対象  **[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**  サポート対象  **[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**  サポート対象  **[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)**  サポート対象外  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)**  サポート対象外  **[検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)**  サポート対象  **[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)**  サポート対象  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)**  サポート対象  **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**  サポート対象 |
| speed使用オプション | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**  サポート対象  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)**  サポート対象外  **[優先度推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)**  サポート対象外 |
| 123 バージョン | 詳細については、[モデル バージョン パターン](https://ai.google.dev/gemini-api/docs/models?hl=ja#model-versions)をご覧ください。  - シャットダウン: `gemini-robotics-er-1.6-preview` |
| calendar\_month最終更新 | 2025 年 12 月 |
| cognition\_2ナレッジ カットオフ | 2025 年 1 月 |

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-29 UTC。"],[],[]]
