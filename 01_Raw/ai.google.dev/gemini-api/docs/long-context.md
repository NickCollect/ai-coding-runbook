---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=zh-TW
fetched_at: 2026-07-06T05:06:52.052053+00:00
title: "\u9577\u8108\u7d61 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 長脈絡

許多 Gemini 模型都提供 100 萬個以上的詞元脈絡窗口。
過去，大型語言模型 (LLM) 一次可傳遞給模型的文字 (或權杖) 數量有限，Gemini 長脈絡窗口可支援許多新的應用實例和開發人員範例。

您目前用於[文字生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw)或[多模態輸入](https://ai.google.dev/gemini-api/docs/vision?hl=zh-tw)等用途的程式碼，無需任何變更即可搭配長脈絡使用。

這份文件將概略說明如何使用脈絡窗口達 100 萬個以上詞元的模型。本頁面簡要介紹脈絡窗口，並探討開發人員應如何看待長脈絡、長脈絡的各種實際用途，以及如何最佳化長脈絡的使用方式。

如要瞭解特定模型的脈絡窗口大小，請參閱「[模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)」頁面。

## 什麼是脈絡窗口？

使用 Gemini 模型的基本方式是將資訊 (脈絡) 傳遞給模型，模型隨後會生成回覆。情境視窗就像短期記憶。人的短期記憶體可儲存的資訊量有限，生成模型也是如此。

如要進一步瞭解模型運作方式，請參閱[生成模型指南](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw#under-the-hood)。

## 開始使用長內容

舊版生成模型一次只能處理 8,000 個權杖。新版模型更進一步，可接受 32,000 個，甚至是 128,000 個權杖。Gemini 是第一個可接受 100 萬個權杖的模型。

實務上，100 萬個權杖會如下所示：

- 50,000 行程式碼 (每行標準 80 個半形字元)
- 過去 5 年內傳送的所有簡訊
- 8 本平均長度的英文小說
- 超過 200 集平均長度的 Podcast 轉錄稿

許多其他模型常見的脈絡窗口較小，因此通常需要採取策略，例如任意捨棄舊訊息、摘要內容、搭配向量資料庫使用 RAG，或篩選提示來節省權杖。

雖然這些技術在特定情境中仍有價值，但 Gemini 的脈絡窗口範圍廣泛，因此建議採用更直接的方法：預先提供所有相關資訊。Gemini 模型專為龐大的脈絡功能而打造，因此展現了強大的脈絡內學習能力。舉例來說，Gemini 僅使用情境內教學教材 (500 頁的參考文法、字典和約 400 個平行句子)，就[學會將英文翻譯成卡拉芒文](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)。卡拉芒文是巴布亞語言，使用者不到 200 人，但 Gemini 的翻譯品質與使用相同教材的人類學習者相近。這說明 Gemini 長脈絡功能帶來的典範轉移，透過強大的脈絡內學習功能，開創全新可能性。

## 長脈絡用途

雖然大多數生成式模型的標準用途仍是文字輸入，但 Gemini 模型系列可支援全新的多模態用途。這些模型可原生理解文字、影片、音訊和圖片。並搭配 [Gemini API，可接收多模態檔案類型](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=zh-tw)，方便使用。

### 長篇文字

事實證明，文字是 LLM 發展動能背後的重要智慧層。如前文所述，LLM 的許多實用限制，都是因為沒有足夠大的脈絡視窗來執行特定工作。這促使檢索增強生成 (RAG) 和其他技術迅速普及，可動態為模型提供相關情境資訊。現在，隨著脈絡窗口越來越大，我們可以使用新技術，發掘新的應用情境。

文字型長背景資訊的新興和標準用途包括：

- 生成大量文字的摘要
  - 如果使用較小的脈絡模型，先前的摘要選項會需要滑動視窗或其他技術，才能在將新權杖傳遞至模型時，保留先前章節的狀態
- 問答
  - 由於脈絡量有限，且模型的事實回憶率偏低，因此過去只有 RAG 才能做到這點
- 代理工作流程
  - 文字是代理程式記錄已完成事項和待辦事項的基礎，如果缺乏世界和代理程式目標的相關資訊，代理程式的可靠性就會受到限制

[大量樣本脈絡學習](https://arxiv.org/pdf/2404.11018)是長脈絡模型最獨特的功能之一。研究顯示，採用常見的「單樣本」或「多樣本」範例範式，向模型呈現一或多個工作範例，並將範例擴增至數百、數千，甚至數十萬個，可帶來全新的模型功能。研究結果顯示，這種多樣本方法與針對特定工作微調的模型效能相近。如果 Gemini 模型在某些應用情境中的效能仍不足以用於正式版，可以嘗試多樣本方法。如您稍後在長內容最佳化一節中瞭解，內容快取可大幅降低這類高輸入權杖工作負載的成本，在某些情況下甚至能縮短延遲時間。

### 長篇影片

長期以來，由於影片本身缺乏無障礙功能，因此影片內容的實用性受到限制。難以快速瀏覽內容、轉錄稿經常無法捕捉影片的細微差異，而且大多數工具無法同時處理圖片、文字和音訊。Gemini 的長文脈文字功能可解讀多模態輸入內容，並持續提供優異的推理和問答能力。

影片長背景資訊的新興和標準用途包括：

- 影片問答
- 影片記憶體，如 [Google 的 Project Astra](https://deepmind.google/technologies/gemini/project-astra/?hl=zh-tw) 所示
- 影片字幕
- 影片推薦系統，透過新的多模態理解功能豐富現有中繼資料
- 影片客製化：查看資料和相關影片中繼資料，然後移除與觀眾無關的影片部分
- 影片內容審查
- 即時影片處理

處理影片時，請務必考量[影片如何轉換為權杖](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw#media-token)，這會影響帳單和用量限制。如要進一步瞭解如何使用影片檔案提示，請參閱[提示指南](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=zh-tw#prompting-with-videos)。

### 長篇音訊

Gemini 模型是首批可解讀音訊的本質多模態大型語言模型。過去，開發人員通常會將多個特定領域的模型串連在一起，例如語音轉文字模型和文字轉文字模型，藉此處理音訊。這導致執行多個往返要求時需要額外延遲，且效能下降通常歸因於多個模型設定的架構中斷連線。

音訊背景資訊的新興和標準用途包括：

- 即時語音轉錄及翻譯
- Podcast / 影片問答
- 會議語音轉錄和摘要
- 語音助理

如要進一步瞭解如何使用音訊檔案提示，請參閱[提示指南](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=zh-tw#prompting-with-videos)。

## 長脈絡最佳化

使用長脈絡和 Gemini 模型時，主要最佳化方式是使用[脈絡快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)。除了先前無法在單一要求中處理大量詞元，另一個主要限制是費用。假設您有一個「與資料對話」應用程式，使用者上傳了 10 份 PDF、一部影片和一些工作文件。過去，您必須使用較複雜的檢索增強生成 (RAG) 工具/框架來處理這些要求，並支付大量權杖費用，才能將資料移至內容視窗。現在您可以快取使用者上傳的檔案，並按小時付費儲存這些檔案。舉例來說，使用 Gemini Flash 時，每項要求的輸入 / 輸出費用比標準輸入 / 輸出費用低約 4 倍，因此如果使用者與資料的對話次數夠多，您身為開發人員就能大幅節省費用。

## 長脈絡限制

在本指南的各個章節中，我們說明瞭 Gemini 模型如何在各種大海撈針檢索評估中，展現優異的效能。這些測試會考量最基本的設定，也就是您要尋找單一針頭。如果有多個「針」或特定資訊要尋找，模型的準確度會降低。成效可能會因脈絡而異。請務必考慮這點，因為擷取正確資訊和成本之間存在固有的取捨關係。單一查詢的準確率可達 99%，但每次傳送查詢時，您都必須支付輸入權杖費用。因此，如要擷取 100 筆資訊，且需要 99% 的效能，您可能需要傳送 100 個要求。這就是一個很好的例子，說明內容快取如何大幅降低使用 Gemini 模型相關的成本，同時維持高效能。

## 常見問題

### 在脈絡窗口中，查詢的最佳位置在哪裡？

在大多數情況下，如果整體脈絡很長，將查詢 / 問題放在提示結尾 (所有其他脈絡之後)，模型效能會更好。

### 在查詢中加入更多權杖時，模型效能是否會受到影響？

一般來說，如果不需要將權杖傳遞至模型，最好避免傳遞。不過，如果有一大段含有某些資訊的詞元，且想詢問與該資訊相關的問題，模型就能準確擷取資訊 (在許多情況下，準確率高達 99%)。

### 如何透過長內容查詢降低費用？

如果您有一組類似的權杖 / 脈絡想重複使用多次，[脈絡快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)功能有助於減少與該資訊相關的提問費用。

### 背景資訊長度會影響模型延遲嗎？

無論要求大小為何，都會有固定的延遲時間，但一般來說，查詢時間越長，延遲時間 (第一個權杖的時間) 就越長。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-22 (世界標準時間)。"],[],[]]
