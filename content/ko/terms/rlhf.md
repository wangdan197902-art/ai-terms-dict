---
title: "인간 피드백 기반 강화 학습"
term_id: "rlhf"
category: "training_techniques"
subcategory: ""
tags: ["alignment", "fine_tuning"]
difficulty: 5
weight: 1
slug: "rlhf"
aliases:
  - /ko/terms/rlhf/
date: "2026-07-18T15:28:25.409708Z"
lastmod: "2026-07-18T16:38:06.782554Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "RLHF는 인간 피드백을 사용하여 보상 모델을 학습시킴으로써 AI 모델의 출력을 인간의 선호도와 정렬시키는 기술입니다."
---

## Definition

인간 피드백 기반 강화 학습(Reinforcement Learning from Human Feedback, RLHF)은 대규모 언어 모델(LLM)의 미세 조정을 통해 그 출력이 인간의 가치와 기대에 더 잘 부합하도록 만드는 방법론입니다. 일반적으로 이 과정은 세 가지 주요 단계로 구성됩니다: 먼저 지도 미세 조정(SFT)으로 기본 모델을 훈련하고, 인간이 제공한 선호도 데이터를 바탕으로 보상 모델을 학습시킨 후, 마지막으로 강화 학습 기법을 사용하여 원본 모델을 최적화합니다.

### Summary

RLHF는 인간 피드백을 사용하여 보상 모델을 학습시킴으로써 AI 모델의 출력을 인간의 선호도와 정렬시키는 기술입니다.

## Key Concepts

- 선호도 데이터(Preference Data)
- 보상 모델(Reward Model)
- 정렬(Alignment)
- 근접 정책 최적화(PPO (Proximal Policy Optimization))

## Use Cases

- 챗봇 성능 개선(Chatbot refinement)
- 콘텐츠 검열(Content moderation)
- 지시 따르기 능력 향상(Improving instruction following)

## Related Terms

- [지도 미세 조정(Supervised Fine-Tuning, 초기 모델 학습 단계)](/en/terms/지도-미세-조정-supervised-fine-tuning-초기-모델-학습-단계/)
- [선호도 최적화(Preference Optimization, 직접 선호도를 최적화하는 접근법)](/en/terms/선호도-최적화-preference-optimization-직접-선호도를-최적화하는-접근법/)
- [DPO(Direct Preference Optimization, 보상 모델 없이 직접 선호도를 최적화하는 알고리즘)](/en/terms/dpo-direct-preference-optimization-보상-모델-없이-직접-선호도를-최적화하는-알고리즘/)
