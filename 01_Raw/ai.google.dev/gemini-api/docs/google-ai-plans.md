---
source_url: https://ai.google.dev/gemini-api/docs/google-ai-plans?hl=ja
fetched_at: 2026-08-10T03:23:59.441881+00:00
title: "Google AI \u30d7\u30e9\u30f3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google AI プラン

AI Studio で Google AI サブスクリプション プランを使用する。

Google AI Pro と Ultra のサブスクリプション プランでは、無料枠と比較して、AI Studio でのプロトタイピングと開発のためのモデルへのアクセスが拡大し、レート制限が引き上げられます。

Google AI プランに登録するには、Google AI Studio 内から直接アップグレードできます。左側のナビゲーション メニューにある [**アップグレード**] ボタンをクリックします。または、[Google AI プランのページ](https://one.google.com/about/google-ai-plans/?hl=ja)にアクセスして登録することもできます。

## 概要

Google AI Pro と Ultra のサブスクリプションでは、Google AI Studio Playground で有料モデルとより高いレート制限を利用できるほか、[ビルドモード](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ja)のコード アシスタントなどの機能を使用してバイブ コーディングを行うことができます。サブスクライバーには、[Playground](https://aistudio.google.com/prompts/new_chat?hl=ja) インターフェースと [Build](https://aistudio.google.com/apps?hl=ja) インターフェースで使用できる、無料枠よりも高いベースラインの日次割り当てが付与されます。1 日あたりの上限は、ローリング時間枠ではなくリセットを使用して適用されます。これにより、Cloud Billing を使用して本番環境規模の開発に移行する前に、スムーズな開発エクスペリエンスが保証されます。

| 計画 | AI Studio の使用 | モデルへのアクセスと特典 |
| --- | --- | --- |
| **無料** | 適度な割り当て | 基本的な上限とアクセス権。アップグレードして上限を引き上げることもできます。 |
| **AI Pro** | 割り当ての増加 | Gemini Pro、Nano Banana、Lyria などのプレミアム モデルを利用できる。 |
| **AI Ultra** | 最大割り当て | プロトタイピング、開発、高度なフロンティア モデル向けの使用量上限が最大のプラン。 |

## Gemini API の使用状況

AI Studio で 1 日あたりのベースライン サブスクリプション割り当てが使い果たされた場合は、Gemini API のリクエストごとの使用量に対して Cloud Billing が有効になっている Gemini API キーを使用して、ワークフローを続行できます。プロジェクトと API キーの Gemini API の使用状況は、[AI Studio ダッシュボード](https://aistudio.google.com/projects?hl=ja)で確認できます。

Google Cloud Platform（GCP）プロジェクトと Cloud Billing が有効になっているサブスクライバーは、Gemini API などの Cloud サービスに対して、[Google Developer Program](https://developers.google.com/program?hl=ja) から毎月 Cloud クレジットを受け取ることができます。前払いと後払いの使用量と請求は変更されません。前払い課金をご利用のお客様がプロモーション クレジットを有効にするには、AI Studio で 0 ドルを超える有料残高が必要です。対象となる Google Cloud クレジットがある場合は、まずそのクレジットが適用されます。[詳細](https://ai.google.dev/gemini-api/docs/billing?hl=ja#billing-plans)

Google AI サブスクリプションの統合により、高度なテストと開発の参入障壁が下がります。ただし、大規模な本番環境デプロイの場合は、Google Cloud プロジェクト、[Google Cloud スターター ティア](https://cloud.google.com/blog/topics/developers-practitioners/the-starter-tier-for-google-ai-studio-explained?hl=ja)、Gemini API キーを使用することをおすすめします。

## 制限事項と互換性

- **AI Studio UI のみ:** デベロッパーの使用に対する Google AI プランの特典は、Google AI Studio ウェブ インターフェース内でのみ適用されます。Gemini API の直接使用（API キーや外部アプリケーションの使用など）は、別途請求および管理されます。ただし、他の Google サービスでサブスクリプションを使用することはできます（[Google AI プラン](https://one.google.com/about/google-ai-plans/?hl=ja)を参照）。
- **API の課金とは異なります:** AI Studio の Google AI プランは、開発と本番環境の API 使用量をカバーする [Gemini API の使用量ティア](https://ai.google.dev/gemini-api/docs/billing?hl=ja)とは異なります。
- **Google One クレジット:** [Google One AI クレジット](https://support.google.com/googleone/answer/16287445?hl=ja)は、AI Studio でサポートされていない別のクレジット システムであり、Google Cloud クレジットとは重複しません。
- **エージェントへのアクセス:** AI Studio 内のエージェント（Deep Research と Antigravity プレビュー）へのアクセスは Google AI プランに含まれておらず、[有料の API キー](https://ai.google.dev/gemini-api/docs/billing?hl=ja#setup-billing)が必要です。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-08-04 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-08-04 UTC。"],[],[]]
