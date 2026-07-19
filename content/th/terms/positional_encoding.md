---
title: การเข้ารหัสตำแหน่ง
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T15:36:58.190859Z'
lastmod: '2026-07-18T16:38:07.563479Z'
draft: false
source: agnes_llm
status: published
language: th
description: เทคนิคที่ฉีดข้อมูลเกี่ยวกับตำแหน่งสัมพัทธ์หรือสัมบูรณ์ของโทเค็นในลำดับเข้าไปในโมเดลทรานส์ฟอร์มเมอร์
---
## Definition

เนื่องจากทรานส์ฟอร์มเมอร์ประมวลผลโทเค็นทั้งหมดแบบขนานแทนที่จะเป็นแบบเรียงลำดับเหมือน RNN โมเดลจึงขาดความรู้โดยกำเนิดเกี่ยวกับลำดับของโทเค็น การเข้ารหัสตำแหน่งจะเพิ่มเวกเตอร์เฉพาะลงในเอนเบดดิ้งของอินพุตเพื่อบอกให้โมเดลทราบถึงลำดับและตำแหน่งของข้อมูลเหล่านั้น

### Summary

เทคนิคที่ฉีดข้อมูลเกี่ยวกับตำแหน่งสัมพัทธ์หรือสัมบูรณ์ของโทเค็นในลำดับเข้าไปในโมเดลทรานส์ฟอร์มเมอร์

## Key Concepts

- ลำดับของข้อมูล
- การสนใจตัวเอง
- ฟังก์ชันไซน์
- เอนเบดดิ้งของโทเค็น

## Use Cases

- การแปลภาษาด้วยเครื่อง
- การสรุปข้อความ
- การสร้างแบบจำลองภาษา

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformer Architecture (สถาปัตยกรรมทรานส์ฟอร์มเมอร์)](/en/terms/transformer-architecture-สถาป-ตยกรรมทรานส-ฟอร-มเมอร/)
- [Embedding (การฝังคำ)](/en/terms/embedding-การฝ-งคำ/)
- [Attention Mechanism (กลไกการให้ความสนใจ)](/en/terms/attention-mechanism-กลไกการให-ความสนใจ/)
- [RoPE (การเข้ารหัสตำแหน่งแบบหมุน)](/en/terms/rope-การเข-ารห-สตำแหน-งแบบหม-น/)
