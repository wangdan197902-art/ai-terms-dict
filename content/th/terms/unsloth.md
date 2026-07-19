---
title: Unsloth
term_id: unsloth
category: basic_concepts
subcategory: ''
tags:
- Optimization
- LLM
- training
- library
difficulty: 3
weight: 1
slug: unsloth
date: '2026-07-18T16:19:35.553306Z'
lastmod: '2026-07-18T16:38:07.665128Z'
draft: false
source: agnes_llm
status: published
language: th
description: Unsloth คือไลบรารีโอเพนซอร์สที่เร่งการฝึกฝนและการอนุมานของโมเดลภาษาขนาดใหญ่
  (LLM) ได้เร็วขึ้นถึง 2 เท่า ผ่านการจัดการหน่วยความจำและการใช้งานเคอร์เนลที่ปรับให้เหมาะสม
---
## Definition

Unsloth เป็นเครื่องมือเฉพาะทางที่ออกแบบมาเพื่อปรับปรุงประสิทธิภาพการปรับแต่งและใช้งานโมเดลภาษาขนาดใหญ่ (LLM) โดยช่วยลดการใช้หน่วยความจำและเพิ่มความเร็วได้อย่างมากผ่านการแทนที่โค้ดมาตรฐานของ PyTorch ด้วยส่วนประกอบที่ปรับให้เหมาะสมเป็นพิเศษ

### Summary

Unsloth คือไลบรารีโอเพนซอร์สที่เร่งการฝึกฝนและการอนุมานของโมเดลภาษาขนาดใหญ่ (LLM) ได้เร็วขึ้นถึง 2 เท่า ผ่านการจัดการหน่วยความจำและการใช้งานเคอร์เนลที่ปรับให้เหมาะสม

## Key Concepts

- การปรับให้เหมาะสมของหน่วยความจำ
- เคอร์เนลแบบกำหนดเอง
- การปรับแต่งโมเดลภาษาขนาดใหญ่
- การเร่งความเร็ว

## Use Cases

- การปรับแต่งโมเดลภาษาขนาดใหญ่บนทรัพยากร GPU ที่มีจำกัด
- การเร่งกระบวนการอนุมาน
- ลดต้นทุนการคำนวณบนคลาวด์สำหรับการฝึกฝน

## Code Example

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-2-7b-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True
)
```

## Related Terms

- [LoRA (เทคนิคการปรับแต่งโมเดลแบบเบา)](/en/terms/lora-เทคน-คการปร-บแต-งโมเดลแบบเบา/)
- [PyTorch (เฟรมเวิร์กการเรียนรู้เชิงลึก)](/en/terms/pytorch-เฟรมเว-ร-กการเร-ยนร-เช-งล-ก/)
- [Hugging Face (แพลตฟอร์มสำหรับโมเดล AI)](/en/terms/hugging-face-แพลตฟอร-มสำหร-บโมเดล-ai/)
- [Flash Attention (อัลกอริทึมการคำนวณ Attention ที่รวดเร็ว)](/en/terms/flash-attention-อ-ลกอร-ท-มการคำนวณ-attention-ท-รวดเร-ว/)
