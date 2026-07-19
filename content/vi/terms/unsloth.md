---
title: Unsloth
term_id: unsloth
category: basic_concepts
subcategory: ''
tags:
- Optimization
- LLM
- training
- library
difficulty: 3
weight: 1
slug: unsloth
date: '2026-07-18T16:15:44.786882Z'
lastmod: '2026-07-18T16:38:07.815005Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Unsloth là một thư viện mã nguồn mở giúp tăng tốc quá trình huấn luyện
  và suy luận của các Mô hình Ngôn ngữ Lớn (LLM) lên tới 2 lần thông qua việc tối
  ưu hóa quản lý bộ nhớ và triển khai các kernel tù
---
## Definition

Unsloth là một công cụ chuyên dụng được thiết kế để tối ưu hóa việc tinh chỉnh (fine-tuning) và triển khai các Mô hình Ngôn ngữ Lớn (LLM). Nó đạt được những bước nhảy vọt về tốc độ và giảm đáng kể lượng bộ nhớ bằng cách thay thế các hàm chuẩn của PyTorch...

### Summary

Unsloth là một thư viện mã nguồn mở giúp tăng tốc quá trình huấn luyện và suy luận của các Mô hình Ngôn ngữ Lớn (LLM) lên tới 2 lần thông qua việc tối ưu hóa quản lý bộ nhớ và triển khai các kernel tùy chỉnh.

## Key Concepts

- Tối ưu hóa Bộ nhớ
- Kernel Tùy chỉnh
- Tinh chỉnh LLM
- Tăng tốc Tốc độ

## Use Cases

- Tinh chỉnh LLM trên các nguồn lực GPU hạn chế
- Tăng tốc các quy trình suy luận
- Giảm chi phí điện toán đám mây cho việc huấn luyện

## Code Example

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-2-7b-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True
)
```

## Related Terms

- [LoRA (Kỹ thuật tinh chỉnh hiệu quả)](/en/terms/lora-kỹ-thuật-tinh-chỉnh-hiệu-quả/)
- [PyTorch (Thư viện học sâu)](/en/terms/pytorch-thư-viện-học-sâu/)
- [Hugging Face (Nền tảng mô hình AI)](/en/terms/hugging-face-nền-tảng-mô-hình-ai/)
- [Flash Attention (Cơ chế chú ý nhanh)](/en/terms/flash-attention-cơ-chế-chú-ý-nhanh/)
