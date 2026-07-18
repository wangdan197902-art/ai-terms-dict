---
title: "구조적 위험 최소화"
term_id: "structural_risk_minimization"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "theory", "regularization"]
difficulty: 3
weight: 1
slug: "structural_risk_minimization"
aliases:
  - /ko/terms/structural_risk_minimization/
date: "2026-07-18T16:17:21.908099Z"
lastmod: "2026-07-18T16:38:06.911807Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델 적합도와 복잡도를 균형 있게 조정하여 일반화 오류의 상한을 최소화하려는 통계 학습의 원리."
---

## Definition

구조적 위험 최소화(SRM)는 과적합을 방지하기 위해 모델의 복잡도를 제어함으로써 기대 위험을 최소화하는 방법론입니다. 이는 경험적 위험 최소화(ERM)에 정규화 항이나 모델 복잡도 페널티를 추가하여 확장된 것으로, 단순함과 정확성 사이의 균형을 찾아 일반화 성능을 높이는 데 목적이 있습니다.

### Summary

모델 적합도와 복잡도를 균형 있게 조정하여 일반화 오류의 상한을 최소화하려는 통계 학습의 원리.

## Key Concepts

- VC 차원 (VC dimension)
- 정규화 (Regularization)
- 일반화 오류 (Generalization error)
- 모델 복잡도 페널티

## Use Cases

- 서포트 벡터 머신(SVM) 훈련
- 회귀 분석에서 다항식 차수 선택
- 과적합 방지를 위한 의사결정나무 가지치기

## Related Terms

- [경험적 위험 최소화 (Empirical risk minimization): 훈련 데이터 오류 최소화의 기본 원리](/en/terms/경험적-위험-최소화-empirical-risk-minimization-훈련-데이터-오류-최소화의-기본-원리/)
- [오컴의 면도날 (Occam's razor): 가장 간단한 설명이 선호된다는 철학적 원리](/en/terms/오컴의-면도날-occam-s-razor-가장-간단한-설명이-선호된다는-철학적-원리/)
- [정규화 (Regularization): 모델 복잡도를 제한하는 기법](/en/terms/정규화-regularization-모델-복잡도를-제한하는-기법/)
- [편향-분산 트레이드오프 (Bias-variance tradeoff): 모델의 오차를 줄이기 위한 균형 잡기](/en/terms/편향-분산-트레이드오프-bias-variance-tradeoff-모델의-오차를-줄이기-위한-균형-잡기/)
