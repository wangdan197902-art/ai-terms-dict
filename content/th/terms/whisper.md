---
title: "วิสเปอร์ (Whisper)"
term_id: "whisper"
category: "basic_concepts"
subcategory: ""
tags: ["speech_recognition", "openai", "practical_ai"]
difficulty: 2
weight: 1
slug: "whisper"
aliases:
  - /th/terms/whisper/
date: "2026-07-18T16:20:32.977650Z"
lastmod: "2026-07-18T16:38:07.667466Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "ระบบรู้จำเสียงพูดอัตโนมัติ (ASR) ที่พัฒนาโดย OpenAI และฝึกฝนด้วยชุดข้อมูลเสียงที่หลากหลายขนาดใหญ่"
---

## Definition

วิสเปอร์เป็นโมเดลรู้จำเสียงพูดอเนกประสงค์ที่ออกแบบมาเพื่อรองรับภาษา สำเนียง และdialects หลากหลายชนิด มันถูกฝึกฝนด้วยข้อมูลเสียงหลายหมื่นชั่วโมงจากหลายภาษาและงานต่างๆ ทำให้มีความแม่นยำสูงแม้ในสภาพแวดล้อมที่มีเสียงรบกวน

### Summary

ระบบรู้จำเสียงพูดอัตโนมัติ (ASR) ที่พัฒนาโดย OpenAI และฝึกฝนด้วยชุดข้อมูลเสียงที่หลากหลายขนาดใหญ่

## Key Concepts

- การรู้จำเสียงพูดอัตโนมัติ
- การรองรับหลายภาษา
- ความทนทานต่อสัญญาณรบกวน
- สถาปัตยกรรมทรานส์ฟอร์เมอร์

## Use Cases

- การสร้างคำบรรยายและซับไตเติ้ลสำหรับวิดีโอ
- การถอดเสียงการประชุมหรือการบรรยาย
- การประมวลผลคำสั่งด้วยเสียง

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Speech-to-text (แปลงเสียงเป็นข้อความ)](/en/terms/speech-to-text-แปลงเส-ยงเป-นข-อความ/)
- [Natural Language Processing (การประมวลผลภาษาธรรมชาติ)](/en/terms/natural-language-processing-การประมวลผลภาษาธรรมชาต/)
- [OpenAI (องค์กรโอเพนเอไอ)](/en/terms/openai-องค-กรโอเพนเอไอ/)
- [Audio classification (การจำแนกประเภทเสียง)](/en/terms/audio-classification-การจำแนกประเภทเส-ยง/)
