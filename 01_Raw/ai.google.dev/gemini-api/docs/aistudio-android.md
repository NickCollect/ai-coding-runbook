---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=ja
fetched_at: 2026-08-10T03:18:00.465974+00:00
title: "Google AI Studio \u3067 Android \u30a2\u30d7\u30ea\u3092\u69cb\u7bc9\u3059\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google AI Studio で Android アプリを構築する

Google AI Studio を使用すると、自然言語プロンプトからネイティブ Android アプリを構築できます。必要なアプリについて説明すると、
[Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ja#antigravity-agent)
が完全な Kotlin プロジェクトと[Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=ja)
プロジェクトを生成します。ブラウザから、ブラウザベースの Android エミュレータでアプリをプレビューしたり、実機にインストールしたり、テスト用に公開したりできます。

## 始める

Android アプリの構築を開始する手順は次のとおりです。

1. 左側のナビゲーション パネルを使用して、Google AI Studio の [[ビルド] モード](https://aistudio.google.com/apps?hl=ja)に移動します。
2. プラットフォーム ピッカーから [**Android**] を選択します。
3. 構築するアプリの説明を入力します（例: *「ローカル ストレージを使用して毎日のタスク トラッカーを作成する」* または *「シンプルな電卓を作成する」*）。
4. エージェントがプロジェクトを生成し、ブラウザベースの Android エミュレータで起動します。

チャットパネルを使用して、ウェブと同じようにアプリを反復処理できます。エージェントは Android プロジェクト内のすべてのファイルを管理し、コードベース全体に変更を反映します。

## ブラウザベースの Android エミュレータ

Android エミュレータはクラウドで完全に実行され、ブラウザにストリーミングされます。
Android SDK、Android Studio、ローカル エミュレータをインストールする必要はありません。

エミュレータには次の機能があります。

- **Pixel のようなデバイスのシミュレーション**: 実機と同じように、アプリをタップ、スクロール、操作できます。
- **回転のサポート**: 縦向きと横向きを切り替えます。
- **ライブプレビュー**: エージェントがコードを変更すると、アプリが再ビルドされ、
  エミュレータが自動的に更新されます。

### エミュレータの制限事項

ブラウザベースのエミュレータは、すべてのハードウェア機能をサポートしていません。エミュレータでは次の機能は使用できません。

- カメラと写真のキャプチャ
- NFC と Bluetooth
- GPS（位置情報はシミュレートされます）
- Google Play 開発者サービス（Google ログイン、マップ、その他の Google Play 開発者サービスの機能は、実機では動作しますが、エミュレータでは動作しません）

## ADB を使用してデバイスにインストールする

ビルドした APK は、USB でパソコンに接続された実機の Android デバイスに直接インストールできます。これには、
[WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=ja) を
使用してブラウザ経由でデバイスと通信します。ローカル ADB のインストールは不要です。

### 前提条件

- WebUSB をサポートする Chrome または Edge ブラウザ。
- [[デベロッパー向けオプション] と [USB デバッグ](https://developer.android.com/studio/debug/dev-options?hl=ja)]
  が有効になっている Android デバイス。
- デバイスをパソコンに接続する USB ケーブル。

### デバイスにアプリをインストールする

1. プレビュー パネルで [**Install on Device**] をクリックします。
2. ブラウザの USB デバイス ピッカーから Android デバイスを選択します。
3. APK が転送され、デバイスにインストールされます。
4. アプリが自動的に起動します。

## Google Play ストアに公開する

Android アプリを
[Google Play Console](https://play.google.com/console?hl=ja) の内部
テストトラックに公開して、最大 100 人のテスターにアプリを配布できます。

### 前提条件

- [Google Play デベロッパー アカウント](https://play.google.com/console/signup?hl=ja)
  （1 回限りの登録料 25 ドルが必要です）。
- Google Play Console でデベロッパー プロファイルが完成していること。

### アプリを公開する

1. Google AI Studio で **[Settings] > [Publish]** を開きます。
2. [**Google Play ストアに公開**] をクリックします。
3. Google Play デベロッパー アカウントで認証します。
4. AI Studio が APK に署名し、アプリの掲載情報を作成（または新しいバージョンをアップロード）して、内部テストトラックに公開します。
5. テスターと共有するリンクが届きます。

AI Studio は、マネージド キーストアを使用して APK の署名を自動的に管理します。アプリの掲載情報（アイコン、スクリーンショット、説明）は、後で Google Play Console でカスタマイズできます。

## 生成されるもの

Android アプリをビルドすると、エージェントは次の構造で標準の Gradle ベースのプロジェクトを生成します。

- **ビルド構成**: `build.gradle.kts` ファイル（プロジェクト レベルとアプリレベル）
  Kotlin DSL を使用。
- **UI レイヤ**: [マテリアル デザイン 3](https://developer.android.com/develop/ui/compose?hl=ja) のテーマ設定を使用した [Jetpack Compose](https://m3.material.io/)
  コンポーネント。
- **アーキテクチャ**: ViewModel とデータ
  クラスを使用した単一アクティビティ アーキテクチャ。
- **リソース**: `AndroidManifest.xml`、ドローアブル、文字列、その他の Android
  リソース。

エージェントは Gradle の依存関係を自動的に管理し、必要に応じて Maven リポジトリと Google リポジトリからパッケージを追加します。

生成されたコードは、プレビュー パネルの [**Code**] タブで表示、編集できます。Android Studio で開発を続行するには、プロジェクトを**ZIP ファイル** としてダウンロードします。

## 制限事項

AI Studio での Android アプリのビルドには、次の制限があります。

### プラットフォームの制限

- **クライアントサイドのみ**: Android アプリにはサーバーサイド コンポーネントが含まれていません。サーバー ランタイムを必要とする機能（シークレット管理、マルチプレイヤー、Firebase、Google Workspace API）は使用できません。
- **単一アクティビティ アーキテクチャ**: 単一アクティビティ、単一モジュール
  プロジェクトのみがサポートされています。
- **Jetpack Compose のみ**: アプリは Kotlin と Jetpack Compose を使用します。Java と XML レイアウトはサポートされていません。
- **NDK またはネイティブ コードなし**: C コードと C++ コードはサポートされていません。
- **Wear OS または Android TV なし**: スマートフォンとタブレットのフォーム ファクタのみが
  サポートされています。

### エクスポートの制限事項

- **ZIP ダウンロードのみ**: プロジェクトを ZIP ファイルとしてダウンロードできます。Android プロジェクトでは、GitHub エクスポートはまだ使用できません。

## 次のステップ

- [Google AI Studio でアプリをビルドする](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ja)
- [フルスタック アプリの開発](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ja)（ウェブ）
- [App Gallery](https://aistudio.google.com/apps?source=showcase&hl=ja) で例を見る。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-19 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-19 UTC。"],[],[]]
