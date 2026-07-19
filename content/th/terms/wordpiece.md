---
title: เวิร์ดพีซ (WordPiece)
term_id: wordpiece
category: engineering_practice
subcategory: ''
tags:
- NLP
- tokenization
- BERT
difficulty: 3
weight: 1
slug: wordpiece
date: '2026-07-18T16:20:32.977691Z'
lastmod: '2026-07-18T16:38:07.667709Z'
draft: false
source: agnes_llm
status: published
language: th
description: อัลกอริทึมการแบ่งคำย่อย (subword tokenization) ที่ผสานคู่อักขระที่พบบ่อยที่สุดแบบวนซ้ำ
  เพื่อจัดการกับคำที่ไม่อยู่ในคลังคำศัพท์
---
## Definition

เวิร์ดพีซเป็นวิธีการแบ่งคำที่ใช้กันอย่างแพร่หลายในโมเดลประมวลผลภาษาธรรมชาติเช่น BERT และ ALBERT โดยจะแยกคำออกเป็นหน่วยย่อยๆ เพื่อจัดการกับความซับซ้อนทางสัณฐานวิทยาและลดขนาดคลังคำศัพท์ พร้อมทั้งรักษาความสามารถในการเข้าใจคำใหม่ๆ

### Summary

อัลกอริทึมการแบ่งคำย่อย (subword tokenization) ที่ผสานคู่อักขระที่พบบ่อยที่สุดแบบวนซ้ำ เพื่อจัดการกับคำที่ไม่อยู่ในคลังคำศัพท์

## Key Concepts

- การแบ่งคำย่อย
- การขยายคลังคำศัพท์
- การจัดการคำที่ไม่อยู่ในคลัง
- การวิเคราะห์ทางสัณฐานวิทยา

## Use Cases

- การเตรียมข้อมูลข้อความสำหรับโมเดล BERT
- การจัดการภาษาที่มีทรัพยากรจำกัด
- การลดขนาดเมทริกซ์การฝังคำ (embedding matrix)

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (การเข้ารหัสคู่ไบต์)](/en/terms/byte-pair-encoding-การเข-ารห-สค-ไบต/)
- [SentencePiece (เซนเทนต์พีซ)](/en/terms/sentencepiece-เซนเทนต-พ-ซ/)
- [Tokenization (การแบ่งโทเค็น)](/en/terms/tokenization-การแบ-งโทเค-น/)
- [NLP preprocessing (การเตรียมข้อมูลก่อนประมวลผล NLP)](/en/terms/nlp-preprocessing-การเตร-ยมข-อม-ลก-อนประมวลผล-nlp/)
