---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja
fetched_at: 2026-08-03T04:28:27.733899+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Interactions API

Interactions API は、Gemini モデルとエージェントを構築するのに最適な方法です。2026 年 6 月より一般提供が開始され、すべての新しいプロジェクトにおすすめです。現在はレガシーと見なされていますが、元の
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ja) API
は引き続き完全にサポートされています。

## Interactions API を使用する理由

- **すべてのアプリケーションに対応するユニバーサル インターフェース**: 単一ターンのテキスト生成、
  マルチモーダル理解、構造化出力、ツール オーケストレーション、
  エージェント ワークフローなど、あらゆるユースケースに対応する標準
  インターフェースとして設計されています。
- **モデルとエージェントに対応する単一の API**: 標準の Gemini モデルと、Deep Research やカスタム マネージド エージェントなどの特殊なエージェントを直接呼び出すための統合エンドポイントとパターンが 1 つにまとめられています。
- [**すぐに使える新機能**: `previous\_interaction\_id` を使用したサーバーサイドの会話状態（オプション）、デバッグと UI レンダリングのための実行ステップのモニタリング、`background=true` を使用した長時間実行タスクのバックグラウンド実行などの機能が用意されています。](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)`previous_interaction_id``background=true`
- **キャッシュ ヒット率の向上とコストの削減**: マルチターンの
  会話を使用する場合、サーバーサイドの状態管理（オプション）により、ターン間でより効率的な
  コンテキスト キャッシュ保存が可能になり、トークン費用を削減できます。
- **新機能のリリース**: 今後、すべての新しいモデル、マルチモーダル
  機能、ツール、エージェント機能は Interactions
  API でリリースされます。

デフォルトでは、Interactions API はリクエストを保存するため、`previous_interaction_id` を使用してサーバーサイドの状態管理機能を利用できます。`store=false` を設定すると、ステートレス動作を選択できます。詳細については、[データの保持](#data-storage-retention)をご覧ください
。

## 始める

- **コーディング エージェントを設定する**: **Gemini Docs MCP** に接続し、
  スキルをインストールして、アシスタントが
  最新のデベロッパー ドキュメントとベスト プラクティスに直接アクセスできるようにします。`gemini-interactions-api`詳細な手順については、
  [コーディング エージェントを設定するガイド](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja)をご覧ください。
- **`generateContent` から移行する**: 既存の統合がある場合は、
  [移行ガイド](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ja)に沿って
  Interactions API に移行してください。
- **使ってみる**: [Interactions API のスタートガイド
  の手順に沿って操作してください](https://ai.google.dev/gemini-api/docs/get-started?hl=ja)。

### 機能ガイド

これらのガイドで、Interactions API の具体的な機能をご確認ください。これらのページで切り替えボタンを使用すると、generateContent API と Interactions API を切り替えることができます。

- [テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja)
- [画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)
- [画像理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)
- [音声の理解](https://ai.google.dev/gemini-api/docs/audio?hl=ja)
- [動画に関する理解を深める](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)
- [ドキュメント処理](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)
- [構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)
- [Deep Research エージェント](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja)
- [Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)
- [候補の推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)

## Interactions API の仕組み

Interactions API は、コアリソースである[**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ja#Resource:Interaction) を中心に構成されています。`Interaction` は、会話またはタスクの完全なターンを表します。セッション レコードとして機能し、インタラクションの履歴全体を**実行ステップ** の時系列シーケンスとして含みます。これらのステップには、モデルの思考、サーバーサイドまたはクライアントサイドのツール呼び出しと結果（`function_call` や `function_result` など）、最終的な `model_output` が含まれます。保存されたリソース（`interactions.get` で取得）には、完全なコンテキストの `user_input` ステップも含まれますが、`interactions.create` レスポンスはモデル生成ステップのみを返します。

[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ja#CreateInteraction) を呼び出すと、新しい `Interaction` リソースが作成されます。

### サーバーサイドの状態管理

完了したインタラクションの `id` を
`previous_interaction_id` パラメータを使用して後続の呼び出しで使用すると、会話を続行できます。サーバーはこの ID を使用して会話履歴を取得するため、チャット履歴全体を再送信する必要はありません。

`previous_interaction_id` パラメータは、`previous_interaction_id` を使用して会話履歴（入力と出力）のみを保持します。他のパラメータは**インタラクション スコープ** であり、現在生成している特定のインタラクションにのみ適用されます。

- `tools`
- `system_instruction`
- `generation_config`（`thinking_level`、`temperature` など）

これらのパラメータを適用する場合は、新しいインタラクションごとに再指定する必要があります。このサーバーサイドの状態管理は省略可能です。各リクエストで会話履歴全体を送信して、ステートレス モードで動作することもできます。

### データの保存と保持

デフォルトでは、API はすべての Interaction オブジェクト（`store=true`）を保存して、サーバーサイドの状態管理機能（`previous_interaction_id`）、[バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)（`background=true` を使用）、オブザーバビリティを簡単に利用できるようにします。

- **有料階層**: インタラクションは **55 日間** 保持されます。
- **無料階層**: インタラクションは **1 日間** 保持されます。

これを無効にする場合は、リクエストで `store=false` を設定します。この制御は状態管理とは別に行われます。インタラクションの保存はいつでも無効にできます。ただし、
`store=false` は [バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja) と互換性がなく、後続のターンで
`previous_interaction_id` を使用できなくなることに注意してください。

有料階層のプロジェクトでは、
[AI Studio](https://aistudio.google.com/logs?hl=ja) で保持期間を設定して、
7 日、14 日、28 日、55 日後にプロジェクト ストレージからログを自動的に削除するように設定できます。保持期間を短くすると、過去の会話の取得に影響する可能性があります。

保存されたインタラクションは、[`delete`](https://ai.google.dev/api/interactions-api?hl=ja#deleteInteraction) メソッドを使用していつでもプログラムで削除できます。これにはインタラクション ID が必要です。AI Studio では、保存されたインタラクション
ログを表示して管理することもできます（プロジェクト ストレージからの削除など）。

保持期間が終了すると、データは自動的に削除されます。

Interactions オブジェクトは、[利用規約](https://ai.google.dev/gemini-api/terms?hl=ja)に従って処理されます。

### AI Studio でインタラクションを表示する

API は、有料階層のプロジェクトで `store=true` で実行された Interactions API リクエストを保存します。Google AI Studio の
[[ログ] ページから直接確認できます](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=ja)。詳しくは、
[ログガイド](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ja)をご覧ください。

## ベスト プラクティス

- **キャッシュ ヒット率**: ステートフル モードと
  ステートレス モードの両方で暗黙的なキャッシュ保存がサポートされています（
  [クイックスタート](https://ai.google.dev/gemini-api/docs/get-started?hl=ja#4_multi-turn_conversations)をご覧ください）。`previous_interaction_id`（ステートフル）を使用して会話を続行すると、システムは会話履歴の暗黙的なキャッシュ保存をより簡単に利用できるため、パフォーマンスが向上し、費用が削減されます。
- **インタラクションの組み合わせ**: 会話内でエージェントと
  モデルのインタラクションを柔軟に組み合わせることができます。たとえば、Deep Research エージェントなどの特殊なエージェントを使用して初期データ収集を行い、標準の Gemini モデルを使用して要約や再フォーマットなどのフォローアップ タスクを実行し、これらのステップを `previous_interaction_id` でリンクできます。

## サポートされているモデルとエージェント

| モデル名 | タイプ | モデル ID |
| --- | --- | --- |
| Gemini 3.5 Flash | モデル | `gemini-3.5-flash` |
| Gemini 3.1 Pro プレビュー版 | モデル | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | モデル | `gemini-3.1-flash-lite` |
| Gemini 3 Flash プレビュー | モデル | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | モデル | `gemini-2.5-pro` |
| Gemini 2.5 Flash | モデル | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | モデル | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | モデル | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | モデル | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS プレビュー | モデル | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | モデル | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | モデル | `gemma-4-26b-a4b-it` |
| Lyria 3 Clip プレビュー | モデル | `lyria-3-clip-preview` |
| Lyria 3 Pro プレビュー | モデル | `lyria-3-pro-preview` |
| Deep Research プレビュー | エージェント | `deep-research-preview-04-2026` |
| Deep Research プレビュー | エージェント | `deep-research-max-preview-04-2026` |
| Antigravity プレビュー | エージェント | `antigravity-preview-05-2026` |

## SDK

Interactions API にアクセスするには、最新バージョンの Google GenAI SDK を使用します。

- Python の場合、`2.3.0` 以降のバージョンの `google-genai` パッケージです。
- JavaScript の場合、`2.3.0` 以降のバージョンの `@google/genai` パッケージです。

SDK のインストール方法について詳しくは、
[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja) ページをご覧ください。

## 制限事項

- **リモート MCP**: Gemini 3 はリモート MCP をサポートしていません。近日中にサポートされる予定です。
- **マルチターンのモデルの互換性**: 会話で異なるモデルを組み合わせる場合（ステートフルまたはステートレス）、後続のモデルは前のモデルの出力モダリティを入力としてサポートする必要があります。たとえば、`gemini-3.1-flash-image` を使用して画像を生成した場合、画像入力を受け付けないモデル（テキストのみのモデルや Lyria などの音楽生成モデル）で会話を続行することはできません。

次の機能は
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ja) API でサポートされていますが、Interactions API では**まだ利用できません
。**

- **[動画メタデータ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)**: `video_metadata` フィールド。動画の理解のためにクリッピング
  間隔とカスタム フレームレートを設定するために使用されます。
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**
- **[自動関数呼び出し（Python）](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ja#automatic_function_calling_python_only)**
- **[明示的なキャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**: サーバーサイドの暗黙的なキャッシュ保存は、Interactions API
  を介して利用できます。`previous_interaction_id`
- **[安全設定](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)**: Interactions API ではカスタムの安全設定はサポートされていません。

## フィードバック

Interactions API の開発には、皆様からのフィードバックが不可欠です。
ご意見やバグの報告、機能のリクエストについては、
[Google AI デベロッパー コミュニティ フォーラム](https://discuss.ai.google.dev/c/gemini-api/4?hl=ja)をご利用ください。

## 次のステップ

- [Interactions API クイックスタート ノートブック](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ja)をお試しください。
- [Gemini Deep Research エージェント](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja)の詳細をご確認ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-16 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-16 UTC。"],[],[]]
