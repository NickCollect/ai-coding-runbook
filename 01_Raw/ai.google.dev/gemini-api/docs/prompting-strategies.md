---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=th
fetched_at: 2026-06-15T06:25:48.231498+00:00
title: "\u0e01\u0e25\u0e22\u0e38\u0e17\u0e18\u0e4c\u0e01\u0e32\u0e23\u0e2d\u0e2d\u0e01\u0e41\u0e1a\u0e1a\u0e17\u0e35\u0e48\u0e01\u0e23\u0e30\u0e15\u0e38\u0e49\u0e19\u0e1c\u0e25\u0e25\u0e31\u0e1e\u0e18\u0e4c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# กลยุทธ์การออกแบบที่กระตุ้นผลลัพธ์

*การออกแบบพรอมต์*คือกระบวนการสร้างพรอมต์หรือคำขอที่เป็นภาษาธรรมชาติ
ซึ่งจะกระตุ้นให้โมเดลภาษาตอบกลับอย่างถูกต้องและมีคุณภาพสูง

หน้านี้จะแนะนำแนวคิด กลยุทธ์ และแนวทางปฏิบัติแนะนำเบื้องต้นเพื่อช่วยให้คุณเริ่มต้นออกแบบพรอมต์เพื่อใช้โมเดล AI จาก Gemini ให้เกิดประโยชน์สูงสุด

## คู่มือการใช้พรอมต์เฉพาะหัวข้อ

หากต้องการกลยุทธ์การใช้พรอมต์ที่เฉพาะเจาะจงมากขึ้น โปรดดูคำแนะนำการใช้พรอมต์อื่นๆ
ในหัวข้อต่อไปนี้

- [การป้อนพรอมต์ด้วยไฟล์สื่อ](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide)
- การป้อนพรอมต์เพื่อสร้างรูปภาพด้วย [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=th#imagen-prompt-guide) และ[การสร้างรูปภาพด้วย Gemini แบบเนทีฟ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th#prompt-guide)
- [การป้อนพรอมต์เพื่อสร้างวิดีโอ](https://ai.google.dev/gemini-api/docs/video?hl=th#prompt-guide)

คุณดูพรอมต์ตัวอย่างอื่นๆ ได้ใน[แกลเลอรีพรอมต์](https://ai.google.dev/gemini-api/prompts?hl=th)
ซึ่งออกแบบมาเพื่อแสดงแนวคิดต่างๆ ที่แชร์ในคู่มือนี้แบบอินเทอร์แอกทีฟ

## คำสั่งที่ชัดเจนและเจาะจง

วิธีที่มีประสิทธิภาพและประสิทธิผลในการปรับแต่งลักษณะการทำงานของโมเดลคือการให้คำสั่งที่ชัดเจนและเฉพาะเจาะจงแก่โมเดล คำสั่งอาจอยู่ในรูปแบบของคำถาม งานแบบทีละขั้นตอน หรือซับซ้อนถึงขั้นการทำแผนที่ประสบการณ์และความคิดของผู้ใช้

### อินพุต

อินพุตคือข้อความที่จำเป็นในพรอมต์ที่คุณต้องการให้โมเดลตอบ อินพุตอาจเป็นคำถามที่โมเดล
ตอบ (อินพุตคำถาม) งานที่โมเดลดำเนินการ (อินพุตงาน) เอนทิตีที่
โมเดลดำเนินการ (อินพุตเอนทิตี) หรืออินพุตบางส่วนที่โมเดลทำให้เสร็จสมบูรณ์หรือ
ดำเนินการต่อ (อินพุตการเติมข้อความ)

| **ประเภทอินพุต** | **พรอมต์** | **เอาต์พุตที่ได้** |
| --- | --- | --- |
| คำถาม | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| งาน | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| เอนทิตี | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### การป้อนข้อมูลบางส่วนให้เสร็จสมบูรณ์

โมเดลภาษาแบบ Generative ทำงานเหมือนเครื่องมือเติมข้อความอัตโนมัติขั้นสูง เมื่อคุณระบุเนื้อหาบางส่วน โมเดลจะสามารถระบุเนื้อหาส่วนที่เหลือหรือเนื้อหาที่โมเดลคิดว่าเป็นการต่อจากเนื้อหานั้นเป็นคำตอบได้ เมื่อทำเช่นนั้น หากคุณ
ใส่ตัวอย่างหรือบริบทใดๆ โมเดลจะนำตัวอย่างหรือบริบทเหล่านั้น
มาพิจารณา

ตัวอย่างต่อไปนี้แสดงพรอมต์ที่มีคำสั่งและอินพุตเอนทิตี

|  |
| --- |
| **พรอมต์:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **คำตอบ:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

แม้ว่าโมเดลจะทําตามที่ได้รับแจ้ง แต่การเขียนคําสั่งเป็นภาษาธรรมชาติบางครั้งก็อาจเป็นเรื่องยากและต้องอาศัยการตีความของโมเดลเป็นอย่างมาก
เช่น เมนูร้านอาหารอาจมีหลายรายการ หากต้องการลดขนาดการตอบกลับ JSON คุณอาจต้องละเว้นรายการที่ไม่ได้สั่งซื้อ ใน
กรณีนี้ คุณสามารถยกตัวอย่างและระบุคำนำหน้าคำตอบ แล้วปล่อยให้โมเดล
เติมข้อความให้สมบูรณ์ได้

|  |
| --- |
| **พรอมต์:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **คำตอบ:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

โปรดสังเกตว่าระบบยกเว้น "ชีสเบอร์เกอร์" จากเอาต์พุตเนื่องจากไม่ได้เป็นส่วนหนึ่งของคำสั่งซื้อ

แม้ว่าคุณจะระบุรูปแบบของออบเจ็กต์การตอบกลับ JSON แบบง่ายได้โดยใช้พรอมต์ แต่เราขอแนะนำให้ใช้ฟีเจอร์[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)ของ Gemini API เมื่อระบุ JSON Schema ที่ซับซ้อนกว่าสำหรับการตอบกลับ

### ข้อจำกัด

ระบุข้อจำกัดในการอ่านพรอมต์หรือการสร้างคำตอบ คุณสามารถ
บอกโมเดลว่าควรทำและไม่ควรทำอะไรได้ เช่น คุณระบุข้อจำกัด
ในพรอมต์เกี่ยวกับความยาวของข้อมูลสรุปที่ต้องการได้

|  |
| --- |
| **พรอมต์:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **คำตอบ:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### รูปแบบคำตอบ

คุณสามารถให้คำสั่งที่ระบุรูปแบบของคำตอบได้ เช่น คุณขอให้จัดรูปแบบคำตอบเป็นตาราง รายการสัญลักษณ์หัวข้อย่อย การเสนอขายโดยใช้เวลาสั้นๆ คำหลัก ประโยค หรือย่อหน้าได้ คำสั่งของระบบต่อไปนี้จะบอกให้
โมเดลตอบกลับในลักษณะที่เป็นการสนทนามากขึ้น

|  |
| --- |
| **คำสั่งของระบบ**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **พรอมต์**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **คำตอบ:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### จัดรูปแบบคำตอบด้วยกลยุทธ์การเติมข้อความ

[กลยุทธ์การเติมข้อความ](#completion)ยังช่วยจัดรูปแบบคำตอบได้ด้วย
ตัวอย่างต่อไปนี้จะแจ้งให้โมเดลสร้างโครงร่างเรียงความ

|  |
| --- |
| **พรอมต์:**    ``` Create an outline for an essay about hummingbirds. ```  **คำตอบ:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

พรอมต์ไม่ได้ระบุรูปแบบสำหรับโครงร่างและโมเดลเลือกรูปแบบให้คุณ
หากต้องการให้โมเดลแสดงโครงร่างในรูปแบบที่เฉพาะเจาะจง คุณสามารถเพิ่มข้อความที่แสดงจุดเริ่มต้นของโครงร่างและปล่อยให้โมเดลทำให้โครงร่างสมบูรณ์ตามรูปแบบที่คุณเริ่มต้น

|  |
| --- |
| **พรอมต์:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **คำตอบ:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## พรอมต์แบบ Zero-Shot กับ Few-Shot

คุณสามารถใส่ตัวอย่างในพรอมต์เพื่อแสดงให้โมเดลเห็นว่าคำตอบที่ถูกต้องมีลักษณะอย่างไร
โมเดลจะพยายามระบุรูปแบบและความสัมพันธ์จากตัวอย่าง
และนำไปใช้เมื่อสร้างคำตอบ พรอมต์ที่มีตัวอย่าง 2-3 รายการเรียกว่าพรอมต์แบบ *few-shot* ส่วนพรอมต์ที่ไม่มีตัวอย่างเรียกว่าพรอมต์แบบ *zero-shot* มักใช้พรอมต์แบบ few-shot
เพื่อควบคุมการจัดรูปแบบ การเรียบเรียง การกำหนดขอบเขต หรือการสร้างรูปแบบทั่วไปของคำตอบของโมเดล
ใช้ตัวอย่างที่เฉพาะเจาะจงและหลากหลายเพื่อช่วยให้โมเดลจำกัดขอบเขตและสร้างผลลัพธ์ที่แม่นยำยิ่งขึ้น

เราขอแนะนำให้ใส่ตัวอย่างแบบ Few-Shot ไว้ในพรอมต์เสมอ พรอมต์ที่ไม่มีตัวอย่างแบบ Few-Shot มักจะมีประสิทธิภาพน้อยกว่า ในความเป็นจริง คุณสามารถนำวิธีการออกจากพรอมต์ได้หากตัวอย่างของคุณแสดงงานที่ทำอยู่ได้อย่างชัดเจน

พรอมต์แบบ Zero-Shot ต่อไปนี้ขอให้โมเดลเลือกคำอธิบายที่ดีที่สุด

|  |
| --- |
| **พรอมต์:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **คำตอบ:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

หากกรณีการใช้งานของคุณกำหนดให้โมเดลต้องสร้างคำตอบที่กระชับ คุณสามารถใส่ตัวอย่างในพรอมต์ที่ให้ความสำคัญกับคำตอบที่กระชับ

พรอมต์ต่อไปนี้มีตัวอย่าง 2 รายการที่แสดงให้เห็นว่าชอบคำอธิบายที่สั้นกว่า
ในการตอบกลับ คุณจะเห็นว่าตัวอย่างได้แนะนำให้โมเดล
เลือกคำอธิบายที่สั้นกว่า (`Explanation2`) แทนที่จะเป็นคำอธิบายที่ยาวกว่า (`Explanation1`) เหมือนที่เคยทำ

|  |
| --- |
| **พรอมต์:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **คำตอบ:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### จำนวนตัวอย่างที่เหมาะสม

โมเดลอย่าง Gemini มักจะตรวจจับรูปแบบได้โดยใช้ตัวอย่างเพียงไม่กี่รายการ แต่คุณอาจต้องทดลองจำนวนตัวอย่างที่จะระบุในพรอมต์เพื่อให้ได้ผลลัพธ์ที่ดีที่สุด ในขณะเดียวกัน หากคุณใส่ตัวอย่างมากเกินไป
โมเดลอาจเริ่ม[ฟิตมากเกินไป](https://developers.google.com/machine-learning/glossary?hl=th#overfitting)
กับคำตอบของตัวอย่าง

### ใช้รูปแบบที่สม่ำเสมอ

ตรวจสอบว่าโครงสร้างและการจัดรูปแบบของตัวอย่างแบบ Few-Shot เหมือนกันเพื่อหลีกเลี่ยงการตอบกลับที่มีรูปแบบไม่พึงประสงค์ วัตถุประสงค์หลักอย่างหนึ่งของการเพิ่มตัวอย่างแบบ Few-Shot ในพรอมต์คือการแสดงรูปแบบการตอบกลับให้โมเดลเห็น ดังนั้นจึงจำเป็นอย่างยิ่งที่จะต้องตรวจสอบว่ารูปแบบสอดคล้องกันในตัวอย่างทั้งหมด โดยเฉพาะอย่างยิ่งการให้ความสนใจกับแท็ก XML, ช่องว่าง, บรรทัดใหม่ และตัวแยกตัวอย่าง

## เพิ่มบริบท

คุณสามารถใส่คำสั่งและข้อมูลในพรอมต์ที่โมเดลต้องใช้เพื่อแก้ปัญหา แทนที่จะคิดว่าโมเดลมีข้อมูลที่จำเป็นทั้งหมดอยู่แล้ว ข้อมูลตามบริบทนี้จะช่วยให้โมเดลเข้าใจข้อจำกัดและรายละเอียดของสิ่งที่คุณขอให้ทำ

ตัวอย่างต่อไปนี้ขอให้โมเดลให้คำแนะนำในการแก้ปัญหาสำหรับเราเตอร์

|  |
| --- |
| **พรอมต์:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **คำตอบ:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

คำตอบดูเหมือนข้อมูลการแก้ปัญหาทั่วไปที่ไม่ได้เจาะจง
ไปที่เราเตอร์หรือสถานะของไฟแสดงสถานะ LED

หากต้องการปรับแต่งคำตอบสำหรับเราเตอร์ที่เฉพาะเจาะจง คุณสามารถเพิ่มคำแนะนำในการแก้ปัญหาของเราเตอร์ลงในพรอมต์เป็นบริบทเพื่อให้ AI อ้างอิงเมื่อให้คำตอบ

|  |
| --- |
| **พรอมต์:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **คำตอบ:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## แบ่งพรอมต์ออกเป็นคอมโพเนนต์

สำหรับกรณีการใช้งานที่ต้องใช้พรอมต์ที่ซับซ้อน คุณสามารถช่วยให้โมเดลจัดการความซับซ้อนนี้ได้โดยการแบ่งสิ่งต่างๆ ออกเป็นคอมโพเนนต์ที่ง่ายขึ้น

1. **แยกย่อยวิธีการ:** สร้างพรอมต์ 1 รายการต่อ 1 วิธีแทนที่จะมีหลายวิธีในพรอมต์เดียว คุณเลือกพรอมต์ที่จะ
   ประมวลผลตามข้อมูลที่ผู้ใช้ป้อนได้
2. **พรอมต์แบบลูกโซ่:** สำหรับงานที่ซับซ้อนซึ่งเกี่ยวข้องกับหลายขั้นตอนตามลำดับ
   ให้แต่ละขั้นตอนเป็นพรอมต์และเชื่อมโยงพรอมต์เข้าด้วยกันตามลำดับ ในเชนของพรอมต์แบบลำดับนี้ เอาต์พุตของพรอมต์หนึ่งในลำดับจะกลายเป็นอินพุตของพรอมต์ถัดไป
   เอาต์พุตของพรอมต์สุดท้ายในลำดับ
   คือเอาต์พุตสุดท้าย
3. **การรวมคำตอบ:** การรวมคือเมื่อคุณต้องการทำงานแบบขนานที่แตกต่างกันในส่วนต่างๆ ของข้อมูล และรวมผลลัพธ์เพื่อสร้างเอาต์พุตสุดท้าย ตัวอย่างเช่น คุณสามารถบอกโมเดลให้ดำเนินการหนึ่งกับข้อมูลส่วนแรก ดำเนินการอีกอย่างกับข้อมูลส่วนที่เหลือ และรวบรวมผลลัพธ์

## ทดลองใช้พารามิเตอร์ของโมเดล

การเรียกแต่ละครั้งที่คุณส่งไปยังโมเดลจะมีค่าพารามิเตอร์ที่ควบคุมวิธีที่โมเดลสร้างการตอบกลับ
โมเดลสามารถสร้างผลลัพธ์ที่แตกต่างกันสำหรับ
ค่าพารามิเตอร์ที่แตกต่างกัน ทดสอบค่าพารามิเตอร์ต่างๆ เพื่อให้ได้ค่าที่ดีที่สุดสำหรับงาน พารามิเตอร์ที่ใช้ได้สำหรับ
โมเดลต่างๆ อาจแตกต่างกัน พารามิเตอร์ที่พบบ่อยที่สุดมีดังนี้

1. **โทเค็นเอาต์พุตสูงสุด:** ระบุจำนวนโทเค็นสูงสุดที่สร้างได้ในคำตอบ โทเค็นมีประมาณ 4 อักขระ โทเค็น 100 รายการจะสอดคล้องกับคำประมาณ 60-80 คำ
2. **อุณหภูมิ:** อุณหภูมิจะควบคุมระดับความสุ่มในการเลือกโทเค็น
   อุณหภูมิใช้สำหรับการสุ่มตัวอย่างระหว่างการสร้างคำตอบ
   ซึ่งจะเกิดขึ้นเมื่อใช้ `topP` และ `topK` อุณหภูมิที่ต่ำเหมาะสำหรับพรอมต์ที่ต้องการคำตอบที่กำหนดได้มากกว่าหรือเป็นคำตอบแบบปลายปิด
   ส่วนอุณหภูมิที่สูงอาจทำให้ได้ผลลัพธ์ที่หลากหลายหรือสร้างสรรค์มากขึ้น อุณหภูมิ 0 จะเป็นแบบดีเทอร์มินิสติก ซึ่งหมายความว่าระบบจะเลือกคำตอบที่มีความน่าจะเป็นสูงสุดเสมอ
3. **`topK`:** พารามิเตอร์ `topK` จะเปลี่ยนวิธีที่โมเดลเลือกโทเค็นสำหรับ
   เอาต์พุต `topK` ที่มีค่า 1 หมายความว่าโทเค็นที่เลือกมีความน่าจะเป็นมากที่สุดในบรรดาโทเค็นทั้งหมดในคำศัพท์ของโมเดล (เรียกอีกอย่างว่าการถอดรหัสแบบตะกละ)
   ส่วน `topK` ที่มีค่า 3 หมายความว่าระบบจะเลือกโทเค็นถัดไปจากโทเค็นที่มีความน่าจะเป็นมากที่สุด 3 รายการโดยใช้ค่าอุณหภูมิ สำหรับแต่ละขั้นตอนการเลือกโทเค็น ระบบจะสุ่มตัวอย่าง
   `topK`โทเค็นที่มีความน่าจะเป็นสูงสุด จากนั้นระบบจะกรองโทเค็นเพิ่มเติมตาม `topP` โดยเลือกโทเค็นสุดท้ายโดยใช้
   การสุ่มตัวอย่างอุณหภูมิ
4. **`topP`:** พารามิเตอร์ `topP` จะเปลี่ยนวิธีที่โมเดลเลือกโทเค็นสำหรับ
   เอาต์พุต ระบบจะเลือกโทเค็นจากโทเค็นที่มีความเป็นไปได้มากที่สุดไปจนถึงน้อยที่สุดจนกว่าผลรวมของ
   ความน่าจะเป็นจะเท่ากับค่า `topP` เช่น หากโทเค็น A, B,
   และ C มีความน่าจะเป็น 0.3, 0.2 และ 0.1 และค่า `topP` คือ 0.5
   โมเดลจะเลือก A หรือ B เป็นโทเค็นถัดไปโดยใช้
   อุณหภูมิและยกเว้น C เป็นตัวเลือก ค่าเริ่มต้นของ `topP` คือ 0.95
5. **`stop_sequences`:** ตั้งค่าลำดับการหยุดเพื่อ
   บอกให้โมเดลหยุดสร้างเนื้อหา ลำดับการหยุดอาจเป็นลำดับอักขระใดก็ได้ พยายามหลีกเลี่ยงการใช้อักขระที่อาจปรากฏในเนื้อหาที่สร้างขึ้น

## กลยุทธ์การปรับพรอมต์เพื่อถามซ้ำ

บางครั้งการออกแบบพรอมต์อาจต้องมีการทำซ้ำ 2-3 ครั้งก่อน
ที่คุณจะได้รับคำตอบที่ต้องการอย่างสม่ำเสมอ ส่วนนี้จะให้คำแนะนำเกี่ยวกับสิ่งที่คุณลองทำได้เมื่อทำซ้ำพรอมต์

1. **ใช้วลีที่แตกต่างกัน:** การใช้คำหรือวลีที่แตกต่างกันในพรอมต์มักจะทำให้โมเดล
   ตอบกลับแตกต่างกัน แม้ว่าทั้งหมดจะมีความหมายเหมือนกันก็ตาม หากคุณไม่ได้รับผลลัพธ์ที่คาดหวังจากพรอมต์ ให้ลอง
   เปลี่ยนวลี

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **เปลี่ยนไปใช้คำสั่งสำหรับงานที่คล้ายกัน:** หากคุณไม่สามารถทำให้โมเดลทำตามคำสั่งสำหรับงานได้ ให้ลองให้คำสั่งสำหรับงานที่คล้ายกันซึ่งให้ผลลัพธ์เดียวกัน

   พรอมต์นี้จะบอกให้โมเดลจัดหมวดหมู่หนังสือโดยใช้หมวดหมู่ที่กำหนดไว้ล่วงหน้า

   |  |
   | --- |
   | **พรอมต์:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **คำตอบ:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   คำตอบถูกต้อง แต่โมเดลไม่ได้อยู่ภายในขอบเขตของตัวเลือก
   นอกจากนี้ คุณยังต้องการสร้างโมเดลให้ตอบกลับด้วยตัวเลือกใดตัวเลือกหนึ่งแทน
   การตอบกลับเป็นประโยคเต็ม ในกรณีนี้ คุณสามารถเรียบเรียงคำสั่งใหม่เป็น
   คำถามแบบหลายตัวเลือกและขอให้โมเดลเลือกตัวเลือกได้

   |  |
   | --- |
   | **พรอมต์:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **คำตอบ:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **เปลี่ยนลำดับเนื้อหาของพรอมต์:** บางครั้งลำดับเนื้อหาในพรอมต์อาจส่งผลต่อคำตอบ ลองเปลี่ยนลำดับเนื้อหาและดูว่า
     การเปลี่ยนแปลงดังกล่าวส่งผลต่อคำตอบอย่างไร

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

## คำตอบสำรอง

การตอบกลับสำรองคือการตอบกลับที่โมเดลส่งคืนเมื่อพรอมต์
หรือการตอบกลับทริกเกอร์ตัวกรองความปลอดภัย ตัวอย่างคำตอบสำรองคือ "ฉันช่วยคุณเรื่องนี้ไม่ได้เพราะเป็นเพียงโมเดลภาษา"

หากโมเดลตอบกลับด้วยคำตอบสำรอง ให้ลองเพิ่มอุณหภูมิ

## การอ้างอิงและการเรียกใช้โค้ด

Gemini สามารถใช้เครื่องมือเพื่อหลีกเลี่ยงการหลอนในสถานการณ์ที่อาจทำให้ได้คำตอบที่ไม่ถูกต้อง

[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) จะเชื่อมต่อโมเดล Gemini กับเนื้อหาเว็บแบบเรียลไทม์ และควรเปิดใช้ทุกครั้งที่โมเดลอาจจำเป็นต้องทราบข้อเท็จจริงที่คลุมเครือหรือล่าสุด

[เครื่องมือการเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)ของ Gemini ช่วยให้โมเดลสร้างและรันโค้ด Python ได้ และควรเปิดใช้ทุกครั้งที่โมเดลต้องดำเนินการทางคณิตศาสตร์ การนับ หรือการคำนวณใดๆ

## Gemini 3

[โมเดล Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-3) ออกแบบมาเพื่อการให้เหตุผลและการทำตามคำสั่งขั้นสูง
โมเดลจะตอบสนองต่อพรอมต์ที่ตรงไปตรงมา มีโครงสร้างที่ดี และกำหนดงานและข้อจำกัดต่างๆ อย่างชัดเจนได้ดีที่สุด
เราขอแนะนำให้ใช้แนวทางต่อไปนี้เพื่อให้ได้ผลลัพธ์ที่ดีที่สุดด้วย Gemini 3

### หลักการสำคัญของการเขียนพรอมต์

- **ระบุอย่างชัดเจนและตรงไปตรงมา:** ระบุเป้าหมายอย่างชัดเจนและกระชับ หลีกเลี่ยง
  ภาษาที่ไม่จำเป็นหรือโน้มน้าวมากเกินไป
- **ใช้โครงสร้างที่สอดคล้องกัน:** ใช้ตัวคั่นที่ชัดเจนเพื่อแยกส่วนต่างๆ
  ของพรอมต์ แท็กรูปแบบ XML (เช่น `<context>`, `<task>`) หรือ
  ส่วนหัว Markdown จะมีประสิทธิภาพ เลือกรูปแบบใดรูปแบบหนึ่งและใช้รูปแบบนั้นอย่างสม่ำเสมอ
  ภายในพรอมต์เดียว
- **กําหนดพารามิเตอร์:** อธิบายคำหรือพารามิเตอร์ที่ไม่ชัดเจนอย่างชัดเจน
- **ควบคุมความละเอียดของเอาต์พุต:** โดยค่าเริ่มต้น โมเดล Gemini 3 จะให้คำตอบที่ตรงไปตรงมาและมีประสิทธิภาพ หากต้องการคำตอบที่เป็นการสนทนาหรือมีรายละเอียดมากขึ้น คุณต้องขออย่างชัดเจนในคำสั่ง
- **จัดการอินพุตหลายรูปแบบอย่างสอดคล้องกัน:** เมื่อใช้ข้อความ รูปภาพ เสียง หรือวิดีโอ ให้ถือว่าอินพุตเหล่านี้เป็นอินพุตระดับเดียวกัน ตรวจสอบว่าวิธีการของคุณอ้างอิงถึงแต่ละรูปแบบอย่างชัดเจน
  ตามที่จำเป็น
- **จัดลำดับความสำคัญของคำสั่งที่สำคัญ:** วางข้อจำกัดด้านพฤติกรรมที่จำเป็น
  คำจำกัดความของบทบาท (ลักษณะตัวตน) และข้อกำหนดรูปแบบเอาต์พุตใน
  คำสั่งของระบบหรือที่จุดเริ่มต้นของพรอมต์ของผู้ใช้
- **โครงสร้างสำหรับบริบทที่ยาว:** เมื่อให้บริบทจำนวนมาก
  (เช่น เอกสาร โค้ด) ให้ระบุบริบททั้งหมดก่อน จากนั้นวางคำสั่งหรือคำถามที่เฉพาะเจาะจงไว้ที่*ท้าย*พรอมต์
- **บริบทของข้อความ Anchor:** หลังจากข้อมูลบล็อกใหญ่ ให้ใช้วลีเปลี่ยนผ่านที่ชัดเจน
  เพื่อเชื่อมโยงบริบทกับคําค้นหา เช่น "จากข้อมูลข้างต้น..."

### กลยุทธ์ของ Gemini 3 Flash

- **ความแม่นยำของวันปัจจุบัน:** เพิ่มข้อความต่อไปนี้ลงในคำสั่งของระบบเพื่อช่วยให้โมเดลทราบว่าวันปัจจุบันอยู่ในปี 2026

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **ความแม่นยำของวันที่สิ้นสุดความรู้:** เพิ่มข้อความต่อไปนี้ลงในคำสั่งของระบบเพื่อให้โมเดลทราบวันที่สิ้นสุดความรู้

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **ประสิทธิภาพการอ้างอิง:** เพิ่มข้อความต่อไปนี้ลงในคำสั่งของระบบ (โดยแก้ไขตามความเหมาะสม) เพื่อปรับปรุงความสามารถของโมเดลในการอ้างอิงคำตอบในบริบทที่ระบุ

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

### การปรับปรุงการให้เหตุผลและการวางแผน

โมเดล Gemini 2.5 และซีรีส์ 3 จะสร้างข้อความ "การคิด" ภายในโดยอัตโนมัติ
เพื่อปรับปรุงประสิทธิภาพการให้เหตุผล ด้วยเหตุนี้ โดยทั่วไปจึงไม่จำเป็นต้องให้
โมเดลร่าง วางแผน หรือให้รายละเอียดขั้นตอนการให้เหตุผลในคำตอบที่ส่งคืน
เอง สำหรับปัญหาที่ต้องใช้การให้เหตุผลอย่างหนัก คำขอที่เรียบง่าย เช่น "คิด
อย่างหนักก่อนตอบ" จะช่วยปรับปรุงประสิทธิภาพได้ แต่ต้องเสียโทเค็นการคิดเพิ่มเติม

ดูรายละเอียดเพิ่มเติมได้ในเอกสารประกอบ[การคิดของ Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

### ตัวอย่างการใช้พรอมต์ที่มีโครงสร้าง

การใช้แท็กหรือมาร์กดาวน์จะช่วยให้โมเดลแยกความแตกต่างระหว่างคำสั่ง บริบท และงานได้

**ตัวอย่าง XML:**

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

**ตัวอย่างมาร์กดาวน์:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### ตัวอย่างเทมเพลตที่รวมแนวทางปฏิบัติแนะนำ

เทมเพลตนี้รวบรวมหลักการสำคัญสำหรับการพรอมต์ด้วย Gemini 3 อย่าลืมทำซ้ำและแก้ไขสำหรับ Use Case เฉพาะของคุณ

**คำสั่งของระบบ:**

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

**พรอมต์ของผู้ใช้:**

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

## เวิร์กโฟลว์ที่เป็น Agent

สำหรับเวิร์กโฟลว์ที่มีเอเจนต์จำนวนมาก มักจะต้องมีวิธีการที่เฉพาะเจาะจงเพื่อควบคุมวิธีที่โมเดลให้เหตุผล วางแผน และดำเนินการ แม้ว่า Gemini จะมีประสิทธิภาพทั่วไปที่ยอดเยี่ยม แต่เอเจนต์ที่ซับซ้อนมักกำหนดให้คุณกำหนดค่าการแลกเปลี่ยนระหว่างต้นทุนการคำนวณ (เวลาในการตอบสนองและโทเค็น) กับความแม่นยำของงาน

เมื่อออกแบบพรอมต์สำหรับเอเจนต์ ให้พิจารณามิติข้อมูลพฤติกรรมต่อไปนี้ที่คุณสามารถควบคุมในเอเจนต์ได้

### การให้เหตุผลและกลยุทธ์

การกำหนดค่าวิธีที่โมเดลคิดและวางแผนก่อนดำเนินการ

- **การแยกย่อยเชิงตรรกะ:** กำหนดว่าโมเดลต้องวิเคราะห์ข้อจำกัด ข้อกำหนดเบื้องต้น และลำดับการดำเนินการอย่างละเอียดเพียงใด
- **การวินิจฉัยปัญหา**: ควบคุมระดับการวิเคราะห์เมื่อระบุสาเหตุและการใช้การให้เหตุผลแบบอนุมานของโมเดล กำหนดว่าโมเดลควรยอมรับคำตอบที่ชัดเจนที่สุดหรือสำรวจคำอธิบายที่ซับซ้อนและมีความเป็นไปได้น้อยกว่า
- **ความครอบคลุมของข้อมูล:** การแลกเปลี่ยนระหว่างการวิเคราะห์นโยบายและเอกสารที่มีอยู่ทั้งหมดกับการจัดลําดับความสําคัญของประสิทธิภาพและความเร็ว

### การดำเนินการและความน่าเชื่อถือ

การกำหนดค่าวิธีที่เอเจนต์ทำงานโดยอัตโนมัติและจัดการอุปสรรค

- **ความสามารถในการปรับตัว:** วิธีที่โมเดลตอบสนองต่อข้อมูลใหม่ พิจารณาว่าควรยึดมั่นตามแผนเริ่มต้นอย่างเคร่งครัดหรือปรับเปลี่ยนทันทีเมื่อการสังเกตขัดแย้งกับสมมติฐาน
- **ความต่อเนื่องและการกู้คืน:** ระดับที่โมเดลพยายามแก้ไขข้อผิดพลาดด้วยตนเอง ความต่อเนื่องสูงจะเพิ่มอัตราความสำเร็จ แต่มีความเสี่ยงที่จะมีค่าใช้จ่ายโทเค็นสูงขึ้นหรือเกิดลูป
- **การประเมินความเสี่ยง:** ตรรกะในการประเมินผลที่ตามมา แยกความแตกต่างอย่างชัดเจนระหว่างการดำเนินการสำรวจที่มีความเสี่ยงต่ำ (การอ่าน) กับการเปลี่ยนแปลงสถานะที่มีความเสี่ยงสูง (การเขียน)

### การโต้ตอบและเอาต์พุต

การกำหนดค่าวิธีที่เอเจนต์สื่อสารกับผู้ใช้และจัดรูปแบบผลลัพธ์

- **ความคลุมเครือและการจัดการสิทธิ์:** กำหนดเวลาที่โมเดลได้รับอนุญาตให้คาดเดาเทียบกับเวลาที่ต้องหยุดการดำเนินการชั่วคราวเพื่อขอคำชี้แจงหรือสิทธิ์จากผู้ใช้
- **ความละเอียด:** ควบคุมระดับเสียงของข้อความที่สร้างขึ้นพร้อมกับการเรียกใช้เครื่องมือ ซึ่งจะกำหนดว่าโมเดลจะอธิบายการดำเนินการของตนให้ผู้ใช้ทราบหรือจะไม่อธิบายในระหว่างการดำเนินการ
- **ความแม่นยำและความสมบูรณ์:** ความเที่ยงตรงที่จำเป็นของเอาต์พุต ระบุว่าโมเดลต้องแก้ปัญหาทุกกรณีขอบและระบุตัวเลขที่แน่นอน หรือยอมรับค่าประมาณคร่าวๆ ได้

### เทมเพลตคำสั่งของระบบ

คำสั่งของระบบต่อไปนี้เป็นตัวอย่างที่นักวิจัยประเมินเพื่อปรับปรุงประสิทธิภาพในการเปรียบเทียบแบบเอเจนต์ ซึ่งโมเดลต้องปฏิบัติตามกฎที่ซับซ้อนและโต้ตอบกับผู้ใช้ โดยจะกระตุ้นให้เอเจนต์ทำหน้าที่เป็นผู้ให้เหตุผลและวางแผนที่ยอดเยี่ยม บังคับใช้พฤติกรรมที่เฉพาะเจาะจงในมิติข้อมูลต่างๆ ที่ระบุไว้ข้างต้น และกำหนดให้โมเดลวางแผนล่วงหน้าก่อนที่จะดำเนินการใดๆ

คุณสามารถปรับเทมเพลตนี้ให้เหมาะกับข้อจำกัดของ Use Case ที่เฉพาะเจาะจงได้

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

## ขั้นตอนถัดไป

- ตอนนี้คุณมีความเข้าใจที่ลึกซึ้งยิ่งขึ้นเกี่ยวกับการออกแบบพรอมต์แล้ว ลองเขียนพรอมต์ของคุณเองโดยใช้ [Google AI Studio](http://aistudio.google.com?hl=th)
- ดูข้อมูลเกี่ยวกับการเขียนพรอมต์แบบหลายรูปแบบได้ที่[การแจ้งด้วยไฟล์สื่อ](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide)
- ดูข้อมูลเกี่ยวกับการเขียนพรอมต์สำหรับรูปภาพได้ที่คำแนะนำในการเขียนพรอมต์สำหรับ [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=th#prompt-guide)
  และ [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=th#imagen-prompt-guide)
- ดูข้อมูลเกี่ยวกับการใช้พรอมต์วิดีโอได้ใน[คู่มือการใช้พรอมต์ของ Veo](https://ai.google.dev/gemini-api/docs/video?hl=th#prompt-guide)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-10 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-10 UTC"],[],[]]
