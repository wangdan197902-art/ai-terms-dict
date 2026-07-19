---
title: 클래스 활성화 매핑
term_id: class_activation_mapping
category: training_techniques
subcategory: ''
tags:
- visualization
- interpretability
- Computer Vision
difficulty: 4
weight: 1
slug: class_activation_mapping
date: '2026-07-18T15:45:14.520213Z'
lastmod: '2026-07-18T16:38:06.816871Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 클래스 활성화 매핑(CAM)은 입력 이미지에서 특정 예측 클래스에 가장 크게 기여하는 영역을 강조 표시하는 시각화 기법입니다.
---
## Definition

CAM은 입력 이미지 위에 오버레이되는 히트맵을 생성하여, 모델이 특정 클래스 레이블을 결정하는 데 가장 많이 기여한 픽셀을 보여줍니다. 이는 최종 컨볼루션 레이어의 특징 맵에 전역 평균 풀링(Global Average Pooling)을 적용하여 작동합니다.

### Summary

클래스 활성화 매핑(CAM)은 입력 이미지에서 특정 예측 클래스에 가장 크게 기여하는 영역을 강조 표시하는 시각화 기법입니다.

## Key Concepts

- 히트맵 시각화
- 해석 가능성
- 특징 중요도
- 전역 평균 풀링

## Use Cases

- 의료 영상 진단 검증
- 자율 주행 객체 감지 디버깅
- 설명 가능한 AI 보고

## Related Terms

- [Grad-CAM (그라디언트 기반 클래스 활성화 매핑)](/en/terms/grad-cam-그라디언트-기반-클래스-활성화-매핑/)
- [Saliency Maps (영향력 지도)](/en/terms/saliency-maps-영향력-지도/)
- [Explainable AI (설명 가능한 인공지능)](/en/terms/explainable-ai-설명-가능한-인공지능/)
- [Convolutional Neural Networks (합성곱 신경망)](/en/terms/convolutional-neural-networks-합성곱-신경망/)
