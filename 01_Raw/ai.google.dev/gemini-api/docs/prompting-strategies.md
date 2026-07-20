---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja
fetched_at: 2026-07-20T04:40:47.217583+00:00
title: "\u30d7\u30ed\u30f3\u30d7\u30c8\u8a2d\u8a08\u6226\u7565 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# プロンプト設計戦略

プロンプト設計とは、言語モデルから正確で高品質なレスポンスを引き出すプロンプト（自然言語リクエスト）を作成するプロセスです。

このページでは、Gemini AI モデルを最大限に活用するためのプロンプト設計の基本的なコンセプト、戦略、ベスト プラクティスについて説明します。

## トピック別のプロンプト ガイド

より具体的なプロンプト戦略をお探しですか？次のプロンプト ガイドをご覧ください。

- [メディア ファイルを使用したプロンプト](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide)
- [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ja#imagen-prompt-guide) と [Gemini ネイティブ画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja#prompt-guide) を使用した画像生成のプロンプト
- [動画生成のプロンプト](https://ai.google.dev/gemini-api/docs/video?hl=ja#prompt-guide)

その他のサンプル プロンプトについては、[プロンプト ギャラリー](https://ai.google.dev/gemini-api/prompts?hl=ja)
をご覧ください。このガイドで説明されているコンセプトの多くをインタラクティブに紹介しています。

## 明確で具体的な指示

モデルの動作をカスタマイズする効果的かつ効率的な方法は、明確で具体的な指示を与えることです。指示は、質問、段階的なタスク、ユーザー エクスペリエンスや考え方を表すような複雑な内容にすることもできます。

### 入力

入力は、モデルにレスポンスを提供させるプロンプトの必須テキストです。入力は、モデルが回答する質問（質問入力）、モデルが実行するタスク（タスク入力）、モデルが動作するエンティティ（エンティティ入力）、またはモデルが完了または続行する部分入力（コンプリーション入力）のいずれかです。

| **入力タイプ** | **プロンプト** | **生成された出力** |
| --- | --- | --- |
| 質問 | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| タスク | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| エンティティ | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### 部分的な入力の補完

生成言語モデルは、高度な予測入力ツールのように機能します。部分的なコンテンツを提供すると、モデルは残りのコンテンツ、またはコンテンツの継続として認識したコンテンツをレスポンスとして提供できます。その場合、例やコンテキストを含めると、モデルはそれらの例やコンテキストを考慮できます。

次の例では、指示とエンティティ入力を含むプロンプトを示しています。

|  |
| --- |
| **プロンプト:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **レスポンス:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  （gemini-2.5-flash） |

モデルはプロンプトに従って動作しましたが、自然言語での指示は難しい場合があり、モデルの解釈に多くの負担が残ります。
たとえば、レストランのメニューに多くのアイテムが含まれているとします。JSON レスポンスのサイズを小さくするには、オーダーされていないアイテムを省略します。この場合、例とレスポンス接頭辞を指定して、モデルに完成させることができます。

|  |
| --- |
| **プロンプト:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **レスポンス:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  （gemini-2.5-flash） |

「cheeseburger」は注文に含まれていないため、出力から除外されています。

プロンプトを使用して単純な JSON レスポンス オブジェクトの形式を指定できますが、
レスポンスに複雑な JSON スキーマを指定する場合は、Gemini API's
[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)機能を使用することをおすすめします。

### 制約

プロンプトの読み取りやレスポンスの生成に関する制約を指定します。行うべきことと、行うべきでないことをモデルに指示できます。たとえば、必要な要約の長さについてプロンプトで制約を指定できます。

|  |
| --- |
| **プロンプト:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **レスポンス:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  （gemini-2.5-flash） |

### 回答の形式

指示の中でレスポンスの形式を指定することもできます。たとえば、表、箇条書き、エレベーター ピッチ、キーワード、文、段落の形式でレスポンスを求めることができます。次のシステム指示は、レスポンスでより会話形式にするようモデルに指示します。

|  |
| --- |
| **システム指示**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **プロンプト**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **レスポンス:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  （gemini-2.5-flash） |

#### 完了戦略でレスポンスの形式を設定する

[完了戦略](#completion)は、レスポンスの形式にも活用できます。
次の例では、小論文の概要を作成するようにモデルに指示しています。

|  |
| --- |
| **プロンプト:**    ``` Create an outline for an essay about hummingbirds. ```  **レスポンス:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  （gemini-2.5-flash） |

プロンプトでアウトラインの形式が指定されていないため、モデルによって形式が選択されています。モデルが特定の形式でアウトラインを返すようにするには、アウトラインの始点を表すテキストを追加し、開始パターンに基づいてモデルを完成させます。

|  |
| --- |
| **プロンプト:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **レスポンス:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  （gemini-2.5-flash） |

## ゼロショット プロンプトと少数ショット プロンプト

プロンプトに、モデルに対して望ましい動作を示す例を含めることができます。モデルは、例からパターンと関係を特定し、回答を生成する際にそれらを適用します。いくつかの
例を含むプロンプトは*少数ショット* プロンプトと呼ばれ、例のない
プロンプトは*ゼロショット* プロンプトと呼ばれます。少数ショット プロンプトは、モデルのレスポンスのフォーマット、フレーズ、範囲、一般的なパターンの設定を規制するために頻繁に使用されます。具体的で多様な例を使用して、モデルが焦点を絞り込み、より正確な結果を生成できるようにします。

プロンプトには、常に少数ショットの例を含めることをおすすめします。少数ショットの例は、モデルに対して指示の適用方法を示すものであり、このようなショットのないプロンプトは効果的でない可能性があります。タスクを説明するのに十分な例が含まれていれば、プロンプトから指示を削除することも可能です。

次のゼロショット プロンプトでは、モデルに最良の説明を選択するよう求めます。

|  |
| --- |
| **プロンプト:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **レスポンス:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  （gemini-2.5-flash） |

ユースケースでモデルが簡潔なレスポンスを生成する必要がある場合は、簡潔なレスポンスを優先する例をプロンプトに含めることができます。

次のプロンプトでは、短い説明を優先する例を 2 つ示します。レスポンスでは、前の例のような長い説明（`Explanation1`）ではなく、短い説明（`Explanation2`）を選択するように例がモデルをガイドしたことがわかります。

|  |
| --- |
| **プロンプト:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **レスポンス:**    ``` Answer: Explanation2 ```  （gemini-2.5-flash） |

### 最適なサンプル数

Gemini などのモデルでは、多くの場合、いくつかの例を使用してパターンを検出できますが、最適な結果を得るには、プロンプトで提供する例の数をテストすることが必要な場合があります。同時に、過剰に多くの例を追加すると、
モデルが例に対するレスポンスを[過学習](https://developers.google.com/machine-learning/glossary?hl=ja#overfitting)
し始める可能性があります。

### 一貫性のある形式

レスポンスが望ましくない形式で返されないように、少数ショットの例の構造と形式を同じにする必要があります。プロンプトに少数ショットの例を追加する主な目的の 1 つは、モデルにレスポンスの形式を示すことです。そのため、すべてのサンプルで形式を統一することが重要になります。特に、XML タグ、空白、改行、サンプルの分割子には注意してください。

## コンテキストを追加する

モデルに必要な情報がすべて与えられていると仮定するのではなく、モデルが問題を解決するために必要な指示や情報をプロンプトに含めることができます。このコンテキスト情報により、モデルは求められている内容について、制約と詳細を理解できます。

次の例では、モデルにルーターのトラブルシューティング ガイダンスを提供するよう求めています。

|  |
| --- |
| **プロンプト:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **レスポンス:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  （gemini-2.5-flash） |

レスポンスは一般的なトラブルシューティング情報のように見えますが、ルーターや LED インジケーター ライトのステータスに固有のものではありません。

特定のルーターに関するレスポンスをカスタマイズするには、ルーターのトラブルシューティング ガイドを、レスポンスの提供時に参照するコンテキストとしてプロンプトに追加します。

|  |
| --- |
| **プロンプト:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **レスポンス:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  （gemini-2.5-flash） |

## プロンプトをコンポーネントに分割する

複雑なプロンプトを必要とするユースケースでは、プロンプトをより単純なコンポーネントに分割することで、モデルでこの複雑さを管理できるようになります。

1. **指示を分割する:** 1 つのプロンプトに複数の指示を記述するのではなく、指示ごとに 1 つのプロンプトを作成します。ユーザーの入力に基づいて、処理するプロンプトを選択できます。
2. **プロンプトを連結する:** 複数の連続したステップを含む複雑なタスクの場合は、各ステップをプロンプトにして、プロンプトを順番に連結します。プロンプトが順番に並んだこの連鎖では、シーケンス内の 1 つのプロンプトの出力が次のプロンプトの入力になります。シーケンス内の最後のプロンプトの出力が最終出力です。
3. **レスポンスを集計する:** 集計とは、データのさまざまな部分に対して異なる並列タスクを実行し、結果を集計して最終出力を生成することです。たとえば、データの最初の部分に対して 1 つのオペレーションを実行し、残りのデータに対して別のオペレーションを実行して、結果を集計するようにモデルに指示できます。

## モデル パラメータをテストする

モデルに送信する呼び出しの一つ一つに、モデルがどのようにレスポンスを生成するかを制御するパラメータ値が含まれています。このモデルは、パラメータ値によって異なる結果を生成できます。さまざまなパラメータ値を試して、タスクに最適な値を取得します。使用可能なパラメータはモデルに世代によって異なる場合があります。最も一般的なパラメータは次のとおりです。

1. **最大出力トークン:** レスポンスで生成できるトークンの最大数を指定します。トークンは約 4 文字です。100 トークンは約 60 ～ 80 語に相当します。
2. **Temperature:** Temperature は、トークン選択のランダム性の度合いを制御します。温度は、レスポンス生成時のサンプリングに使用されます。レスポンス生成は、`topP` と `topK` が適用された場合に発生します。温度が低いほど、確定的で自由度を抑えたレスポンスが求められるプロンプトに適しています。一方、温度が高いと、より多様で創造的な結果を導くことができます。Temperature 0 は決定的であり、最も高い確率のレススポンスが常に選択されることを意味します。
3. **`topK`:** `topK` パラメータは、モデルが出力用のトークンを選択する方法を変更します。`topK` が 1 の場合、選択されるトークンは、モデルの語彙内のすべてのトークンで最も確率の高いものであることになります（グリーディ デコードとも呼ばれます）。`topK` が 3 の場合は、最も確率が高い上位 3 つのトークンから次のトークン選択されることになります（温度を使用します）。トークン選択ステップごとに、確率が最も高い `topK` トークンがサンプリングされます。その後、トークンは `topP` に基づいてさらにフィルタリングされ、最終的なトークンは温度サンプリングを用いて選択されます。
4. **`topP`:** `topP` パラメータは、モデルが出力用のトークンを選択する方法を変更します。トークンは、確率の合計が `topP` 値に等しくなるまで、確率の高いものから低いものへと選択されます。たとえば、トークン A、B、C の確率が 0.3、0.2、0.1 で、`topP` が 0.5 だとします。このとき、モデルは次のトークンとして A か B を Temperature を使って選択し、C は候補から外します。デフォルトの `topP` 値は 0.95 です。
5. **`stop_sequences`:** 停止シーケンスを設定して、コンテンツの生成を停止するようモデルに指示します。停止シーケンスには任意の文字シーケンスを使用できます。生成されたコンテンツに表示される可能性のある文字シーケンスは使用しないようにしてください。

## プロンプトの反復処理に関する戦略

プロンプト設計では、望ましいレスポンスを一貫して得られるようになるまでにイテレーション（反復）が何度か必要になることがあります。このセクションでは、プロンプトを反復処理する際に試すことができるいくつかのガイダンスについて説明します。

1. **異なるフレーズを使用する:** プロンプトで異なる単語やフレーズを使用すると、すべて同じ意味であっても、多くの場合、モデルの応答は異なります。プロンプトから期待される結果が得られない場合は、言い換えてみてください。

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **同様のタスクに切り替える:** モデルに対してタスクの指示に従わせることができない場合は、同じ結果が得られる同様のタスクの指示を出してみてください。

   このプロンプトは、事前定義されたカテゴリを使用して書籍を分類するようモデルに指示します。

   |  |
   | --- |
   | **プロンプト:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **レスポンス:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  （gemini-2.5-flash） |

   レスポンスは正解ですが、モデルがオプションの境界内に収まっていません。また、完全な文ではなく、いずれかのオプションのみを使用して応答するようにモデル化する必要があります。この場合は、指示を多肢選択式の質問として言い換えて、モデルにオプションの選択を求めることができます。

   |  |
   | --- |
   | **プロンプト:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **レスポンス:**

     ```
     The correct answer is mythology.
     ```

     （gemini-2.5-flash）
   - **プロンプト コンテンツの順序を変更する:** プロンプト内のコンテンツの順序がレスポンスに影響する場合があります。コンテンツの順序を変更して、レスポンスにどう影響するかを確認してみます。

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## フォールバック レスポンス

フォールバック レスポンスは、プロンプトまたはレスポンスのいずれかが安全フィルタをトリガーした場合に、モデルが返すレスポンスです。フォールバック レスポンスの例としては、「私は言語モデルにすぎないため、それについては対応できません」が挙げられます。

モデルがフォールバック レスポンスを返す場合は、温度を上げてみてください。

## グラウンディングとコード実行

Gemini は、ツールを使用して、誤ったレスポンスを生成する可能性のあるシナリオでハルシネーションを回避できます。

[Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)は、
Gemini モデルをリアルタイムのウェブ コンテンツに接続します。モデルが
不明な事実や最新の事実を知る必要がある場合は、この機能を有効にする必要があります。

Gemini の [コード実行ツール](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)を使用すると、
モデルは Python コードを生成して実行できます。モデル
が算術演算、カウント、計算を行う必要がある場合は、この機能を有効にする必要があります。

## Gemini 3

[Gemini 3 モデル](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-3)は、高度な
推論と指示の遵守を目的として設計されています。
タスクと制約が明確に定義された、直接的で構造化されたプロンプトに最適に応答します。Gemini 3 で最適な結果を得るには、次の方法をおすすめします。

### プロンプトの基本原則

- **正確かつ直接的に記述する:** 目標を明確かつ簡潔に記述します。不要な表現や説得力のある表現は避けてください。
- **一貫した構造を使用する:** 明確な区切り文字を使用して、プロンプトのさまざまな部分を分離します。XML スタイルのタグ（`<context>`、`<task>` など）や
  Markdown 見出しが効果的です。1 つの形式を選択し、1 つのプロンプト内で一貫して使用します。
- **パラメータを定義する:** あいまいな用語やパラメータは明示的に説明します。
- **出力の冗長性を制御する:** デフォルトでは、Gemini 3 モデルは直接的で効率的な回答を提供します。より会話形式または詳細なレスポンスが必要な場合は、指示で明示的にリクエストする必要があります。
- **マルチモーダル入力を一貫して処理する:** テキスト、画像、音声、動画を使用する場合は、同じクラスの入力として扱います。必要に応じて、指示で各モダリティを明確に参照してください。
- **重要な指示を優先する:** 重要な動作制約、ロール定義（ペルソナ）、出力形式の要件は、システム指示またはユーザー プロンプトの冒頭に記述します。
- **長いコンテキストの構造化:** 大量のコンテキスト（ドキュメント、コードなど）を提供する場合は、最初にすべてのコンテキストを指定します。具体的な指示や質問は、プロンプトの末尾に記述します。
- **コンテキストを固定する:** 大量のデータブロックの後に、コンテキストとクエリを橋渡しする明確な移行フレーズ（「上記の情報に基づいて...」など）を使用します。

### Gemini 3 Flash の戦略

- **現在日の精度:** モデルが 2026 年の現在日に注意を払うように、次の句をシステム指示に追加します。

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **ナレッジ カットオフの精度:** モデルがナレッジ カットオフを認識するように、次の句をシステム指示に追加します。

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **グラウンディングのパフォーマンス:** 提供されたコンテキストでレスポンスをグラウンディングするモデルの能力を向上させるには、次の句をシステム指示に追加します（必要に応じて編集します）。

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### 推論と計画の強化

Gemini 2.5 シリーズと 3 シリーズのモデルは、推論のパフォーマンスを向上させるために、内部の「思考」テキストを自動的に生成します。そのため、返されたレスポンス自体でモデルがアウトライン、計画、推論ステップの詳細を示す必要はありません。高度な推論が必要な問題については、「回答する前に慎重に検討してください」などの簡単なリクエストでパフォーマンスを向上させることができますが、思考トークンが追加されます。

詳細については、[Gemini の思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)に関するドキュメントをさらに
ご覧ください。

### 構造化されたプロンプトの例

タグまたは Markdown を使用すると、モデルは指示、コンテキスト、タスクを区別できます。

**XML の例:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Markdown 記法の例:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### ベスト プラクティスを組み合わせたテンプレートの例

このテンプレートは、Gemini 3 でプロンプトを使用するための基本原則を捉えています。特定のユースケースに合わせて、必ず反復処理と変更を行ってください。

**システム指示:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**ユーザー プロンプト:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## エージェント ワークフロー

高度なエージェント ワークフローでは、モデルがタスクを推論、計画、実行する方法を制御するために、具体的な指示が必要になることがよくあります。Gemini は一般的なパフォーマンスに優れていますが、複雑なエージェントでは、多くの場合、計算コスト（レイテンシとトークン）とタスクの精度とのトレードオフを構成する必要があります。

エージェントのプロンプトを設計する際は、エージェントで制御できる次の動作の側面を考慮してください。

### 推論と戦略

行動を起こす前にモデルが思考し、計画を立てる方法の構成。

- **論理分解:** モデルが制約、前提条件、オペレーションの順序をどの程度徹底的に分析する必要があるかを定義します。
- **問題の診断**: 原因を特定する際の分析の深さと、モデルの仮説的推論の使用を制御します。モデルが最も明白な回答を受け入れるか、複雑で可能性の低い説明を探索するかを決定します。
- **情報の網羅性:** 利用可能なすべてのポリシーとドキュメントを分析することと、効率と速度を優先することのトレードオフ。

### 実行と信頼性

エージェントが自律的に動作し、障害を処理する方法の構成。

- **適応性:** モデルが新しいデータにどのように反応するか。最初の計画を厳守するか、観測結果が仮定と矛盾する場合はすぐにピボットするかを決定します。
- **永続性と復旧:** モデルがエラーを自己修正しようとする度合い。永続性が高いほど成功率は向上しますが、トークン費用やループが増加するリスクがあります。
- **リスク評価:** 結果を評価するロジック。低リスクの探索的アクション（読み取り）と高リスクの状態変更（書き込み）を明示的に区別します。

### インタラクションと出力

エージェントがユーザーと通信し、結果の形式を設定する方法の構成。

- **あいまいさと権限の処理:** モデルが仮定を行うことが許可される場合と、実行を一時停止してユーザーに明確化または権限を求める必要がある場合を定義します。
- **冗長性:** ツール呼び出しとともに生成されるテキストの量を制御します。これにより、モデルがユーザーにアクションを説明するか、実行中に無音のままにするかが決まります。
- **精度と完全性:** 出力の必要な忠実度。モデルがすべてのエッジケースを解決して正確な数値を提示する必要があるか、概算で許容されるかを指定します。

### システム指示テンプレート

次のシステム指示は、モデルが複雑なルールブックを遵守し、ユーザーとやり取りする必要があるエージェント ベンチマークのパフォーマンスを向上させるために研究者によって評価された例です。エージェントが強力な推論者およびプランナーとして行動することを推奨し、上記のディメンション全体で特定の動作を強制し、モデルが行動を起こす前に積極的に計画を立てることを要求します。

このテンプレートは、特定のユースケースの制約に合わせて調整できます。

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## 次のステップ

- プロンプト設計について理解を深めたので、
  独自のプロンプトを[Google AI Studio](http://aistudio.google.com?hl=ja)を使用して作成してみてください。
- マルチモーダル プロンプトの詳細については、
  [メディア ファイルを使用したプロンプト](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide)をご覧ください。
- 画像プロンプトの詳細については、[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja#prompt-guide)
  と [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ja#imagen-prompt-guide) のプロンプト ガイドをご覧ください。
- 動画プロンプトの詳細については、[Veo プロンプト ガイド](https://ai.google.dev/gemini-api/docs/video?hl=ja#prompt-guide)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-10 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-10 UTC。"],[],[]]
