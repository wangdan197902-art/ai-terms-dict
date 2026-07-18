---
title: "Kết nối Trừu tượng (Residual Connection)"
term_id: "residual_connection"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "optimization", "deep_learning"]
difficulty: 3
weight: 1
slug: "residual_connection"
aliases:
  - /vi/terms/residual_connection/
date: "2026-07-18T15:37:10.128018Z"
lastmod: "2026-07-18T16:38:07.713415Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một cơ chế thêm đầu vào trực tiếp vào đầu ra của một lớp để tạo điều kiện thuận lợi cho việc truyền gradient trong các mạng sâu."
---

## Definition

Các kết nối trừu tượng, còn được gọi là kết nối bỏ qua (skip connections), cho phép gradient chảy qua mạng bằng cách thêm trực tiếp đầu vào vào đầu ra của lớp tiếp theo. Kiến trúc này giải quyết vấn đề biến mất gradient (vanishing gradient) trong các mạng nơ-ron sâu.

### Summary

Một cơ chế thêm đầu vào trực tiếp vào đầu ra của một lớp để tạo điều kiện thuận lợi cho việc truyền gradient trong các mạng sâu.

## Key Concepts

- Kết nối Bỏ qua (Skip Connections)
- Vấn đề Biến mất Gradient (Vanishing Gradient Problem)
- Học Trừu tượng Sâu (Deep Residual Learning)
- Dòng chảy Gradient (Gradient Flow)

## Use Cases

- Huấn luyện các mạng nơ-ron tích chập (CNN) sâu
- Kiến trúc Transformer
- Các mô hình phân loại ảnh

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (kết nối bỏ qua)](/en/terms/skip_connection-kết-nối-bỏ-qua/)
- [vanishing_gradient (biến mất gradient)](/en/terms/vanishing_gradient-biến-mất-gradient/)
- [deep_learning (học sâu)](/en/terms/deep_learning-học-sâu/)
- [resnet (mạng residual)](/en/terms/resnet-mạng-residual/)
