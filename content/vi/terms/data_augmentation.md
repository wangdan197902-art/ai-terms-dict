---
title: "Data Augmentation"
term_id: "data_augmentation"
category: "training_techniques"
subcategory: ""
tags: ["machine_learning", "preprocessing", "cv"]
difficulty: 2
weight: 1
slug: "data_augmentation"
aliases:
  - /vi/terms/data_augmentation/
date: "2026-07-18T15:46:50.868998Z"
lastmod: "2026-07-18T16:38:07.741988Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Data Augmentation (Tăng cường dữ liệu) là kỹ thuật sử dụng để tăng tính đa dạng và kích thước của tập dữ liệu huấn luyện bằng cách áp dụng các phép biến đổi lên các điểm dữ liệu hiện có."
---

## Definition

Phương pháp này mở rộng tập dữ liệu huấn luyện một cách nhân tạo bằng cách tạo ra các phiên bản biến đổi của các mẫu hiện có, chẳng hạn như xoay ảnh, thêm nhiễu vào âm thanh hoặc thay thế từ đồng nghĩa trong văn bản. Nó giúp ngăn ngừa

### Summary

Data Augmentation (Tăng cường dữ liệu) là kỹ thuật sử dụng để tăng tính đa dạng và kích thước của tập dữ liệu huấn luyện bằng cách áp dụng các phép biến đổi lên các điểm dữ liệu hiện có.

## Key Concepts

- Ngăn chặn Overfitting (Học quá khớp)
- Mở rộng Tập dữ liệu
- Khả năng Tổng quát hóa
- Phép biến đổi

## Use Cases

- Cải thiện độ bền của mô hình thị giác máy tính
- Nâng cao hiệu suất mô hình xử lý ngôn ngữ tự nhiên với lượng văn bản hạn chế
- Cân bằng các tập dữ liệu mất cân bằng

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularization (Điều chuẩn hóa)](/en/terms/regularization-điều-chuẩn-hóa/)
- [Synthetic Data (Dữ liệu Tổng hợp)](/en/terms/synthetic-data-dữ-liệu-tổng-hợp/)
- [Transfer Learning (Học chuyển giao)](/en/terms/transfer-learning-học-chuyển-giao/)
- [Overfitting (Học quá khớp)](/en/terms/overfitting-học-quá-khớp/)
