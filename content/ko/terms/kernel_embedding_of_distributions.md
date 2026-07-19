---
title: 분포의 커널 임베딩
term_id: kernel_embedding_of_distributions
category: training_techniques
subcategory: ''
tags:
- Advanced Statistics
- Kernel Methods
- theory
difficulty: 5
weight: 1
slug: kernel_embedding_of_distributions
date: '2026-07-18T16:00:54.436737Z'
lastmod: '2026-07-18T16:38:06.857194Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 확률 분포를 재현 가능 커널 힐베르트 공간(RKHS)으로 매핑하여 벡터 연산을 통해 분포 간 비교 및 조작을 가능하게 하는
  기법입니다.
---
## Definition

분포의 커널 임베딩(KED)은 확률적 객체(분포)를 재현 가능 커널 힐베르트 공간(RKHS)이라는 고차원 특징 공간 내의 점(point)으로 취급할 수 있게 합니다. 분포를 RKHS 내의 평균 임베딩(mean embedding)으로 매핑함으로써, 복잡한 확률적 연산을 선형 대수 연산(벡터 덧셈, 내적 등)으로 단순화할 수 있습니다. 이를 통해 두 분포 간의 거리나 유사도를 계산하거나, 분포 변환을 수행할 수 있습니다.

### Summary

확률 분포를 재현 가능 커널 힐베르트 공간(RKHS)으로 매핑하여 벡터 연산을 통해 분포 간 비교 및 조작을 가능하게 하는 기법입니다.

## Key Concepts

- 재현 가능 커널 힐베르트 공간(RKHS)
- 평균 임베딩(Mean Embedding)
- 비모수 추론
- 분포 비교

## Use Cases

- 두 표본 가설 검정(Two-sample hypothesis testing)
- 관측 데이터로부터 인과 관계 발견(Causal discovery)
- 생성 모델 출력 결과 비교

## Related Terms

- [최대 평균 불일치(Maximum Mean Discrepancy)](/en/terms/최대-평균-불일치-maximum-mean-discrepancy/)
- [힐베르트 공간 (Hilbert Space)](/en/terms/힐베르트-공간-hilbert-space/)
- [가우시안 프로세스 (Gaussian Process)](/en/terms/가우시안-프로세스-gaussian-process/)
- [통계적 검정 (Statistical Testing)](/en/terms/통계적-검정-statistical-testing/)
