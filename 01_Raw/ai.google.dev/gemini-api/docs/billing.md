---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=zh-TW
fetched_at: 2026-11-02T07:13:26.379771+00:00
title: "\u8a08\u8cbb\u65b9\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 計費方式

本指南將概略說明不同的 Gemini API 計費選項、如何啟用計費和監控用量，並提供有關計費的常見問題解答。

## 關於帳單和等級

Gemini API 的計費方式會根據您的付款記錄而定。

| 用量層級 | 資格賽 | [帳單層級上限](#spend-caps) |
| --- | --- | --- |
| **免費** | [有效專案](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#google-cloud-projects)或免費試用方案 | 不適用 |
| **第 1 級** | [設定並連結有效的帳單帳戶](#setup-billing) | $250 美元 |
| **第 2 級** | 首次付款成功後，3 天內支付 $100 美元 | $2,000 美元 |
| **第 3 級** | 支付 $1,000 美元 + 首次付款成功後 30 天 | $20,000 美元 - $100,000 美元以上 |

新帳戶會先採用免費方案，可存取 Gemini API 和 AI Studio 中的[特定模型](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)，但須遵守模型免費方案的[速率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)。

如要直接從「建構」模式部署應用程式，符合資格的帳戶可以使用 **Google Cloud 入門級**。這個方案可讓您發布最多 2 個全端應用程式，不必設定 Google Cloud 雲端專案或帳單帳戶。如要瞭解資格詳情，請參閱「[從 Google AI Studio 部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-tw#starter-tier-eligibility)」，並參閱 [Google Cloud 入門級說明文件](https://docs.cloud.google.com/docs/starter-tier?hl=zh-tw)。

如要提高速率限制、使用進階模型，以及確保系統**不會**使用提示和回覆內容來改善 Google 產品\*，請[連結帳單帳戶](#setup-billing)並[預付](#prepay)費用，改用付費方案。然後，系統會根據累計支出和帳戶年齡，將你移至較高的層級。

層級、速率限制和帳單帳戶上限，都是在[帳單帳戶](#cloud-billing)層級決定。

\* *企業級資料隱私權：如要進一步瞭解付費服務的資料使用方式，請參閱[服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw#data-use-paid)。*

## 設定帳單資訊以存取付費方案

您可以建立專案並設定帳單，或匯入現有專案，在 [Google AI Studio](https://aistudio.google.com/projects?hl=zh-tw) 升級至付費層級。
從免費方案升級至付費方案時，請連結帳單帳戶並[預付款項](#prepay)，為帳戶儲值至少 $5 美元 (或其他貨幣的等值金額)。

1. 前往 AI Studio 的「API 金鑰」頁面、「專案」頁面，或 AI Studio 中顯示「設定帳單」按鈕的任何位置。
   - 新使用者預設會建立[專案和 API 金鑰](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#google-cloud-projects)。
   - 如需新金鑰，請按一下「建立 API 金鑰」，然後按照對話方塊的指示，將金鑰/專案配對新增至表格。
2. 找出要從免費方案升級至付費層級的專案，然後點選「帳單層級」欄下方的「設定帳單」。
3. 如果你從未設定 Google 帳單帳戶：
   - 系統會要求你選取國家/地區，並同意《服務條款》。
   - 接著，請填寫或確認聯絡資訊和付款方式，然後繼續。
4. 如果您過去曾設定 Google 帳單帳戶：
   - 系統會要求你從現有帳單帳戶中選擇。
   - 如不想使用現有帳戶，請按一下「新增帳單帳戶」，然後填寫或確認聯絡資訊和付款方式，即可繼續操作。
5. 接下來，您會看到下列其中一個畫面：
   - 系統要求預付至少 $5 美元，才能完成帳單設定 (表示系統已自動將您的帳戶指派至[預付](#prepay)帳單方案)。
   - 帳戶可選擇[預付](#prepay)或[後付](#postpay)方案。
   - 在新的預付系統向所有使用者推出前 (2026 年 3 月 23 日起)，暫時採用[後付](#postpay)結帳方案。
6. 預付或選取後付後，帳戶設定即完成。

### 升級至下一個付費層級

如果你已訂閱付費方案，且符合[條件](#about-billing)，系統會自動將你升級至下一個方案 (升級作業的[處理時間](#processing-times)不一定)。

## 確認帳單狀態

[將帳單帳戶連結至專案](#setup-billing)後，即可在 [AI Studio 帳單頁面](https://aistudio.google.com/billing?hl=zh-tw)監控帳戶狀態。與免費級別不同，付費級別狀態是動態的；用量級別取決於帳戶記錄，但只有在[預付](#prepay)抵免額餘額為正數時，Gemini API 才會處理要求。

在「專案」頁面中，您可以在「帳單級別」欄下方查看專案的級別和帳單方案。您可能需要對專案採取任何帳單狀態動作，這些動作會顯示在「帳單層級」或「狀態」欄中：

- 如果專案未連結至帳單帳戶，請點選「***設定帳單***」。
- 如果專案已連結帳單帳戶，但必須使用需要設定的「***預付***」計費方案，請按照畫面上的指示操作。
- 如果帳單帳戶必須購買點數，但預付付款帳戶尚未設定或可用點數餘額已用盡，則會顯示「***沒有點數***」。

點選任一訊息，即可採取必要行動。

## 監控使用情況

如要監控 Gemini API 用量，請前往 [Google AI Studio](https://aistudio.google.com/usage?hl=zh-tw) 的「資訊主頁」 >「用量」。

## 計費方案

Gemini API 和 AI Studio 的帳單方案分為兩類，決定您何時支付用量費用：預付和後付。您可以在「AI Studio Billing」(AI Studio 帳單) 頁面查看已指派的帳單方案，以及管理付款方式。

### 預付

在預付計費方案中，您會預先購買抵免額，並將抵免額計入預付餘額，而系統會[近乎即時](#processing-times)地從預付抵免額餘額中扣除 Gemini API 用量費用。你可以[在帳戶中新增額度](#buy-credits)來預付費用，或設定[自動儲值](#auto-reload)。購買抵免額後，未使用的抵免額會在 12 個月後失效，且[無法退款](#refunds) ([改用後付型帳戶](#postpay)的情況除外)。

當帳單帳戶的預付額度餘額達到 $0 美元時，連結至該帳單帳戶的所有專案中的所有 API 金鑰都會同時停止運作。您必須先新增點數，否則要求會失敗，並顯示 [HTTP 402 須付款](https://ai.google.dev/gemini-api/docs/api-errors?hl=zh-tw)錯誤。預付抵免額僅適用於 Gemini API 使用費用，無法用於支付其他 Google Cloud 服務費用。

新使用者預設會採用預付方案。如果專案是在預付和後付帳單方案推出前建立，可能需要[更新專案的帳單詳細資料](#verify-billing)，才能繼續使用 Gemini API。

*請注意，[可開立月結單的 (或離線)](https://docs.cloud.google.com/billing/docs/concepts?hl=zh-tw#billing_account_types)帳戶不適用預付功能。*

#### 在現有的後付帳戶中新增預付方案

如果現有的 Cloud Billing 帳戶使用**後付**方案，可以新增**預付**功能，預先購買抵免額。有了預付抵免額，您就能使用 Gemini API，不必建立新的 Cloud Billing 帳戶。

在設定程序中，為現有帳戶新增**預付**款項時，系統會顯示強制確認畫面，說明所選的 Cloud Billing 帳戶將會修改。

系統必須在您提交預付款*前*修改帳戶狀態。
因此，如果在確認修改後但完成預付款設定前取消程序，已連結至該 Cloud Billing 帳戶的專案可能會暫時中斷服務。確認轉換前，請務必準備好完成預付款程序。如果遇到問題，請參閱「[取消**預付**設定後服務中斷](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-tw#prepay-issue)」。

如果符合資格，並手動從「預付」週期切換至「後付」週期，系統會自動將所有剩餘的預付抵免額餘額，退還至預付時使用的原付款方式。不過，如果因其他原因關閉 Cloud Billing 帳戶，剩餘的預付抵免額將會失效，且無法退款。

#### 購買抵免額

您可以在使用 Gemini API 前手動購買抵免額，並將抵免額存入預付帳戶的信用額度餘額。

如要購買點數，請前往「AI Studio 帳單」頁面，然後選取「購買點數」。
最低購買金額為 $5 美元。預付抵免額的金額上限為 $5,000 美元。

#### 自動重新載入

自動儲值是選用功能，可讓系統在預付抵免額餘額不足時自動加值。這有助於避免服務中斷。

你可以在「AI Studio 帳單」頁面的「可用抵免額」資訊卡中設定自動儲值，並查看自動儲值狀態。按一下「設定自動儲值」或「管理自動儲值」，設定付款方式、儲值金額，以及觸發儲值付款的最低餘額。

#### 每月自動扣款上限

預付使用者可設定每月自動扣款上限，避免因頻繁自動儲值而產生意外費用。使用這項功能，即可在單一帳單週期內，設定自動加值次數上限。如果帳單週期內的自動儲值總金額達到上限，系統就會停用自動儲值功能，直到下個月初才會重新啟用。您手動發起的一次性付款不會計入這項限制。

啟用自動儲值功能後，如要設定每月自動扣款上限，請按照下列步驟操作：

1. 前往「AI Studio 帳單」頁面。
2. 按一下「管理自動儲值功能」。
3. 展開「每月限額」部分，然後輸入自動儲值的每月上限。
4. 按一下 [儲存]。

### 後付

在後付費方案中，Cloud Billing 帳戶會累積費用，並在月底或費用達到[系統根據帳戶層級自動指派的支出上限](#tier-spend-caps)時，自動扣款。系統會透過連結至後付帳戶的付款方式收費，您可以在 [AI Studio 帳單](https://aistudio.google.com/billing?hl=zh-tw)頁面管理付款方式。在「帳單」頁面中，您可以查看餘額、到期日和過往付款記錄，以及付款和管理付款方式。

[為新專案設定帳單資訊](#setup-billing)時，如果符合後付資格，您可以在[帳單設定](#setup-billing)對話方塊中選擇預付或後付。

將 Cloud Billing 帳戶切換為使用後付費方案後，連結至該帳單帳戶的所有專案都會切換為後付費方案。如要將符合資格的帳戶改為預付，請按照「[改為預付](#migrate-to-prepay)」一文的步驟操作。您也可以將專案移至採用不同帳單方案的帳單帳戶，藉此變更專案的收費週期；請參閱「[管理專案的帳單](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-tw)」一文。

如要進一步瞭解後付方案的收費週期，請參閱 [Cloud Billing 指南](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-tw)。

### 改用預付

Google AI Studio 正在將開發人員帳戶的 Gemini API 用量帳單，從後付改為預付。這項變更只會影響 Gemini API；連結至帳單帳戶的其他 Google Cloud 服務仍會採用後付方案。

請在帳戶通知中的轉換日期前切換至預付方案並儲值，以免服務中斷。如果帳戶只使用免費方案功能，則不必採取任何行動。

如要將現有的後付帳戶改為預付，請按照下列步驟操作：

1. 前往「AI Studio 帳單」頁面。
2. 選取帳單帳戶的「切換至預付」。
3. [購買抵免額](#buy-credits) (最低 $5 美元)，做為起始餘額。

為避免服務在切換後中斷，請設定[自動儲值](#auto-reload)，在抵免餘額不足時自動儲值。

## 支出上限

Gemini API 支援帳單帳戶層級和專案層級的每月支出上限。這些控制項旨在保護帳戶，避免產生預期外的超額費用，並確保生態系統的服務可用性。

*請注意，[可開立月結單的 (或離線)](https://docs.cloud.google.com/billing/docs/concepts?hl=zh-tw#billing_account_types)
帳戶不適用支出上限。*

### 專案支出上限

您可以在 AI Studio 中設定[專案層級](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#google-cloud-projects)的支出上限。
如果您在同一個帳單帳戶下有多個專案，且想確保每個專案都有足夠的累計支出上限，這項功能就非常實用。

如要為 AI Studio 中的每個專案設定支出上限，請使用具備專案編輯者、擁有者或管理員[角色](https://docs.cloud.google.com/iam/docs/roles-overview?hl=zh-tw)的帳戶，依序前往「Monthly spend cap」 >「Edit spend cap」，然後在「Spend」頁面中設定。

如要瞭解在 AI Studio 中查看或編輯支出上限和帳單資訊所需的特定 Google Cloud IAM 權限，請參閱 [AI Studio 疑難排解指南](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=zh-tw#iam-permissions)。

如果[將專案移至其他帳單帳戶](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-tw#change_the_billing_account_for_a_project)，專案原先設定的支出上限會保留，但累積支出會在新的帳單週期重設為 $0。

如果執行長時間執行的工作 (例如[批次模式](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)完成和代理程式工作階段)，可能會超出專案支出上限。

AI Studio 的帳單資料處理時間可能會延遲，最多約 10 分鐘。如果系統在累積更多費用前尚未處理帳單資料，您可能會超出專案上限。

### 帳單帳戶層級支出上限

每個[等級](#about-billing)都有每月支出上限：

| 用量層級 | 支出上限 |
| --- | --- |
| **免費** | 不適用 |
| **第 1 級** | $250 美元 |
| **第 2 級** | $2,000 美元 |
| **第 3 級** | $20,000 美元至 $100,000 美元 |

系統會在[帳單帳戶](#cloud-billing)層級，對 Gemini API 設下每月用量上限。預設上限為預先設定，但您可以[要求提高上限](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=zh-tw)，以因應更高的用量。系統會彙整已啟用 Gemini API 服務的所有連結專案支出總額。當帳戶累計總額達到層級上限後，系統會暫停與該帳單帳戶連結的所有專案服務，直到下一個帳單週期開始 (每月 1 號) 為止。

#### 評估帳單帳戶支出

如要評估過往的每月支出，判斷新的[帳單帳戶層級支出上限](#tier-spend-caps)是否會影響進行中的專案，請按照下列步驟操作：

1. 在 Google Cloud 控制台中，查看 [Cloud Billing 帳戶的「報表」](https://console.cloud.google.com/billing/reports?hl=zh-tw)頁面。
   - 如果有多個帳單帳戶，請在系統提示時選擇要查看費用報表的 Cloud Billing 帳戶。
2. 報表預設會依「當月」的「服務」分組。您會在表格的「服務」欄中看到「Gemini API」，並在「用量費用」欄中看到總支出。
3. 如要查看 Gemini API 用量的詳細費用，請將「依分組」篩選器設為依 **SKU** 分組，並將「服務」篩選器設為「Gemini API」。
4. 將「依使用日期篩選時間範圍」調整為所需範圍，即可評估特定期間的歷史支出。

## 處理時間

帳單信號和更新不一定會即時顯示。

- **抵免額用量**：使用費用通常會在幾分鐘內從餘額扣除。
- **確認付款**：大多數的信用卡付款都會立即完成，但部分付款方式 (例如銀行轉帳) 可能需要數天才能完成。購買點數的交易正式確認後，服務才會恢復或升級。
- **等級升級**：付款成功或符合[升級條件](#about-billing)後，等級通常會在 10 分鐘內升級。
- **總費用明細圖表**：[「帳單」](https://aistudio.google.com/billing?hl=zh-tw)頁面和[「支出」](https://aistudio.google.com/spend?hl=zh-tw)頁面上的總費用明細圖表，最多需要 24 小時才會更新。

請參閱有關[收費週期](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-tw#delayed-billing)和[交易](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=zh-tw#missing-transactions)延遲的 Cloud Billing 指南，進一步瞭解可能發生的帳單延遲情形。

## 退款

**預付**帳單帳戶無法申請退款，但變更帳戶類型時除外。

**預付帳戶切換為後付帳戶類型時** (符合[條件](#about-billing)並[手動升級](#postpay)帳戶後)，預付帳戶會關閉，剩餘的預付抵免額會自動退還至已登記的付款方式。

如果因升級為後付以外的原因[關閉](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=zh-tw#close-a-billing-account)預付帳戶，系統會停用所有預付點數餘額，

已購買抵免額的有效期限為 1 年。抵免額過期後即會失效，無法再使用。

**後付**帳戶適用 [Google Cloud 退款政策](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=zh-tw#request_a_refund)。

## Cloud Billing 帳戶

Gemini API 會使用 [Cloud Billing 帳戶](https://cloud.google.com/billing/docs/concepts?hl=zh-tw)支付服務費用，您可以在 [AI Studio 中直接設定](#setup-billing)。您可以使用 AI Studio 追蹤支出、瞭解費用，以及付款。

層級、速率限制和帳單帳戶上限都是在帳單帳戶層級決定。

### 專案和 API 金鑰

連結至 Cloud Billing 帳戶的所有[專案](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#google-cloud-projects)，都會沿用該帳戶的使用量層級、相關費率限制和帳戶上限。如果[將專案從一個帳單帳戶移至另一個帳單帳戶](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-tw#change_the_billing_account_for_a_project)，專案的層級 (以及隨後的速率限制和帳戶上限) 會切換至新帳單帳戶的層級。

與帳單帳戶相關聯的所有專案，其累計支出 (所有 Google Cloud 產品) 和帳戶存在時間，都會計入該帳單帳戶的[層級資格](#about-billing)。

如要返回免費層級，可以[取消專案與帳單帳戶的連結](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-tw#disable_billing_for_a_project)。

[API 金鑰](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw)是在專案內產生的憑證。
沒有獨立的帳單設定，而是沿用專案的層級限制和帳單狀態。專案中所有金鑰的累計用量，都會計入該專案的支出上限和帳單帳戶的總支出。

## 常見問題

以下各節提供常見問題的解答。

### 我需要支付什麼費用？

Gemini API 的價格取決於以下因素：

- 輸入詞元數
- 輸出詞元數
- 快取詞元數
- 快取權杖儲存時間

如需定價資訊，請參閱[定價頁面](https://ai.google.dev/pricing?hl=zh-tw)。

### 如何查看配額？

您可以在 [AI Studio](https://aistudio.google.com/usage?hl=zh-tw) 中查看配額和系統限制。

### 如何升級至更高的速率限制層級，或要求更多配額？

當帳戶達到下一個[層級的規定](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-tw#usage-tiers)時，系統會自動授予更多配額。

### 在歐洲經濟區 (包括歐盟)、英國和瑞士，可以免費使用 Gemini API 嗎？

是的，我們在[許多區域](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-tw)提供免費和付費方案。

### 如果我為 Gemini API 設定帳單，是否需要支付 Google AI Studio 的使用費用？

除非使用者連結付費 API 金鑰來存取付費功能，否則 AI Studio 仍可免費使用。在 AI Studio 中，將付費 API 金鑰連結至付費專案後，系統就會針對該金鑰的 AI Studio 用量收費。您可以視需要使用與各類型連結的 API 金鑰，在付費方案專案和免費方案專案之間切換。

### 如果我使用免費方案，如何升級至更高方案？

如要使用較高的層級，必須先在專案中設定帳單資訊。在 Google AI Studio 中，按一下「設定帳單」。系統會引導你選取或建立 Cloud Billing 帳戶。如果必須採用預付型帳單模式，系統會透過「設定帳單」程序，引導您建立連結至 Cloud Billing 帳戶的預付帳戶。

### 免費方案可以使用 100 萬個權杖嗎？

Gemini API 的免費方案會因所選模型而異。目前，您可以透過下列方式試用 100 萬個詞元的脈絡窗口：

- 在 Google AI Studio 中
- 指定車款可享免付費方案
- 後付費方案

### 升級至較高 (付費) 層級後，可以還原為免費方案嗎？

如要降級至免費方案，請在要降級的每個專案中[停用計費功能](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-tw#disable_billing_for_a_project)。

### 如何計算我使用的權杖數量？

使用 [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=zh-tw#count_tokens) 方法計算權杖數量。如要進一步瞭解權杖，請參閱[權杖指南](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw)。

### 如果我透過 AI Studio 申請第一個 Cloud Billing 帳戶，還能獲得 Google Cloud 免費試用方案嗎？

首次註冊 Cloud Billing 帳戶時，系統會啟動 [Google Cloud 免費試用](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=zh-tw#free-trial)，並提供 $300 美元的[迎新抵免額](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-tw#welcome-credits)。不過，這些抵免額無法用於支付 AI Studio 用量。您可以使用歡迎抵免額支付 Google Cloud 中其他符合資格的服務費用 (請注意，一旦抵免額用完或過期 (90 天內)，系統就會自動透過您設定的付款方式，收取任何額外使用費)。

### 我可以使用 Google Cloud 迎新抵免額搭配 Gemini API 嗎？

否，Google Cloud [迎新抵免額](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-tw#welcome-credits)或免費試用抵免額無法用於 Gemini API 或 AI Studio。

如果 Google Cloud 迎新抵免額在您取得後才不符合資格，您仍可在抵免額到期前 (90 天後)，將剩餘抵免額用於 Gemini API 和 AI Studio。

### Google Cloud 免費試用方案是否適用於 Gemini API 用量？

不行。自 2026 年 3 月起，Gemini API 用量費用將不計入 [$300 美元的 Google Cloud 免費試用](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=zh-tw#free-trial)計畫。

### Google Cloud 抵免額如何與預付方案搭配運作？

預付使用者必須先[購買預付額度](#buy-credits)，才能將任何符合資格的 Google Cloud 抵免額用於 Gemini API。如果預付抵免額餘額有效，系統會先使用適用於 Gemini API 的 Google Cloud 抵免額，再使用預付抵免額餘額。當帳單帳戶的預付抵免額餘額達到 $0 時，系統將不再使用 Google Cloud 抵免額。

並非所有 Google Cloud 抵免額 (例如 [Google Cloud 迎新抵免額](#cloud-credits)) 都能用於 Gemini API 和 AI Studio。

### 如何計費？

Gemini API 的帳單事務是由 [Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=zh-tw) 系統處理。如要瞭解如何透過產品設定 Cloud Billing，請參閱 [Cloud Billing 說明文件](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-tw)。

### 系統會對失敗的要求收費嗎？

如果要求失敗並傳回 400 或 500 錯誤，系統不會收取使用的權杖費用。不過，這類要求仍會計入配額。

### 「`GetTokens`」是否已結算？

對 `GetTokens` API 的要求不會產生費用，也不會計入推論配額。

### 如果我使用付費 API 帳戶，Google AI Studio 資料會如何處理？

如要瞭解啟用 Cloud 帳單後資料的處理方式，請參閱《[服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw#paid-services)》的「付費服務」部分，並查看「Google 如何使用您的資料」。請注意，只要至少有 1 個 API 專案啟用帳單功能，Google AI Studio 提示就會適用相同的「付費服務」條款。如要驗證，請前往 [Gemini API 金鑰頁面](https://aistudio.google.com/api-keys?hl=zh-tw)，查看「方案」下方是否有任何專案標示為「付費」。

### 什麼是預付結算？哪些人必須使用預付結算模式？

預付帳單功能可讓 AI Studio 中的 Gemini API 使用者預購抵免額。2026 年 3 月 23 日起，AI Studio 新使用者可能必須採用預付方案。在 AI Studio 的「設定帳單」過程中，使用者介面會引導您完成帳單設定流程，並指出是否需要預付款。

### 如何購買預付抵免額？是否有最低或最高金額限制？

你可以在 AI Studio 的「帳單」頁面[購買點數](#buy-credits)。在購買過程中，使用者介面會顯示您所在區域和層級的最低預付金額，以及帳戶一次可儲值的最高金額。

### 我可以設定預付帳戶，在需要時自動購買更多點數嗎？

建議您在 AI Studio 帳單設定中設定[自動重新載入](#auto-reload)。您指定「觸發」抵免額餘額 (例如「當餘額低於 $30 美元時」) 和「儲值金額」(例如「加值 $100 美元」)。

### 我可以限制自動儲值金額嗎？

可以。預付型方案使用者可以在「自動儲值」小工具中設定「每月自動扣款上限」。當帳單週期內的自動儲值總金額達到這個上限時，系統會停用自動儲值功能，直到下個月為止。手動購買的點數不會計入這項限制。

### 未使用的點數可以退款嗎？

所有預付 API 點數的有效期限為 1 年，且無法退款。詳閱[預付帳戶的退款政策](#refunds)。

### 預付抵免額會過期嗎？

會，抵免額會在購買日起 12 個月後到期。

### 預付額度用完會怎麼樣？

為避免產生更多費用，由該 Cloud Billing 預付帳戶支付的所有專案中，所有 Gemini API 服務都會立即停止。專案不會自動降級為免費方案。

如要恢復目前付費層級的服務，請[購買額外點數](#buy-credits)。購買抵免額後，您應該就能使用 Gemini API。請注意，系統更新以反映信用額度時，可能會有[延遲](#processing-times)。

如要降級至免費方案，可以選擇在要降級的專案中[停用計費功能](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=zh-tw#disable_billing_for_a_project)。

### 為什麼預付額度大於 $0，但使用量卻停止了？

你可能已達到目前方案的[用量上限](#tier-spend-caps)。
隨著你升級至較高的級別，用量限制也會自動增加。[Cloud Billing 帳戶狀態](#missed-payment)也可能影響 Gemini API AI Studio 用量。

### 為什麼我的預付帳戶信用額度餘額為負值？

由於帳單和處理系統相當複雜，因此在您用完所有抵免額後，我們可能[延遲](#processing-times)停止服務。這類超額用量可能會在 AI Studio 帳單資訊主頁中顯示為負值抵免餘額。如果發生這種情況，服務會暫停，而負餘額會從您下次購買的抵免額中扣除。

為避免 Gemini API 服務暫停，建議您設定[自動儲值](#auto-reload)，在抵免餘額低於指定值時自動購買更多抵免額。

### 預付抵免額是否可用於其他 Google Cloud 服務，例如 Gemini Enterprise Agent Platform？

不行，預付抵免額只能用於 Gemini API。您使用的任何其他 Google Cloud 服務 (Compute、Storage、Gemini Enterprise Agent Platform) 都會按照標準 [Cloud 計費週期](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-tw)計費。

### 可以從預付改為後付嗎？

否，系統不支援從預付帳單方案切換至後付帳單方案。

### 可以從後付切換為預付帳單嗎？

可以，您可以在 [AI Studio 帳單](https://aistudio.google.com/billing?hl=zh-tw)頁面轉換現有的後付帳戶。如需操作說明，請參閱「[改用預付方案](#migrate-to-prepay)」。

### 如果改用月結方案，預付額度會怎麼樣？

升級至[後付](#postpay)後，Cloud Billing 會關閉預付付款帳戶、停用[自動儲值](#auto-reload)，並自動將任何未使用的預付抵免額退還給您 (退款處理時間依標準程序而定)。

### 我可以在哪裡查看目前的預付額度餘額和交易記錄？

如要管理 Gemini API 餘額和交易記錄，請直接前往 Google AI Studio 的「帳單」分頁。

### 為什麼會看到「帳單帳戶類型無效或不受支援」？

如果所選帳單帳戶類型或帳單帳戶狀態不符合 AI Studio 付費層級的資格，系統可能會封鎖 [AI Studio 帳單頁面](https://aistudio.google.com/billing?hl=zh-tw)的付款互動，並顯示「帳單帳戶類型無效或不支援」訊息。

請前往 [Cloud Console](https://console.cloud.google.com/billing/?hl=zh-tw) 查看帳單帳戶狀態。其中一種不符合資格的類型可能是*免費試用帳戶*，在這種情況下，您可以在 AI Studio 中[啟用帳單](#setup-billing)，即可符合資格。其中一種閒置狀態是「已關閉」，在這種情況下，您可以[重新開啟帳戶](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=zh-tw)。

### Google Cloud 控制台會顯示 Gemini API 用量費用嗎？

可以。Gemini API 費用以及 Cloud Billing 帳戶支付的任何其他 Google Cloud 服務相關費用，都會顯示在 [Cloud Billing 控制台](https://console.cloud.google.com/billing?hl=zh-tw)的[費用管理頁面](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=zh-tw#cost-reports)。請注意，你只能在 AI Studio 中管理預付額度餘額。

### 為什麼我在 AI Studio 帳單中可以看到 Gemini API 用量和抵免額用量，但 Cloud Billing Console 中卻沒有顯示？

Google Cloud 和 AI Studio 會按照不同間隔，將用量資料回報給 Cloud Billing。由於帳單和處理系統較為複雜，您可能需要等待一段時間，才能在 Cloud Billing 中查看服務用量和費用。費用明細通常會在一天內顯示，但有時可能超過 24 小時。如要進一步瞭解延遲結算，請參閱 [Cloud Billing 說明文件](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=zh-tw#delayed-billing)。

### 如果我使用其他 Google Cloud 服務，且費用適用於後付費週期，如果我未付款會發生什麼情況？

如果其他 Google Cloud 服務的款項未繳清，即使**預付抵免額充足**，系統仍會暫停您在 AI Studio 中存取 Gemini API。AI Studio 的用量會透過 Google Cloud Billing 帳戶計費，該帳戶可同時用於 AI Studio 的預付帳單，以及其他 Cloud 服務的後付帳單。如果後付餘額有問題，與該帳戶相關的所有服務都會停止運作。如果 Cloud Billing 帳戶因下列問題遭到標記，Gemini API 用量就會遭到停權：

- 逾期或未繳的餘額
- 已遭拒的付款
- 付款方式無效或過期

如要恢復服務，請前往 Google Cloud Billing 控制台[解決後付費帳戶問題](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=zh-tw#resolving-declined-payments)。解決問題後，您就能重新使用預付型 Gemini API 抵免額和服務。

### 取消預付設定後，為什麼專案會中斷？

**問題：**您已啟動程序，要為現有的後付帳單帳戶新增預付功能，但尚未完成預付設定，就關閉視窗或取消程序。與該帳單帳戶連結的其他專案將無法存取 Gemini API。

**原因：**在轉換流程中，接受確認對話方塊後，系統會立即在帳單帳戶中建立支援預付的基礎架構。如果未完成預付步驟，設定會維持無法收費的狀態。由於這項狀態適用於帳單帳戶層級，因此凡是連結至該帳單帳戶且依賴預付服務的專案，都會受到存取限制。

**解決方法：**由於帳戶狀態已變更，如果放棄付款流程，系統不會自動還原狀態。如要還原連結專案的服務，請執行下列任一操作：

- **完成設定：**返回 Google AI Studio，重新啟動帳單設定流程，然後完成預付款程序。付款處理完畢後，預付帳單方案就會啟用，服務也會恢復。
- **聯絡支援團隊：**如果您不想使用預付計費方案，並想將帳單帳戶還原為後付方案，請[聯絡 Cloud Billing 支援團隊](https://cloud.google.com/support/billing?hl=zh-tw)，手動重設帳戶狀態。

### 如何取得帳單相關協助？

如需帳單相關協助，請參閱「[取得 Cloud Billing 支援](https://cloud.google.com/support/billing?hl=zh-tw)」。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-28 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-28 (世界標準時間)。"],[],[]]
