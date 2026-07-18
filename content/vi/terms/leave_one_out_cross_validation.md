---
title: "Kiểm định chéo bỏ qua một mẫu (Leave-one-out cross-validation)"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /vi/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:00:34.329594Z"
lastmod: "2026-07-18T16:38:07.775477Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một kỹ thuật lấy mẫu lại nghiêm ngặt, trong đó mô hình được huấn luyện trên tất cả các mẫu trừ một mẫu và được kiểm tra trên mẫu bị loại bỏ duy nhất đó, lặp lại cho mọi điểm dữ liệu."
---

## Definition

Kiểm định chéo bỏ qua một mẫu (LOOCV) là một trường hợp cụ thể của kiểm định chéo k-fold, trong đó k bằng số lượng mẫu trong tập dữ liệu. Nó cung cấp ước lượng gần như không chệch về hiệu suất của mô hình bằng cách huấn luyện trên n-1 mẫu và kiểm tra trên mẫu còn lại, lặp lại quá trình này cho từng điểm dữ liệu trong tập dữ liệu.

### Summary

Một kỹ thuật lấy mẫu lại nghiêm ngặt, trong đó mô hình được huấn luyện trên tất cả các mẫu trừ một mẫu và được kiểm tra trên mẫu bị loại bỏ duy nhất đó, lặp lại cho mọi điểm dữ liệu.

## Key Concepts

- Lấy mẫu lại
- Đánh giá mô hình
- Sự đánh đổi Bias-Variance
- Chi phí tính toán

## Use Cases

- Đánh giá mô hình trên các tập dữ liệu y tế nhỏ
- Điều chỉnh siêu tham số khi dữ liệu khan hiếm
- So sánh hiệu suất thuật toán một cách nghiêm ngặt

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [kiểm định chéo k-fold (k-fold cross-validation)](/en/terms/kiểm-định-chéo-k-fold-k-fold-cross-validation/)
- [chia tập train/test (train_test_split)](/en/terms/chia-tập-train-test-train_test_split/)
- [bootstrap](/en/terms/bootstrap/)
- [điểm số kiểm định chéo (cross_validation_score)](/en/terms/điểm-số-kiểm-định-chéo-cross_validation_score/)
