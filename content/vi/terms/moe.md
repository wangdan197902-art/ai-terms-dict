---
title: "Hỗn hợp Chuyên gia (Mixture of Experts)"
term_id: "moe"
category: "basic_concepts"
subcategory: ""
tags: ["Architecture", "Efficiency", "LLMs"]
difficulty: 4
weight: 1
slug: "moe"
date: "2026-07-18T16:04:03.260420Z"
lastmod: "2026-07-18T16:38:07.784266Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một mẫu kiến trúc kết hợp nhiều mạng nơ-ron chuyên biệt (chuyên gia) thông qua cơ chế cổng để xử lý đầu vào."
---
## Definition

Hỗn hợp Chuyên gia (MoE) là một kiến trúc học máy được thiết kế để cải thiện hiệu quả và khả năng mở rộng. Thay vì sử dụng một mô hình lớn duy nhất cho tất cả các nhiệm vụ, MoE sử dụng nhiều mô hình nhỏ hơn gọi là 'chuyên gia', chỉ kích hoạt những chuyên gia phù hợp nhất với từng đầu vào cụ thể.

### Summary

Một mẫu kiến trúc kết hợp nhiều mạng nơ-ron chuyên biệt (chuyên gia) thông qua cơ chế cổng để xử lý đầu vào.

## Key Concepts

- Kích hoạt Dớt (Sparse Activation)
- Mạng Cổng (Gating Network)
- Chuyên môn hóa của Chuyên gia
- Khả năng Mở rộng

## Use Cases

- Huấn luyện các mô hình ngôn ngữ lớn một cách hiệu quả về chi phí tính toán
- Giảm độ trễ suy luận cho các mô hình khổng lồ
- Xử lý đa dạng các loại đầu vào trong các hệ thống đa phương thức

## Related Terms

- [Sparse Transformers (Transformer thưa)](/en/terms/sparse-transformers-transformer-thưa/)
- [Conditional Computation (Tính toán điều kiện)](/en/terms/conditional-computation-tính-toán-điều-kiện/)
- [Large Language Models (Mô hình ngôn ngữ lớn)](/en/terms/large-language-models-mô-hình-ngôn-ngữ-lớn/)
- [Neural Architecture Search (Tìm kiếm kiến trúc thần kinh)](/en/terms/neural-architecture-search-tìm-kiếm-kiến-trúc-thần-kinh/)
