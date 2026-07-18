---
title: "시간적 편향"
term_id: "temporal_bias"
category: "ethics_safety"
subcategory: ""
tags: ["ethics", "bias", "time-series"]
difficulty: 4
weight: 1
slug: "temporal_bias"
aliases:
  - /ko/terms/temporal_bias/
date: "2026-07-18T16:17:51.303204Z"
lastmod: "2026-07-18T16:38:06.913487Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델이 과거의 맥락보다 최근 데이터를 우선시하여 예측이 치우치게 만드는 체계적인 오류입니다."
---

## Definition

시간적 편향은 기계 학습 모델이 오래된 관측치보다 최근의 관측치에 불균형하게 높은 가중치를 둘 때 발생합니다. 이는 주로 비정상성(non-stationary) 데이터 분포나 특정 훈련 프로토콜로 인해 나타납니다. 이로 인해 모델은 과거의 패턴을 제대로 반영하지 못하고 최근의 일시적인 변동에 과적합될 위험이 있으며, 장기적인 예측 성능 저하로 이어질 수 있습니다.

### Summary

모델이 과거의 맥락보다 최근 데이터를 우선시하여 예측이 치우치게 만드는 체계적인 오류입니다.

## Key Concepts

- 데이터 드리프트
- 비정상성
- 근접 효과
- 모델 성능 저하

## Use Cases

- 금융 시장 예측
- 소셜 미디어 트렌드 분석
- 탈퇴율 모델링

## Related Terms

- [Concept drift (개념 드리프트)](/en/terms/concept-drift-개념-드리프트/)
- [Catastrophic forgetting (파국적 망각)](/en/terms/catastrophic-forgetting-파국적-망각/)
- [Time-series analysis (시계열 분석)](/en/terms/time-series-analysis-시계열-분석/)
- [Fairness in AI (AI 공정성)](/en/terms/fairness-in-ai-ai-공정성/)
