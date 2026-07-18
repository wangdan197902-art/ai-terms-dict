---
title: "Dense (ชั้นหนาแน่น)"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /th/terms/dense/
date: "2026-07-18T15:50:01.830751Z"
lastmod: "2026-07-18T16:38:07.597954Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "เลเยอร์หรือเทนเซอร์ที่ทุกองค์ประกอบเชื่อมต่อกับทุกองค์ประกอบของเลเยอร์หรือมิติก่อนหน้า"
---

## Definition

ในโครงข่ายประสาทเทียม คำว่า 'dense' หมายถึงเลเยอร์แบบเชื่อมต่อเต็มรูปแบบ (fully connected) ซึ่งแต่ละนิวรอนจะได้รับข้อมูลนำเข้าจากนิวรอนทั้งหมดในเลเยอร์ก่อนหน้า สิ่งนี้แตกต่างจากการเชื่อมต่อแบบเบาบาง (sparse connections) ที่พบในเลเยอร์คอนโวลูชันหรือ...

### Summary

เลเยอร์หรือเทนเซอร์ที่ทุกองค์ประกอบเชื่อมต่อกับทุกองค์ประกอบของเลเยอร์หรือมิติก่อนหน้า

## Key Concepts

- Fully Connected (เชื่อมต่อเต็มรูปแบบ)
- Weight Matrix (เมทริกซ์น้ำหนัก)
- Activation Function (ฟังก์ชันกระตุ้น)
- Feature Integration (การรวมคุณลักษณะ)

## Use Cases

- เลเยอร์จัดประเภทสุดท้ายใน MLPs
- การรวมคุณลักษณะในโมเดลผสม
- งานถดถอยอย่างง่าย

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (โครงข่ายประสาทเทียมแบบฟีดฟอร์เวิร์ด)](/en/terms/feedforward-neural-network-โครงข-ายประสาทเท-ยมแบบฟ-ดฟอร-เว-ร-ด/)
- [Backpropagation (การแพร่ย้อนกลับ)](/en/terms/backpropagation-การแพร-ย-อนกล-บ/)
- [ReLU (ฟังก์ชันกระตุ้นเชิงเส้นส่วนเดียว)](/en/terms/relu-ฟ-งก-ช-นกระต-นเช-งเส-นส-วนเด-ยว/)
- [Bias Term (พจน์ค่าเบี่ยงเบน)](/en/terms/bias-term-พจน-ค-าเบ-ยงเบน/)
