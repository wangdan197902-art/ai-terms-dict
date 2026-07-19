---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
date: "2026-07-18T16:03:47.110320Z"
lastmod: "2026-07-18T16:38:07.783376Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "MobileNet là một họ các mạng nơ-ron sâu nhẹ, được thiết kế dành cho các ứng dụng thị giác trên thiết bị di động và nhúng."
---
## Definition

MobileNet sử dụng các phép tích chập tách biệt theo chiều sâu (depthwise separable convolutions) để giảm đáng kể chi phí tính toán và kích thước mô hình so với các phép tích chập tiêu chuẩn. Kiến trúc này cho phép trích xuất đặc trưng hiệu quả trên

### Summary

MobileNet là một họ các mạng nơ-ron sâu nhẹ, được thiết kế dành cho các ứng dụng thị giác trên thiết bị di động và nhúng.

## Key Concepts

- Tích chập tách biệt theo chiều sâu
- Hiệu suất mô hình
- Điện toán biên
- Học chuyển giao

## Use Cases

- Phát hiện đối tượng thời gian thực trên điện thoại thông minh
- Phân loại ảnh trên các thiết bị IoT
- Nhận diện khuôn mặt trong ứng dụng di động

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (Mạng nơ-ron xáo trộn)](/en/terms/shufflenet-mạng-nơ-ron-xáo-trộn/)
- [SqueezeNet (Mạng nơ-ron nén)](/en/terms/squeezenet-mạng-nơ-ron-nén/)
- [EfficientNet (Mạng nơ-ron hiệu quả)](/en/terms/efficientnet-mạng-nơ-ron-hiệu-quả/)
- [Convolutional Neural Network (Mạng nơ-ron tích chập)](/en/terms/convolutional-neural-network-mạng-nơ-ron-tích-chập/)
