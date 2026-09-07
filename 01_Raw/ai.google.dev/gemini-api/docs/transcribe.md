---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=ko
fetched_at: 2026-09-07T05:48:09.051883+00:00
title: "\uc624\ub514\uc624 \uc2a4\ud06c\ub9bd\ud2b8 \uc791\uc131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 오디오 스크립트 작성

Gemini API는 Gemini 3.5 Transcribe 모델 (`gemini-3.5-transcribe`)을 사용하여 오디오 파일의 음성을 텍스트로 변환합니다. Gemini의 오디오 이해 기능을 기반으로 자동 언어 식별, 화자 분리, 단어 수준 타임스탬프, 맞춤 어휘 힌트를 사용하여 정확한 변환을 제공합니다. 또한 머뭇거림 삭제 및 스마트 서식 지정 기능이 포함된 [스마트 스크립트](#transcription-modes) 모드도 제공합니다.

오디오 파일을 텍스트로 변환하려면 오디오를 업로드하고 `gemini-3.5-transcribe`에 전달하세요.

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const audioFile = await client.files.upload({
  file: "path/to/sample.mp3",
  config: { mime_type: "audio/mp3" },
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
});

console.log(interaction.output_text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## 개요

Gemini 3.5 Transcribe는 음성 텍스트 변환 작업에 최적화되어 있습니다. 다양한 억양, 배경 소음, 다국어 대화를 처리합니다.

주요 기능은 다음과 같습니다.

- **자동 음성 인식 (ASR):** [85개 이상의 언어](#supported-languages)를 자동으로 감지합니다. 수동 구성 없이 문장 내 및 문장 간 코드 전환을 처리합니다.
- **맞춤 어휘:** 최대 1, 000개의 구문을 전달하여 도메인별 용어, 약어,고유명사에 대한 인식을 편향시킵니다.
- **화자 분리:** 여러 화자를 구분하고 발화된 세그먼트를 고유한 라벨에 속성으로 지정합니다.
- **단어 수준 타임스탬프:** 인식된 각 단어의 정확한 시작 및 종료 타임스탬프를 생성합니다.
- **스마트 스크립트:** 유창하지 않은 부분, 추임새, 반복을 정리하고 구조화된 서식을 적용합니다.
- **형식 지정 및 정규화:** 대문자, 구두점, 역 텍스트 정규화(예: '2천6백만 달러'를 '2, 600만 달러'로 변환)를 적용합니다.

오디오 콘텐츠에 대한 일반적인 오디오 추론 또는 질의 응답에는 [오디오 이해](https://ai.google.dev/gemini-api/docs/audio?hl=ko)를 사용하세요. 텍스트 음성 변환 오디오 합성에는 [텍스트 음성 변환](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)을 사용합니다.

## 언어 감지 및 힌트

기본적으로 모델은 음성 언어를 자동으로 감지합니다. 화자가 코드 전환을 하면 언어를 동적으로 전환합니다.

자동 감지를 사용하려면 `language_codes`를 생략하거나 빈 목록을 제공하세요.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "language_codes": [],
        }
    },
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      language_codes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "language_codes": []
      }
    }
  }'
```

언어를 미리 알고 있는 경우 `language_codes`에 BCP-47 언어 코드를 지정하여 전사 정확도를 높이세요 ([지원되는 언어](#supported-languages) 참고).

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### 자바스크립트

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## 커스텀 어휘

음성 모델이 흔하지 않은 단어, 전문 용어, 브랜드 이름 또는 고유 명사를 인식하도록 조정할 수 있습니다. `custom_vocabulary` 배열에 최대 1,000개의 용어를 제공합니다 (최상의 결과는 일반적으로 최대 100개의 용어로 달성됨).

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
        }
    },
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      custom_vocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## 화자 분할

화자 분할은 녹음 파일에서 서로 다른 음성을 식별하고 각 세그먼트에 `spk_1` 또는 `spk_2`와 같은 화자 식별자로 태그를 지정합니다. 최대 8명의 화자가 지원됩니다 (3명 이상의 화자에 대한 속성은 실험적임).

`mode` 내에서 `diarization_mode`를 구성하여 분할을 사용 설정합니다.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "diarization_mode": "speaker",
            },
        }
    },
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        diarization_mode: "speaker",
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "diarization_mode": "speaker"
        }
      }
    }
  }'
```

## 단어 수준 타임스탬프

단어 수준 타임스탬프는 오디오 스트림에서 인식된 모든 단어의 정확한 시작 및 종료 오프셋을 제공합니다.

`mode` 내에서 `timestamp_granularities`를 구성하여 타임스탬프를 사용 설정합니다.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "timestamp_granularities": ["word"],
            },
        }
    },
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        timestamp_granularities: ["word"],
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "timestamp_granularities": ["word"]
        }
      }
    }
  }'
```

`mode`에서 `diarization_mode`과 `timestamp_granularities`을 결합하여 화자 라벨과 단어 타임스탬프를 모두 수신할 수 있습니다.

### Python

```
generation_config = {
    "transcription_config": {
        "custom_vocabulary": ["Gemini"],
        "mode": {
            "type": "verbatim",
            "diarization_mode": "speaker",
            "timestamp_granularities": ["word"],
        },
    }
}
```

### 자바스크립트

```
const generationConfig = {
  transcription_config: {
    custom_vocabulary: ["Gemini"],
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "custom_vocabulary": ["Gemini"],
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## 스크립트 작성 모드

Gemini 3.5 Transcribe는 `mode` 파라미터를 통해 두 가지 스크립트 모드를 지원합니다.

- **`verbatim` (기본값)**: 말한 모든 내용을 단어별로 정확하게 기록하며, 원시 필러 단어 ('음', '어', '그', '알잖아'), 반복, 일시중지, 잘못된 시작을 보존합니다. 타임스탬프와 화자 분할은 이 모드 (`{"type": "verbatim", ...}`) 내에서 구성됩니다.
- **`smart` (스마트 스크립트)**: 지능형 후처리를 적용하여 읽기용 스크립트를 최적화합니다.
  - **말더듬기 제거**: 대화형 필러 단어, 말더듬기, 잘못된 시작을 제거합니다.
  - **인라인 자체 수정**: 말한 수정사항을 직접 해결합니다 (예:*'화요일에 만나자. 아니, 수요일 2시에 만나자'*가 *'수요일 오후 2시에 만나자'*가 됨).
  - **자동 구조화된 형식 지정**: 음성으로 말한 생각을 단락, 번호 매기기 목록, 글머리 기호, 형식화된 날짜, 통화, 숫자로 자동 구조화합니다.
  - **문법 정리**: 자연스러운 구두점, 문장 대소문자, 흐름을 적용합니다.

| 음성 오디오 | `verbatim` 출력 | `smart` (스마트 스크립트) 출력 |
| --- | --- | --- |
| '음, 회의에는 앨리스를 초대해야 할 것 같아. 아니, 밥과 캐롤을 초대해야 해.' | '음, 회의에는 앨리스를 초대해야 할 것 같아. 아니, 밥과 캐롤을 초대해야 해.' | '회의에 김민수와 이수진을 초대하는 게 좋을 것 같아.' |
| 'First item review budget second item finalize timeline third item send recap'(첫 번째 항목 예산 검토, 두 번째 항목 일정 확정, 세 번째 항목 요약 보내기) | 'first item review budget second item finalize timeline third item send recap'(첫 번째 항목 예산 검토, 두 번째 항목 타임라인 확정, 세 번째 항목 요약 보내기) | '1. 예산 검토 2. 타임라인을 마무리합니다. 3. 요약 보내기' |

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": "smart",
        }
    },
)
print(interaction.output_text)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: "smart",
    },
  },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": "smart"
      }
    }
  }'
```

## 스크립트 출력 파싱

전체 스크립트 텍스트가 `interaction.output_text`에 반환됩니다.

`timestamp_granularities` 또는 `diarization_mode`가 사용 설정되면 API는 상호작용 콘텐츠에 연결된 자세한 단어 수준 주석도 반환합니다.

단어 타임스탬프와 화자 전환을 추출하고 반복하는 방법은 다음과 같습니다.

### Python

```
def extract_word_annotations(interaction):
    words = []
    for step in getattr(interaction, "steps", []) or []:
        for content in getattr(step, "content", []) or []:
            for annotation in getattr(content, "annotations", []) or []:
                if getattr(annotation, "type", None) == "word_info":
                    words.append(annotation)
    return words

words = extract_word_annotations(interaction)

for w in words:
    speaker = f"[{w.speaker}] " if getattr(w, "speaker", None) else ""
    start = getattr(w, "start_offset", "")
    end = getattr(w, "end_offset", "")
    timing = f"({start} -> {end}) " if start and end else ""
    print(f"{speaker}{timing}{w.text}")
```

### 자바스크립트

```
function extractWordAnnotations(interaction) {
  const words = [];
  for (const step of interaction.steps ?? []) {
    for (const content of step.content ?? []) {
      for (const annotation of content.annotations ?? []) {
        if (annotation.type === "word_info") {
          words.push(annotation);
        }
      }
    }
  }
  return words;
}

const words = extractWordAnnotations(interaction);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.start_offset && w.end_offset) ? `(${w.start_offset} -> ${w.end_offset}) ` : "";
  console.log(`${speaker}${timing}${w.text}`);
}
```

### REST

```
{
  "id": "interactions/abc123xyz",
  "status": "completed",
  "steps": [
    {
      "id": "step_001",
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Hello world",
          "annotations": [
            {
              "type": "word_info",
              "text": "Hello",
              "speaker": "spk_1",
              "start_offset": "0.100s",
              "end_offset": "0.450s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.850s"
            }
          ]
        }
      ]
    }
  ]
}
```

## 지원 언어

Gemini 3.5 Transcribe에서 지원되는 언어와 BCP-47 언어 코드는 다음과 같습니다.

| 언어 | BCP-47 코드 | 언어 | BCP-47 코드 |
| --- | --- | --- | --- |
| 아프리칸스어 | `af-ZA` | 일본어 | `ja-JP` |
| 암하라어 | `am-ET` | 자바어 | `jv-ID` |
| 아랍어(이집트) | `ar-EG` | Kabuverdianu | `kea-CV` |
| 아르메니아어 | `hy-AM` | 칸나다어 | `kn-IN` |
| 아삼어 | `as-IN` | 카자흐어 | `kk-KZ` |
| 아제르바이잔어 | `az-AZ` | 한국어 | `ko-KR` |
| 벨라루스어 | `be-BY` | 키르기스어 | `ky-KG` |
| 벵골어(방글라데시) | `bn-BD` | 라트비아어 | `lv-LV` |
| 벵골어(인도) | `bn-IN` | 링갈라어 | `ln-CD` |
| 보스니아어 | `bs-BA` | 리투아니아어 | `lt-LT` |
| 불가리아어 | `bg-BG` | 마케도니아어 | `mk-MK` |
| 불가리아어 (아로마어) | `rup-BG` | 말레이어 | `ms-MY` |
| 버마어 | `my-MM` | 말라얄람어 | `ml-IN` |
| 광둥어 (번체) | `yue-Hant-HK` | 몰타어 | `mt-MT` |
| 카탈로니아어 | `ca-ES` | 중국어 (간체) | `cmn-Hans-CN` |
| 세부아노어 | `ceb` | 마라타어 | `mr-IN` |
| 표준 크메르어 | `km-KH` | 몽골어 | `mn-MN` |
| 크로아티아어 | `hr-HR` | 네팔어 | `ne-NP` |
| 체코어 | `cs-CZ` | 노르웨이어 | `nb-NO` |
| 덴마크어 | `da-DK` | 오리야어 | `or-IN` |
| 네덜란드어 | `nl-NL` | 폴란드어 | `pl-PL` |
| 영어(영국) | `en-GB` | 포르투갈어(브라질) | `pt-BR` |
| 영어(인도) | `en-IN` | 포르투갈어(포르투갈) | `pt-PT` |
| 영어(미국) | `en-US` | 펀자브어 | `pa-IN` |
| 에스토니아어 | `et-EE` | 펀자브어 (구르무키 문자) | `pa-Guru-IN` |
| 페르시아어 | `fa-IR` | 루마니아어 | `ro-RO` |
| 필리핀어 | `fil-PH` | 러시아어 | `ru-RU` |
| 핀란드어 | `fi-FI` | 세르비아어 | `sr-RS` |
| 프랑스어 | `fr-FR` | 신디어 (아랍 문자) | `sd-Arab-IN` |
| 갈리시아어 | `gl-ES` | 슬로바키아어 | `sk-SK` |
| 조지아어 | `ka-GE` | 슬로베니아어 | `sl-SI` |
| 독일어 | `de-DE` | 스페인어(라틴 아메리카) | `es-419` |
| 그리스어 | `el-GR` | 스페인어(미국) | `es-US` |
| 구자라트어 | `gu-IN` | 스와힐리어(케냐) | `sw-KE` |
| 하우사어 | `ha-NG` | 스웨덴어 | `sv-SE` |
| 히브리어 | `he-IL` | 타지크어 | `tg-TJ` |
| 힌디어 | `hi-IN` | 텔루구어 | `te-IN` |
| 헝가리어 | `hu-HU` | 태국어 | `th-TH` |
| 아이슬란드어 | `is-IS` | 튀르키예어 | `tr-TR` |
| 인도 영어 | `en-IN` | 우크라이나어 | `uk-UA` |
| 인도네시아어 | `id-ID` | 우즈베크어 | `uz-UZ` |
| 이탈리아어 | `it-IT` | 베트남어 | `vi-VN` |

## 지원되는 오디오 형식

Gemini 3.5 Transcribe는 다음 오디오 형식 MIME 유형을 지원합니다.

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

지원되는 MIME 유형 및 매개변수 스키마의 전체 목록은 [Interactions API 참조](https://ai.google.dev/api/interactions-api?hl=ko#Resource:Content)를 참고하세요.

## 파라미터 참조

`generation_config`에서 `transcription_config` 객체 내 필드를 설정하여 트랜스크립션을 구성합니다.

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `language_codes` | 문자열 배열 | BCP-47 언어 코드 (예: `["en-US"]`)입니다. 생략되거나 비어 있는 경우 (`[]`) 모델이 언어를 자동으로 감지하고 코드 전환을 처리합니다. |
| `custom_vocabulary` | 문자열 배열 | 음성 인식을 편향시킬 수 있는 최대 1,000개의 맞춤 용어, 약어 또는 고유 이름 |
| `mode` | 객체 또는 문자열 | 스크립트 작성 모드 구성입니다. `"smart"` 또는 있는 그대로 모드 객체 (`{"type": "verbatim", ...}`)를 허용합니다. 기본값은 있는 그대로 전사입니다. |
| `mode.type` | 문자열 | *(있는 그대로 모드만 해당)* 모드 식별자입니다. 항상 `"verbatim"`로 설정됩니다. |
| `mode.timestamp_granularities` | 문자열 배열 | *(직접 인용 모드만 해당)* 반환할 타임스탬프의 단위입니다. 단어 시작 및 종료 오프셋을 사용 설정하려면 `["word"]`를 전달합니다. |
| `mode.diarization_mode` | 문자열 | *(직접 인용 모드만 해당)* 화자 분리 모드입니다. `"speaker"`를 전달하여 명확한 발화자를 식별하고 라벨을 지정합니다. |

## 권장사항

- **깔끔한 오디오 제공:** 오디오 녹음에서 음성 분리가 명확하고 심각한 클리핑이 없는지 확인합니다.
- **언어를 알고 있는 경우 언어 힌트 제공:** 오디오 언어를 미리 알고 있는 경우 `language_codes`를 지정하여 정확도를 극대화하세요.
- **타겟 맞춤 어휘:** 일반적인 일상 단어 대신 `custom_vocabulary`에 고유한 도메인 용어, 브랜드 이름 또는 고유명사만 포함합니다.
- **큰 녹음 파일에 Files API 사용:** 몇 초보다 긴 파일의 경우 `client.files.upload`를 사용하여 파일을 업로드하고 반환된 파일 URI를 모델에 전달합니다.

## 제한사항

- **오디오 길이:** 표준 단항 요청은 최대 1시간 길이의 오디오 파일을 지원합니다. 화자 분할 또는 단어 수준 타임스탬프와 같은 기능을 사용 설정하면 오디오 처리가 30분으로 제한됩니다.
- **단어 수준 타임스탬프:** 단어 수준 타임스탬프를 사용 설정하면 전체 변환 텍스트의 정확도가 저하될 수 있습니다.
- **화자 분할:** 화자 분할은 최대 8명의 화자를 지원합니다. 3명 이상의 화자에 대한 화자 속성은 실험 단계에 있습니다.
- **맞춤 어휘:** `custom_vocabulary`에 최대 1,000개의 단어를 제공할 수 있지만 일반적으로 최대 100개의 단어로 최상의 결과를 얻을 수 있습니다.
- **모드 호환성:** 스마트 스크립트 (`"smart"`)는 `timestamp_granularities` 또는 `diarization_mode`와 함께 사용할 수 없습니다.

## 다음 단계

- Live API를 사용하여 [실시간 스크립트 가이드](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=ko)로 실시간 오디오를 스트리밍합니다.
- [오디오 이해](https://ai.google.dev/gemini-api/docs/audio?hl=ko)를 살펴보고 오디오 콘텐츠를 분석, 요약하거나 쿼리하세요.
- [Text-to-speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)를 사용하여 텍스트에서 오디오를 합성하는 방법을 알아봅니다.
- 모델 가격 및 토큰 한도는 [가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#gemini-3.5-transcribe)를 확인하세요.
- 미디어 파일 업로드 및 관리에 관한 자세한 내용은 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko) 가이드를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-08-28(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-08-28(UTC)"],[],[]]
