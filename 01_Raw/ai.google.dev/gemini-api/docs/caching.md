---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=ja
fetched_at: 2026-07-20T04:37:29.206089+00:00
title: "\u30b3\u30f3\u30c6\u30ad\u30b9\u30c8\u306e\u30ad\u30e3\u30c3\u30b7\u30e5\u4fdd\u5b58 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# コンテキストのキャッシュ保存

一般的な AI ワークフローでは、同じ入力トークンをモデルに何度も渡すことがあります。Gemini API は、パフォーマンスとコストを最適化するために暗黙的なキャッシュ保存を提供します。

## 暗黙的なキャッシュ保存

暗黙的なキャッシュ保存は、すべての Gemini 2.5 以降のモデルでデフォルトで有効になっています。[[ステートフル（`previous\_interaction\_id` を使用）とステートレスの両方の会話モードでサポートされています。](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#multi-turn-conversations)](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#stateless-conversations)`previous_interaction_id`リクエストがキャッシュにヒットした場合、コスト削減分が自動的に渡されます。有効にするために必要な操作はありません。コンテキスト キャッシュ保存の最小入力トークン数は、次の表にモデルごとに示されています。

| モデル | 最小トークン数 |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro プレビュー版 | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

暗黙的なキャッシュ ヒットの可能性を高めるには:

- 大規模で一般的なコンテンツは、プロンプトの先頭に配置します。
- 類似した接頭辞を含むリクエストを短時間で送信します。

キャッシュ ヒットしたトークンの数は、レスポンス オブジェクトの `usage.total_cached_tokens`（Python と JavaScript）フィールドで確認できます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-07 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-07 UTC。"],[],[]]
