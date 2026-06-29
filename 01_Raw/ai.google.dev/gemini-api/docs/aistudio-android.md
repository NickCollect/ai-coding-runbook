---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=zh-TW
fetched_at: 2026-06-29T05:33:44.860650+00:00
title: "\u5728 Google AI Studio \u4e2d\u5efa\u69cb Android \u61c9\u7528\u7a0b\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 在 Google AI Studio 中建構 Android 應用程式

Google AI Studio 可讓您根據自然語言提示建構原生 Android 應用程式。說明您想要的應用程式，[Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-tw#antigravity-agent) 就會生成完整的 Kotlin 和 [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=zh-tw) 專案。您可以在瀏覽器中預覽應用程式，透過瀏覽器型 Android 模擬器安裝應用程式到實體裝置，並發布應用程式以進行測試。

## 開始使用

如要開始建構 Android 應用程式，請按照下列步驟操作：

1. 使用左側導覽面板，前往 Google AI Studio 的[建構模式](https://aistudio.google.com/apps?hl=zh-tw)。
2. 從平台挑選器中選取「Android」**Android**。
3. 輸入提示詞，描述要建構的應用程式 (例如*「建立具有本機儲存空間的每日工作追蹤表」*或*「建立簡易計算機」*)。
4. 代理程式會產生專案，並在以瀏覽器為基礎的 Android 模擬器中啟動專案。

接著，您就能使用聊天面板反覆改良應用程式，就像在網頁上操作一樣。代理程式會管理 Android 專案中的所有檔案，並在程式碼集內傳播變更。

## 瀏覽器式 Android 模擬器

Android 模擬器完全在雲端執行，並串流至瀏覽器。
您不需要安裝 Android SDK、Android Studio 或本機模擬器。

模擬器提供以下功能：

- **模擬 Pixel 裝置**：輕觸、捲動及與應用程式互動，就像在實際裝置上操作一樣。
- **支援旋轉**：切換直向和橫向模式。
- **即時預覽**：當代理程式變更程式碼時，應用程式會重建，模擬器也會自動重新整理。

### 模擬器限制

瀏覽器型模擬器不支援所有硬體功能。模擬器不支援下列功能：

- 拍攝相片
- NFC 和藍牙
- GPS (模擬位置)
- Google Play 服務 (Google 登入、地圖和其他 Play 服務功能可在實體裝置上運作，但無法在模擬器中運作)

## 透過 ADB 安裝到裝置

您可以直接在透過 USB 連接至電腦的實體 Android 裝置上安裝建構的 APK。這項功能會使用 [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=zh-tw)，透過瀏覽器與裝置通訊。您無需在本機安裝 ADB。

### 必要條件

- 支援 WebUSB 的 Chrome 或 Edge 瀏覽器。
- 已啟用[開發人員選項和 USB 偵錯](https://developer.android.com/studio/debug/dev-options?hl=zh-tw)的 Android 裝置。
- 將裝置連接到電腦的 USB 傳輸線。

### 在裝置上安裝應用程式

1. 在預覽面板中，按一下「在裝置上安裝」。
2. 在瀏覽器的 USB 裝置選擇器中選取 Android 裝置。
3. APK 會傳輸到裝置並安裝。
4. 應用程式會自動啟動。

## 發布至 Play 商店

您可以將 Android 應用程式發布至 [Google Play 管理中心](https://play.google.com/console?hl=zh-tw)的內部測試群組，最多可將應用程式發布給 100 位測試人員。

### 必要條件

- [Google Play 開發人員帳戶](https://play.google.com/console/signup?hl=zh-tw) (需支付 $25 美元的單次註冊費)。
- 在 Play 管理中心填妥開發人員設定檔。

### 發布應用程式

1. 在 Google AI Studio 中開啟「設定」>「發布」。
2. 按一下「發布至 Play 商店」。
3. 使用 Google Play 開發人員帳戶進行驗證。
4. AI Studio 會簽署 APK、建立應用程式資訊 (或上傳新版本)，並發布至內部測試群組。
5. 您會收到一個連結，可分享給測試人員。

AI Studio 會使用代管的 KeyStore 自動管理 APK 簽署作業。您可以在 Play 管理中心自訂應用程式資訊 (圖示、螢幕截圖、說明)。

## 生成內容

建構 Android 應用程式時，代理程式會產生標準的 Gradle 專案，結構如下：

- **建構設定**：使用 Kotlin DSL 的 `build.gradle.kts` 檔案 (專案和應用程式層級)。
- **UI 層**：使用 [Material 3](https://m3.material.io/) 主題設定的 [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=zh-tw) 元件。
- **架構**：單一活動架構，包含 ViewModel 和資料類別。
- **資源**：`AndroidManifest.xml`、可繪項目、字串和其他 Android 資源。

代理程式會自動管理 Gradle 依附元件，並視需要從 Maven 和 Google 存放區新增套件。

您可以使用預覽面板中的「程式碼」分頁，查看及編輯產生的程式碼。如要在 Android Studio 中繼續開發，請將專案下載為 **ZIP 檔案**。

## 限制

在 AI Studio 中建構 Android 應用程式時，有下列限制：

### 平台限制

- **僅限用戶端**：Android 應用程式不含伺服器端元件。
  需要伺服器執行階段的功能 (密鑰管理、多人遊戲、Firebase、Google Workspace API) 無法使用。
- **單一活動架構**：僅支援單一活動、單一模組專案。
- **僅限 Jetpack Compose**：應用程式使用 Kotlin 和 Jetpack Compose。不支援 Java 和 XML 版面配置。
- **不含 NDK 或原生程式碼**：不支援 C 和 C++ 程式碼。
- **不支援 Wear OS 或 Android TV**：僅支援手機和平板電腦板型規格。

### 匯出限制

- **僅下載 ZIP 檔**：您可以將專案下載為 ZIP 檔案。Android 專案目前無法匯出至 GitHub。

## 後續步驟

- [在 Google AI Studio 中建構應用程式](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-tw)
- [開發全端應用程式](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-tw) (網頁)
- 請參閱[應用程式庫](https://aistudio.google.com/apps?source=showcase&hl=zh-tw)中的範例。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-19 (世界標準時間)。"],[],[]]
