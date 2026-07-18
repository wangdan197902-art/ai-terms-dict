---
title: "Mærkede data"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /da/terms/labeled_data/
date: "2026-07-18T16:04:07.969978Z"
lastmod: "2026-07-18T17:15:09.303654Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "Data, hvor den korrekte output- eller målvalue er angivet sammen med inputfunktionerne."
---

## Definition

Mærkede data består af inputprøver parret med tilsvarende sandhedsværdier (ground truth), hvilket danner grundlaget for overvåget maskinlæring. Det giver algoritmerne mulighed for at lære mappningen mellem input og output.

### Summary

Data, hvor den korrekte output- eller målvalue er angivet sammen med inputfunktionerne.

## Key Concepts

- Overvåget læring
- Sandhedsværdi (Ground Truth)
- Annotation
- Målvariabel

## Use Cases

- Træning af billedklassifikatorer
- Udvikling af talegenkendelsessystemer
- Prediktiv modellering inden for finanssektoren

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (umærkede data)](/en/terms/unlabeled_data-umærkede-data/)
- [supervised_learning (overvåget læring)](/en/terms/supervised_learning-overvåget-læring/)
- [data_annotation (dataannotation)](/en/terms/data_annotation-dataannotation/)
- [training_set (træningsdataset)](/en/terms/training_set-træningsdataset/)
