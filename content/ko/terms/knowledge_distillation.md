---
title: "지식 증류"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T16:01:07.728865Z"
lastmod: "2026-07-18T16:38:06.857559Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "지식 증류는 작은 학생 모델이 더 큰 교사 모델의 행동을 모방하도록 학습시켜 모델을 압축하는 기술입니다."
---
## Definition

지식 증류는 대규모 복잡한 신경망(교사)을 더 작고 효율적인 네트워크(학생)로 압축하기 위해 사용되는 머신러닝 방법론입니다. 학생 모델은 교사 모델의 출력 분포(소프트 타겟)를 따라가며 학습하여, 원본 모델의 성능을 유지하면서 추론 속도와 효율성을 높입니다.

### Summary

지식 증류는 작은 학생 모델이 더 큰 교사 모델의 행동을 모방하도록 학습시켜 모델을 압축하는 기술입니다.

## Key Concepts

- 교사-학생 모델
- 모델 압축
- 소프트 타겟
- 효율성

## Use Cases

- 엣지 디바이스용 모델 배포
- 추론 지연 시간 단축
- 클라우드 컴퓨팅 비용 절감

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression (모델 압축)](/en/terms/model-compression-모델-압축/)
- [Pruning (가지치기)](/en/terms/pruning-가지치기/)
- [Quantization (양자화)](/en/terms/quantization-양자화/)
- [Neural Networks (신경망)](/en/terms/neural-networks-신경망/)
