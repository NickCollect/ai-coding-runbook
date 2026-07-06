---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja
fetched_at: 2026-07-06T05:17:33.327285+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Interactions API

Interactions API は、Gemini モデルとエージェントを構築する最も簡単な方法を提供する新しいインターフェースです。2026 年 6 月の時点で、一般提供が開始され、すべての新しいプロジェクトで推奨されるインターフェースとなっています。

現在ではレガシーと見なされていますが、元の [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ja) API は引き続き完全にサポートされています。

## Interactions API を使用する理由

- **すぐに使える新機能**: `previous_interaction_id` を使用したサーバーサイドの会話状態（オプション）、デバッグと UI レンダリング用の実行ステップのモニタリング、`background=true` を使用した長時間実行タスクの[バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)。
- **キャッシュ ヒット率の向上によるコスト削減**: サーバーサイドの状態管理により、ターン間でコンテキスト キャッシュをより効率的に使用できるため、マルチターンの会話のトークン費用を削減できます。
- **フロンティア モデルとエージェント向けに構築**: 思考モデル、多段階のツール使用、複雑な推論フロー向けに特別に構築されており、エージェント アプリケーションの構築、デバッグ、オーケストレーションのプロセスを簡素化します。
- **モデルとエージェント用の単一の API**: Gemini モデルとエージェント（Deep Research やカスタム マネージド エージェントなど）を直接呼び出すための統合インターフェース。個別のエンドポイントやパターンを学習する必要はありません。
- **新機能のリリース場所**: 今後、コア メインライン ファミリー以外の新しいモデルと機能、新しいエージェント機能とツールは、Interactions API でリリースされます。

デフォルトでは、Interactions API はリクエストを保存するため、`previous_interaction_id` を使用してサーバーサイドの状態管理機能を活用できます。`store=false` を設定すると、ステートレス動作を有効にできます。詳細については、[データの保持](#data-storage-retention)をご覧ください。

## 始める

- **コーディング エージェントを設定する**: **Gemini Docs MCP** に接続し、`gemini-interactions-api` スキルをインストールして、アシスタントが最新のデベロッパー ドキュメントとベスト プラクティスに直接アクセスできるようにします。[コーディング エージェントを設定する →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja)
- **`generateContent` から移行する**: 既存の統合がある場合は、[移行ガイド](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ja)に沿って Interactions API に移行します。
- **スタートガイド**: [Interactions API スタートガイド](https://ai.google.dev/gemini-api/docs/get-started?hl=ja)をご覧ください。

### 機能ガイド

以下のガイドで Interactions API の具体的な機能をご確認ください。これらのページの切り替えを使用して、generateContent API と Interactions API を切り替えることができます。

- [テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja)
- [画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)
- [画像の理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)
- [音声の理解](https://ai.google.dev/gemini-api/docs/audio?hl=ja)
- [動画に関する理解を深める](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)
- [ドキュメント処理](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)
- [構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)
- [Deep Research エージェント](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja)
- [Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)
- [候補の推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)

## Interactions API の仕組み

Interactions API は、[**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ja#Resource:Interaction) というコアリソースを中心に構成されています。`Interaction` は、会話またはタスクの完全なターンを表します。セッション レコードとして機能し、インタラクションの履歴全体を **実行ステップ**の時系列順のシーケンスとして含みます。これらのステップには、モデルの思考、サーバーサイドまたはクライアントサイドのツール呼び出しと結果（`function_call` や `function_result` など）、最終的な `model_output` が含まれます。保存されたリソース（`interactions.get` で取得）には、完全なコンテキストの `user_input` ステップも含まれますが、`interactions.create` レスポンスはモデル生成ステップのみを返します。

[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ja#CreateInteraction) を呼び出すと、新しい `Interaction` リソースが作成されます。

### サーバーサイドの状態管理

`previous_interaction_id` パラメータを使用して、完了したインタラクションの `id` を後続の呼び出しで使用し、会話を続けることができます。サーバーはこの ID を使用して会話履歴を取得するため、チャット履歴全体を再送信する必要がなくなります。

`previous_interaction_id` パラメータは、`previous_interaction_id` を使用して会話履歴（入力と出力）のみを保持します。他のパラメータは**インタラクション スコープ**であり、現在生成している特定のインタラクションにのみ適用されます。

- `tools`
- `system_instruction`
- `generation_config`（`thinking_level`、`temperature` などを含む）

つまり、これらのパラメータを適用する場合は、新しいインタラクションごとに再指定する必要があります。このサーバーサイドの状態管理は省略可能です。各リクエストで完全な会話履歴を送信して、ステートレス モードで動作することもできます。

### データ ストレージと保持

デフォルトでは、API はすべての Interaction オブジェクト（`store=true`）を保存します。これは、サーバーサイドの状態管理機能（`previous_interaction_id` を使用）、[バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)（`background=true` を使用）、オブザーバビリティの目的での使用を簡素化するためです。

- **有料プラン**: システムはインタラクションを **55 日間**保持します。
- **無料枠**: 1 日間、インタラクションが保持されます。

この動作を希望しない場合は、リクエストで `store=false` を設定できます。このコントロールは状態管理とは別のもので、あらゆるインタラクションでストレージをオプトアウトできます。ただし、`store=false` は[バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)と互換性がなく、以降のターンで `previous_interaction_id` を使用できなくなります。

保存されたインタラクションは、[API リファレンス](https://ai.google.dev/api/interactions-api?hl=ja)にある削除メソッドを使用して、いつでも削除できます。やり取りを削除できるのは、やり取り ID がわかっている場合のみです。

保持期間が終了すると、データは自動的に削除されます。

システムは、[条件](https://ai.google.dev/gemini-api/terms?hl=ja)に従って Interaction オブジェクトを処理します。

## ベスト プラクティス

- **キャッシュ ヒット率**: `previous_interaction_id` を使用して会話を継続すると、システムは会話履歴の暗黙的なキャッシュ保存をより簡単に利用できるようになり、パフォーマンスが向上し、費用が削減されます。
- **インタラクションの組み合わせ**: 会話内でエージェントとモデルのインタラクションを柔軟に組み合わせることができます。たとえば、初期のデータ収集には Deep Research エージェントなどの特殊なエージェントを使用し、要約や再フォーマットなどの後続のタスクには標準の Gemini モデルを使用し、これらの手順を `previous_interaction_id` でリンクできます。

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
| Lyria 3 クリップのプレビュー | モデル | `lyria-3-clip-preview` |
| Lyria 3 Pro プレビュー | モデル | `lyria-3-pro-preview` |
| Deep Research プレビュー | エージェント | `deep-research-preview-04-2026` |
| Deep Research プレビュー | エージェント | `deep-research-max-preview-04-2026` |
| Antigravity のプレビュー | エージェント | `antigravity-preview-05-2026` |

## SDK

Interactions API にアクセスするには、最新バージョンの Google GenAI SDK を使用します。

- Python では、これは `2.3.0` バージョン以降の `google-genai` パッケージです。
- JavaScript では、これは `2.3.0` バージョン以降の `@google/genai` パッケージです。

SDK のインストール方法について詳しくは、[ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja) ページをご覧ください。

## 制限事項

- **リモート MCP**: Gemini 3 はリモート MCP をサポートしていません。近日中にサポート予定です。

次の機能は [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ja) API でサポートされていますが、Interactions API では**まだ利用できません**。

- **[動画メタデータ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)**: 動画の理解のためにクリッピング間隔とカスタム フレームレートを設定するために使用される `video_metadata` フィールド。
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**
- **[自動関数呼び出し（Python）](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ja#automatic_function_calling_python_only)**
- **[明示的なキャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**: サーバーサイドの暗黙的なキャッシュ保存は、`previous_interaction_id` を介して Interactions API で利用できます。

## フィードバック

皆様からのフィードバックは、Interactions API の開発に不可欠です。ご意見やバグの報告、機能のリクエストについては、[Google AI デベロッパー コミュニティ フォーラム](https://discuss.ai.google.dev/c/gemini-api/4?hl=ja)をご利用ください。

## 次のステップ

- [Interactions API クイックスタート ノートブック](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ja)をお試しください。
- [Gemini Deep Research エージェント](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja)の詳細を確認する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-26 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-26 UTC。"],[],[]]
