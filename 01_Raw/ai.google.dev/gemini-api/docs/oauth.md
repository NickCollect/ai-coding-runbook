---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=zh-TW
fetched_at: 2026-05-05T13:25:51.963832+00:00
title: "\u900f\u904e OAuth \u9032\u884c\u9a57\u8b49\u7684\u5feb\u901f\u5165\u9580\u5c0e\u89bd\u8ab2\u7a0b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

- [首頁](https://ai.google.dev/gemini-api/docs/首頁)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [文件](https://ai.google.dev/gemini-api/docs/文件)

提供意見

# 透過 OAuth 進行驗證的快速入門導覽課程

如要向 Gemini API 驗證，最簡單的方法是設定 API 金鑰，詳情請參閱 [Gemini API 快速入門導覽課程](https://ai.google.dev/gemini-api/docs/Gemini API 快速入門導覽課程)。如需更嚴格的存取控制，請改用 OAuth。本指南將協助您設定 OAuth 驗證。

本指南會使用簡化的驗證方法，適用於測試環境。在正式環境中，建議您先瞭解[驗證和授權](https://ai.google.dev/gemini-api/docs/驗證和授權)，再[選擇適合應用程式的存取憑證](https://ai.google.dev/gemini-api/docs/選擇適合應用程式的存取憑證)。

## 目標

- 設定 OAuth 的雲端專案
- 設定應用程式預設憑證
- 在程式中管理憑證，而非使用 `gcloud auth`

## 必要條件

如要執行這項快速入門導覽課程，您需要：

- [Google Cloud 專案](https://ai.google.dev/gemini-api/docs/Google Cloud 專案)
- [在本機安裝 gcloud CLI](https://ai.google.dev/gemini-api/docs/在本機安裝 gcloud CLI)

## 設定雲端專案

如要完成本快速入門導覽課程，請先設定雲端專案。

### 1. 啟用 API

使用 Google API 前，請先在 Google Cloud 專案中啟用 API。

- 在 Google Cloud 控制台中啟用 Google Generative Language API。

  [啟用 API](https://ai.google.dev/gemini-api/docs/啟用 API)

### 2. 設定 OAuth 同意畫面

接著設定專案的 OAuth 同意畫面，並將自己新增為測試使用者。如果已為 Cloud 專案完成這個步驟，請跳至下一節。

1. 在 Google Cloud 控制台中，依序前往「選單」 >「Google Auth platform」 >「總覽」。

   [前往 Google Auth 平台](https://ai.google.dev/gemini-api/docs/前往 Google Auth 平台)
2. 填寫專案設定表單，並在「目標對象」部分將使用者類型設為「外部」。
3. 填寫表單的其餘部分，接受使用者資料政策條款，然後按一下「建立」。
4. 目前可以略過新增範圍，然後按一下「儲存並繼續」。日後為 Google Workspace 機構以外的使用者建立應用程式時，您必須新增並驗證應用程式所需的授權範圍。
5. 新增測試使用者：

   1. 前往 Google Auth Platform 的[目標對象頁面](https://ai.google.dev/gemini-api/docs/目標對象頁面)。
   2. 在「測試使用者」下方，按一下「新增使用者」。
   3. 輸入您的電子郵件地址和任何其他授權測試使用者，然後按一下「儲存」。

### 3. 授權電腦應用程式的憑證

如要以使用者身分驗證，並存取應用程式中的使用者資料，您需要建立一或多個 OAuth 2.0 用戶端 ID。Google 的 OAuth 伺服器會使用用戶端 ID 來識別個別應用程式。如果您的應用程式在多個平台上執行，則必須為每個平台分別建立用戶端 ID。

1. 在 Google Cloud 控制台中，依序前往「選單」 >「Google Auth platform」(Google 驗證平台) >「Clients」(用戶端)。

   [前往「憑證」](https://ai.google.dev/gemini-api/docs/前往「憑證」)
2. 按一下「Create Client」(建立用戶端)。
3. 依序點選「Application type」(應用程式類型) >「Desktop app」(電腦版應用程式)。
4. 在「Name」(名稱) 欄位中，輸入憑證名稱。這個名稱只會顯示在 Google Cloud 控制台中。
5. 按一下「建立」，系統會顯示「已建立 OAuth 用戶端」畫面，其中包含新的用戶端 ID 和用戶端密鑰。
6. 按一下「確定」。新建立的憑證會顯示在「OAuth 2.0 用戶端 ID」 下方。
7. 按一下下載按鈕儲存 JSON 檔案。並儲存為 `client_secret_<identifier>.json`，然後重新命名為 `client_secret.json`，並移至工作目錄。

## 設定應用程式預設憑證

如要將 `client_secret.json` 檔案轉換為可用的憑證，請將檔案位置傳遞至 `gcloud auth application-default login` 指令的 `--client-id-file` 引數。

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

本教學課程中簡化的專案設定會觸發「Google 尚未驗證這個應用程式」對話方塊。這是正常現象，請選擇「繼續」。

這會將產生的權杖放在已知位置，以便 `gcloud` 或用戶端程式庫存取。

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

設定應用程式預設憑證 (ADC) 後，大多數語言的用戶端程式庫幾乎不需要任何協助，就能找到這些憑證。

### Curl

如要快速測試這項功能是否正常運作，請使用 curl 存取 REST API：

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

在 Python 中，用戶端程式庫應會自動找到這些憑證：

```
pip install google-genai
```

測試這項功能的最簡單指令碼可能如下：

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## 後續步驟

如果運作正常，即可開始嘗試[對文字資料進行語意擷取](https://ai.google.dev/gemini-api/docs/對文字資料進行語意擷取)。

## 自行管理憑證 [Python]

在許多情況下，您無法使用 `gcloud` 指令從用戶端 ID (`client_secret.json`) 建立存取權杖。Google 提供多種語言的程式庫，讓您在應用程式中管理該程序。本節將以 Python 示範該程序。如需其他語言的這類程序範例，請參閱 [Drive API 說明文件](https://ai.google.dev/gemini-api/docs/Drive API 說明文件)。

### 1. 安裝所需的程式庫

安裝 Python 專用的 Google 用戶端程式庫和 Gemini 用戶端程式庫。

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. 撰寫憑證管理工具

如要盡量減少授權畫面點選次數，請在工作目錄中建立名為 `load_creds.py` 的檔案，以快取 `token.json` 檔案供日後重複使用，或在檔案過期時重新整理。

請先使用下列程式碼，將 `client_secret.json` 檔案轉換為可搭配 `genai.configure` 使用的權杖：

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

### 3. 編寫程式

現在建立 `script.py`：

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. 執行程式

在工作目錄中執行範例：

```
python script.py
```

首次執行指令碼時，系統會開啟瀏覽器視窗，並提示您授權存取權。

1. 如果尚未登入 Google 帳戶，系統會提示你登入。如果您登入了多個帳戶，請務必**選取設定專案時設為「測試帳戶」的帳戶。**
2. 授權資訊會儲存在檔案系統中，因此下次執行程式碼範例時，系統不會提示您授權。

您已成功設定驗證。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://ai.google.dev/gemini-api/docs/創用 CC 姓名標示 4.0 授權)，程式碼範例則為[阿帕契 2.0 授權](https://ai.google.dev/gemini-api/docs/阿帕契 2.0 授權)。詳情請參閱《[Google Developers 網站政策](https://ai.google.dev/gemini-api/docs/Google Developers 網站政策)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？
