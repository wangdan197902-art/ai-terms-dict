---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /vi/terms/relu/
date: "2026-07-18T15:36:56.894148Z"
lastmod: "2026-07-18T16:38:07.713002Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Hàm đơn vị tuyến tính được chỉnh lưu (ReLU) là một hàm kích hoạt, trả về đầu vào nếu dương, ngược lại trả về 0."
---

## Definition

ReLU được sử dụng rộng rãi trong các mạng nơ-ron học sâu do hiệu quả tính toán cao và khả năng giảm thiểu vấn đề suy giảm gradient. Được định nghĩa toán học là f(x) = max(0, x), nó đưa tính phi tuyến vào mạng mà không làm tăng đáng kể chi phí tính toán.

### Summary

Hàm đơn vị tuyến tính được chỉnh lưu (ReLU) là một hàm kích hoạt, trả về đầu vào nếu dương, ngược lại trả về 0.

## Key Concepts

- Tính phi tuyến
- Hàm kích hoạt
- Suy giảm gradient
- Tuyến tính từng khúc

## Use Cases

- Các lớp ẩn trong CNN
- Mạng truyền thẳng sâu
- Mô hình nhận dạng hình ảnh

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (Hàm sigmoid)](/en/terms/sigmoid-hàm-sigmoid/)
- [Tanh (Hàm hyperbolic tangent)](/en/terms/tanh-hàm-hyperbolic-tangent/)
- [Leaky ReLU (ReLU rò rỉ)](/en/terms/leaky-relu-relu-rò-rỉ/)
- [Neural Network (Mạng nơ-ron)](/en/terms/neural-network-mạng-nơ-ron/)
