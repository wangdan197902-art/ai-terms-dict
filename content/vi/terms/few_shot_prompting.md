---
title: "Gợi ý ít ví dụ (Few-Shot Prompting)"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /vi/terms/few_shot_prompting/
date: "2026-07-18T15:34:47.846629Z"
lastmod: "2026-07-18T16:38:07.709040Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Gợi ý ít ví dụ là kỹ thuật cung cấp cho các mô hình ngôn ngữ lớn (LLM) một số lượng nhỏ các ví dụ đầu vào-đầu ra trong lời nhắc để hướng dẫn hành vi của chúng."
---

## Definition

Phương pháp này tận dụng khả năng học trong ngữ cảnh (in-context learning) của các mô hình ngôn ngữ lớn bằng cách cung cấp trực tiếp một vài ví dụ minh họa trong lời nhắc. Không giống như tinh chỉnh (fine-tuning) yêu cầu cập nhật trọng số mô hình, kỹ thuật này chỉ thay đổi đầu vào để hướng dẫn mô hình thực hiện nhiệm vụ cụ thể mà không cần huấn luyện lại.

### Summary

Gợi ý ít ví dụ là kỹ thuật cung cấp cho các mô hình ngôn ngữ lớn (LLM) một số lượng nhỏ các ví dụ đầu vào-đầu ra trong lời nhắc để hướng dẫn hành vi của chúng.

## Key Concepts

- Học trong ngữ cảnh
- Kỹ thuật gợi ý (Prompt engineering)
- Hướng dẫn dựa trên ví dụ
- So sánh với zero-shot

## Use Cases

- Định dạng phân tích cảm xúc
- Thích ứng phong cách mã nguồn
- Trích xuất dữ liệu có cấu trúc

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (không ví dụ)](/en/terms/zero_shot-không-ví-dụ/)
- [prompt_engineering (kỹ thuật gợi ý)](/en/terms/prompt_engineering-kỹ-thuật-gợi-ý/)
- [in_context_learning (học trong ngữ cảnh)](/en/terms/in_context_learning-học-trong-ngữ-cảnh/)
- [llm (mô hình ngôn ngữ lớn)](/en/terms/llm-mô-hình-ngôn-ngữ-lớn/)
