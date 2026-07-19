---
title: 二段階（ツーステージ）
term_id: two_stage
category: basic_concepts
subcategory: ''
tags:
- architecture
- Computer Vision
difficulty: 3
weight: 1
slug: two_stage
date: '2026-07-18T10:57:56.792601Z'
lastmod: '2026-07-18T11:44:45.029551Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 処理が明確に区別された連続したフェーズで行われるパイプラインアーキテクチャ。
---
## Definition

二段階アーキテクチャは、複雑なタスクを2つの分離されたステップに分割します。通常、検出に続き分類や精製が行われます。コンピュータビジョンでは、Faster R-CNNなどのオブジェクトデテクタ

### Summary

処理が明確に区別された連続したフェーズで行われるパイプラインアーキテクチャ。

## Key Concepts

- 逐次処理
- リージョン提案
- モジュール性
- パイプライン

## Use Cases

- 物体検出（例：Faster R-CNN）
- 顔認識パイプライン
- LLMにおける多段階推論

## Related Terms

- [single_stage (シングルステージ)](/en/terms/single_stage-シングルステージ/)
- [object_detection (物体検出)](/en/terms/object_detection-物体検出/)
- [pipeline (パイプライン)](/en/terms/pipeline-パイプライン/)
