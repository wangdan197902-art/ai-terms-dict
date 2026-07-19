---
title: Ước lượng mật độ hạt nhân
term_id: kernel_density_estimation
category: basic_concepts
subcategory: ''
tags:
- statistics
- probability
- Data Analysis
difficulty: 3
weight: 1
slug: kernel_density_estimation
date: '2026-07-18T15:58:51.062756Z'
lastmod: '2026-07-18T16:38:07.772188Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một phương pháp phi tham số dùng để ước lượng hàm mật độ xác suất của
  một biến ngẫu nhiên dựa trên một mẫu dữ liệu hữu hạn.
---
## Definition

Ước lượng mật độ hạt nhân (KDE) là một kỹ thuật thống kê cơ bản làm mịn các điểm dữ liệu rời rạc để tạo ra một đường cong phân phối xác suất liên tục. Nó đặt một hàm hạt nhân, thường là hàm Gauss, lên mỗi điểm dữ liệu và tổng hợp chúng lại.

### Summary

Một phương pháp phi tham số dùng để ước lượng hàm mật độ xác suất của một biến ngẫu nhiên dựa trên một mẫu dữ liệu hữu hạn.

## Key Concepts

- Hàm mật độ xác suất
- Thống kê phi tham số
- Làm mịn dữ liệu
- Hạt nhân Gauss

## Use Cases

- Phân tích dữ liệu khám phá (EDA)
- Phát hiện bất thường trong dữ liệu đơn biến
- Trực quan hóa phân phối đặc trưng trong tập dữ liệu

## Code Example

```python
from scipy.stats import gaussian_kde
import numpy as np

data = np.random.normal(0, 1, 100)
kde = gaussian_kde(data)
x_vals = np.linspace(-3, 3, 100)
y_vals = kde(x_vals)
```

## Related Terms

- [Histogram (Biểu đồ tần suất)](/en/terms/histogram-biểu-đồ-tần-suất/)
- [Parzen Window (Cửa sổ Parzen)](/en/terms/parzen-window-cửa-sổ-parzen/)
- [Bandwidth Selection (Lựa chọn băng thông)](/en/terms/bandwidth-selection-lựa-chọn-băng-thông/)
- [Scipy Stats (Thư viện thống kê Scipy)](/en/terms/scipy-stats-thư-viện-thống-kê-scipy/)
