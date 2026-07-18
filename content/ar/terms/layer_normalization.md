---
title: "التطبيع الطبقي"
term_id: "layer_normalization"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "optimization", "architecture"]
difficulty: 3
weight: 1
slug: "layer_normalization"
aliases:
  - /ar/terms/layer_normalization/
date: "2026-07-18T16:05:20.138293Z"
lastmod: "2026-07-18T17:15:08.521211Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "تقنية تقوم بتطبيع تنشيطات طبقة الشبكة العصبية عبر بُعد الميزات لكل عينة فردية."
---

## Definition

يساهم التطبيع الطبقي في استقرار التدريب من خلال تقليل الانزياح التبايني الداخلي، وهو فعال بشكل خاص في الهياكل المتكررة ومحولات الانتباه (Transformers). وعلى عكس التطبيع الدفعي الذي يعتمد على إحصائيات

### Summary

تقنية تقوم بتطبيع تنشيطات طبقة الشبكة العصبية عبر بُعد الميزات لكل عينة فردية.

## Key Concepts

- التطبيع
- الانزياح التبايني الداخلي
- نماذج المحول (Transformers)
- الشبكات العصبية المتكررة

## Use Cases

- تدريب نماذج المحول مثل BERT
- استقرار تدريب الشبكات العصبية المتكررة/LSTM
- التعلم العميق بأحجام دفعات صغيرة

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (التطبيع الدفعي)](/en/terms/batch_normalization-التطبيع-الدفعي/)
- [transformer (المحول)](/en/terms/transformer-المحول/)
- [normalization (التطبيع)](/en/terms/normalization-التطبيع/)
- [deep_learning (التعلم العميق)](/en/terms/deep_learning-التعلم-العميق/)
