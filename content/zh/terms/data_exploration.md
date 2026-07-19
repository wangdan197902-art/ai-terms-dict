---
title: "数据探索"
term_id: "data_exploration"
category: "training_techniques"
subcategory: ""
tags: ["analysis", "preprocessing", "visualization"]
difficulty: 2
weight: 1
slug: "data_exploration"
date: "2026-07-18T11:12:36.731239Z"
lastmod: "2026-07-18T11:44:45.474577Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "在正式建模之前，对数据集进行初步分析，以发现模式、识别异常并验证假设。"
---
## Definition

数据探索，通常称为探索性数据分析（EDA），是机器学习工作流程中至关重要的初步步骤。它涉及总结数据的主要特征，经常使用可视化技术来揭示数据的内在结构和分布情况。

### Summary

在正式建模之前，对数据集进行初步分析，以发现模式、识别异常并验证假设。

## Key Concepts

- 探索性数据分析
- 可视化
- 模式识别
- 异常检测

## Use Cases

- 在模型训练前识别特征之间的相关性
- 检测和处理缺失值或异常值
- 验证数据质量和分布假设

## Code Example

```python
import pandas as pd
import seaborn as sns
df = pd.read_csv('data.csv')
sns.pairplot(df)
plt.show()
```

## Related Terms

- [feature_engineering (特征工程)](/en/terms/feature_engineering-特征工程/)
- [data_cleaning (数据清洗)](/en/terms/data_cleaning-数据清洗/)
- [EDA (探索性数据分析)](/en/terms/eda-探索性数据分析/)
- [statistical_analysis (统计分析)](/en/terms/statistical_analysis-统计分析/)
