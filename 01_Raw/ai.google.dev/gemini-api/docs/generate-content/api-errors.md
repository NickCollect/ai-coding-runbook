---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=ja
fetched_at: 2026-10-12T07:05:57.569224+00:00
title: "API \u30a8\u30e9\u30fc \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash が利用可能になりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ja)。

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
| 400 | INVALID\_ARGUMENT | リクエストの本文の形式が正しくありません。 | リクエストに誤字脱字があるか、必須フィールドが入力されていません。 | リクエストの形式、例、サポートされているバージョンについては、[API リファレンス](https://ai.google.dev/api?hl=ja)をご覧ください。古いエンドポイントで新しい API バージョンの機能を使用すると、エラーが発生する可能性があります。 |
| 400 | FAILED\_PRECONDITION | Gemini API の無料枠は、お住まいの国ではご利用いただけません。Google AI Studio でプロジェクトの課金を有効にしてください。 | 無料枠がサポートされていないリージョンでリクエストを行っている。また、Google AI Studio のプロジェクトで課金が有効になっていない。 | Gemini API を使用するには、[Google AI Studio](https://aistudio.google.com/apikey?hl=ja) を使用して有料プランを設定する必要があります。 |
| 402 | RESOURCE\_EXHAUSTED | 前払いクレジットの残高がなくなりました。 | 請求先アカウントのプリペイド クレジットがなくなったため、その請求先アカウントにリンクされているすべての API キーが機能しなくなります。 | 請求先アカウントに[クレジットを追加](https://ai.google.dev/gemini-api/docs/billing?hl=ja#buy-credits)するか、[オートチャージ](https://ai.google.dev/gemini-api/docs/billing?hl=ja#auto-reload)をオンにします。このリクエストは再試行しないでください。クレジットが追加されるまで成功しません。 |
| 403 | PERMISSION\_DENIED | API キーに必要な権限がありません。 | 誤った API キーを使用している。[適切な認証](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ja)を行わずにチューニング済みモデルを使用しようとしている。 | API キーが設定され、適切なアクセス権が付与されていることを確認します。また、チューニング済みモデルを使用するには、適切な認証を行う必要があります。 |
| 404 | NOT\_FOUND | リクエストされたリソースが見つかりませんでした。 | リクエストで参照されている画像、音声、動画ファイルが見つかりませんでした。 | リクエスト内のすべてのパラメータが API バージョンに対して有効かどうかを確認します。 |
| 429 | RESOURCE\_EXHAUSTED | API のレート上限（RPM、TPM、RPD、費用など）のいずれかを超えています。 | リクエストの送信数が多すぎる、トークンの使用数が多すぎる、アカウントのお支払い履歴と階層に基づく上限を超えている。 | モデルの[レート上限](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja)を超えていないことを確認します。しばらく待ってから再試行してください。リクエストのレートまたはサイズを減らします。必要に応じて、[レート上限の引き上げをリクエスト](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja#request-rate-limit-increase)します。 |
| 499 | CANCELLED | オペレーションがキャンセルされました。通常、キャンセルは呼び出し元により行われます。 | API がレスポンスを完了する前に、クライアントが接続を閉じました。 | クライアントまたはネットワーク インフラストラクチャが接続を早期に終了しているかどうかを確認します（クライアントサイドのタイムアウトなど）。 |
| 500 | INTERNAL | Google 側で予期しないエラーが発生しました。 | 入力コンテキストが長すぎます。 | [Gemini API のステータス ページ](https://aistudio.google.com/status?hl=ja)で、進行中のインシデントがないか確認します。入力コンテキストを減らすか、別のモデルに一時的に切り替えて（Gemini 2.5 Pro から Gemini 2.5 Flash など）、動作するかどうかを確認します。しばらく待ってから、もう一度リクエストしてみてください。再試行しても問題が解決しない場合は、Google AI Studio の [**フィードバックを送信**] ボタンを使用してご報告ください。 |
| 503 | UNAVAILABLE | サービスが一時的に過負荷状態になっているか、ダウンしている可能性があります。 | サービスが一時的に容量不足になっています。 | [Gemini API のステータス ページ](https://aistudio.google.com/status?hl=ja)で、進行中のインシデントがないか確認します。別のモデルに一時的に切り替えて（Gemini 2.5 Pro から Gemini 2.5 Flash など）、動作するかどうかを確認します。しばらく待ってから、もう一度リクエストしてみてください。再試行しても問題が解決しない場合は、Google AI Studio の [**フィードバックを送信**] ボタンを使用してご報告ください。 |
| 504 | DEADLINE\_EXCEEDED | サービスが期限内に処理を完了できません。 | プロンプト（またはコンテキスト）が大きすぎて、時間内に処理できません。 | このエラーを回避するには、クライアント リクエストで「タイムアウト」を大きく設定します。 |

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
| `details` | 配列 | `ErrorInfo` や `LocalizedMessage` などのエラーの追加コンテキスト。 |

## 次のステップ

- [API のトラブルシューティング](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja): 一般的な問題とエラー シナリオを解決します。
- [レート制限](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja): リクエストの上限と割り当ての処理について学習します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-20 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-20 UTC。"],[],[]]
