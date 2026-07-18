---
title: "흐름 기반 생성 모델(Flow-based generative model)"
term_id: "flow_based_generative_model"
category: "basic_concepts"
subcategory: ""
tags: ["generative", "probability", "invertible"]
difficulty: 4
weight: 1
slug: "flow_based_generative_model"
aliases:
  - /ko/terms/flow_based_generative_model/
date: "2026-07-18T15:56:02.182961Z"
lastmod: "2026-07-18T16:38:06.841173Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "단순한 분포를 복잡한 데이터 분포로 매핑하기 위해 가역 변환을 사용하는 생성 모델의 한 종류입니다."
---

## Definition

흐름 기반 생성 모델은 가우시안과 같은 간단한 기본 분포에 일련의 가역적이고 미분 가능한 변환을 적용하여 복잡한 확률 분포를 구성합니다. 이러한 모델은 정확한 우도(exact likelihood) 계산을 가능하게 하며, 데이터 생성 및 밀도 추정에 효과적입니다.

### Summary

단순한 분포를 복잡한 데이터 분포로 매핑하기 위해 가역 변환을 사용하는 생성 모델의 한 종류입니다.

## Key Concepts

- 가역 변환(Invertible Transformations)
- 정확한 우도(Exact Likelihood)
- 정규화 흐름(Normalizing Flows)
- 변수 변경(Change of Variables)

## Use Cases

- 이미지 생성(Image generation)
- 밀도 추정(Density estimation)
- 이상 탐지(Anomaly detection)

## Related Terms

- [Normalizing Flow (정규화 흐름)](/en/terms/normalizing-flow-정규화-흐름/)
- [GAN (생성 적대 신경망)](/en/terms/gan-생성-적대-신경망/)
- [VAE (변분 오토인코더)](/en/terms/vae-변분-오토인코더/)
- [Coupling Layer (결합 레이어)](/en/terms/coupling-layer-결합-레이어/)
