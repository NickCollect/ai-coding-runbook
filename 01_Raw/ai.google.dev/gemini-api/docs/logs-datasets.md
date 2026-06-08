---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ja
fetched_at: 2026-06-08T05:34:27.125793+00:00
title: "\u30ed\u30b0\u3068\u30c7\u30fc\u30bf\u30bb\u30c3\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# ログとデータセット

このガイドでは、既存の Gemini API アプリケーションのロギングを有効にするために必要なすべての情報を提供します。このガイドでは、Google AI Studio ダッシュボードで既存のアプリケーションまたは新しいアプリケーションのログを表示して、モデルの動作やユーザーがアプリケーションを操作する方法を把握する方法について説明します。ロギングを使用して、デベロッパーのユースケース全体で Gemini の改善に役立つように、*使用状況のフィードバック
を Google と共有します（省略可）*。[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ja)

すべての `GenerateContent` および `StreamGenerateContent` API 呼び出しがサポートされています。
[OpenAI 互換](https://ai.google.dev/gemini-api/docs/openai?hl=ja)
エンドポイントを介して行われたものを含みます。

## 1. Google AI Studio でロギングを有効にする

始める前に、課金が有効になっているプロジェクトを所有していることを確認してください。

1. Google [AI Studio](https://aistudio.google.com/logs?hl=ja) で [ログ] ページを開きます。
2. プルダウンからプロジェクトを選択し、[有効にする] ボタンを押して、デフォルトですべてのリクエストのロギングを有効にします。

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=ja)

すべてのプロジェクトまたは特定のプロジェクトのロギングを有効または無効にできます。これらの設定は、Google AI Studio でいつでも変更できます。

## 2. AI Studio でログを表示する

1. [AI Studio](https://aistudio.google.com/logs?hl=ja) に移動します。
2. ロギングを有効にしたプロジェクトを選択します。
3. ログがテーブルに新しい順に表示されます。

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

エントリをクリックすると、リクエストとレスポンスのペアが全ページに表示されます。完全なプロンプト、Gemini からの完了した回答、前のターンのコンテキストを確認できます。各プロジェクトのデフォルトのストレージ上限は 1,000 ログです。データセットに保存されていないログは 55 日後に期限切れになります。プロジェクトがストレージ上限に達すると、ログを削除するように求められます。

## 3. データセットをキュレートして共有する

- ログテーブルの上部にあるフィルタバーで、フィルタするプロパティを選択します。
- フィルタされたログビューで、チェックボックスを使用して、すべてのログまたは一部のログを選択します。
- リストの上部に表示される [データセットを作成] ボタンをクリックします。
- 新しいデータセットにわかりやすい名前と説明（省略可）を付けます。
- キュレートされたログセットを含む、作成したデータセットが表示されます。
- データセットを CSV、JSONL ファイルとして、または Google スプレッドシートにエクスポートして、さらに分析します。

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

データセットは、さまざまなユースケースで役立ちます。

- **チャレンジ セットをキュレートする:** AI の改善が必要な領域をターゲットとする今後の改善を推進します。
- **サンプルセットをキュレートする:** たとえば、実際の使用状況のサンプルを使用して別のモデルからレスポンスを生成したり、デプロイ前のルーチン チェック用のエッジケースのコレクションを作成したりします。
- **評価セット:** 重要な機能全体で実際の使用状況を表すセット。他のモデルやシステム命令の反復処理と比較します。

デモンストレーションの例としてデータセットを共有することで、AI 研究、Gemini API、Google AI Studio の進歩に貢献できます。これにより、さまざまなコンテキストでモデルを改良し、多くの分野やアプリケーションでデベロッパーにとって有用な AI システムを作成できます。

## 次のステップとテスト内容

ロギングを有効にしたら、次のことを試してください。

- **セッション履歴でプロトタイプを作成する:** [AI Studio Build](https://aistudio.google.com/apps?hl=ja) を活用してコードアプリをバイブさせ、API キーを追加してユーザーログの履歴を有効にします。
- **Gemini Batch API でログを再実行する:** Gemini Batch API を介してログを再実行し、レスポンスのサンプリング
  とモデルまたはアプリケーション ロジックの評価にデータセットを使用します
  。

## 互換性

現在、次の機能ではロギングはサポートされていません。

- Imagen モデルと Veo モデル
- Gemini エンベディング モデル
- 動画、GIF、PDF を含む入力

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
