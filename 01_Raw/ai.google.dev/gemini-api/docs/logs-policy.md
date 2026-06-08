---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=ja
fetched_at: 2026-06-08T05:40:23.570827+00:00
title: "\u30c7\u30fc\u30bf\u30ed\u30ae\u30f3\u30b0\u3068\u5171\u6709 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# データロギングと共有

このページでは、
[Gemini API ログ](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ja)の保存と管理について説明します。Gemini API ログは、課金が有効になっているプロジェクトのサポート対象の Gemini API 呼び出しから取得される、デベロッパーが所有する
API データです。ログには、ユーザーのリクエストからモデルのレスポンスまでのプロセス全体が含まれます。

## 1. 共有できるデータ

プロジェクト オーナーは、Gemini API 呼び出しのロギングを有効にするかどうかを選択できます。ロギングは、お客様自身が使用するため、または Google とのフィードバックや共有を通じてモデルの継続的な改善に役立てるために使用できます。

ロギングを有効にすると、プロダクトの改善とモデルのトレーニングのために次のデータを提供することで、さまざまな分野やユースケースのデベロッパーにとって価値のある AI システムの構築に役立てることができます。

- **データセット:** Google AI Studio の [Logs and Datasets] インターフェースを使用して、サポートされている Gemini API 呼び出しから関心のあるログ（リクエスト、レスポンス、メタデータなど）を選択します。データセットに含めることで提供されます。データセットの作成時にオプトアウトすることもできます。
- **フィードバック:** ログを確認する際に、フィードバックを提供できます。これには、高評価/低評価の評価や、提供するコメントが含まれます。

[[データセットを Google と共有すると、リクエストやレスポンスなど、そのデータセット内のログは「無償サービス」の利用規約に従って処理されます。つまり、データセットは、モデルの改善とトレーニングなど、Google のプロダクト、サービス、機械学習技術の開発と改善に使用される可能性があります。](https://developers.google.com/terms?hl=ja)](https://ai.google.dev/gemini-api/terms?hl=ja#data-use-unpaid)**個人情報や機密情報は含めないでください。**

## 2. データの使用方法

デフォルトでは、ログは 55 日後に期限切れになります。この期間を過ぎると、ログは使用できなくなります。データセットを作成して、この期間を超えて関心のあるログや価値のあるログを保持し、ダウンストリームのユースケースで使用したり、モデルの改善に任意で貢献したりできます。データセットに保存されたログには有効期限はありませんが、各プロジェクトのデフォルトのストレージ上限は 1,000 ログです。

デフォルトでは、ロギングは課金が有効になっているプロジェクトでのみ使用できるため、
データ使用に関する[規約](https://developers.google.com/terms?hl=ja)
に従い、ログ内のプロンプトとレスポンスはプロダクトの改善や
開発には使用されません。

ログのデータセットを Google と共有することを選択した場合、これらのデータセットは、AI
システムとアプリケーションが使用されるドメインとコンテキストの多様性をより深く理解するための実際のデモンストレーション
データとして使用されます。このデータは、モデルの品質の向上や、将来のモデルとサービスのトレーニングと評価に役立てられる可能性があります。[このデータは、無償サービスのデータ使用に関する規約に従って処理されます。](https://ai.google.dev/gemini-api/terms?hl=ja#data-use-unpaid)そのため、人間のレビュアーが、共有した
API 入出力の読み取り、注釈付け、処理を行う場合があります。モデルの改善にデータを使用する前に、このプロセスの一部として、ユーザーのプライバシーを保護するための措置が
Google により講じられます。措置には Google アカウント、API キー、およびクラウド
プロジェクトからのデータの切り離しが含まれます。これらは人間のレビュアーによる読み取りや注記の前に行われます。

## 3. データの権限

API データの提供を有効にすることで、このドキュメントに記載されているように、Google がデータを処理して使用するために必要な権限があることを確認します。**有料サービスを通じて取得した機密情報、機密情報、専有情報を含むログは提供しないでください**
。API 利用規約の「[コンテンツの送信](https://developers.google.com/terms?hl=ja#b_submission_of_content)」
に規定されている内容に従って使用者から Google に与えられる許可は、Google による使用に適用される法律で求められる範囲の中で、使用者が本サービスに送信したコンテンツ（たとえばプロンプトや、それに関連したシステム命令、キャッシュに保存されたコンテンツ、画像、動画、文書などのファイル）、および生成された回答にまで範囲が拡大されます。

## 4. データ共有とフィードバック

データを例として共有することで、AI 研究、Gemini API、Google AI Studio の最先端技術の発展に貢献できます。これにより、さまざまなコンテキストでモデルを継続的に改善し、さまざまな分野やユースケースのデベロッパーにとって価値のある AI システムを構築できます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
