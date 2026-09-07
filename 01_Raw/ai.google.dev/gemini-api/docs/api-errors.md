---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=ja
fetched_at: 2026-09-07T05:45:27.646581+00:00
title: "API \u30a8\u30e9\u30fc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# API エラー

このページでは、Interactions API のすべてのエラーコードのリファレンスを提供し、エラー レスポンスの形式について説明します。また、リクエスト タイプごとに API がエラーを配信する方法についても説明します。

## 標準の API エラーコード

これらの一般的なリクエストレベルのエラーコードは、標準の HTTP ステータス コードに対応しています。
アプリケーション ロジックで `code` フィールドを使用して、エラーをプログラムで処理します。

| コード | HTTP ステータス | 説明 | 推奨される対応 |
| --- | --- | --- | --- |
| `invalid_request` | 400 不正なリクエスト | リクエストの形式が正しくないか、無効なパラメータが含まれています。 | [API リファレンス](https://ai.google.dev/api/interactions-api?hl=ja)に照らして入力を確認してください。 |
| `parameter_unknown` | 400 不正なリクエスト | リクエストに不明なパラメータが含まれています。 | 認識されないパラメータを削除して、もう一度お試しください。 |
| `authentication` | 401 Unauthorized（未承認） | API キーがないか、無効です。 | [API キー](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)を確認してください。 |
| `permission_denied` | 403 Forbidden（アクセス拒否） | API キーにこのリソースに対する権限がありません。 | API キーの権限とプロジェクトへのアクセス権を確認してください。 |
| `not_found` | 404 見つかりません | リクエストされたリソースが見つかりませんでした。 | リソースパスとパラメータを確認してください。 |
| `model_not_found` | 404 見つかりません | 指定されたモデルが見つかりませんでした。 | モデル名を確認するか、別のモデルにフォールバックしてください。 |
| `rate_limit_exceeded` | 429 Too Many Requests（リクエスト数が多すぎる） | 1 分あたりまたは 1 秒あたりのリクエスト数またはトークンの上限を超えました。 | 指数バックオフを利用して、待機と再試行を繰り返してください。 |
| `quota_exceeded` | 429 Too Many Requests（リクエスト数が多すぎる） | 1 日あたりの割り当てを超過しました。 | 割り当てがリセットされるまで待つか、割り当ての増加をリクエストしてください。 |
| `cancelled` | 499 クライアントがリクエストをクローズしました | クライアントがリクエストの完了前にキャンセルしました。 | 何もする必要はない。通常、これはクライアントが切断されたことを意味します。 |
| `api_error` | 500 Internal Server Error（内部サーバーエラー） | サーバーで予期しないエラーが発生しました。 | リクエストを再試行してください。問題が解決しない場合は、サポートにお問い合わせください。 |
| `service_unavailable` | 503 Service Unavailable（サービス利用不可） | サービスが一時的に過負荷状態になっているか、ダウンしています。 | 指数バックオフを利用して、待機と再試行を繰り返してください。 |

## 生成がブロックされたコード

これらのエラーコードは、ポリシー、安全性、コンテンツの制限によりモデルの出力がブロックされたことを示します。これらのコードのいずれかを受け取った場合は、入力を変更して再試行してください。

| コード | 説明 |
| --- | --- |
| `safety` | 安全性の違反（有害なコンテンツ）によりリクエストがブロックされました。 |
| `recitation` | 著作権または朗読の制限によりリクエストがブロックされました。 |
| `language` | サポートされていない言語によりリクエストがブロックされました。 |
| `prohibited_content` | 禁止コンテンツに関するガイドラインによりリクエストがブロックされました。 |
| `spii` | 個人を特定できる機密情報の制限によりリクエストがブロックされました。 |
| `blocklist` | ブロックリストの禁止用語によりリクエストがブロックされました。 |
| `image_safety` | 安全性の違反により画像の生成がブロックされました。 |
| `image_prohibited_content` | 禁止コンテンツに関するガイドラインにより画像の生成がブロックされました。 |
| `image_recitation` | 著作権または朗読の制限により画像の生成がブロックされました。 |
| `image_other` | 不明な理由により画像の生成がブロックされました。 |
| `content_blocked` | 不明なポリシー上の理由によりリクエストがブロックされました。 |

## 生成エラーコード

これらのエラーコードは、モデルで生成された出力の構造上の問題（形式が正しくない関数呼び出しや、宣言されていないツール呼び出しなど）を示します。

| コード | 説明 |
| --- | --- |
| `malformed_function_call` | モデルが、解析できない関数呼び出しを生成しました。 |
| `malformed_tool_call` | モデルが、解析できないツール呼び出しを生成しました。 |
| `unexpected_tool_call` | モデルが、リクエストで宣言されていないツールを呼び出しました。 |
| `no_image` | モデルが画像を生成できませんでした。 |
| `too_many_tool_calls` | モデルが、許可されている数よりも多くのツール呼び出しを生成しました。 |
| `missing_thought_signature` | レスポンスに必要な思考署名がありません。 |

## エラー レスポンスの形式

Interactions API からのエラーはすべて、`error` を含む `code` と `message` オブジェクトを返します。たとえば、サポートされていないツールタイプを渡すと、次のようになります。

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| フィールド | タイプ | 説明 |
| --- | --- | --- |
| `code` | 文字列 | `snake_case` の機械可読形式のエラーコード。 |
| `message` | 文字列 | 発生した問題の説明（人が読める形式）。 |

## エラーの配信方法

API は、標準の HTTP リクエストを行うか、ストリーミング（SSE）リクエストを行うかによって、エラーの配信方法が異なります。

### 標準の HTTP リクエスト

標準（非ストリーミング）リクエストの場合、API は HTTP レスポンス ステータス コード（`400 Bad Request`、`401 Unauthorized`、`429 Too Many Requests` など）を設定し、JSON レスポンス本文に `error` オブジェクトを返します。

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### ストリーミング（SSE）リクエスト

ストリーミング リクエスト（`stream: true`）の場合、API はサーバー送信イベント（SSE）ストリームを介して `event_type` が `"error"` に設定されたエラーイベントを送信します。`error` フィールドには、同じ `code` と `message` 構造が含まれます。

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

SSE イベント スキーマの詳細については、[Interactions API リファレンス](https://ai.google.dev/api/interactions-api?hl=ja)をご覧ください。

## 次のステップ

- [API のトラブルシューティング](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja): よくある問題とエラー シナリオを解決する。
- [レート制限](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja): リクエストの上限と割り当ての処理について学習する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
