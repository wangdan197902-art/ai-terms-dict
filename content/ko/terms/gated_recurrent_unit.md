---
title: "게이트드 리커런트 유닛"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
aliases:
  - /ko/terms/gated_recurrent_unit/
date: "2026-07-18T15:56:39.948112Z"
lastmod: "2026-07-18T16:38:06.843996Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "정보 흐름을 제어하기 위해 게이트 메커니즘을 사용하는 순환 신경망(RNN) 아키텍처의 일종으로, LSTM의 단순화된 대안입니다."
---

## Definition

게이트드 리커런트 유닛(GRU)은 시계열 데이터의 장기적 의존성을 포착하도록 설계된 특수한 순환 신경망(RNN) 셀입니다. 이는 롱 숏텀 메모리(LSTM) 아키텍처를 단순화하여 계산 효율성을 높이고 학습 속도를 개선합니다.

### Summary

정보 흐름을 제어하기 위해 게이트 메커니즘을 사용하는 순환 신경망(RNN) 아키텍처의 일종으로, LSTM의 단순화된 대안입니다.

## Key Concepts

- 순환 신경망
- 업데이트 게이트
- 리셋 게이트
- 시퀀스 모델링

## Use Cases

- 자연어 처리
- 시계열 예측
- 음성 인식

## Code Example

```python
import torch.nn as nn

# Define a simple GRU layer
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1)

# Example input: (seq_len, batch, input_size)
input_data = torch.randn(5, 3, 10)
hidden_state = None

output, hidden = gru(input_data, hidden_state)
```

## Related Terms

- [LSTM](/en/terms/lstm/)
- [RNN](/en/terms/rnn/)
- [딥러닝 (Deep Learning)](/en/terms/딥러닝-deep-learning/)
- [시퀀스 투 시퀀스 (Sequence-to-Sequence)](/en/terms/시퀀스-투-시퀀스-sequence-to-sequence/)
