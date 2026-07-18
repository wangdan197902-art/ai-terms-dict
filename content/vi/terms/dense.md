---
title: "Dense (Mật độ cao/Lớp kết nối đầy đủ)"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /vi/terms/dense/
date: "2026-07-18T15:49:14.511969Z"
lastmod: "2026-07-18T16:38:07.748297Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một lớp hoặc tensor trong đó mọi phần tử đều được kết nối với mọi phần tử của lớp hoặc chiều trước đó."
---

## Definition

Trong mạng nơ-ron, 'dense' (mật độ cao) đề cập đến các lớp kết nối đầy đủ (fully connected), nơi mỗi nơ-ron nhận đầu vào từ tất cả các nơ-ron ở lớp trước đó. Điều này tương phản với các kết nối thưa thớt thường thấy trong các mạng tích chập (convolutional) hoặc...

### Summary

Một lớp hoặc tensor trong đó mọi phần tử đều được kết nối với mọi phần tử của lớp hoặc chiều trước đó.

## Key Concepts

- Kết nối đầy đủ (Fully Connected)
- Ma trận trọng số (Weight Matrix)
- Hàm kích hoạt (Activation Function)
- Tích hợp đặc trưng (Feature Integration)

## Use Cases

- Các lớp phân loại cuối cùng trong MLP
- Hợp nhất đặc trưng trong các mô hình lai
- Các bài toán hồi quy đơn giản

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Mạng nơ-ron truyền tiến)](/en/terms/feedforward-neural-network-mạng-nơ-ron-truyền-tiến/)
- [Backpropagation (Lan truyền ngược)](/en/terms/backpropagation-lan-truyền-ngược/)
- [ReLU (Hàm kích hoạt ReLU)](/en/terms/relu-hàm-kích-hoạt-relu/)
- [Bias Term (Số hạng thiên vị)](/en/terms/bias-term-số-hạng-thiên-vị/)
