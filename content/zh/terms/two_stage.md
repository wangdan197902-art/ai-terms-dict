---
title: 两阶段的
term_id: two_stage
category: basic_concepts
subcategory: ''
tags:
- architecture
- Computer Vision
difficulty: 3
weight: 1
slug: two_stage
date: '2026-07-18T10:59:01.893980Z'
lastmod: '2026-07-18T11:44:45.395979Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种流水线架构，其中处理过程分为 distinct 且顺序进行的阶段。
---
## Definition

两阶段架构将复杂任务划分为两个独立的步骤，通常涉及检测后跟分类或细化。在计算机视觉中，典型的例子包括像 Faster R-CNN 这样的对象检测器，先生成区域建议，再进行分类。

### Summary

一种流水线架构，其中处理过程分为 distinct 且顺序进行的阶段。

## Key Concepts

- 顺序处理
- 区域提议
- 模块化
- 流水线

## Use Cases

- 对象检测（例如 Faster R-CNN）
- 人脸识别流水线
- 大语言模型中的多步推理

## Related Terms

- [single_stage (单阶段)](/en/terms/single_stage-单阶段/)
- [object_detection (对象检测)](/en/terms/object_detection-对象检测/)
- [pipeline (流水线)](/en/terms/pipeline-流水线/)
