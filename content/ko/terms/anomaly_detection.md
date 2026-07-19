---
title: 이상 탐지(Anomaly detection)
term_id: anomaly_detection
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- security
- Data Analysis
difficulty: 2
weight: 1
slug: anomaly_detection
date: '2026-07-18T15:40:52.252634Z'
lastmod: '2026-07-18T16:38:06.807694Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 데이터의 대부분과 현저히 벗어난 드문 항목, 사건 또는 관측치를 식별하는 과정입니다.
---
## Definition

이상 탐지는 아웃라이어 탐지라고도 하며, 예상되는 동작에 적합하지 않은 패턴을 찾기 위해 데이터를 분석합니다. 사이버 보안, 사기 탐지 및 시스템 관리 분야에서 널리 사용되며,

### Summary

데이터의 대부분과 현저히 벗어난 드문 항목, 사건 또는 관측치를 식별하는 과정입니다.

## Key Concepts

- 아웃라이어(Outliers)
- 패턴 인식
- 사기 탐지
- 통계적 편차

## Use Cases

- 신용카드 사기 탐지
- 네트워크 침입 탐지
- 산업용 결함 진단

## Code Example

```python
from sklearn.ensemble import IsolationForest
model = IsolationForest(contamination=0.1)
model.fit(data)
```

## Related Terms

- [아웃라이어 탐지 (Outlier detection)](/en/terms/아웃라이어-탐지-outlier-detection/)
- [머신러닝 (Machine learning)](/en/terms/머신러닝-machine-learning/)
- [데이터 마이닝 (Data mining)](/en/terms/데이터-마이닝-data-mining/)
- [사기 예방 (Fraud prevention)](/en/terms/사기-예방-fraud-prevention/)
