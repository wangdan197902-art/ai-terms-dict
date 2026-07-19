---
title: Hồi quy Spike-and-slab
term_id: spike_and_slab_regression
category: basic_concepts
subcategory: ''
tags:
- statistics
- bayesian
- Regression
difficulty: 4
weight: 1
slug: spike_and_slab_regression
date: '2026-07-18T16:12:58.594161Z'
lastmod: '2026-07-18T16:38:07.807529Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một phương pháp chọn biến Bayes sử dụng tiên nghiệm hỗn hợp để phân biệt
  giữa các hệ số bằng không và khác không.
---
## Definition

Hồi quy Spike-and-slab là một kỹ thuật thống kê Bayes được sử dụng cho việc chọn biến và mô hình hóa thưa. Nó sử dụng một phân phối tiên nghiệm hỗn hợp gồm hai thành phần: một 'spike' (thường là một phân phối Dirac tại 0 hoặc có phương sai rất nhỏ) đại diện cho các hệ số bằng không, và một 'slab' (thường là một phân phối chuẩn rộng) đại diện cho các hệ số khác không. Phương pháp này cho phép mô hình tự động loại bỏ các biến không liên quan trong khi vẫn giữ lại những biến có ý nghĩa thống kê.

### Summary

Một phương pháp chọn biến Bayes sử dụng tiên nghiệm hỗn hợp để phân biệt giữa các hệ số bằng không và khác không.

## Key Concepts

- Suy luận Bayes
- Mô hình hóa thưa
- Tiên nghiệm hỗn hợp
- Chọn biến

## Use Cases

- Phân tích dữ liệu genomics chiều cao
- Nhận diện yếu tố rủi ro tài chính
- Chọn đặc trưng trong mô hình dự đoán

## Related Terms

- [Lasso (Phương pháp hồi quy co rút với chuẩn L1)](/en/terms/lasso-phương-pháp-hồi-quy-co-rút-với-chuẩn-l1/)
- [Ridge Regression (Hồi quy Ridge/L2)](/en/terms/ridge-regression-hồi-quy-ridge-l2/)
- [Bayesian Linear Regression (Hồi quy tuyến tính Bayes)](/en/terms/bayesian-linear-regression-hồi-quy-tuyến-tính-bayes/)
- [Sparsity (Tính thưa)](/en/terms/sparsity-tính-thưa/)
