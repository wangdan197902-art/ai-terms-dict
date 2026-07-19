---
title: 위스퍼
term_id: whisper
category: basic_concepts
subcategory: ''
tags:
- Speech Recognition
- openai
- Practical AI
difficulty: 2
weight: 1
slug: whisper
date: '2026-07-18T16:20:35.008879Z'
lastmod: '2026-07-18T16:38:06.920394Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 다양한 오디오 데이터셋으로 학습된 오픈AI(OpenAI)의 자동 음성 인식(ASR) 시스템입니다.
---
## Definition

위스퍼는 다양한 언어, 방언, 억양을 처리하도록 설계된 범용 음성 인식 모델입니다. 수백만 시간 분량의 다국어 및 다중 작업 Supervised 데이터를 학습하여, 노이즈가 많은 환경에서도 강건하게 작동하며 여러 언어로 음성을 텍스트로 변환할 수 있습니다.

### Summary

다양한 오디오 데이터셋으로 학습된 오픈AI(OpenAI)의 자동 음성 인식(ASR) 시스템입니다.

## Key Concepts

- 자동 음성 인식
- 다국어 지원
- 노이즈 내성
- 트랜스포머 아키텍처

## Use Cases

- 비디오 자막 생성
- 회의 또는 강의 녹음 텍스트 변환
- 음성 명령 처리

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Speech-to-text (음성-텍스트 변환)](/en/terms/speech-to-text-음성-텍스트-변환/)
- [Natural Language Processing (자연어 처리)](/en/terms/natural-language-processing-자연어-처리/)
- [OpenAI (오픈AI)](/en/terms/openai-오픈ai/)
- [Audio classification (오디오 분류)](/en/terms/audio-classification-오디오-분류/)
