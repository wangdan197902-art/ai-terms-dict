---
title: "Beschriftete Daten"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /de/terms/labeled_data/
date: "2026-07-18T11:21:06.047121Z"
lastmod: "2026-07-18T11:44:44.956968Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Daten, bei denen der korrekte Ausgabe- oder Zielwert zusammen mit den Eingabemerkmalswerten bereitgestellt wird."
---

## Definition

Beschriftete Daten bestehen aus Eingabeproben, die mit entsprechenden Ground-Truth-Labels (Grundwahrheiten) gepaart sind und dienen als Grundlage für das überwachtes maschinelles Lernen. Sie ermöglichen es Algorithmen, die Abbildung zwischen Eingabe und Ausgabe zu lernen.

### Summary

Daten, bei denen der korrekte Ausgabe- oder Zielwert zusammen mit den Eingabemerkmalswerten bereitgestellt wird.

## Key Concepts

- Überwachtes Lernen
- Ground Truth (Grundwahrheit)
- Annotation (Beschriftung)
- Zielvariable

## Use Cases

- Schulung von Bildklassifikatoren
- Entwicklung von Spracherkennungssystemen
- Prädiktive Modellierung im Finanzwesen

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (Unbeschriftete Daten)](/en/terms/unlabeled_data-unbeschriftete-daten/)
- [supervised_learning (Überwachtes Lernen)](/en/terms/supervised_learning-überwachtes-lernen/)
- [data_annotation (Datenannotation)](/en/terms/data_annotation-datenannotation/)
- [training_set (Trainingsdatensatz)](/en/terms/training_set-trainingsdatensatz/)
