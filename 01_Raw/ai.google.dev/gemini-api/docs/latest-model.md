---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=th
fetched_at: 2026-09-28T06:25:31.981264+00:00
title: "\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e43\u0e2b\u0e21\u0e48\u0e43\u0e19 Gemini 3.8 Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# มีอะไรใหม่ใน Gemini 3.8 Flash

[ดูรุ่นทั้งหมด](https://ai.google.dev/gemini-api/docs/models?hl=th)

Gemini 3.8 Flash (`gemini-3.8-flash`) พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) และพร้อมใช้งานจริงแล้ว โมเดล Flash นี้เป็นโมเดลที่ชาญฉลาดที่สุดของเรา ซึ่งออกแบบมาเพื่อวิศวกรรมซอฟต์แวร์ในระยะยาว เอเจนต์อัตโนมัติ และเวิร์กโฟลว์ที่ซับซ้อนขององค์กร

คู่มือนี้จะอธิบายสิ่งใหม่ๆ ใน Gemini 3.8 Flash, การเปลี่ยนแปลง API, ตัวอย่างโค้ด และคำแนะนำในการย้ายข้อมูล

## โมเดลใหม่

| รุ่น | รหัสโมเดล | ระดับการคิดเริ่มต้น | ราคา | คำอธิบาย |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash พร้อมให้บริการจนถึงสิ้นปีในราคาช่วงแนะนำที่ $0.75/โทเค็นอินพุต 1 ล้านโทเค็น และ $3.75/โทเค็นเอาต์พุต 1 ล้านโทเค็น ดูรายละเอียดเพิ่มเติมได้ที่[ราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th) | โมเดล Flash ที่ชาญฉลาดที่สุดของเรา ซึ่งออกแบบมาเพื่อวิศวกรรมซอฟต์แวร์ในระยะยาว เอเจนต์อัตโนมัติ และเวิร์กโฟลว์ที่ซับซ้อนขององค์กร |

Gemini 3.8 Flash รองรับหน้าต่างบริบทขนาด 1 ล้านโทเค็น, โทเค็นเอาต์พุตสูงสุด 64, 000 โทเค็น, ระดับการคิดที่ปรับได้ (`low`, `medium`, `high`) และชุดเครื่องมือในตัวที่ครอบคลุมเหมือนเดิม

ดูรายละเอียดทั้งหมดได้ที่[หน้าโมเดล Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=th) ดูรายละเอียดราคาช่วงแนะนำได้ที่[ส่วนราคา](#pricing)ด้านล่างหรือ[หน้าราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3.8-flash)

## คู่มือเริ่มใช้งานฉบับย่อ

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a three.js script that renders a realistic 3D black hole."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Write a three.js script that renders a realistic 3D black hole."))
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
            Input: interactions.NewInteractionsInput("Write a three.js script that renders a realistic 3D black hole."),
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a three.js script that renders a realistic 3D black hole."
  }'
```

## มีอะไรใหม่ใน Gemini 3.8 Flash

- **วิศวกรรมซอฟต์แวร์ระยะยาว:** ให้ผลลัพธ์ที่ยอดเยี่ยมในเกณฑ์มาตรฐานการเขียนโค้ดในโลกแห่งความเป็นจริง การรีแฟคเตอร์แบบหลายไฟล์ที่ซับซ้อน และการดำเนินการเครื่องมือแบบดีเทอร์มินิสติก ดูรายละเอียดได้ที่[ระเบียบวิธีวิจัยการประเมิน](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=th)
- **Agent ที่ทำงานได้ด้วยตนเอง:** ช่วยให้คุณสร้างเวิร์กโฟลว์การวางแผนแบบหลายขั้นตอนและการจัดการเครื่องมือที่ยืดหยุ่น ซึ่งจะช่วยลดลูปและข้อผิดพลาดที่ล้มเหลวได้อย่างมาก
- **เวิร์กโฟลว์ที่ซับซ้อนขององค์กร:** ให้ความแม่นยำที่เหนือกว่า การให้เหตุผลเชิงลึก และความเข้มงวดด้านข้อเท็จจริงสูงในงานโดเมนที่ซับซ้อนและไปป์ไลน์ข้อมูลขนาดใหญ่
- **โมเดลเริ่มต้นสำหรับ Agent ที่ได้รับการจัดการ:** Agent เริ่มต้นสำหรับ Agent ที่ได้รับการจัดการ ซึ่งก็คือ [Agent ของ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th) จะใช้ Gemini 3.8 Flash [Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=th) ยังใช้ Gemini 3.8 Flash โดยค่าเริ่มต้นด้วย
- **ราคาช่วงแนะนำ:** Gemini 3.8 Flash พร้อมให้บริการในราคาช่วงแนะนำที่ $0.75/โทเค็นอินพุต 1 ล้านโทเค็น และ $3.75/โทเค็นเอาต์พุต 1 ล้านโทเค็นจนถึงวันที่ 31 ธันวาคม 2026 ราคามาตรฐานที่ $1.50/โทเค็นอินพุต 1 ล้านโทเค็นและ $7.50/โทเค็นเอาต์พุต 1 ล้านโทเค็นจะมีผลในวันที่ 1 มกราคม 2027

Gemini 3.8 Flash สามารถใช้โทเค็นมากขึ้นในงานที่ซับซ้อนและใช้เวลานานขึ้นได้ตามที่ออกแบบไว้ โมเดลจะใช้ขั้นตอนการให้เหตุผลที่สั้นลง เรียกใช้เครื่องมือซ้ำๆ และตรวจสอบงานระหว่างทางเพื่อให้ได้ผลลัพธ์ที่มีคุณภาพสูงขึ้นสำหรับเป้าหมายที่ซับซ้อนและมีหลายขั้นตอน เวิร์กโฟลว์บางอย่างไม่จำเป็นต้องมีการยืนยันในระดับนี้ สำหรับงานประจำวัน คุณสามารถลดความพยายามในการ[ให้เหตุผล](#understanding-reasoning-levels)เพื่อลดการใช้โทเค็นได้ หรือคุณจะใช้ Gemini 3.7 Flash ต่อไปก็ได้

## ทำความเข้าใจระดับการให้เหตุผล

Gemini 3.8 Flash ช่วยให้คุณควบคุมเวลาในการตอบสนองและความชาญฉลาดได้อย่างยืดหยุ่นด้วยการปรับระดับการคิดของโมเดล ดังนี้

- **การประมวลผลความคิดน้อย**: ลดเวลาในการตอบสำหรับงานที่สำคัญต่อเวลาในการตอบสนอง เช่น ไปป์ไลน์การตอบสนองต่อเหตุการณ์ แชทแบบเรียลไทม์ การเขียนฉบับร่าง และการวิเคราะห์ข้อมูลอย่างรวดเร็ว
- **ปานกลาง (ค่าเริ่มต้น):** คุณภาพดีที่สุดสำหรับงานส่วนใหญ่ แนะนำสำหรับโค้ดที่ซับซ้อนและกรณีการใช้งานแบบเอเจนต์ ซึ่งให้ความแม่นยำในการผ่านครั้งแรกสูงกว่า
- **ใช้ความคิดอย่างหนัก**: เพิ่มความสามารถในการให้เหตุผลและการประสานงานเครื่องมือของโมเดลให้สูงสุด ดีที่สุดสำหรับการให้เหตุผลอย่างลึกซึ้ง คณิตศาสตร์ และงานหลายขั้นตอนที่ซับซ้อน

ตัวอย่างต่อไปนี้จะตั้งค่า `thinking_level` เป็น `medium` สำหรับคำขอวิเคราะห์โค้ดที่ซับซ้อน

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium"
  }
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.MEDIUM) // Balanced reasoning effort for complex tasks
                .build())
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
            Input: interactions.NewInteractionsInput("Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelMedium.ToPointer(), // Balanced reasoning effort for complex tasks
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## อัปเดต Agent ของ Antigravity

เนื่องจากประสิทธิภาพและการให้เหตุผลที่ดียิ่งขึ้น ตอนนี้เราจึงสร้าง[เอเจนต์ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th) ใน Gemini Managed Agents ด้วย Gemini 3.8 Flash โดยค่าเริ่มต้น

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("antigravity-preview-09-2026"))
        .input(
            InteractionsInput.of(
                "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
                    + "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
                    + "Check search indexing with Google Search for site:web.dev. "
                    + "Format the output as a side-by-side scorecard table with prioritized fixes."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput(
                "Audit https://web.dev for performance, Core Web Vitals, and SEO. " +
                    "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. " +
                    "Check search indexing with Google Search for site:web.dev. " +
                    "Format the output as a side-by-side scorecard table with prioritized fixes.",
            ),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote"
}'
```

[กำหนดค่า](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#model-selection)โมเดล Gemini พื้นฐานได้โดยใช้ `agent_config`

## รายการตรวจสอบการย้ายข้อมูล

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### ย้ายข้อมูลไปยัง gemini-3.8-flash

- **อัปเดตรหัสโมเดล:** เปลี่ยนสตริงโมเดลเป้าหมายเป็น `gemini-3.8-flash`
- **นำพารามิเตอร์การสุ่มตัวอย่างที่เลิกใช้งานแล้วออก**
  - ลบ `temperature`, `top_p` และ `top_k` ออกจากไฟล์กำหนดค่าการสร้าง
  - แทนที่ `thinking_budget` ด้วยสตริง enum `thinking_level` โปรดทราบว่า `minimal` ไม่รองรับใน Flash 3.8
  - นำ `candidate_count` ออก (ไม่รองรับใน Gemini 3 ขึ้นไป)
- **บังคับใช้กฎการตรวจสอบการเลี้ยว:**
  - สร้างมาตรฐานการสนทนาไปมาแบบหลายรอบในฝั่งเซิร์ฟเวอร์ `previous_interaction_id`
  - นำการตอบกลับของโมเดลที่กรอกข้อมูลไว้ล่วงหน้าออก
- **การตรวจสอบการเรียกใช้ฟังก์ชัน:**
  - วางชิ้นงานมัลติโมดอลไว้ในเพย์โหลดการตอบกลับ
  - จัดรูปแบบวิธีการในบรรทัดโดยใช้ `\n\n`
  - หากเห็น`Malformed_Function_Call`ข้อผิดพลาดที่เชื่อมโยงกับข้อความก่อนเครื่องมือ โปรดดู[วิธีแก้ปัญหาข้อกำหนดของข้อความก่อนเครื่องมือ](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#workarounds-for-pre-tool-text-requirements)
  - เฉพาะในกรณีที่ใช้ GenerateContent API: ตรวจสอบว่าออบเจ็กต์ `FunctionResponse` ทั้งหมดมี `call_id` และ `name`
- **ข้อกำหนดพื้นฐานของ Gemini 3:** ดูการอัปเดต SDK และการรักษาลายเซ็นความคิดได้ที่[รายการตรวจสอบการย้ายข้อมูล Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=th#migration)

## ราคา

ใช้ประโยชน์จากราคาช่วงแนะนำใน Google AI Studio และแพลตฟอร์ม Agent ของ Gemini Enterprise จนถึงวันที่ 31 ธันวาคม 2026 สำหรับ Gemini 3.8 Flash, Gemini 3.7 Flash และ Gemini 3.6 Flash ราคามาตรฐานจะมีผลในวันที่ 1 มกราคม 2027 ดูระดับราคาทั้งหมดได้ที่[หน้าราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3.8-flash)

## ขั้นตอนถัดไป

- ดูข้อกำหนดของ API ได้ใน[ภาพรวมของโมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)
- สํารวจการประสานงานแบบหลายเอเจนต์ใน[ภาพรวมของ Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)
- ทดสอบและปรับแต่งพรอมต์ใน [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
