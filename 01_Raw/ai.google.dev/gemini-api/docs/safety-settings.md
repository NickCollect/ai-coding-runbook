---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-TW
fetched_at: 2026-10-19T05:51:48.639873+00:00
title: "\u5b89\u5168\u8a2d\u5b9a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 安全設定

您可以在原型設計階段調整 Gemini API 的安全設定，判斷應用程式是否需要更嚴謹或寬鬆的安全設定。您可以調整這些設定，限制或允許特定類型的內容。

本指南說明如何為互動設定安全設定、內容遭到封鎖時會發生什麼情況，以及可使用的類別和門檻。

## 設定安全性設定

建立互動時，請傳遞 `safety_settings` 清單。每項設定都會將有害內容類別 (`type`) 與封鎖門檻 (`threshold`) 配對。

以下範例會將仇恨言論 (`hate_speech`) 類別設為 `block_low_and_above`，封鎖任何可能屬於仇恨言論的內容：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Some potentially unsafe prompt.",
    safety_settings=[
        {
            "type": "hate_speech",
            "threshold": "block_low_and_above",
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Some potentially unsafe prompt.",
    safety_settings: [
      {
        type: "hate_speech",
        threshold: "block_low_and_above",
      },
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.HarmCategory;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.SafetySetting;
import com.google.genai.gaos.models.interactions.Threshold;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .type(HarmCategory.HATE_SPEECH)
        .threshold(Threshold.BLOCK_LOW_AND_ABOVE)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Some potentially unsafe prompt."))
        .safetySettings(List.of(hateSpeechSafety))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Some potentially unsafe prompt."),
            SafetySettings: []interactions.SafetySetting{
                {
                    Type:      interactions.HarmCategoryHateSpeech,
                    Threshold: interactions.ThresholdBlockLowAndAbove,
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Some potentially unsafe prompt.",
    "safety_settings": [
      {"type": "hate_speech", "threshold": "block_low_and_above"}
    ]
  }'
```

每個類別只能包含一項設定。未設定的類別會使用預設門檻，Gemini 2.5 和後續模型的預設門檻為「關閉」。

## 內容遭封鎖時

如果安全過濾器封鎖輸入內容或模型的回覆，互動就會失敗，並顯示 HTTP `400` 錯誤。但不會傳回遭封鎖的內容。

錯誤 `code` 會說明要求遭封鎖的原因：

- `safety`：輸入內容或回應遭到安全篩選器封鎖。
- `jailbreak`、`prohibited_content` 或 `blocklist`：輸入內容因該原因而遭封鎖。錯誤 `message` 開頭為 `Input blocked:`。

例如：

```
{
  "error": {
    "code": "safety",
    "message": "Request blocked due to safety violations (harmful content). Please modify your input and retry."
  }
}
```

如果是背景互動 (`background=true`)，互動的 `status` 會設為 `failed`，且相同的 `code` 和 `message` 會出現在 `errors` 清單中。串流時，錯誤會以 `error` 事件的形式傳送。

## 安全篩選機制

Gemini API 的可調整安全篩選器涵蓋下列類別：

| 類別 | 值 (API) | 說明 |
| --- | --- | --- |
| 騷擾 | `harassment` | 不當、威脅或意圖霸凌、折磨或嘲笑他人的內容。 |
| 仇恨言論 | `hate_speech` | 鼓吹暴力攻擊或煽動仇恨具有某些特質的個人或群體。 |
| 煽情露骨內容 | `sexually_explicit` | 含有情色露骨內容。 |
| 危險內容 | `dangerous_content` | 宣傳、鼓吹或助長危險活動的內容。 |
| 越獄 | `jailbreak` | 旨在規避安全篩選器的提示。 |

您可以運用這些篩選機制，根據使用情境將模型調整為適當的狀態。舉例來說，如果您正在製作電玩遊戲對白，可能為配合遊戲風格，而允許較多遭評為「危險」的內容。

除了可調整的安全篩選機制，Gemini API 也內建核心危害內容防護措施，例如危害兒童安全的內容。這類有害內容一律會遭到封鎖，無法調整。

## 封鎖門檻

由於模型本身具有安全性，因此額外篩選器預設為「關閉」。預設模型行為涵蓋大多數用途，因此只有在應用程式持續需要時，才應調整這些設定。

下表說明可為各類別設定的門檻。舉例來說，如果將「仇恨言論」設為「封鎖極少數內容」 (`block_only_high`)，系統會封鎖極可能是仇恨言論的內容，並允許機率較低的內容。

| 門檻 (Google AI Studio) | 門檻 (API) | 說明 |
| --- | --- | --- |
| 關閉 | `off` | 關閉安全篩選器 |
| 封鎖少數 | `block_only_high` | 封鎖不安全機率高的內容 |
| 封鎖一些 | `block_medium_and_above` | 封鎖有害機率中等以上的內容 |
| 封鎖多數 | `block_low_and_above` | 封鎖不安全機率低、中等、高的內容 |

### 機率與嚴重程度

Gemini API 會將內容屬於不安全類別的機率評估為高、中、低或微乎其微。系統會根據這個機率封鎖內容，而非根據危害的嚴重程度。有些內容可能不太會造成危害，但一旦發生，後果可能很嚴重。舉例來說，請比較下列句子：

1. 機器人打了我。
2. 機器人把我砍傷了。

第一句可能較不安全，但您可能認為第二句更嚴重。請仔細測試，找出適合您用途的封鎖層級，同時盡可能減少對使用者的傷害。

## 在 Google AI Studio 調整安全設定

在「執行設定」面板中，依序點選「進階設定」下方的「安全設定」，開啟「執行安全設定」模式。在模式中，您可以使用滑桿調整各安全類別的內容篩選等級：

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=zh-tw)

傳送要求 (例如向模型提問) 時，如果要求內容遭到封鎖，系統會顯示 warning「Content blocked」(內容遭到封鎖) 訊息。如要查看更多詳細資料，請將滑鼠游標懸停在「Content blocked」(內容已封鎖) 文字上，即可查看有害內容的類別和機率。

## 後續步驟

- 如要進一步瞭解完整 API，請參閱 [Interactions API 參考資料](https://ai.google.dev/api/interactions-api?hl=zh-tw)。
- 請參閱[安全指南](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-tw)，概略瞭解使用 LLM 開發時的安全考量。
- 如要進一步瞭解如何評估機率與嚴重程度，請參閱 [Jigsaw 團隊](https://developers.perspectiveapi.com/s/about-the-api-score)的說明。
- 進一步瞭解有助於安全解決方案的產品，例如 [Perspective API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-15 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-15 (世界標準時間)。"],[],[]]
