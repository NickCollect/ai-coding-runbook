---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja
fetched_at: 2026-09-14T05:37:35.376495+00:00
title: "Gemini MCP \u3068\u30b9\u30ad\u30eb\u3092\u4f7f\u7528\u3057\u3066\u30b3\u30fc\u30c7\u30a3\u30f3\u30b0 \u30a2\u30b7\u30b9\u30bf\u30f3\u30c8\u3092\u8a2d\u5b9a\u3059\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini MCP とスキルを使用してコーディング アシスタントを設定する

AI コーディング アシスタントは強力ですが、トレーニング データが特定の日付で打ち切られるため、新しい API
機能や変更が反映されないという制限があります。Gemini 固有のドキュメントにアクセスできない場合、エージェントは最適化されたアプローチではなく、一般的なパターンを提案することがあります。

進化する Gemini API とその推奨される使用方法に合わせてコーディング アシスタントを最新の状態に保つには、**Gemini Docs MCP**
を設定し、**Gemini API スキル**
で環境を強化することをおすすめします。これらのツールは単独で使用できますが、連携して完全なカバレッジを提供するように設計されています。

## Gemini Docs MCP を接続する

Gemini は、`https://gemini-api-docs-mcp.dev` に公開 Model Context
Protocol（MCP）サーバーをホストしています。コーディング
エージェントをこのサーバーに接続すると、すべてのクエリが最新の API、コードの更新、最適な構成例にアクセスできるようになります。

エージェントのターミナルまたはプロジェクト ルートで次のコマンドを実行して、サーバーをインストールします。

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

このサーバーは、エージェントが公式の Gemini ドキュメント ファイルからリアルタイムの API 定義と統合パターンを取得するために使用できる
`search_documentation` 関数を追加します。

## API 開発スキルを追加する

このスキルは、アシスタントのコンテキストに**組み込みのルールとベスト プラクティス** （正しい SDK
バージョンと現在のモデル バージョンの適用など）を直接提供します。このスキルは Gemini Docs MCP
サービスと連携して動作します。両方がインストールされている場合、このスキルは MCP サービスをドキュメントに使用しますが、MCP
がインストールされていない場合でも、フォールバックとして `ai.google.dev` から `llms.txt` を取得します。

これらのスキルをインストールするには、次のいずれかのサポートされているツールを使用します。両方のインストール手順は、各スキル
モジュールの下に記載されています。

- **[skills.sh](https://skills.sh)**: 推奨。ポータブル エージェントの動作のオープン標準。
- **[Context7](https://context7.com)**: Context7 エコシステムをすでに利用しているユーザー向けにサポートされています。

### gemini-api-dev

[Gemini API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja)（Interactions API）を使用してアプリを構築するためのスキル。Interactions API
は、Gemini モデルとエージェントを使用して構築する最もシンプルで最適な方法です。このスキルは次のことをカバーしています。

- テキスト生成、マルチターン チャット、ストリーミング
- 関数呼び出し、構造化出力、画像生成
- バックグラウンド実行と Deep Research エージェント
- サーバーサイドの会話状態管理
- 現在のモデルへのプロンプトのルーティングと、非推奨モデルの回避
- Python と TypeScript SDK のパターン

#### skills.sh でインストールする

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Context7 でインストールする

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Gemini Live API を使用してリアルタイムの会話型 AI
アプリケーションを構築するためのスキル。このスキルは、次のドキュメントとベスト プラクティスを提供します。

- 低レイテンシ ストリーミング用の WebSocket 接続
- 音声、動画、テキストのストリーミング
- 音声検出と割り込みサポート

#### skills.sh でインストールする

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Context7 でインストールする

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

## インストールを確認する

インストール後、コーディング アシスタントが Gemini Docs MCP サーバーに接続し、インストールしたスキルを使用できることを確認します。

### 1. エージェントの動作を確認する

確認する最も確実な方法は、Gemini API に関する技術的な質問をエージェントにすることです。

**プロンプト:** 「Gemini API でコンテキスト キャッシュ保存を使用するにはどうすればよいですか？」

設定が成功すると、次のようになります。

- **正確なコードを提供する**: 最新のエンドポイントから `cacheContent` や `cachedContents.create` などの特定の Gemini メソッドを参照します。
- **MCP ツールを使用する**: **Gemini Docs MCP サーバー** に接続されていること、または `search_documentation` ツールを使用してデータを取得していることを示します。
- **読み込まれたスキルを呼び出す**: セカンダリ ラッパーに依存している場合は、「Using skill: gemini-api-dev」というインジケーターが表示されます。

### 2. マニフェストとツールを確認する

エージェントが一般的な回答をする場合は、環境固有の Discovery コマンドまたは Status コマンドを使用して、Docs MCP
またはスキルがメモリに読み込まれていることを確認します。

| 環境 | MCP の検証 | スキルの検証 |
| --- | --- | --- |
| **Claude Code** | ターミナルで「`/mcp`」と入力して、アクティブなサーバーと `search_documentation` ツールを表示します。 | ターミナルで「`/skills`」と入力して、アクティブなマニフェストをすべて一覧表示します。 |
| **Cursor** | **[設定] > [機能] > [MCP]** に移動します。サーバーが [接続済み] になっていることを確認します。 | **[設定] > [ルール]** を開きます。[Agent Decides] にスキルが表示されていることを確認します。 |
| **Antigravity** | **[Customizations] > [Connections]** サイドバーで MCP のステータスを確認します。 | 「`/skills list`」と入力するか、**[Customizations] > [Rules]** サイドバーを確認します。 |
| **Gemini CLI** | `gemini mcp list` を実行するか、`/mcp list` を使用します。 | `gemini skills list` を実行するか、セッション内で `/skills` スラッシュ コマンドを使用します。 |
| **Copilot** | `@gemini /mcp` と入力して、アクティブなデータコネクタを一覧表示します。 | `@gemini /skills`（または `/skills`）と入力して、アクティブな拡張機能を表示します。 |

## トラブルシューティング

エージェントが一般的な情報しか提供しない場合や、Gemini 固有のメソッドを認識しない場合は、次の点を確認してください。

### エージェントがスキルを検出できなかった

ほとんどのエージェントは、起動時にのみスキルのインデックスを作成します。

**解決策:** IDE（Cursor/VS Code）を完全に再起動するか、ターミナルベースのエージェント（Claude Code）を終了して再度開きます。

### グローバルとローカルの競合

`--global` フラグを使用してインストールした場合、エージェントがプロジェクト固有のルールを優先して無視している可能性があります。

**解決策:** グローバル フラグを使用せずに、スキルをプロジェクト ルートに直接インストールしてみてください。

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

最終更新日 2026-09-10 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-10 UTC。"],[],[]]
