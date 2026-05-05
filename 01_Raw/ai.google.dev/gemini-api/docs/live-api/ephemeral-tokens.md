---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ja
fetched_at: 2026-05-05T20:45:57.919142+00:00
title: "Ephemeral tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Ephemeral tokens

エフェメラル トークンは、[WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) を介して Gemini
API にアクセスするための有効期間の短い認証トークンです。ユーザーのデバイスから API に直接接続する場合（
[クライアントからサーバーへの](https://ai.google.dev/gemini-api/docs/live?hl=ja#implementation-approach)
実装）のセキュリティを強化するように設計されています。標準の API キーと同様に、エフェメラル トークンはウェブブラウザやモバイルアプリなどのクライアントサイド アプリケーションから抽出できます。ただし、エフェメラル
トークンは有効期限が短く、制限できるため、本番環境でのセキュリティ リスクを大幅に軽減できます。クライアントサイド アプリケーションから Live
API に直接アクセスして API キーのセキュリティを強化する場合は、エフェメラル トークンを使用する必要があります。

## エフェメラル トークンの仕組み

エフェメラル トークンの仕組みの概要は次のとおりです。

1. クライアント（ウェブアプリなど）がバックエンドで認証されます。
2. バックエンドが Gemini API のプロビジョニング サービスにエフェメラル トークンをリクエストします。
3. Gemini API が有効期間の短いトークンを発行します。
4. バックエンドが、Live API への WebSocket 接続用のトークンをクライアントに送信します。これを行うには、API キーをエフェメラル トークンに置き換えます。
5. クライアントは、トークンを API キーとして使用します。

![一時トークンの概要](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=ja)

クライアントサイドにデプロイされた有効期間の長い API キーとは異なり、トークンは抽出されても有効期間が短いため、セキュリティが強化されます。クライアントが Gemini に直接データを送信するため、レイテンシが改善され、バックエンドでリアルタイム データをプロキシする必要がなくなります。

## エフェメラル トークンを作成する

Gemini からエフェメラル トークンを取得する方法の簡単な例を次に示します。
デフォルトでは、このリクエストのトークン（`newSessionExpireTime`）を使用して新しい Live API セッションを開始するのに 1 分、その接続でメッセージを送信するのに 30 分（`expireTime`）かかります。

### Python

```
import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

  const token: AuthToken = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

`expireTime` の値の制約、デフォルト値、その他のフィールド仕様については、
[API リファレンス](https://ai.google.dev/api/live?hl=ja#ephemeral-auth-tokens)をご覧ください。
`expireTime` の期間内に、10 分ごとに呼び出しを再接続するには
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=ja#session-resumption) が必要です（これは、
if `uses: 1` の場合でも同じトークンで行うことができます）。

エフェメラル トークンを一連の構成にロックすることもできます。これは、アプリケーションのセキュリティをさらに強化し、システム命令をサーバーサイドに保持するのに役立ちます。

### Python

```
client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

フィールドのサブセットをロックすることもできます。詳細については、[SDK のドキュメント](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
をご覧ください。

## エフェメラル トークンを使用して Live API に接続する

エフェメラル トークンを取得したら、API キーと同じように使用します（ただし、Live API でのみ、API の `v1alpha` バージョンでのみ機能します）。

[エフェメラル トークンの使用は、クライアントからサーバーへの実装アプローチに従うアプリケーション
をデプロイする場合にのみ有効です。](https://ai.google.dev/gemini-api/docs/live?hl=ja#implementation-approach)

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

その他の例については、[Live API のスタートガイド](https://ai.google.dev/gemini-api/docs/live?hl=ja)をご覧ください。

## ベスト プラクティス

- `expire_time` パラメータを使用して、有効期限を短く設定します。
- トークンは期限切れになるため、プロビジョニング プロセスを再開する必要があります。
- 独自のバックエンドの安全な認証を確認します。エフェメラル トークンのセキュリティは、バックエンドの認証方法と同じレベルになります。
- 通常、このパスは安全と見なされるため、バックエンドから Gemini への接続にエフェメラル トークンを使用することは避けてください。

## 制限事項

現時点では、エフェメラル トークンは [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) とのみ互換性があります。

## 次のステップ

- 詳細については、エフェメラル トークンに関する Live API [リファレンス](https://ai.google.dev/api/live?hl=ja#ephemeral-auth-tokens)
  をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
