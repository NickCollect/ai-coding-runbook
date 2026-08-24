---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=zh-TW
fetched_at: 2026-08-24T02:20:02.354509+00:00
title: "\u4f7f\u7528 Gemini API \u91d1\u9470 \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini API 金鑰

如要使用 Gemini API，必須驗證要求。您可以使用標準或授權 API 金鑰進行驗證。

[建立或查看 Gemini API 金鑰](https://aistudio.google.com/apikey?hl=zh-tw)

## API 金鑰類型：標準與授權

API 金鑰可存取 Gemini API，但安全性特徵不同。為提升安全性，Gemini API 將從標準 API 金鑰改用授權金鑰：

- **標準 API 金鑰**：將要求與 Google Cloud 專案建立關聯，以利帳單和配額管理。標準金鑰不會識別呼叫者，因此可支援的權限和存取權控管精細度有限。
- **授權 (auth) 金鑰**：直接繫結至 Google Cloud 服務帳戶。使用授權金鑰時，系統會以繫結服務帳戶的身分處理要求，方便您進行精細的存取權控管。授權金鑰預設只能用於 Generative Language API (Gemini API)，且可快速強制停用遭外洩的金鑰，一旦系統偵測到金鑰外洩，就會立即停止使用。

為確保安全使用，Gemini API 將從標準金鑰改用驗證金鑰：

- **預設驗證金鑰**：在 Google AI Studio 建立的所有新 API 金鑰，都會自動建立為驗證金鑰。
- **拒絕未設限的金鑰**：Gemini API 會拒絕**未設限標準金鑰**的要求。已明確套用限制的標準 API 金鑰仍可繼續使用。這項限制可防止未經授權使用可能公開分享或連結至其他服務的金鑰。
- **2026 年 9 月**：Gemini API 將拒絕**標準金鑰**的要求。請務必在上述日期前[遷移至驗證金鑰](#migrate-to-auth-key)，以免服務中斷。請務必在 2026 年 9 月前遷移至驗證金鑰。

## 在 Google AI Studio 中管理 API 金鑰

您可以在 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-tw) 中直接管理專案和金鑰。

### Google Cloud 專案

每個 Gemini API 金鑰都與 [Google Cloud 專案](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=zh-tw)相關聯。
Google Cloud 專案可管理帳單、協作者和權限。Google AI Studio 提供輕量型介面，方便您存取這些專案。

- **預設專案**：如果您是新使用者，接受《服務條款》後，Google AI Studio 會自動建立預設的 Google Cloud 雲端專案和 API 金鑰。如要重新命名這個專案，請前往資訊主頁的「專案」檢視畫面。
- **現有專案**：如果您已有 Google Cloud 帳戶，AI Studio 不會建立預設專案。而是必須匯入現有專案。

### 匯入專案

根據預設，Google AI Studio 不會顯示所有 Google Cloud 專案。您必須匯入要使用的專案：

1. 前往 [Google AI Studio](https://aistudio.google.com?hl=zh-tw)。
2. 開啟左側面板的「資訊主頁」，然後選取「專案」。
3. 按一下「匯入專案」按鈕。
4. 搜尋並選取要匯入的 Google Cloud 雲端專案，然後按一下**匯入**。
5. 匯入後，請前往資訊主頁的「API 金鑰」頁面，在該專案中建立金鑰。

### 排解金鑰建立權限問題

如果「建立 API 金鑰」按鈕無法使用，並顯示「您沒有權限在這個專案中建立金鑰」訊息，表示您沒有必要的 IAM 權限。

請 Google Cloud 專案或機構管理員授予您具備下列權限的角色 (例如專案編輯者)：

- `resourcemanager.projects.get`：允許 AI Studio 驗證專案。
- `apikeys.keys.create`：允許產生金鑰。
- `serviceusage.services.enable`：確認已啟用 Generative Language API。
- `iam.serviceAccounts.create`：建立連結的服務帳戶時必須提供。
- `iam.serviceAccountApiKeyBindings.create`：將服務帳戶繫結至 API 金鑰。

如果無法取得管理員存取權，可以建立未與機構相關聯的新 Google Cloud 專案，產生金鑰。

## 設定環境

取得金鑰後，請設定環境，以便在應用程式中安全地使用金鑰。

### 選項 1：使用環境變數 (建議)

設定環境變數 `GEMINI_API_KEY` 或 `GOOGLE_API_KEY`。Gemini API 用戶端程式庫會自動偵測並使用這些變數。如果兩者都已設定，系統會優先採用 `GOOGLE_API_KEY`。

選取作業系統來設定變數：

### Linux/macOS - Bash

確認您是否有 Bash 設定檔：

```
~/.bashrc
```

如果沒有，請建立並開啟：

```
touch ~/.bashrc && open ~/.bashrc
```

在檔案結尾新增匯出指令：

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

儲存檔案，然後套用變更：

```
source ~/.bashrc
```

### macOS - Zsh

確認你是否有 zsh 設定檔：

```
~/.zshrc
```

如果沒有，請建立並開啟：

```
touch ~/.zshrc && open ~/.zshrc
```

新增匯出指令：

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

儲存檔案，然後套用變更：

```
source ~/.zshrc
```

### Windows

1. 在 Windows 搜尋列中搜尋「環境變數」。
2. 在「系統內容」對話方塊中，按一下「環境變數」。
3. 在「使用者變數」或「系統變數」下方，按一下「新增...」。
4. 將變數名稱設為 `GEMINI_API_KEY`，並將值設為您的 API 金鑰。
5. 按一下 [確定] 進行儲存。開啟新的終端機工作階段，載入變數。

### 方法 2：在程式碼中明確提供 API 金鑰

初始化用戶端時，您可以明確傳遞 API 金鑰。只有在無法使用環境變數時，才需要這麼做。

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
    "google.golang.org/genai/interactions"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.6-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.6-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## 安全性和密鑰管理

請妥善保管 Gemini API 金鑰，如同其他密碼一般。一旦遭盜用，他人就能耗用專案配額、產生非預期的帳單費用，以及存取私人資源。

### 重大安全性規則

- **確保金鑰機密性**：請勿將 API 金鑰登錄至 Git 等原始碼控管系統。
- **切勿在正式版中向用戶端公開金鑰**：請勿直接在網頁或行動應用程式中以硬式編碼加入 API 金鑰。使用者可以擷取用戶端程式碼中編譯的鍵。如要保護用戶端應用程式，請執行後端 Proxy 伺服器，進行實際的 API 呼叫。

### 密鑰管理最佳做法

- **環境變數**：從環境變數而非設定檔讀取金鑰。
- **Secret Manager**：在實際工作環境中，請將金鑰儲存在安全的密鑰儲存空間，例如 [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=zh-tw)。
- **帳單快訊**：在 Google Cloud 控制台中設定帳單快訊，當用量或費用暴增時，系統會通知您。

### 洩漏事件應對檢查清單

如果懷疑 API 金鑰外洩，請採取下列行動：

1. **產生新金鑰**：在 Google AI Studio 或 Cloud Platform Console 中建立替代金鑰。
2. **更新應用程式**：使用新金鑰部署程式碼。
3. **停用或刪除遭入侵的金鑰**：新金鑰通過驗證後，請在 Cloud Console 中停用遭洩漏的金鑰。請勿刪除舊金鑰，直到新金鑰完全啟用為止，以免應用程式停機。
4. **稽核使用情形**：在 Google Cloud 控制台中查看帳單記錄和 API 使用情形，找出未經授權的活動。

## 限制及保護金鑰

為 API 金鑰新增限制，可將金鑰遭盜用時造成的潛在損害降到最低。

### 套用要求來源限制

來源限制會規定哪些 IP 位址、網站或應用程式可以使用您的金鑰。

1. 前往 [Google Cloud 控制台的「憑證」頁面](https://console.cloud.google.com/apis/credentials?hl=zh-tw)。
2. 選取專案，然後按一下要限制的 API 金鑰名稱。
3. 在「應用程式限制」下方，選取「IP 位址」 (或適合您環境的限制類型)。
4. 指定允許的 IP 位址或範圍，然後按一下「儲存」。

### 保護未設限的標準 API 金鑰

如要繼續使用 Gemini API，請務必保護未設限的金鑰。

#### 方法 A：將金鑰限制在僅限 Gemini API (AI Studio)

如果金鑰只用於 Gemini API，請直接在 AI Studio 中保護金鑰：

1. 在 [Google AI Studio](https://aistudio.google.com/api-keys?hl=zh-tw) 的「API 金鑰」頁面中，找出標有「無限制」標籤的金鑰。
2. 將游標懸停在標籤上，然後按一下對話方塊中的「新增限制」。
3. 選取「僅限 Gemini API」。
4. 按一下「限制金鑰」確認操作。

#### 方法 B：限制其他服務的金鑰 (Google Cloud 控制台)

如果金鑰與其他 Google API 共用 (不建議)，請在 Cloud Console 中限制金鑰。**注意：套用這些限制後，使用這組金鑰的 Gemini API 要求將會失敗。**

1. 前往 [Google Cloud 控制台的「憑證」頁面](https://console.cloud.google.com/apis/credentials?hl=zh-tw)。
2. 選取專案和 API 金鑰。
3. 在「API restrictions」下方，使用「Select API restrictions」下拉式選單，選取要讓這個金鑰存取的 API。請勿選取「Generative Language API」。
4. 按一下 [儲存]。在 AI Studio 中建立獨立的受限金鑰，繼續使用 Gemini API。

### 封鎖閒置金鑰

2026 年 5 月 7 日起，Gemini API 會封鎖長期閒置的未設限 API 金鑰。這些金鑰在 AI Studio 中會顯示「已封鎖」標記。您必須產生新金鑰或使用現有的受限金鑰，才能繼續操作。

## 改用驗證金鑰

請按照下列步驟建立新的驗證型 API 金鑰，並更新應用程式：

1. 前往 [AI Studio API 金鑰頁面](https://aistudio.google.com/api-keys?hl=zh-tw)。
2. 檢查「金鑰類型」欄，找出列為「標準」的金鑰。
3. 按一下「建立 API 金鑰」，產生新的金鑰。在 AI Studio 中建立的所有新金鑰，都會自動建立為授權金鑰。
4. 複製新的驗證型 API 金鑰。
5. 更新應用程式程式碼、環境變數和任何部署設定，以使用新的驗證 API 金鑰。
6. 測試應用程式，確認新金鑰是否正常運作。
7. 驗證完成後，請刪除或撤銷舊的流量金鑰，以免遭到濫用。

## 限制

Google AI Studio 對專案和金鑰管理設有下列限制：

- 您一次最多可從 Google AI Studio 的「專案」頁面建立 10 個專案。
- 「API 金鑰」和「專案」頁面最多會顯示 100 個金鑰和 50 個專案。
- 系統只會顯示未設限的 API 金鑰，或是專門設限於 Generative Language API (Gemini API) 的 API 金鑰。

如要進行進階專案管理，或修改具有其他限制的鍵，請使用 [Google Cloud 控制台的「憑證」頁面](https://console.cloud.google.com/apis/credentials?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
