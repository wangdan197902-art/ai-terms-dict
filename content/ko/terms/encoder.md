---
title: "인코더"
term_id: "encoder"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Network Architecture", "Feature Engineering", "Transformers"]
difficulty: 3
weight: 1
slug: "encoder"
date: "2026-07-18T15:34:19.126489Z"
lastmod: "2026-07-18T16:38:06.794705Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "인코더는 입력 데이터를 압축되고 의미 있는 표현으로 변환하는 신경망의 구성 요소입니다."
---
## Definition

인코더는 원시 입력 시퀀스나 데이터 구조를 처리하여 잠재 공간(latent space) 표현, 즉 종종 임베딩이나 코드로 불리는 형태로 변환합니다. 이들은 트랜스포머 및 오토인코더와 같은 아키텍처의 핵심 구성 요소입니다.

### Summary

인코더는 입력 데이터를 압축되고 의미 있는 표현으로 변환하는 신경망의 구성 요소입니다.

## Key Concepts

- 특징 추출
- 잠재 공간
- 시퀀스 처리
- 압축

## Use Cases

- 트랜스포머 모델에서 입력 텍스트 처리
- 노이즈 제거를 위한 오토인코더 내 이미지 압축
- 리뷰에서 감정 특징 추출

## Code Example

```python
import torch.nn as nn

class SimpleEncoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, hidden_dim)
    
    def forward(self, x):
        return torch.relu(self.fc(x))
```

## Related Terms

- [Decoder (디코더)](/en/terms/decoder-디코더/)
- [Transformer (트랜스포머)](/en/terms/transformer-트랜스포머/)
- [Autoencoder (오토인코더)](/en/terms/autoencoder-오토인코더/)
- [Latent Variable (잠재 변수)](/en/terms/latent-variable-잠재-변수/)
