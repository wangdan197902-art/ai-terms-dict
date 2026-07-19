---
title: الطبقة المخفية
term_id: hidden_layer
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- Deep Learning
difficulty: 3
weight: 1
slug: hidden_layer
date: '2026-07-18T16:00:47.316641Z'
lastmod: '2026-07-18T17:15:08.511919Z'
draft: false
source: agnes_llm
status: published
language: ar
description: طبقة وسيطة في الشبكة العصبية تقع بين طبقات الإدخال والإخراج وتقوم بمعالجة
  الميزات.
---
## Definition

تتكون الطبقة المخفية من عصبونات تتلقى مدخلات من الطبقات السابقة، وتطبق الأوزان والانحيازات، ثم تمرر البيانات المحولة للأمام عبر دالة التنشيط. تتيح هذه الطبقات للشبكات العصبية

### Summary

طبقة وسيطة في الشبكة العصبية تقع بين طبقات الإدخال والإخراج وتقوم بمعالجة الميزات.

## Key Concepts

- الشبكات العصبية
- استخراج الميزات
- دوال التنشيط
- التعلم العميق

## Use Cases

- أنظمة التعرف على الصور
- نماذج معالجة اللغات الطبيعية
- التحليلات التنبؤية

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (العصبون)](/en/terms/neuron-العصبون/)
- [backpropagation (الانتشار العكسي)](/en/terms/backpropagation-الانتشار-العكسي/)
- [activation_function (دالة التنشيط)](/en/terms/activation_function-دالة-التنشيط/)
- [deep_learning (التعلم العميق)](/en/terms/deep_learning-التعلم-العميق/)
