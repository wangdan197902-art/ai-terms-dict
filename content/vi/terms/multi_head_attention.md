---
title: Chú ý Đa đầu
term_id: multi_head_attention
category: basic_concepts
subcategory: ''
tags:
- transformer
- NLP
- Deep Learning
difficulty: 4
weight: 1
slug: multi_head_attention
date: '2026-07-18T15:27:19.519171Z'
lastmod: '2026-07-18T16:38:07.690547Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một cơ chế trong các mô hình Transformer cho phép mô hình chú ý đến thông
  tin từ các không gian biểu diễn con khác nhau đồng thời.
---
## Definition

Chú ý Đa đầu mở rộng cơ chế chú ý tiêu chuẩn bằng cách chạy nó nhiều lần song song với các phép chiếu tuyến tính khác nhau đã được học. Điều này cho phép mô hình cùng lúc chú ý đến thông...

### Summary

Một cơ chế trong các mô hình Transformer cho phép mô hình chú ý đến thông tin từ các không gian biểu diễn con khác nhau đồng thời.

## Key Concepts

- Chú ý tự thân
- Phép chiếu tuyến tính
- Nối chuỗi

## Use Cases

- Xử lý Ngôn ngữ Tự nhiên (NLP)
- Dịch máy
- Phân loại ảnh với Vision Transformers

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

- [Scaled Dot-Product Attention (Chú ý tích vô hướng có tỷ lệ)](/en/terms/scaled-dot-product-attention-chú-ý-tích-vô-hướng-có-tỷ-lệ/)
- [Transformer (Mô hình Transformer)](/en/terms/transformer-mô-hình-transformer/)
- [Embedding (Mã hóa nhúng)](/en/terms/embedding-mã-hóa-nhúng/)
