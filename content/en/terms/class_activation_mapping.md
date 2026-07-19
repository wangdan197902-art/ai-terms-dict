---
title: Class activation mapping
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
date: '2026-07-18T09:49:31.456578Z'
lastmod: '2026-07-18T11:44:44.651681Z'
draft: false
source: agnes_llm
status: published
language: en
description: Class activation mapping (CAM) is a visualization technique that highlights
  the regions in an input image most responsible for a specific predicted class.
---
## Definition

CAM generates heatmaps overlaid on input images to show which pixels contributed most to the model's decision for a particular class label. It works by applying global average pooling to the final convolutional feature maps, weighted by the importance of each map for the target class. This technique enhances model interpretability, allowing developers to debug biases, verify that models focus on relevant features rather than artifacts, and build trust in computer vision applications.

### Summary

Class activation mapping (CAM) is a visualization technique that highlights the regions in an input image most responsible for a specific predicted class.

## Key Concepts

- Heatmap Visualization
- Interpretability
- Feature Importance
- Global Average Pooling

## Use Cases

- Medical image diagnosis verification
- Autonomous object detection debugging
- Explainable AI reporting

## Related Terms

- [Grad-CAM](/en/terms/grad-cam/)
- [Saliency Maps](/en/terms/saliency-maps/)
- [Explainable AI](/en/terms/explainable-ai/)
- [Convolutional Neural Networks](/en/terms/convolutional-neural-networks/)
