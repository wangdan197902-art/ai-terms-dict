---
title: Feature scaling
term_id: feature_scaling
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- statistics
- Optimization
difficulty: 2
weight: 1
slug: feature_scaling
date: '2026-07-18T15:53:20.659781Z'
lastmod: '2026-07-18T16:38:07.757446Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Quy trình chuẩn hóa phạm vi của các biến độc lập hoặc đặc trưng của dữ
  liệu để đảm bảo tính đồng nhất về độ lớn.
---
## Definition

Feature scaling chuẩn hóa phạm vi của các biến đầu vào để ngăn chặn các đặc trưng có độ lớn lớn hơn chi phối quá trình học. Các phương pháp phổ biến bao gồm chuẩn hóa (scaling min-max) và chuẩn hóa...

### Summary

Quy trình chuẩn hóa phạm vi của các biến độc lập hoặc đặc trưng của dữ liệu để đảm bảo tính đồng nhất về độ lớn.

## Key Concepts

- Chuẩn hóa
- Tiêu chuẩn hóa
- Hạ gradient
- Tiền xử lý dữ liệu

## Use Cases

- Huấn luyện mạng nơ-ron
- Phân cụm K-means
- Máy vectơ hỗ trợ (SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling (Scaling Min-Max)](/en/terms/min-max-scaling-scaling-min-max/)
- [Z-score Normalization (Chuẩn hóa Z-score)](/en/terms/z-score-normalization-chuẩn-hóa-z-score/)
- [Data preprocessing (Tiền xử lý dữ liệu)](/en/terms/data-preprocessing-tiền-xử-lý-dữ-liệu/)
- [Gradient Descent (Hạ gradient)](/en/terms/gradient-descent-hạ-gradient/)
