---
title: Phi系数
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T11:30:05.607465Z'
lastmod: '2026-07-18T11:44:45.542716Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 衡量两个二元变量之间关联程度的统计指标。
---
## Definition

Phi系数（φ）是用于衡量两个二元变量之间关联程度的指标，可视为二值变量的皮尔逊相关系数。其取值范围为-1到+1，其中0表示无关联。

### Summary

衡量两个二元变量之间关联程度的统计指标。

## Key Concepts

- 二元变量
- 相关性
- 列联表
- 关联强度

## Use Cases

- 评估二元分类器在准确率之外的性能
- 分析具有“是/否”回复的调查数据中的关系
- 在包含分类输入的数据集中进行特征选择

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

- [Cramer's V (克拉默V系数)](/en/terms/cramer-s-v-克拉默v系数/)
- [Pearson correlation (皮尔逊相关系数)](/en/terms/pearson-correlation-皮尔逊相关系数/)
- [Confusion matrix (混淆矩阵)](/en/terms/confusion-matrix-混淆矩阵/)
- [Mutual information (互信息)](/en/terms/mutual-information-互信息/)
