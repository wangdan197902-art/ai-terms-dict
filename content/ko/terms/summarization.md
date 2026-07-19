---
title: 요약(Summarization)
term_id: summarization
category: application_paradigms
subcategory: ''
tags:
- NLP
- Text Processing
- applications
difficulty: 3
weight: 1
slug: summarization
date: '2026-07-18T15:36:19.379650Z'
lastmod: '2026-07-18T16:38:06.800573Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 긴 텍스트의 핵심 정보를 보존하면서 간결하고 일관된 요약을 생성하는 자연어 처리(NLP) 작업입니다.
---
## Definition

텍스트 요약은 중요한 의미를 잃지 않고 대량의 텍스트를 짧은 버전으로 축소합니다. 추출 방식(Source에서 중요한 문장을 선택) 또는 생성 방식(Abstractive, 새로운 문장 생성)이 있습니다...

### Summary

긴 텍스트의 핵심 정보를 보존하면서 간결하고 일관된 요약을 생성하는 자연어 처리(NLP) 작업입니다.

## Key Concepts

- 추출형 요약(Extractive Summarization)
- 생성형 요약(Abstractive Summarization)
- 정보 밀도(Information Density)
- 일관성(Coherence)

## Use Cases

- 뉴스 기사 압축
- 회의록 생성
- 법률 문서 검토

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [NLP (자연어 처리)](/en/terms/nlp-자연어-처리/)
- [Transformer Models (트랜스포머 모델)](/en/terms/transformer-models-트랜스포머-모델/)
- [BERT (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [T5 (Text-to-Text Transfer Transformer)](/en/terms/t5-text-to-text-transfer-transformer/)
