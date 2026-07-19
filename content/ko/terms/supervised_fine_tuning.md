---
title: 지도 미세 조정
term_id: supervised_fine_tuning
category: training_techniques
subcategory: ''
tags:
- training
- LLM
- Fine-Tuning
difficulty: 4
weight: 1
slug: supervised_fine_tuning
date: '2026-07-18T15:36:33.155955Z'
lastmod: '2026-07-18T16:38:06.800681Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 특정 작업이나 도메인에 맞게 적응시키기 위해 사전 훈련된 모델을 특정 데이터셋으로 추가로 훈련하는 과정입니다.
---
## Definition

지도 미세 조정(SFT)은 언어 모델과 같은 대규모 사전 훈련된 모델을 가져와 특정 하류 작업을 위해 레이블이 지정된 작고 고품질의 데이터셋으로 훈련을 계속하는 것을 의미합니다.

### Summary

특정 작업이나 도메인에 맞게 적응시키기 위해 사전 훈련된 모델을 특정 데이터셋으로 추가로 훈련하는 과정입니다.

## Key Concepts

- 사전 훈련된 모델
- 전이 학습
- 지시 튜닝
- 도메인 적응

## Use Cases

- 맞춤형 챗봇 개발
- 전문 의료 Q&A 시스템
- 코드 생성 어시스턴트

## Code Example

```python
model.train()
for batch in dataloader:
    inputs, labels = batch
    outputs = model(inputs, labels=labels)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
```

## Related Terms

- [Pre-training (사전 훈련)](/en/terms/pre-training-사전-훈련/)
- [Reinforcement Learning from Human Feedback (인간 피드백 기반 강화 학습)](/en/terms/reinforcement-learning-from-human-feedback-인간-피드백-기반-강화-학습/)
- [Prompt Engineering (프롬프트 엔지니어링)](/en/terms/prompt-engineering-프롬프트-엔지니어링/)
- [LLM (대규모 언어 모델)](/en/terms/llm-대규모-언어-모델/)
