---
title: "Ma trận nhầm lẫn"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /vi/terms/confusion_matrix/
date: "2026-07-18T15:45:55.032771Z"
lastmod: "2026-07-18T16:38:07.739168Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một bảng dùng để mô tả hiệu suất của một mô hình phân loại trên một tập dữ liệu kiểm thử."
---

## Definition

Ma trận nhầm lẫn là một bố cục bảng cụ thể cho phép trực quan hóa hiệu suất của một thuật toán, thường là thuật toán học có giám sát. Nó hiển thị số lượng các kết quả dương tính thật (true positive), âm tính thật (true negative), dương tính giả (false positive) và âm tính giả (false negative).

### Summary

Một bảng dùng để mô tả hiệu suất của một mô hình phân loại trên một tập dữ liệu kiểm thử.

## Key Concepts

- Dương tính thật (True Positives)
- Âm tính giả (False Negatives)
- Độ chính xác (Precision)
- Độ nhạy (Recall)

## Use Cases

- Đánh giá các bộ phân loại nhị phân
- Phân tích hiệu suất phân loại đa lớp
- Gỡ lỗi thiên vị mô hình trên các tập dữ liệu mất cân bằng

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (Độ chính xác)](/en/terms/precision-độ-chính-xác/)
- [recall (Độ nhạy)](/en/terms/recall-độ-nhạy/)
- [F1 score (Chỉ số F1)](/en/terms/f1-score-chỉ-số-f1/)
- [ROC curve (Đường cong ROC)](/en/terms/roc-curve-đường-cong-roc/)
