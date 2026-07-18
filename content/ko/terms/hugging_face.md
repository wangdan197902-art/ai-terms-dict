---
title: "허깅페이스 (Hugging Face)"
term_id: "hugging_face"
category: "basic_concepts"
subcategory: ""
tags: ["platform", "open-source", "community"]
difficulty: 2
weight: 1
slug: "hugging_face"
aliases:
  - /ko/terms/hugging_face/
date: "2026-07-18T15:58:47.710681Z"
lastmod: "2026-07-18T16:38:06.850573Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "머신러닝 개발을 위한 오픈소스 도구, 모델 및 데이터를 제공하는 선도적인 플랫폼 및 커뮤니티입니다."
---

## Definition

허깅페이스는 오픈소스 AI 생태계의 중심이 된 주요 기업이자 온라인 플랫폼입니다. 방대한 사전 학습된 모델, 데이터셋, 데모 애플리케이션 저장소를 제공합니다(applications...)

### Summary

머신러닝 개발을 위한 오픈소스 도구, 모델 및 데이터를 제공하는 선도적인 플랫폼 및 커뮤니티입니다.

## Key Concepts

- 오픈소스
- 모델 허브
- Transformers 라이브러리
- 커뮤니티 협업

## Use Cases

- 텍스트 분류를 위한 사전 학습된 NLP 모델 접근
- 커뮤니티와 맞춤형 머신러닝 모델 공유
- Gradio 또는 Streamlit 통합을 사용한 데모 애플리케이션 구축

## Code Example

```python
from transformers import pipeline

# Load a pre-trained sentiment analysis model from Hugging Face
classifier = pipeline('sentiment-analysis')
result = classifier('I love using Hugging Face!')
print(result)
```

## Related Terms

- [Transformers](/en/terms/transformers/)
- [모델 저장소 (Model Repository)](/en/terms/모델-저장소-model-repository/)
- [오픈소스 AI (Open Source AI)](/en/terms/오픈소스-ai-open-source-ai/)
- [데이터셋 허브 (Dataset Hub)](/en/terms/데이터셋-허브-dataset-hub/)
