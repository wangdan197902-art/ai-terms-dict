---
title: "로터리 티켓 가설(Lottery ticket hypothesis)"
term_id: "lottery_ticket_hypothesis"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "pruning", "theory"]
difficulty: 4
weight: 1
slug: "lottery_ticket_hypothesis"
aliases:
  - /ko/terms/lottery_ticket_hypothesis/
date: "2026-07-18T16:03:15.502047Z"
lastmod: "2026-07-18T16:38:06.871910Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "밀집 신경망에는 초기화 상태에서 독립적으로 훈련될 때 원래 네트워크의 정확도와 맞먹을 수 있는 더 작은 부분 신경망이 포함되어 있다는 이론."
---

## Definition

로터리 티켓 가설은 대규모로 무작위 초기화된 신경망 내에 학습에 잘 적합된 희소 부분 신경망('당첨 티켓')이 존재한다고 제안합니다. 가지치기를 통해

### Summary

밀집 신경망에는 초기화 상태에서 독립적으로 훈련될 때 원래 네트워크의 정확도와 맞먹을 수 있는 더 작은 부분 신경망이 포함되어 있다는 이론.

## Key Concepts

- 가중치 가지치기(Weight pruning)
- 희소 네트워크(Sparse networks)
- 모델 압축(Model compression)
- 초기화 민감도(Initialization sensitivity)

## Use Cases

- 엣지 장치에 경량 모델 배포
- 학습 중 계산 비용 절감
- 추론 속도 가속화

## Related Terms

- [Network Pruning (네트워크 가지치기)](/en/terms/network-pruning-네트워크-가지치기/)
- [Model Distillation (모델 증류)](/en/terms/model-distillation-모델-증류/)
- [Sparse Training (희소 학습)](/en/terms/sparse-training-희소-학습/)
- [Efficient AI (효율적 AI)](/en/terms/efficient-ai-효율적-ai/)
