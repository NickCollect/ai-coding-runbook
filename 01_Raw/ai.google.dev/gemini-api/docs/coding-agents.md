---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja
fetched_at: 2026-07-06T05:06:58.965170+00:00
title: "Gemini MCP \u3068\u30b9\u30ad\u30eb\u3092\u4f7f\u7528\u3057\u3066\u30b3\u30fc\u30c7\u30a3\u30f3\u30b0 \u30a2\u30b7\u30b9\u30bf\u30f3\u30c8\u3092\u8a2d\u5b9a\u3059\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini MCP とスキルを使用してコーディング アシスタントを設定する

AI コーディング アシスタントは強力ですが、制限があります。トレーニング データは特定の日付でカットオフされ、新しい API 機能や変更が反映されません。Gemini 固有のドキュメントにアクセスできない場合、エージェントは最適化されたアプローチではなく、一般的なパターンを提案する可能性があります。

進化する Gemini API とその推奨される使用方法に合わせてコーディング アシスタントを最新の状態に保つには、**Gemini Docs MCP** を設定し、**Gemini API Skills** で環境を強化することをおすすめします。これらのツールは個別に使用できますが、連携して完全なカバレッジを提供するように設計されています。

## Gemini Docs MCP を接続する

Gemini は、`https://gemini-api-docs-mcp.dev` にパブリック Model Context Protocol（MCP）サーバーをホストします。コーディング エージェントをこのサーバーに接続すると、すべてのクエリが最新の API、コード更新、最適な構成例にアクセスできるようになります。

エージェントのターミナルまたはプロジェクト ルートで次のコマンドを実行して、サーバーをインストールします。

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

このサーバーは、エージェントが公式の Gemini ドキュメント ファイルからリアルタイムの API 定義と統合パターンを取得するために使用できる `search_documentation` 関数を追加します。

## API 開発スキルを追加する

スキルは、アシスタントのコンテキストに直接 **組み込みのルールとベスト プラクティス**（正しい SDK と現在のモデル バージョンの適用など）を提供します。このスキルは Gemini Docs MCP サービスと連携して動作します。両方がインストールされている場合、このスキルはドキュメントに MCP サービスを使用しますが、MCP がインストールされていない場合でも、フォールバックとして `ai.google.dev` から `llms.txt` を取得します。

これらのスキルをインストールするには、次のいずれかのサポートされているツールを使用します。両方のインストール手順は、各スキルモジュールの下に記載されています。

- **[skills.sh](https://skills.sh)**: 推奨。ポータブル エージェントの動作に関するオープン標準。
- **[Context7](https://context7.com)**: Context7 エコシステムをすでに利用しているユーザーが対象です。

### gemini-api-dev

汎用 Gemini 開発の基礎となるスキル。このスキルでは、次のドキュメントとベスト プラクティスを提供します。

- 現在のモデル（Gemini 3.1 Pro/Flash など）へのプロンプトのルーティングと、非推奨モデルの回避
- マルチモーダル プロンプト、関数呼び出し、構造化された出力、一般的な統合パターン

#### skills.sh を使用してインストールする

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Context7 を使用してインストールする

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Gemini Live API を使用してリアルタイムの会話型 AI アプリケーションを構築するスキル。このスキルでは、次のドキュメントとベスト プラクティスを提供します。

- 低レイテンシ ストリーミング用の WebSocket 接続
- 音声、動画、テキストのストリーミング
- 音声アクティビティ検出と割り込みのサポート

#### skills.sh を使用してインストールする

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Context7 を使用してインストールする

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) を使用してアプリを構築するためのスキル。Interactions API は、Gemini モデルとエージェントを操作するための統合インターフェースであり、エージェント アプリケーション向けに設計されています。このスキルでは、次の内容について学習します。

- テキスト生成、マルチターン チャット、ストリーミング
- 関数呼び出し、構造化出力、画像生成
- バックグラウンド実行と Deep Research エージェント
- サーバーサイドの会話状態管理
- Python と TypeScript の SDK パターン

#### skills.sh を使用してインストールする

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Context7 を使用してインストールする

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## インストールを確認する

インストール後、コーディング アシスタントが Gemini Docs MCP サーバーに接続し、インストールしたスキルを使用できることを確認します。

### 1. エージェントの動作を確認する

最も確実な方法は、Gemini API に関する技術的な質問をエージェントにすることです。

**プロンプト:** 「Gemini API でコンテキスト キャッシュ保存機能を使用するにはどうすればよいですか？」

設定が正常に完了すると、次のようになります。

- **正確なコードを提供する**: 最新のエンドポイントから `cacheContent` や `cachedContents.create` などの特定の Gemini メソッドを参照します。
- **MCP ツールを使用する**: **Gemini Docs MCP サーバー**に接続されていること、または `search_documentation` ツールを使用してデータを取得していることを示します。
- **読み込まれたスキルを呼び出す**: 「スキルを使用中: gemini-api-dev」というインジケーターを表示します（セカンダリ ラッパーを使用している場合）。

### 2. 現象とツールを確認する

エージェントが一般的な回答をした場合は、環境固有の Discovery コマンドまたは Status コマンドを使用して、Docs MCP またはスキルがメモリに読み込まれていることを確認します。

| 環境 | MCP の確認 | スキルの確認 |
| --- | --- | --- |
| **Claude Code** | ターミナルに「`/mcp`」と入力して、アクティブなサーバーと `search_documentation` ツールを表示します。 | ターミナルで `/skills` と入力して、アクティブなすべてのマニフェストを一覧表示します。 |
| **Cursor** | **[設定] > [機能] > [MCP]** に移動します。サーバーが [接続済み] になっていることを確認します。 | **[設定] > [ルール]** を開きます。スキルが [Agent Decides] に表示されていることを確認します。 |
| **Antigravity** | [**カスタマイズ > 接続**] サイドバーで MCP のステータスを確認します。 | `/skills list` と入力するか、[**カスタマイズ] > [ルール]** のサイドバーを確認します。 |
| **Gemini CLI** | `gemini mcp list` を実行するか、`/mcp list` を使用します。 | `gemini skills list` を実行するか、セッション中に `/skills` スラッシュ コマンドを使用します。 |
| **Copilot** | `@gemini /mcp` と入力して、アクティブなデータコネクタを一覧表示します。 | `@gemini /skills`（または `/skills`）と入力すると、有効な拡張機能が表示されます。 |

## トラブルシューティング

エージェントが一般的な情報しか提供しない場合や、Gemini 固有のメソッドを認識しない場合は、次の点を確認してください。

### エージェントがスキルを検出できなかった

ほとんどのエージェントは、起動時にのみスキルをインデックス登録します。

**修正:** IDE（Cursor/VS Code）を完全に再起動するか、ターミナルベースのエージェント（Claude Code）を終了して再度開きます。

### グローバルな競合とローカルな競合

`--global` フラグを使用してインストールした場合、エージェントはプロジェクト固有のルールを優先してこのフラグを無視している可能性があります。

**修正:** グローバル フラグなしで、スキルをプロジェクト ルートに直接インストールしてみてください。

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## リソース

- [GitHub の Gemini API スキル](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja)
- [使ってみる](https://ai.google.dev/gemini-api/docs/get-started?hl=ja)
- [ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
