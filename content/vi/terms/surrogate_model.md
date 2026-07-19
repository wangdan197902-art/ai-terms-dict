---
title: Mô hình thay thế
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T16:13:26.365935Z'
lastmod: '2026-07-18T16:38:07.809005Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một mô hình toán học đơn giản hóa được sử dụng để xấp xỉ hành vi của
  một mô hình phức tạp hơn, tốn kém tính toán hoặc không thể truy cập trực tiếp.
---
## Definition

Trong học máy và tối ưu hóa, mô hình thay thế đóng vai trò là đại diện cho một hàm mục tiêu khó đánh giá trực tiếp. Nó được huấn luyện trên các cặp đầu vào-đầu ra từ mô hình gốc để xấp xỉ hành vi của nó.

### Summary

Một mô hình toán học đơn giản hóa được sử dụng để xấp xỉ hành vi của một mô hình phức tạp hơn, tốn kém tính toán hoặc không thể truy cập trực tiếp.

## Key Concepts

- Xấp xỉ mô hình
- Tối ưu hóa hộp đen
- Hiệu quả tính toán
- Mô hình đại diện

## Use Cases

- Tối ưu hóa siêu tham số
- Tăng tốc mô phỏng thiết kế kỹ thuật
- Phân tích độ nhạy của các hệ thống phức tạp

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Tối ưu hóa Bayes (Bayesian Optimization)](/en/terms/tối-ưu-hóa-bayes-bayesian-optimization/)
- [Quá trình Gaussian (Gaussian Process)](/en/terms/quá-trình-gaussian-gaussian-process/)
- [Hàm hộp đen (Black-Box Function)](/en/terms/hàm-hộp-đen-black-box-function/)
- [Máy giả lập (Emulator)](/en/terms/máy-giả-lập-emulator/)
