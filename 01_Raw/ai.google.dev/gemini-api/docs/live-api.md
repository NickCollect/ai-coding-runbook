---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=ja
fetched_at: 2026-06-08T05:36:39.668223+00:00
title: "Gemini Live API \u306e\u6982\u8981 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini Live API の概要

Live API を使用すると、Gemini と音声とビジョンによるやり取りを低レイテンシかつリアルタイムで行うことができます。音声、画像、テキストの連続ストリームを処理して、人間のような音声による応答を即座に提供し、ユーザーに自然な会話エクスペリエンスを提供します。

![Live API の概要](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=ja)

[Google AI Studio で Live API を試すmic](https://aistudio.google.com/live?hl=ja)
[GitHub からサンプルアプリをクローンするcode](https://github.com/google-gemini/gemini-live-api-examples)
[コーディング エージェントのスキルを使用するterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja)

## ユースケース

Live API を使用すると、次のようなさまざまな業界向けのリアルタイム音声エージェントを構築できます。

- **e コマースと小売:** パーソナライズされたおすすめを提供するショッピング アシスタントや、お客様の問題を解決するサポート エージェント。
- **ゲーム:** インタラクティブなノンプレーヤー キャラクター（NPC）、ゲーム内ヘルプ アシスタント、ゲーム内コンテンツのリアルタイム翻訳。
- **次世代インターフェース:** ロボット、スマートグラス、車両での音声と動画に対応したエクスペリエンス。
- **ヘルスケア:** 患者のサポートと教育のためのヘルス コンパニオン。
- **金融サービス:** 資産管理と投資ガイダンスのための AI アドバイザー。
- **教育:** パーソナライズされた指導とフィードバックを提供する AI メンターと学習者コンパニオン。

## 主な機能

Live API は、堅牢な音声エージェントを構築するための包括的な機能セットを提供します。

- [**多言語サポート**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja#supported-languages):
  70 の言語で会話できます。
- [**割り込み**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja#interruptions):
  ユーザーはいつでもモデルを中断して、応答性の高いやり取りを行うことができます。
- [**ツールの使用**](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja):
  関数呼び出しや Google 検索などのツールを統合して、動的な
  やり取りを実現します。
- [**音声文字変換**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja#audio-transcription):
  ユーザー入力とモデル出力の両方のテキスト文字変換を提供します。
- [**プロアクティブ音声**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja#proactive-audio):
  モデルが応答するタイミングやコンテキストを制御できます。
- [**アフェクティブ ダイアログ**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja#affective-dialog):
  ユーザーの入力表現に合わせて、回答のスタイルとトーンを調整します。

## 技術仕様

次の表に、Live API の技術仕様の概要を示します。

| カテゴリ | 詳細 |
| --- | --- |
| 入力モダリティ | 音声（RAW 16 ビット PCM 音声、16kHz、リトル エンディアン）、画像（JPEG <= 1FPS）、テキスト |
| 出力モダリティ | 音声（RAW 16 ビット PCM 音声、24kHz、リトル エンディアン） |
| プロトコル | ステートフル WebSocket 接続（WSS） |

## 実装方法を選択する

Live API と統合する場合は、次のいずれかの実装方法を選択する必要があります。

- **サーバー間**: バックエンドは Live API に
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) を使用して接続します。通常、クライアントはストリーム データ（音声、動画、テキスト）をサーバーに送信し、サーバーはそれを Live API に転送します。
- **クライアントからサーバー**: フロントエンド コードは Live API
  に直接接続し、[WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) を使用してバックエンドをバイパスしてデータをストリーミングします。

## 始める

開発環境に一致するガイドを選択してください。

サーバー間

### [GenAI SDK のチュートリアル](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ja)

GenAI SDK を使用して Gemini Live API に接続し、Python バックエンドでリアルタイムのマルチモーダル アプリケーションを構築します。

クライアントからサーバー

### [WebSocket のチュートリアル](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ja)

WebSocket を使用して Gemini Live API に接続し、JavaScript フロントエンドとエフェメラル トークンを使用してリアルタイムのマルチモーダル アプリケーションを構築します。

Agent Development Kit

### [ADK のチュートリアル](https://google.github.io/adk-docs/streaming/)

エージェントを作成し、Agent Development Kit（ADK）ストリーミングを使用して音声と動画の通信を有効にします。

## パートナーとの統合

リアルタイムの音声アプリと動画アプリの開発を効率化するには、
WebRTC または WebSocket 経由で Gemini Live
API をサポートするサードパーティ統合を使用します。

[LiveKit

Gemini Live API を LiveKit エージェントで使用します。](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Daily の Pipecat

Gemini Live と Pipecat を使用してリアルタイムの AI チャットボットを作成します。](https://docs.pipecat.ai/guides/features/gemini-live)
[Software Mansion の Fishjam

Fishjam を使用してライブ動画と音声のストリーミング アプリケーションを作成します。](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Stream の Vision Agents

Vision Agents を使用してリアルタイムの音声と動画の AI アプリケーションを構築します。](https://visionagents.ai/integrations/gemini)
[Voximplant

Voximplant を使用して、インバウンド通話とアウトバウンド通話を Live API に接続します。](https://voximplant.com/products/gemini-client)
[Agora

Agora を使用してリアルタイムの会話型 AI アプリケーションを構築します。](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Firebase AI Logic を使用して Gemini Live API を使ってみましょう。](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
