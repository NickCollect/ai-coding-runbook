---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=zh-TW
fetched_at: 2026-06-15T06:27:24.597128+00:00
title: "Gemini API \u6700\u4f73\u5316\u548c\u63a8\u8ad6 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini API 最佳化和推論

Gemini API 提供多種最佳化機制，可協助您根據特定工作負載需求，在速度、成本和可靠性之間取得平衡。無論是建構即時對話機器人，還是執行大量離線資料處理管道，選擇合適的範例都能大幅降低成本或提升效能。

| 功能 | 標準 | Flex | 優先順序 | 批次 | 快取 |
| --- | --- | --- | --- | --- | --- |
| **定價** | 原價 | 50% 折扣 | 比標準價格高出 75% 至 100% | 50% 折扣 | 90% 折扣 + 按比例分攤的權杖儲存空間 |
| **延遲** | 秒到分鐘 | 分鐘 (目標：1 到 15 分鐘) | 秒 | 長達 24 小時 | 縮短第一個詞元生成時間 |
| **穩定性** | 高 / 中高 | 盡可能提供最佳服務 (可捨棄) | 高 (不會脫落) | 高 (處理量) | 不適用 |
| **介面** | 同步 | 同步 | 同步 | 非同步 | 已儲存狀態 |
| **最佳用途** | 一般應用程式工作流程 | 非緊急的連續鏈結 | 生產環境、面向使用者的應用程式 | 龐大的資料集、離線評估 | 對相同檔案重複查詢 |

## 推論服務層級 (同步)

在標準生成呼叫中傳遞 `service_tier` 參數，即可在以可靠性為重和以成本為重的同步流量之間切換。

### 標準推論 (預設)

標準層級是連續生成內容的預設選項。可提供正常的回應時間，不會收取額外費用，也不會出現大量排隊情況。

- **可靠性：**標準嚴重性
- **價格：**標準價格。
- **適用情況：**最適合日常互動式應用程式。

### 優先推論 (延遲時間最佳化)

[優先順序](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)處理程序會將要求傳送至高重要性的運算佇列。這類流量絕對不會遭到捨棄 (絕不會遭到其他層級搶占)，而且可靠性最高。如果超過動態優先順序限制，系統會將要求降級為標準處理程序，而不是傳回錯誤。

- **可靠性：**最高嚴重程度
- **價格：**比標準費率高 75% 至 100%。
- **適用情況：**客戶聊天機器人、即時詐欺偵測，以及業務關鍵的副駕駛。

### 彈性推論 (成本最佳化)

[彈性推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-tw)會利用離峰時段的運算容量，因此與標準費率相比，可享有 50% 的折扣。要求會同步處理，因此您不必重新編寫程式碼來管理批次物件。由於這是「可捨棄」的流量，如果系統發生標準流量尖峰，要求可能會遭到搶占。

- **可靠性：**無保證，可捨棄的重大性
- **價格：**標準價格的 50% (按權杖計費)。
- **最適合：**多步驟代理式工作流程，其中呼叫 N+1 取決於呼叫 N 的輸出內容、背景 CRM 更新和離線評估。

## 批次 API (大量、非同步)

[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw) 的設計宗旨，是以標準費用的 50%，非同步處理大量要求。您可以內嵌字典或使用 JSONL 輸入檔案 (最多 2 GB) 提交要求。這項服務會使用背景處理量佇列處理要求，目標處理時間為 24 小時。

- **可靠性：**可捨棄，但有 24 小時自動重試和佇列系統
- **價格：**標準價格的 50%。
- **最適合：**預先處理大量資料集、執行週期性迴歸測試套件，以及大量產生圖片或嵌入內容。

## 脈絡快取 (節省輸入內容)

當較短的要求重複參照大量初始脈絡時，就會使用「[脈絡快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)」。

- **隱式快取：**Gemini 2.5 以上模型會自動啟用這項功能。
  如果要求根據常見提示前置字元命中現有快取，系統會將節省的費用轉移給您。
- **明確快取：**您可以手動建立快取物件，並指定存留時間 (TTL)。建立後，您可以在後續要求中參照快取權杖，避免重複傳遞相同的語料庫酬載。
- **價格：**根據快取權杖數量和儲存時間 (TTL) 計費。
- **最適合：**具有大量系統指令的聊天機器人、重複分析冗長影片檔案，或針對大型文件集進行查詢。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-04-29 (世界標準時間)。"],[],[]]
