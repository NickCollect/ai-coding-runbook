---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-TW
fetched_at: 2026-05-05T13:11:57.830556+00:00
title: "\u4f7f\u7528 Gemini MCP \u548c Skills \u8a2d\u5b9a\u7a0b\u5f0f\u8a2d\u8a08\u52a9\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

- [首頁](https://ai.google.dev/gemini-api/docs/首頁)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [文件](https://ai.google.dev/gemini-api/docs/文件)

提供意見

# 使用 Gemini MCP 和 Skills 設定程式設計助理

AI 程式設計助理功能強大，但仍有其限制，例如訓練資料會在特定日期截止，因此無法提供新的 API 功能和變更。如果無法存取 Gemini 專屬文件，服務專員可能會建議一般模式，而非最佳化方法。

為確保程式設計助理能跟上不斷演進的 Gemini API 和建議用法，建議您設定 **Gemini 文件 MCP**，並透過 **Gemini API 技能**強化環境。這些工具可獨立使用，但設計宗旨是搭配運作，提供完整涵蓋範圍。

## 連結 Gemini Docs MCP

Gemini 在 `https://gemini-api-docs-mcp.dev` 託管公開的 Model Context Protocol (MCP) 伺服器。將程式碼編寫代理程式連線至這個伺服器，可確保所有查詢都能存取最新的 API、程式碼更新和最佳設定範例。

在代理程式的終端機或專案根目錄中執行下列指令，安裝伺服器：

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

這個伺服器會新增 `search_documentation` 函式，供代理程式從官方 Gemini 說明文件檔案擷取即時 API 定義和整合模式。

## 新增 API 開發技能

這些技能會直接在助理的環境中提供**內建規則和最佳做法** (例如強制使用正確的 SDK 和目前模型版本)。這項技能會與 Gemini 文件 MCP 服務搭配運作：如果兩者都已安裝，這項技能會使用 MCP 服務來產生說明文件，但即使未安裝 MCP，系統也會從 `ai.google.dev` 擷取 `llms.txt` 做為備援。

如要安裝這些技能，可以使用下列任一支援的工具。每個技能模組下方都有安裝說明：

- **[skills.sh](https://ai.google.dev/gemini-api/docs/skills.sh)**：建議使用。可攜式代理程式行為的開放標準。
- **[Context7](https://ai.google.dev/gemini-api/docs/Context7)**：支援已使用 Context7 生態系統的使用者。

### gemini-api-dev

這是開發一般用途 Gemini 應用程式的基礎技能。這項技能提供下列項目的文件和最佳做法：

- 將提示詞傳送至目前模型 (例如 Gemini 3.1 Pro/Flash)，並避開已淘汰的模型
- 多模態提示、函式呼叫、結構化輸出內容和常見的整合模式

#### 使用 skills.sh 安裝

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### 使用 Context7 安裝

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

這項技能可協助您使用 Gemini Live API 建構即時對話式 AI 應用程式。這項技能提供下列項目的文件和最佳做法：

- WebSocket 連線，用於低延遲串流
- 串流音訊、影片和文字
- 語音活動偵測和插話支援

#### 使用 skills.sh 安裝

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### 使用 Context7 安裝

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

使用 [Interactions API](https://ai.google.dev/gemini-api/docs/Interactions API) 建構應用程式的技能。Interactions API 是與 Gemini 模型和代理程式互動的統一介面，專為代理程式應用程式設計。這項技能涵蓋的主題包括：

- 生成文字、進行多輪對話及串流
- 函式呼叫、結構化輸出內容和圖像生成
- 背景執行和 Deep Research 代理
- 伺服器端對話狀態管理
- Python 和 TypeScript SDK 模式

#### 使用 skills.sh 安裝

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### 使用 Context7 安裝

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## 驗證安裝

安裝完成後，請確認程式碼助理可以連線至 Gemini Docs MCP 伺服器，並使用您安裝的技能。

### 1. 驗證服務專員行為

如要驗證，最可靠的方式是向服務專員詢問有關 Gemini API 的技術問題。

**提示：**「如何使用 Gemini API 的脈絡快取功能？」

設定成功後，系統會：

- **提供準確的程式碼**：從最新端點參照特定 Gemini 方法，例如 `cacheContent` 或 `cachedContents.create`。
- **使用 MCP 工具**：顯示工具已連線至 **Gemini 文件 MCP 伺服器**，或使用 `search_documentation` 工具擷取資料。
- **叫用已載入的技能**：顯示「使用技能：gemini-api-dev」指標 (如果依附於次要包裝函式)。

### 2. 驗證表現和工具

如果代理程式提供一般或通用答案，請使用環境專用的 Discovery 或 Status 指令，確認文件 MCP 或技能已載入記憶體。

| 環境 | MCP 驗證 | 技能驗證 |
| --- | --- | --- |
| **Claude Code** | 在終端機中輸入 `/mcp`，即可查看有效伺服器和 `search_documentation` 工具。 | 在終端機中輸入 `/skills`，即可列出所有有效資訊清單。 |
| **游標** | 依序前往「設定」>「功能」>「MCP」。確認伺服器為「已連線」狀態。 | 依序開啟「設定」>「規則」。確認技能顯示在「Agent Decides」下方。 |
| **Antigravity** | 檢查「自訂」>「連結」側欄中的 MCP 狀態。 | 輸入 `/skills list` 或查看「自訂」>「規則」側欄。 |
| **Gemini CLI** | 執行 `gemini mcp list` 或使用 `/mcp list`。 | 執行 `gemini skills list` 或在工作階段中使用 `/skills` 斜線指令。 |
| **Copilot** | 輸入 `@gemini /mcp` 即可列出有效的資料連接器。 | 輸入 `@gemini /skills` (或 `/skills`) 即可查看有效擴充功能。 |

## 疑難排解

如果代理程式只提供一般資訊，或無法辨識 Gemini 專屬方法，請檢查下列事項：

### 代理程式未探索到技能

大多數代理程式只會在啟動時為技能建立索引。

**修正方式：**完全重新啟動 IDE (Cursor/VS Code)，或結束並重新開啟終端機型代理程式 (Claude Code)。

### 全球與在地衝突

如果您使用 `--global` 旗標安裝代理程式，代理程式可能會忽略該旗標，而採用專案專屬規則。

**修正：**嘗試直接在專案根目錄中安裝技能，不要使用全域標記：

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## 資源

- [GitHub 上的 Gemini API 技能](https://ai.google.dev/gemini-api/docs/GitHub 上的 Gemini API 技能)
- [互動 API](https://ai.google.dev/gemini-api/docs/互動 API)
- [快速入門導覽課程](https://ai.google.dev/gemini-api/docs/快速入門導覽課程)
- [程式庫](https://ai.google.dev/gemini-api/docs/程式庫)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://ai.google.dev/gemini-api/docs/創用 CC 姓名標示 4.0 授權)，程式碼範例則為[阿帕契 2.0 授權](https://ai.google.dev/gemini-api/docs/阿帕契 2.0 授權)。詳情請參閱《[Google Developers 網站政策](https://ai.google.dev/gemini-api/docs/Google Developers 網站政策)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？
