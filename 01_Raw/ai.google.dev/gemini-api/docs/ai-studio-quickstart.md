---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ja
fetched_at: 2026-07-20T04:42:38.791966+00:00
title: "Google AI Studio \u306e\u30af\u30a4\u30c3\u30af\u30b9\u30bf\u30fc\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google AI Studio のクイックスタート

[Google AI Studio](https://aistudio.google.com/?hl=ja) を使用すると、さまざまなプロンプトでモデルを簡単に試すことができます。構築の準備ができたら、[Get code] を選択し、好みのプログラミング言語で [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=ja) の使用を開始できます。

## プロンプトと設定

Google AI Studio には、さまざまなユースケース向けに設計されたプロンプト用のインターフェースが複数用意されています。このガイドでは、会話機能の構築に使用される**チャット プロンプト**について説明します。このプロンプト技法では、複数の入力とレスポンスのターンを使用して出力を生成できます。詳しくは、[以下のチャット プロンプトの例](#chat_example)をご覧ください。他にも、**リアルタイム ストリーミング**、**動画生成**などのオプションがあります。

AI Studio には、**実行設定**パネルもあります。このパネルでは、[モデル パラメータ](https://ai.google.dev/docs/prompting-strategies?hl=ja#model-parameters)、[安全設定](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)を調整したり、[構造化された出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)、[グラウンディング](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)などのツールを切り替えたりできます。

## チャット プロンプトの例: カスタム チャット アプリケーションを作成する

[Gemini](https://gemini.google.com/?hl=ja) などの汎用 chatbot を使用したことがある場合は、生成 AI モデルがオープンエンドのダイアログにどれほど強力であるかを直接体験したことがあるでしょう。汎用チャットボットは便利ですが、特定のユースケースに合わせて調整する必要があることがよくあります。

たとえば、自社製品に関する会話のみをサポートするカスタマー サービス chatbot を構築するとします。特定のトーンやスタイルで話す chatbot を作成したい場合があります。たとえば、ジョークをたくさん言う bot、詩人のように韻を踏む bot、回答に絵文字をたくさん使う bot などです。

この例では、Google AI Studio を使用して、木星の衛星の 1 つであるエウロパに住むエイリアンのように会話するフレンドリーなチャットボットを構築する方法を示します。

### ステップ 1 - チャット プロンプトを作成する

chatbot を構築するには、ユーザーと chatbot の間のやり取りの例を提供して、モデルが求める回答を提供できるようにする必要があります。

チャット プロンプトを作成するには:

1. [Google AI Studio](https://aistudio.google.com/?hl=ja) を開きます。**Playground** は、新しいチャット プロンプトとともにデフォルトで開きます。
2. 右上にある [**実行設定**] tune をクリックしてパネルを開き、[[**システム指示**](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#system-instructions)] 入力フィールドを見つけます。次の内容をテキスト入力フィールドに貼り付けます。

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

システム指示を追加したら、モデルとチャットしてアプリケーションのテストを開始します。

1. [**Type something...**] とラベルの付いたテキスト入力ボックスに、ユーザーがする可能性のある質問や観察結果を入力します。次に例を示します。

   **ユーザー:**

   ```
   What's the weather like?
   ```
2. [**実行**] ボタンをクリックして、chatbot からレスポンスを取得します。レスポンスは次のようになります。

   **モデル:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   （gemini-2.5-pro）

### ステップ 2 - ボットのチャット機能を強化する

1 つの指示で、基本的なエウロパのエイリアン チャットボットを作成できました。ただし、1 つの指示だけでは、モデルのレスポンスの一貫性と品質を確保するのに十分でない場合があります。具体的な指示がないと、天気に関する質問に対するモデルの回答は非常に長くなる傾向があり、独自の解釈が加わる可能性があります。

システム指示に追加して、chatbot のトーンをカスタマイズします。

1. 新しいチャット プロンプトを開始するか、同じプロンプトを使用します。システム指示は、チャット セッションの開始後に変更できます。
2. [**システム指示**] セクションで、既存の指示を次のように変更します。

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. 質問（`What's the weather like?`）を再入力し、[**実行**] ボタンをクリックします。新しいチャットを開始していない場合、回答は次のようになります。

   **モデル:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   （gemini-2.5-pro）

このアプローチを使用すると、chatbot にさらに深みを追加できます。質問を追加したり、回答を編集したりして、チャットボットの品質を高めます。手順の追加や変更を続け、チャットボットの動作がどのように変化するかをテストします。

### ステップ 3 - 次のステップ

他のプロンプト タイプと同様に、プロンプトのプロトタイプが完成したら、[**コードを取得**] ボタンを使用してコーディングを開始するか、プロンプトを保存して後で作業したり、他のユーザーと共有したりできます。

## 関連情報

- コードに進む準備ができたら、[API スタートガイド](https://ai.google.dev/gemini-api/docs/get-started?hl=ja)をご覧ください。
- より良いプロンプトを作成する方法については、[プロンプト設計のガイドライン](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
