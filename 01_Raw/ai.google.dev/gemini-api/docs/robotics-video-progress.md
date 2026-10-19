---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja
fetched_at: 2026-10-19T05:45:06.483203+00:00
title: "\u52d5\u753b\u7406\u89e3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 動画理解

Gemini Robotics-ER 2 は、次の 2 つの機能を使用して、継続的な動画フィードからタスクの進行状況を追跡できます。

- モーメント検出: キーイベントが発生した正確なタイムスタンプを特定します。
- 進行状況の分類: 各動画を 5 つの完了率の範囲（0 ～ 20%、20 ～ 40%、40 ～ 60%、60 ～ 80%、80 ～ 100%）のいずれかに割り当てます。

## モーメントの検出

モーメント検出は、重大なイベントが発生した正確な動画フレーム（カップが満杯になったときや、結び目が結ばれたときなど）を特定します。ロボットはこれを使用して、成功の確認、ステップの順序付け、修正のトリガーを行います。

次のプロンプトの例では、動画内の特定のタスクの完了時点を識別するようモデルに指示しています。

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

次の図は、モデルがタスク完了のタイムスタンプを特定している、モーメント検出動画のフレームの例を示しています。

![タイムスタンプ オーバーレイ付きのモーメント検出出力が表示された動画フレームの例](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=ja)

## 進行状況の分類

進行状況の分類では、動画が 5 つの完了範囲（0 ～ 20%、20 ～ 40%、40 ～ 60%、60 ～ 80%、80 ～ 100%）のいずれかに割り当てられます。これにより、ロボットはリアルタイムで状況を認識し、ワークフロー全体を再起動することなく、アクションを調整したり、失敗したステップを再試行したりできます。

次のプロンプトの例では、動画の現在の進行状況レベルを分類するようにモデルに求めています。

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

次の図は、進行状況分類動画のフレームの例を示しています。モデルは進行状況の範囲を割り当てています。

![進行状況の分類出力と進行状況の範囲ラベルを示す動画フレームの例](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=ja)

## 例

マルチステップ タスク トラッキングを含む実行可能な例については、[ロボティクス クックブック](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)をご覧ください。

## 次のステップ

- [ロボット工学用の Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) - リアルタイムの双方向ストリーミング。
- [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja) - 空間推論を伴う長期的なタスク。
- [Gemini Robotics ER の概要](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ja) - モデルの比較と機能。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-08 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-08 UTC。"],[],[]]
