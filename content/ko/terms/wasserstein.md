---
title: 바서스타인(거리 측정)
term_id: wasserstein
category: basic_concepts
subcategory: ''
tags:
- metrics
- GAN
- probability
difficulty: 4
weight: 1
slug: wasserstein
date: '2026-07-18T15:31:05.711729Z'
lastmod: '2026-07-18T16:38:06.787757Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 하나의 확률 분포를 다른 하나로 변환하는 데 필요한 최소 비용에 기반하여 확률 분포 간의 거리를 측정하는 지표입니다.
---
## Definition

바서스타인 거리(또는 지상 이동자 거리)는 한 분포에서 질량을 이동시키는 데 필요한 최소 '작업량'을 계산하여 두 확률 분포 간의 불일치성을 정량화합니다. 이는 특히 생성 모델의 훈련 안정성에 유용합니다.

### Summary

하나의 확률 분포를 다른 하나로 변환하는 데 필요한 최소 비용에 기반하여 확률 분포 간의 거리를 측정하는 지표입니다.

## Key Concepts

- 지상 이동자 거리
- 확률 분포
- 최적 운송
- 기울기 안정성

## Use Cases

- 안정적인 GAN 훈련
- 도메인 적응
- 분포 유사성 측정

## Related Terms

- [KL Divergence (KL 발산)](/en/terms/kl-divergence-kl-발산/)
- [Generative Adversarial Networks (생성 적대 신경망)](/en/terms/generative-adversarial-networks-생성-적대-신경망/)
- [Optimal Transport (최적 운송)](/en/terms/optimal-transport-최적-운송/)
- [Distribution Matching (분포 일치)](/en/terms/distribution-matching-분포-일치/)
