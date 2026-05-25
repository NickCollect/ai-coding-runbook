---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=ja
fetched_at: 2026-05-25T05:26:16.359125+00:00
title: "Gemini \u306e\u975e\u63a8\u5968 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini の非推奨

このページでは、Gemini API の[安定版（GA）](https://ai.google.dev/gemini-api/docs/models?hl=ja#stable)モデルと[プレビュー版](https://ai.google.dev/gemini-api/docs/models?hl=ja#preview)モデルの既知の非推奨スケジュールを示します。「**非推奨**」とは、モデルのサポートが終了し、近い将来に「**シャットダウン**」されることをお知らせするものです。モデルが「**シャットダウン**」されると、完全にオフになり、エンドポイントは使用できなくなります。

非推奨の発表は[リリースノート](https://ai.google.dev/gemini-api/docs/changelog?hl=ja)のページで行われ、発表された最も早いシャットダウン日はこのページで追跡されます。すでにシャットダウンされているモデルは、背景がグレーで表示されます。

## Gemini 3 モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `gemini-3.5-flash` | 2026 年 5 月 19 日 | 提供終了日は未発表 |  |
| `gemini-3.1-flash-lite` | 2026 年 5 月 7 日 | 2027 年 5 月 7 日 |  |
| モデルをプレビュー | | | |
| `gemini-3.1-flash-lite-preview` | 2026 年 3 月 3 日 | 2026 年 5 月 25 日 | `gemini-3.1-flash-lite` |
| `gemini-3.1-flash-image-preview` | 2026 年 2 月 26 日 | 提供終了日は未発表 |  |
| `gemini-3.1-pro-preview` | 2026 年 2 月 19 日 | 提供終了日は未発表 |  |
| `gemini-3-pro-image-preview` | 2025 年 11 月 20 日 | 提供終了日は未発表 |  |
| `gemini-3-flash-preview` | 2025 年 12 月 17 日 | 提供終了日は未発表 | `gemini-3.5-flash` |
| `gemini-3-pro-preview` | 2025 年 11 月 18 日 | 2026 年 3 月 9 日 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Pro モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | 2025 年 6 月 17 日 | 2026 年 10 月 16 日 | `gemini-3.1-pro-preview` |
| モデルをプレビュー | | | |
| `gemini-2.5-pro-preview-03-25` | 2025 年 3 月 3 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | 2025 年 5 月 6 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | 2025 年 6 月 5 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Flash モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | 2025 年 6 月 17 日 | 2026 年 10 月 16 日 | `gemini-3.5-flash` |
| `gemini-2.5-flash-image` | 2025 年 10 月 2 日 | 2026 年 10 月 2 日 | `gemini-3.1-flash-image-preview` |
| `gemini-2.5-flash-lite` | 2025 年 7 月 22 日 | 2026 年 10 月 16 日 | `gemini-3.1-flash-lite` |
| モデルをプレビュー | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | 2025 年 9 月 25 日 | 2026 年 3 月 31 日 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | 2025 年 5 月 20 日 | 2025 年 11 月 18 日 | `gemini-3.5-flash` |
| `gemini-2.5-flash-image-preview` | 2025 年 5 月 7 日 | 2026 年 1 月 15 日 | `gemini-2.5-flash-image` |
| `gemini-2.5-flash-preview-09-25` | 2025 年 9 月 25 日 | 2026 年 2 月 17 日 | `gemini-3.5-flash` |

## Gemini 2.0 モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | 2025 年 2 月 5 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash` |
| `gemini-2.0-flash-001` | 2025 年 2 月 5 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash` |
| `gemini-2.0-flash-lite` | 2025 年 2 月 25 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-001` | 2025 年 2 月 25 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash-lite` |
| モデルをプレビュー | | | |
| `gemini-2.0-flash-preview-image-generation` | 2025 年 5 月 7 日 | 2025 年 11 月 14 日 | `gemini-2.5-flash-image` |
| `gemini-2.0-flash-lite-preview` | 2025 年 2 月 5 日 | 2025 年 12 月 9 日 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | 2025 年 2 月 5 日 | 2025 年 12 月 9 日 | `gemini-2.5-flash-lite` |

## Live API モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `gemini-2.0-flash-live-001` | 2025 年 4 月 9 日 | 2025 年 12 月 9 日 | `gemini-3.1-flash-live-preview` |
| モデルをプレビュー | | | |
| `gemini-3.1-flash-live-preview` | 2026 年 3 月 11 日 | 提供終了日は未発表 |  |
| `gemini-2.5-flash-native-audio-preview-12-2025` | 2025 年 12 月 12 日 | 提供終了日は未発表 | `gemini-3.1-flash-live-preview` |
| `gemini-live-2.5-flash-preview` | 2025 年 6 月 17 日 | 2025 年 12 月 9 日 | `gemini-3.1-flash-live-preview` |

## 音声モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| モデルをプレビュー | | | |
| `gemini-3.1-flash-tts-preview` | 2026 年 4 月 13 日 | 提供終了日は未発表 |  |
| `gemini-2.5-flash-preview-tts` | 2025 年 5 月 20 日 | 提供終了日は未発表 | `gemini-3.1-flash-tts-preview` |
| `gemini-2.5-pro-preview-tts` | 2025 年 5 月 20 日 | 提供終了日は未発表 | `gemini-3.1-flash-tts-preview` |

## エンベディング モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `gemini-embedding-001` | 2025 年 7 月 14 日 | 2026 年 7 月 14 日 |  |
| `text-embedding-004` | 2024 年 4 月 9 日 | 2026 年 1 月 14 日 | `gemini-embedding-001` |
| モデルをプレビュー | | | |
| `embedding-001` | 2024 年 4 月 9 日 | 2025 年 10 月 30 日 | `gemini-embedding-001` |
| `embedding-gecko-001` |  | 2025 年 10 月 30 日 | `gemini-embedding-001` |
| `gemini-embedding-exp` |  | 2025 年 10 月 30 日 | `gemini-embedding-001` |
| `gemini-embedding-exp-03-07` |  | 2025 年 10 月 30 日 | `gemini-embedding-001` |

## Imagen モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | 2025 年 6 月 24 日 | 2026 年 6 月 24 日 | `gemini-3-pro-image-preview` または `gemini-2.5-flash-image` |
| `imagen-4.0-ultra-generate-001` | 2025 年 6 月 24 日 | 2026 年 6 月 24 日 | `gemini-3-pro-image-preview` または `gemini-2.5-flash-image` |
| `imagen-4.0-fast-generate-001` | 2025 年 6 月 24 日 | 2026 年 6 月 24 日 | `gemini-3-pro-image-preview` または `gemini-2.5-flash-image` |
| `imagen-3.0-generate-002` | 2025 年 2 月 6 日 | 2025 年 11 月 10 日 | `imagen-4.0-generate-001` |
| モデルをプレビュー | | | |
| `imagen-4.0-generate-preview-06-06` | 2025 年 6 月 24 日 | 2026 年 2 月 17 日 | `imagen-4.0-generate-001` |
| `imagen-4.0-ultra-generate-preview-06-06` | 2025 年 6 月 24 日 | 2026 年 2 月 17 日 | `imagen-4.0-ultra-generate-001` |

## Veo モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | 2025 年 9 月 9 日 | 近日提供予定 | `veo-3.1-generate-preview` |
| `veo-3.0-fast-generate-001` | 2025 年 9 月 9 日 | 近日提供予定 | `veo-3.1-lite-generate-preview` |
| `veo-2.0-generate-001` | 2025 年 4 月 9 日 | 近日提供予定 | `veo-3.1-generate-preview` |
| モデルをプレビュー | | | |
| `veo-3.1-lite-generate-preview` | 2026 年 3 月 31 日 | 提供終了日は未発表 |  |
| `veo-3.1-generate-preview` | 2025 年 10 月 15 日 | 提供終了日は未発表 |  |
| `veo-3.1-fast-generate-preview` | 2025 年 10 月 15 日 | 提供終了日は未発表 |  |
| `veo-3.0-generate-preview` | 2025 年 7 月 31 日 | 2025 年 11 月 12 日 | `veo-3.1-generate-preview` |
| `veo-3.0-fast-generate-preview` | 2025 年 7 月 31 日 | 2025 年 11 月 12 日 | `veo-3.1-fast-generate-preview` |

## Lyria モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| `lyria-3-clip-preview` | 2026 年 3 月 25 日 | 提供終了日は未発表 |  |
| `lyria-3-pro-preview` | 2026 年 3 月 25 日 | 提供終了日は未発表 |  |
| `lyria-realtime-exp` | 2025 年 5 月 20 日 | 提供終了日は未発表 |  |

## ロボット工学モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される交換** |
| --- | --- | --- | --- |
| モデルをプレビュー | | | |
| `gemini-robotics-er-1.6-preview` | 2026 年 4 月 14 日 | サービス終了日は未発表 |  |
| `gemini-robotics-er-1.5-preview` | 2025 年 9 月 25 日 | 2026 年 4 月 30 日 | `gemini-robotics-er-1.6-preview` |

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-19 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-19 UTC。"],[],[]]
