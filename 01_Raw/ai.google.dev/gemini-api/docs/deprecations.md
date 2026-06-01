---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-TW
fetched_at: 2026-06-01T05:57:45.258151+00:00
title: "Gemini \u6dd8\u6c70\u9805\u76ee \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini 淘汰項目

本頁列出 Gemini API 中[穩定版 (正式發布)](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#stable) 和[搶先版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#preview)模型的已知淘汰時間表。「**淘汰**」是指我們宣布不再支援某個模型，並會在不久的將來「**關閉**」該模型。模型「**關閉**」後，就會完全關閉，且端點將無法再使用。

淘汰公告會發布在「[版本資訊](https://ai.google.dev/gemini-api/docs/changelog?hl=zh-tw)」頁面，而最早的停用日期則會追蹤並顯示在這個頁面。
已停用的模型會以灰色背景表示。

## Gemini 3 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `gemini-3.5-flash` | 2026 年 5 月 19 日 | 未公布關閉日期 |  |
| `gemini-3.1-flash-image` | 2026 年 5 月 28 日 | 未公布關閉日期 |  |
| `gemini-3-pro-image` | 2026 年 5 月 28 日 | 未公布關閉日期 |  |
| `gemini-3.1-flash-lite` | 2026 年 5 月 7 日 | 2027 年 5 月 7 日 |  |
| 預先發布版模型 | | | |
| `gemini-3.1-flash-image-preview` | 2026 年 2 月 26 日 | 2026 年 6 月 25 日 | `gemini-3.1-flash-image` |
| `gemini-3.1-pro-preview` | 2026 年 2 月 19 日 | 未公布關閉日期 |  |
| `gemini-3-pro-image-preview` | 2025 年 11 月 20 日 | 2026 年 6 月 25 日 | `gemini-3-pro-image` |
| `gemini-3-flash-preview` | 2025 年 12 月 17 日 | 未公布關閉日期 | `gemini-3.5-flash` |
| `gemini-3-pro-preview` | 2025 年 11 月 18 日 | 2026 年 3 月 9 日 | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | 2026 年 3 月 3 日 | 2026 年 5 月 25 日 | `gemini-3.1-flash-lite` |

## Gemini 2.5 Pro 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | 2025 年 6 月 17 日 | 2026 年 10 月 16 日 | `gemini-3.1-pro-preview` |
| 預先發布版模型 | | | |
| `gemini-2.5-pro-preview-03-25` | 2025 年 3 月 3 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | 2025 年 5 月 6 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | 2025 年 6 月 5 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Flash 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | 2025 年 6 月 17 日 | 2026 年 10 月 16 日 | `gemini-3.5-flash` |
| `gemini-2.5-flash-image` | 2025 年 10 月 2 日 | 2026 年 10 月 2 日 | `gemini-3.1-flash-image-preview` |
| `gemini-2.5-flash-lite` | 2025 年 7 月 22 日 | 2026 年 10 月 16 日 | `gemini-3.1-flash-lite` |
| 預先發布版模型 | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | 2025 年 9 月 25 日 | 2026 年 3 月 31 日 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | 2025 年 5 月 20 日 | 2025 年 11 月 18 日 | `gemini-3.5-flash` |
| `gemini-2.5-flash-image-preview` | 2025 年 5 月 7 日 | 2026 年 1 月 15 日 | `gemini-2.5-flash-image` |
| `gemini-2.5-flash-preview-09-25` | 2025 年 9 月 25 日 | 2026 年 2 月 17 日 | `gemini-3.5-flash` |

## Gemini 2.0 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | 2025 年 2 月 5 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash` |
| `gemini-2.0-flash-001` | 2025 年 2 月 5 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash` |
| `gemini-2.0-flash-lite` | 2025 年 2 月 25 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-001` | 2025 年 2 月 25 日 | 2026 年 6 月 1 日 | `gemini-2.5-flash-lite` |
| 預先發布版模型 | | | |
| `gemini-2.0-flash-preview-image-generation` | 2025 年 5 月 7 日 | 2025 年 11 月 14 日 | `gemini-2.5-flash-image` |
| `gemini-2.0-flash-lite-preview` | 2025 年 2 月 5 日 | 2025 年 12 月 9 日 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | 2025 年 2 月 5 日 | 2025 年 12 月 9 日 | `gemini-2.5-flash-lite` |

## 使用中的 API 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `gemini-2.0-flash-live-001` | 2025 年 4 月 9 日 | 2025 年 12 月 9 日 | `gemini-3.1-flash-live-preview` |
| 預先發布版模型 | | | |
| `gemini-3.1-flash-live-preview` | 2026 年 3 月 11 日 | 未公布關閉日期 |  |
| `gemini-2.5-flash-native-audio-preview-12-2025` | 2025 年 12 月 12 日 | 未公布關閉日期 | `gemini-3.1-flash-live-preview` |
| `gemini-live-2.5-flash-preview` | 2025 年 6 月 17 日 | 2025 年 12 月 9 日 | `gemini-3.1-flash-live-preview` |

## 音訊模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| 預先發布版模型 | | | |
| `gemini-3.1-flash-tts-preview` | 2026 年 4 月 13 日 | 未公布關閉日期 |  |
| `gemini-2.5-flash-preview-tts` | 2025 年 5 月 20 日 | 未公布關閉日期 | `gemini-3.1-flash-tts-preview` |
| `gemini-2.5-pro-preview-tts` | 2025 年 5 月 20 日 | 未公布關閉日期 | `gemini-3.1-flash-tts-preview` |

## 嵌入模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `gemini-embedding-001` | 2025 年 7 月 14 日 | 2026 年 7 月 14 日 | `gemini-embedding-2` |
| `text-embedding-004` | 2024 年 4 月 9 日 | 2026 年 1 月 14 日 | `gemini-embedding-2` |
| 預先發布版模型 | | | |
| `embedding-001` | 2024 年 4 月 9 日 | 2025 年 10 月 30 日 | `gemini-embedding-2` |
| `embedding-gecko-001` |  | 2025 年 10 月 30 日 | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | 2025 年 10 月 30 日 | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | 2025 年 10 月 30 日 | `gemini-embedding-2` |

## Imagen 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | 2025 年 6 月 24 日 | 2026 年 6 月 24 日 | `gemini-3-pro-image-preview` 或  `gemini-2.5-flash-image` |
| `imagen-4.0-ultra-generate-001` | 2025 年 6 月 24 日 | 2026 年 6 月 24 日 | `gemini-3-pro-image-preview` 或  `gemini-2.5-flash-image` |
| `imagen-4.0-fast-generate-001` | 2025 年 6 月 24 日 | 2026 年 6 月 24 日 | `gemini-3-pro-image-preview` 或  `gemini-2.5-flash-image` |
| `imagen-3.0-generate-002` | 2025 年 2 月 6 日 | 2025 年 11 月 10 日 | `imagen-4.0-generate-001` |
| 預先發布版模型 | | | |
| `imagen-4.0-generate-preview-06-06` | 2025 年 6 月 24 日 | 2026 年 2 月 17 日 | `imagen-4.0-generate-001` |
| `imagen-4.0-ultra-generate-preview-06-06` | 2025 年 6 月 24 日 | 2026 年 2 月 17 日 | `imagen-4.0-ultra-generate-001` |

## Veo 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | 2025 年 9 月 9 日 | 即將推出 | `veo-3.1-generate-preview` |
| `veo-3.0-fast-generate-001` | 2025 年 9 月 9 日 | 即將推出 | `veo-3.1-lite-generate-preview` |
| `veo-2.0-generate-001` | 2025 年 4 月 9 日 | 即將推出 | `veo-3.1-generate-preview` |
| 預先發布版模型 | | | |
| `veo-3.1-lite-generate-preview` | 2026 年 3 月 31 日 | 未公布關閉日期 |  |
| `veo-3.1-generate-preview` | 2025 年 10 月 15 日 | 未公布關閉日期 |  |
| `veo-3.1-fast-generate-preview` | 2025 年 10 月 15 日 | 未公布關閉日期 |  |
| `veo-3.0-generate-preview` | 2025 年 7 月 31 日 | 2025 年 11 月 12 日 | `veo-3.1-generate-preview` |
| `veo-3.0-fast-generate-preview` | 2025 年 7 月 31 日 | 2025 年 11 月 12 日 | `veo-3.1-fast-generate-preview` |

## Lyria 模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| `lyria-3-clip-preview` | 2026 年 3 月 25 日 | 未公布關閉日期 |  |
| `lyria-3-pro-preview` | 2026 年 3 月 25 日 | 未公布關閉日期 |  |
| `lyria-realtime-exp` | 2025 年 5 月 20 日 | 未公布關閉日期 |  |

## 機器人模型

| **型號** | **發布日期** | **停用日期** | **建議更換** |
| --- | --- | --- | --- |
| 預先發布版模型 | | | |
| `gemini-robotics-er-1.6-preview` | 2026 年 4 月 14 日 | 未公布關閉日期 |  |
| `gemini-robotics-er-1.5-preview` | 2025 年 9 月 25 日 | 2026 年 4 月 30 日 | `gemini-robotics-er-1.6-preview` |

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-29 (世界標準時間)。"],[],[]]
