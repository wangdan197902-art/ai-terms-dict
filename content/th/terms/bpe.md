---
title: "BPE (Byte Pair Encoding)"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
date: "2026-07-18T15:34:56.358186Z"
lastmod: "2026-07-18T16:38:07.558712Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "การเข้ารหัสคู่ไบต์เป็นอัลกอริทึมที่ใช้สำหรับการแบ่งคำย่อย (subword tokenization) โดยจะทำการรวมคู่อักขระที่ปรากฏบ่อยที่สุดเข้าด้วยกันอย่างซ้ำๆ เพื่อสร้างคลังคำศัพท์"
---
## Definition

การเข้ารหัสคู่ไบต์ (BPE) เป็นเทคนิคการบีบอัดข้อมูลที่ถูกนำมาปรับใช้ในงานประมวลผลภาษาธรรมชาติเพื่อจัดการกับคำที่ไม่อยู่ในคลังคำศัพท์ (out-of-vocabulary) เริ่มต้นจากคลังคำศัพท์ที่เป็นตัวอักษรเดี่ยว แล้วทำการรวมคู่ตัวอักษรที่พบบ่อยที่สุดเข้าด้วยกันอย่างเป็นขั้นตอน

### Summary

การเข้ารหัสคู่ไบต์เป็นอัลกอริทึมที่ใช้สำหรับการแบ่งคำย่อย (subword tokenization) โดยจะทำการรวมคู่อักขระที่ปรากฏบ่อยที่สุดเข้าด้วยกันอย่างซ้ำๆ เพื่อสร้างคลังคำศัพท์

## Key Concepts

- การแบ่งคำย่อย (Subword Tokenization)
- การรวมคลังคำศัพท์ (Vocabulary Merging)
- การวิเคราะห์ความถี่ (Frequency Analysis)
- การจัดการคำที่ไม่อยู่ในคลังคำศัพท์ (Out-of-Vocabulary Handling)

## Use Cases

- การเตรียมข้อมูลข้อความสำหรับโมเดลภาษาขนาดใหญ่
- การจัดการกับภาษาที่มีโครงสร้างคำซับซ้อน
- การลดขนาดคลังคำศัพท์ในเครือข่ายประสาทเทียม

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece (วิธีการแบ่งคำแบบ WordPiece)](/en/terms/wordpiece-ว-ธ-การแบ-งคำแบบ-wordpiece/)
- [SentencePiece (ไลบรารีสำหรับแบ่งคำระดับประโยค)](/en/terms/sentencepiece-ไลบราร-สำหร-บแบ-งคำระด-บประโยค/)
- [Tokenization (กระบวนการแบ่งข้อความเป็นหน่วยย่อย)](/en/terms/tokenization-กระบวนการแบ-งข-อความเป-นหน-วยย-อย/)
- [Subword Units (หน่วยคำย่อย)](/en/terms/subword-units-หน-วยคำย-อย/)
