---
title: "증류(Distillation)"
term_id: "distillation"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "compression", "model_efficiency"]
difficulty: 3
weight: 1
slug: "distillation"
aliases:
  - /ko/terms/distillation/
date: "2026-07-18T15:23:57.551284Z"
lastmod: "2026-07-18T16:38:06.771670Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "작은 학생 모델이 큰 교사 모델의 동작을 모방하도록 학습시키는 모델 압축 기술인 지식 증류(Knowledge Distillation)."
---

## Definition

이 과정은 복잡하고 고성능인 '교사(Teacher)' 신경망에서 더 단순하고 효율적인 '학생(Student)' 네트워크로 지식을 전달합니다. 학생 모델은 하드 라벨(Hard Labels)뿐만 아니라 교사 모델의 부드러운 타겟(Soft Targets)에서도 학습하여 성능을 유지하면서 모델을 경량화합니다.

### Summary

작은 학생 모델이 큰 교사 모델의 동작을 모방하도록 학습시키는 모델 압축 기술인 지식 증류(Knowledge Distillation).

## Key Concepts

- 교사-학생 아키텍처(Teacher-Student Architecture)
- 소프트 타겟(Soft Targets)
- 모델 압축(Model Compression)
- 추론 효율성(Inference Efficiency)

## Use Cases

- 모바일 기기용 대형 언어 모델 배포
- 실시간 컴퓨터 비전 애플리케이션의 지연 시간 단축
- 엣지 컴퓨팅 환경을 위한 딥러닝 모델 최적화

## Related Terms

- [Quantization (양자화)](/en/terms/quantization-양자화/)
- [Pruning (가지치기)](/en/terms/pruning-가지치기/)
- [Transfer Learning (전이 학습)](/en/terms/transfer-learning-전이-학습/)
- [Neural Architecture Search (신경망 구조 탐색)](/en/terms/neural-architecture-search-신경망-구조-탐색/)
