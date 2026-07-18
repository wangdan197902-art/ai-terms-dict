---
title: "الانتباه الذاتي"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /ar/terms/self_attention/
date: "2026-07-18T15:30:54.694946Z"
lastmod: "2026-07-18T17:15:08.448801Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "آلية تسمح للشبكة العصبية بوزن أهمية أجزاء مختلفة من تسلسل الإدخال بالنسبة لبعضها البعض."
---

## Definition

يتيح الانتباه الذاتي للنماذج التقاط التبعيات بين جميع المواقع في التسلسل في وقت واحد، بغض النظر عن المسافة. من خلال حساب درجات الانتباه بين كل زوج من الرموز، يتيح ذلك...

### Summary

آلية تسمح للشبكة العصبية بوزن أهمية أجزاء مختلفة من تسلسل الإدخال بالنسبة لبعضها البعض.

## Key Concepts

- الاستعلام-المفتاح-القيمة
- درجات الانتباه
- الوزن السياقي
- المعالجة المتوازية

## Use Cases

- الترجمة الآلية
- تلخيص النصوص
- تصنيف الصور عبر محولات الرؤية (Vision Transformers)

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [المحول (Transformer)](/en/terms/المحول-transformer/)
- [الانتباه متعدد الرؤوس (Multi-Head Attention)](/en/terms/الانتباه-متعدد-الرؤوس-multi-head-attention/)
- [التضمينات (Embeddings)](/en/terms/التضمينات-embeddings/)
- [نمذجة التسلسل (Sequence Modeling)](/en/terms/نمذجة-التسلسل-sequence-modeling/)
