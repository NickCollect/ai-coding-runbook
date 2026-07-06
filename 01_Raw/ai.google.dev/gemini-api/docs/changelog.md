---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=ja
fetched_at: 2026-07-06T05:16:33.898622+00:00
title: "\u30ea\u30ea\u30fc\u30b9\u30ce\u30fc\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# リリースノート

このページでは、Gemini API の更新について説明します。

## 2026 年 6 月 30 日

- **Gemini Omni Flash の一般公開プレビュー版**: 高速動画生成と会話型動画編集用に設計された高性能マルチモーダル モデルである `gemini-omni-flash-preview` をリリースしました。[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) を使用すると、テキストの説明から 720p の 3 ～ 10 秒の動画を生成したり、静止画像をアニメーション化したりして、会話形式で出力を編集、調整できます。まず、[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ja) ガイドと [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=ja) モデルカードをご覧ください。
- 超低レイテンシと費用対効果の高い画像生成と編集に最適化された組み込みのマルチモーダル モデルである `gemini-3.1-flash-lite-image`（Nano Banana Lite）を一般提供（GA）としてリリースしました。[Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=ja) モデルカードと[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)ガイドをご覧ください。

## 2026 年 6 月 24 日

- **パソコンの使用**: Gemini 3.5 Flash で[パソコンの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)ツールの公開プレビューのサポートを開始しました。このリリースには、インテントを使用した簡素化されたアクション、ブラウザ、モバイル、デスクトップ環境の組み込みサポート、構成可能な安全性ポリシー、高度なプロンプト インジェクション検出が含まれています。

## 2026 年 6 月 17 日

- **音声生成のストリーミング サポート**: `streamGenerateContent`（Interactions API の `stream: true`）を介したストリーミングが、`gemini-3.1-flash-tts-preview` モデルでサポートされるようになりました。詳細については、[テキスト読み上げ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja#streaming)ガイドをご覧ください。

## 2026 年 6 月 15 日

- **サポート終了のお知らせ**: 次の画像生成モデルはサポートが終了し、**2026 年 8 月 17 日**に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

  - **Imagen 4 モデルと Gemini 3 Image モデル**:

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    コードを新しい安定版またはプレビュー版のエンドポイントに移行するには、[Gemini の非推奨](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja#imagen-models)のページをご覧ください。
- **非推奨のお知らせ**: 次の動画生成モデルは非推奨となり、**2026 年 6 月 30 日**に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

  - **Veo モデル**:

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    サービスの中断を避けるため、Veo 3.1 プレビュー モデル ID（`veo-3.1-generate-preview`、`veo-3.1-fast-generate-preview`）または [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=ja) で利用可能な 3.1 GA モデルを使用するように統合を更新してください。
- **サポート終了のお知らせ**: 試験運用版の GMP コンテキスト ビュー ツール（Google マップによるグラウンディングの出力用の固定インターフェース）は、**2026 年 6 月 15 日**に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

## 2026 年 6 月 1 日

- 次の Gemini 2.0 モデルは、現在[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されています。

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  代わりに [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) または [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) を使用してください。

## 2026 年 5 月 28 日

- ネイティブのビジュアル モデルである [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=ja) と [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=ja) の一般提供（GA）バージョンである `gemini-3.1-flash-image`（Nano Banana 2）と `gemini-3-pro-image`（Nano Banana Pro）をリリースしました。
- **動画から画像への生成のサポート**: 動画ファイル（直接アップロードまたは公開 YouTube URL 経由）をテキスト プロンプトとともにマルチモーダル コンテキストとして渡して、高品質のサムネイル、映画のような映画ポスター、概要インフォグラフィックを生成できるようになりました。この機能は `gemini-3.1-flash-image` モデルでのみご利用いただけます。詳しくは、[動画から画像への生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja#video-to-image)ガイドをご覧ください。
- 非推奨のお知らせ: `gemini-3.1-flash-image-preview` モデルと `gemini-3-pro-image-preview` モデルは非推奨となり、2026 年 6 月 25 日に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

## 2026 年 5 月 25 日

- `gemini-3.1-flash-lite-preview` モデルは[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されました。代わりに [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) を使用してください。

## 2026 年 5 月 19 日

- エージェント タスクとコーディング タスクで最先端のパフォーマンスを維持する最もインテリジェントなモデルである [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) の一般提供（GA）バージョン `gemini-3.5-flash` をリリースしました。これは、`gemini-flash-latest` の背後にあるモデルです。
- **Gemini API の Managed Agents** を公開プレビュー版でリリースしました。これにより、デベロッパーは、Google がホストする安全な分離された Linux サンドボックス環境で実行される自律型のステートフル エージェントを構築してデプロイできます。詳細については、[エージェントの概要](https://ai.google.dev/gemini-api/docs/agents?hl=ja)ページと[クイックスタート](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja)をご覧ください。
- 汎用 **Antigravity Agent** マネージド エージェント [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=ja) を公開プレビューでリリースしました。Antigravity エージェントは、サンドボックス コンテナ内でコードの計画、推論、記述、実行、ファイルの管理、ウェブの閲覧を自律的に行うことができます。コードサンプルと仕様については、[Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja) のガイドをご覧ください。

## 2026 年 5 月 7 日

- 速度、スケーラビリティ、費用対効果に最適化された [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) の一般提供（GA）バージョン `gemini-3.1-flash-lite` をリリースしました。
- 非推奨のお知らせ: `gemini-3.1-flash-lite-preview` モデルは 2026 年 5 月 11 日に非推奨となり、2026 年 5 月 25 日に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

## 2026 年 5 月 6 日

- **今後の重大な変更**: [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) のリクエストとレスポンスのスキーマ（`outputs` → `steps`）と出力形式の構成（`response_format`）が変更されます。新しいスキーマは **5 月 26 日**にデフォルトとなり、旧スキーマは **6 月 8 日**に削除されます。詳しくは、[移行ガイド](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ja)をご覧ください。

## 2026 年 5 月 5 日

- マルチモーダル検索をサポートするように**ファイル検索**を更新しました。`gemini-embedding-2` モデルを使用して、画像をネイティブに埋め込み、検索できるようになりました。グラウンディング メタデータに、視覚的な引用の `media_id` と、情報の検索場所を示す `page_numbers` が含まれるようになりました。詳細については、[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)ガイドをご覧ください。

## 2026 年 5 月 4 日

- Gemini API でイベント ドリブンの [Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=ja) のサポートを開始し、Batch API と長時間実行オペレーションのポーリング ワークフローを置き換えました。

## 2026 年 4 月 30 日

- `gemini-robotics-er-1.5-preview` モデルは[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されました。代わりに [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=ja) を使用してください。

## 2026 年 4 月 22 日

- `gemini-embedding-2` を一般提供（GA）としてリリースしました。詳細については、[エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)のページをご覧ください。

## 2026 年 4 月 21 日

- コラボレーション プランニング、可視化のサポート、MCP サーバーの統合、ファイル検索を備えた [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) エージェントの新しいバージョンをリリースしました。

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=ja): スピードと効率性を重視して設計されており、クライアント UI にストリーミングで戻すのに最適です。
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=ja): コンテキストの自動収集と合成の最大包括性。

## 2026 年 4 月 15 日

- 費用対効果に優れ、表現力豊かで、制御可能なテキスト読み上げモデルである [Gemini 3.1 Flash TTS プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ja)をリリースしました。詳細については、[Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja) のドキュメントをご覧ください。

## 2026 年 4 月 14 日

- 更新されたロボット工学モデルである `gemini-robotics-er-1.6-preview` をリリースしました。楽器の読み取り、空間認識能力と物理的推論能力の向上などの新機能が追加されました。詳細については、[Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ja) のページと[ブログ](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=ja)をご覧ください。
- 非推奨のお知らせ: `gemini-robotics-er-1.5-preview` モデルは 2026 年 4 月 30 日午前 9 時（太平洋標準時）に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

## 2026 年 4 月 2 日

- [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=ja) のリリースの一環として、`gemma-4-26b-a4b-it` と `gemma-4-31b-it` をリリースしました。これらは [AI Studio](https://aistudio.google.com?hl=ja) と Gemini API を通じて利用できます。

## 2026 年 4 月 1 日

- 新しい [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja) 推論ティアと [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja) 推論ティアを導入し、費用やレイテンシを最適化するためのオプションを増やしました。

## 2026 年 3 月 31 日

- 最も費用対効果の高い[動画生成](https://ai.google.dev/gemini-api/docs/video?hl=ja)モデルである Veo 3.1 Lite プレビュー版 [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=ja) をリリースしました。このモデルは、迅速なイテレーションと大量のアプリケーションの構築を目的として設計されています。
- `gemini-2.5-flash-lite-preview-09-2025` モデルがシャットダウンされました。代わりに [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ja) を使用してください。

## 2026 年 3 月 26 日

- リアルタイムの会話と音声優先の AI アプリケーション向けに設計された最新の音声から音声への（A2A）モデルである [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ja) をリリースしました。まず、[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja) のドキュメントをお読みください。

## 2026 年 3 月 25 日

- [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=ja) 音楽生成モデル（[`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=ja)（30 秒のクリップ）と [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=ja)（フルレングスの曲））をリリースしました。どちらのモデルもテキストと画像の入力を受け付け、高品質の 48 kHz ステレオ音声を生成します。詳細とコードサンプルについては、[音楽生成](https://ai.google.dev/gemini-api/docs/music-generation?hl=ja)ガイドをご覧ください。

## March 23, 2026

- AI Studio で[前払いと後払いの課金プラン](https://ai.google.dev/gemini-api/docs/billing?hl=ja)をリリースしました。既存のアカウントに影響する可能性があります。詳しくは、[課金](https://ai.google.dev/gemini-api/docs/billing?hl=ja)に関するドキュメントをご覧ください。

## 2026 年 3 月 18 日

- 新しい[組み込みツールと関数呼び出しの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)機能をリリースしました。これにより、1 回の API 呼び出しで Gemini の組み込みツールとカスタム関数呼び出しツールを同時に使用できるようになりました。
- 今後、Gemini 3 モデルで [Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja#supported_models)がサポートされるようになります。

## 2026 年 3 月 16 日

- ユーザーの請求エクスペリエンスを向上させるため、[使用量階層](https://ai.google.dev/gemini-api/docs/billing?hl=ja#about-billing)と[請求先アカウントの費用上限](https://ai.google.dev/gemini-api/docs/billing?hl=ja#tier-spend-caps)を刷新しました。

## 2026 年 3 月 12 日

- AI Studio の課金に[プロジェクト単位の費用上限](https://ai.google.dev/gemini-api/docs/billing?hl=ja#project-spend-caps)を導入しました。

## 2026 年 3 月 10 日

- 初のマルチモーダル エンベディング モデルである `gemini-embedding-2-preview` をリリースしました。テキスト、画像、動画、音声、PDF の入力をサポートし、すべてのモダリティを統合されたエンベディング空間にマッピングします。詳細については、[エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)をご覧ください。
- 非推奨のお知らせ: `gemini-2.5-flash-lite-preview-09-2025` モデルは 2026 年 3 月 31 日に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

## 2026 年 3 月 9 日

- Gemini 3 Pro プレビュー版モデルは[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されました。`gemini-3-pro-preview` が [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) を指すようになりました。

## 2026 年 3 月 3 日

- Gemini 3 シリーズ初の Flash-Lite モデルである Gemini 3.1 Flash-Lite プレビュー版をリリースしました。仕様、特定のアップデート、デベロッパー向けガイダンスについては、[モデルページ](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ja)をご覧ください。

## 2026 年 2 月 26 日

- Nano Banana 2（[Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=ja)）をリリースしました。これは、スピードと大量のユースケース向けに最適化された高効率モデルです。
- 非推奨のお知らせ: Gemini 3 Pro プレビュー版（`gemini-3-pro-preview`）は 2026 年 3 月 9 日に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

## 2026 年 2 月 19 日

- 新しい Gemini 3 シリーズ ファミリーの最新バージョンである [Gemini 3.1 Pro プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja)をリリースしました。
- bash とツールの両方を使用して構築しているユーザー向けに、カスタムツールの優先順位付けに優れた別のエンドポイント `gemini-3.1-pro-preview-customtools` をリリースしました。

## 2026 年 2 月 18 日

- 非推奨のお知らせ: 以下のモデルは 2026 年 6 月 1 日に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 2026 年 2 月 17 日

- 次のモデルは[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されています。

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 2026 年 1 月 29 日

- `gemini-3-pro-preview` と `gemini-3-flash-preview` でコンピュータ使用ツールのサポートを開始しました。

## 2026 年 1 月 21 日

- `latest` エイリアスを変更しました。

  - `gemini-pro-latest` が `gemini-3-pro-preview` に切り替わりました
  - `gemini-flash-latest` が `gemini-3-flash-preview` に切り替わりました

## 2026 年 1 月 15 日

- 非推奨のお知らせ: 以下のモデルは 2026 年 2 月 17 日に[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されます。

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- `gemini-2.5-flash-image-preview` モデルがシャットダウンされました。

## 2026 年 1 月 14 日

- `text-embedding-004` モデルは[シャットダウン](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)されました。

## 2026 年 1 月 13 日

- [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ja) の 4K 出力解像度を追加し、すべての解像度で縦向き動画のサポートを強化しました。

## 2026 年 1 月 12 日

- モデルのライフサイクル機能がリリースされました。一部のモデルでは、ライフサイクル ステージと非推奨のタイムラインが指定されるようになりました。詳細については、次のドキュメントをご覧ください。

  - [モデルのステージ](https://ai.google.dev/api/generate-content?hl=ja#ModelStatus)

## 2026 年 1 月 8 日

- Gemini API のデータ入力ソースとして、Cloud Storage バケットとパブリック DB およびプライベート DB の事前署名付き URL のサポートを開始しました。ファイルサイズの上限も 20 MB から 100 MB に引き上げられています。詳しくは、[ファイル入力方法ガイド](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja)をご覧ください。

## 2025 年 12 月 19 日

- v1beta で Interactions API に互換性を破る変更を導入しました。思考モデルの「思考」のコンセプトに沿うように、`total_reasoning_tokens` フィールドの名前を `total_thought_tokens` に変更しました。

## 2025 年 12 月 17 日

- Gemini 3 Flash プレビュー版（`gemini-3-flash-preview`）をリリースしました。このモデルは、大規模モデルに匹敵する高速なフロンティア クラスのパフォーマンスを、わずかなコストで実現します。視覚的および空間的推論とエージェント コーディング機能がアップグレードされています。次の新機能に関するドキュメントをご覧ください。

  - [マルチモーダル関数レスポンス](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#multimodal)
  - [画像を含むコード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja#images)

## 2025 年 12 月 12 日

- Live API の新しいネイティブ音声モデルである `gemini-2.5-flash-native-audio-preview-12-2025` をリリースしました。この更新により、モデルの複雑なワークフローを処理する能力が向上します。詳細については、[Live API ガイド](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja)と [Gemini 2.5 Flash ネイティブ音声](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=ja)をご覧ください。

## 2025 年 12 月 11 日

- Interactions API をリリースしました。この API は、Gemini モデルとエージェントを操作するための統合インターフェースを提供します。詳しくは、[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) ガイドをご覧ください。
- Gemini Deep Research エージェントのプレビュー版をリリースしました。複数ステップのリサーチタスクの計画、実行、結果の合成を自律的に行うことができます。詳しくは、[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) のガイドをご覧ください。

## 2025 年 12 月 10 日

- [テキスト読み上げモデル](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)の機能強化（Gemini 2.5 Flash TTS プレビュー版（低レイテンシ向けに最適化）と Gemini 2.5 Pro TTS プレビュー版（品質向けに最適化）を含む）をリリースしました。表現力、正確なペース、シームレスな会話が強化されています。

## 2025 年 12 月 9 日

- 次の Gemini Live API モデルは現在シャットダウンされています。
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 2025 年 12 月 5 日

- [Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)の Gemini 3 の課金は、2026 年 1 月 5 日に開始されます。

## 2025 年 12 月 4 日

- 非推奨のお知らせ: `gemini-2.5-flash-image-preview` モデルは 2026 年 1 月 15 日にシャットダウンされます。

## 2025 年 12 月 3 日

- サポート終了のお知らせ: `text-embedding-004` モデルは 2026 年 1 月 14 日にシャットダウンされます。

## 2025 年 11 月 20 日

- Gemini 3 Pro Image Preview（`gemini-3-pro-image-preview`）をリリースしました。これは、Nano Banana モデルの次のイテレーションです。詳細については、[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)のページをご覧ください。

## 2025 年 11 月 18 日

- Gemini 3 シリーズの最初のモデルである `gemini-3-pro-preview` をリリースしました。これは、強力なエージェント機能とコーディング機能を備えた、最先端の推論とマルチモーダル理解モデルです。

  Gemini 3 Pro プレビュー版では、インテリジェンスとパフォーマンスの改善に加えて、次の点に関する新しい動作が導入されています。

  - [メディアの解像度](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja)
  - [思考シグネチャ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ja)
  - [思考レベル](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#thinking-levels)

  移行、新機能、仕様については、[Gemini 3 デベロッパー ガイド](https://ai.google.dev/gemini-api/docs/gemini-3?hl=ja)をご覧ください。

## 2025 年 11 月 11 日

- サポート終了のお知らせ: 次のモデルはシャットダウンされます。

  - 11 月 12 日:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 11 月 14 日:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 2025 年 11 月 10 日

- 次のモデルはシャットダウンされます。

  - `imagen-3.0-generate-002`

  代わりに [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=ja#imagen-4) を使用してください。詳細については、[Gemini の非推奨の表](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)をご覧ください。

## 2025 年 11 月 6 日

- File Search API を公開プレビューとしてリリースし、デベロッパーが独自のデータに基づいて回答を生成できるようにしました。詳しくは、新しい[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)ページをご覧ください。

## 2025 年 11 月 4 日

- [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja) の場合、画像の入力トークン数が 1,290 から 258 に削減され、画像編集の費用が削減されました。
- サポート終了のお知らせ: 次のモデルはシャットダウンされます。

  - 11 月 18 日:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 12 月 2 日:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 12 月 9 日:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 2025 年 10 月 29 日

- Gemini API の新しい[ロギングとデータセット](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ja) ツールをリリースしました。

## 2025 年 10 月 20 日

- 次の Gemini Live API モデルは現在シャットダウンされています。

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  代わりに `gemini-2.5-flash-native-audio-preview-09-2025` を使用できます。
- サポート終了のお知らせ: `gemini-2.0-flash-live-001` と `gemini-live-2.5-flash-preview` のシャットダウンは 2025 年 12 月 9 日に予定されています。

## 2025 年 10 月 17 日

- **Google マップによるグラウンディング**が一般提供になりました。詳細については、[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)のドキュメントをご覧ください。

## 2025 年 10 月 15 日

- [Veo 3.1 と 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=ja#veo-3.1) モデルを公開プレビュー版でリリースしました。新機能は次のとおりです。

  - Veo で作成した動画を拡張する。
  - 最大 3 枚の画像を参照して動画を生成します。
  - 動画の生成元となる最初と最後のフレームの画像を提供します。

  今回のリリースでは、Veo 3 の出力動画の長さとして 4 秒、6 秒、8 秒のオプションも追加されました。
- サポート終了のお知らせ: `veo-3.0-generate-preview` と `veo-3.0-fast-generate-preview` のサービスは 2025 年 11 月 12 日に終了します。

## 2025 年 10 月 7 日

- [Gemini 2.5 コンピュータの使用プレビュー](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)をリリースしました

## 2025 年 10 月 2 日

- Gemini 2.5 Flash Image の一般提供を開始: [Gemini を使用した画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)

## 2025 年 9 月 29 日

- 次の Gemini 1.5 モデルは現在シャットダウンされています。
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 2025 年 9 月 25 日

- Gemini Robotics-ER 1.5 モデルのプレビュー版をリリースしました。ロボット アプリケーションでモデルを使用する方法については、[ロボットの概要](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ja)をご覧ください。
- 次のプレビュー モデルをリリースしました。

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  詳細については、[モデル](https://ai.google.dev/gemini-api/docs/models?hl=ja)のページをご覧ください。

## 2025 年 9 月 23 日

- `gemini-2.5-flash-native-audio-preview-09-2025` をリリースしました。これは、関数呼び出しと音声の途切れの処理が改善された Live API の新しいネイティブ音声モデルです。詳細については、[Live API ガイド](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja)と [Gemini 2.5 Flash ネイティブ音声](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-native-audio)をご覧ください。

## 2025 年 9 月 16 日

- 非推奨のお知らせ: 以下のモデルは 2025 年 10 月にシャットダウンされます。

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07`（`gemini-embedding-exp`）

  最新のエンベディング モデルの詳細については、[エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)のページをご覧ください。

## 2025 年 9 月 10 日

- [Batch API のエンベディング モデル](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja#batch-embedding)のサポートをリリースし、[OpenAI 互換性ライブラリ](https://ai.google.dev/gemini-api/docs/openai?hl=ja#batch)に Batch API を追加して、バッチクエリをさらに簡単に開始できるようにしました。

## 2025 年 9 月 9 日

- Veo 3 と Veo 3 Fast の GA をリリースしました。価格が引き下げられ、アスペクト比、解像度、シードに関する新しいオプションが追加されました。詳しくは、[Veo のドキュメント](https://ai.google.dev/gemini-api/docs/video?hl=ja#model-features)をご覧ください。

## 2025 年 8 月 26 日

- 最新のネイティブ画像生成モデルである [Gemini 2.5 Image プレビュー版](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-image-preview)をリリースしました。

## 2025 年 8 月 18 日

- プロンプトに追加のコンテキストとして URL を提供するツールである [URL コンテキスト ツール](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)を一般提供（GA）としてリリースしました。`gemini-2.0-flash` モデルでの URL コンテキストの使用のサポート（試験運用版で提供）は、1 週間後に終了します。

## 2025 年 8 月 14 日

- Imagen 4 Ultra、Standard、Fast モデルを一般提供（GA）としてリリースしました。詳細については、[Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ja) のページをご覧ください。

## 2025 年 8 月 7 日

- 画像から動画への生成の `allow_adult` 設定が、制限付きの地域でも利用できるようになりました。詳しくは、[Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=ja#veo-model-parameters) のページをご覧ください。

## 2025 年 7 月 31 日

- Veo 3 プレビュー モデルの画像から動画を生成する機能をリリースしました。
- Veo 3 Fast プレビュー モデルをリリースしました。
- Veo 3 について詳しくは、[Veo](https://ai.google.dev/gemini-api/docs/video?hl=ja) ページをご覧ください。

## 2025 年 7 月 22 日

- 高速、低コスト、高性能の Gemini 2.5 モデルである `gemini-2.5-flash-lite` をリリースしました。詳しくは、[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-lite) をご覧ください。

## 2025 年 7 月 17 日

- Veo の最新アップデートである `veo-3.0-generate-preview` をリリースしました。音声付きの動画を生成できるようになりました。Veo 3 について詳しくは、[Veo](https://ai.google.dev/gemini-api/docs/video?hl=ja) ページをご覧ください。
- Imagen 4 Standard と Ultra のレート制限が引き上げられました。詳細については、[レートの上限](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja)のページをご覧ください。

## 2025 年 7 月 14 日

- テキスト エンベディング モデルの安定版である `gemini-embedding-001` をリリースしました。詳細については、[エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)をご覧ください。`gemini-embedding-exp-03-07` モデルは 2025 年 8 月 14 日に非推奨になります。

## 2025 年 7 月 7 日

- Gemini API バッチモードをリリースしました。リクエストをバッチ処理して、非同期で処理するために送信します。詳細については、[バッチモード](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ja)をご覧ください。

## 2025 年 6 月 26 日

- プレビュー モデル `gemini-2.5-pro-preview-05-06` と `gemini-2.5-pro-preview-03-25` は、最新の安定版 `gemini-2.5-pro` にリダイレクトされるようになりました。
- `gemini-2.5-pro-exp-03-25` がシャットダウンされます。

## 2025 年 6 月 24 日

- Imagen 4 Ultra と Standard のプレビュー モデルをリリースしました。詳細については、[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)のページをご覧ください。

## 2025 年 6 月 17 日

- 最も強力なモデルの安定版である `gemini-2.5-pro` をリリースしました。適応型思考が搭載されています。詳細については、[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-pro) と [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=ja) をご覧ください。`gemini-2.5-pro-preview-05-06` は 2025 年 6 月 26 日に `gemini-2.5-pro` にリダイレクトされます。
- 最初の安定版 2.5 Flash モデルである `gemini-2.5-flash` をリリースしました。詳細については、[Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash) をご覧ください。`gemini-2.5-flash-preview-04-17` は 2025 年 7 月 15 日に非推奨となります。
- 低コストで高性能な Gemini 2.5 モデルである `gemini-2.5-flash-lite-preview-06-17` をリリースしました。詳しくは、[Gemini 2.5 Flash-Lite プレビュー版](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-lite)をご覧ください。

## 2025 年 6 月 5 日

- 最も強力なモデルの新しいバージョンである `gemini-2.5-pro-preview-06-05` をリリースしました。適応型思考が搭載されています。詳細については、[Gemini 2.5 Pro プレビュー版](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-pro-preview-06-05)と[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)をご覧ください。`gemini-2.5-pro-preview-05-06` は 2025 年 6 月 26 日に `gemini-2.5-pro` にリダイレクトされます。

## 2025 年 5 月 27 日

- 最後に利用可能だったチューニング モデルである Gemini 1.5 Flash 001 がシャットダウンされました。チューニングはどのモデルでもサポートされなくなりました。[Gemini API を使用したファインチューニング](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ja)をご覧ください。

## 2025 年 5 月 20 日

**API の更新:**

- クリッピング間隔と構成可能なフレームレート サンプリングを使用した[カスタム動画プリプロセス](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#customize-video-processing)のサポートを開始しました。
- マルチツール使用を開始しました。これにより、同じ `generateContent` リクエストで[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)と [Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)を構成できます。
- Live API で[非同期関数呼び出し](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja#async-function-calling)のサポートを開始しました。
- プロンプトに追加のコンテキストとして URL を提供するための試験運用版の [URL コンテキスト ツール](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)をリリースしました。

**モデルの更新:**

- 価格とパフォーマンスのバランスが最適化され、適応思考に対応した Gemini の[プレビュー](https://ai.google.dev/gemini-api/docs/models?hl=ja#model-versions) モデルである `gemini-2.5-flash-preview-05-20` をリリースしました。詳細については、[Gemini 2.5 Flash プレビュー版](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-preview)と[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)をご覧ください。
- 1 人または 2 人のスピーカーで[音声の生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)が可能な [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-pro-preview-tts) モデルと [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-preview-tts) モデルをリリースしました。
- `lyria-realtime-exp` モデルをリリースしました。このモデルは、リアルタイムで[音楽を生成](https://ai.google.dev/gemini-api/docs/music-generation?hl=ja)します。
- ネイティブ オーディオ出力機能を備えた Live API 向けの新しい Gemini モデル `gemini-2.5-flash-preview-native-audio-dialog` と `gemini-2.5-flash-exp-native-audio-thinking-dialog` をリリースしました。詳細については、[Live API ガイド](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja#native-audio-output)と [Gemini 2.5 Flash ネイティブ音声](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-native-audio)をご覧ください。
- `gemma-3n-e4b-it` プレビュー版をリリースしました。[Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=ja) のリリースの一環として、[AI Studio](https://aistudio.google.com?hl=ja) と Gemini API を通じてご利用いただけます。

## 2025 年 5 月 7 日

- 画像の生成と編集用のプレビュー モデルである `gemini-2.0-flash-preview-image-generation` をリリースしました。詳細については、[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)と [Gemini 2.0 Flash プレビュー版の画像生成](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.0-flash-preview-image-generation)をご覧ください。

## 2025 年 5 月 6 日

- コードと関数呼び出しが改善された、最も強力なモデルの新しいバージョンである `gemini-2.5-pro-preview-05-06` をリリースしました。`gemini-2.5-pro-preview-03-25` は、モデルの新しいバージョンを自動的に参照します。

## 2025 年 4 月 17 日

- 価格とパフォーマンスのバランスが最適化され、適応思考に対応した Gemini の[プレビュー](https://ai.google.dev/gemini-api/docs/models?hl=ja#model-versions) モデルである `gemini-2.5-flash-preview-04-17` をリリースしました。詳細については、[Gemini 2.5 Flash プレビュー版](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-preview)と[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)をご覧ください。

## 2025 年 4 月 16 日

- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.0-flash) のコンテキスト キャッシュ保存をリリースしました。

## 2025 年 4 月 9 日

**モデルの更新:**

- 詳細で芸術的なニュアンスのある動画を生成できる、一般提供（GA）のテキストと画像から動画へのモデル `veo-2.0-generate-001` をリリースしました。詳細については、[Veo のドキュメント](https://ai.google.dev/gemini-api/docs/video?hl=ja)をご覧ください。
- 課金が有効になっている [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) モデルの公開プレビュー版である `gemini-2.0-flash-live-001` をリリースしました。

  - **セッション管理と信頼性の強化**

    - **セッションの再開:** ネットワークが一時的に中断してもセッションを維持します。API がサーバーサイドのセッション状態の保存（最大 24 時間）をサポートするようになり、中断したところから再接続して再開するためのハンドル（session\_resumption）が提供されるようになりました。
    - **コンテキスト圧縮によるセッションの延長:** 以前の制限時間を超えてやり取りを延長できます。スライディング ウィンドウ メカニズムを使用してコンテキスト ウィンドウの圧縮を構成し、コンテキストの長さを自動的に管理して、コンテキストの上限による突然の終了を防ぎます。
    - **Graceful Disconnect Notification（正常な切断通知）:** 接続が閉じようとしているタイミングを示す `GoAway` サーバー メッセージを受信し、終了前に正常な処理を行うことができます。
  - **インタラクションのダイナミクスをより細かく制御**
  - **構成可能な音声アクティビティ検出（VAD）:** 感度レベルを選択するか、自動 VAD を完全に無効にして、新しいクライアント イベント（`activityStart`、`activityEnd`）を使用して手動で発言権を制御します。
  - **構成可能な割り込み処理:** ユーザー入力によってモデルのレスポンスを中断するかどうかを決定します。
  - **構成可能なターン カバレッジ:** API がすべての音声と映像の入力を継続的に処理するか、エンドユーザーが発話していることが検出された場合にのみキャプチャするかを選択します。
  - **構成可能なメディア解像度:** 入力メディアの解像度を選択して、品質またはトークン使用量を最適化します。
  - **より豊富な出力と機能**
  - **音声と言語のオプションの拡大:** オーディオ出力用に 2 つの新しい音声と 30 の新しい言語から選択できます。出力言語は `speechConfig` 内で構成できるようになりました。
  - **テキスト ストリーミング:** テキスト レスポンスが生成されるたびに増分で受信し、ユーザーへの表示を高速化します。
  - **トークン使用量レポート:** サーバー メッセージの `usageMetadata` フィールドに提供される詳細なトークン数で、使用状況に関する分析情報を取得します。これは、モダリティとプロンプトまたはレスポンス フェーズごとに分類されます。

## 2025 年 4 月 4 日

- 課金が有効になっている Gemini 2.5 Pro の公開プレビュー版である `gemini-2.5-pro-preview-03-25` をリリースしました。無料枠で `gemini-2.5-pro-exp-03-25` を引き続き使用できます。

## 2025 年 3 月 25 日

- 思考モードがデフォルトで常にオンになっている公開試験運用版の Gemini モデル `gemini-2.5-pro-exp-03-25` をリリースしました。詳しくは、[Gemini 2.5 Pro（試験運用版）](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-pro-preview-03-25)をご覧ください。

## 2025 年 3 月 12 日

**モデルの更新:**

- 画像生成と編集が可能な試験運用版の [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja#gemini) モデルをリリースしました。
- [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=ja) のリリースの一環として、`gemma-3-27b-it` がリリースされました。[AI Studio](https://aistudio.google.com?hl=ja) と Gemini API を通じてご利用いただけます。

**API の更新:**

- メディアソースとして [YouTube URL](https://ai.google.dev/gemini-api/docs/vision?hl=ja#youtube) のサポートを追加しました。
- 20 MB 未満の[インライン動画](https://ai.google.dev/gemini-api/docs/vision?hl=ja#inline-video)を含めるサポートを追加しました。

## 2025 年 3 月 11 日

**SDK の更新:**

- [Google Gen AI SDK for TypeScript と JavaScript](https://googleapis.github.io/js-genai) を一般提供プレビューとしてリリースしました。

## 2025 年 3 月 7 日

**モデルの更新:**

- `gemini-embedding-exp-03-07`（公開プレビュー版の [試験運用版](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=ja)の Gemini ベースのエンベディング モデル）をリリースしました。

## 2025 年 2 月 28 日

**API の更新:**

- Gemini 2.0 Pro に基づく試験運用版モデル `gemini-2.0-pro-exp-02-05` に、[ツールとしての検索](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)のサポートが追加されました。

## 2025 年 2 月 25 日

**モデルの更新:**

- 速度、スケーラビリティ、費用対効果に最適化された [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-2.0-flash-lite) の一般提供（GA）バージョンである `gemini-2.0-flash-lite` をリリースしました。

## 2025 年 2 月 19 日

**AI Studio の更新:**

- [追加地域](https://ai.google.dev/gemini-api/docs/available-regions?hl=ja)（コソボ、グリーンランド、フェロー諸島）のサポート。

**API の更新:**

- [追加地域](https://ai.google.dev/gemini-api/docs/available-regions?hl=ja)（コソボ、グリーンランド、フェロー諸島）のサポート。

## 2025 年 2 月 18 日

**モデルの更新:**

- Gemini 1.0 Pro のサポートは終了しました。サポートされているモデルの一覧については、[Gemini モデル](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)をご覧ください。

## 2025 年 2 月 11 日

**API の更新:**

- [OpenAI ライブラリの互換性](https://ai.google.dev/gemini-api/docs/openai?hl=ja)に関する最新情報。

## 2025 年 2 月 6 日

**モデルの更新:**

- `imagen-3.0-generate-002`（[Gemini API の Imagen 3](https://ai.google.dev/gemini-api/docs/imagen?hl=ja) の一般提供（GA）版）をリリースしました。

**SDK の更新:**

- [Google Gen AI SDK for Java](https://github.com/googleapis/java-genai) の公開プレビューをリリースしました。

## 2025 年 2 月 5 日

**モデルの更新:**

- テキストのみの出力をサポートする [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-2.0-flash) の一般提供（GA）バージョンである `gemini-2.0-flash-001` をリリースしました。
- Gemini 2.0 Pro の[試験運用版](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=ja)の公開プレビュー版である `gemini-2.0-pro-exp-02-05` をリリースしました。
- 費用対効果を最適化した試験運用版の一般公開プレビュー [モデル](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-2.0-flash-lite) `gemini-2.0-flash-lite-preview-02-05` をリリースしました。

**API の更新:**

- コード実行に[ファイル入力とグラフ出力](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja#input-output)のサポートを追加しました。

**SDK の更新:**

- [Google Gen AI SDK for Python](https://googleapis.github.io/python-genai/) を一般提供（GA）としてリリースしました。

## 2025 年 1 月 21 日

**モデルの更新:**

- `gemini-2.0-flash-thinking-exp-01-21` をリリースしました。これは、[Gemini 2.0 Flash 思考モード](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)の基盤となるモデルの最新のプレビュー バージョンです。

## 2024 年 12 月 19 日

**モデルの更新:**

- Gemini 2.0 Flash 思考モードの公開プレビュー版をリリースしました。思考モードは、レスポンスの生成中にモデルの思考プロセスを表示し、より強力な推論機能でレスポンスを生成できるテスト時計算モデルです。

  Gemini 2.0 Flash Thinking モードの詳細については、[概要ページ](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=ja)をご覧ください。

## 2024 年 12 月 11 日

**モデルの更新:**

- [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-2.0-flash) の公開プレビュー版をリリースしました。Gemini 2.0 Flash Experimental の機能の一部を以下に示します。
  - Gemini 1.5 Pro の 2 倍の速度
  - Live API を使用した双方向ストリーミング
  - テキスト、画像、音声形式のマルチモーダル レスポンス生成
  - コード実行、検索、関数呼び出しなどの機能を使用するためのマルチターン推論による組み込みツールの使用

Gemini 2.0 Flash の詳細については、[概要ページ](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=ja)をご覧ください。

## 2024 年 11 月 21 日

**モデルの更新:**

- さらに強力な試験運用版 Gemini API モデルである `gemini-exp-1121` をリリースしました。

**モデルの更新:**

- `gemini-1.5-flash-002` を使用するように `gemini-1.5-flash-latest` モデル エイリアスと `gemini-1.5-flash` モデル エイリアスを更新しました。
  - `top_k` パラメータの変更: `gemini-1.5-flash-002` モデルは、1 ～ 41（41 を除く）の範囲の `top_k` 値をサポートします。40 より大きい値は 40 に変更されます。

## 2024 年 11 月 14 日

**モデルの更新:**

- 強力な試験運用版 Gemini API モデルである `gemini-exp-1114` をリリースしました。

## 2024 年 11 月 8 日

**API の更新:**

- OpenAI ライブラリ / REST API で [Gemini のサポート](https://ai.google.dev/gemini-api/docs/openai?hl=ja)を追加しました。

## 2024 年 10 月 31 日

**API の更新:**

- [Google 検索によるグラウンディングのサポート](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)を追加しました。

## 2024 年 10 月 3 日

**モデルの更新:**

- 最も小規模な Gemini API モデルの安定版である `gemini-1.5-flash-8b-001` をリリースしました。

## 2024 年 9 月 24 日

**モデルの更新:**

- Gemini 1.5 Pro と 1.5 Flash の 2 つの新しい安定版である `gemini-1.5-pro-002` と `gemini-1.5-flash-002` をリリースし、一般提供を開始しました。
- `gemini-1.5-pro-002` を使用するように `gemini-1.5-pro-latest` モデルコードを更新し、`gemini-1.5-flash-002` を使用するように `gemini-1.5-flash-latest` モデルコードを更新しました。
- `gemini-1.5-flash-8b-exp-0827` の代わりとして `gemini-1.5-flash-8b-exp-0924` をリリースしました。
- Gemini API と AI Studio 向けに[市民の誠実性に関する安全フィルタ](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja#safety-filters)をリリースしました。
- Python と NodeJS で Gemini 1.5 Pro と 1.5 Flash の 2 つの新しいパラメータ（[`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=ja#FIELDS.frequency_penalty) と [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=ja#FIELDS.presence_penalty)）のサポートをリリースしました。

## 2024 年 9 月 19 日

**AI Studio の更新:**

- モデルの回答に高評価ボタンと低評価ボタンを追加し、ユーザーが回答の質についてフィードバックを提供できるようにしました。

**API の更新:**

- Google Cloud クレジットのサポートが追加されました。これにより、Gemini API の使用に対して Google Cloud クレジットを使用できるようになりました。

## 2024 年 9 月 17 日

**AI Studio の更新:**

- プロンプトと、それを実行するコードを Colab ノートブックにエクスポートする [**Colab で開く**] ボタンを追加しました。この機能は、ツールを使用したプロンプト（JSON モード、関数呼び出し、コード実行）をまだサポートしていません。

## 2024 年 9 月 13 日

**AI Studio の更新:**

- 比較モードのサポートが追加されました。これにより、モデルとプロンプトのレスポンスを比較して、ユースケースに最適なものを見つけることができます。

## 2024 年 8 月 30 日

**モデルの更新:**

- Gemini 1.5 Flash は、[モデル構成による JSON スキーマの提供](https://ai.google.dev/gemini-api/docs/json-mode?hl=ja#supply-schema-in-config)をサポートしています。

## 2024 年 8 月 27 日

**モデルの更新:**

- 次の[試験運用モデル](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=ja)をリリースしました。
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 2024 年 8 月 9 日

**API の更新:**

- [PDF 処理](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)のサポートを追加しました。

## 2024 年 8 月 5 日

**モデルの更新:**

- Gemini 1.5 Flash のファインチューニングのサポートがリリースされました。

## 2024 年 8 月 1 日

**モデルの更新:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-1.5-pro) の新しい試験運用版 `gemini-1.5-pro-exp-0801` をリリースしました。

## 2024 年 7 月 12 日

**モデルの更新:**

- Google AI サービスおよびツールでの Gemini 1.0 Pro Vision のサポートが終了しました。

## 2024 年 6 月 27 日

**モデルの更新:**

- Gemini 1.5 Pro の 200 万トークンのコンテキスト ウィンドウの一般提供リリース。

**API の更新:**

- [コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)のサポートを追加しました。

## 2024 年 6 月 18 日

**API の更新:**

- [コンテキスト キャッシュ](https://ai.google.dev/gemini-api/docs/caching?hl=ja)のサポートを追加しました。

## 2024 年 6 月 12 日

**モデルの更新:**

- Gemini 1.0 Pro Vision が非推奨になりました。

## 2024 年 5 月 23 日

**モデルの更新:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-1.5-pro)（`gemini-1.5-pro-001`）が一般提供（GA）になりました。
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-1.5-flash)（`gemini-1.5-flash-001`）が一般提供（GA）されました。

## 2024 年 5 月 14 日

**API の更新:**

- Gemini 1.5 Pro の 200 万トークンのコンテキスト ウィンドウ（順番待ちリスト）を導入しました。
- Gemini 1.0 Pro の従量課金制の[課金](https://ai.google.dev/gemini-api/docs/billing?hl=ja)を導入しました。Gemini 1.5 Pro と Gemini 1.5 Flash の課金も近日中に開始予定です。
- Gemini 1.5 Pro の今後の有料枠のレート制限を引き上げました。
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ja) に組み込みの動画サポートを追加しました。
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ja) に書式なしテキストのサポートを追加しました。
- 並列関数呼び出しのサポートを追加しました。これにより、一度に複数の呼び出しを返すことができます。

## 2024 年 5 月 10 日

**モデルの更新:**

- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-1.5-flash)（`gemini-1.5-flash-latest`）のプレビュー版をリリースしました。

## 2024 年 4 月 9 日

**モデルの更新:**

- プレビュー版の [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#gemini-1.5-pro)（`gemini-1.5-pro-latest`）をリリースしました。
- 768 未満の[伸縮性エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja#elastic-embedding) サイズをサポートする新しいテキスト エンベディング モデル `text-embeddings-004` をリリースしました。

**API の更新:**

- プロンプトで使用するメディア ファイルを一時的に保存するための [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ja) をリリースしました。
- テキスト、画像、音声データを使用したプロンプト（マルチモーダル プロンプト）のサポートを追加しました。詳細については、[メディアを使用したプロンプト](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=ja)をご覧ください。
- [システム指示](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ja)のベータ版をリリースしました。
- 関数呼び出しの実行動作を定義する[関数呼び出しモード](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#function_calling_mode)を追加しました。
- `response_mime_type` 構成オプションのサポートを追加しました。これにより、[JSON 形式](https://ai.google.dev/gemini-api/docs/api-overview?hl=ja#json)でレスポンスをリクエストできます。

## 2024 年 3 月 19 日

**モデルの更新:**

- Google AI Studio または Gemini API で [Gemini 1.0 Pro のチューニング](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)のサポートを追加しました。

## 2023 年 12 月 13 日

**モデルの更新:**

- gemini-pro: 幅広いタスクに対応する新しいテキスト モデル。機能と効率のバランスが取れています。
- gemini-pro-vision: さまざまなタスクに対応する新しいマルチモーダル モデル。機能と効率のバランスが取れている。
- embedding-001: 新しいエンベディング モデル。
- aqa: 生成された回答のグラウンディングにテキスト パッセージを使用して質問に答えるようにトレーニングされた、特別に調整された新しいモデル。

詳細については、[Gemini モデル](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)をご覧ください。

**API バージョンの更新:**

- v1: 安定版 API チャンネル。
- v1beta: Beta チャンネル。このチャンネルには、開発中の機能が含まれている可能性があります。

詳細については、[API バージョンのトピック](https://ai.google.dev/gemini-api/docs/api-versions?hl=ja)をご覧ください。

**API の更新:**

- `GenerateContent` は、チャットとテキスト用の単一の統合エンドポイントです。
- `StreamGenerateContent` メソッドで利用可能なストリーミング。
- マルチモーダル機能: 画像が新しいサポート対象のモダリティ
- 新しいベータ版の機能:
  - [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)
  - [セマンティック リトリーバー](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=ja)
  - Attributed Question Answering（AQA）
- 候補数の更新: Gemini モデルは 1 つの候補のみを返します。
- 安全性設定と安全性評価のカテゴリが異なります。詳しくは、[安全設定](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)をご覧ください。
- Gemini モデルのモデル チューニングはまだサポートされていません（開発中です）。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-30 UTC。"],[],[]]
