---
title: TensorFlow Hub
term_id: tensorflow_hub
category: basic_concepts
subcategory: ''
tags:
- tensorflow
- libraries
- Transfer Learning
difficulty: 3
weight: 1
slug: tensorflow_hub
date: '2026-07-18T16:13:53.146277Z'
lastmod: '2026-07-18T16:38:07.810192Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Kho lưu trữ các mô-đun học máy có thể tái sử dụng, cho phép học chuyển
  giao với các mô hình đã được huấn luyện trước.
---
## Definition

TensorFlow Hub là một nền tảng để xuất bản và tái sử dụng các thành phần học máy. Nó cho phép các nhà phát triển truy cập vào các mô hình đã được huấn luyện trước cho nhiều tác vụ khác nhau như phân loại ảnh, nhúng văn bản, v.v.

### Summary

Kho lưu trữ các mô-đun học máy có thể tái sử dụng, cho phép học chuyển giao với các mô hình đã được huấn luyện trước.

## Key Concepts

- Học chuyển giao
- Tái sử dụng mô-đun
- Mô hình đã huấn luyện trước
- Hiệu quả

## Use Cases

- Tạo mẫu mô hình nhanh chóng
- Giảm chi phí huấn luyện
- Triển khai các mô hình NLP/CV tiên tiến nhất

## Code Example

```python
import tensorflow_hub as hub
module = hub.load('https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5')
```

## Related Terms

- [Hugging Face (Nền tảng chia sẻ mô hình AI)](/en/terms/hugging-face-nền-tảng-chia-sẻ-mô-hình-ai/)
- [Keras Applications (Các ứng dụng mẫu trong Keras)](/en/terms/keras-applications-các-ứng-dụng-mẫu-trong-keras/)
- [Transfer Learning (Học chuyển giao)](/en/terms/transfer-learning-học-chuyển-giao/)
- [Model Zoo (Kho lưu trữ mô hình)](/en/terms/model-zoo-kho-lưu-trữ-mô-hình/)
