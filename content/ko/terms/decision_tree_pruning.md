---
title: "의사결정나무 가지치기"
term_id: "decision_tree_pruning"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "trees"]
difficulty: 3
weight: 1
slug: "decision_tree_pruning"
aliases:
  - /ko/terms/decision_tree_pruning/
date: "2026-07-18T15:51:28.982838Z"
lastmod: "2026-07-18T16:38:06.829937Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "사본 분류에 거의 기여하지 않는 부분을 제거하여 의사결정나무의 크기를 줄이는 기법입니다."
---

## Definition

가지치기(Pruning)는 예측력이 약한 가지(branch)를 제거함으로써 의사결정나무 모델의 과적합을 방지하는 방법입니다. 이는 트리의 성장을 조기에 중단하는 사전 가지치기(pre-pruning)나, 완전히 성장시킨 후 불필요한 부분을 잘라내는 사후 가지치기(post-pruning) 방식으로 수행할 수 있습니다.

### Summary

사본 분류에 거의 기여하지 않는 부분을 제거하여 의사결정나무의 크기를 줄이는 기법입니다.

## Key Concepts

- 과적합 방지
- 사전 가지치기
- 사후 가지치기
- 모델 복잡도

## Use Cases

- 모델 일반화 성능 향상
- 추론 지연 시간 단축
- 규칙 추출 단순화

## Related Terms

- [정규화 (Regularization - 모델 복잡도를 제한하여 과적합을 방지하는 기법)](/en/terms/정규화-regularization-모델-복잡도를-제한하여-과적합을-방지하는-기법/)
- [교차 검증 (Cross-validation - 데이터 분할을 통해 모델 성능을 평가하는 방법)](/en/terms/교차-검증-cross-validation-데이터-분할을-통해-모델-성능을-평가하는-방법/)
- [엔트로피 (Entropy - 데이터의 불순도 또는 무질서도를 측정하는 지표)](/en/terms/엔트로피-entropy-데이터의-불순도-또는-무질서도를-측정하는-지표/)
- [정보 이득 (Information gain - 특성 분할 시 엔트로피가 감소하는 정도)](/en/terms/정보-이득-information-gain-특성-분할-시-엔트로피가-감소하는-정도/)
