---
title: "투 스테이지(Two-stage)"
term_id: "two_stage"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "computer_vision"]
difficulty: 3
weight: 1
slug: "two_stage"
aliases:
  - /ko/terms/two_stage/
date: "2026-07-18T15:33:06.668023Z"
lastmod: "2026-07-18T16:38:06.792101Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "처리 과정이 명확히 구분된 순차적 단계로 이루어지는 파이프라인 아키텍처."
---

## Definition

투 스테이지 아키텍처는 복잡한 작업을 두 개의 별도 단계로 나누며, 일반적으로 탐지(Detection) 이후 분류(Classification) 또는 정제(Refinement) 과정을 포함합니다. 컴퓨터 비전 분야에서는 객체 탐지기와 같은 예시가 있으며, 대표적으로 Faster R-CNN 등이 있습니다.

### Summary

처리 과정이 명확히 구분된 순차적 단계로 이루어지는 파이프라인 아키텍처.

## Key Concepts

- 순차적 처리
- 영역 제안(Region Proposal)
- 모듈성
- 파이프라인

## Use Cases

- 객체 탐지 (예: Faster R-CNN)
- 얼굴 인식 파이프라인
- 대규모 언어 모델(LLM)의 다단계 추론

## Related Terms

- [single_stage (싱글 스테이지: 한 번의 단계로 결과를 도출하는 방식)](/en/terms/single_stage-싱글-스테이지-한-번의-단계로-결과를-도출하는-방식/)
- [object_detection (객체 탐지: 이미지 내 물체의 위치와 종류를 식별하는 작업)](/en/terms/object_detection-객체-탐지-이미지-내-물체의-위치와-종류를-식별하는-작업/)
- [pipeline (파이프라인: 여러 단계를 연결하여 데이터를 처리하는 구조)](/en/terms/pipeline-파이프라인-여러-단계를-연결하여-데이터를-처리하는-구조/)
