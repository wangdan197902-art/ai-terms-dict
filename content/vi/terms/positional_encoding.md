---
title: Mã hóa vị trí
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
date: '2026-07-18T15:36:48.459168Z'
lastmod: '2026-07-18T16:38:07.712092Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một kỹ thuật đưa thông tin về vị trí tương đối hoặc tuyệt đối của các
  token trong một chuỗi vào các mô hình Transformer.
---
## Definition

Vì các mô hình Transformer xử lý tất cả các token song song thay vì tuần tự như RNN, chúng thiếu kiến thức nội tại về thứ tự của token. Mã hóa vị trí thêm các vectơ cụ thể vào các embedding đầu vào để xác định thứ tự này.

### Summary

Một kỹ thuật đưa thông tin về vị trí tương đối hoặc tuyệt đối của các token trong một chuỗi vào các mô hình Transformer.

## Key Concepts

- Thứ tự chuỗi
- Tự chú ý (Self-Attention)
- Hàm sin/cos
- Embedding Token

## Use Cases

- Dịch máy
- Tóm tắt văn bản
- Mô hình ngôn ngữ

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

- [Kiến trúc Transformer (Transformer Architecture)](/en/terms/kiến-trúc-transformer-transformer-architecture/)
- [Embedding (Biểu diễn vector)](/en/terms/embedding-biểu-diễn-vector/)
- [Cơ chế chú ý (Attention Mechanism)](/en/terms/cơ-chế-chú-ý-attention-mechanism/)
- [RoPE (Rotary Positional Embedding)](/en/terms/rope-rotary-positional-embedding/)
