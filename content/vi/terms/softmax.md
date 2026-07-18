---
title: "Softmax"
term_id: "softmax"
category: "basic_concepts"
subcategory: ""
tags: ["math", "neural-networks", "classification"]
difficulty: 2
weight: 1
slug: "softmax"
aliases:
  - /vi/terms/softmax/
date: "2026-07-18T15:37:23.306463Z"
lastmod: "2026-07-18T16:38:07.714292Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một hàm toán học chuyển đổi một vector các điểm số thực trị tùy ý thành một phân phối xác suất."
---

## Definition

Softmax được sử dụng rộng rãi trong lớp đầu ra của mạng nơ-ron cho các tác vụ phân loại đa lớp. Nó nhận một vector các logit thô và chuẩn hóa chúng sao cho mỗi phần tử đại diện cho một xác suất có thể xảy ra.

### Summary

Một hàm toán học chuyển đổi một vector các điểm số thực trị tùy ý thành một phân phối xác suất.

## Key Concepts

- Phân phối xác suất
- Logits
- Chuẩn hóa
- Phân loại đa lớp

## Use Cases

- Lớp đầu ra phân loại ảnh
- Dự đoán token trong mô hình ngôn ngữ
- Phân loại đa nhãn

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (Hàm tìm chỉ mục của giá trị lớn nhất)](/en/terms/argmax-hàm-tìm-chỉ-mục-của-giá-trị-lớn-nhất/)
- [Cross-Entropy Loss (Hàm mất mát Entropy chéo)](/en/terms/cross-entropy-loss-hàm-mất-mát-entropy-chéo/)
- [Logits (Các điểm số thô trước khi chuẩn hóa)](/en/terms/logits-các-điểm-số-thô-trước-khi-chuẩn-hóa/)
- [Neural Network (Mạng nơ-ron)](/en/terms/neural-network-mạng-nơ-ron/)
