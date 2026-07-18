---
title: "Hàm Tanh"
term_id: "tanh"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "mathematics"]
difficulty: 2
weight: 1
slug: "tanh"
aliases:
  - /vi/terms/tanh/
date: "2026-07-18T16:13:39.910171Z"
lastmod: "2026-07-18T16:38:07.809855Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Tanh, hay hàm tiếp tuyến hyperbol, là một hàm kích hoạt ánh xạ các giá trị đầu vào vào khoảng giá trị từ -1 đến 1."
---

## Definition

Hàm tiếp tuyến hyperbol (Tanh) là một hàm kích hoạt phi tuyến thường được sử dụng trong mạng nơ-ron. Nó nén các giá trị đầu vào vào khoảng (-1, 1), cung cấp các đầu ra có tâm bằng không, điều này giúp...

### Summary

Tanh, hay hàm tiếp tuyến hyperbol, là một hàm kích hoạt ánh xạ các giá trị đầu vào vào khoảng giá trị từ -1 đến 1.

## Key Concepts

- Hàm kích hoạt
- Phi tuyến tính
- Đầu ra có tâm bằng không
- Lan truyền ngược

## Use Cases

- Mạng nơ-ron hồi quy (RNN)
- Cổng tế bào LSTM
- Các lớp ẩn trong MLP

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (Hàm Sigmoid)](/en/terms/sigmoid-hàm-sigmoid/)
- [relu (Hàm ReLU)](/en/terms/relu-hàm-relu/)
- [neural_networks (Mạng nơ-ron)](/en/terms/neural_networks-mạng-nơ-ron/)
