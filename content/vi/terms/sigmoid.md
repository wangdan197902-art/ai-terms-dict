---
title: "Hàm Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:11:46.160273Z"
lastmod: "2026-07-18T16:38:07.804702Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một hàm toán học ánh xạ bất kỳ số thực nào thành một giá trị nằm giữa 0 và 1, tạo thành một đường cong hình chữ S."
---
## Definition

Hàm sigmoid, được xác định là σ(z) = 1 / (1 + e^-z), được sử dụng rộng rãi trong học máy để mô hình hóa xác suất. Nó nén các giá trị đầu vào vào khoảng (0, 1), khiến nó phù hợp cho các bài toán phân loại nhị phân.

### Summary

Một hàm toán học ánh xạ bất kỳ số thực nào thành một giá trị nằm giữa 0 và 1, tạo thành một đường cong hình chữ S.

## Key Concepts

- Hàm logistic
- Ánh xạ xác suất
- Vấn đề tiêu biến gradient
- Phi tuyến tính

## Use Cases

- Đầu ra phân loại nhị phân
- Hồi quy logistic
- Kích hoạt trong mạng nơ-ron nông

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Hồi quy Logistic](/en/terms/hồi-quy-logistic/)
- [Hàm kích hoạt](/en/terms/hàm-kích-hoạt/)
