---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=th
fetched_at: 2026-06-15T06:30:26.212969+00:00
title: "\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e4c\u0e14\u0e49\u0e27\u0e22\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 OAuth \u0e2d\u0e22\u0e48\u0e32\u0e07\u0e23\u0e27\u0e14\u0e40\u0e23\u0e47\u0e27 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การตรวจสอบสิทธิ์ด้วยการเริ่มต้นใช้งาน OAuth อย่างรวดเร็ว

วิธีที่ง่ายที่สุดในการตรวจสอบสิทธิ์ Gemini API คือการกำหนดค่าคีย์ API ตามที่อธิบายไว้ใน[การเริ่มต้นใช้งาน Gemini API อย่างรวดเร็ว](https://ai.google.dev/gemini-api/docs/quickstart?hl=th) หากต้องการการควบคุมการเข้าถึงที่เข้มงวดมากขึ้น คุณสามารถใช้ OAuth แทนได้ คู่มือนี้จะช่วยคุณตั้งค่าการตรวจสอบสิทธิ์ด้วย OAuth

คู่มือนี้ใช้วิธีการตรวจสอบสิทธิ์แบบง่ายที่เหมาะ
สำหรับสภาพแวดล้อมการทดสอบ สำหรับสภาพแวดล้อมการใช้งานจริง โปรดดูข้อมูลเกี่ยวกับ[การตรวจสอบสิทธิ์และการให้สิทธิ์](https://developers.google.com/workspace/guides/auth-overview?hl=th)
ก่อน
[เลือกข้อมูลเข้าสู่ระบบเพื่อเข้าถึง](https://developers.google.com/workspace/guides/create-credentials?hl=th#choose_the_access_credential_that_is_right_for_you)
ที่เหมาะสมกับแอปของคุณ

## วัตถุประสงค์

- ตั้งค่าโปรเจ็กต์ที่อยู่ในระบบคลาวด์สำหรับ OAuth
- ตั้งค่าข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน
- จัดการข้อมูลเข้าสู่ระบบในโปรแกรมแทนการใช้ `gcloud auth`

## ข้อกำหนดเบื้องต้น

คุณต้องมีสิ่งต่อไปนี้จึงจะเรียกใช้การเริ่มต้นอย่างรวดเร็วนี้ได้

- [โปรเจ็กต์ Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=th)
- [การติดตั้ง gcloud CLI ในเครื่อง](https://cloud.google.com/sdk/docs/install?hl=th)

## ตั้งค่าโปรเจ็กต์ที่อยู่ในระบบคลาวด์

หากต้องการทําคู่มือเริ่มใช้งานฉบับย่อนี้ให้เสร็จสมบูรณ์ คุณต้องตั้งค่าโปรเจ็กต์ที่อยู่ในระบบคลาวด์ก่อน

### 1. เปิดใช้ API

ก่อนใช้ Google API คุณต้องเปิดใช้ API ในโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google

- เปิดใช้ Google Generative Language API ในคอนโซล Google Cloud

  [เปิดใช้ API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=th)

### 2. กำหนดค่าหน้าจอขอความยินยอม OAuth

จากนั้นกำหนดค่าหน้าจอขอความยินยอม OAuth ของโปรเจ็กต์และเพิ่มตัวคุณเองเป็นผู้ใช้ทดสอบ
หากคุณดำเนินการขั้นตอนนี้สำหรับโปรเจ็กต์ที่อยู่ในระบบคลาวด์เสร็จแล้ว ให้ข้ามไปยัง
ส่วนถัดไป

1. ในคอนโซล Google Cloud ให้ไปที่**เมนู** >
   **แพลตฟอร์มการตรวจสอบสิทธิ์ของ Google** > **ภาพรวม**

   [ไปที่แพลตฟอร์ม Google Auth](https://console.developers.google.com/auth/overview?hl=th)
2. กรอกแบบฟอร์มการกำหนดค่าโปรเจ็กต์และตั้งค่าประเภทผู้ใช้เป็น**ภายนอก**
   ในส่วน**กลุ่มเป้าหมาย**
3. กรอกข้อมูลในแบบฟอร์มส่วนที่เหลือ ยอมรับข้อกำหนดของนโยบายข้อมูลผู้ใช้ แล้วคลิก**สร้าง**
4. ตอนนี้คุณสามารถข้ามการเพิ่มขอบเขต แล้วคลิก**บันทึกและดำเนินการต่อ** ในอนาคต เมื่อสร้างแอปเพื่อใช้ภายนอกองค์กร Google Workspace คุณต้องเพิ่มและยืนยันขอบเขตการให้สิทธิ์ที่แอปของคุณต้องการ
5. เพิ่มผู้ใช้ทดสอบ

   1. ไปที่[หน้ากลุ่มเป้าหมาย](https://console.developers.google.com/auth/audience?hl=th)ของ
      แพลตฟอร์ม Google Auth
   2. ในส่วน**ผู้ใช้ทดสอบ** ให้คลิก**เพิ่มผู้ใช้**
   3. ป้อนอีเมลและผู้ใช้ทดสอบที่ได้รับอนุญาตอื่นๆ แล้วคลิก**บันทึก**

### 3. ให้สิทธิ์ข้อมูลเข้าสู่ระบบสำหรับแอปพลิเคชันบนเดสก์ท็อป

หากต้องการตรวจสอบสิทธิ์ในฐานะผู้ใช้ปลายทางและเข้าถึงข้อมูลผู้ใช้ในแอป คุณต้องสร้างรหัสไคลเอ็นต์ OAuth 2.0 อย่างน้อย 1 รายการ รหัสไคลเอ็นต์ใช้เพื่อระบุ
แอปเดี่ยวไปยังเซิร์ฟเวอร์ OAuth ของ Google หากแอปทำงานบนหลายแพลตฟอร์ม
คุณต้องสร้างรหัสไคลเอ็นต์แยกต่างหากสำหรับแต่ละแพลตฟอร์ม

1. ในคอนโซล Google Cloud ให้ไปที่**เมนู** > **แพลตฟอร์มการตรวจสอบสิทธิ์ของ Google** >
   **ไคลเอ็นต์**

   [ไปที่ข้อมูลเข้าสู่ระบบ](https://console.developers.google.com/auth/clients?hl=th)
2. คลิก**สร้างไคลเอ็นต์**
3. คลิก**ประเภทแอปพลิเคชัน** > **แอปเดสก์ท็อป**
4. ในช่อง**ชื่อ** ให้พิมพ์ชื่อของข้อมูลเข้าสู่ระบบ ชื่อนี้จะแสดงในคอนโซล Google Cloud เท่านั้น
5. คลิก**สร้าง** หน้าจอไคลเอ็นต์ OAuth ที่สร้างขึ้นจะปรากฏขึ้น โดยแสดงรหัสไคลเอ็นต์และรหัสลับไคลเอ็นต์ใหม่
6. คลิก**ตกลง** ข้อมูลเข้าสู่ระบบที่สร้างขึ้นใหม่จะปรากฏในส่วน**รหัสไคลเอ็นต์ OAuth 2.0**
7. คลิกปุ่มดาวน์โหลดเพื่อบันทึกไฟล์ JSON ระบบจะบันทึกเป็น
   `client_secret_<identifier>.json` แล้วเปลี่ยนชื่อเป็น `client_secret.json`
   และย้ายไปยังไดเรกทอรีการทำงาน

## ตั้งค่าข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน

หากต้องการแปลงไฟล์ `client_secret.json` เป็นข้อมูลเข้าสู่ระบบที่ใช้ได้ ให้ส่งตำแหน่งของไฟล์ไปยังอาร์กิวเมนต์ `--client-id-file` ของคำสั่ง `gcloud auth application-default login`

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

การตั้งค่าโปรเจ็กต์แบบง่ายในบทแนะนำนี้จะทริกเกอร์กล่องโต้ตอบ **"Google ยังไม่ได้
ยืนยันแอปนี้"** ซึ่งเป็นเรื่องปกติ ให้เลือก**"ดำเนินการต่อ"**

ซึ่งจะวางโทเค็นที่ได้ไว้ในตำแหน่งที่รู้จักกันดีเพื่อให้เข้าถึงได้
โดย `gcloud` หรือไลบรารีของไคลเอ็นต์

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

เมื่อตั้งค่าข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน (ADC) แล้ว ไลบรารีของไคลเอ็นต์ในภาษาต่างๆ ส่วนใหญ่จะต้องการความช่วยเหลือเพียงเล็กน้อยหรือไม่ต้องการเลยในการค้นหา

### Curl

วิธีที่เร็วที่สุดในการทดสอบว่าการตั้งค่านี้ใช้งานได้คือการใช้เพื่อเข้าถึง REST
API โดยใช้ curl ดังนี้

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

ใน Python ไลบรารีของไคลเอ็นต์ควรค้นหาโดยอัตโนมัติ

```
pip install google-genai
```

สคริปต์ขั้นต่ำในการทดสอบอาจเป็นดังนี้

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## ขั้นตอนถัดไป

หากใช้งานได้ แสดงว่าคุณพร้อมที่จะลอง[การดึงข้อมูลเชิงความหมายในข้อมูลข้อความ](https://ai.google.dev/docs/semantic_retriever?hl=th)แล้ว

## จัดการข้อมูลเข้าสู่ระบบด้วยตนเอง [Python]

ในหลายกรณี คุณจะไม่มีคำสั่ง `gcloud` เพื่อสร้างโทเค็นการเข้าถึงจากรหัสไคลเอ็นต์ (`client_secret.json`) Google มีไลบรารีในหลายภาษาเพื่อให้คุณจัดการกระบวนการดังกล่าวภายในแอปได้ ส่วนนี้จะแสดงกระบวนการใน Python ตัวอย่างที่เทียบเท่าของขั้นตอนประเภทนี้สำหรับภาษาอื่นๆ มีอยู่ใน[เอกสารประกอบของ Drive API](https://developers.google.com/drive/api/quickstart/python?hl=th)

### 1. ติดตั้งไลบรารีที่จำเป็น

ติดตั้งไลบรารีของไคลเอ็นต์ Google สำหรับ Python และไลบรารีของไคลเอ็นต์ Gemini

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. เขียนเครื่องมือจัดการข้อมูลเข้าสู่ระบบ

หากต้องการลดจำนวนครั้งที่คุณต้องคลิกผ่านหน้าจอการให้สิทธิ์
ให้สร้างไฟล์ชื่อ `load_creds.py` ในไดเรกทอรีการทำงานเพื่อ
แคชไฟล์ `token.json` ที่สามารถนำกลับมาใช้ใหม่ได้ในภายหลัง หรือรีเฟรชหากไฟล์หมดอายุ

เริ่มต้นด้วยโค้ดต่อไปนี้เพื่อแปลงไฟล์ `client_secret.json` เป็นโทเค็นที่ใช้กับ `genai.configure` ได้

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. เขียนโปรแกรม

ตอนนี้มาสร้าง`script.py`กัน

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. เรียกใช้โปรแกรม

ในไดเรกทอรีการทำงาน ให้เรียกใช้ตัวอย่างโดยทำดังนี้

```
python script.py
```

เมื่อเรียกใช้สคริปต์เป็นครั้งแรก สคริปต์จะเปิดหน้าต่างเบราว์เซอร์และแจ้งให้คุณ
ให้สิทธิ์เข้าถึง

1. หากยังไม่ได้ลงชื่อเข้าใช้บัญชี Google คุณจะได้รับข้อความแจ้งให้
   ลงชื่อเข้าใช้ หากลงชื่อเข้าใช้ไว้หลายบัญชี **โปรดเลือกบัญชีที่คุณตั้งค่าเป็น "บัญชีทดสอบ" เมื่อกำหนดค่าโปรเจ็กต์**
2. ระบบจะจัดเก็บข้อมูลการให้สิทธิ์ไว้ในระบบไฟล์ ดังนั้นในครั้งถัดไปที่คุณ
   เรียกใช้โค้ดตัวอย่าง ระบบจะไม่แจ้งให้คุณขอรับการให้สิทธิ์

คุณตั้งค่าการตรวจสอบสิทธิ์เรียบร้อยแล้ว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
