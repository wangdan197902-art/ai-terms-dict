---
title: Điều chỉnh Prompt
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T16:08:49.733154Z'
lastmod: '2026-07-18T16:38:07.795691Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một phương pháp tinh chỉnh hiệu quả về tham số, tối ưu hóa các embedding
  đầu vào liên tục thay vì cập nhật toàn bộ trọng số mô hình.
---
## Definition

Điều chỉnh prompt liên quan đến việc thêm các prompt mềm có thể huấn luyện (các vector liên tục) vào lớp đầu vào của mô hình ngôn ngữ đã được huấn luyện trước, trong khi giữ nguyên các tham số nền tảng của mô hình. Cách tiếp cận này cho phép

### Summary

Một phương pháp tinh chỉnh hiệu quả về tham số, tối ưu hóa các embedding đầu vào liên tục thay vì cập nhật toàn bộ trọng số mô hình.

## Key Concepts

- prompt mềm
- hiệu quả tham số
- trọng số cố định
- học few-shot

## Use Cases

- Thích ứng LLM cho các lĩnh vực cụ thể
- Tinh chỉnh với nguồn lực thấp
- Tối ưu hóa học đa nhiệm

## Related Terms

- [PEFT (Fine-tuning hiệu quả về tham số)](/en/terms/peft-fine-tuning-hiệu-quả-về-tham-số/)
- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [in-context learning (Học trong ngữ cảnh)](/en/terms/in-context-learning-học-trong-ngữ-cảnh/)
- [fine-tuning (Tinh chỉnh)](/en/terms/fine-tuning-tinh-chỉnh/)
