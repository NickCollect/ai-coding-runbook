---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=zh-TW
fetched_at: 2026-10-26T05:50:37.723042+00:00
title: "AI Studio \u5be6\u9a57\u5ba4\u4e2d\u7684\u4ee3\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# AI Studio 實驗室中的代理

Google AI Studio Playground 提供視覺化介面，讓您不必建立及編寫 API 呼叫，就能製作原型並瞭解如何建構受管理代理程式。

如要開始使用，請前往 Google AI Studio 導覽面板中的「Playground」分頁，然後將切換鈕切換至「Agents」。

## 預先建構的範本

「Agents」(代理) 分頁中有一系列範本，可透過設定工具和環境設定，預先設定基礎 Antigravity 代理。所有範本皆為開放原始碼，並發布於 [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/) 存放區。探索這些範本是瞭解如何建構及架構自有代管代理程式的絕佳方式。

舉例來說，選取「AI Radio」範本時，系統會啟用所有允許的工具，並連結專門用於製作電台節目的 `AGENTS.md` 檔案和技能。如要查看這些設定，請在 Playground 使用者介面的「Environment」(環境) 專區下方，按一下「Sources」(來源) 按鈕。

## 工具設定

在 Playground 的「代理程式設定」下方，您可以切換下列內建工具的存取權：

- **Google 搜尋：**存取開放網路，以即時資訊建立基準。
- **網址內容：**擷取並剖析特定網頁網址的文字內容。
- **程式碼執行：**直接在獨立的沙箱環境中執行 Bash 和 Python 指令。
- **檔案系統工具：**讀取、寫入、列出及刪除工作區內的檔案。

## 環境設定

受管理代理程式會在安全、暫時性的 Linux 沙箱 (即環境) 中執行，並提供運作所需的工作區和工具。詳情請參閱[受管理代理程式環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)指南。

### 控管代理程式行為

代理的行為、角色和功能主要取決於環境中的檔案。代理程式會自動偵測並載入特殊 `.agents` 資料夾中的設定：

- **`AGENTS.md`**：預先載入代理程式的環境，定義系統指令和角色。
- **`SKILL.md`**：位於各技能資料夾 (例如 `.agents/skills/my-skill/SKILL.md`) 下方，用於定義特定功能和工作流程。

### 佈建環境

您可以在啟動工作階段前，將檔案掛接到環境，藉此設定代理程式使用的環境。您可以透過掛接來源建立新環境，也可以還原先前的環境：

- **如要建立新環境**，請在「環境設定」面板中點選「新增來源」，然後選擇下列來源類型：

| 來源類型 | 說明 | 安裝路徑 |
| --- | --- | --- |
| **內嵌檔案** | 直接在 Playground UI 中撰寫或貼上設定檔、模擬資料集或公用程式指令碼 (最多 100 KB)。 | 使用者定義的目的地路徑 (例如 `/workspace/scripts/parser.py`)。 |
| **Google Cloud Storage** | 掛接公開或私人的 Cloud Storage bucket。  私人 bucket 需要標準 OAuth 2.0 不記名權杖。詳情請參閱「[私人來源](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#private-sources)」。 | 將 GCS bucket 路徑 (例如 `gs://your-bucket-name/data/`) 對應至工作區目錄 (例如 `/workspace/data/`)。 |
| **GitHub 存放區** | 複製公開或私人的程式碼庫。  如要複製私人存放區，必須使用 GitHub 個人存取權杖 (PAT) 進行基本驗證。詳情請參閱「[私人來源](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#private-sources)」。 | 直接複製到 `/workspace/` (通常位於 `/workspace/<repo-name>`)。 |

- **如要還原先前的環境**，可以[重複使用現有的環境 ID](#reusing-an-existing-environment-id)，複製並分叉其確切狀態。

### 重複使用現有環境 ID

如果您已花時間設定沙箱環境，就不必從頭開始。如要使用現有環境：

1. 前往 AI Studio 的「環境」面板，然後將「類型」切換為「現有」
2. **輸入「Environment ID」(環境 ID)，例如 `env_abc123`**

詳情請參閱「[設定環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#configure-an-environment)」。您也可以從 UI 的「環境」分頁擷取目前工作階段的環境 ID。

首次傳送訊息給服務專員後，該工作階段的環境設定就會固定。互動正在執行時，您無法掛接新來源或修改網路許可清單。

## 下載環境

建立環境後，您隨時可以使用 AI Studio Playground 環境設定中的「下載」按鈕，下載環境快照，以 tarball 形式擷取環境檔案。

## 安全與成本管理

### 管理權杖用量

與產生單一輸出的標準即時通訊要求不同，Antigravity Agent 會執行自主工作流程。這項工具會規劃、執行程式碼、觀察結果，然後疊代。也就是說，單一提示可能會導致無上限的權杖消耗量。

如要控管費用，請**在提示中提供明確的終止條件，並為 Agent 縮小工作範圍**。舉例來說，提示可以是「Review the pull request and stop once you have generated the markdown summary.」(審查提取要求，產生 Markdown 摘要後停止)。*請勿嘗試自行編寫修正內容*。

### 額外費用

根據預設，Playground 上的所有代理程式範本都能存取 Gemini API 服務，並從環境中發出 API 呼叫，以滿足要求。這些項目可能會產生額外費用，但不會反映在權杖消耗量中。

同樣地，如果您新增其他外部服務，代理程式可能會代表您呼叫這些服務，進而產生額外費用。

### 網路許可清單

根據預設，為確保安全，AI Studio 會嚴格控管及限制代理程式沙箱環境中的所有輸出網路要求。如要授予代理程式存取外部 API、網路服務或套件管理工具的權限，請明確宣告這些項目：

1. 前往 AI Studio 的「環境」面板。
2. 選取「網路」旁的「規則」按鈕。
3. 在「網路設定」面板中，按一下「新增至允許清單」，然後填寫相關詳細資料：
   - **網域限制：**只有加入清單的特定網域或萬用字元模式，才能由代理程式的虛擬機器存取。舉例來說，您可以輸入確切網域 (例如 `api.github.com`)，也可以輸入廣泛模式 (例如 `*.googleapis.com`)。
   - **新增 HTTP 標頭和權杖插入：**使用「新增 HTTP 標頭」選項，為特定網域安全地插入必要憑證 (例如 API 權杖)。這些憑證會安全地通過輸出 Proxy，絕不會直接以原始文字的形式顯示在代理程式沙箱中。

將網域加入許可清單時，請務必謹慎。授予代理程式已驗證服務的存取權，代表代理程式可以代您執行動作，如果未仔細監控，可能會導致非預期的動作。

### 憑證最佳做法

如果工作流程需要代理程式向外部服務進行驗證，您必須負責佈建及設定這些憑證的範圍。請遵循下列規範，降低風險：

- **使用最低權限憑證：**建立服務帳戶或 API 金鑰時，只授予代理程式所需的權限。請避免傳遞具有廣泛或管理員存取權的憑證。
- **盡量使用短期權杖：**盡可能使用有時間限制的憑證或權杖，而非長期有效的 API 金鑰。
- **取得完整存取權：**代理程式可以使用有權存取的任何憑證，完成您指派的工作。請只提供您願意授予完整存取權的憑證。
- **定期輪替憑證：**將與代理程式共用的憑證視為任何程式輔助憑證，並定期輪替。

### 連結外部工具和 API

您可以連結外部工具和 API (例如 Model Context Protocol / MCP 伺服器)，擴充代理的功能。這麼做時，請注意下列事項：

- 請只連結信任來源的工具。惡意或編寫不當的工具可能會洩漏資料或執行非預期的動作。
- 請根據用途需求，為工具設定最低必要權限。如果工具支援唯讀模式，請優先使用該模式，除非必須寫入。
- 將工具連線至正式版資料來源前，請先使用範例或合成資料進行測試，確認代理程式會如預期使用這些資料。

### 專人監督

代理可自主推論、規劃及執行多步驟工作流程。這項功能非常強大，但也表示您應適當監督，尤其是修改資料或與外部系統互動的工作。

部署前，請務必驗證產生的程式碼、資料轉換或設定變更等重要輸出內容。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-08-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-08-19 (世界標準時間)。"],[],[]]
