---
title: "데이터 탐색(Data Exploration)"
term_id: "data_exploration"
category: "training_techniques"
subcategory: ""
tags: ["analysis", "preprocessing", "visualization"]
difficulty: 2
weight: 1
slug: "data_exploration"
date: "2026-07-18T15:47:25.983505Z"
lastmod: "2026-07-18T16:38:06.824651Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "공식적인 모델링 전에 데이터셋을 초기 분석하여 패턴을 발견하고 이상 징후를 파악하며 가설을 검증하는 과정입니다."
---
## Definition

데이터 탐색(탐색적 데이터 분석, EDA라고도 함)은 머신러닝 워크플로우에서 중요한 사전 단계입니다. 이 과정은 주로 시각화 도구를 사용하여 데이터의 주요 특성을 요약하고 이해하는 것을 포함합니다.

### Summary

공식적인 모델링 전에 데이터셋을 초기 분석하여 패턴을 발견하고 이상 징후를 파악하며 가설을 검증하는 과정입니다.

## Key Concepts

- 탐색적 데이터 분석(Exploratory Data Analysis)
- 시각화(Visualization)
- 패턴 인식(Pattern Recognition)
- 이상 탐지(Anomaly Detection)

## Use Cases

- 모델 훈련 전 특징(feature) 간 상관관계 식별
- 누락된 값 또는 이상치 감지 및 처리
- 데이터 품질 및 분포 가정 검증

## Code Example

```python
import pandas as pd
import seaborn as sns
df = pd.read_csv('data.csv')
sns.pairplot(df)
plt.show()
```

## Related Terms

- [feature_engineering (특징 공학)](/en/terms/feature_engineering-특징-공학/)
- [data_cleaning (데이터 클렌징)](/en/terms/data_cleaning-데이터-클렌징/)
- [EDA (탐색적 데이터 분석)](/en/terms/eda-탐색적-데이터-분석/)
- [statistical_analysis (통계 분석)](/en/terms/statistical_analysis-통계-분석/)
