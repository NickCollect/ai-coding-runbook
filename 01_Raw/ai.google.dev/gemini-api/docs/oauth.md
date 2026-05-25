---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=ko
fetched_at: 2026-05-25T05:19:42.209364+00:00
title: "OAuth\ub97c \ud1b5\ud55c \uc778\uc99d \ube60\ub978 \uc2dc\uc791 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# OAuth를 통한 인증 빠른 시작

[Gemini API에 인증하는 가장 쉬운 방법은 Gemini API 빠른 시작에 설명된 대로 API 키를 구성하는 것입니다.](https://ai.google.dev/gemini-api/docs/quickstart?hl=ko) 더 엄격한 액세스 제어가 필요한 경우 OAuth를 대신 사용할 수 있습니다. 이 가이드는 OAuth를 사용하여 인증을 설정하는 데 도움이 됩니다.

이 가이드에서는 테스트 환경에 적합한 간소화된 인증 접근 방식을 사용합니다. [[프로덕션 환경의 경우 앱에 적합한 액세스 사용자 인증 정보를 선택하기 전에 인증 및 승인에 대해 알아보세요.](https://developers.google.com/workspace/guides/auth-overview?hl=ko)](https://developers.google.com/workspace/guides/create-credentials?hl=ko#choose_the_access_credential_that_is_right_for_you)

## 목표

- OAuth용 클라우드 프로젝트 설정
- 애플리케이션 기본 사용자 인증 정보 설정
- `gcloud auth`를 사용하는 대신 프로그램에서 사용자 인증 정보 관리

## 기본 요건

이 빠른 시작을 실행하려면 다음이 필요합니다.

- [Google Cloud 프로젝트](https://developers.google.com/workspace/guides/create-project?hl=ko)
- [gcloud CLI의 로컬 설치](https://cloud.google.com/sdk/docs/install?hl=ko)

## 클라우드 프로젝트 설정

이 빠른 시작을 완료하려면 먼저 Cloud 프로젝트를 설정해야 합니다.

### 1. API 사용 설정

Google API를 사용하려면 먼저 Google Cloud 프로젝트에서 API를 사용 설정해야 합니다.

- Google Cloud 콘솔에서 Google Generative Language API를 사용 설정합니다.

  [API 사용 설정](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=ko)

### 2. OAuth 동의 화면 구성

다음으로 프로젝트의 OAuth 동의 화면을 구성하고 자신을 테스트 사용자로 추가합니다. Cloud 프로젝트에서 이 단계를 이미 완료했다면 다음 섹션으로 건너뛰세요.

1. Google Cloud 콘솔에서 **메뉴** > **Google 인증 플랫폼** > **개요** 로 이동합니다.

   [Google 인증 플랫폼으로 이동](https://console.developers.google.com/auth/overview?hl=ko)
2. 프로젝트 구성 양식을 작성하고 **잠재고객** 섹션에서 사용자 유형을 **외부** 로 설정합니다.
3. 양식의 나머지 부분을 작성하고 사용자 데이터 정책 약관에 동의한 후 **만들기** 를 클릭합니다.
4. 지금은 범위를 추가하지 않아도 되며 **저장하고 계속하기** 를 클릭합니다. 나중에 Google Workspace 조직 외부에서 사용할 앱을 만들 때는 앱에 필요한 승인 범위를 추가하고 확인해야 합니다.
5. 테스트 사용자 추가:

   1. Google 인증 플랫폼의
      [잠재고객 페이지](https://console.developers.google.com/auth/audience?hl=ko)로 이동합니다.
   2. ****\*\*테스트 사용자\*\* 에서 \*\*사용자 추가\*\* 를 클릭합니다.****
   3. 이메일 주소와 기타 승인된 테스트 사용자를 입력한 후 **저장** 을 클릭합니다.

### 3. 데스크톱 애플리케이션의 사용자 인증 정보 승인

최종 사용자로 인증하고 앱에서 사용자 데이터에 액세스하려면 OAuth 2.0 클라이언트 ID를 하나 이상 만들어야 합니다. 클라이언트 ID는 Google OAuth 서버에서 단일 앱을 식별하는 데 사용됩니다. 앱이 여러 플랫폼에서 실행되는 경우 각 플랫폼에 대해 별도의 클라이언트 ID를 만들어야 합니다.

1. Google Cloud 콘솔에서 **메뉴** > **Google 인증 플랫폼** > **클라이언트** 로 이동합니다.

   [사용자 인증 정보로 이동](https://console.developers.google.com/auth/clients?hl=ko)
2. **클라이언트 만들기** 를 클릭합니다.
3. **애플리케이션 유형** > **데스크톱 앱** 을 클릭합니다.
4. **이름** 필드에 사용자 인증 정보의 이름을 입력합니다. 이 이름은 Google Cloud 콘솔에만 표시됩니다.
5. **만들기** 를 클릭합니다. OAuth 클라이언트 생성됨 화면이 표시되고 여기에 새 클라이언트 ID와 클라이언트 보안 비밀번호가 표시됩니다.
6. **확인** 을 클릭합니다. 새로 만든 사용자 인증 정보가 **OAuth 2.0 클라이언트 ID** 아래에 표시됩니다.
7. 다운로드 버튼을 클릭하여 JSON 파일을 저장합니다. 파일은
   `client_secret_<identifier>.json`으로 저장되며 이름을 `client_secret.json`
   으로 바꾸고 작업 디렉터리로 이동합니다.

## 애플리케이션 기본 사용자 인증 정보 설정

`client_secret.json` 파일을 사용 가능한 사용자 인증 정보로 변환하려면 해당 위치를 `gcloud auth application-default login` 명령어의 `--client-id-file` 인수에 전달합니다.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

이 가이드의 간소화된 프로젝트 설정은 **"Google에서
이 앱을 확인하지 않았습니다."** 대화상자를 트리거합니다. 이는 정상적인 현상이므로 **"계속"**을 선택합니다.

이렇게 하면 결과 토큰이 잘 알려진 위치에 배치되므로 `gcloud` 또는 클라이언트 라이브러리에서 액세스할 수 있습니다.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

애플리케이션 기본 사용자 인증 정보 (ADC)를 설정하면 대부분의 언어에서 클라이언트 라이브러리가 이를 찾는 데 최소한의 도움만 필요합니다.

### Curl

이 기능이 작동하는지 테스트하는 가장 빠른 방법은 curl을 사용하여 REST API에 액세스하는 것입니다.

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

Python에서 클라이언트 라이브러리는 자동으로 이를 찾아야 합니다.

```
pip install google-genai
```

테스트를 위한 최소 스크립트는 다음과 같습니다.

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## 다음 단계

작동하는 경우 텍스트 데이터에서
[시맨틱 검색을 시도할 수 있습니다](https://ai.google.dev/docs/semantic_retriever?hl=ko).

## 사용자 인증 정보 직접 관리 [Python]

대부분의 경우 클라이언트 ID (`client_secret.json`)에서 액세스 토큰을 만드는 데 사용할 수 있는 `gcloud` 명령어가 없습니다. Google은 앱 내에서 이 프로세스를 관리할 수 있도록 여러 언어로 라이브러리를 제공합니다. 이 섹션에서는 Python에서 이 프로세스를 보여줍니다. 다른 언어의 경우 이와 유사한 절차의 예가
[Drive API 문서](https://developers.google.com/drive/api/quickstart/python?hl=ko)에 나와 있습니다.

### 1. 필요한 라이브러리 설치

Python용 Google 클라이언트 라이브러리와 Gemini 클라이언트 라이브러리를 설치합니다.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. 사용자 인증 정보 관리자 작성

승인 화면을 클릭해야 하는 횟수를 최소화하려면 작업 디렉터리에 `load_creds.py`라는 파일을 만들어 나중에 재사용하거나 만료된 경우 새로고침할 수 있는 `token.json` 파일을 캐시합니다.

다음 코드를 사용하여 `client_secret.json` 파일을 `genai.configure`에서 사용할 수 있는 토큰으로 변환합니다.

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

### 3. 프로그램 작성

이제 `script.py`를 만듭니다.

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. 프로그램 실행

작업 디렉터리에서 다음 샘플을 실행합니다.

```
python script.py
```

스크립트를 처음 실행하면 브라우저 창이 열리고 액세스 권한을 부여하라는 메시지가 표시됩니다.

1. 아직 Google 계정에 로그인하지 않았으면 로그인하라는 메시지가 표시됩니다. 여러 계정에 로그인되어 있는 경우 **프로젝트를 구성할 때 '테스트 계정'으로 설정한 계정을 선택해야 합니다.**
2. 승인 정보가 파일 시스템에 저장되므로 다음에 샘플 코드를 실행할 때는 승인하라는 메시지가 표시되지 않습니다.

인증을 설정했습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
