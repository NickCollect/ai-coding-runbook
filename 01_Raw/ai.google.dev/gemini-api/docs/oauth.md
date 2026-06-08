---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=ja
fetched_at: 2026-06-08T05:37:23.727760+00:00
title: "OAuth \u306b\u3088\u308b\u8a8d\u8a3c\u306e\u30af\u30a4\u30c3\u30af\u30b9\u30bf\u30fc\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# OAuth による認証のクイックスタート

Gemini API への認証の最も簡単な方法は、
[Gemini API クイックスタート](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja)の説明に従って API キーを構成することです。より厳格なアクセス制御が必要な場合は、代わりに OAuth を使用できます。このガイドでは、OAuth を使用して認証を設定する方法について説明します。

このガイドでは、テスト環境に適した簡素化された認証方法を使用します。[[本番環境の場合は、アプリに適したアクセス認証情報を選択する前に、認証と認可について学習してください。](https://developers.google.com/workspace/guides/auth-overview?hl=ja)](https://developers.google.com/workspace/guides/create-credentials?hl=ja#choose_the_access_credential_that_is_right_for_you)

## 目標

- OAuth 用にクラウド プロジェクトを設定する
- アプリケーションのデフォルト認証情報を設定する
- `gcloud auth` を使用する代わりに、プログラムで認証情報を管理する

## 前提条件

このクイックスタートを実行するには、次のものが必要です。

- [Google Cloud プロジェクト](https://developers.google.com/workspace/guides/create-project?hl=ja)
- [gcloud CLI のローカル インストール](https://cloud.google.com/sdk/docs/install?hl=ja)

## クラウド プロジェクトを設定する

このクイックスタートを完了するには、まず Cloud プロジェクトを設定する必要があります。

### 1. API を有効にする

Google API を使用する前に、Google Cloud プロジェクトで API を有効にする必要があります。

- Google Cloud コンソールで、Google Generative Language API を有効にします。

  [API を有効にする](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=ja)

### 2. OAuth 同意画面を構成する

次に、プロジェクトの OAuth 同意画面を構成し、テストユーザーとして自分を追加します。Cloud プロジェクトでこの手順をすでに完了している場合は、次のセクションに進んでください。

1. Google Cloud コンソールで、**メニュー** > **Google Auth Platform** > [**概要**] に移動します。

   [Google Auth Platform に移動](https://console.developers.google.com/auth/overview?hl=ja)
2. プロジェクト構成フォームに記入し、[**対象ユーザー**] セクションでユーザータイプを [**外部**] に設定します。
3. フォームの残りの部分を入力し、ユーザーデータに関するポリシーの条項に同意して、[**作成**] をクリックします。
4. ここでは、スコープの追加をスキップして、[**保存して次へ**] をクリックします。今後、Google Workspace 組織外で使用するアプリを作成する場合は、アプリに必要な認可スコープを追加して確認する必要があります。
5. テストユーザーを追加します。

   1. Google Auth Platform の
      [[対象ユーザー] ページ](https://console.developers.google.com/auth/audience?hl=ja)に移動します。
   2. [**テストユーザー**] で [**ユーザーを追加**] をクリックします。
   3. メールアドレスと他の承認済みテストユーザーを入力し、[**保存**] をクリックします。

### 3. デスクトップ アプリケーションの認証情報を承認する

エンドユーザーとして認証を行い、アプリ内でユーザーデータにアクセスするには、1 つ以上の OAuth 2.0 クライアント ID を作成する必要があります。クライアント ID は、Google の OAuth サーバーで個々のアプリを識別するために使用します。アプリが複数のプラットフォームで実行される場合は、プラットフォームごとに個別のクライアント ID を作成する必要があります。

1. Google Cloud コンソールで、**メニュー** > **Google Auth Platform** > [**クライアント**] に移動します。

   [[認証情報] に移動](https://console.developers.google.com/auth/clients?hl=ja)
2. [**クライアントの作成**] をクリックします。
3. [**アプリケーション タイプ**] > [**デスクトップ アプリ**] をクリックします。
4. [**名前**] フィールドに、認証情報の名前を入力します。この名前は Google Cloud コンソールにのみ表示されます。
5. [**作成**] をクリックします。[OAuth クライアントを作成しました] 画面が表示され、新しいクライアント ID とクライアント シークレットが表示されます。
6. [**OK**] をクリックします。新しく作成した認証情報が [**OAuth 2.0 クライアント ID**] に表示されます。
7. ダウンロード ボタンをクリックして JSON ファイルを保存します。
   `client_secret_<identifier>.json` として保存されます。名前を `client_secret.json`
   に変更して、作業ディレクトリに移動します。

## アプリケーションのデフォルト認証情報を設定する

`client_secret.json` ファイルを使用可能な認証情報に変換するには、その場所を `gcloud auth application-default login` コマンドの `--client-id-file` 引数に渡します。

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

このチュートリアルの簡素化されたプロジェクト設定では、[**"Google はこのアプリを確認していません"**] ダイアログが表示されます。これは正常です、[**続行**]を選択します。

これにより、結果のトークンが既知の場所に配置され、`gcloud` またはクライアント ライブラリからアクセスできるようになります。

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

アプリケーションのデフォルト認証情報（ADC）を設定すると、ほとんどの言語のクライアント ライブラリは、最小限の操作で認証情報を検索できます。

### Curl

これが機能していることをテストする最も簡単な方法は、curl を使用して REST API にアクセスすることです。

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

Python では、クライアント ライブラリが自動的に検索します。

```
pip install google-genai
```

テスト用の最小限のスクリプトは次のとおりです。

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## 次のステップ

これが機能したら、テキストデータで
[セマンティック検索](https://ai.google.dev/docs/semantic_retriever?hl=ja)を試すことができます。

## 認証情報を自分で管理する [Python]

多くの場合、クライアント ID（`client_secret.json`）からアクセス トークンを作成するために `gcloud` コマンドを使用できません。Google は、アプリ内でそのプロセスを管理できるように、多くの言語でライブラリを提供しています。このセクションでは、Python でのプロセスについて説明します。他の言語での同様の手順の例については、
[Drive API のドキュメント](https://developers.google.com/drive/api/quickstart/python?hl=ja)をご覧ください。

### 1. 必要なライブラリをインストールする

Python 用の Google クライアント ライブラリと Gemini クライアント ライブラリをインストールします。

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. 認証情報マネージャーを作成する

認証画面を何度もクリックする必要がないように、作業ディレクトリに `load_creds.py` というファイルを作成します。このファイルは、後で再利用できる `token.json` ファイルをキャッシュします。有効期限が切れた場合は更新されます。

次のコードから始めて、`client_secret.json` ファイルを `genai.configure` で使用できるトークンに変換します。

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. プログラムを作成する

次に、`script.py` を作成します。

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. プログラムを実行する

作業ディレクトリで、サンプルを実行します。

```
python script.py
```

スクリプトを初めて実行すると、ブラウザ ウィンドウが開き、アクセス権の承認を求められます。

1. Google アカウントにログインしていない場合は、ログインを求められます。複数のアカウントにログインしている場合は、**プロジェクトの構成時に [テスト アカウント] として設定したアカウントを選択してください。**
2. 認可情報はファイル システムに保存されるため、次回サンプルコードを実行するときに認可を求められることはありません。

認証の設定が完了しました。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
