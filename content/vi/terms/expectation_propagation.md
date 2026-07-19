---
title: Lan truyền kỳ vọng
term_id: expectation_propagation
category: basic_concepts
subcategory: ''
tags:
- Bayesian Methods
- inference
- Probabilistic Models
difficulty: 5
weight: 1
slug: expectation_propagation
date: '2026-07-18T15:52:13.619322Z'
lastmod: '2026-07-18T16:38:07.755639Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một thuật toán suy luận xấp xỉ được sử dụng để ước lượng các phân phối
  hậu nghiệm trong các mô hình đồ thị xác suất phức tạp.
---
## Definition

Lan truyền kỳ vọng (Expectation Propagation - EP) xấp xỉ các tích phân không giải được được bằng cách lặp đi lặp lại tinh chỉnh các xấp xỉ Gaussian cho phân phối hậu nghiệm thực sự. Nó cực tiểu hóa độ phân kỳ Kullback-Leibler giữa phân phối xấp xỉ và phân phối đích.

### Summary

Một thuật toán suy luận xấp xỉ được sử dụng để ước lượng các phân phối hậu nghiệm trong các mô hình đồ thị xác suất phức tạp.

## Key Concepts

- Xấp xỉ hậu nghiệm
- Khớp moment (Moment Matching)
- Độ phân kỳ Kullback-Leibler
- Quá trình Gaussian

## Use Cases

- Quá trình Gaussian thưa (Sparse Gaussian Processes)
- Hồi quy logistic Bayes
- Phân rã ma trận xác suất

## Related Terms

- [variational_inference (suy luận biến phân)](/en/terms/variational_inference-suy-luận-biến-phân/)
- [gaussian_processes (quá trình Gaussian)](/en/terms/gaussian_processes-quá-trình-gaussian/)
- [bayesian_inference (suy luận Bayes)](/en/terms/bayesian_inference-suy-luận-bayes/)
- [mean_field_approximation (xấp xỉ trường trung bình)](/en/terms/mean_field_approximation-xấp-xỉ-trường-trung-bình/)
