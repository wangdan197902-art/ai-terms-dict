---
title: "Merket data"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /no/terms/labeled_data/
date: "2026-07-18T16:02:08.005827Z"
lastmod: "2026-07-18T16:38:07.017381Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Data der det korrekte utdata eller målverdien er oppgitt sammen med inngangsfunksjonene."
---

## Definition

Merket data består av inngangseksempler parret med tilsvarende sanntidsmerkelapper, og fungerer som grunnlaget for overvåket maskinlæring. Det lar algoritmer lære kartleggingen mellom inngang

### Summary

Data der det korrekte utdata eller målverdien er oppgitt sammen med inngangsfunksjonene.

## Key Concepts

- Overvåket læring
- Sanntid
- Annotering
- Målvariabel

## Use Cases

- Trening av bildeklassifiserere
- Bygging av talegjenkjennelsessystemer
- Prediktiv modellering i finans

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (umerket data)](/en/terms/unlabeled_data-umerket-data/)
- [supervised_learning (overvåket læring)](/en/terms/supervised_learning-overvåket-læring/)
- [data_annotation (dataannotering)](/en/terms/data_annotation-dataannotering/)
- [training_set (treningsdatasett)](/en/terms/training_set-treningsdatasett/)
