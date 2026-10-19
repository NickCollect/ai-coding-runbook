---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=ja
fetched_at: 2026-10-19T05:53:25.886545+00:00
title: "Gemini Developer API \u3067\u306e\u30c7\u30fc\u30bf\u4fdd\u6301\u30bc\u30ed \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini Developer API でのデータ保持ゼロ

このページでは、Gemini Developer API で一般的に「データ保持ゼロ」と呼ばれるものの詳細について説明します。

## トレーニングの制限

[Gemini API 利用規約](https://ai.google.dev/gemini-api/terms?hl=ja)に記載されているとおり、有料サービスを使用する場合、Google はプロダクトの改善にプロンプト（関連するシステム指示、キャッシュに保存されたコンテンツ、画像、動画、ドキュメントなどのファイルを含む）やレスポンスを使用しません。有料サービスは[こちら](https://ai.google.dev/gemini-api/terms?hl=ja#paid-services)で定義されています。

## 顧客データの保持とデータの保持ゼロの実現

顧客データは通常、次のシナリオと条件で一定期間保持されます。データの保持をゼロにするには、次の各領域で特定のアクションを行うか、特定の機能を使用しないようにする必要があります。

- **不正行為のモニタリングのためのプロンプトのロギング**: [Gemini API の追加利用規約](https://ai.google.dev/gemini-api/terms?hl=ja)に記載されているように、有料サービスの場合、Google は[使用禁止に関するポリシー](https://policies.google.com/terms/generative-ai/use-policy?hl=ja)の違反を検出する目的でのみ、一定期間プロンプトとレスポンスをログに記録します。ワークロードでデータ保持ゼロの保証や企業データ処理契約が必要な場合は、Vertex AI を使用します。詳細については、[Gemini Enterprise Agent Platform とデータ保持ゼロ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=ja)をご覧ください。
- **Google 検索によるグラウンディング**: [Gemini API 追加サービス規約](https://ai.google.dev/gemini-api/terms?hl=ja#grounding-with-google-search)に記載されているように、Google はグラウンディングされた結果と検索候補を作成する目的で、プロンプト、コンテキスト情報、生成された出力を 30 日間保存します。保存された情報は、グラウンディングをサポートするシステムのデバッグとテストに使用されることがあります。**Google 検索によるグラウンディングを使用する場合、この情報の保存を無効にすることはできません。**
- **Google マップによるグラウンディング**: [Gemini API の追加利用規約](https://ai.google.dev/gemini-api/terms?hl=ja)に記載されているとおり、Google はグラウンディングされた検索結果を作成する目的で、プロンプト、コンテキスト情報、生成された出力を 30 日間保存します。この保存された情報は、サービスの信頼性エンジニアリング（サービスの問題が発生した場合のデバッグなど）にのみ使用されます。**Google マップによるグラウンディングを使用する場合、この情報の保存を無効にすることはできません。**
- **Interactions API**: Interactions API は、会話のアクティブ状態を管理して、マルチターンの会話を可能にします。**デフォルトでは、Interactions API は状態の保存を有効にします**。データ フットプリントをゼロにするには、API リクエストで `store` パラメータを明示的に `false` に設定して、デフォルトの状態保持をオプトアウトする必要があります。
- **Live API**: このステートフル API は、会話の状態を保存することでリアルタイムの再接続を可能にします。データ保持をゼロにするには、**SessionResumptionConfig を構成しないでください**。セッション ハンドルが生成されると、会話の状態（テキスト、音声、動画など）が最長 24 時間保持されます。
- **File API Storage**: File API を使用すると、ユーザーは大きなアセットをアップロードできます。ファイルは、ユーザーが削除するか、有効期限が切れるまで保存されます。File API の使用は ZDR ロギングとは無関係です。ユーザーは、データフットプリントをゼロにするために、手動でファイルを削除する必要があります。
- **明示的なコンテキスト キャッシュ保存**: ユーザーは `cached_content` フィールドを使用して、大きなデータセット（長い動画やドキュメント ライブラリなど）を手動でキャッシュ保存できます。これらのリクエストのログは ZDR 削除ポリシーに従いますが、キャッシュに保存されたコンテキスト自体は、ユーザー定義の `ttl` または `expire_time` で保存されます。データ フットプリントを完全にゼロにするには、cached\_content 機能を使用しないでください。
- **暗黙的なメモリ内キャッシュ保存**: デフォルトでは、Gemini モデルはレイテンシとデベロッパーの費用を削減するために、データをメモリ内のキャッシュに保存します。このデータは厳密に RAM 内に保存され（保存時ではなく）、プロジェクト レベルで分離されています。TTL は 24 時間です。**これはデータ保持ゼロに違反しません。**

## 次のステップ

- [生成 AI の使用禁止に関するポリシー](https://policies.google.com/terms/generative-ai/use-policy?hl=ja)をご確認ください。
- [Gemini API 追加利用規約](https://ai.google.dev/gemini-api/terms?hl=ja)を確認します。
- エンタープライズ グレードのセルフサービス ZDR 制御が必要な場合は、[Gemini Enterprise Agent Platform のデータ保持ゼロ ガイド](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-16 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-16 UTC。"],[],[]]
