---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=zh-CN
fetched_at: 2026-08-24T02:34:45.797854+00:00
title: "\u7ed3\u7b97 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 结算

本指南概述了不同的 Gemini API 结算选项，说明了如何启用结算和监控用量，并提供了有关结算的常见问题解答 (FAQ)。

## 结算和层级简介

Gemini API 的结算层级取决于您的支付记录。

| 使用层 | 资格赛 | [结算层级上限](#spend-caps) |
| --- | --- | --- |
| **免费** | [有效项目](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#google-cloud-projects)或免费试用 | 不适用 |
| **第 1 层级** | [设置并关联有效的结算账号](#setup-billing) | $250 |
| **第 2 层级支持人员** | 支付 100 美元 + 自首次成功付款时起已满 3 天 | 2000 美元 |
| **第 3 层级支持人员** | 支付了 1,000 美元 + 自首次成功付款时起已满 30 天 | 20,000 美元至 100,000 美元以上 |

新账号会从免费层级开始，该层级允许在 Gemini API 和 AI Studio 中访问[特定模型](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)，但不得超过这些模型的免费层级[速率限制](https://aistudio.google.com/rate-limit?hl=zh-cn)。

如需直接从构建模式部署应用，您可以使用 **Google Cloud 启动层**。借助此层级，您无需设置 Google Cloud 项目或结算账号即可发布最多 2 个全栈应用。如需了解详情，请参阅[从 Google AI Studio 进行部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-cn)，并参阅 [Google Cloud 启动层级文档](https://docs.cloud.google.com/docs/starter-tier?hl=zh-cn)。

如需提高速率限制、使用高级模型，并确保您的提示和回答**不会**用于改进 Google 产品\*，您可以[关联结算账号](#setup-billing)并[预付款](#prepay)，以便改用付费方案。
然后，您将根据累计支出和账号使用时长升级到更高层级。在第 3 级，您或许可以选择改用[后付费](#postpay)结算。

层级、速率限制和结算账号上限均在[结算账号](#cloud-billing)级别确定。

\* *企业级数据隐私保护：如需详细了解付费服务的数据使用情况，请参阅[《服务条款》](https://ai.google.dev/gemini-api/terms?hl=zh-cn#data-use-paid)。*

## 设置结算信息以使用付费层级

您可以创建项目并设置结算信息，也可以导入现有项目，以便在 [Google AI Studio](https://aistudio.google.com/projects?hl=zh-cn) 中升级到付费层级。
从免费层级升级到付费层级意味着关联结算账号并[预付款](#prepay)，以便向您的账号添加至少 10 美元（或等值的其他货币）的赠金。

1. 前往 AI Studio 的 [API 密钥](https://aistudio.google.com/api-keys?hl=zh-cn)页面、[项目](https://aistudio.google.com/projects?hl=zh-cn)页面，或 AI Studio 中显示**设置结算**按钮的任何页面。
   - 系统会默认为新用户创建[项目和 API 密钥](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#google-cloud-projects)。
   - 如果您需要新密钥，请点击[**创建 API 密钥**](https://aistudio.google.com/api-keys?hl=zh-cn)，然后按照对话框中的说明向表格中添加密钥-项目对。
2. 找到要从免费层级升级到付费层级的免费层级项目，然后点击*结算层级*列下方的**设置结算**。
3. 如果您之前从未设置过 Google 结算账号，请执行以下操作：
   - 系统会要求您选择国家/地区，以同意服务条款。
   - 然后，填写或确认您的联系信息和支付方式，以继续操作。
4. 如果您之前设置过 Google 结算账号，请执行以下操作：
   - 系统会要求您从现有结算账号中进行选择。
   - 如果您不想使用任何现有账号，请点击**添加新的结算账号**，然后填写或确认您的联系信息和付款方式，以继续操作。
5. 接下来，您将：
   - 被要求预付至少 10 美元才能完成结算设置（这意味着您的账号会自动分配到[预付款](#prepay)结算方案），
   - 为您的账号提供[预付款](#prepay)和[后付费](#postpay)结算方案。
   - 在新的预付费系统普及到所有用户之前（自 2026 年 3 月 23 日起），暂时分配给[后付费](#postpay)结算方案。
6. 预付款或选择后付费后，您的账号设置即告完成。

### 升级到下一个付费层级

如果您已订阅付费层级，并且满足方案变更[条件](#about-billing)，系统会自动将您升级到下一层级（具体取决于[处理时间](#processing-times)）。

## 验证结算状态

将[结算账号](#setup-billing)关联到项目后，您可以在 [AI Studio 结算页面](https://aistudio.google.com/billing?hl=zh-cn)上监控其状态。与免费层级不同，付费层级状态是动态的；虽然您的使用层级由您的账号历史记录决定，但只有在您有正向[预付款](#prepay)余额时，Gemini API 才会处理请求。

在[项目](https://aistudio.google.com/projects?hl=zh-cn)页面上，您可以在*结算层级*列下查看项目的层级和结算方案。您可能需要针对项目采取的任何结算状态操作都会显示在*结算层级*或*状态*列中：

- 如果项目没有关联的结算账号，请点击“***设置结算***”。
- 如果项目已关联结算账号，但需要使用尚未设置的[预付款](#prepay)结算方案，则显示“***设置预付款***”。
- 如果结算账号需要购买积分，但预付款支付账号未设置或可用积分余额已用完，则显示“***无积分***”。

点击任意消息即可继续执行必要的操作。

## 监控用量

您可以在 [Google AI Studio](https://aistudio.google.com/usage?hl=zh-cn) 中监控 Gemini API 的使用情况，具体方法是依次前往**信息中心** > **使用情况**。

## 结算方案

Gemini API 和 AI Studio 的结算方案分为两类，它们决定了您何时支付使用费：预付款和后付费。您可以在 [AI Studio 结算](https://aistudio.google.com/billing?hl=zh-cn)页面上查看分配给您的结算方案并管理付款方式。

### 预付款

在预付款结算方案中，您需要在使用 Gemini API 之前购买额度并将其充入预付款余额，然后系统会[近乎实时地](#processing-times)从您的预付款余额中扣除 API 使用费。
您可以[向账号中添加金额](#buy-credits)以进行预付款，也可以设置[自动充值](#auto-reload)。购买积分后，未使用的积分将在 12 个月后过期，且[不可退款](#refunds)，[改用后付费账号](#postpay)的情况除外。

当结算账号中的预付款项余额达到 0 美元时，与该结算账号关联的所有项目中的所有 API 密钥将同时停止运行。预付款项仅适用于 Gemini API 使用费用；您无法使用它们支付其他 Google Cloud 服务的费用。

新用户默认采用预付款结算方案。在推出预付款和后付款结算方案之前创建的项目可能需要[更新项目的结算详细信息](#verify-billing)，然后才能继续使用 Gemini API。

*请注意，预付款不适用于[账单结算（或离线）](https://docs.cloud.google.com/billing/docs/concepts?hl=zh-cn#billing_account_types)账号。*

#### 购买点数

您可以在使用 Gemini API 之前手动购买积分，将其充入预付款账号的信用余额中。

如需购买点数，请前往 [AI Studio 结算](https://aistudio.google.com/billing?hl=zh-cn)页面，然后选择**购买点数**。
最低购买金额为 10 美元。您可预付的最高积分金额为 5,000 美元。

#### 自动重新加载

自动充值是一项可选功能，可在预付款余额不足时自动充值。这有助于防止服务中断。

您可以在 [AI Studio 结算](https://aistudio.google.com/billing?hl=zh-cn)页面的*可用点数*卡片中设置自动充值并查看自动充值状态。点击**设置自动充值**或**管理自动充值**，设置付款方式、充值金额以及触发充值付款的最低余额。

#### 每月自动扣款限额

月度自动扣款限额适用于预付款用户，有助于防止因频繁自动充值而产生意外费用。使用此功能可设置单个结算周期内自动充值的最高限额。如果结算周期内的自动充值总金额达到此限额，系统会停用自动充值功能，直到下个月初。您手动发起的一次性付款不计入此限制。

启用自动充值后，如需设置每月自动扣款限额，请执行以下操作：

1. 前往 [AI Studio 结算](https://aistudio.google.com/billing?hl=zh-cn)页面。
2. 点击**管理自动充值**。
3. 展开**每月限额**部分，然后输入自动充值的每月限额。
4. 点击**保存**。

### 后付费

在后付费结算方案中，您的 Cloud Billing 账号会累积费用，系统会在月底自动扣款，或者在费用达到根据账号层级[自动分配的支出上限](#tier-spend-caps)时自动扣款。系统会通过与您的后付费账号关联的付款方式收取费用，您可以在 [AI Studio 结算](https://aistudio.google.com/billing?hl=zh-cn)页面上管理该付款方式。

当您满足[第 3 级条件](#about-billing)时，可以手动从预付费方案切换到后付费方案。如需更改方案，您需要在账号符合条件后，点击 [AI Studio 结算](https://aistudio.google.com/billing?hl=zh-cn)页面右上角显示的**改用后付费**按钮。

然后，在**结算**页面上，您将能够查看余额、到期日期和过往付款，以及进行付款和管理付款方式。

为新项目[设置结算信息](#setup-billing)时，如果您符合后付费条件，则可以在[结算设置](#setup-billing)对话框中选择预付款或后付费。

将 Cloud Billing 账号改用后付费结算方案后，与该结算账号关联的所有项目都会改用后付费方案。您无法将该结算账号重新切换回预付款结算方案。您可以将项目移至采用其他结算方案的结算账号，以更改该项目的结算周期；请访问有关[管理项目结算](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-cn)的 Cloud 文档。

如需详细了解后付费结算周期，请参阅 [Cloud 结算指南](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-cn)。

## 支出上限

Gemini API 支持在结算账号层级和项目层级设置每月支出上限。这些控制措施旨在保护您的账号免遭意外超支，并保护生态系统以确保服务可用性。

*请注意，支出上限不适用于[账单结算（或离线）](https://docs.cloud.google.com/billing/docs/concepts?hl=zh-cn#billing_account_types)账号。*

### 项目支出上限

您可以在 AI Studio 中设置自己的[项目级](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#google-cloud-projects)支出上限。如果您在同一结算账号下有多个项目，并且希望确保每个项目都有足够的累计支出限额，此功能会非常有用。

拥有项目编辑者、所有者或管理员[角色](https://docs.cloud.google.com/iam/docs/roles-overview?hl=zh-cn)的账号可以在 AI Studio 的[支出](https://aistudio.google.com/spend?hl=zh-cn)页面上设置每个项目的支出上限，具体操作为依次点击**每月支出上限** > **修改支出上限**。

如需详细了解在 AI Studio 中查看或修改支出上限和结算信息所需的特定 Google Cloud IAM 权限，请参阅 [AI Studio 问题排查指南](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=zh-cn#iam-permissions)。

如果您[将项目移至其他结算账号](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-cn#change_the_billing_account_for_a_project)，则为该项目设置的所有支出上限都会保留，但所有累积支出都会在新的结算周期开始时重置为 0 美元。

长时间运行的任务（例如[批量模式](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)补全和代理会话）可能会产生超出项目支出上限的超额费用。

AI Studio 中的结算数据处理时间可能会延迟，最长延迟时间约为 10 分钟。如果结算数据在产生更多费用之前尚未处理，您可能会超出项目上限。

### 结算账号层级支出上限

每个[层级](#about-billing)都有每月支出限额：

| 使用层 | 支出上限 |
| --- | --- |
| **免费** | 不适用 |
| **第 1 层级** | $250 |
| **第 2 层级支持人员** | 2000 美元 |
| **第 3 层级支持人员** | 20,000 美元至 100,000 美元 |

系统会在[结算账号](#cloud-billing)级强制执行 Gemini API 的每月用量上限。虽然默认限制是预设的，但您可以[申请提高限制](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=zh-cn)，以适应更高的用量。总支出是已启用 Gemini API 服务的所有关联项目的支出总和。当账号累计总费用达到层级限额后，与相应结算账号关联的所有项目中的服务都会暂停，直到下一个结算周期（每个月的 1 号）开始。

#### 评估结算账号支出

如需评估您过往的每月支出，确定新的[结算账号层级支出上限](#tier-spend-caps)是否会影响您正在进行的项目，请按以下步骤操作：

1. 在 Google Cloud 控制台中，查看您的 [Cloud Billing 账号报告](https://console.cloud.google.com/billing/reports?hl=zh-cn)页面。
   - 如果您有多个结算账号，请在系统提示时选择要查看哪个 Cloud Billing 账号的费用报告。
2. 报告默认按“服务”分组，并显示“当月”的数据。您将在表格的**服务**列中看到 **Gemini API**，并在**使用费用**列中看到总支出。
3. 如需查看仅限 Gemini API 使用量的精细费用，请将**分组依据**过滤条件设置为按 **SKU** 分组，并将**服务**过滤条件设置为 **Gemini API**。
4. 将**按使用日期划分的时间范围**过滤条件调整为所需的范围，以评估您在某个时间段内的历史支出。

## 处理时间

结算信号和更新不一定实时发生。

- **赠金使用情况**：使用费用通常会在几分钟内从您的余额中扣除。
- **付款确认**：虽然大多数银行卡付款都是即时完成的，但有些付款方式（例如银行转账）可能需要几天时间才能完成。只有在点数购买交易得到正式确认后，服务才会恢复或升级。
- **会员等级升级**：成功付款后，或当您满足[升级条件](#about-billing)时，会员等级通常会在 10 分钟内升级。
- **总费用明细图表**：[结算](https://aistudio.google.com/billing?hl=zh-cn)页面和[支出](https://aistudio.google.com/spend?hl=zh-cn)页面上显示的总费用明细图表最多可能需要 24 小时才能更新。

请参阅有关[扣款周期](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-cn#delayed-billing)和[交易](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=zh-cn#missing-transactions)延迟时间的 Cloud Billing 指南，详细了解可能出现的结算延迟。

## 退款

**预付款**结算账号不允许退款，除非是切换账号类型。

**当预付费账号切换为后付费账号类型**（在您满足[条件](#about-billing)并[手动升级](#postpay)账号后），预付费账号会被关闭，所有剩余的预付款项会自动退还到您账号中记录的付款方式。

如果您因升级到后付费账号以外的任何原因而[关闭](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=zh-cn#close-a-billing-account)预付费账号，则所有剩余的预付金额都将作废。

购买的点数在 1 年后过期。过期后，积分将作废，无法再找回。

**后付费**账号遵循 [Google Cloud 退款政策](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=zh-cn#request_a_refund)。

## Cloud Billing 账号

Gemini API 使用 [Cloud Billing 账号](https://cloud.google.com/billing/docs/concepts?hl=zh-cn)进行结算，您可以[直接在 AI Studio 中设置](#setup-billing)。您可以使用 AI Studio 跟踪支出、了解费用并付款。

层级、速率限制和结算账号上限均在结算账号级确定。

### 项目和 API 密钥

与 Cloud Billing 账号关联的所有[项目](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#google-cloud-projects)都会沿用相应结算账号的使用量层级以及关联的费率限制和账号上限。如果您将项目从一个结算账号[更改为](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-cn#change_the_billing_account_for_a_project)另一个结算账号，则该项目的层级以及后续的速率限制和账号上限将切换为新结算账号的层级。

与结算账号关联的所有项目的累计支出（针对所有 Google Cloud 产品）和账号使用时长都会计入该结算账号的[层级资格条件](#about-billing)。

您可以[解除项目与结算账号的关联](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-cn#disable_billing_for_a_project)，以返回免费层级。

[API 密钥](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn)是在项目中生成的凭据。它们没有独立的结算设置，而是继承项目的层级限制和结算状态。一个项目内所有密钥的累计使用量都会计入该项目的支出上限和结算账号的总支出。

## 常见问题解答

以下部分解答了一些常见问题。

### 系统按什么向我收费？

Gemini API 的价格取决于以下因素：

- 输入 token 数
- 输出 token 数
- 缓存的 token 数
- 缓存的令牌存储时长

如需了解价格信息，请参阅[价格页面](https://ai.google.dev/pricing?hl=zh-cn)。

### 在哪里可以查看我的配额？

您可以在 [AI Studio](https://aistudio.google.com/usage?hl=zh-cn) 中查看配额和系统限制。

### 如何改用更高的速率限制层级或申请更多配额？

当您的账号达到下一个[层级要求](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-cn#usage-tiers)时，系统会自动授予您更多配额。

### 我可以在欧洲经济区（包括欧盟）、英国和瑞士免费使用 Gemini API 吗？

是的，我们已在[多个地区](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-cn)推出免费层级和付费层级。

### 如果我为 Gemini API 设置了结算信息，是否需要为 Google AI Studio 用量付费？

除非用户关联付费 API 密钥以访问付费功能，否则 AI Studio 的使用仍免费。
在 AI Studio 中将付费 API 密钥与付费项目相关联后，您将需要为该密钥的 AI Studio 用量付费。您可以根据需要，使用与付费层级项目和免费层级项目分别关联的 API 密钥，在两者之间切换。

### 如果我使用的是免费层级，如何升级到更高级别？

如需使用更高级别，您必须为项目设置结算信息。在 Google AI Studio 中点击[**设置结算信息**](#setup-billing)。此向导将引导您选择或创建 Cloud Billing 账号。如果您必须采用预付费结算模式，**设置结算**流程会引导您完成创建与 Cloud Billing 账号关联的预付费账号的流程。

### 我可以在免费层级中使用 100 万个令牌吗？

Gemini API 的免费层级因所选模型而异。目前，您可以通过以下方式试用支持 100 万个 token 的上下文窗口：

- 在 Google AI Studio 中
- 部分型号可免费使用
- 后付费方案

### 升级到更高级别（付费）层级后，我可以恢复到免费层级吗？

如需降级到免费层级，您可以为要降级的每个项目[停用结算功能](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-cn#disable_billing_for_a_project)。

### 如何计算我使用的令牌数量？

使用 [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=zh-cn#count_tokens) 方法统计令牌数量。如需详细了解令牌，请参阅[令牌指南](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)。

### 如果我通过 AI Studio 注册我的第一个 Cloud Billing 账号，是否仍可获得 Google Cloud 免费试用？

当您首次注册 Cloud Billing 账号时，[Google Cloud 免费试用](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=zh-cn#free-trial)即会开始，并且您会获得 300 美元的[欢迎赠金](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-cn#welcome-credits)。不过，这些积分不能用于支付 AI Studio 使用费。您可以使用欢迎赠金支付 Google Cloud 中的其他符合条件的服务费用（请注意，一旦这些赠金用完或过期（在 90 天内），任何额外的用量费用都会自动通过您已确定的付款方式结算）。

### 我可以使用 Google Cloud 迎新赠金来使用 Gemini API 吗？

不能，Google Cloud [迎新赠金](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-cn#welcome-credits)或免费试用赠金不能用于支付 Gemini API 或 AI Studio 的费用。

如果您在 Google Cloud 迎新赠金不符合条件之前获得了该赠金，则可以在赠金到期之前（90 天后）将剩余的赠金用于 Gemini API 和 AI Studio。

### Google Cloud 免费试用是否适用于 Gemini API 用量？

不会。自 2026 年 3 月起，Gemini API 使用费将明确不包含在 [300 美元的 Google Cloud 免费试用](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=zh-cn#free-trial)计划中。

### Google Cloud 赠金如何与预付款搭配使用？

预付费用户必须先[购买预付积分](#buy-credits)，然后才能将任何符合条件的 Google Cloud 积分用于 Gemini API 用量。当您有有效的预付款项余额时，符合 Gemini API 使用条件的 Google Cloud 赠金会先于预付款项余额被消耗。当结算账号中的预付款项余额达到 0 美元时，系统将不再消耗 Google Cloud 赠金。

并非所有 Google Cloud 赠金（例如 [Google Cloud 迎新赠金](#cloud-credits)）都可用于 Gemini API 和 AI Studio。

### 如何结算？

Gemini API 的结算由 [Cloud 结算](https://cloud.google.com/billing/docs/concepts?hl=zh-cn)系统处理。如需了解产品内 Cloud Billing 设置，请参阅 [Cloud Billing 文档](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-cn)。

### 我需要为失败的请求付费吗？

如果您的请求失败并返回 400 或 500 错误，您无需为所用的令牌付费。不过，该请求仍会占用您的配额。

### `GetTokens` 是否已结算？

对 `GetTokens` API 的请求不会产生费用，也不会计入推理配额。

### 如果我拥有付费 API 账号，Google AI Studio 如何处理我的数据？

如需详细了解启用 Cloud 结算后数据的处理方式，请参阅[服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn#paid-services)（请参阅“付费服务”下的“Google 如何使用您的数据”）。请注意，只要至少有 1 个 API 项目已启用结算功能，您的 Google AI Studio 提示就会按照相同的“付费服务”条款进行处理。您可以在 [Gemini API 密钥页面](https://aistudio.google.com/api-keys?hl=zh-cn)上验证这一点，如果看到任何项目在“方案”下标记为“付费”，则表示至少有 1 个 API 项目已启用结算功能。

### 什么是预付款结算，哪些人必须使用预付款结算模式？

预付费结算模式允许 AI Studio 中的 Gemini API 用户预先购买积分。自 2026 年 3 月 23 日起，AI Studio 新用户可能需要采用预付费结算方案。在 AI Studio [设置结算信息](#setup-billing)过程中，界面会引导您完成结算设置流程，并指明您是否需要预付款。

### 如何购买预付款积分？是否有最低金额或最高金额限制？

您可以在 AI Studio 的“结算”页面上[购买点数](#buy-credits)。在购买过程中，界面会显示您所在地区和会员等级所需的最低预购金额，以及您的账号一次最多可充值的金额。

### 我可以将预付款账号配置为在需要时自动购买更多积分吗？

是的，我们建议您在 AI Studio 结算设置中配置[自动重新加载](#auto-reload)。您可以指定“触发”点数余额（例如“当我的余额低于 30 美元时”）和“充值金额”（例如“充值 100 美元”）。

### 我可以限制自动充值金额吗？

可以。预付费用户可以在**自动充值** widget 中设置[每月自动扣款限额](#monthly-auto-charge-limit)。当结算周期内的自动充值总金额达到此限额时，系统会停用自动充值功能，直到下个月为止。手动购买的积分不计入此限额。

### 我可以获得未使用积分的退款吗？

所有预付费 API 积分的有效期均为 1 年，且无法退款。阅读[预付费账号的退款政策](#refunds)。

### 我的预付款点数会过期吗？

会，积分会在购买之日起 12 个月后过期。

### 当我的预付费抵用金余额降至 0 美元时，会发生什么情况？

由相应 Cloud Billing 预付款账号支付的所有项目中的所有 Gemini API 服务将立即停止，以避免产生更多费用。您的项目不会自动降级为免费层级。

如需恢复当前付费层级的服务，您必须[购买更多积分](#buy-credits)。购买点数后，您应该能够使用 Gemini API。请注意，我们的系统可能需要一些时间才能更新并显示您的余额，因此可能会出现[延迟](#processing-times)。

（可选）如需降级到免费层级，您可以为要降级的项目[停用结算功能](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-cn#disable_billing_for_a_project)。

### 为什么我的使用量停止了，即使我的预付款余额大于 0 美元？

您可能已达到当前层级的[用量限额](#tier-spend-caps)。
随着您升级到更高级别，用量限额会自动提高。您的 Gemini API AI Studio 使用情况也可能会因 [Cloud Billing 账号的状态](#missed-payment)而受到影响。

### 为什么我的预付款账号的信用余额为负数？

由于我们的结算和处理系统较为复杂，因此在您用完所有积分后，我们可能无法及时停止使用。这部分超额用量可能会在 AI Studio 结算信息中心内显示为负的信用余额。如果出现这种情况，您的服务会被暂停，并且您的负余额将从您下次购买的积分中扣除。

为避免 Gemini API 服务暂停，我们建议您设置[自动充值](#auto-reload)，以便在点数余额低于您指定的值时自动购买更多点数。

### 我能否将预付款项用于其他 Google Cloud 服务，例如 Gemini Enterprise Agent Platform？

不可以，预付款点数只能用于 Gemini API。您使用的任何其他 Google Cloud 服务（Compute、Storage、Gemini Enterprise Agent Platform）均按标准 [Cloud 结算周期](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-cn)结算。

### 我可以改用后付费结算方案吗？

当您建立付款记录并[达到符合条件的层级](#about-billing)时，您可以选择将所有未来的 Gemini API 使用费用转为标准的、整合的 Google Cloud [后付费结算周期](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-cn#view-your-charging-cycle)。

### 如果我从预付费方案改用后付费方案，我的预付费积分会怎么样？

升级到[后付费](#postpay)后，Cloud Billing 会关闭您的预付款支付账号，关闭[自动充值](#auto-reload)，并自动将所有未使用的预付款赠金退还给您（退款处理时间需遵循标准）。

### 在哪里可以查看我的当前预付款余额和交易记录？

Gemini API 的所有余额管理和交易记录都必须直接在 Google AI Studio 的“结算”标签页中完成。

### 为什么我会看到“结算账号类型无效或不受支持”？

如果所选结算账号类型或结算账号状态不符合 AI Studio 付费层的条件，[AI Studio 结算页面](https://aistudio.google.com/billing?hl=zh-cn)上的付款互动可能会被屏蔽，并替换为“结算账号类型处于非活动状态或不受支持”消息。

请查看 [Cloud 控制台](https://console.cloud.google.com/billing/?hl=zh-cn)，了解结算账号的状态。一种不符合条件的账号类型可能是*免费试用账号*，在这种情况下，您可以在 AI Studio 中[启用结算功能](#setup-billing)，从而符合条件。一种非活跃状态可能是*已关闭*，在这种情况下，您可以[重新开启账号](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=zh-cn)。

### 我的 Gemini API 使用费用会显示在 Google Cloud 控制台中吗？

可以。Gemini API 费用以及 Cloud Billing 账号支付的任何其他 Google Cloud 服务的相关费用都可以在 [Cloud Billing 控制台](https://console.cloud.google.com/billing?hl=zh-cn)的[费用管理页面](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=zh-cn#cost-reports)中查看。请注意，您只能在 AI Studio 中管理预付款余额。

### 为什么我的 Gemini API 用量未显示在 Cloud Billing 控制台中，而我可以在 AI Studio 结算中看到该用量以及我的赠金消耗情况？

Google Cloud 和 AI Studio 会以不同的时间间隔向 Cloud Billing 报告使用情况数据。由于我们的结算和处理系统较为复杂，您可能会在使用服务与可在 Cloud Billing 中查看的使用量和费用之间看到延迟现象。通常一天之内即可获得您的费用明细，但有时可能需要 24 小时以上。如需详细了解延迟结算，请参阅 [Cloud Billing 文档](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-cn#delayed-billing)。

### 如果我使用的其他 Google Cloud 服务会产生费用，并且这些费用采用后付费结算周期，那么如果我未按时付款会怎么样？

如果您未支付其他 Google Cloud 服务的费用，即使**预付款余额充足**，您在 AI Studio 中使用 Gemini API 的权限也可能会被暂停。AI Studio 的使用由 Google Cloud 结算账号提供支持，该账号可以同时用于 AI Studio 的预付款结算和其他 Cloud 服务的后付款结算。如果您的后付费余额存在问题，则与相应账号关联的所有服务都会暂停。如果您的 Cloud Billing 账号因以下问题而被标记，您的 Gemini API 使用权限将被中止：

- 欠款或逾期未结款项
- 付款被拒
- 付款方式无效或已过期

如需恢复服务，您必须在 Google Cloud 结算控制台中[解决后付费账号问题](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=zh-cn#resolving-declined-payments)。解决问题后，您将重新获得对预付费 Gemini API 积分和服务的访问权限。

### 在哪里可以获得结算方面的帮助？

如需有关结算的帮助，请参阅[获取 Cloud Billing 支持](https://cloud.google.com/support/billing?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-07。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-07。"],[],[]]
