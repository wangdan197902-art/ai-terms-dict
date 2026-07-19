---
title: المحول
term_id: transformer
category: basic_concepts
subcategory: ''
tags:
- architecture
- NLP
- attention
difficulty: 4
weight: 1
slug: transformer
date: '2026-07-18T15:31:48.544626Z'
lastmod: '2026-07-18T17:15:08.451434Z'
draft: false
source: agnes_llm
status: published
language: ar
description: بنية للتعلم العميق تعتمد على آليات الانتباه الذاتي لمعالجة البيانات المتسلسلة
  بالتوازي بدلاً من التسلسل.
---
## Definition

تم تقديم بنية المحول في ورقة بحثية بعنوان 'الانتباه هو كل ما تحتاجه'، حيث أحدثت ثورة في معالجة اللغات الطبيعية وما بعدها. تستخدم هذه البنية انتباهاً ذاتياً متعدد الرؤوس لوزن أهمية

### Summary

بنية للتعلم العميق تعتمد على آليات الانتباه الذاتي لمعالجة البيانات المتسلسلة بالتوازي بدلاً من التسلسل.

## Key Concepts

- الانتباه الذاتي
- الانتباه متعدد الرؤوس
- التشفير الموضعي
- بنية المشفر-المفكك

## Use Cases

- الترجمة الآلية
- توليد النصوص
- التعرف على الصور (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (آلية الانتباه)](/en/terms/attention_mechanism-آلية-الانتباه/)
- [bert (نموذج BERT)](/en/terms/bert-نموذج-bert/)
- [gpt (نموذج GPT)](/en/terms/gpt-نموذج-gpt/)
- [self_attention (الانتباه الذاتي)](/en/terms/self_attention-الانتباه-الذاتي/)
