---
title: "Online"
term_id: "online"
category: "basic_concepts"
subcategory: ""
tags: ["ML Paradigms", "Streaming", "Adaptive Systems"]
difficulty: 3
weight: 1
slug: "online"
date: "2026-07-18T09:35:02.712187Z"
lastmod: "2026-07-18T11:44:44.604037Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Refers to machine learning models that learn continuously from new data streams in real-time without retraining from scratch."
---
## Definition

Online learning is a machine learning paradigm where the model is updated incrementally as new data points arrive, rather than being trained on a static batch of data all at once. This approach is crucial for applications dealing with streaming data, such as stock market predictions or real-time fraud detection. It allows systems to adapt quickly to changing patterns and distributions over time, ensuring that the model remains relevant and accurate in dynamic environments without requiring significant computational resources for full retraining.

### Summary

Refers to machine learning models that learn continuously from new data streams in real-time without retraining from scratch.

## Key Concepts

- Incremental Learning
- Streaming Data
- Real-time Adaptation
- Batch vs. Online

## Use Cases

- Real-time fraud detection
- Stock price prediction
- Personalized recommendation systems

## Code Example

```python
from sklearn.linear_model import SGDClassifier
model = SGDClassifier()
# Simulate online learning with partial_fit
model.partial_fit(X_batch, y_batch, classes=[0, 1])
```

## Related Terms

- [streaming_data](/en/terms/streaming_data/)
- [incremental_learning](/en/terms/incremental_learning/)
- [real_time_processing](/en/terms/real_time_processing/)
- [batch_learning](/en/terms/batch_learning/)
