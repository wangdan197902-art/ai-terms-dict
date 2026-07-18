---
title: "Chưng cất kiến thức"
term_id: "distillation"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "compression", "model_efficiency"]
difficulty: 3
weight: 1
slug: "distillation"
aliases:
  - /vi/terms/distillation/
date: "2026-07-18T15:24:27.512683Z"
lastmod: "2026-07-18T16:38:07.682728Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Chưng cất kiến thức là một kỹ thuật nén mô hình, trong đó một mô hình nhỏ hơn (mô hình sinh viên) học cách bắt chước hành vi của một mô hình lớn hơn (mô hình giáo viên)."
---

## Definition

Quá trình này liên quan đến việc chuyển giao kiến thức từ một mạng nơ-ron 'giáo viên' phức tạp, hiệu suất cao sang một mạng 'sinh viên' đơn giản và hiệu quả hơn. Mô hình sinh viên không chỉ học từ các nhãn cứng (hard labels) mà còn từ các đầu ra mềm (soft outputs) của mô hình giáo viên, giúp nó nắm bắt được thông tin chi tiết về phân phối xác suất của dữ liệu.

### Summary

Chưng cất kiến thức là một kỹ thuật nén mô hình, trong đó một mô hình nhỏ hơn (mô hình sinh viên) học cách bắt chước hành vi của một mô hình lớn hơn (mô hình giáo viên).

## Key Concepts

- Kiến trúc Giáo viên-Sinh viên
- Nhãn mềm (Soft Targets)
- Nén mô hình
- Hiệu suất suy luận

## Use Cases

- Triển khai các mô hình ngôn ngữ lớn trên thiết bị di động
- Giảm độ trễ trong các ứng dụng thị giác máy tính thời gian thực
- Tối ưu hóa các mô hình học sâu cho môi toán biên (edge computing)

## Related Terms

- [Lượng tử hóa (Quantization) - Giảm độ chính xác số của trọng số](/en/terms/lượng-tử-hóa-quantization-giảm-độ-chính-xác-số-của-trọng-số/)
- [Cắt tỉa (Pruning) - Loại bỏ các kết nối hoặc nơ-ron không cần thiết](/en/terms/cắt-tỉa-pruning-loại-bỏ-các-kết-nối-hoặc-nơ-ron-không-cần-thiết/)
- [Học chuyển giao (Transfer Learning) - Áp dụng kiến thức từ tác vụ này sang tác vụ khác](/en/terms/học-chuyển-giao-transfer-learning-áp-dụng-kiến-thức-từ-tác-vụ-này-sang-tác-vụ-khác/)
- [Tìm kiếm kiến trúc nơ-ron (Neural Architecture Search) - Tự động tìm kiến trúc mô hình tốt nhất](/en/terms/tìm-kiếm-kiến-trúc-nơ-ron-neural-architecture-search-tự-động-tìm-kiến-trúc-mô-hình-tốt-nhất/)
