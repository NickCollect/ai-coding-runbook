---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=ja
fetched_at: 2026-07-27T04:49:55.184609+00:00
title: "\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u306e\u6982\u8981 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# エージェントの概要

Gemini API のマネージド エージェントは、構成可能なエージェント ハーネスを提供します。1 回の API 呼び出しで、エージェントが推論、コードの実行、ファイルの管理、ウェブの自律的な閲覧を行う Linux サンドボックスがプロビジョニングされます。

[rocket\_launch

クイックスタート

最初のエージェント呼び出しを行い、レスポンスをストリーミングし、カスタム エージェントを構築します。](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja)
[smart\_toy

Antigravity エージェント

デフォルト エージェントの機能、ツール、マルチモーダル入力、料金。](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja)
[experiment

AI Studio のエージェント

コードを記述せずにエージェントをプロトタイピングするためのビジュアル プレイグラウンド。](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ja)

## 利用可能なマネージド エージェント

- **[Antigravity エージェント](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja)**: 汎用
  マネージド エージェント (Gemini 3.6 Flash 搭載)。Google がホストする安全な Linux サンドボックス内でコードを実行し、ファイルを管理し、ウェブを検索します。
  基盤となるモデル（Gemini 3.6 Flash、Gemini 3.5 Flash、Gemini 3.5 Flash-Lite など）を
  `agent_config`を使用して構成し、独自の指示、スキル、データで拡張して
  [カスタム エージェントを構築](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja)できます。
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja)**: 自律型リサーチ エージェント
  市場分析、デュー デリジェンス、文献レビューなどのユースケースで使用する、複数ステップのリサーチタスクを計画、実行、統合する

## セキュリティとベスト プラクティス

すべてのエージェントは、OS レベルで分離されたサンドボックス環境で実行されます。
サンドボックスには、デフォルトで無制限の送信ネットワーク アクセスがあります。許可リストを使用して、ネットワーク アクセスを制限または無効にできます。

### ネットワーク アクセス

デフォルトでは、環境には無制限の送信ネットワーク アクセスがあります。`network` 許可リストを使用して、送信トラフィックを特定のドメインまたはワイルドカード パターンに制限します。構成の詳細については、
[ネットワーク許可リスト](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ja#network_allow_list)（AI
Studio）または[ネットワーク ルール](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja#with_network_rules)
（API）をご覧ください。

### 外部ツールと API

外部ツールと API を接続して、エージェントを拡張できます。信頼できるソースのツールのみを使用し、権限を必要最小限の範囲に設定してください。認証情報は、出力プロキシ ヘッダー変換を介して安全に挿入され、サンドボックス内で公開されることはありません。エージェントはアクセスできる認証情報を使用する可能性があるため、完全なスコープを付与してもよい認証情報のみを提供してください。

- 最小権限のサービス アカウントまたは API キーを使用します。
- 有効期間の長い鍵よりも有効期間の短いトークンを優先します。
- 完全なスコープを付与してもよい認証情報のみを提供してください。
- 認証情報を定期的にローテーションします。

ヘッダー変換の構成の詳細については、
[認証情報](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja#credentials)をご覧ください。

### 人間による監視

出力をデプロイする前に必ず確認してください（生成されたコード、データ変換、構成の変更）。特に、データを変更したり、外部システムとやり取りしたりするタスクの場合は注意が必要です。

## 料金

マネージド エージェントは、[従量課金制モデル](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#pricing-for-agents)
を Gemini モデルのトークンとツールの使用量に基づいて使用します。1 回のインタラクションで複数の推論ループがトリガーされ、通常は 10 万～ 300 万トークンが消費されます。プレビュー期間中は、環境コンピューティングの**料金は発生しません** 。タスクごとの内訳の[推定費用](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja#availability-and-pricing)
をご覧ください。マネージド エージェントは、無料枠、無料のレート上限、使用量上限のある無料枠でもご利用いただけます。

## 上限

| 上限 | 説明 |
| --- | --- |
| **環境の有効期間** | 環境は、7 日間操作がないと完全に削除されます。 |
| **VM のスピンダウン** | リソースを節約するため、VM は操作が行われない状態がしばらく続くとシャットダウンします。次のリクエストで状態が復元されます（コールド スタート）。 |
| **プリインストールされたソフトウェア** | Python 3.12 と Node.js 22 を搭載した Ubuntu ベースの環境。環境のベースイメージの詳細については、[プリインストールされたソフトウェア](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja#pre-installed-software)をご覧ください。 |
| **最大エージェント数** | マネージド エージェントは最大 1,000 個まで使用できます。 |

## エージェント フレームワーク

次のフレームワークと SDK を使用して、Gemini でエージェントを構築することもできます。

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=ja): Build
  stateful, complex application flows and multi-agent systems using graph
  structures.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=ja): Gemini エージェントを
  プライベート データに接続して、RAG で強化されたワークフローを実現します。
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=ja): 共同作業を行う、
  ロールプレイングの自律型 AI エージェントをオーケストレートします。
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=ja): JavaScript/TypeScript で AI を活用したユーザー インターフェースとエージェントを構築します。
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): 相互運用可能な AI エージェントを構築してオーケストレートするための
  オープンソース フレームワーク。
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=ja): Google Antigravity を強化するのと同じツール、エージェント ループ、コンテキスト
  管理を使用して、自律型 AI エージェントを構築します。Python でプログラミングできます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-21 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-21 UTC。"],[],[]]
