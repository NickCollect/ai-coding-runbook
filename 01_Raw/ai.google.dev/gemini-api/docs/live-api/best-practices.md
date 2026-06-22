---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=ja
fetched_at: 2026-06-22T06:30:24.187257+00:00
title: "Live API \u306e\u30d9\u30b9\u30c8 \u30d7\u30e9\u30af\u30c6\u30a3\u30b9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Live API のベスト プラクティス

このガイドでは、Live API の使用を最適化するために従うことができるベスト プラクティスについて説明します。
概要と一般的なユースケースのサンプルコードについては、[Live API を使ってみる](https://ai.google.dev/gemini-api/docs/live?hl=ja)
をご覧ください。

## 明確なシステム指示を設計する

Live API のパフォーマンスを最大限に引き出すには、エージェントのペルソナ、会話ルール、ガードレールをこの順序で明確に定義した、一連のシステム指示（SI）を用意することをおすすめします。

最適な結果を得るには、各エージェントを個別の SI に分割します。

1. **エージェントのペルソナを指定する:** エージェントの名前、役割、望ましい特性について詳しく説明します。アクセントを指定する場合は、優先する出力言語（英語話者の場合は英国のアクセントなど）も必ず指定してください。
2. **会話ルールを指定する:** モデルに適用する順序でルールを記述します。会話の 1 回限りの要素と会話ループを区別します。例:

   - **1 回限りの要素:** お客様の詳細情報（名前、ロケーション、ポイントカード番号など）を 1 回収集します。
   - **会話ループ:** ユーザーは、おすすめ、価格、返品、配達について話し合うことができ、トピックからトピックへと移動したい場合があります。ユーザーが望む限り、この会話ループを継続してもよいことをモデルに伝えます。
3. **フロー内のツール呼び出しを個別の文で指定する:** たとえば、お客様の詳細情報を収集する 1 回限りのステップで `get_user_info` 関数を呼び出す必要がある場合、最初のステップはユーザー情報の収集です。*まず、お客様に名前、ロケーション、ポイントカード番号の提供を依頼します。*次に、これらの詳細情報を使用して `get_user_info` を呼び出します。
4. **必要なガードレールを追加します。**モデルに実行させたくない一般的な会話のガードレールを指定します。x が発生した場合にモデルに y を実行させたい場合は、具体的な例を自由に指定してください。それでも望ましいレベルの精度が得られない場合は、unmistakably という単語を使用して、モデルが正確になるようにガイドします。

## ツールを正確に定義する

Live API でツールを使用する場合は、ツール定義を具体的に記述します。
ツール呼び出しを呼び出す条件を Gemini に必ず伝えてください。詳細については、[ツール定義](#tool-definitions-example)の
例のセクションをご覧ください。

## 効果的なプロンプトを作成する

- **明確なプロンプトを使用する:** プロンプトで、モデルが実行すべきことと実行すべきでないことの例を示します。また、プロンプトは一度に 1 つのペルソナまたはロールにつき 1 つに制限するようにします。長い複数ページのプロンプトではなく、プロンプト チェーンの使用を検討してください。このモデルは、単一の関数呼び出しを含むタスクで最適なパフォーマンスを発揮します。
- **開始コマンドと情報を提供する:** Live API は、応答する前にユーザー入力を想定しています。Live API に会話を開始させるには、ユーザーに挨拶するか、会話を開始するよう求めるプロンプトを含めます。Live API であいさつをパーソナライズするために、ユーザーに関する情報を含めます。

## 言語を指定する

Live API のカスケード `gemini-live-2.5-flash` で最適なパフォーマンスを得るには、API の `language_code` がユーザーが話す言語と一致していることを確認してください。

モデルが英語以外の言語で応答することを想定している場合は、システム指示の一部として次の内容を含めます。

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## ストリーミング

リアルタイム音声を実装する際は、次のベスト プラクティスを参考にしてください。

- **チャンクサイズとレイテンシ**: 20～40 ミリ秒のチャンクで音声を送信します。
- **割り込み処理**: モデルが返信している間にユーザーが発話すると、サーバーは `"interrupted": true` を含む `server_content` メッセージを送信します。エージェントがユーザーに話しかけ続けるのを防ぐため、クライアントサイドの音声バッファを直ちに破棄する必要があります。

## コンテキスト管理

ネイティブ音声トークンは急速に蓄積されるため（音声 1 秒あたり約 25 トークン）、長いセッションの場合は `ContextWindowCompressionConfig` を使用します。

## クライアント バッファリング

送信前に、入力音声を大幅に（1 秒など）バッファリングしないでください。レイテンシを最小限に抑えるため、小さなチャンク（20～100 ミリ秒）で送信してください。

## 再サンプリング

クライアント アプリケーションが、送信前にマイク入力（通常は 44.1 kHz または 48 kHz）を 16 kHz に再サンプリングするようにしてください。

## セッション管理

セッションのライフサイクルを処理し、信頼性の高いユーザー エクスペリエンスを確保するには、次のガイドラインに沿ってください。

- **コンテキスト ウィンドウの圧縮を有効にする:** 音声トークンは 1 秒あたり約 25 トークンの割合で蓄積されます。圧縮しない場合、音声のみのセッションは 15 分、音声と動画のセッションは 2 分に制限されます。[コンテキスト ウィンドウの圧縮を有効にすると、セッションを無制限に延長できます。](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ja#context-window-compression)
- **セッションの再開を実装する:** サーバーは WebSocket 接続を定期的にリセットする場合があります。[セッションの再開を使用すると、コンテキストを失うことなくシームレスに再接続できます。](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ja#session-resumption)`SessionResumptionUpdate` メッセージから最新の再開トークンを保持し、再接続時にハンドルとして渡します。再開トークンは、最後のセッションが終了してから 2 時間有効です。
- **GoAway メッセージを処理する:** サーバーは、接続を終了する前に
  [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ja#goaway-message) メッセージを送信します。このメッセージをリッスンし、`timeLeft` フィールドを使用して、接続が閉じる前に正常に終了するか、再接続します。
- **generationComplete シグナルを処理する:**
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ja#generation-complete-message)
  メッセージを使用すると、モデルがレスポンスの生成を完了したタイミングを把握できるため、
  アプリケーションで UI を更新したり、次のアクションに進んだりできます。

実装の詳細については、
[セッション管理](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ja)をご覧ください。

## 例

この例では、ベスト プラクティスと
[システム指示の設計に関するガイドライン](#system-instruction-guidelines)の両方を組み合わせて、
キャリアコーチとしてのモデルのパフォーマンスをガイドしています。

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### ツール定義

この JSON は、キャリアコーチの例で呼び出される関連関数を定義します。関数を定義する際は、名前、説明、パラメータ、呼び出し条件を含めると、最適な結果が得られます。

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## 料金と課金

Gemini Live API は、トークンの使用量に応じて厳密に課金されます。Live API は永続的な WebSocket セッションを維持するため、課金はアクティブなコンテキスト ウィンドウに基づく複合モデルに従います。

### セッション コンテキスト ウィンドウ（複合費用）

API は、セッション コンテキスト ウィンドウに存在するすべてのトークンに対してターンごとに課金します。「ターン」とは、ユーザー入力 1 回とモデルの対応するレスポンスを指します。

- **蓄積:** コンテキスト ウィンドウには、現在のターンの新しいトークンと、以前のターンから蓄積されたすべてのトークンが含まれます。
- **再課金:** 過去のトークンは、構成されたコンテキスト ウィンドウ サイズまで、新しいターンごとに再処理され、計上されます。セッションが長くなるほど、会話履歴が再処理されるため、ターンあたりの費用が増加します。

### 音声トークンと文字起こし

Live API はネイティブでマルチモーダルです。音響のニュアンスとトーンを保持するため、会話履歴を生の音声トークンとして保持します。

- **音声の課金:** API は、ターンごとに蓄積されたネイティブ音声トークンに対して、標準の音声入力レートで課金します。
- **文字起こし追加料金:** 音声からテキストへの文字起こしが有効になっている場合（`inputAudioTranscription` または `outputAudioTranscription`）、API は、標準の音声トークン費用に加えて、文字起こし用に生成されたすべてのテキスト トークンに対してテキスト トークン出力レートで課金します。

### コンテキスト制限による費用の管理

長いセッションで費用が際限なく増加しないようにするには、`contextWindowCompression` を使用してコンテキスト ウィンドウ サイズを構成します。

圧縮トリガー（25,000 トークンなど）とスライディング ウィンドウ（8,000 トークンなど）を設定すると、しきい値に達した時点で古いトークンが自動的に削除されます。その後、API は保持された履歴と新しいトークンに対してのみ、後続のターンを課金します。

### プロアクティブ音声モード

プロアクティブ音声モードが有効になっている場合、入力トークンは Live API がリッスンしている間ずっと課金されますが、出力トークンは API が応答したときにのみ課金されます。

- **Gemini 3.1 の注意:** プロアクティブ音声モードは `gemini-3.1-flash-live-preview` ではサポートされていません。このモデルでは、入力のストリーミングを積極的に行っている場合にのみ、音声に対して課金されます。

料金の詳細については、[Gemini API の料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
