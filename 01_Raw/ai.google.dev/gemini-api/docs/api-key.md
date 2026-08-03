---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=th
fetched_at: 2026-08-03T04:40:58.960135+00:00
title: "\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e04\u0e35\u0e22\u0e4c Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การใช้คีย์ Gemini API

หากต้องการใช้ Gemini API คุณต้องตรวจสอบสิทธิ์คำขอ โดยสามารถตรวจสอบสิทธิ์ได้โดยใช้คีย์ API มาตรฐานหรือคีย์ API การให้สิทธิ์

[สร้างหรือดูคีย์ Gemini API](https://aistudio.google.com/apikey?hl=th)

## ประเภทคีย์ API: มาตรฐานเทียบกับการให้สิทธิ์

คีย์ API ให้สิทธิ์เข้าถึง Gemini API แต่ลักษณะด้านความปลอดภัยจะแตกต่างกัน Gemini API กำลังเปลี่ยนจากคีย์ API มาตรฐานเป็นคีย์การให้สิทธิ์เพื่อปรับปรุงความปลอดภัย

- **คีย์ API มาตรฐาน**: เชื่อมโยงคำขอกับโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google เพื่อวัตถุประสงค์ในการเรียกเก็บเงินและโควต้า คีย์มาตรฐานจะไม่ระบุผู้เรียก ซึ่งจำกัดความละเอียดของสิทธิ์และการควบคุมการเข้าถึงที่คีย์รองรับได้
- **คีย์การให้สิทธิ์ (Auth)**: ผูกกับบัญชีบริการ Google Cloud โดยตรง
  เมื่อใช้คีย์การให้สิทธิ์ ระบบจะประมวลผลคำขอภายใต้ข้อมูลประจำตัวของบัญชีบริการที่ผูกไว้ ซึ่งช่วยให้ควบคุมการเข้าถึงได้อย่างละเอียด โดยค่าเริ่มต้น คีย์การให้สิทธิ์จะจำกัดไว้สำหรับ Generative Language API (Gemini API) และมีการบังคับใช้คีย์ที่รั่วไหลอย่างรวดเร็ว ซึ่งจะหยุดการใช้งานคีย์ที่รั่วไหลซึ่งระบบตรวจพบได้อย่างรวดเร็ว

Gemini API จะเปลี่ยนจากคีย์มาตรฐานเป็นคีย์การตรวจสอบสิทธิ์เพื่อให้มั่นใจว่ามีการใช้งานที่ปลอดภัย

- **คีย์การให้สิทธิ์เป็นค่าเริ่มต้น**: คีย์ API ใหม่ทั้งหมดที่สร้างใน Google AI Studio
  จะสร้างเป็นคีย์การให้สิทธิ์โดยอัตโนมัติ
- **ระบบปฏิเสธคีย์ที่ไม่มีข้อจำกัด**: Gemini API จะปฏิเสธคำขอ
  จาก **คีย์มาตรฐานที่ไม่มีข้อจำกัด** คีย์ API มาตรฐานที่มีการใช้ข้อจำกัดที่ชัดเจนจะยังคงใช้งานได้ ข้อจำกัดนี้จะป้องกันการใช้คีย์ที่ไม่ได้รับอนุญาตซึ่งอาจมีการแชร์แบบสาธารณะหรือลิงก์กับบริการอื่นๆ
- **ในเดือนกันยายน 2026**: Gemini API จะปฏิเสธคำขอจาก **คีย์
  มาตรฐาน** คุณต้อง[ย้ายข้อมูลไปใช้คีย์การให้สิทธิ์](#migrate-to-auth-key)
  ก่อนวันที่นี้เพื่อหลีกเลี่ยงการหยุดชะงักของบริการ โปรดย้ายข้อมูลไปใช้คีย์การให้สิทธิ์ก่อนเดือนกันยายน 2026

## การจัดการคีย์ API ใน Google AI Studio

คุณจัดการโปรเจ็กต์และคีย์ได้โดยตรงใน [Google AI Studio](https://aistudio.google.com/apikey?hl=th)

### โปรเจ็กต์ Google Cloud

คีย์ Gemini API ทุกคีย์จะเชื่อมโยงกับ[โปรเจ็กต์ Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=th)
โปรเจ็กต์ Google Cloud จะจัดการการเรียกเก็บเงิน ผู้ทำงานร่วมกัน และสิทธิ์ Google AI Studio มีอินเทอร์เฟซแบบเบาเพื่อเข้าถึงโปรเจ็กต์เหล่านี้

- **โปรเจ็กต์เริ่มต้น**: หากคุณเป็นผู้ใช้ใหม่ Google AI Studio จะสร้างโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google และคีย์ API เริ่มต้นโดยอัตโนมัติหลังจากที่คุณยอมรับข้อกำหนดในการให้บริการ คุณเปลี่ยนชื่อโปรเจ็กต์นี้ได้โดยไปที่มุมมอง**โปรเจ็กต์** ในแดชบอร์ด
- **โปรเจ็กต์ที่มีอยู่**: หากคุณมีบัญชี Google Cloud อยู่แล้ว AI
  Studio จะไม่สร้างโปรเจ็กต์เริ่มต้น แต่คุณต้องนำเข้าโปรเจ็กต์ที่มีอยู่

### การนำเข้าโปรเจ็กต์

โดยค่าเริ่มต้น Google AI Studio จะไม่แสดงโปรเจ็กต์ Google Cloud ทั้งหมด คุณต้องนำเข้าโปรเจ็กต์ที่ต้องการใช้โดยทำดังนี้

1. ไปที่ [Google AI Studio](https://aistudio.google.com?hl=th)
2. เปิด**แดชบอร์ด** จากแผงด้านซ้าย แล้วเลือก**โปรเจ็กต์**
3. คลิกปุ่ม**นำเข้าโปรเจ็กต์**
4. ค้นหาและเลือกโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google ที่ต้องการนำเข้า แล้วคลิก**นำเข้า**
5. เมื่อนำเข้าแล้ว ให้ไปที่หน้า**คีย์ API** ในแดชบอร์ดเพื่อสร้างคีย์ในโปรเจ็กต์นั้น

### การแก้ปัญหาเกี่ยวกับสิทธิ์ในการสร้างคีย์

หากปุ่ม**สร้างคีย์ API** ไม่พร้อมใช้งานและแสดงข้อความ:
*"คุณไม่มีสิทธิ์สร้างคีย์ในโปรเจ็กต์นี้"* แสดงว่าคุณไม่มีสิทธิ์ IAM ที่
จำเป็น

โปรดขอให้ผู้ดูแลระบบโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google หรือผู้ดูแลระบบองค์กรกำหนดบทบาทที่มีสิทธิ์ต่อไปนี้ให้คุณ (เช่น ผู้แก้ไขโปรเจ็กต์)

- `resourcemanager.projects.get`: อนุญาตให้ AI Studio ยืนยันโปรเจ็กต์
- `apikeys.keys.create`: อนุญาตให้สร้างคีย์
- `serviceusage.services.enable`: ตรวจสอบว่าได้เปิดใช้ Generative Language API แล้ว
- `iam.serviceAccounts.create`: จำเป็นต้องใช้ในการสร้างบัญชีบริการที่ลิงก์
- `iam.serviceAccountApiKeyBindings.create`: ผูกบัญชีบริการกับคีย์ API

หากคุณไม่สามารถเข้าถึงระดับผู้ดูแลระบบได้ คุณสามารถสร้างโปรเจ็กต์ Google Cloud ใหม่ที่ไม่ได้เชื่อมโยงกับองค์กรเพื่อสร้างคีย์ได้

## การตั้งค่าสภาพแวดล้อม

เมื่อมีคีย์แล้ว ให้กำหนดค่าสภาพแวดล้อมเพื่อใช้คีย์อย่างปลอดภัยในแอปพลิเคชัน

### ตัวเลือกที่ 1: ใช้ตัวแปรสภาพแวดล้อม (แนะนำ)

ตั้งค่าตัวแปรสภาพแวดล้อม `GEMINI_API_KEY` หรือ `GOOGLE_API_KEY` ไลบรารีของไคลเอ็นต์ Gemini API จะตรวจหาและใช้ตัวแปรเหล่านี้โดยอัตโนมัติ หากตั้งค่าทั้ง 2 ตัวแปรไว้ `GOOGLE_API_KEY` จะมีความสำคัญเหนือกว่า

เลือกระบบปฏิบัติการเพื่อตั้งค่าตัวแปร

### Linux/macOS - Bash

ตรวจสอบว่าคุณมีไฟล์การกำหนดค่า Bash หรือไม่ โดยทำดังนี้

```
~/.bashrc
```

หากไม่มี ให้สร้างไฟล์และเปิดไฟล์โดยทำดังนี้

```
touch ~/.bashrc && open ~/.bashrc
```

เพิ่มคำสั่งส่งออกที่ส่วนท้ายของไฟล์โดยทำดังนี้

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

บันทึกไฟล์ แล้วใช้การเปลี่ยนแปลงโดยทำดังนี้

```
source ~/.bashrc
```

### macOS - Zsh

ตรวจสอบว่าคุณมีไฟล์การกำหนดค่า Zsh หรือไม่ โดยทำดังนี้

```
~/.zshrc
```

หากไม่มี ให้สร้างไฟล์และเปิดไฟล์โดยทำดังนี้

```
touch ~/.zshrc && open ~/.zshrc
```

เพิ่มคำสั่งส่งออกโดยทำดังนี้

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

บันทึกไฟล์ แล้วใช้การเปลี่ยนแปลงโดยทำดังนี้

```
source ~/.zshrc
```

### Windows

1. ค้นหา "ตัวแปรสภาพแวดล้อม" ในแถบค้นหาของ Windows
2. คลิก**ตัวแปรสภาพแวดล้อม** ในกล่องโต้ตอบคุณสมบัติของระบบ
3. ในส่วน**ตัวแปรผู้ใช้** หรือ**ตัวแปรระบบ** ให้คลิก**ใหม่...**
4. ตั้งชื่อตัวแปรเป็น `GEMINI_API_KEY` และตั้งค่าเป็นคีย์ API
5. คลิก**ตกลง** เพื่อบันทึก เปิดเซสชันเทอร์มินัลใหม่เพื่อโหลดตัวแปร

### ตัวเลือกที่ 2: ระบุคีย์ API อย่างชัดเจนในโค้ด

คุณส่งคีย์ API อย่างชัดเจนได้เมื่อเริ่มต้นไคลเอ็นต์ ให้ทำเช่นนี้เฉพาะในกรณีที่คุณใช้ตัวแปรสภาพแวดล้อมไม่ได้

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

## การรักษาความปลอดภัยและการจัดการข้อมูลลับ

ปฏิบัติต่อคีย์ Gemini API เหมือนรหัสผ่าน หากคีย์ถูกละเมิด ผู้อื่นจะใช้โควต้าของโปรเจ็กต์ เรียกเก็บเงินที่ไม่คาดคิด และเข้าถึงทรัพยากรส่วนตัวได้

### กฎความปลอดภัยที่สำคัญ

- **เก็บคีย์ไว้เป็นความลับ**: อย่าตรวจสอบคีย์ API ในระบบควบคุมแหล่งที่มา
  เช่น Git
- **อย่าเปิดเผยคีย์ฝั่งไคลเอ็นต์ในสภาพแวดล้อมจริง**: อย่าฮาร์ดโค้ดคีย์ API
  โดยตรงในเว็บหรือแอปบนอุปกรณ์เคลื่อนที่ ผู้ใช้สามารถแยกคีย์ที่คอมไพล์ในโค้ดฝั่งไคลเอ็นต์ได้ หากต้องการรักษาความปลอดภัยแอปฝั่งไคลเอ็นต์ ให้เรียกใช้พร็อกซีเซิร์ฟเวอร์แบ็กเอนด์เพื่อเรียก API จริง

### แนวทางปฏิบัติแนะนำสำหรับการจัดการข้อมูลลับ

- **ตัวแปรสภาพแวดล้อม**: อ่านคีย์จากตัวแปรสภาพแวดล้อมแทนที่จะอ่านจาก
  ไฟล์การกำหนดค่า
- **Secret Manager**: สำหรับสภาพแวดล้อมจริง ให้จัดเก็บคีย์ไว้ในที่เก็บข้อมูลลับที่ปลอดภัย
  เช่น [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=th)
- **การแจ้งเตือนการเรียกเก็บเงิน**: ตั้งค่าการแจ้งเตือนการเรียกเก็บเงินใน Google Cloud Console เพื่อ
  แจ้งให้คุณทราบหากมีการใช้งานหรือค่าใช้จ่ายเพิ่มขึ้นอย่างรวดเร็ว

### เช็กลิสต์การตอบสนองต่อการรั่วไหล

หากสงสัยว่าคีย์ API รั่วไหล ให้ทำดังนี้

1. **สร้างคีย์ใหม่**: สร้างคีย์ทดแทนใน Google AI Studio หรือ
   Cloud Console
2. **อัปเดตแอปพลิเคชัน**: นำโค้ดไปใช้โดยใช้คีย์ใหม่
3. **ปิดใช้หรือลบคีย์ที่ถูกละเมิด**: ปิดใช้คีย์ที่รั่วไหลใน
   Cloud Console เมื่อยืนยันคีย์ใหม่แล้ว อย่าลบคีย์เก่าจนกว่าคีย์ใหม่จะทำงานอย่างเต็มรูปแบบเพื่อหลีกเลี่ยงการหยุดทำงานของแอปพลิเคชัน
4. **ตรวจสอบการใช้งาน**: ตรวจสอบบันทึกการเรียกเก็บเงินและการใช้งาน API ใน Google Cloud
   Console เพื่อระบุกิจกรรมที่ไม่ได้รับอนุญาต

## การจำกัดและการรักษาความปลอดภัยคีย์

การเพิ่มข้อจำกัดให้แก่คีย์ API จะช่วยลดความเสียหายที่อาจเกิดขึ้นหากคีย์ถูกละเมิด

### ใช้ข้อจำกัดเกี่ยวกับแหล่งที่มาของคำขอ

ข้อจำกัดเกี่ยวกับแหล่งที่มาจะจำกัดที่อยู่ IP, เว็บไซต์ หรือแอปพลิเคชันที่ใช้คีย์ได้

1. ไปที่หน้า[ข้อมูลเข้าสู่ระบบคอนโซล Google Cloud](https://console.cloud.google.com/apis/credentials?hl=th)
2. เลือกโปรเจ็กต์ แล้วคลิกชื่อคีย์ API ที่ต้องการจำกัด
3. ในส่วน**ข้อจำกัดแอปพลิเคชัน** ให้เลือก**ที่อยู่ IP** (หรือ
   ประเภทข้อจำกัดที่เหมาะสมกับสภาพแวดล้อมของคุณ)
4. ระบุที่อยู่ IP หรือช่วงที่อนุญาต แล้วคลิก**บันทึก**

### การรักษาความปลอดภัยคีย์ API มาตรฐานที่ไม่มีข้อจำกัด

หากต้องการใช้ Gemini API ต่อไป คุณต้องรักษาความปลอดภัยคีย์ที่ไม่มีข้อจำกัด

#### วิธีที่ 1: จำกัดคีย์ไว้สำหรับ Gemini API เท่านั้น (AI Studio)

หากใช้คีย์สำหรับ Gemini API เท่านั้น ให้รักษาความปลอดภัยคีย์โดยตรงใน AI Studio โดยทำดังนี้

1. ในหน้า**คีย์ API** ใน[Google AI Studio](https://aistudio.google.com/api-keys?hl=th) ให้ค้นหาคีย์ที่มีป้ายกำกับ
   **ไม่มีข้อจำกัด**
2. วางเมาส์เหนือป้ายกำกับ แล้วคลิก**เพิ่มข้อจำกัด** ในกล่องโต้ตอบ
3. เลือก**จำกัดไว้สำหรับ Gemini API เท่านั้น**
4. คลิก**จำกัดคีย์** เพื่อยืนยัน

#### วิธีที่ 2: จำกัดคีย์สำหรับบริการอื่นๆ (คอนโซล Google Cloud)

หากมีการแชร์คีย์กับ Google API อื่นๆ (ไม่แนะนำ) ให้จำกัดคีย์ใน Cloud Console **หมายเหตุ: คำขอ Gemini API ที่ใช้คีย์นี้จะล้มเหลวหลังจากใช้ข้อจำกัดเหล่านี้**

1. ไปที่หน้าข้อมูลเข้าสู่ระบบ [คอนโซล Google Cloud](https://console.cloud.google.com/apis/credentials?hl=th)
2. เลือกโปรเจ็กต์และคีย์ API
3. ในส่วน**ข้อจำกัด API** ให้ใช้เมนูแบบเลื่อนลง**เลือกข้อจำกัด API** เพื่อ
   เลือก API ที่ต้องการให้คีย์นี้เข้าถึง อย่าเลือก **Generative Language API**
4. คลิก**บันทึก** สร้างคีย์ที่แยกต่างหากและมีข้อจำกัดใน AI Studio เพื่อใช้ Gemini API ต่อไป

### คีย์ที่ไม่ได้ใช้งานซึ่งถูกบล็อก

ตั้งแต่วันที่ 7 พฤษภาคม 2026 เป็นต้นไป Gemini API จะบล็อกคีย์ API ที่ไม่มีข้อจำกัดซึ่งไม่ได้ใช้งานเป็นระยะเวลานาน คีย์เหล่านี้จะแสดงแท็ก**ถูกบล็อก** ใน AI Studio คุณต้องสร้างคีย์ใหม่หรือใช้คีย์ที่มีข้อจำกัดที่มีอยู่เพื่อดำเนินการต่อ

## ย้ายข้อมูลไปใช้คีย์การให้สิทธิ์

ทำตามขั้นตอนต่อไปนี้เพื่อสร้างคีย์ API การให้สิทธิ์ใหม่และอัปเดตแอปพลิเคชัน

1. ไปที่หน้าคีย์ API ของ [AI Studio](https://aistudio.google.com/api-keys?hl=th)
2. ตรวจสอบคอลัมน์**ประเภทคีย์** เพื่อระบุคีย์ที่แสดงเป็น**มาตรฐาน**
3. คลิก**สร้างคีย์ API** เพื่อสร้างคีย์ใหม่ คีย์ใหม่ทั้งหมดที่สร้างใน AI Studio จะสร้างเป็นคีย์การให้สิทธิ์โดยอัตโนมัติ
4. คัดลอกคีย์ API การให้สิทธิ์ใหม่
5. อัปเดตโค้ดของแอปพลิเคชัน ตัวแปรสภาพแวดล้อม และการกำหนดค่าการติดตั้งใช้งานทั้งหมดให้ใช้คีย์ API การตรวจสอบสิทธิ์ใหม่
6. ทดสอบแอปพลิเคชันเพื่อยืนยันว่าแอปพลิเคชันทำงานได้อย่างถูกต้องด้วยคีย์ใหม่
7. เมื่อยืนยันแล้ว ให้ลบหรือเพิกถอนคีย์การรับส่งข้อมูลเก่าเพื่อป้องกันการใช้งานในทางที่ผิด

## ข้อจำกัด

Google AI Studio มีข้อจำกัดต่อไปนี้ในการจัดการโปรเจ็กต์และคีย์

- คุณสร้างโปรเจ็กต์ได้สูงสุดครั้งละ 10 โปรเจ็กต์จากหน้า**โปรเจ็กต์** ของ Google AI Studio
- หน้า**คีย์ API** และ**โปรเจ็กต์** จะแสดงคีย์ได้สูงสุด 100 คีย์และโปรเจ็กต์ได้สูงสุด 50 โปรเจ็กต์
- ระบบจะแสดงเฉพาะคีย์ API ที่ไม่มีข้อจำกัดหรือจำกัดไว้สำหรับ Generative Language API (Gemini API) โดยเฉพาะ

หากต้องการจัดการโปรเจ็กต์ขั้นสูงหรือแก้ไขคีย์ที่มีข้อจำกัดอื่นๆ ให้ใช้
[หน้าข้อมูลเข้าสู่ระบบคอนโซล Google Cloud](https://console.cloud.google.com/apis/credentials?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
