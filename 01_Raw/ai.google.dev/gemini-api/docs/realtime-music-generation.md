---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ja
fetched_at: 2026-07-27T04:49:20.780239+00:00
title: "Lyria RealTime \u3092\u4f7f\u7528\u3057\u305f\u30ea\u30a2\u30eb\u30bf\u30a4\u30e0\u306e\u97f3\u697d\u751f\u6210 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Lyria RealTime を使用したリアルタイムの音楽生成

Gemini API は
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=ja)を使用して、最先端のリアルタイム ストリーミング音楽
生成モデルへのアクセスを提供します。デベロッパーは、ユーザーがインタラクティブに楽器の音楽を作成、継続的に操作、演奏できるアプリケーションを構築できます。

[Lyria RealTime の音楽生成では、WebSocket を使用して、永続的な双方向の
低レイテンシ ストリーミング接続を使用します。](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

[[Lyria RealTime を使用して構築できるものを体験するには、Prompt DJ アプリまたは MIDI DJ アプリを使用して AI Studio
で試してください。](https://aistudio.google.com/apps/bundled/promptdj?hl=ja)](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=ja)

## 音楽の生成と操作

Lyria RealTime は、[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)
を介して Websocket を使用してモデルとのリアルタイム通信を維持するという点で、Live API と同様に機能します。

次のコードは、音楽を生成する方法を示しています。

### Python

この例では、`client.aio.live.music.connect()` を使用して Lyria RealTime セッションを初期化し、`session.set_weighted_prompts()` で最初のプロンプトを送信します。また、`session.set_music_generation_config` を使用して初期構成を設定し、`session.play()` を使用して音楽生成を開始し、受信した音声チャンクを処理するように `receive_audio()` を設定します。

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

この例では、`client.live.music.connect()` を使用して Lyria RealTime セッションを初期化し、`session.setWeightedPrompts()` で最初のプロンプトを送信します。また、`session.setMusicGenerationConfig` を使用して初期構成を設定し、`session.play()` を使用して音楽生成を開始し、受信した音声チャンクを処理するように `onMessage` コールバックを設定します。

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

`session.play()`、`session.pause()`、`session.stop()`、`session.reset_context()` を使用して、セッションを開始、一時停止、停止、リセットできます。

## リアルタイムで音楽を操作する

プロンプトを送信し、生成パラメータをリアルタイムで更新することで、音楽生成をリアルタイムで操作できます。

### Lyria RealTime にプロンプトを設定する

ストリームがアクティブな間は、新しい `WeightedPrompt` メッセージをいつでも送信して、生成された音楽を変更できます。モデルは、新しい入力に基づいてスムーズに移行します。

プロンプトは、`text`（実際のプロンプト）と `weight` を含む適切な形式にする必要があります。`weight` には `0` 以外の任意の値を指定できます。通常は `1.0` から始めることをおすすめします。

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

プロンプトを大幅に変更すると、モデルの移行が少し急になる可能性があるため、中間的な重み値をモデルに送信して、クロスフェードを実装することをおすすめします。

### 構成を更新する

音楽生成パラメータをリアルタイムで更新することで、音楽生成を操作できます。パラメータを更新するだけでなく、構成全体を設定する必要があります。そうしないと、他のフィールドがデフォルト値にリセットされます。

bpm またはスケールを更新すると、モデルが大幅に変更されるため、`reset_context()` を使用してコンテキストをリセットし、新しい構成を考慮に入れるようにモデルに指示する必要があります。ストリームは停止しませんが、移行は困難になります。他のパラメータでは必要ありません。

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## Lyria RealTime のプロンプト ガイド

Lyria RealTime にプロンプトを設定するために使用できるプロンプトの例を次に示します。

- 楽器: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- 音楽ジャンル: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- ムード/説明: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

これらはほんの一例です。Lyria RealTime では、他にもさまざまなことができます。独自のプロンプトを試してみてください。

## ベスト プラクティス

- クライアント アプリケーションは、スムーズな再生を確保するために、堅牢な音声バッファリングを実装する必要があります。これにより、ネットワーク ジッターと生成レイテンシのわずかな変動に対応できます。
- 効果的なプロンプト:
  - わかりやすいラベルを付けます。ムード、ジャンル、楽器を表す形容詞を使用します。
  - 反復処理を行い、徐々に操作します。プロンプトを完全に変更するのではなく、要素を追加または変更して、音楽をよりスムーズに変化させてみてください。
  - `WeightedPrompt` の重みを調整して、新しいプロンプトが進行中の生成に与える影響の強さを調整します。

## 詳細な技術情報

このセクションでは、Lyria RealTime の音楽生成の使用方法について詳しく説明します。

### 仕様

- 出力形式: RAW 16 ビット PCM 音声
- サンプルレート: 48 kHz
- チャンネル数: 2（ステレオ）

### コントロール

音楽生成は、次のものを含むメッセージを送信することで、リアルタイムで影響を受ける可能性があります。

- `WeightedPrompt`: 音楽のアイデア、ジャンル、楽器、ムード、特徴を表すテキスト文字列。複数のプロンプトを指定して、影響をブレンドすることもできます。Lyria RealTime に最適なプロンプトを設定する方法について詳しくは、[上記](#steer-music)をご覧ください。
- `MusicGenerationConfig`: 音楽生成プロセスの構成。出力音声の特性に影響します。パラメータは次のとおりです。
  - `guidance`:（浮動小数点）範囲: `[0.0, 6.0]`。デフォルト: `4.0`。
    モデルがプロンプトにどの程度厳密に従うかを制御します。ガイダンスが高いほど、プロンプトへの準拠度は向上しますが、移行がより急になります。
  - `bpm`:（整数）範囲: `[60, 200]`。
    生成された音楽に必要な 1 分あたりのビート数を設定します。モデルが新しい bpm を考慮に入れるには、コンテキストを停止/再生またはリセットする必要があります。
  - `density`:（浮動小数点）範囲: `[0.0, 1.0]`。
    音符/音の密度を制御します。値が小さいほど音楽がまばらになり、値が大きいほど音楽が「忙しく」なります。
  - `brightness`:（浮動小数点）範囲: `[0.0, 1.0]`。
    音質を調整します。値が高いほど、音声が「明るく」なり、一般的に高周波が強調されます。
  - `scale`:（列挙型）生成の音階（キーとモード）を設定します。SDK で提供される
    [`Scale` 列挙値](#scale-enum)を使用します。モデルが新しいスケールを考慮に入れるには、コンテキストを停止/再生またはリセットする必要があります。
  - `mute_bass`:（ブール値）デフォルト: `False`。
    モデルが出力の低音を減らすかどうかを制御します。
  - `mute_drums`:（ブール値）デフォルト: `False`。
    モデルが出力のドラムを減らすかどうかを制御します。
  - `only_bass_and_drums`:（ブール値）デフォルト: `False`。
    低音とドラムのみを出力するようにモデルを操作します。
  - `music_generation_mode`:（列挙型）音楽の `QUALITY`（デフォルト値）または `DIVERSITY` に焦点を当てるかどうかをモデルに示します。`VOCALIZATION` に設定して、モデルが別の楽器として発声（新しいプロンプトとして追加）を生成できるようにすることもできます。
- `PlaybackControl`: 再生、一時停止、停止、コンテキストのリセットなど、再生の側面を制御するコマンド。

`bpm`、`density`、`brightness`、`scale` に値を指定しない場合、モデルは最初のプロンプトに基づいて最適な値を決定します。

`temperature`（0.0 ～ 3.0、デフォルト 1.1）、`top_k`（1 ～ 1,000、デフォルト 40）、`seed`（0 ～ 2,147,483,647、デフォルトでランダムに選択）などの従来のパラメータも、`MusicGenerationConfig` でカスタマイズできます。

#### スケール列挙値

モデルが受け入れられるスケール値は次のとおりです。

| 列挙値 | スケール / キー |
| --- | --- |
| `C_MAJOR_A_MINOR` | ハ長調 / イ短調 |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | 変ニ長調 / 変ロ短調 |
| `D_MAJOR_B_MINOR` | ニ長調 / ロ短調 |
| `E_FLAT_MAJOR_C_MINOR` | 変ホ長調 / ハ短調 |
| `E_MAJOR_D_FLAT_MINOR` | ホ長調 / 嬰ハ短調/変ニ短調 |
| `F_MAJOR_D_MINOR` | ヘ長調 / ニ短調 |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | 変ト長調 / 変ホ短調 |
| `G_MAJOR_E_MINOR` | ト長調 / ホ短調 |
| `A_FLAT_MAJOR_F_MINOR` | 変イ長調 / ヘ短調 |
| `A_MAJOR_G_FLAT_MINOR` | イ長調 / 嬰ヘ短調/変ト短調 |
| `B_FLAT_MAJOR_G_MINOR` | 変ロ長調 / ト短調 |
| `B_MAJOR_A_FLAT_MINOR` | ロ長調 / 嬰ト短調/変イ短調 |
| `SCALE_UNSPECIFIED` | デフォルト / モデルが決定 |

モデルは演奏される音符をガイドできますが、相対キーを区別しません。したがって、各列挙型は相対的な長調と短調の両方に対応します。たとえば、`C_MAJOR_A_MINOR` はピアノのすべての白鍵に対応し、`F_MAJOR_D_MINOR` は変ロ以外のすべての白鍵に対応します。

### 制限事項

- インストゥルメンタルのみ: モデルはインストゥルメンタル音楽のみを生成します。
- 安全性: プロンプトは安全フィルタによってチェックされます。フィルタをトリガーするプロンプトは無視され、その場合は出力の `filtered_prompt` フィールドに説明が書き込まれます。
- [ウォーターマーク: 出力音声には、責任ある AI の原則に従って識別用のウォーターマークが常に付加されます。](https://ai.google/responsibility/principles/?hl=ja)

## 次のステップ

- [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=ja) でフルソングとボーカル トラックを生成する。
- 音楽の代わりに、
  [TTS モデル](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)を使用して複数話者の会話を生成する方法を学習する。
- [[画像や動画を生成する方法を確認する。](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)](https://ai.google.dev/gemini-api/docs/video?hl=ja)
- 音楽や音声を生成する代わりに、Gemini が音声ファイルを
  [理解する](https://ai.google.dev/gemini-api/docs/audio?hl=ja)方法を確認する。
- [Live API を使用して Gemini とリアルタイムで会話する。](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)

その他のコードサンプルとチュートリアルについては、[クックブック](https://github.com/google-gemini/cookbook)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-16 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-16 UTC。"],[],[]]
