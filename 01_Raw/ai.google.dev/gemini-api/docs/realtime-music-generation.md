---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ko
fetched_at: 2026-05-05T13:09:30.890019+00:00
title: "Lyria RealTime\uc744 \uc0ac\uc6a9\ud55c \uc2e4\uc2dc\uac04 \uc74c\uc545 \uc0dd\uc131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

- [홈](https://ai.google.dev/gemini-api/docs/홈)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [문서](https://ai.google.dev/gemini-api/docs/문서)

의견 보내기

# Lyria RealTime을 사용한 실시간 음악 생성

[Lyria RealTime](https://ai.google.dev/gemini-api/docs/Lyria RealTime)을 사용하는 Gemini API는 최첨단의 실시간 스트리밍 음악
생성 모델에 대한 액세스를 제공합니다. 이를 통해 개발자는 사용자가 악기 음악을 대화형으로 만들고, 지속적으로 조작하고, 연주할 수 있는 애플리케이션을 빌드할 수 있습니다.

Lyria RealTime 음악 생성은 WebSocket을 사용하여 지속적인 양방향,
저지연 스트리밍 연결을 사용합니다.
[WebSocket](https://ai.google.dev/gemini-api/docs/WebSocket).

[[Lyria RealTime을 사용하여 빌드할 수 있는 기능을 경험하려면 프롬프트 DJ 또는 MIDI DJ 앱을 사용하여 AI Studio
에서 사용해 보세요.](https://ai.google.dev/gemini-api/docs/[Lyria RealTime을 사용하여 빌드할 수 있는 기능을 경험하려면 프롬프트 DJ 또는 MIDI DJ 앱을 사용하여 AI Studio에서 사용해 보세요.)](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=ko)

## 음악 생성 및 제어

Lyria RealTime은 [Live API](https://ai.google.dev/gemini-api/docs/Live API)
와 유사하게 작동하며, WebSocket을 사용하여 모델과의 실시간 통신을 유지합니다.

다음 코드는 음악을 생성하는 방법을 보여줍니다.

### Python

이 예에서는 `client.aio.live.music.connect()`를 사용하여 Lyria RealTime 세션을 초기화한 다음, `session.set_weighted_prompts()`를 사용하여 초기 프롬프트를 `session.set_music_generation_config`를 사용하는 초기 구성과 함께 전송하고, `session.play()`를 사용하여 음악 생성을 시작하고, 수신하는 오디오 청크를 처리하도록 `receive_audio()`를 설정합니다.

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

이 예에서는 `client.live.music.connect()`를 사용하여 Lyria RealTime 세션을 초기화한 다음, `session.setWeightedPrompts()`를 사용하여 초기 프롬프트를 `session.setMusicGenerationConfig`를 사용하는 초기 구성과 함께 전송하고, `session.play()`를 사용하여 음악 생성을 시작하고, 수신하는 오디오 청크를 처리하도록 `onMessage` 콜백을 설정합니다.

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

그런 다음 `session.play()`, `session.pause()`, `session.stop()` 및 `session.reset_context()`를 사용하여 세션을 시작, 일시중지, 중지 또는 재설정할 수 있습니다.

## 실시간으로 음악 조작

프롬프트를 전송하고 생성 매개변수를 실시간으로 업데이트하여 음악 생성을 실시간으로 조작할 수 있습니다.

### Lyria RealTime 프롬프트

스트림이 활성 상태인 동안 언제든지 새 `WeightedPrompt` 메시지를 전송하여 생성된 음악을 변경할 수 있습니다. 모델은 새 입력에 따라 원활하게 전환됩니다.

프롬프트는 `text` (실제 프롬프트) 및 `weight`를 사용하여 올바른 형식을 따라야 합니다. `weight`는 `0`을 제외한 모든 값을 사용할 수 있습니다. `1.0`
이 일반적으로 좋은 시작점입니다.

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

프롬프트를 크게 변경하면 모델 전환이 다소 갑작스러울 수 있으므로 중간 가중치 값을 모델에 전송하여 일종의 크로스페이딩을 구현하는 것이 좋습니다.

### 구성 업데이트

음악 생성 매개변수를 실시간으로 업데이트하여 음악 생성을 조작할 수 있습니다. 매개변수를 업데이트할 수만 있는 것이 아니라 전체 구성을 설정해야 합니다. 그렇지 않으면 다른 필드가 기본값으로 재설정됩니다.

bpm 또는 스케일을 업데이트하는 것은 모델에 큰 변화이므로 새 구성을 고려하도록 `reset_context()`를 사용하여 컨텍스트를 재설정하도록 모델에 지시해야 합니다. 스트림이 중지되지는 않지만 전환이 어려울 수 있습니다. 다른 매개변수에는 이 작업을 할 필요가 없습니다.

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

## Lyria RealTime 프롬프트 가이드

다음은 Lyria RealTime에 프롬프트를 작성하는 데 사용할 수 있는 프롬프트의 전체 목록입니다.

- 악기: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
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
- 음악 장르: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
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
- 분위기/설명: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

이러한 예 외에도 Lyria RealTime은 훨씬 더 많은 작업을 할 수 있습니다. 자체 프롬프트를 실험해 보세요.

## 권장사항

- 클라이언트 애플리케이션은 원활한 재생을 보장하기 위해 강력한 오디오 버퍼링을 구현해야 합니다. 이렇게 하면 네트워크 지터와 생성 지연 시간의 약간의 변동을 고려하는 데 도움이 됩니다.
- 효과적인 프롬프트 작성:
  - 자세히 설명합니다. 분위기, 장르, 악기를 설명하는 형용사를 사용합니다.
  - 점진적으로 반복하고 조작합니다. 프롬프트를 완전히 변경하는 대신 요소를 추가하거나 수정하여 음악을 더 원활하게 변형해 보세요.
  - `WeightedPrompt`의 가중치를 실험하여 새 프롬프트가 진행 중인 생성에 미치는 영향을 조정합니다.

## 기술 세부정보

이 섹션에서는 Lyria RealTime 음악 생성 사용 방법에 관한 세부정보를 설명합니다.

### 사양

- 출력 형식: 원시 16비트 PCM 오디오
- 샘플링 레이트: 48kHz
- 채널: 2 (스테레오)

### 컨트롤

음악 생성은 다음을 포함하는 메시지를 전송하여 실시간으로 영향을 받을 수 있습니다.

- `WeightedPrompt`: 음악적 아이디어, 장르, 악기, 분위기 또는 특징을 설명하는 텍스트 문자열입니다. 영향을 혼합하기 위해 여러 프롬프트가 제공될 수 있습니다. Lyria RealTime에 프롬프트를 작성하는 가장 좋은 방법에 관한 자세한 내용은 [위](https://ai.google.dev/gemini-api/docs/위)를 참고하세요.
- `MusicGenerationConfig`: 음악 생성 프로세스의 구성으로, 출력 오디오의 특징에 영향을 미칩니다. 매개변수는 다음과 같습니다.
  - `guidance`: (float) 범위: `[0.0, 6.0]`. 기본값: `4.0`.
    모델이 프롬프트를 얼마나 엄격하게 따르는지 제어합니다. 안내 값이 높을수록 프롬프트 준수가 개선되지만 전환이 더 갑작스러워집니다.
  - `bpm`: (int) 범위: `[60, 200]`.
    생성된 음악에 원하는 분당 비트를 설정합니다. 모델이 새 bpm을 고려하도록 컨텍스트를 중지/재생하거나 재설정해야 합니다.
  - `density`: (float) 범위: `[0.0, 1.0]`.
    음악적 음표/사운드의 밀도를 제어합니다. 값이 낮을수록 음악이 더 희소해지고 값이 높을수록 '더 바쁜' 음악이 생성됩니다.
  - `brightness`: (float) 범위: `[0.0, 1.0]`.
    음색 품질을 조정합니다. 값이 높을수록 '더 밝은' 사운드 오디오가 생성되며 일반적으로 높은 주파수를 강조합니다.
  - `scale`: (Enum) 생성을 위한 음악적 스케일 (키 및 모드)을 설정합니다. SDK에서 제공하는
    [`Scale` enum 값을](https://ai.google.dev/gemini-api/docs/`Scale` enum 값을) 사용합니다. 모델이 새 스케일을 고려하도록 컨텍스트를 중지/재생하거나 재설정해야 합니다.
  - `mute_bass`: (bool) 기본값: `False`.
    모델이 출력의 베이스를 줄이는지 여부를 제어합니다.
  - `mute_drums`: (bool) 기본값: `False`.
    모델 출력이 출력의 드럼을 줄이는지 여부를 제어합니다.
  - `only_bass_and_drums`: (bool) 기본값: `False`.
    베이스와 드럼만 출력하도록 모델을 조작합니다.
  - `music_generation_mode`: (Enum) 모델에 음악의 `QUALITY` (기본값) 또는 `DIVERSITY`에 집중해야 하는지 나타냅니다. 모델이 보컬을 다른 악기로 생성하도록 `VOCALIZATION`으로 설정할 수도 있습니다 (새 프롬프트로 추가).
- `PlaybackControl`: 재생, 일시중지, 중지 또는 컨텍스트 재설정과 같은 재생 측면을 제어하는 명령어입니다.

`bpm`, `density`, `brightness`, `scale`의 경우 값이 제공되지 않으면 모델이 초기 프롬프트에 따라 가장 적합한 값을 결정합니다.

`temperature` (0.0~3.0, 기본값 1.1), `top_k`(1~1000, 기본값 40), `seed` (0~2,147,483,647, 기본적으로 무작위로 선택됨)와 같은 더 클래식한 매개변수도 `MusicGenerationConfig`에서 맞춤설정할 수 있습니다.

#### 스케일 enum 값

다음은 모델이 허용할 수 있는 모든 스케일 값입니다.

| enum 값 | 스케일 / 키 |
| --- | --- |
| `C_MAJOR_A_MINOR` | C 장조 / A 단조 |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | D♭ 장조 / B♭ 단조 |
| `D_MAJOR_B_MINOR` | D 장조 / B 단조 |
| `E_FLAT_MAJOR_C_MINOR` | E♭ 장조 / C 단조 |
| `E_MAJOR_D_FLAT_MINOR` | E 장조 / C♯/D♭ 단조 |
| `F_MAJOR_D_MINOR` | F 장조 / D 단조 |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ 장조 / E♭ 단조 |
| `G_MAJOR_E_MINOR` | G 장조 / E 단조 |
| `A_FLAT_MAJOR_F_MINOR` | A♭ 장조 / F 단조 |
| `A_MAJOR_G_FLAT_MINOR` | A 장조 / F♯/G♭ 단조 |
| `B_FLAT_MAJOR_G_MINOR` | B♭ 장조 / G 단조 |
| `B_MAJOR_A_FLAT_MINOR` | B 장조 / G♯/A♭ 단조 |
| `SCALE_UNSPECIFIED` | 기본값 / 모델 결정 |

모델은 연주되는 음표를 안내할 수 있지만 상대 키를 구분하지는 않습니다. 따라서 각 enum은 상대 장조와 단조에 모두 해당합니다. 예를 들어 `C_MAJOR_A_MINOR`는 피아노의 모든 흰색 키에 해당하고 `F_MAJOR_D_MINOR`는 B♭을 제외한 모든 흰색 키에 해당합니다.

### 제한사항

- 연주곡만: 모델은 연주곡만 생성합니다.
- 안전: 프롬프트는 안전 필터로 확인됩니다. 필터를 트리거하는 프롬프트는 무시되며, 이 경우 출력의 `filtered_prompt` 필드에 설명이 작성됩니다.
- [워터마크: 출력 오디오는 항상 책임감 있는 AI](https://ai.google.dev/gemini-api/docs/워터마크: 출력 오디오는 항상 책임감 있는 AI) 원칙에 따라 식별을 위해 워터마크 처리됩니다.

## 다음 단계

- [Lyria 3](https://ai.google.dev/gemini-api/docs/Lyria 3)로 전체 노래와 보컬 트랙을 생성합니다.
- 음악 대신
  [TTS 모델](https://ai.google.dev/gemini-api/docs/TTS 모델)을 사용하여 다중 화자 대화를 생성하는 방법을 알아봅니다.
- [이미지](https://ai.google.dev/gemini-api/docs/이미지) 또는 [동영상](https://ai.google.dev/gemini-api/docs/동영상)을 생성하는 방법을 알아봅니다.
- 음악 또는 오디오를 생성하는 대신 Gemini가 오디오 파일을 이해하는 방법을 알아봅니다.
- [Live API](https://ai.google.dev/gemini-api/docs/Live API)를 사용하여 Gemini와 실시간으로 대화합니다.

[Cookbook](https://ai.google.dev/gemini-api/docs/Cookbook)에서 더 많은
코드 예와 가이드를 살펴보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0 라이선스)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://ai.google.dev/gemini-api/docs/Apache 2.0 라이선스)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://ai.google.dev/gemini-api/docs/Google Developers 사이트 정책)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?
