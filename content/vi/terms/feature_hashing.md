---
title: "Feature hashing"
term_id: "feature_hashing"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "text-mining", "optimization"]
difficulty: 3
weight: 1
slug: "feature_hashing"
aliases:
  - /vi/terms/feature_hashing/
date: "2026-07-18T15:53:20.659749Z"
lastmod: "2026-07-18T16:38:07.757212Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một kỹ thuật ánh xạ các đặc trưng thưa thớt có chiều cao thành một vectơ kích thước cố định bằng cách sử dụng hàm băm."
---

## Definition

Feature hashing, còn được gọi là thủ thuật băm (hashing trick), cho phép các mô hình học máy xử lý không gian đặc trưng lớn và thưa thớt mà không cần duy trì ánh xạ tường minh giữa các đặc trưng và chỉ mục. Bằng cách áp dụng...

### Summary

Một kỹ thuật ánh xạ các đặc trưng thưa thớt có chiều cao thành một vectơ kích thước cố định bằng cách sử dụng hàm băm.

## Key Concepts

- Hàm băm
- Vectơ thưa thớt
- Giảm chiều dữ liệu
- Hiệu quả bộ nhớ

## Use Cases

- Phân loại văn bản với từ vựng lớn
- Hệ thống gợi ý với tập hợp mặt hàng khổng lồ
- Xử lý dữ liệu luồng theo thời gian thực

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding (Mã hóa một-hot)](/en/terms/one-hot-encoding-mã-hóa-một-hot/)
- [Bag of Words (Túi từ)](/en/terms/bag-of-words-túi-từ/)
- [Dimensionality reduction (Giảm chiều dữ liệu)](/en/terms/dimensionality-reduction-giảm-chiều-dữ-liệu/)
- [Sparse matrix (Ma trận thưa)](/en/terms/sparse-matrix-ma-trận-thưa/)
