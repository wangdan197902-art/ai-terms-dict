---
title: "In-Context Learning"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:23:05.192126Z"
lastmod: "2026-07-18T16:38:07.679154Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một kỹ thuật mà mô hình học cách thực hiện nhiệm vụ bằng cách quan sát các ví dụ được cung cấp trong lời nhắc (prompt)."
---
## Definition

Học trong ngữ cảnh (In-context Learning - ICL) cho phép các mô hình ngôn ngữ lớn thích nghi với các nhiệm vụ mới mà không cần cập nhật trọng số. Bằng cách cung cấp các cặp đầu vào-đầu ra trong ngữ cảnh của lời nhắc, mô hình suy luận ra quy luật và thực hiện nhiệm vụ ngay lập tức.

### Summary

Một kỹ thuật mà mô hình học cách thực hiện nhiệm vụ bằng cách quan sát các ví dụ được cung cấp trong lời nhắc (prompt).

## Key Concepts

- Few-Shot Learning (Học vài ví dụ)
- Zero-Shot (Học không ví dụ)
- Thiết kế Lời nhắc (Prompt Design)
- Thích ứng Không cần Trọng số (Weight-Free Adaptation)

## Use Cases

- Nhanh chóng thử nghiệm khả năng của mô hình trên các tập dữ liệu mới
- Chuyển đổi nhiệm vụ động trong các đại diện trò chuyện
- Xây dựng nguyên mẫu ứng dụng AI mà không cần huấn luyện lại

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (Kỹ thuật thiết kế lời nhắc)](/en/terms/prompt-engineering-kỹ-thuật-thiết-kế-lời-nhắc/)
- [Few-Shot (Vài ví dụ)](/en/terms/few-shot-vài-ví-dụ/)
- [Zero-Shot (Không ví dụ)](/en/terms/zero-shot-không-ví-dụ/)
- [Meta-Learning (Siêu học/Học để học)](/en/terms/meta-learning-siêu-học-học-để-học/)
