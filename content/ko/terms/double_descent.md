---
title: "더블 디센트(Double Descent)"
term_id: "double_descent"
category: "basic_concepts"
subcategory: ""
tags: ["Theory", "Deep Learning", "Generalization"]
difficulty: 5
weight: 1
slug: "double_descent"
date: "2026-07-18T15:53:50.594601Z"
lastmod: "2026-07-18T16:38:06.834588Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델 복잡도가 보간 임계값(interpolation threshold)을 넘어 증가함에 따라 테스트 오차가 감소했다가 다시 증가하고, 이후 다시 감소하는 현상."
---
## Definition

더블 디센트는 전통적인 편향-분산 트레이드오프(bias-variance tradeoff)에 도전하며, 훈련 데이터를 완전히 보간(interpolating)함에도 불구하고 매우 과매개변수화된(overparameterized) 모델이 낮은 테스트 오차를 달성할 수 있음을 보여줍니다. 초기에는 오차가 상승하지만, 모델 복잡도가 특정 임계점을 넘어서면 오차가 다시 감소하는 U자형 곡선과 그 이후의 추가적인 감소를 포함합니다.

### Summary

모델 복잡도가 보간 임계값(interpolation threshold)을 넘어 증가함에 따라 테스트 오차가 감소했다가 다시 증가하고, 이후 다시 감소하는 현상.

## Key Concepts

- 보간 임계값(Interpolation Threshold)
- 과매개변수화(Overparameterization)
- 편향-분산 트레이드오프(Bias-Variance Tradeoff)
- 테스트 오차(Test Error)

## Use Cases

- 신경망 확장 법칙(Scaling Laws) 분석
- 딥러닝 일반화 이해
- 대규모 AI 시스템에서의 모델 선택

## Related Terms

- [과적합(Overfitting) - 모델이 훈련 데이터에 지나치게 맞춰져 새로운 데이터에 대한 성능이 떨어지는 현상](/en/terms/과적합-overfitting-모델이-훈련-데이터에-지나치게-맞춰져-새로운-데이터에-대한-성능이-떨어지는-현상/)
- [과소적합(Underfitting) - 모델이 훈련 데이터의 패턴을 충분히 학습하지 못하는 현상](/en/terms/과소적합-underfitting-모델이-훈련-데이터의-패턴을-충분히-학습하지-못하는-현상/)
- [뉴럴 탠젠트 커널(Neural Tangent Kernel) - 무한히 넓은 신경망을 분석하기 위한 커널 방법](/en/terms/뉴럴-탠젠트-커널-neural-tangent-kernel-무한히-넓은-신경망을-분석하기-위한-커널-방법/)
- [정규화(Regularization) - 과적합을 방지하기 위해 모델 복잡도에 제약을 가하는 기법](/en/terms/정규화-regularization-과적합을-방지하기-위해-모델-복잡도에-제약을-가하는-기법/)
