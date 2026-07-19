---
title: เครือข่ายฟีดฟอร์เวิร์ด (Feed-Forward Network)
term_id: feed_forward_network
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- fundamentals
difficulty: 2
weight: 1
slug: feed_forward_network
date: '2026-07-18T15:53:39.072106Z'
lastmod: '2026-07-18T16:38:07.606313Z'
draft: false
source: agnes_llm
status: published
language: th
description: คลาสของเครือข่ายประสาทเทียมเทียมที่การเชื่อมต่อระหว่างโหนดไม่เกิดวงจร
  โดยส่งผ่านข้อมูลในทิศทางเดียว
---
## Definition

เครือข่ายฟีดฟอร์เวิร์ด (FFN) หรือที่เรียกว่าเพอร์เซปตรอนหลายชั้น (MLP) ประมวลผลข้อมูลแบบลำดับผ่านชั้นของนิวรอนจากอินพุตไปยังเอาต์พุตโดยไม่มีการวนกลับ นิวรอนแต่ละตัวรับอินพุต คำนวณผลรวมถ่วงน้ำหนัก และผ่านฟังก์ชันกระตุ้น เพื่อส่งผลลัพธ์ไปยังชั้นถัดไป โครงสร้างนี้ทำให้ข้อมูลไหลไปข้างหน้าเพียงทิศทางเดียวเท่านั้น

### Summary

คลาสของเครือข่ายประสาทเทียมเทียมที่การเชื่อมต่อระหว่างโหนดไม่เกิดวงจร โดยส่งผ่านข้อมูลในทิศทางเดียว

## Key Concepts

- ไม่มีวงจร
- ชั้น (อินพุต, ซ่อน, เอาต์พุต)
- ฟังก์ชันกระตุ้น
- ผลรวมถ่วงน้ำหนัก

## Use Cases

- งานถดถอยอย่างง่าย
- ปัญหาการจำแนกประเภทกับข้อมูลตาราง
- บล็อกการสร้างสำหรับสถาปัตยกรรมที่ลึกขึ้น

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron (เพอร์เซปตรอนหลายชั้น)](/en/terms/multi-layer-perceptron-เพอร-เซปตรอนหลายช-น/)
- [Backpropagation (การแพร่ย้อนกลับ)](/en/terms/backpropagation-การแพร-ย-อนกล-บ/)
- [Activation Function (ฟังก์ชันกระตุ้น)](/en/terms/activation-function-ฟ-งก-ช-นกระต-น/)
- [Neural Network (เครือข่ายประสาทเทียม)](/en/terms/neural-network-เคร-อข-ายประสาทเท-ยม/)
