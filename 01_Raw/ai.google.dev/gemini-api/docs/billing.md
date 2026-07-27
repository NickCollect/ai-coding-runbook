---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=ja
fetched_at: 2026-07-27T04:36:01.463799+00:00
title: "\u8ab2\u91d1 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 課金

このガイドでは、Gemini API のさまざまな課金オプションの概要、課金を有効にして使用状況をモニタリングする方法、課金に関するよくある質問（FAQ）の回答について説明します。

## お支払いと階層について

Gemini API の請求階層は、お支払い履歴に基づいて決まります。

| 使用量ティア | 予選 | [課金ティアの上限](#spend-caps) |
| --- | --- | --- |
| **無料** | [有効なプロジェクト](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#google-cloud-projects)または無料トライアル | なし |
| **Tier 1** | [有効な請求先アカウントを設定してリンクしている](#setup-billing) | $250 |
| **Tier 2** | $100 のお支払い + 最初のお支払いが完了してから 3 日 | $2,000 |
| **Tier 3** | $1,000 のお支払い + 最初のお支払いが完了してから 30 日 | $20,000 ～$100,000 以上 |

新しいアカウントは無料枠から始まり、Gemini API と AI Studio の[特定のモデル](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)に、モデルの無料枠の[レート上限](https://aistudio.google.com/rate-limit?hl=ja)までアクセスできます。

ビルドモードからアプリケーションを直接デプロイするには、**Google Cloud Starter Tier** を使用します。このティアでは、Google Cloud プロジェクトや請求先アカウントを設定せずに、最大 2 つのフルスタック アプリケーションを公開できます。詳細については、[Google AI Studio からのデプロイ](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=ja)をご覧ください。詳細については、[Google Cloud スターター ティアのドキュメント](https://docs.cloud.google.com/docs/starter-tier?hl=ja)をご覧ください。

**より高いレート上限にアクセスし、高度なモデルを使用し、プロンプトとレスポンスが Google プロダクトの改善に使用されないようにするには、[課金アカウントをリンク](#setup-billing)して[前払い](#prepay)を行い、有料階層に移行します。\***その後、累計費用とアカウントの利用期間に基づいて、上位のティアに移行します。Tier 3 では、[後払い](#postpay)請求に切り替えることができる場合があります。

ティア、レートの上限、請求先アカウントの上限はすべて、[請求先アカウント](#cloud-billing) レベルで決定されます。

\* *エンタープライズ グレードのデータ プライバシー: 有料サービスのデータ使用について詳しくは、[利用規約](https://ai.google.dev/gemini-api/terms?hl=ja#data-use-paid)をご覧ください。*

## お支払い情報を設定して有料プランを利用する

[Google AI Studio](https://aistudio.google.com/projects?hl=ja) でプロジェクトを作成してお支払い情報を設定するか、既存のプロジェクトをインポートして、有料枠にアップグレードできます。無料枠から有料枠にアップグレードするには、請求先アカウントをリンクして[前払い](#prepay)を行い、アカウントに 10 ドル以上（または他の通貨での同等額）のクレジットを追加します。

1. AI Studio の [API キー](https://aistudio.google.com/api-keys?hl=ja)ページ、[プロジェクト](https://aistudio.google.com/projects?hl=ja) ページ、または AI Studio の [**お支払い情報を設定**] ボタンが表示されている任意の場所に移動します。
   - 新規ユーザーには、デフォルトで[プロジェクトと API キー](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#google-cloud-projects)が作成されます。
   - 新しいキーが必要な場合は、[[**API キーを作成**](https://aistudio.google.com/api-keys?hl=ja)] をクリックし、ダイアログに沿ってキーとプロジェクトのペアをテーブルに追加します。
2. 有料階層にアップグレードする無料枠プロジェクトを見つけ、[*課金階層*] 列の [**課金を設定**] をクリックします。
3. Google 請求先アカウントをまだ設定していない場合:
   - 利用規約に同意するために、国を選択するよう求められます。
   - 次に、連絡先情報とお支払い方法を入力または確認して、続行します。
4. 過去に Google 請求先アカウントを設定したことがある場合:
   - 既存の請求先アカウントから選択するよう求められます。
   - 既存のアカウントを使用しない場合は、[**新しいお支払いアカウントを追加**] をクリックして、連絡先情報とお支払い方法を入力または確認してから続行します。
5. 次に、以下のいずれかになります。
   - 請求先の設定を完了するために最低 $10 の前払いを求められた（つまり、アカウントが[前払い](#prepay)請求プランに自動的に割り当てられている）。
   - アカウントの[前払い](#prepay)と[後払い](#postpay)の請求プランを選択できます。
   - 新しい前払いシステムがすべてのユーザーに反映されるまでの間（2026 年 3 月 23 日から）、[後払い](#postpay)の請求プランに割り当てられます。
6. 前払いまたは後払いを選択すると、アカウントの設定が完了します。

### 次の有料プランにアップグレードする

すでに有料プランをご利用で、プラン変更の[条件](#about-billing)を満たしている場合は、自動的に次の階層にアップグレードされます（[処理時間](#processing-times)が適用されます）。

## 課金ステータスを確認する

プロジェクトに[請求先アカウントをリンク](#setup-billing)すると、[AI Studio の [お支払い] ページ](https://aistudio.google.com/billing?hl=ja)でステータスをモニタリングできます。無料枠とは異なり、有料枠のステータスは動的です。使用枠はアカウント履歴によって決まりますが、Gemini API は、[前払い](#prepay)のクレジット残高がプラスの場合にのみリクエストを処理します。

[[プロジェクト](https://aistudio.google.com/projects?hl=ja)] ページで、[*課金階層*] 列にプロジェクトの階層と課金プランが表示されます。プロジェクトで必要な課金ステータスのアクションは、[*課金ティア*] 列または [*ステータス*] 列に表示されます。

- プロジェクトに請求先アカウントがリンクされていない場合は、[***請求先アカウントを設定***] をクリックします。
- プロジェクトに請求先アカウントが関連付けられているが、設定が必要な[前払い](#prepay)のお支払いプランを使用する必要がある場合は、[***前払いを設定***] をクリックします。
- 請求先アカウントでクレジットの購入が必要であるにもかかわらず、前払いのお支払いアカウントが設定されていないか、利用可能なクレジット残高がなくなった場合は、「***クレジットなし***」と表示されます。

いずれかのメッセージをクリックして、必要な操作を行います。

## 使用量のモニタリング

Gemini API の使用状況は、[Google AI Studio](https://aistudio.google.com/usage?hl=ja) の [**ダッシュボード**] > [**使用量**] でモニタリングできます。

## お支払いプラン

Gemini API と AI Studio の課金プランは、使用料金を支払うタイミングを決定する 2 つのカテゴリ（前払いと後払い）に分類されます。割り当てられた課金プランの確認とお支払い方法の管理は、[AI Studio の課金](https://aistudio.google.com/billing?hl=ja)ページで行うことができます。

### 前払い

前払い請求プランでは、Gemini API の使用前に前払い残高に対するクレジットを購入し、API の使用料金は前払いクレジット残高から[ほぼリアルタイム](#processing-times)で差し引かれます。プリペイド方式をご利用いただくには、アカウントに[クレジットを追加](#buy-credits)するか、[オートチャージ](#auto-reload)を設定します。クレジットを購入した後、未使用のクレジットは 12 か月後に有効期限切れとなり、[後払いアカウントに切り替えた](#postpay)場合を除き、[払い戻しはできません](#refunds)。

請求先アカウントのプリペイド クレジット残高が 0 ドルになると、その請求先アカウントにリンクされているすべてのプロジェクトのすべての API キーが同時に機能しなくなります。前払いクレジットは Gemini API の使用料金にのみ適用されます。他の Google Cloud サービスの支払いに使用することはできません。

新規ユーザーはデフォルトで前払いのお支払いプランになります。前払いと後払いのお支払いプランの導入前に作成されたプロジェクトでは、Gemini API を引き続き使用する前に、[プロジェクトの請求先情報を更新](#verify-billing)する必要がある場合があります。

*なお、[請求書発行（オフライン）](https://docs.cloud.google.com/billing/docs/concepts?hl=ja#billing_account_types)アカウントでは前払いをご利用いただけません。*

#### クレジットを購入する

Gemini API の使用前にクレジットを手動で購入して、前払いアカウントのクレジット残高にチャージできます。

クレジットを購入するには、[AI Studio のお支払い](https://aistudio.google.com/billing?hl=ja)ページに移動して、[**クレジットを購入**] を選択します。最小購入額は 10 米ドルです。前払いできるクレジットの最大額は $5,000 です。

#### 自動再読み込み

オートチャージは、前払いクレジット残高が少なくなったときに自動的にチャージされるオプション機能です。これは、サービスの中断を防ぐのに役立ちます。

オートチャージを設定し、オートチャージのステータスを確認するには、[[AI Studio の請求](https://aistudio.google.com/billing?hl=ja)] ページの [*利用可能なクレジット*] カードをご覧ください。[**オートチャージを設定**] または [**オートチャージを管理**] をクリックして、お支払い方法、チャージ額、チャージ支払いをトリガーする最低残高を設定します。

#### 1 か月あたりの自動チャージの上限

毎月のオートチャージの上限は、前払いユーザーが利用できる機能で、頻繁なクレジットの自動チャージによる予期しない費用の発生を防ぐことができます。この機能を使用すると、1 回の請求サイクル内で自動チャージできる上限を設定できます。請求期間内の自動チャージの合計額がこの上限に達すると、翌月の初めまで自動チャージは無効になります。手動で開始した 1 回限りの支払いは、この上限にカウントされません。

オートチャージが有効になっている場合に、1 か月の自動チャージの上限額を設定するには:

1. [AI Studio の [お支払い]](https://aistudio.google.com/billing?hl=ja) ページに移動します。
2. [**オートチャージを管理**] をクリックします。
3. [**月間の上限**] セクションを開き、オートチャージの月間の上限額を入力します。
4. [**保存**] をクリックします。

### 後払い

後払いプランでは、Cloud 請求先アカウントに費用が蓄積され、月末に自動的に請求されます。また、アカウントの階層に基づいて自動的に割り当てられた[費用上限](#tier-spend-caps)に費用が達した時点でも請求されます。お支払いは、Postpay のお支払いアカウントに登録されているお支払い方法に請求されます。このお支払い方法は、[[AI Studio の課金](https://aistudio.google.com/billing?hl=ja)] ページで管理できます。

[Tier 3 の条件](#about-billing)を満たしている場合は、前払いプランから後払いプランに手動で切り替えることができます。プランを変更するには、アカウントが対象になったときに [AI Studio のお支払い](https://aistudio.google.com/billing?hl=ja)ページの右上に表示される [**後払いに切り替え**] ボタンをクリックする必要があります。

[**お支払い**] ページでは、残高、お支払い期日、過去のお支払いの確認、お支払いの実行、お支払い方法の管理を行うことができます。

新しいプロジェクトの[お支払い情報を設定](#setup-billing)する際に、後払いの対象となる場合は、[[お支払い設定](#setup-billing)] ダイアログで前払いと後払いを選択できます。

Cloud 請求先アカウントを後払いプランに変更すると、その請求先アカウントにリンクされているすべてのプロジェクトが後払いプランに変更されます。その請求先アカウントを前払い料金プランに戻すことはできません。プロジェクトを別の料金プランの請求先アカウントに移動して、そのプロジェクトの請求サイクルを変更できます。Cloud ドキュメントの[プロジェクトの課金の管理](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ja)をご覧ください。

後払いの請求サイクルの詳細については、[Cloud Billing のガイド](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ja)をご覧ください。

## 利用額上限

Gemini API は、請求先アカウント階層とプロジェクト レベルの両方で月間の利用額上限をサポートしています。これらの制御は、アカウントを予期しない超過料金から保護し、エコシステムを保護してサービスの可用性を確保するように設計されています。

*費用の上限は、[請求書発行（オフライン）](https://docs.cloud.google.com/billing/docs/concepts?hl=ja#billing_account_types)アカウントでは使用できません。*

### プロジェクトの費用上限

AI Studio では、独自の[プロジェクト単位](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#google-cloud-projects)の費用上限を設定できます。これは、同じ請求先アカウントに複数のプロジェクトがあり、各プロジェクトが累積費用上限に十分アクセスできるようにする場合に便利です。

プロジェクトの編集者、オーナー、管理者の[ロール](https://docs.cloud.google.com/iam/docs/roles-overview?hl=ja)を持つアカウントは、AI Studio の [[費用](https://aistudio.google.com/spend?hl=ja)] ページで、[**月間の費用上限**] > [**費用上限を編集**] の順に選択して、プロジェクトごとに費用上限を設定できます。

AI Studio で費用上限と請求情報を表示または編集するために必要な特定の Google Cloud IAM 権限の詳細については、[AI Studio のトラブルシューティング ガイド](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=ja#iam-permissions)をご覧ください。

[プロジェクトを別の請求先アカウントに移動](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ja#change_the_billing_account_for_a_project)すると、そのプロジェクトに設定した費用上限は維持されますが、累積費用は新しい請求期間で $0 にリセットされます。

[バッチモード](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)の完了やエージェント セッションなどの長時間実行されるタスクでは、プロジェクトの費用上限を超える超過料金が発生する可能性があります。

AI Studio では、課金データの処理時間が最大 10 分程度遅延する可能性があります。請求データが処理される前に料金が加算されると、プロジェクトの上限を超過する可能性があります。

### 請求先アカウントの階層の費用上限

各[ティア](#about-billing)には、月間の費用の上限が設定されています。

| 使用量ティア | 利用額上限 |
| --- | --- |
| **無料** | なし |
| **Tier 1** | $250 |
| **Tier 2** | $2,000 |
| **Tier 3** | 20,000 ～ 100,000 ドル |

Gemini API の月間使用量上限は、[請求先アカウント](#cloud-billing)単位で適用されます。デフォルトの上限は事前に設定されていますが、使用量が増加した場合は、[引き上げをリクエスト](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=ja)できます。合計費用は、Gemini API サービスが有効になっているリンクされたすべてのプロジェクトで集計されます。アカウントの合計が階層の上限に達すると、次の請求期間（毎月 1 日）が始まるまで、その請求先アカウントにリンクされているすべてのプロジェクトでサービスが一時停止されます。

#### 請求先アカウントの費用を評価する

過去の月間費用を評価して、新しい[請求先アカウントのティア別費用上限](#tier-spend-caps)が進行中のプロジェクトに影響するかどうかを確認する手順は次のとおりです。

1. Google Cloud コンソールで、[Cloud 請求先アカウントの [レポート]](https://console.cloud.google.com/billing/reports?hl=ja) ページを表示します。
   - 請求先アカウントが複数ある場合は、プロンプトが表示されます。このプロンプトで、費用レポートを表示する Cloud 請求先アカウントを選択します。
2. レポートはデフォルトで、[当月] の [サービス別にグループ化] に設定されています。テーブルの [**サービス**] 列に **Gemini API** が表示され、[**使用料金**] 列に合計費用が表示されます。
3. Gemini API の使用量に限定した詳細な費用を表示するには、[**グループ条件**] フィルタを [**SKU**] でグループ化するように設定し、[**サービス**] フィルタを [**Gemini API**] に設定します。
4. [**使用日別の期間**] フィルタを目的の期間に調整して、過去の費用を評価します。

## 処理時間

課金シグナルと更新は必ずしもリアルタイムで行われるわけではありません。

- **クレジットの使用量**: 通常、使用料金は数分以内に残高から引き落とされます。
- **お支払いの確認**: ほとんどのカード支払いは即時に行われますが、お支払い方法によっては（銀行振込など）、清算に数日かかることがあります。サービスは、クレジットの購入が正式に確認された後にのみ再開またはアップグレードされます。
- **メンバーシップのアップグレード**: お支払いが完了した場合、または[アップグレード条件](#about-billing)を満たした場合、通常は 10 分以内にメンバーシップのアップグレードが反映されます。
- **合計費用の内訳グラフ**: [[お支払い](https://aistudio.google.com/billing?hl=ja)] ページと [[費用](https://aistudio.google.com/spend?hl=ja)] ページに表示される合計費用の内訳グラフは、更新に最大 24 時間かかることがあります。

課金の遅延の可能性について詳しくは、[課金サイクル](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ja#delayed-billing)と[トランザクション](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=ja#missing-transactions) レイテンシに関する Cloud Billing ガイドをご覧ください。

## 払い戻し

アカウント タイプの切り替えの場合を除き、**前払い**の請求先アカウントでは払い戻しはできません。

**前払いアカウントが後払いアカウント タイプに切り替わる場合**（[条件](#about-billing)を満たし、アカウントを[手動でアップグレード](#postpay)した後）、前払いアカウントは閉鎖され、残りの前払いクレジットは自動的に登録されているお支払い方法に払い戻されます。

後払いへのアップグレード以外の理由で前払いアカウントを[閉鎖](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=ja#close-a-billing-account)した場合、残りの前払いクレジットは失効します。

購入したクレジットの有効期限は 1 年です。有効期限が切れると、クレジットは没収され、取得できなくなります。

**後払い**アカウントには、[Google Cloud の払い戻しポリシー](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=ja#request_a_refund)が適用されます。

## Cloud 請求先アカウント

Gemini API は、課金サービスに [Cloud 請求先アカウント](https://cloud.google.com/billing/docs/concepts?hl=ja)を使用します。これは、[AI Studio で直接設定](#setup-billing)できます。AI Studio を使用すると、費用の追跡、費用の把握、支払いができます。

階層、レート上限、請求先アカウントの上限はすべて、請求先アカウント レベルで決定されます。

### プロジェクトと API キー

Cloud 請求先アカウントにリンクされているすべての[プロジェクト](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#google-cloud-projects)は、請求先アカウントの使用量階層と、関連するレート上限とアカウント上限を継承します。[プロジェクトをある請求先アカウントから別の請求先アカウントに変更](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ja#change_the_billing_account_for_a_project)すると、その階層と、それに伴うレート制限とアカウント上限が、新しい請求先アカウントの階層に切り替わります。

請求先アカウントに関連付けられたすべてのプロジェクトの累積費用（すべての Google Cloud プロダクトの合計）とアカウントの有効期間は、その請求先アカウントの[階層の資格要件](#about-billing)の対象となります。

[プロジェクトと請求先アカウントのリンクを解除](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ja#disable_billing_for_a_project)して、無料枠に戻ることができます。

[API キー](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)は、プロジェクト内で生成される認証情報です。独立した課金設定はなく、プロジェクトの階層上限と課金ステータスを継承します。プロジェクト内のすべてのキーの累積使用量は、そのプロジェクトの費用上限と請求先アカウントの合計費用にカウントされます。

## よくある質問

以降のセクションでは、よくある質問とその回答を紹介します。

### 何に対して料金が発生しますか？

Gemini API の料金は、次の要素に基づきます。

- 入力トークン数
- 出力トークン数
- キャッシュに保存されたトークン数
- キャッシュに保存されたトークンの保存期間

料金については、[料金ページ](https://ai.google.dev/pricing?hl=ja)をご覧ください。

### 割り当てはどこで確認できますか？

割り当てとシステム上限は [AI Studio](https://aistudio.google.com/usage?hl=ja) で確認できます。

### レート上限の上位 Tier に移行するにはどうすればよいですか？また、割り当ての増加をリクエストするにはどうすればよいですか？

アカウントが次の[階層の要件](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja#usage-tiers)を満たすと、割り当てが自動的に増加します。

### EEA（EU を含む）、英国、スイスで Gemini API を無料で使用できますか？

はい。無料枠と有料枠は[多くのリージョン](https://ai.google.dev/gemini-api/docs/available-regions?hl=ja)でご利用いただけます。

### Gemini API でお支払い情報を設定した場合、Google AI Studio の使用に対して課金されますか？

有料機能にアクセスするために有料の API キーをリンクしない限り、AI Studio の使用は無料です。AI Studio の有料プロジェクトの一部として有料 API キーをリンクすると、そのキーの AI Studio の使用量に対して課金されます。有料ティア プロジェクトと無料ティア プロジェクトは、各タイプにリンクされているそれぞれの API キーを使用して、必要に応じて切り替えることができます。

### 無料枠から上位の Tier にアップグレードするにはどうすればよいですか？

上位の階層にアクセスするには、プロジェクトで課金を設定する必要があります。Google AI Studio で [[**お支払い情報を設定**](#setup-billing)] をクリックします。Cloud 請求先アカウントの選択または作成の手順が表示されます。前払い請求モデルを使用する必要がある場合は、**課金の設定**プロセスで、Cloud 請求先アカウントにリンクされた前払いアカウントを作成する手順が案内されます。

### 無料枠で 100 万個のトークンを使用できますか？

Gemini API の無料枠は、選択したモデルによって異なります。現時点では、次の方法で 100 万トークンのコンテキスト ウィンドウを試すことができます。

- Google AI Studio で
- 一部のモデルでは無料プランをご利用いただけます
- 後払いプランの場合

### 上位（有料）階層にアップグレードした後、無料枠に戻すことはできますか？

無料枠にダウングレードするには、ダウングレードする各プロジェクトで[課金を無効](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ja#disable_billing_for_a_project)にします。

### 使用しているトークンの数を計算するにはどうすればよいですか？

[`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ja#count_tokens) メソッドを使用して、トークン数をカウントします。トークンの詳細については、[トークンガイド](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)をご覧ください。

### AI Studio から初めて Cloud 請求先アカウントに登録した場合でも、Google Cloud の無料トライアルを利用できますか？

初めて Cloud 請求先アカウントに登録すると、[Google Cloud の無料トライアル](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=ja#free-trial)が開始され、$300 の[ウェルカム クレジット](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ja#welcome-credits)が付与されます。ただし、これらのクレジットを AI Studio の使用料金の支払いに使用することはできません。ウェルカム クレジットは、Google Cloud 内の他の対象サービスのお支払いに使用できます（クレジットが消費されるか、有効期限（90 日以内）が切れると、追加の使用料金は設定されたお支払い方法に自動的に請求されます）。

### Google Cloud ウェルカム クレジットを Gemini API で使用できますか？

いいえ。Google Cloud の[ウェルカム クレジット](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ja#welcome-credits)または無料トライアル クレジットは、Gemini API または AI Studio には使用できません。

Google Cloud ウェルカム クレジットの対象外になる前にクレジットが付与された場合は、クレジットの有効期限（90 日後）が切れるまで、残りのクレジットを Gemini API と AI Studio で使用できます。

### Google Cloud の無料トライアルは Gemini API の使用量に適用されますか？

いいえ。2026 年 3 月より、Gemini API の使用料金は [300 ドルの Google Cloud 無料トライアル](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=ja#free-trial) プログラムの対象外となります。

### Google Cloud クレジットは前払いとどのように連携しますか？

前払いユーザーは、Gemini API の使用に適用できる Google Cloud クレジットを使用する前に、まず[前払いクレジットを購入](#buy-credits)する必要があります。前払いクレジットの残高が有効になると、Gemini API の対象となる Google Cloud クレジットは、前払いクレジットの残高よりも先に使用されます。請求先アカウントのプリペイド クレジット残高が $0 になると、Google Cloud クレジットは使用されなくなります。

[Google Cloud ウェルカム クレジット](#cloud-credits)など、一部の Google Cloud クレジットは Gemini API と AI Studio に使用できません。

### 請求はどのように処理されますか？

Gemini API の課金は、[Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=ja) システムによって処理されます。プロダクト内の Cloud Billing の設定については、[Cloud Billing のドキュメント](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ja)をご覧ください。

### 失敗したリクエストに対して課金されますか？

リクエストが 400 エラーまたは 500 エラーで失敗した場合、使用されたトークンに対して課金されることはありません。ただし、リクエストは割り当てに対してカウントされます。

### `GetTokens` は課金対象ですか？

`GetTokens` API へのリクエストは課金されず、推論割り当てにもカウントされません。

### 有料の API アカウントを使用している場合、Google AI Studio のデータはどのように処理されますか？

Cloud 請求が有効になっている場合のデータの取り扱いについては、[利用規約](https://ai.google.dev/gemini-api/terms?hl=ja#paid-services)（「有料サービス」の「Google による使用者のデータの利用方法」を参照）をご覧ください。少なくとも 1 つの API プロジェクトで課金が有効になっている限り、Google AI Studio プロンプトは同じ「有料サービス」の条件で扱われます。これは、[プラン] で「有料」とマークされているプロジェクトがあるかどうかを [Gemini API キーページ](https://aistudio.google.com/api-keys?hl=ja)で確認できます。

### 前払い請求とは何ですか？また、前払い請求モデルを使用する必要があるのは誰ですか？

プリペイド課金では、AI Studio の Gemini API のユーザーがクレジットを事前に購入できます。2026 年 3 月 23 日以降、AI Studio の新規ユーザーは、プリペイド課金プランへの登録が必要になる場合があります。AI Studio の[お支払い設定](#setup-billing)プロセスでは、UI に沿ってお支払い設定フローを進めます。前払いが必須かどうかは、UI に表示されます。

### 前払いクレジットを購入するにはどうすればよいですか？購入できる金額に上限や下限はありますか？

AI Studio の [お支払い] ページで[クレジットを購入](#buy-credits)できます。購入手続きの際、UI には、お住まいの地域とティアレベルに必要な購入前残高の最小額と、アカウントに一度にチャージできる最大額が表示されます。

### 必要に応じてクレジットを自動的に購入するように前払いアカウントを設定できますか？

はい。AI Studio の課金設定で[自動再読み込み](#auto-reload)を構成することをおすすめします。「トリガー」となるクレジット残高（「残高が 30 ドルを下回った場合」など）と「チャージ金額」（「100 ドルを追加」など）を指定します。

### 自動リチャージの金額を制限できますか？

はい。プリペイド ユーザーは、[**オートチャージ**] ウィジェットで [[1 か月の上限額](#monthly-auto-charge-limit)] を設定できます。請求期間内のオートチャージの合計額がこの上限に達すると、翌月までオートチャージは無効になります。手動でクレジットを購入した場合、この上限にはカウントされません。

### 未使用のクレジットの払い戻しを受けることはできますか？

プリペイド API クレジットはすべて 1 年後に期限切れとなり、払い戻しはできません。[前払いアカウントの払い戻しポリシー](#refunds)をご確認ください。

### プリペイド クレジットに有効期限はありますか？

はい。クレジットは購入日から 12 か月後に有効期限が切れます。

### プリペイド クレジットの残高が $0 になるとどうなりますか？

Cloud 請求先前払いアカウントで支払われたすべてのプロジェクトのすべての Gemini API サービスが直ちに停止し、追加の料金が発生しなくなります。プロジェクトは自動的に無料枠にダウングレードされません。

現在の有料階層レベルでサービスを復元するには、[追加のクレジットを購入](#buy-credits)する必要があります。クレジットを購入すると、Gemini API を使用できるようになります。なお、クレジット残高が反映されるまで、[遅延](#processing-times)が生じることがあります。

必要に応じて、無料枠にダウングレードするには、ダウングレードするプロジェクトの[課金を無効](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ja#disable_billing_for_a_project)にします。

### プリペイド クレジットの残高が $0 を超えているのに、使用量が停止したのはなぜですか？

現在のプランの[使用量上限](#tier-spend-caps)に達した可能性があります。上位のティアに進むと、使用量の上限が自動的に引き上げられます。Gemini API AI Studio の使用状況は、[Cloud 請求先アカウントのステータス](#missed-payment)によっても影響を受ける可能性があります。

### プリペイド アカウントのクレジット残高がマイナスになっているのはなぜですか？

請求システムと処理システムが複雑なため、クレジットをすべて使用した後、使用を停止するまでに[遅延](#processing-times)が生じる可能性があります。この超過使用量は、AI Studio の課金ダッシュボードにマイナスのクレジット残高として表示されることがあります。この場合、サービスは一時停止され、マイナス残高は次回のクレジット購入時に差し引かれます。

Gemini API サービスが一時停止しないようにするには、クレジット残高が指定した値を下回ったときに自動的にクレジットを購入する[自動再読み込み](#auto-reload)を設定することをおすすめします。

### 前払いクレジットを Gemini Enterprise Agent Platform などの他の Google Cloud サービスに使用できますか？

いいえ。前払いクレジットは Gemini API の使用に限定されています。使用する他の Google Cloud サービス（Compute、Storage、Gemini Enterprise Agent Platform）は、標準の [Cloud 請求サイクル](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ja)で請求されます。

### 後払いプランに切り替えることはできますか？

お支払い履歴を確立し、[後払い請求プランの対象となるティアに達する](#about-billing)と、今後の Gemini API の使用料金をすべて標準の統合 Google Cloud [後払い請求サイクル](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ja#view-your-charging-cycle)に移行するかどうかを選択できます。

### 後払いプランに切り替えた場合、前払いクレジットはどうなりますか？

[後払い](#postpay)にアップグレードすると、Cloud Billing は前払い支払いアカウントを閉鎖し、[自動チャージ](#auto-reload)を無効にして、未使用の前払いクレジットを自動的に払い戻します（標準の払い戻し処理時間に従います）。

### 現在のプリペイド クレジットの残高と取引履歴はどこで確認できますか？

Gemini API の残高管理と取引履歴はすべて、Google AI Studio の [お支払い] タブで直接行う必要があります。

### 「請求先アカウントの種類が無効であるか、サポートされていません」というメッセージが表示されるのはなぜですか？

選択した請求先アカウントの種類または請求先アカウントのステータスが AI Studio の有料階層の対象でない場合、[AI Studio の [お支払い] ページ](https://aistudio.google.com/billing?hl=ja)でのお支払いの操作がブロックされ、「請求先アカウントの種類が無効またはサポートされていません」というメッセージが表示されることがあります。

[Cloud Console](https://console.cloud.google.com/billing/?hl=ja) で、お支払いアカウントのステータスを確認します。対象外のタイプの 1 つに*無料トライアル アカウント*があります。この場合は、AI Studio で[課金を有効](#setup-billing)にすると、対象となります。無効な状態の 1 つに [*閉鎖*] があります。この場合は、[アカウントを再開](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=ja)できます。

### Gemini API の使用料金は Google Cloud コンソールに表示されますか？

はい。Gemini API の費用と、Cloud 請求先アカウントで支払われる他の Google Cloud サービスの費用は、[Cloud Billing コンソール](https://console.cloud.google.com/billing?hl=ja)の[費用管理ページ](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=ja#cost-reports)で確認できます。プリペイド クレジット残高は AI Studio でのみ管理できます。

### AI Studio の課金ではクレジットの使用量とともに Gemini API の使用量が表示されるのに、Cloud Billing コンソールには表示されないのはなぜですか？

Google Cloud と AI Studio は、さまざまな間隔で使用量データを Cloud Billing に報告します。請求システムと処理システムの複雑さにより、サービスの使用と、Cloud Billing に表示される使用量や費用との間に遅延が生じる場合があります。通常、費用の詳細は 1 日以内に確認できますが、24 時間以上かかる場合もあります。遅延請求の詳細については、[Cloud Billing のドキュメント](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ja#delayed-billing)をご覧ください。

### 後払い請求サイクルの対象となる費用が発生する他の Google Cloud サービスを使用している場合、支払いを忘れるとどうなりますか？

他の Google Cloud サービスの支払いが滞ると、**利用可能なプリペイド クレジットの残高に関係なく**、AI Studio での Gemini API へのアクセスが一時停止される可能性があります。AI Studio の使用量は Google Cloud 請求先アカウントで管理されます。このアカウントでは、AI Studio の前払い請求と他の Cloud サービスの後払い請求の両方を共有できます。後払い残高に問題があると、そのアカウントに関連付けられているすべてのサービスが停止します。Cloud 請求先アカウントに次のような問題が報告された場合、Gemini API の使用は一時停止されます。

- 未払いまたは支払い期限が過ぎている残高
- お支払いが承認されなかった場合
- 無効または期限切れのお支払い方法

サービスを復元するには、Google Cloud Billing コンソールで[後払いアカウントの問題を解決](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=ja#resolving-declined-payments)する必要があります。問題を解決すると、Gemini API のプリペイド クレジットとサービスに再びアクセスできるようになります。

### 請求に関するサポートはどこで受けられますか？

課金に関するサポートについては、[Cloud Billing サポートを利用する](https://cloud.google.com/support/billing?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-07 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-07 UTC。"],[],[]]
