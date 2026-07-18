---
title: "Hệ số Phi"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /vi/terms/phi_coefficient/
date: "2026-07-18T16:07:47.065396Z"
lastmod: "2026-07-18T16:38:07.793042Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một thước đo thống kê về mối liên hệ giữa hai biến nhị phân."
---

## Definition

Hệ số Phi (φ) là một thước đo mối liên hệ giữa hai biến nhị phân, đóng vai trò là hệ số tương quan Pearson dành cho các biến định tính nhị phân. Giá trị của nó nằm trong khoảng từ -1 đến +1, trong đó 0 biểu thị không có mối liên hệ.

### Summary

Một thước đo thống kê về mối liên hệ giữa hai biến nhị phân.

## Key Concepts

- Biến nhị phân
- Tương quan
- Bảng ngẫu nhiên (Contingency table)
- Cường độ liên kết

## Use Cases

- Đánh giá hiệu suất của bộ phân loại nhị phân vượt ra ngoài độ chính xác
- Phân tích mối quan hệ trong dữ liệu khảo sát với câu trả lời Có/Không
- Lựa chọn đặc trưng trong các tập dữ liệu có đầu vào dạng danh mục

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramer's V (Hệ số Cramer's V)](/en/terms/cramer-s-v-hệ-số-cramer-s-v/)
- [Pearson correlation (Tương quan Pearson)](/en/terms/pearson-correlation-tương-quan-pearson/)
- [Confusion matrix (Ma trận nhầm lẫn)](/en/terms/confusion-matrix-ma-trận-nhầm-lẫn/)
- [Mutual information (Thông tin tương hỗ)](/en/terms/mutual-information-thông-tin-tương-hỗ/)
