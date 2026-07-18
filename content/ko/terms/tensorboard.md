---
title: "TensorBoard"
term_id: "tensorboard"
category: "basic_concepts"
subcategory: ""
tags: ["tensorflow", "tools", "visualization"]
difficulty: 2
weight: 1
slug: "tensorboard"
aliases:
  - /ko/terms/tensorboard/
date: "2026-07-18T16:18:04.373257Z"
lastmod: "2026-07-18T16:38:06.913887Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "머신러닝 실험을 모니터링하고 모델 성능을 디버깅하기 위한 시각화 도구 모음입니다."
---

## Definition

TensorBoard는 TensorFlow 실행 과정과 그래프를 검사하고 이해하기 위한 일련의 웹 애플리케이션입니다. 시간 경과에 따른 손실(loss) 및 정확도(accuracy)와 같은 메트릭스를 시각화하고 모델 그래프를 탐색하는 도구를 제공합니다.

### Summary

머신러닝 실험을 모니터링하고 모델 성능을 디버깅하기 위한 시각화 도구 모음입니다.

## Key Concepts

- 시각화
- 하이퍼파라미터 튜닝
- 그래프 검사
- 메트릭 추적

## Use Cases

- 훈련 수렴 디버깅
- 모델 아키텍처 비교
- 임베딩 공간 시각화

## Code Example

```python
from tensorboard.callback import TensorBoardCallback
callback = TensorBoardCallback(log_dir='./logs')
```

## Related Terms

- [MLflow (머신러닝 라이프사이클 관리 플랫폼)](/en/terms/mlflow-머신러닝-라이프사이클-관리-플랫폼/)
- [Weights & Biases (실험 추적 및 시각화 도구)](/en/terms/weights-biases-실험-추적-및-시각화-도구/)
- [TensorFlow (딥러닝 프레임워크)](/en/terms/tensorflow-딥러닝-프레임워크/)
- [Experiment Tracking (실험 추적)](/en/terms/experiment-tracking-실험-추적/)
