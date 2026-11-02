---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=ja
fetched_at: 2026-11-02T07:03:19.197573+00:00
title: "\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u306e\u6982\u8981 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# エージェントの概要

Gemini API のマネージド エージェントは、構成可能なエージェント ハーネスを提供します。1 回の API 呼び出しで、エージェントが推論、コードの実行、ファイルの管理、ウェブの自律的な閲覧を行う Linux サンドボックスがプロビジョニングされます。

[rocket\_launch

クイックスタート

最初のエージェント呼び出しを行い、レスポンスをストリーミングして、カスタム エージェントを構築します。](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja)
[smart\_toy

Antigravity エージェント

デフォルトのエージェントの機能、ツール、マルチモーダル入力、料金。](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja)
[experiment

AI Studio のエージェント

コードを記述せずにエージェントのプロトタイピングを行うためのビジュアル プレイグラウンド。](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ja)

## 利用可能なマネージド エージェント

- **[Antigravity エージェント](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja)**: Gemini 3.8 Flash で構築された汎用マネージド エージェント。Google がホストする安全な Linux サンドボックス内でコードを実行し、ファイルを管理し、ウェブを検索します。`agent_config` を使用して基盤となるモデル（Gemini 3.6 Flash や Gemini 3.5 Flash-Lite など）を構成し、独自の指示、スキル、データで拡張して[カスタム エージェントを構築](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja)できます。
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja)**: マーケット分析、デュー デリジェンス、文献レビューなどのユースケース向けに、複数ステップからなるリサーチタスクを計画、実行、統合する自律型リサーチ エージェント。

## セキュリティとベスト プラクティス

各エージェントは、OS レベルで分離されたサンドボックス環境で実行されます。サンドボックスには、デフォルトで無制限の送信ネットワーク アクセスがあります。許可リストを使用して、ネットワーク アクセスを制限または無効にできます。

### ネットワーク アクセス

デフォルトでは、環境には制限のないアウトバウンド ネットワーク アクセスがあります。`network` 許可リストを使用して、下り（外向き）トラフィックを特定のドメインまたはワイルドカード パターンに制限します。構成の詳細については、[ネットワーク許可リスト](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ja#network_allow_list)（AI Studio）または[ネットワーク ルール](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja#with_network_rules)（API）をご覧ください。

### 外部ツールと API

外部ツールや API を接続して、エージェントを拡張できます。信頼できるソースのツールのみを使用し、権限の範囲を必要最小限に設定します。シークレットをマネージド認証情報として保存し、ID で参照します。これにより、下り（外向き）プロキシはリクエスト時にシークレットを挿入し、サンドボックス内で公開されることはありません。エージェントはアクセス可能な認証情報を使用する可能性があるため、完全なスコープを付与してもよい認証情報のみを指定してください。

- 最小権限のサービス アカウントまたは API キーを使用します。
- 有効期間の長い鍵よりも有効期間の短いトークンを優先します。
- 完全なスコープを付与してもよい認証情報のみを提供してください。
- 認証情報を定期的にローテーションします。

認証情報の種類と管理オペレーションについては、[認証情報](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ja)をご覧ください。許可リストルールのヘッダーをインラインで設定することもできます。[ネットワーク構成](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja#network-configuration)をご覧ください。

### 人間による監視

特に、データを変更するタスクや外部システムとやり取りするタスクについては、出力をデプロイする前に必ず確認してください（生成されたコード、データ変換、構成の変更など）。

## 料金

マネージド エージェントは、Gemini モデルのトークンとツールの使用量に基づく[従量課金制モデル](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#pricing-for-agents)を使用します。1 回のインタラクションで複数の推論ループがトリガーされ、通常は 10 万～ 300 万個のトークンが消費されます。プレビュー期間中は、環境コンピューティングの料金は**請求されません**。タスクごとの内訳については、[見積もり費用](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja#availability-and-pricing)をご覧ください。マネージド エージェントは、無料枠の無料レート上限と使用量割り当てでも利用できます。

## 上限

| 上限 | 説明 |
| --- | --- |
| **環境の有効期間** | 環境は、7 日間使用されないと完全に削除されます。 |
| **VM のスピンダウン** | リソースを節約するため、VM は操作が行われない状態がしばらく続くとシャットダウンします。次のリクエストは、状態を復元します（コールド スタート）。 |
| **プリインストールされているソフトウェア** | Python 3.12 と Node.js 22 を使用する Ubuntu ベースの環境。環境のベースイメージの詳細については、[プリインストールされたソフトウェア](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja#pre-installed-software)をご覧ください。 |
| **最大エージェント数** | 管理対象エージェントは最大 1,000 個まで使用できます。 |

## エージェント フレームワーク

次のフレームワークと SDK を使用して、Gemini でエージェントを構築することもできます。

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=ja): グラフ構造を使用して、ステートフルで複雑なアプリケーション フローとマルチエージェント システムを構築します。
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=ja): Gemini エージェントをプライベート データに接続して、RAG 強化ワークフローを実現します。
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=ja): 共同作業を行うロールプレイングの自律型 AI エージェントをオーケストレートします。
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=ja): JavaScript/TypeScript で AI を活用したユーザー インターフェースとエージェントを構築します。
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): 相互運用可能な AI エージェントを構築してオーケストレートするためのオープンソース フレームワーク。
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=ja): Google Antigravity を支える同じツール、エージェント ループ、コンテキスト管理を使用して、自律型 AI エージェントを構築します。Python でプログラミングできます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-09 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-09 UTC。"],[],[]]
