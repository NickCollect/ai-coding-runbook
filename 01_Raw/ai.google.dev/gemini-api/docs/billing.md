---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=ko
fetched_at: 2026-05-05T20:48:02.599386+00:00
title: "\uacb0\uc81c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 결제

이 가이드에서는 다양한 Gemini API 결제 옵션을 간략히 설명하고, 결제를 사용 설정하고 사용량을 모니터링하는 방법을 설명하며, 결제에 관해 자주 묻는 질문 (FAQ)에 대한 답변을 제공합니다.

## 결제 및 등급 정보

Gemini API 결제는 결제 내역을 기준으로 합니다.

| 사용 등급 | 검증 | [결제 등급 한도](#spend-caps) |
| --- | --- | --- |
| **무료** | [활성 프로젝트](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#google-cloud-projects) 또는 무료 체험판 | 해당 사항 없음 |
| **Tier 1** | [활성 결제 계정 설정 및 연결](#setup-billing) | $250 |
| **Tier 2** | $100 지급 + 첫 번째 결제 완료 후 3일 | 2,000달러 |
| **Tier 3** | $1,000 결제 + 첫 번째 결제 완료 후 30일 | $20,000~$100,000 이상 |

신규 계정은 무료 등급으로 시작하며, 이 등급에서는 Gemini API 및 AI Studio의 [특정 모델](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)에 액세스할 수 있습니다(모델의 무료 등급 [요금 한도](https://aistudio.google.com/rate-limit?hl=ko)까지).

**더 높은 비율 제한에 액세스하고, 고급 모델을 사용하고, 프롬프트와 대답이 Google 제품을 개선하는 데 사용되지 않도록 하려면\* [결제 계정을 연결](#setup-billing)하고 [선불](#prepay)로 유료 등급으로 전환하세요.**
그런 다음 누적 비용 및 계정 연령에 따라 상위 등급으로 이동합니다. 3등급에서는 [후불](#postpay) 결제로 전환할 수 있습니다.

등급, 비율 한도, 결제 계정 한도는 모두 [결제 계정](#cloud-billing) 수준에서 결정됩니다.

\* *엔터프라이즈급 데이터 개인 정보 보호: 유료 서비스의 데이터 사용에 관한 자세한 내용은 [서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko#data-use-paid)을 참고하세요.*

## 결제를 설정하여 유료 등급 이용하기

[Google AI Studio](https://aistudio.google.com/projects?hl=ko)에서 프로젝트를 만들고 결제를 설정하거나 기존 프로젝트를 가져와 유료 등급으로 업그레이드할 수 있습니다.
무료 등급에서 유료 등급으로 업그레이드하려면 결제 계정을 연결하고 [선불 결제](#prepay)하여 계정에 최소 10달러 (또는 다른 통화로 이에 상응하는 금액)의 크레딧을 추가해야 합니다.

1. AI Studio [API 키](https://aistudio.google.com/api-keys?hl=ko) 페이지, [프로젝트](https://aistudio.google.com/projects?hl=ko) 페이지 또는 AI Studio에서 **결제 설정** 버튼이 표시되는 곳으로 이동합니다.
   - 신규 사용자는 기본적으로 [프로젝트 및 API 키](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#google-cloud-projects)가 생성됩니다.
   - 새 키가 필요한 경우 [**API 키 만들기**](https://aistudio.google.com/api-keys?hl=ko)를 클릭하고 대화상자에 따라 키-프로젝트 쌍을 표에 추가합니다.
2. 유료 등급으로 업그레이드할 무료 등급 프로젝트를 찾아 *결제 등급* 열에서 **결제 설정**을 클릭합니다.
3. Google 결제 계정을 이전에 설정한 적이 없는 경우 다음 단계를 따르세요.
   - 서비스 약관에 동의하려면 국가를 선택하라는 메시지가 표시됩니다.
   - 그런 다음 연락처 정보와 결제 수단을 입력하거나 확인하여 계속 진행합니다.
4. 이전에 Google 결제 계정을 설정한 경우 다음 단계를 따르세요.
   - 기존 결제 계정 중에서 선택하라는 메시지가 표시됩니다.
   - 기존 계정을 사용하지 않으려면 **새 결제 계정 추가**를 클릭하고 연락처 정보와 결제 수단을 입력하거나 확인한 후 계속합니다.
5. 다음으로 다음 중 하나가 표시됩니다.
   - 결제 설정을 완료하기 위해 최소 10달러를 선불로 지불하라는 메시지가 표시된 경우 (계정이 [선불](#prepay) 결제 요금제에 자동으로 할당됨)
   - 계정의 [선불](#prepay) 및 [후불](#postpay) 요금제 중에서 선택할 수 있습니다.
   - 새 선불 시스템이 모든 사용자에게 전파될 때까지 (2026년 3월 23일부터) 중간 기간 동안 [후불](#postpay) 결제 요금제에 할당됩니다.
6. 선불을 선택하거나 후불을 선택하면 계정 설정이 완료됩니다.

### 다음 유료 등급으로 업그레이드

이미 유료 등급을 사용 중이며 요금제 변경 [기준](#about-billing)을 충족하는 경우 다음 등급으로 자동 업그레이드됩니다([처리 시간](#processing-times)에 따라 다름).

## 결제 상태 확인

프로젝트에 [결제 계정을 연결](#setup-billing)한 후 [AI Studio 결제 페이지](https://aistudio.google.com/billing?hl=ko)에서 상태를 모니터링할 수 있습니다. 무료 등급과 달리 유료 등급 상태는 동적입니다. 사용 등급은 계정 기록에 따라 결정되지만, [선불](#prepay) 크레딧 잔액이 있어야 Gemini API에서 요청을 처리합니다.

[프로젝트](https://aistudio.google.com/projects?hl=ko) 페이지의 *결제 등급* 열에서 프로젝트의 등급과 요금제를 확인할 수 있습니다. 프로젝트에 대해 취해야 할 수 있는 결제 상태 작업은 *결제 등급* 또는 *상태* 열에 표시됩니다.

- 프로젝트에 연결된 결제 계정이 없는 경우 '***결제 설정***'
- 프로젝트에 연결된 결제 계정이 있지만 설정해야 하는 [선불](#prepay) 결제 요금제를 사용해야 하는 경우 '***선불 설정***'
- 결제 계정에서 크레딧을 구매해야 하지만 선불 결제 계정이 설정되지 않았거나 사용 가능한 크레딧 잔액이 소진된 경우 '***사용 가능한 크레딧 없음***'

메시지를 클릭하여 필요한 조치를 진행합니다.

## 사용량 모니터링

[Google AI Studio](https://aistudio.google.com/usage?hl=ko)의 **대시보드** > **사용량**에서 Gemini API 사용량을 모니터링할 수 있습니다.

## 요금제

Gemini API 및 AI Studio의 요금제는 사용량에 대한 결제 시점을 결정하는 두 가지 카테고리(선불 및 후불)로 나뉩니다. [AI Studio 결제](https://aistudio.google.com/billing?hl=ko) 페이지에서 할당된 요금제를 확인하고 결제 수단을 관리할 수 있습니다.

### 선불

선불 요금제에서는 Gemini API 사용 전에 선불 잔액에 사용할 크레딧을 구매하며, API 사용 비용은 [거의 실시간](#processing-times)으로 선불 크레딧 잔액에서 차감됩니다.
계정에 [크레딧을 추가](#buy-credits)하거나 [자동 충전](#auto-reload)을 설정하여 선불로 결제할 수 있습니다. 크레딧을 구매한 후 미사용 크레딧은 12개월 후에 만료되며 [후불 계정으로 전환](#postpay)한 후를 제외하고 [환불되지 않습니다](#refunds).

결제 계정의 선불 크레딧 잔액이 0이 되면 해당 결제 계정에 연결된 모든 프로젝트의 모든 API 키가 동시에 작동 중지됩니다.
선불 크레딧은 Gemini API 사용 비용에만 적용되며 다른 Google Cloud 서비스 비용을 지불하는 데 사용할 수 없습니다.

신규 사용자는 선불 요금제가 기본값으로 설정됩니다. 선불 및 후불 요금제 도입 이전에 생성된 프로젝트는 Gemini API를 계속 사용하려면 [프로젝트의 결제 세부정보를 업데이트](#verify-billing)해야 할 수 있습니다.

*[인보이스 (또는 오프라인)](https://docs.cloud.google.com/billing/docs/concepts?hl=ko#billing_account_types) 계정에는 선불을 사용할 수 없습니다.*

#### 크레딧 구매

Gemini API를 사용하기 전에 크레딧을 수동으로 구매하여 선불 계정 크레딧 잔액에 충전할 수 있습니다.

크레딧을 구매하려면 [AI Studio 결제](https://aistudio.google.com/billing?hl=ko) 페이지로 이동하여 **크레딧 구매**를 선택하세요.
최소 구매 금액은 10달러입니다. 선불로 결제할 수 있는 최대 크레딧 금액은 5,000달러입니다.

#### 자동 새로고침

자동 충전은 잔액이 부족할 때 선불 크레딧 잔액을 자동으로 충전하는 선택적 기능입니다. 이는 서비스 중단을 방지하는 데 유용합니다.

[AI Studio 결제](https://aistudio.google.com/billing?hl=ko) 페이지의 *사용 가능한 크레딧* 카드에서 자동 충전 설정을 구성하고 자동 충전 상태를 확인할 수 있습니다. **자동 충전 설정** 또는 **자동 충전 관리**를 클릭하여 결제 수단, 충전 금액, 충전 결제를 트리거하는 최소 잔액을 설정합니다.

### 후불

후불 결제 요금제에서는 Cloud Billing 계정에 비용이 발생하며, 월말에 또는 계정 등급에 따라 [자동으로 할당된 지출 한도](#tier-spend-caps)에 비용이 도달하면 자동으로 비용이 청구됩니다.
결제 금액은 [AI Studio 결제](https://aistudio.google.com/billing?hl=ko) 페이지에서 관리할 수 있는 후불 결제 계정에 연결된 결제 수단으로 청구됩니다.

[3단계 기준](#about-billing)을 충족하면 선불 요금제에서 후불 요금제로 수동으로 전환할 수 있습니다. 요금제를 변경하려면 계정이 자격 요건을 충족할 때 [AI Studio 결제](https://aistudio.google.com/billing?hl=ko) 페이지의 오른쪽 상단에 표시되는 **후불로 전환** 버튼을 클릭해야 합니다.

그런 다음 **결제** 페이지에서 잔액, 기한, 이전 결제를 확인하고 결제를 진행하며 결제 수단을 관리할 수 있습니다.

새 프로젝트의 [결제를 설정](#setup-billing)할 때 후불 요금제를 사용할 수 있는 경우 [결제 설정](#setup-billing) 대화상자에서 선불 요금제와 후불 요금제 중에서 선택할 수 있습니다.

Cloud Billing 계정을 전환하여 후불 요금제를 사용하면 해당 결제 계정에 연결된 모든 프로젝트가 후불 요금제로 전환됩니다. 해당 결제 계정을 선불 요금제로 다시 이동할 수 없습니다. 프로젝트를 다른 결제 요금제의 결제 계정으로 이동하여 해당 프로젝트의 청구 주기를 변경할 수 있습니다. [프로젝트 결제 관리](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ko)에 관한 Cloud 문서를 참고하세요.

후불 요금제 청구 주기에 대한 자세한 내용은 [Cloud Billing 가이드](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ko)를 참고하세요.

## 비용 한도

Gemini API는 결제 계정 등급 및 프로젝트 수준 모두에서 월별 지출 한도를 지원합니다. 이러한 컨트롤은 계정에서 예상치 못한 초과 사용이 발생하지 않도록 보호하고 서비스 가용성을 보장하기 위해 생태계를 보호하도록 설계되었습니다.

*[인보이스 (또는 오프라인)](https://docs.cloud.google.com/billing/docs/concepts?hl=ko#billing_account_types) 계정에는 지출 한도를 사용할 수 없습니다.*

### 프로젝트 지출 한도

AI Studio에서 자체 [프로젝트 수준](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#google-cloud-projects) 지출 한도를 설정할 수 있습니다.
동일한 결제 계정에 여러 프로젝트가 있고 각 프로젝트가 누적 지출 한도에 충분히 액세스할 수 있도록 하려는 경우에 유용합니다.

프로젝트 편집자, 소유자 또는 관리자 [역할](https://docs.cloud.google.com/iam/docs/roles-overview?hl=ko)이 있는 계정은 AI Studio의 [지출](https://aistudio.google.com/spend?hl=ko) 페이지에서 **월별 지출 한도** > **지출 한도 수정**을 통해 프로젝트별 지출 한도를 설정할 수 있습니다.

[프로젝트를 다른 결제 계정으로 이동](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ko#change_the_billing_account_for_a_project)하면 해당 프로젝트에 이미 설정된 지출 한도가 유지되지만 누적된 지출은 새 결제 주기에 $0로 재설정됩니다.

[일괄 모드](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko) 완료에는 초과 사용량이 발생할 수 있습니다.

AI Studio에서 청구 데이터 처리 시간이 최대 10분 정도 약간 지연될 수 있습니다. 추가 요금이 발생하기 전에 결제 데이터가 처리되지 않으면 프로젝트 한도를 초과하는 요금이 발생할 수 있습니다.

### 결제 계정 등급 지출 한도

각 [등급](#about-billing)에는 최대 월별 지출 한도가 있습니다.

| 사용 등급 | 비용 한도 |
| --- | --- |
| **무료** | 해당 사항 없음 |
| **Tier 1** | $250 |
| **Tier 2** | 2,000달러 |
| **Tier 3** | $20,000~$100,000 |

Gemini API의 월별 사용량 한도는 [결제 계정](#cloud-billing) 수준에서 적용됩니다. 기본 한도는 사전 설정되어 있지만 사용량이 많은 경우 [상향 조정을 요청](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=ko)할 수 있습니다. 총 지출은 Gemini API 서비스가 사용 설정된 연결된 모든 프로젝트에서 집계됩니다. 누적 계정 합계가 등급 한도에 도달하면 다음 결제 주기 (매월 1일)가 시작될 때까지 해당 결제 계정에 연결된 모든 프로젝트의 서비스가 일시중지됩니다.

#### 결제 계정 지출 평가하기

새 [결제 계정 등급 지출 한도](#tier-spend-caps)가 진행 중인 프로젝트에 영향을 미치는지 확인하기 위해 이전 월별 지출을 평가하려면 다음 단계를 따르세요.

1. Google Cloud 콘솔에서 [Cloud Billing 계정 보고서](https://console.cloud.google.com/billing/reports?hl=ko) 페이지를 확인합니다.
   - 결제 계정이 두 개 이상인 경우 프롬프트에서 비용 보고서를 보려는 Cloud Billing 계정을 선택합니다.
2. 보고서는 기본적으로 '당월'의 '서비스별 그룹화'로 설정됩니다. 표의 **서비스** 열에 **Gemini API**가 표시되고 **사용 비용** 열에 총 지출이 표시됩니다.
3. Gemini API 사용량으로 제한된 상세 비용을 확인하려면 **그룹화 기준** 필터를 **SKU**로, **서비스** 필터를 **Gemini API**로 설정합니다.
4. **사용일별 기간** 필터를 원하는 범위로 조정하여 특정 기간의 이전 지출을 평가합니다.

## 처리 시간

청구 신호와 업데이트가 항상 실시간으로 이루어지는 것은 아닙니다.

- **크레딧 사용량**: 사용 비용은 일반적으로 몇 분 이내에 잔액에서 차감됩니다.
- **결제 확인**: 대부분의 카드 결제는 즉시 이루어지지만 일부 결제 수단 (예: 은행 송금)은 승인되는 데 며칠이 걸릴 수 있습니다. 크레딧 구매가 공식적으로 확인된 후에만 서비스가 재개되거나 업그레이드됩니다.
- **등급 업그레이드**: 결제가 완료되거나 [업그레이드 기준](#about-billing)을 충족하면 일반적으로 10분 이내에 등급 업그레이드가 반영됩니다.
- **총비용 분석 그래프**: [결제](https://aistudio.google.com/billing?hl=ko) 페이지와 [지출](https://aistudio.google.com/spend?hl=ko) 페이지에 총비용 분석을 표시하는 그래프는 업데이트되는 데 최대 24시간이 걸릴 수 있습니다.

[청구 주기](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ko#delayed-billing) 및 [거래](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=ko#missing-transactions) 지연 시간에 관한 Cloud Billing 가이드를 읽고 청구 지연 가능성에 대해 자세히 알아보세요.

## 환불

계정 유형을 전환하는 경우를 제외하고 **선불** 결제 계정은 환불이 허용되지 않습니다.

**선불 계정이 후불 계정 유형으로 전환되는 경우** ([기준](#about-billing)을 충족하고 계정을 [직접 업그레이드](#postpay)한 후) 선불 계정이 폐쇄되고 남아 있는 선불 크레딧은 등록된 결제 수단으로 자동 환불됩니다.

후불로 업그레이드하는 경우를 제외한 어떤 이유로든 선불 계정을 [폐쇄](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=ko#close-a-billing-account)하면 남은 선불 크레딧이 소멸됩니다.

구매한 크레딧은 1년 후에 만료됩니다. 만료된 크레딧은 소멸되며 복구할 수 없습니다.

**후불** 계정에는 [Google Cloud 환불 정책](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=ko#request_a_refund)이 적용됩니다.

## Cloud Billing 계정

Gemini API는 결제 서비스에 [Cloud Billing 계정](https://cloud.google.com/billing/docs/concepts?hl=ko)을 사용하며, 이 계정은 [AI Studio에서 직접 설정](#setup-billing)할 수 있습니다.
AI Studio를 사용하여 지출을 추적하고, 비용을 파악하고, 결제할 수 있습니다.

등급, 비율 한도, 결제 계정 한도는 모두 결제 계정 수준에서 결정됩니다.

### 프로젝트 및 API 키

Cloud Billing 계정에 연결된 모든 [프로젝트](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#google-cloud-projects)는 결제 계정의 사용량 등급과 연결된 요금 한도 및 계정 한도를 상속합니다. 한 결제 계정에서 다른 결제 계정으로 [프로젝트를 변경](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ko#change_the_billing_account_for_a_project)하면 프로젝트의 등급이 새 결제 계정의 등급으로 전환되고 이에 따라 비율 한도와 계정 한도도 전환됩니다.

결제 계정에 연결된 모든 프로젝트의 누적 지출 (모든 Google Cloud 제품에 대한) 및 계정 기간은 해당 결제 계정의 [등급 자격 요건](#about-billing)에 포함됩니다.

결제 계정에서 [프로젝트를 연결 해제](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ko#disable_billing_for_a_project)하여 무료 등급으로 돌아갈 수 있습니다.

[API 키](https://ai.google.dev/gemini-api/docs/api-key?hl=ko)는 프로젝트 내에서 생성된 사용자 인증 정보입니다.
독립적인 결제 설정이 없으며 프로젝트의 등급 한도와 결제 상태를 상속합니다. 프로젝트 내 모든 키의 누적 사용량은 해당 프로젝트의 지출 한도와 결제 계정의 총 지출에 포함됩니다.

## 자주 묻는 질문(FAQ)

다음 섹션에서는 자주 묻는 질문(FAQ)에 대한 답변을 제공합니다.

### 무엇에 대해 비용이 청구되나요?

Gemini API 가격은 다음을 기준으로 합니다.

- 입력 토큰 수
- 출력 토큰 수
- 캐시된 토큰 수
- 캐시된 토큰 스토리지 기간

가격 정보는 [가격 책정 페이지](https://ai.google.dev/pricing?hl=ko)를 참고하세요.

### 할당량은 어디에서 확인할 수 있나요?

[AI Studio](https://aistudio.google.com/usage?hl=ko)에서 할당량과 시스템 한도를 확인할 수 있습니다.

### 더 높은 비율 제한 등급으로 이동하거나 할당량을 늘리려면 어떻게 해야 하나요?

계정이 다음 [등급 요구사항](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko#usage-tiers)에 도달하면 할당량이 자동으로 부여됩니다.

### EEA (EU 포함), 영국, 스위스에서 Gemini API를 무료로 사용할 수 있나요?

예, [여러 지역](https://ai.google.dev/gemini-api/docs/available-regions?hl=ko)에서 무료 등급과 유료 등급을 사용할 수 있습니다.

### Gemini API로 결제를 설정하면 Google AI Studio 사용량에 대해 요금이 청구되나요?

유료 기능에 액세스하기 위해 사용자가 유료 API 키를 연결하지 않는 한 AI Studio 사용은 무료로 유지됩니다.
AI Studio에서 유료 프로젝트의 일부로 유료 API 키를 연결하면 해당 키의 AI Studio 사용량에 대해 요금이 청구됩니다. 각 유형에 연결된 해당 API 키를 사용하여 필요에 따라 유료 등급 프로젝트와 무료 등급 프로젝트 간에 전환할 수 있습니다.

### 무료 등급을 사용하는 경우 상위 등급으로 업그레이드하려면 어떻게 해야 하나요?

상위 등급에 액세스하려면 프로젝트에서 결제를 설정해야 합니다. Google AI Studio에서 [**결제 설정**](#setup-billing)을 클릭합니다. Cloud Billing 계정을 선택하거나 만드는 과정을 안내합니다. 선불 결제 모델을 사용해야 하는 경우 **결제 설정** 프로세스에서 Cloud Billing 계정에 연결된 선불 계정을 만드는 과정을 안내합니다.

### 무료 등급에서 1백만 개의 토큰을 사용할 수 있나요?

Gemini API의 무료 등급은 선택한 모델에 따라 다릅니다. 현재는 다음과 같은 방법으로 100만 개의 토큰 컨텍스트 윈도우를 사용해 볼 수 있습니다.

- Google AI Studio
- 일부 모델의 경우 무료 요금제 제공
- 후불 요금제

### 상위 (유료) 등급으로 업그레이드한 후 무료 등급으로 되돌릴 수 있나요?

무료 등급으로 다운그레이드하려면 다운그레이드할 각 프로젝트에서 [결제를 사용 중지](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ko#disable_billing_for_a_project)하면 됩니다.

### 사용 중인 토큰 수를 어떻게 계산할 수 있나요?

[`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#count_tokens) 메서드를 사용하여 토큰 수를 계산합니다. 토큰에 대해 자세히 알아보려면 [토큰 가이드](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)를 참고하세요.

### AI Studio를 통해 첫 번째 Cloud Billing 계정에 가입해도 Google Cloud 무료 체험판을 이용할 수 있나요?

첫 Cloud Billing 계정에 가입하면 [Google Cloud 무료 체험](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=ko#free-trial)이 시작되고 $300 상당의 [환영 크레딧](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ko#welcome-credits)이 부여됩니다.
하지만 이러한 크레딧은 AI Studio 사용량에 대한 비용을 지불하는 데 사용할 수 없습니다. 웰컴 크레딧을 사용하여 Google Cloud 내에서 다른 대상 서비스를 결제할 수 있습니다. 크레딧이 소진되거나 90일 이내에 만료되면 추가 사용 비용이 설정된 결제 수단으로 자동 청구됩니다.

### Gemini API에 Google Cloud 환영 크레딧을 사용할 수 있나요?

아니요, Google Cloud [환영 크레딧](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ko#welcome-credits) 또는 무료 체험 크레딧은 Gemini API 또는 AI Studio에 사용할 수 없습니다.

요건을 충족하지 않게 되기 전에 Google Cloud 환영 크레딧을 부여받은 경우 크레딧이 만료될 때까지 (90일 후) Gemini API 및 AI Studio에서 남은 크레딧을 사용할 수 있습니다.

### Google Cloud 무료 체험은 Gemini API 사용량에 적용되나요?

아니요. 2026년 3월부터 Gemini API 사용 비용은 [$300 Google Cloud 무료 체험판](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=ko#free-trial) 프로그램에서 제외됩니다.

### 결제는 어떻게 처리되나요?

Gemini API 결제는 [Cloud 결제](https://cloud.google.com/billing/docs/concepts?hl=ko) 시스템에서 처리합니다. [Cloud Billing 문서](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ko)에서 제품 내 Cloud Billing 결제 설정에 대해 알아보세요.

### 실패한 요청에 대해 요금이 청구되나요?

400 또는 500 오류로 요청이 실패하면 사용된 토큰에 대한 요금이 청구되지 않습니다. 하지만 요청은 할당량 계산에 포함됩니다.

### `GetTokens`에 요금이 청구되나요?

`GetTokens` API에 대한 요청은 요금이 청구되지 않으며 추론 할당량에 포함되지 않습니다.

### 유료 API 계정이 있는 경우 내 Google AI Studio 데이터는 어떻게 처리되나요?

Cloud 결제가 사용 설정된 경우 데이터가 처리되는 방식에 대한 자세한 내용은 [서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko#paid-services)을 참고하세요('유료 서비스'의 'Google에서 사용자 데이터를 사용하는 방식' 참고). 하나 이상의 API 프로젝트에 결제가 사용 설정되어 있는 한 Google AI Studio 프롬프트는 동일한 '유료 서비스' 약관에 따라 처리됩니다. [Gemini API 키 페이지](https://aistudio.google.com/api-keys?hl=ko)에서 '요금제' 아래에 '유료'로 표시된 프로젝트가 있는지 확인하세요.

### 선불 결제란 무엇이며 누가 선불 결제 모델을 사용해야 하나요?

선불 결제를 사용하면 AI Studio의 Gemini API 사용자가 크레딧을 사전 구매할 수 있습니다.
2026년 3월 23일부터 AI Studio의 신규 사용자는 선불 요금제를 사용해야 할 수 있습니다. AI Studio [결제 설정](#setup-billing) 과정에서 UI를 통해 결제 설정 흐름을 안내하고 선불이 필요한지 여부를 표시합니다.

### 선불 크레딧을 구매하려면 어떻게 해야 하나요? 최소 금액이나 최대 금액이 있나요?

AI Studio 결제 페이지에서 [크레딧을 구매](#buy-credits)할 수 있습니다. 구매 절차 중에 UI는 지역 및 등급 수준에 필요한 최소 사전 구매 금액과 계정에 한 번에 있을 수 있는 최대 금액을 제공합니다.

### 필요에 따라 크레딧을 자동으로 구매하도록 선불 계정을 구성할 수 있나요?

예, AI Studio 결제 설정에서 [자동 충전](#auto-reload)을 구성하는 것이 좋습니다. '트리거' 크레딧 잔액 (예: '잔액이 30달러 미만이 되면')과 '충전 금액' (예: '100달러 추가')을 지정합니다.

### 사용하지 않은 크레딧을 환불받을 수 있나요?

선불 API 크레딧은 1년 후에 만료되며 환불되지 않습니다. [선불 계정 환불 정책](#refunds)을 읽어 보세요.

### 선불 크레딧에 만료 기한이 있나요?

예, 크레딧은 구매일로부터 12개월 후에 만료됩니다.

### 선불 크레딧 잔액이 0이 되면 어떻게 되나요?

요금이 추가로 청구되지 않도록 해당 Cloud Billing 선불 계정으로 결제되는 모든 프로젝트의 모든 Gemini API 서비스가 즉시 중지됩니다. 프로젝트가 무료 등급으로 자동 다운그레이드되지 않습니다.

현재 유료 등급 수준에서 서비스를 복원하려면 [추가 크레딧을 구매](#buy-credits)해야 합니다. 크레딧을 구매한 후에는 Gemini API를 사용할 수 있습니다. Google 시스템에서 크레딧 잔액을 반영하기 위해 업데이트하는 동안 [지연](#processing-times)이 발생할 수 있습니다.

원하는 경우 무료 등급으로 다운그레이드하려면 다운그레이드하려는 프로젝트에서 [결제를 사용 중지](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=ko#disable_billing_for_a_project)하면 됩니다.

### 선불 크레딧 잔액이 0보다 큰데도 사용이 중지된 이유는 무엇인가요?

현재 등급의 [사용량 한도](#tier-spend-caps)에 도달했을 수 있습니다.
상위 등급으로 올라갈수록 사용량 한도가 자동으로 증가합니다. [Cloud Billing 계정 상태](#missed-payment)로 인해 Gemini API AI Studio 사용량도 영향을 받을 수 있습니다.

### 선불 계정 크레딧 잔액이 마이너스인 이유는 무엇인가요?

Google의 결제 및 처리 시스템이 복잡하기 때문에 크레딧을 모두 사용한 후 사용량을 차단하는 데 [지연](#processing-times)이 발생할 수 있습니다. 이 초과 사용량은 AI Studio 결제 대시보드에 마이너스 크레딧 잔액으로 표시될 수 있습니다. 이 경우 서비스가 일시중지되고 다음 크레딧 구매 시 마이너스 잔액이 차감됩니다.

Gemini API 서비스가 일시중지되지 않도록 하려면 크레딧 잔액이 지정한 값 미만으로 떨어지면 자동으로 크레딧을 추가 구매하도록 [자동 재충전](#auto-reload)을 설정하는 것이 좋습니다.

### Gemini Enterprise Agent Platform과 같은 다른 Google Cloud 서비스에 선불 크레딧을 사용할 수 있나요?

아니요. 선불 크레딧은 Gemini API 사용에만 사용할 수 있습니다. 사용하는 기타 Google Cloud 서비스 (컴퓨트, 스토리지, Gemini Enterprise Agent Platform)는 표준 [Cloud 청구 주기](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ko)를 사용하여 청구됩니다.

### 후불 결제 요금제로 전환할 수 있나요?

결제 내역을 만들고 [후불 요금제에 적합한 등급에 도달](#about-billing)하면 향후 모든 Gemini API 사용 비용을 표준 통합 Google Cloud [후불 청구 주기](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ko#view-your-charging-cycle)로 전환할 수 있습니다.

### 후불로 전환하면 선불 크레딧은 어떻게 되나요?

[후불](#postpay)로 업그레이드하면 Cloud Billing에서 선불 결제 계정을 닫고 [자동 재충전](#auto-reload)을 사용 중지하며 사용하지 않은 선불 크레딧을 자동으로 환불합니다 (표준 환불 처리 시간 적용).

### 현재 선불 크레딧 잔액과 거래 내역은 어디에서 확인할 수 있나요?

Gemini API의 모든 잔액 관리 및 거래 내역은 Google AI Studio 결제 탭 내에서 직접 수행해야 합니다.

### '결제 계정 유형이 비활성 상태이거나 지원되지 않음'이라는 메시지가 표시되는 이유는 무엇인가요?

선택한 결제 계정 유형 또는 결제 계정 상태가 AI Studio의 유료 등급에 적합하지 않은 경우 [AI Studio 결제 페이지](https://aistudio.google.com/billing?hl=ko)의 결제 상호작용이 차단되고 '결제 계정 유형이 비활성 상태이거나 지원되지 않습니다'라는 메시지가 표시될 수 있습니다.

[Cloud Console](https://console.cloud.google.com/billing/?hl=ko)에서 결제 계정의 상태를 확인하세요. 자격 요건을 충족하지 않는 유형 중 하나는 *무료 체험판 계정*입니다. 이 경우 AI Studio에서 [결제를 활성화](#setup-billing)하면 자격 요건을 충족할 수 있습니다. 비활성 상태 중 하나는 *닫힘* 상태이며, 이 경우 [계정을 다시 열 수 있습니다](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=ko).

### Gemini API 사용 비용이 Google Cloud 콘솔에 표시되나요?

예. Gemini API 비용은 Cloud Billing 계정에서 결제하는 다른 Google Cloud 서비스와 관련된 비용과 함께 [Cloud Billing 콘솔](https://console.cloud.google.com/billing?hl=ko)의 [비용 관리 페이지](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=ko#cost-reports)에서 확인할 수 있습니다. AI Studio에서만 선불 크레딧 잔액을 관리할 수 있습니다.

### AI Studio 결제에는 Gemini API 사용량과 크레딧 사용량이 표시되는데 Cloud Billing 콘솔에는 표시되지 않는 이유는 무엇인가요?

Google Cloud 및 AI Studio는 다양한 간격으로 Cloud Billing에 사용량 데이터를 보고합니다. Google의 청구 및 처리 시스템이 복잡하기 때문에 서비스 사용과 Cloud Billing에서 볼 수 있는 사용량 및 비용 사이에 지연이 발생할 수 있습니다. 일반적으로 비용 세부정보는 1일 이내에 제공되지만 경우에 따라 24시간이 초과될 수도 있습니다.
[Cloud Billing 문서](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=ko#delayed-billing)에서 지연된 결제에 대해 자세히 알아보세요.

### 후불 결제 주기가 적용되는 비용으로 다른 Google Cloud 서비스를 사용하는 경우 결제를 놓치면 어떻게 되나요?

다른 Google Cloud 서비스의 결제가 누락되면 **사용 가능한 선불 크레딧 수와 관계없이** AI Studio에서 Gemini API 액세스가 정지될 수 있습니다. AI Studio 사용량은 Google Cloud 결제 계정으로 청구되며, 이 계정은 AI Studio의 선불 결제와 다른 Cloud 서비스의 후불 결제를 모두 공유할 수 있습니다. 후불 잔액에 문제가 있으면 해당 계정에 연결된 모든 서비스가 중지됩니다. Cloud Billing 계정에 다음과 같은 문제가 있는 것으로 표시되면 Gemini API 사용이 정지됩니다.

- 연체 또는 기한이 지난 잔액
- 결제 거부
- 잘못되었거나 만료된 결제 수단

서비스를 복원하려면 Google Cloud Billing 콘솔에서 [후불 계정 문제를 해결](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=ko#resolving-declined-payments)해야 합니다. 문제를 해결하면 선불 Gemini API 크레딧 및 서비스에 다시 액세스할 수 있습니다.

### 결제 관련 도움은 어디에서 받을 수 있나요?

결제 관련 도움을 받으려면 [Cloud Billing 지원 받기](https://cloud.google.com/support/billing?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-28(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-28(UTC)"],[],[]]
