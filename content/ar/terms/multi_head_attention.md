---
title: "الانتباه متعدد الرؤوس"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /ar/terms/multi_head_attention/
date: "2026-07-18T15:28:01.146766Z"
lastmod: "2026-07-18T17:15:08.443669Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "آلية في نماذج المحولات تسمح للنموذج بالاهتمام بمعلومات من فضاءات تمثيلية مختلفة في وقت واحد."
---

## Definition

يوسع الانتباه متعدد الرؤوس آلية الانتباه القياسية عن طريق تشغيلها عدة مرات بالتوازي مع إسقاطات خطية مختلفة تم تعلمها. يتيح هذا للنموذج الاهتمام معاً بمعلومات من زوايا متعددة.

### Summary

آلية في نماذج المحولات تسمح للنموذج بالاهتمام بمعلومات من فضاءات تمثيلية مختلفة في وقت واحد.

## Key Concepts

- الانتباه الذاتي
- الإسقاطات الخطية
- الدمج

## Use Cases

- معالجة اللغات الطبيعية (NLP)
- الترجمة الآلية
- تصنيف الصور باستخدام محولات الرؤية

## Code Example

```python
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        # Simplified forward pass logic
        pass
```

## Related Terms

- [Scaled Dot-Product Attention (انتجاه حاصل الضرب النقطي المقياس)](/en/terms/scaled-dot-product-attention-انتجاه-حاصل-الضرب-النقطي-المقياس/)
- [Transformer (المحول)](/en/terms/transformer-المحول/)
- [Embedding (التضمين)](/en/terms/embedding-التضمين/)
