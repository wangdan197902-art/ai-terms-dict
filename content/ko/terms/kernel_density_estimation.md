---
title: "커널 밀도 추정"
term_id: "kernel_density_estimation"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "probability", "data-analysis"]
difficulty: 3
weight: 1
slug: "kernel_density_estimation"
aliases:
  - /ko/terms/kernel_density_estimation/
date: "2026-07-18T16:00:54.436693Z"
lastmod: "2026-07-18T16:38:06.857053Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "유한한 데이터 표본을 바탕으로 확률 변수의 확률 밀도 함수를 추정하는 비모수적 방법입니다."
---

## Definition

커널 밀도 추정(KDE)은 이산적인 데이터 점을 부드럽게(smoothing) 하여 연속적인 확률 분포 곡선을 생성하는 기본 통계 기법입니다. 일반적으로 가우시안(Gaussian) 커널 함수와 같은 커널 함수를 각 데이터 점에 배치하고 이를 합산하여 전체 데이터의 확률 밀도를 추정합니다. 히스토그램과 달리 계급(bin)의 선택에 민감하지 않으며 데이터의 실제 분포 형태를 더 자연스럽게 보여줍니다.

### Summary

유한한 데이터 표본을 바탕으로 확률 변수의 확률 밀도 함수를 추정하는 비모수적 방법입니다.

## Key Concepts

- 확률 밀도 함수
- 비모수 통계
- 부드러운 처리(스무딩)
- 가우시안 커널

## Use Cases

- 탐색적 데이터 분석(EDA)
- 단변량 데이터의 이상치 탐지
- 데이터셋 내 특징(feature) 분포 시각화

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

- [히스토그램 (Histogram)](/en/terms/히스토그램-histogram/)
- [파르젠 윈도우 (Parzen Window)](/en/terms/파르젠-윈도우-parzen-window/)
- [대역폭 선택 (Bandwidth Selection)](/en/terms/대역폭-선택-bandwidth-selection/)
- [Scipy Stats (Scipy 통계 모듈)](/en/terms/scipy-stats-scipy-통계-모듈/)
