---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja
fetched_at: 2026-09-07T05:36:13.131784+00:00
title: "\u30c8\u30e9\u30d6\u30eb\u30b7\u30e5\u30fc\u30c6\u30a3\u30f3\u30b0 \u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# トラブルシューティング ガイド

このガイドでは、Gemini API の呼び出し時に発生する一般的な問題を診断して解決する方法について説明します。Gemini API バックエンド サービスまたはクライアント SDK のいずれかで問題が発生する可能性があります。クライアント SDK は、次のリポジトリでオープンソース化されています。

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

API キーに関する問題が発生した場合は、[API キーの設定ガイド](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)に沿って API キーが正しく設定されていることを確認してください。

## エラーコード

HTTP ステータス コード、生成ブロック コード、コンテンツ エラーコードなど、すべてのエラーコードのリファレンスについては、[API エラー](https://ai.google.dev/gemini-api/docs/api-errors?hl=ja)のページをご覧ください。

## 再試行方法

リクエストを再試行する必要があることを示すエラー（`429 RESOURCE_EXHAUSTED` や `503 UNAVAILABLE` など）を受け取った場合は、指数バックオフ戦略を実装することをおすすめします。つまり、最初の再試行の前に短い時間待機し、後続の再試行間の待機時間を徐々に増やします。

[Python SDK](https://github.com/googleapis/python-genai) などの Gemini API の公式クライアント SDK には、タイムアウト、ネットワークの問題、レート制限（`429` と `5xx` のステータス コード）などの一時的なエラーを処理するための指数バックオフによる自動再試行ロジックがデフォルトで含まれています。たとえば、Python SDK は、一時的なエラーを最大 4 回自動的に再試行します。最初の遅延は約 1 秒で、最大遅延は 60 秒です。

REST API リクエストを直接行う場合や、再試行ロジックをカスタマイズする場合は、次のベスト プラクティスに沿って、リクエストの成功率を高め、サービスへの過負荷を防ぎます。

- **指数バックオフを使用する:** 最初の再試行の前に短い時間（1 秒など）待機し、遅延を指数関数的に増やします（2 秒、4 秒、8 秒など）。
- **ジッターを追加する:** すべてのクライアントが同時に再試行しないように、遅延にランダムな「ジッター」を追加します。
- **特定のエラーで再試行する:** 一時的なエラー（`429`、`408`、`5xx` など）でのみ再試行します。クライアント エラー（`400`、`403` など）は、無効な API キーや構文エラーなどの問題を示しているため、再試行しないでください。
- **最大再試行回数を設定する:** 無限ループを回避するために、再試行の最大回数を定義します。

## API 呼び出しでモデル パラメータのエラーを確認する

モデル パラメータが次の値の範囲内であることを確認します。

|  |  |
| --- | --- |
| **モデル パラメータ** | **値（範囲）** |
| 候補の数 | 1 ～ 8（整数） |
| 温度 | 0.0-1.0 |
| 最大出力トークン | [モデルのページ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)で、使用しているモデルの最大トークン数を特定します。 |
| TopP | 0.0-1.0 |

パラメータ値を確認するだけでなく、必要な機能をサポートする正しい [API バージョン](https://ai.google.dev/gemini-api/docs/api-versions?hl=ja)（`/v1` や `/v1beta` など）とモデルを使用していることを確認してください。たとえば、機能がベータ版でリリースされている場合、その機能は `/v1beta` API バージョンでのみ使用できます。

## 適切なモデルかどうかを確認する

[モデルのページ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)に記載されているサポート対象のモデルを使用していることを確認します。

## 思考モデルでのレイテンシまたはトークン使用量の増加

レイテンシやトークン使用量が増加するのは、Gemini 3.x モデルで思考がデフォルトで有効になっていることが原因であることがよくあります。非推奨の Gemini 2.5 モデルでも、デフォルトの思考が使用されます。

思考モデルは、品質を向上させるために内部推論トークンを生成します。この推論プロセスにより、レスポンスのレイテンシとトークンの合計消費量が増加します。

レイテンシの短縮を優先する場合や、費用を最小限に抑える必要がある場合は、思考レベルを下げるか、思考をオフにできます。

構成の詳細とコードサンプルについては、[思考ガイド](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#thinking-levels)をご覧ください。

## 安全性に関する問題

API 呼び出しで安全設定が原因でプロンプトがブロックされたというメッセージが表示された場合は、API 呼び出しで設定したフィルタに照らしてプロンプトを確認します。

`BlockedReason.OTHER` が表示された場合は、クエリまたはレスポンスが[利用規約](https://ai.google.dev/terms?hl=ja)に違反しているか、サポートされていない可能性があります。

## 朗読に関する問題

RECITATION という理由でモデルの出力生成が停止した場合は、モデル出力が特定のデータに類似している可能性があります。この問題を解決するには、プロンプト / コンテキストをできるだけ一意にし、Temperature を高くしてみてください。

## トークンの繰り返しに関する問題

出力トークンが繰り返し表示される場合は、次の提案を試して、出力トークンを減らすか、削除してください。

| 説明 | 原因 | 推奨される回避策 |
| --- | --- | --- |
| マークダウン テーブルのハイフンの繰り返し | これは、モデルが視覚的に整列された Markdown テーブルを作成しようとしたときに、テーブルの内容が長い場合に発生する可能性があります。ただし、Markdown の配置は正しくレンダリングするために必要ではありません。 | プロンプトに指示を追加して、Markdown テーブルを生成するための具体的なガイドラインをモデルに提供します。これらのガイドラインに沿った例を示します。温度を調整してみることもできます。コードやマークダウン テーブルなどの構造化された出力を生成する場合は、高い Temperature（0.8 以上）の方が効果的です。  以下は、この問題を回避するためにプロンプトに追加できるガイドラインの例です。     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| マークダウン テーブル内の繰り返しトークン | ハイフンが繰り返されるのと同様に、モデルがテーブルの内容を視覚的に揃えようとすると、この現象が発生します。Markdown の配置は、正しくレンダリングするために必須ではありません。 | - 次のような指示をシステム プロンプトに追加してみてください。      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - 温度を調整してみてください。温度が高い（0.8 以上）ほど、一般的に出力の繰り返しや重複を排除できます。 |
| 構造化された出力内の改行の繰り返し（`\n`） | モデル入力に `\u` や `\t` などの Unicode またはエスケープ シーケンスが含まれていると、改行が繰り返されることがあります。 | - プロンプトで禁止されているエスケープ シーケンスを確認し、UTF-8 文字に置き換えます。たとえば、JSON の例で `\u` エスケープ シーケンスを使用すると、モデルがその出力を生成する際に同じエスケープ シーケンスを使用する可能性があります。 - 許可されるエスケープについてモデルに指示します。次のようなシステム指示を追加します。      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| 構造化出力を使用したテキストの繰り返し | モデル出力で、定義された構造化スキーマとフィールドの順序が異なると、テキストが繰り返されることがあります。 | - プロンプトでフィールドの順序を指定しないでください。 - すべての出力フィールドを必須にします。 |
| ツールの呼び出しの繰り返し | これは、モデルが以前の思考のコンテキストを失った場合や、強制的に使用できないエンドポイントを呼び出した場合に発生する可能性があります。 | モデルに、思考プロセス内で状態を維持するように指示します。システム指示の末尾に以下を追加します。    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| 構造化された出力の一部ではない繰り返しテキスト | これは、モデルが解決できないリクエストでスタックした場合に発生する可能性があります。 | - 思考がオンになっている場合は、手順で問題を解決する方法を明示的に指示しないでください。最終的な出力のみをリクエストします。 - 温度を 0.8 以上に設定してみてください。 - 「簡潔に答えて」、「同じことを繰り返さないで」、「答えは 1 回だけ提供して」などの指示を追加します。 |

## ブロックされた API キーまたは機能しない API キー

このセクションでは、Gemini API キーがブロックされているかどうかを確認する方法と、ブロックされている場合の対処方法について説明します。

### キーがブロックされる理由

一部の API キーが一般公開されている可能性がある脆弱性が確認されました。お客様のデータを保護し、不正アクセスを防止するため、これらの既知の漏洩キーが Gemini API にアクセスできないように事前にブロックしました。

### 鍵が影響を受けるかどうかを確認する

キーが漏洩したことが判明した場合、そのキーを Gemini API で使用することはできません。[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) を使用すると、Gemini API の呼び出しがブロックされている API キーを確認し、新しいキーを生成できます。これらの鍵を使用しようとすると、次のエラーが返されることもあります。

```
Your API key was reported as leaked. Please use another API key.
```

### ブロックされた API キーに対するアクション

Gemini API インテグレーション用の新しい API キーは、[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) を使用して生成する必要があります。新しいキーが安全に保管され、公開されないように、API キーの管理方法を見直すことを強くおすすめします。

### 脆弱性による予期しない請求

[課金に関するサポートケースを送信します](https://console.cloud.google.com/support/chat?hl=ja)。請求チームが対応しております。進展がありましたら、できるだけ早くご連絡いたします。

### 漏洩した鍵に対する Google のセキュリティ対策

**API キーが漏洩した場合、Google はアカウントの費用超過や不正使用からどのように保護してくれますか？**

- [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) を使用して新しいキーをリクエストすると、API キーが発行されるようになります。この API キーはデフォルトで Google AI Studio にのみ制限され、他のサービスからのキーは受け付けられません。これにより、意図しないクロスキーの使用を防ぐことができます。
- Gemini API で使用される漏洩した API キーはデフォルトでブロックされるため、費用の不正使用やアプリケーション データの不正使用を防ぐことができます。
- API キーのステータスは [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) で確認できます。API キーの漏洩が確認された場合は、直ちに対処できるよう、Google からお客様に積極的にご連絡いたします。

## モデル出力を改善する

モデルの出力の品質を高めるには、より構造化されたプロンプトの作成を検討してください。[プロンプト エンジニアリング ガイド](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)のページでは、基本的なコンセプト、戦略、ベスト プラクティスについて説明します。

## トークンの上限について

トークンとその上限のカウント方法について詳しくは、[トークンガイド](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)をご覧ください。

## 既知の問題

- この API は、一部の言語のみをサポートしています。サポートされていない言語でプロンプトを送信すると、予期しないレスポンスが生成されたり、レスポンスがブロックされたりする可能性があります。最新情報については、[利用可能な言語](https://ai.google.dev/gemini-api/docs/models?hl=ja#supported-languages)をご覧ください。

## バグを報告する

ご不明な点がある場合は、[Google AI デベロッパー フォーラム](https://discuss.ai.google.dev?hl=ja)でディスカッションにご参加ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-04 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-04 UTC。"],[],[]]
