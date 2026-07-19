---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T15:37:11.587744Z'
lastmod: '2026-07-18T16:38:07.564323Z'
draft: false
source: agnes_llm
status: published
language: th
description: ReLU (Rectified Linear Unit) คือฟังก์ชันกระตุ้น (activation function)
  ที่ส่งค่าอินพุตออกมาโดยตรงหากมีค่าเป็นบวก และส่งค่าศูนย์ออกหากมีค่าน้อยกว่าหรือเท่ากับศูนย์
---
## Definition

ReLU นิยมใช้ในโครงข่ายประสาทเทียมสำหรับการเรียนรู้เชิงลึกเนื่องจากมีความคุ้มค่าในการคำนวณสูงและช่วยบรรเทาปัญหาเกรเดียนต์หายไปได้ โดยนิยามทางคณิตศาสตร์คือ f(x) = max(0, x) ซึ่งแนะนำความเป็นไม่เชิงเส้น (non-linearity) ให้กับโมเดล

### Summary

ReLU (Rectified Linear Unit) คือฟังก์ชันกระตุ้น (activation function) ที่ส่งค่าอินพุตออกมาโดยตรงหากมีค่าเป็นบวก และส่งค่าศูนย์ออกหากมีค่าน้อยกว่าหรือเท่ากับศูนย์

## Key Concepts

- ความเป็นไม่เชิงเส้น (Non-linearity)
- ฟังก์ชันกระตุ้น (Activation Function)
- ปัญหาเกรเดียนต์หาย (Vanishing Gradient)
- เชิงเส้นเป็นช่วงๆ (Piecewise Linear)

## Use Cases

- เลเยอร์ซ่อนใน CNN (Hidden layers in CNNs)
- เครือข่ายฟีดฟอร์เวิร์ดเชิงลึก (Deep Feedforward Networks)
- แบบจำลองการรู้จำภาพ (Image Recognition Models)

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (ฟังก์ชันซิกมอยด์)](/en/terms/sigmoid-ฟ-งก-ช-นซ-กมอยด/)
- [Tanh (ฟังก์ชันไทรโกลูเมนไฮเพอร์โบลา)](/en/terms/tanh-ฟ-งก-ช-นไทรโกล-เมนไฮเพอร-โบลา/)
- [Leaky ReLU (ReLU แบบรั่ว)](/en/terms/leaky-relu-relu-แบบร-ว/)
- [Neural Network (โครงข่ายประสาทเทียม)](/en/terms/neural-network-โครงข-ายประสาทเท-ยม/)
