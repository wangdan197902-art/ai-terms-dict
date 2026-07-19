---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:37.915781Z"
lastmod: "2026-07-18T16:38:07.688912Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Điều chỉnh Rank Thấp là một phương pháp tinh chỉnh hiệu quả về tham số, chèn các ma trận phân rã rank có thể huấn luyện vào các trọng số mô hình hiện có."
---
## Definition

LoRA đóng băng các trọng số đã được huấn luyện trước và chèn các ma trận phân rã có thể huấn luyện vào mỗi lớp của kiến trúc Transformer. Bằng cách chỉ tối ưu hóa các ma trận rank thấp này, LoRA giảm đáng kể

### Summary

Điều chỉnh Rank Thấp là một phương pháp tinh chỉnh hiệu quả về tham số, chèn các ma trận phân rã rank có thể huấn luyện vào các trọng số mô hình hiện có.

## Key Concepts

- Tinh chỉnh hiệu quả tham số
- Phân rã Rank
- Đóng băng trọng số
- Mô-đun Adapter

## Use Cases

- Tùy chỉnh LLM
- Thích ứng theo lĩnh vực cụ thể
- Huấn luyện trong điều kiện hạn chế tài nguyên

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Điều chỉnh hiệu quả tham số)](/en/terms/peft-điều-chỉnh-hiệu-quả-tham-số/)
- [Tinh chỉnh (Fine-Tuning)](/en/terms/tinh-chỉnh-fine-tuning/)
- [Lượng tử hóa](/en/terms/lượng-tử-hóa/)
