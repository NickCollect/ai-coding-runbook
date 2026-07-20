---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=ja
fetched_at: 2026-07-20T04:48:36.002298+00:00
title: "Gemini API \u3067\u30c4\u30fc\u30eb\u3092\u4f7f\u7528\u3059\u308b \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API でツールを使用する

ツールは Gemini モデルの機能を拡張し、現実世界でのアクション、リアルタイムの情報へのアクセス、複雑な計算タスクの実行を可能にします。モデルは、[Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja) を使用して、標準のリクエストとレスポンスのやり取りとリアルタイム ストリーミング セッションの両方でツールを使用できます。

ツールは、モデルがクエリへの回答に使用できる特定の機能（Google 検索やコード実行など）です。Gemini API は、フルマネージドの組み込みツール スイートを提供します。また、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)を使用してカスタムツールを定義することもできます。

マルチステップの目標指向システムを構築するには、[エージェントの概要](https://ai.google.dev/gemini-api/docs/agents?hl=ja)をご覧ください。

## 利用可能な組み込みツール

| ツール | 説明 | ユースケース |
| --- | --- | --- |
| [Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) | ウェブ上の最新の出来事や事実に基づいて回答を生成し、ハルシネーションを減らします。 | \- 最近の出来事に関する質問に答える   \- さまざまなソースで事実を確認する |
| [Google マップ](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja) | 場所の検索、ルートの取得、豊富なローカル コンテキストの提供が可能な位置認識アシスタントを構築します。 | - 複数の立ち寄り先を含む旅行プランの作成   - ユーザーの条件に基づくローカル ビジネスの検索 |
| [コードの実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja) | モデルが Python コードを記述して実行し、数学の問題を解決したり、データを正確に処理したりできるようにします。 | \- 複雑な数式を解く   \- テキストデータを正確に処理、分析する |
| [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja) | 特定のウェブページやドキュメントのコンテンツを読み取って分析するようにモデルに指示します。 | \- 特定の URL またはドキュメントに基づいて質問に回答する   \- さまざまなウェブページから情報を取得する |
| [コンピュータ使用（プレビュー）](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja) | Gemini が画面を表示し、ウェブブラウザの UI を操作するアクションを生成できるようにします（クライアント サイド実行）。 | \- ウェブベースの反復的なワークフローの自動化   \- ウェブ アプリケーションのユーザー インターフェースのテスト |
| [ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja) | 独自のドキュメントをインデックス登録して検索し、検索拡張生成（RAG）を有効にします。 | - 技術マニュアルの検索   - 独自データに関する質問応答 |

特定のツールに関連する費用の詳細については、[料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#pricing_for_tools)をご覧ください。

## ツールの実行の仕組み

ツールを使用すると、モデルは会話中にアクションをリクエストできます。ツールが組み込み（Google が管理）かカスタム（ユーザーが管理）かによって、フローは異なります。

### 組み込みツールのフロー

組み込みツール（Google 検索、Google マップ、URL コンテキスト、ファイル検索、コード実行）の場合、プロセス全体が 1 回の API 呼び出しで行われます。

1. **ユーザー**が「GOOG の最新の株価の平方根は？」というプロンプトを送信します。
2. **Gemini** はツールが必要であると判断し、Google のサーバーでツールを実行します（株価を検索してから、Python コードを実行して平方根を計算するなど）。
3. **Gemini** は、ツールの結果に基づいて最終的な回答を返します。

### カスタムツールフロー（関数呼び出し）

カスタムツールとコンピュータ使用の場合、アプリケーションが実行を処理します。

1. **ユーザー**は、関数（ツール）宣言とともにプロンプトを送信します。
2. **Gemini** は、常に一意の `id` を使用して、特定の関数（`{"name": "get_order_status", "args": {"order_id": "123"}}` など）を呼び出すために構造化された JSON を返送することがあります。
3. **ユーザー**がアプリケーションまたは環境で関数を実行します。
4. 関数呼び出しと同じ `id` を使用して、関数の結果を Gemini に送り返します。
5. **Gemini** は、結果を使用して最終的なレスポンスまたは別のツール呼び出しを生成します。

詳しくは、[関数呼び出しガイド](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)をご覧ください。

### 組み込みツールとカスタムツールのフローを組み合わせる

組み込みツールとカスタムツール（関数呼び出し）を組み合わせたリクエストの場合、モデルは[ツール コンテキストの循環](https://ai.google.dev/gemini-api/docs/toold-combination?hl=ja)を使用して、さまざまな環境での実行を調整します。

1. **ユーザー**は、プロンプトを送信し、有効にする組み込みツールとカスタム関数を宣言して、組み合わせサポートをオンにするフラグを設定します。
2. **Gemini** は、組み込みツールを実行し、クライアントサイドの関数呼び出しが生成された場合はユーザーに譲ります（最初に実行されるのは、プロンプトとモデルの判断によって異なります）。次のようなレスポンスが返されます。
   - ツール呼び出しの確認
   - ツール レスポンスの結果（モデルが 2 つの並列関数呼び出しを生成した場合、JSON の後に続くことがあります）
   - 関数を呼び出す構造化 JSON
   - コンテキストを保持するための暗号化された思考シグネチャ
3. **ユーザー**がアプリケーションまたは環境で関数を実行します。
4. **ユーザー**は、Gemini のレスポンスのすべての部分と、関数呼び出しの結果を返します。
5. **Gemini** は、結合されたすべてのコンテキストを使用して最終的な回答を生成します。

[ツールの組み合わせガイド](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)で、組み込みツールとカスタムツールの組み合わせのサポートを有効にする方法と、コンテキストの循環の例をご覧ください。

## 構造化出力と関数呼び出し

Gemini には、構造化された出力を生成する 2 つの方法があります。モデルが独自のツールやデータシステムに接続して中間ステップを実行する必要がある場合は、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)を使用します。カスタム UI のレンダリングなど、モデルの最終的なレスポンスが特定のスキーマに厳密に準拠する必要がある場合は、[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)を使用します。

## ツールを使用した構造化出力

[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)と組み込みツールを組み合わせることで、外部データまたは計算に基づいてグラウンディングされたモデルのレスポンスが厳密なスキーマに準拠するようにできます。

コード例については、[ツールを使用した構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=ja#structured_outputs_with_tools)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
