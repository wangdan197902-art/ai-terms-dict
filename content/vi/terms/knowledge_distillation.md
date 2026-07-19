---
title: "Knowledge Distillation"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T15:58:59.615781Z"
lastmod: "2026-07-18T16:38:07.772653Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Knowledge Distillation (Chưng cất tri thức) là một kỹ thuật nén mô hình, trong đó một mô hình nhỏ hơn (sinh viên) học cách bắt chước hành vi của một mô hình lớn hơn (giáo viên)."
---
## Definition

Knowledge Distillation là một phương pháp học máy dùng để nén một mạng nơ-ron lớn, phức tạp (mô hình giáo viên) thành một mạng nhỏ gọn, hiệu quả hơn (mô hình sinh viên). Mô hình sinh viên được huấn luyện để

### Summary

Knowledge Distillation (Chưng cất tri thức) là một kỹ thuật nén mô hình, trong đó một mô hình nhỏ hơn (sinh viên) học cách bắt chước hành vi của một mô hình lớn hơn (giáo viên).

## Key Concepts

- Mô hình Giáo viên-Sinh viên
- Nén mô hình
- Nhãn mềm (Soft Targets)
- Hiệu quả

## Use Cases

- Triển khai mô hình trên thiết bị biên
- Giảm độ trễ suy luận
- Giảm chi phí điện toán đám mây

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression (Nén mô hình)](/en/terms/model-compression-nén-mô-hình/)
- [Pruning (Cắt tỉa mô hình)](/en/terms/pruning-cắt-tỉa-mô-hình/)
- [Quantization (Lượng tử hóa)](/en/terms/quantization-lượng-tử-hóa/)
- [Neural Networks (Mạng nơ-ron)](/en/terms/neural-networks-mạng-nơ-ron/)
