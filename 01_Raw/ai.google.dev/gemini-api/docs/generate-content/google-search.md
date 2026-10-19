---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=th
fetched_at: 2026-10-19T05:55:28.434472+00:00
title: "\u0e1e\u0e37\u0e49\u0e19\u0e10\u0e32\u0e19\u0e14\u0e49\u0e27\u0e22 Google Search \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# พื้นฐานด้วย Google Search

การเชื่อมต่อแหล่งข้อมูลกับ Google Search จะเชื่อมต่อโมเดล Gemini กับเนื้อหาเว็บแบบเรียลไทม์และจะใช้งานได้กับทุกภาษาที่มี ซึ่งจะช่วยให้ Gemini ให้คำตอบที่แม่นยำยิ่งขึ้นและอ้างอิงแหล่งข้อมูลที่ตรวจสอบได้แม้จะผ่านการตัดข้อมูลมาแล้ว

การเชื่อมต่อแหล่งข้อมูลจะช่วยให้คุณสร้างแอปพลิเคชันที่ทำสิ่งต่อไปนี้ได้

- **เพิ่มความแม่นยำของข้อเท็จจริง:** ลดการสร้างข้อมูลที่ไม่ถูกต้องของโมเดลโดยอิงคำตอบตามข้อมูลในโลกแห่งความเป็นจริง
- **เข้าถึงข้อมูลแบบเรียลไทม์:** ตอบคำถามเกี่ยวกับเหตุการณ์และหัวข้อล่าสุด
- **ระบุแหล่งที่มา:** สร้างความเชื่อมั่นให้ผู้ใช้ด้วยการแสดงแหล่งที่มาของข้อมูลที่โมเดลอ้าง

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

ดูข้อมูลเพิ่มเติมได้โดยลองใช้สมุดบันทึกเครื่องมือ [Search tool](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=th)

## วิธีการทำงานของการเชื่อมต่อแหล่งข้อมูลกับ Google Search

เมื่อคุณเปิดใช้เครื่องมือ `google_search` โมเดลจะจัดการเวิร์กโฟลว์ทั้งหมดของการค้นหา ประมวลผล และอ้างอิงข้อมูลโดยอัตโนมัติ

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=th)

1. **พรอมต์ของผู้ใช้:** แอปพลิเคชันของคุณส่งพรอมต์ของผู้ใช้ไปยัง Gemini API โดยเปิดใช้เครื่องมือ `google_search`
2. **การวิเคราะห์พรอมต์:** โมเดลจะวิเคราะห์พรอมต์และพิจารณาว่าการค้นหาใน Google Search จะช่วยปรับปรุงคำตอบได้หรือไม่
3. **Google Search:** หากจำเป็น โมเดลจะสร้างคำค้นหาอย่างน้อย 1 รายการและดำเนินการค้นหาโดยอัตโนมัติ
4. **การประมวลผลผลการค้นหา:** โมเดลจะประมวลผลผลการค้นหา สังเคราะห์ข้อมูล และกำหนดคำตอบ
5. **คำตอบที่เชื่อมต่อแหล่งข้อมูล:** API จะแสดงคำตอบสุดท้ายที่ใช้งานง่ายซึ่งเชื่อมต่อแหล่งข้อมูลกับผลการค้นหา คำตอบนี้ประกอบด้วยคำตอบที่เป็นข้อความของโมเดลและ `groundingMetadata` พร้อมคำค้นหา ผลลัพธ์จากเว็บ และการอ้างอิง

## ทำความเข้าใจคำตอบที่เชื่อมต่อแหล่งข้อมูล

เมื่อเชื่อมต่อแหล่งข้อมูลกับคำตอบได้สำเร็จ คำตอบจะมีช่อง `groundingMetadata` ข้อมูลที่มีโครงสร้างนี้มีความสำคัญอย่างยิ่งต่อการยืนยันข้อมูลที่อ้างและสร้างประสบการณ์การอ้างอิงที่สมบูรณ์ในแอปพลิเคชัน

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API จะแสดงข้อมูลต่อไปนี้พร้อมกับ `groundingMetadata`

- `webSearchQueries` : อาร์เรย์ของคำค้นหาที่ใช้ ซึ่งมีประโยชน์สำหรับการแก้ไขข้อบกพร่องและทำความเข้าใจกระบวนการให้เหตุผลของโมเดล
- `searchEntryPoint` : มี HTML และ CSS สำหรับแสดงคำแนะนำการค้นหาที่จำเป็น ข้อกำหนดการใช้งานทั้งหมดมีรายละเอียดอยู่ใน [ข้อกำหนดในการให้บริการ](https://ai.google.dev/gemini-api/terms?hl=th#grounding-with-google-search)
- `groundingChunks` : อาร์เรย์ของออบเจ็กต์ที่มีแหล่งที่มาของเว็บ (`uri` และ `title`)
- `groundingSupports` : อาร์เรย์ของ Chunk เพื่อเชื่อมต่อ `text` คำตอบของโมเดลกับแหล่งที่มาใน `groundingChunks` Chunk แต่ละรายการจะลิงก์ `segment` ข้อความ (กำหนดโดย `startIndex` และ `endIndex`) กับ `groundingChunkIndices` อย่างน้อย 1 รายการ ซึ่งเป็นกุญแจสำคัญในการสร้างการอ้างอิงในบรรทัด

นอกจากนี้ คุณยังใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Search ร่วมกับเครื่องมือบริบท [URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) เพื่อเชื่อมต่อแหล่งข้อมูลกับคำตอบทั้งในข้อมูลเว็บสาธารณะ
และ URL ที่เฉพาะเจาะจงที่คุณระบุได้ด้วย

## การระบุแหล่งที่มาด้วยการอ้างอิงในบรรทัด

API จะแสดงข้อมูลการอ้างอิงที่มีโครงสร้าง ซึ่งช่วยให้คุณควบคุมวิธีแสดงแหล่งที่มาในอินเทอร์เฟซผู้ใช้ได้อย่างสมบูรณ์ คุณสามารถใช้ช่อง `groundingSupports` และ `groundingChunks` เพื่อลิงก์คำกล่าวของโมเดลกับแหล่งที่มาโดยตรง ต่อไปนี้เป็นรูปแบบทั่วไปสำหรับการประมวลผลข้อมูลเมตาเพื่อสร้างคำตอบที่มีการอ้างอิงในบรรทัดที่คลิกได้

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

คำตอบใหม่ที่มีการอ้างอิงในบรรทัดจะมีลักษณะดังนี้

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## ราคา

เมื่อคุณใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Search ร่วมกับโมเดล Gemini 3 และโมเดลใหม่กว่า ระบบจะเรียกเก็บเงินจากโปรเจ็กต์ของคุณสำหรับคำค้นหา**แต่ละรายการ** ที่โมเดลตัดสินใจดำเนินการ
โมเดลการเรียกเก็บเงินต่อคำค้นหานี้รวมคำขอค้นหาฟรี 5,000 รายการต่อเดือนที่ใช้ร่วมกันในโมเดล Gemini 3 และโมเดลใหม่กว่าทั้งหมด จากนั้นจะมีค่าใช้จ่ายอยู่ที่ **$14 ต่อคำขอค้นหา 1,000 รายการ**

ตัวอย่างเช่น หากโมเดลตัดสินใจดำเนินการคำค้นหาหลายรายการเพื่อตอบ พรอมต์เดียว (เช่น การค้นหา `"UEFA Euro 2024 winner"` และ `"Spain vs
England Euro 2024 final score"` ภายใน การเรียก API เดียวกัน) ระบบจะนับเป็นการใช้งานเครื่องมือที่เรียกเก็บเงินได้สอง ครั้งสำหรับคำขอนั้น สำหรับการเรียกเก็บเงิน เราจะละเว้นคำค้นหาเว็บที่ว่างเปล่าเมื่อนับคำค้นหาที่ไม่ซ้ำกัน

เมื่อคุณใช้การเชื่อมต่อแหล่งข้อมูลกับ Search ร่วมกับโมเดล Gemini 2.5 หรือโมเดลเก่ากว่า ระบบจะเรียกเก็บเงินจากโปรเจ็กต์ของคุณต่อพรอมต์

ดูข้อมูลการกำหนดราคารายละเอียดได้ที่หน้า[การกำหนดราคา Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=th)

## โมเดลที่รองรับ

ดูความสามารถทั้งหมดได้ในหน้าภาพรวมของ[โมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)

| โมเดล | การเชื่อมต่อแหล่งข้อมูลกับ Google Search |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image Preview | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3 Pro Image Preview | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## การผสมผสานเครื่องมือที่รองรับ

คุณสามารถใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Search ร่วมกับเครื่องมืออื่นๆ เช่น
[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th),
[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) และ
[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th) (รองรับใน
โมเดล Gemini 3.5 Flash-Lite และโมเดลใหม่กว่า) เพื่อรองรับกรณีการใช้งานที่ซับซ้อนมากขึ้น
โมเดล Gemini 3 ยังรองรับการรวมเครื่องมือในตัวเหล่านี้กับเครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน) ดูข้อมูลเพิ่มเติมได้ในหน้าการผสมผสานเครื่องมือ

## ขั้นตอนถัดไป

- ลองใช้[การเชื่อมต่อแหล่งข้อมูลกับ Google Search ใน Gemini API
  สูตรการแก้ปัญหา](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=th)
- ดูข้อมูลเกี่ยวกับเครื่องมืออื่นๆ ที่มี เช่น [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
- ดูวิธีเพิ่มพรอมต์ด้วย URL ที่เฉพาะเจาะจงโดยใช้เครื่องมือ[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-13 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-13 UTC"],[],[]]
