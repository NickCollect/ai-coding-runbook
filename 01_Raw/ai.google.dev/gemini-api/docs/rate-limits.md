---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja
fetched_at: 2026-08-03T04:36:50.085982+00:00
title: "\u30ec\u30fc\u30c8\u5236\u9650 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# レート制限

レート制限は、特定の期間内に Gemini API に送信できるリクエスト数を規制します。この制限は、公正な使用を維持し、不正使用を防ぎ、すべてのユーザーのシステム パフォーマンスを維持するのに役立ちます。

[AI Studio で有効なレート制限を表示する](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=ja)

## レート制限の仕組み

レート制限は通常、次の 3 つのディメンションで測定されます。

- 1 分あたりのリクエスト数（**RPM**）
- 1 分あたりのトークン数（入力）（**TPM**）
- 1 日あたりのリクエスト数（**RPD**）

使用量は各上限に対して評価され、いずれかの上限を超えるとレート制限エラーがトリガーされます。たとえば、RPM 上限が 20 の場合、TPM やその他の上限を超えていなくても、1 分以内に 21 件のリクエストを行うとエラーが発生します。

レート制限は、API キーごとではなく、プロジェクトごとに適用されます。1 日あたりのリクエスト数（**RPD**）の割り当ては、午前 0 時（太平洋時間）にリセットされます。

上限は使用する特定のモデルによって異なり、一部の上限は特定のモデルにのみ適用されます。たとえば、1 分あたりの画像数（IPM）は、画像を生成できるモデル（Nano Banana）でのみ計算されますが、概念的には TPM と似ています。他のモデルでは、1 日あたりのトークン数（TPD）の上限が設定されている場合があります。

試験運用版モデルとプレビュー版モデルでは、レート制限が厳しくなっています。

### 費用ベースのレート制限

Gemini API では、1 分あたりのリクエスト数（RPM）と 1 分あたりのトークン数（TPM）の上限に加えて、予期しない料金が発生しないように費用ベースのレート制限が適用されます。これらの制限がアカウントに適用されるかどうかは、請求
履歴と[使用量ティア](#usage-tiers)によって異なります。

[次の表に、使用量ティアごとの費用ベースのレート制限を示します。](#usage-tiers)これらの制限は、10 分間のローリング ウィンドウで評価されます。これらの制限がアカウントに適用されるかどうかは、請求履歴とアカウントのステータスによって異なります。

| 使用量ティア | 費用レート制限（10 分あたり） |
| --- | --- |
| **無料** | なし |
| **Tier 1** | $10 |
| **Tier 2** | $200 |
| **Tier 3** | $200 |

費用ベースのレート制限に達すると、API から `429 RESOURCE_EXHAUSTED` エラーが返されます。この問題を解決するには:

- しばらく待ってから**再試行** してください。
- **コンテキスト ウィンドウを小さくしたり、出力を短くしたりするなどして、コストの高いリクエストのレートを減らします**。
- 通常の使用中にこの上限に達することが続く場合は、
  [レート制限の引き上げをリクエストしてください](#request-rate-limit-increase)。

## 使用量ティア

レート制限は、プロジェクトの使用量ティアに関連付けられています。API の使用量と費用が増加すると、レート制限が引き上げられた上位のティアに自動的にアップグレードされます。

Tier 2 と Tier 3 の資格は、プロジェクトにリンクされている請求先アカウントの Google Cloud サービス（Gemini API を含むがこれに限定されない）の合計累積費用に基づいています。

| 使用量ティア | 予選 | [請求ティアの上限](https://ai.google.dev/gemini-api/docs/billing?hl=ja#tier-spend-caps) |
| --- | --- | --- |
| **無料** | [有効なプロジェクト](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#google-cloud-projects)または無料トライアル | なし |
| **Tier 1** | [有効な請求先アカウントを設定してリンクしている](https://ai.google.dev/gemini-api/docs/billing?hl=ja#setup-billing) | $250 |
| **Tier 2** | $100 の支払い + 最初のお支払いが完了してから 3 日 | $2,000 |
| **Tier 3** | $1,000 の支払い + 最初のお支払いが完了してから 30 日 | $20,000 ～$100,000 以上 |

通常、記載されている資格要件を満たしていれば承認されますが、審査プロセスで特定された他の要因に基づいて、アップグレード リクエストが拒否される場合があります。

このシステムは、すべてのユーザーに対して Gemini API プラットフォームのセキュリティと整合性を維持するのに役立ちます。

## Gemini API のレート制限

レート制限は、使用量ティアなどのさまざまな要因によって異なり、Google AI Studio で確認できます。ティアとアカウントのステータスは時間の経過とともに変化するため、レート制限は自動的に更新されます。

[AI Studio で有効なレート制限を表示する](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=ja)

指定されたレート制限は保証されておらず、実際の容量は異なる場合があります。

## 優先推論のレート制限

[優先度](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)の高い消費は、消費量が全体的なインタラクティブ トラフィックの
レート制限にカウントされる場合でも、独自のレート
制限を保持します。**デフォルトのレート制限は、モデルとティアごとに[標準レート制限](https://aistudio.google.com/rate-limit?hl=ja)の 0.3 倍です**

## Batch API のレート制限

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja) リクエストには、非バッチ API 呼び出しとは別に、独自のレート
制限が適用されます。

- **同時実行バッチ リクエスト:** 100
- **入力ファイルサイズの制限:** 2 GB
- **ファイル ストレージの上限:** 20 GB
- **モデルごとにキューに登録されたトークン:** [**バッチ キューに登録されたトークン**] 表に、特定のモデルのすべてのアクティブなバッチジョブでバッチ処理用にキューに登録できるトークンの最大数が表示されます。

### Tier 1

| モデル | バッチ キューに登録されたトークン |
| --- | --- |
| テキスト出力モデル | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro プレビュー版 | 5,000,000 |
| Gemini 3.1 Flash Lite | 10,000,000 |
| Gemini 3.1 Flash Lite プレビュー版 | 10,000,000 |
| Gemini 3.5 Flash | 3,000,000 |
| Gemini 2.5 Pro | 5,000,000 |
| Gemini 2.5 Pro TTS | 25,000 |
| Gemini 2.5 Flash | 3,000,000 |
| Gemini 2.5 Flash プレビュー版 | 3,000,000 |
| Gemini 2.5 Flash Image プレビュー版 | 3,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash Lite | 10,000,000 |
| Gemini 2.5 Flash Lite プレビュー版 | 10,000,000 |
| Gemini 2.0 Flash | 10,000,000 |
| Gemini 2.0 Flash Image | 3,000,000 |
| Gemini 2.0 Flash Lite | 10,000,000 |
| マルチモーダル生成モデル | | | | |
| Gemini 3.1 Flash Image プレビュー版 🍌 | 1,000,000 |
| Gemini 3.1 Flash Lite Image 🍌 | 2,000,000 |
| Gemini 3 Pro Image プレビュー版 🍌 | 2,000,000 |
| エンベディング モデル | | | | |
| Gemini エンベディング | 500,000 |

### Tier 2

| モデル | バッチ キューに登録されたトークン |
| --- | --- |
| テキスト出力モデル | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro プレビュー版 | 500,000,000 |
| Gemini 3.1 Flash Lite | 500,000,000 |
| Gemini 3.1 Flash Lite プレビュー版 | 500,000,000 |
| Gemini 3.5 Flash | 400,000,000 |
| Gemini 2.5 Pro | 500,000,000 |
| Gemini 2.5 Pro TTS | 100,000 |
| Gemini 2.5 Flash | 400,000,000 |
| Gemini 2.5 Flash プレビュー版 | 400,000,000 |
| Gemini 2.5 Flash Image プレビュー版 | 400,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash Lite | 500,000,000 |
| Gemini 2.5 Flash Lite プレビュー版 | 500,000,000 |
| Gemini 2.0 Flash | 1,000,000,000 |
| Gemini 2.0 Flash Image | 400,000,000 |
| Gemini 2.0 Flash Lite | 1,000,000,000 |
| マルチモーダル生成モデル | | | | |
| Gemini 3.1 Flash Image プレビュー版 🍌 | 250,000,000 |
| Gemini 3.1 Flash Lite Image 🍌 | 270,000,000 |
| Gemini 3 Pro Image プレビュー版 🍌 | 270,000,000 |
| エンベディング モデル | | | | |
| Gemini エンベディング | 5,000,000 |

### Tier 3

| モデル | バッチ キューに登録されたトークン |
| --- | --- |
| テキスト出力モデル | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro プレビュー版 | 1,000,000,000 |
| Gemini 3.1 Flash Lite | 1,000,000,000 |
| Gemini 3.1 Flash Lite プレビュー版 | 1,000,000,000 |
| Gemini 3.5 Flash | 1,000,000,000 |
| Gemini 2.5 Pro | 1,000,000,000 |
| Gemini 2.5 Pro TTS | 1,000,000 |
| Gemini 2.5 Flash | 1,000,000,000 |
| Gemini 2.5 Flash プレビュー版 | 1,000,000,000 |
| Gemini 2.5 Flash Image プレビュー版 | 1,000,000,000 |
| Gemini 2.5 Flash TTS | 4,000,000 |
| Gemini 2.5 Flash Lite | 1,000,000,000 |
| Gemini 2.5 Flash Lite プレビュー版 | 1,000,000,000 |
| Gemini 2.0 Flash | 5,000,000,000 |
| Gemini 2.0 Flash Image | 1,000,000,000 |
| Gemini 2.0 Flash Lite | 5,000,000,000 |
| マルチモーダル生成モデル | | | | |
| Gemini 3.1 Flash Image プレビュー版 🍌 | 750,000,000 |
| Gemini 3.1 Flash Lite Image 🍌 | 1,000,000,000 |
| Gemini 3 Pro Image プレビュー版 🍌 | 1,000,000,000 |
| エンベディング モデル | | | | |
| Gemini エンベディング | 10,000,000 |

## 次のティアにアップグレードする方法

無料ティアから有料ティアに移行するには、まず
[AI Studio で請求を設定する必要があります](https://ai.google.dev/gemini-api/docs/billing?hl=ja)。

プロジェクトが[指定された条件](#usage-tiers)を満たすと、
自動的に次のティアにアップグレードされます。無料ティアから Tier 1 へのティアのアップグレードは通常、すぐに有効になります。それ以降のティアのアップグレードは 10 分以内に有効になります。AI Studio の [[プロジェクト] ページ](https://aistudio.google.com/projects?hl=ja)に移動して、ティアを確認します。

## レート制限の引き上げをリクエストする

モデル バリエーションごとに、関連付けられたレート制限（1 分あたりのリクエスト数、RPM）があります。
これらのレート制限の詳細については、
[AI Studio のレート制限](https://aistudio.google.com/rate-limit?hl=ja)のページをご覧ください。

[有料ティアのレート制限の引き上げをリクエストする](https://forms.gle/ETzX94k8jf7iSotH9)

レート制限の引き上げを保証するものではありませんが、リクエストの審査に最善を尽くします。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-03 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-03 UTC。"],[],[]]
