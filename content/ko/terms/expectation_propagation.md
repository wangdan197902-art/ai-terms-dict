---
title: "기대 전파"
term_id: "expectation_propagation"
category: "basic_concepts"
subcategory: ""
tags: ["bayesian_methods", "inference", "probabilistic_models"]
difficulty: 5
weight: 1
slug: "expectation_propagation"
aliases:
  - /ko/terms/expectation_propagation/
date: "2026-07-18T15:55:04.752703Z"
lastmod: "2026-07-18T16:38:06.838500Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "복잡한 확률적 그래픽 모델에서 사후 분포를 추정하는 데 사용되는 근사 추론 알고리즘."
---

## Definition

기대 전파(EP)는 실제 사후 분포에 대한 가우시안 근사를 반복적으로 정교화하여 계산이 불가능한 적분을 근사합니다. 이는 근사된 분포와 실제 사후 분포 사이의 켤레-라이블러(Kullback-Leibler) 발산을 최소화하는 방식으로 작동합니다.

### Summary

복잡한 확률적 그래픽 모델에서 사후 분포를 추정하는 데 사용되는 근사 추론 알고리즘.

## Key Concepts

- 사후 근사
- 모멘트 일치
- 켤레-라이블러 발산
- 가우시안 프로세스

## Use Cases

- 희소 가우시안 프로세스
- 베이지안 로지스틱 회귀
- 확률적 행렬 인수분해

## Related Terms

- [variational_inference (변분 추론)](/en/terms/variational_inference-변분-추론/)
- [gaussian_processes (가우시안 프로세스)](/en/terms/gaussian_processes-가우시안-프로세스/)
- [bayesian_inference (베이지안 추론)](/en/terms/bayesian_inference-베이지안-추론/)
- [mean_field_approximation (평균장 근사)](/en/terms/mean_field_approximation-평균장-근사/)
