---
title: Dữ liệu có nhãn
term_id: labeled_data
category: basic_concepts
subcategory: ''
tags:
- data
- Supervised Learning
- fundamentals
difficulty: 1
weight: 1
slug: labeled_data
date: '2026-07-18T15:59:51.756841Z'
lastmod: '2026-07-18T16:38:07.774303Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Dữ liệu trong đó giá trị đầu ra hoặc mục tiêu chính xác được cung cấp
  cùng với các đặc trưng đầu vào.
---
## Definition

Dữ liệu có nhãn bao gồm các mẫu đầu vào được ghép cặp với các nhãn thực tế tương ứng, đóng vai trò là nền tảng cho học máy có giám sát. Nó cho phép các thuật toán học ánh xạ giữa đầu vào và đầu ra.

### Summary

Dữ liệu trong đó giá trị đầu ra hoặc mục tiêu chính xác được cung cấp cùng với các đặc trưng đầu vào.

## Key Concepts

- Học có giám sát
- Thực tế cơ bản (Ground Truth)
- Gán nhãn
- Biến mục tiêu

## Use Cases

- Huấn luyện bộ phân loại hình ảnh
- Xây dựng hệ thống nhận dạng giọng nói
- Mô hình dự báo trong tài chính

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (dữ liệu không nhãn)](/en/terms/unlabeled_data-dữ-liệu-không-nhãn/)
- [supervised_learning (học có giám sát)](/en/terms/supervised_learning-học-có-giám-sát/)
- [data_annotation (gán nhãn dữ liệu)](/en/terms/data_annotation-gán-nhãn-dữ-liệu/)
- [training_set (tập huấn luyện)](/en/terms/training_set-tập-huấn-luyện/)
