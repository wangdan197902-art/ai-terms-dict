---
title: "two-stage"
term_id: "two_stage"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "computer_vision"]
difficulty: 3
weight: 1
slug: "two_stage"
aliases:
  - /en/terms/two_stage/
date: "2026-07-18T09:39:43.446873Z"
lastmod: "2026-07-18T11:44:44.619503Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A pipeline architecture where processing occurs in distinct, sequential phases."
---

## Definition

Two-stage architectures divide a complex task into two separate steps, typically involving detection followed by classification or refinement. In computer vision, examples include object detectors like Faster R-CNN, which first generate region proposals and then classify them. This separation allows for higher accuracy and modularity compared to single-stage methods, though it may incur higher computational overhead due to the sequential nature of the process.

### Summary

A pipeline architecture where processing occurs in distinct, sequential phases.

## Key Concepts

- Sequential processing
- Region proposal
- Modularity
- Pipeline

## Use Cases

- Object detection (e.g., Faster R-CNN)
- Face recognition pipelines
- Multi-step reasoning in LLMs

## Related Terms

- [single_stage](/en/terms/single_stage/)
- [object_detection](/en/terms/object_detection/)
- [pipeline](/en/terms/pipeline/)
