---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=ja
fetched_at: 2026-10-26T05:43:01.172129+00:00
title: "API \u30a8\u30e9\u30fc \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# API エラー

このページでは、`GenerateContent` API から返されるバックエンド エラーコードのリファレンス、gRPC エラー レスポンスの形式、トラブルシューティングの手順について説明します。

## HTTP エラーコード

次の表に、一般的なバックエンド エラーコード、その原因の説明、推奨される解決策を示します。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP コード** | ステータス | **説明** | **例** | **ソリューション** |
| 400 | INVALID\_ARGUMENT | リクエストの本文の形式が正しくありません。 | リクエストに入力ミスがあるか、必須フィールドがありません。 | リクエストの形式、例、サポートされているバージョンについては、[API リファレンス](https://ai.google.dev/api?hl=ja)をご覧ください。古いエンドポイントで新しい API バージョンの機能を使用すると、エラーが発生する可能性があります。 |
| 400 | FAILED\_PRECONDITION | Gemini API の無料枠は、お住まいの国ではご利用いただけません。Google AI Studio でプロジェクトの課金を有効にしてください。 | 無料枠がサポートされていないリージョンでリクエストを行っており、Google AI Studio のプロジェクトで課金が有効になっていない。 | Gemini API を使用するには、[Google AI Studio](https://aistudio.google.com/apikey?hl=ja) を使用して有料プランを設定する必要があります。 |
| 402 | RESOURCE\_EXHAUSTED | 前払いクレジット残高が不足しています。 | 請求先アカウントの前払いクレジットがなくなったため、その請求先アカウントにリンクされているすべての API キーが機能しなくなります。 | 請求先アカウントに[クレジットを追加](https://ai.google.dev/gemini-api/docs/billing?hl=ja#buy-credits)するか、[オートチャージ](https://ai.google.dev/gemini-api/docs/billing?hl=ja#auto-reload)をオンにしてください。このリクエストは再試行しないでください。クレジットが追加されるまで成功しません。 |
| 403 | PERMISSION\_DENIED | API キーに必要な権限がないか、プロジェクトの API アクセスが制限されています。 | 間違った API キーまたは漏洩した API キーを使用している、プロジェクトが無料枠の対象外である、請求先アカウントに未払い残高がある、または[適切な認証](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ja)を行わずにチューニング済みモデルを使用しようとしている。 | API キーが有効でアクティブであることを確認し、[Google AI Studio](https://aistudio.google.com/billing?hl=ja) でプロジェクトの課金とティアのステータスを確認します。または、[プロジェクトが制限されているか、利用できない場合のトラブルシューティング](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja#project-unavailable)をご覧ください。 |
| 404 | NOT\_FOUND | リクエストされたリソースが見つかりませんでした。 | リクエストで参照されている画像、音声、動画ファイルが見つかりませんでした。 | リクエスト内のすべてのパラメータが API バージョンに対して有効かどうかを確認します。 |
| 429 | RESOURCE\_EXHAUSTED | API のレート制限（RPM、TPM、RPD、費用など）のいずれかを超えている。 | 送信しているリクエストが多すぎるか、使用しているトークンが多すぎるか、アカウントのお支払い履歴と階層の費用ベースの上限を超えています。 | モデルの[レート制限](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja)内であることを確認します。しばらく待ってから再試行します。リクエストのレートまたはサイズを小さくします。必要に応じて、[レート制限の引き上げをリクエスト](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja#request-rate-limit-increase)します。 |
| 499 | CANCELLED | オペレーションがキャンセルされました。通常、キャンセルは呼び出し元により行われます。 | API がレスポンスを完了する前に、クライアントが接続を終了しました。 | クライアントまたはネットワーク インフラストラクチャが接続を早期に終了していないか確認します（例: クライアントサイドのタイムアウト）。 |
| 500 | 社内向け | Google 側で予期しないエラーが発生しました。 | 入力コンテキストが長すぎます。 | [Gemini API のステータス ページ](https://aistudio.google.com/status?hl=ja)で、進行中のインシデントがないか確認します。入力コンテキストを減らすか、一時的に別のモデルに切り替えて（Gemini 2.5 Pro から Gemini 2.5 Flash など）、動作するかどうかを確認します。または、しばらくしてからリクエストを再試行してください。再試行しても問題が解決しない場合は、Google AI Studio の [**フィードバックを送信**] ボタンを使用して報告してください。 |
| 503 | UNAVAILABLE | サービスが一時的に過負荷状態になっているか、停止している可能性があります。 | サービスが一時的に容量不足になっています。 | [Gemini API のステータス ページ](https://aistudio.google.com/status?hl=ja)で、進行中のインシデントがないか確認します。一時的に別のモデルに切り替えて（例: Gemini 2.5 Pro から Gemini 2.5 Flash）、動作するかどうかを確認します。または、しばらくしてからリクエストを再試行してください。再試行しても問題が解決しない場合は、Google AI Studio の [**フィードバックを送信**] ボタンを使用して報告してください。 |
| 504 | DEADLINE\_EXCEEDED | サービスが期限内に処理を完了できない。 | プロンプト（またはコンテキスト）が大きすぎて、時間内に処理できません。 | このエラーを回避するには、クライアント リクエストで「timeout」を大きく設定します。 |

## エラー レスポンスの形式

`GenerateContent` リクエストが失敗すると、API は HTTP ステータス コード（`400 Bad Request`、`403 Forbidden`、`429 Too Many Requests` など）を設定し、gRPC ステータスの詳細を含む JSON レスポンス本文を返します。

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| フィールド | タイプ | 説明 |
| --- | --- | --- |
| `code` | integer | HTTP ステータス コード。 |
| `message` | 文字列 | エラーの説明（人が読める形式）。 |
| `status` | 文字列 | `SCREAMING_CASE` の gRPC ステータス コード。 |
| `details` | 配列 | 追加のエラー コンテキスト（`ErrorInfo` や `LocalizedMessage` など）。 |

## 次のステップ

- [API のトラブルシューティング](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja): 一般的な問題とエラーのシナリオを解決します。
- [レート制限](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja): リクエストの上限と割り当ての処理について説明します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-23 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-23 UTC。"],[],[]]
