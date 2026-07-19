---
title: الذاكرة طويلة وقصيرة المدى
term_id: long_short_term_memory
category: basic_concepts
subcategory: ''
tags:
- architecture
- RNN
- Deep Learning
difficulty: 4
weight: 1
slug: long_short_term_memory
date: '2026-07-18T15:37:27.951694Z'
lastmod: '2026-07-18T17:15:08.462978Z'
draft: false
source: agnes_llm
status: published
language: ar
description: بنية متخصصة للشبكات العصبية المتكررة مصممة لتعلم التبعيات طويلة المدى
  في البيانات التسلسلية.
---
## Definition

تعالج شبكات الذاكرة طويلة وقصيرة المدى مشكلة تلاشي التدرج الشائعة في الشبكات العصبية المتكررة القياسية من خلال استخدام حالة الخلية وثلاث آليات تحكّم: مدخلات، ونسيان، ومخرجات. تنظم هذه الآليات تدفق المعلومات

### Summary

بنية متخصصة للشبكات العصبية المتكررة مصممة لتعلم التبعيات طويلة المدى في البيانات التسلسلية.

## Key Concepts

- آليات التحكّم
- حالة الخلية
- البيانات التسلسلية
- تلاشي التدرج

## Use Cases

- التنبؤ بسلاسل الزمن
- التعرف على الكلام
- الترجمة الآلية

## Code Example

```python
import torch.nn as nn
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=1)
```

## Related Terms

- [recurrent_neural_network (الشبكة العصبية المتكررة)](/en/terms/recurrent_neural_network-الشبكة-العصبية-المتكررة/)
- [gates (صمامات التحكّم)](/en/terms/gates-صمامات-التحك-م/)
- [sequence_modeling (نمذجة التسلسل)](/en/terms/sequence_modeling-نمذجة-التسلسل/)
- [nlp (معالجة اللغات الطبيعية)](/en/terms/nlp-معالجة-اللغات-الطبيعية/)
