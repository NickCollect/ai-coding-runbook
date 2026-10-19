---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=zh-TW
fetched_at: 2026-10-19T05:36:51.470500+00:00
title: "\u8108\u7d61\u5feb\u53d6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 脈絡快取

在一般的 AI 工作流程中，您可能會反覆將相同的輸入權杖傳遞給模型。Gemini API 提供隱含快取功能，可提升效能並節省費用。

## 隱含快取

所有 Gemini 2.5 和更新版本模型，預設都會啟用隱式快取功能。有狀態 (使用 `previous_interaction_id`) 和無狀態對話模式均支援這項功能。如果要求命中快取，我們會自動降低費用。開啟這項功能時，不需要進行任何設定。下表列出各模型的輸入詞元數下限：

| 模型 | 詞元數量下限 |
| --- | --- |
| Gemini 4 Argon | 4,096 |
| Gemini 3.8 Flash | 4,096 |
| Gemini 3.6 Flash | 4,096 |
| Gemini 3.1 Pro 預先發布版 | 4,096 |
| Gemini 2.5 Flash | 2,048 |
| Gemini 2.5 Pro | 2,048 |

如要提高隱性快取命中率，請採取下列行動：

- 嘗試在提示開頭放置大型且常見的內容
- 嘗試在短時間內傳送具有類似前置字元的要求

您可以在回應物件的 `usage.total_cached_tokens` (Python 和 JavaScript) 欄位中，查看快取命中的詞元數量。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-13 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-13 (世界標準時間)。"],[],[]]
