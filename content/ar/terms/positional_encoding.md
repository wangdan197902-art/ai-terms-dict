---
title: التشفير الموضعي
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
date: '2026-07-18T15:38:09.821422Z'
lastmod: '2026-07-18T17:15:08.464472Z'
draft: false
source: agnes_llm
status: published
language: ar
description: تقنية تُدخل معلومات حول الموقع النسبي أو المطلق للرموز في تسلسل ما إلى
  نماذج المحولات (Transformers).
---
## Definition

بما أن نماذج المحولات تعالج جميع الرموز بالتوازي بدلاً من التسلسل كما تفعل الشبكات العصبية المتكررة (RNNs)، فإنها تفتقر إلى المعرفة الفطرية بترتيب الرموز. يضيف التشفير الموضعي متجهات محددة إلى تضمينات المدخلات لتحديد موقع كل رمز ضمن التسلسل، مما يسمح للنموذج بفهم ترتيب البيانات.

### Summary

تقنية تُدخل معلومات حول الموقع النسبي أو المطلق للرموز في تسلسل ما إلى نماذج المحولات (Transformers).

## Key Concepts

- ترتيب التسلسل
- الانتباه الذاتي
- الدوال الجيبية
- تضمين الرموز

## Use Cases

- الترجمة الآلية
- تلخيص النصوص
- نمذجة اللغة

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

- [بنية المحول (Transformer Architecture)](/en/terms/بنية-المحول-transformer-architecture/)
- [التضمين (Embedding)](/en/terms/التضمين-embedding/)
- [آلية الانتباه (Attention Mechanism)](/en/terms/آلية-الانتباه-attention-mechanism/)
- [RoPE](/en/terms/rope/)
