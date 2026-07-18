---
title: "Označená data"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /cs/terms/labeled_data/
date: "2026-07-18T16:05:22.044987Z"
lastmod: "2026-07-18T17:15:09.146418Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Data, kde jsou správné výstupy nebo cílové hodnoty poskytovány spolu s vstupními znaky."
---

## Definition

Označená data se skládají ze vstupních vzorků spárovaných s příslušnými štítky základní pravdy (ground truth) a tvoří základ pro učení se s učitelem. Umožňují algoritmům naučit se mapování mezi vstupy a výstupy.

### Summary

Data, kde jsou správné výstupy nebo cílové hodnoty poskytovány spolu s vstupními znaky.

## Key Concepts

- Učení se s učitelem
- Základní pravda
- Anotace
- Cílová proměnná

## Use Cases

- Trénování klasifikátorů obrázků
- Vývoj systémů rozpoznávání řeči
- Prediktivní modelování ve financích

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (neoznačená data)](/en/terms/unlabeled_data-neoznačená-data/)
- [supervised_learning (učení se s učitelem)](/en/terms/supervised_learning-učení-se-s-učitelem/)
- [data_annotation (anotace dat)](/en/terms/data_annotation-anotace-dat/)
- [training_set (trénovací sada)](/en/terms/training_set-trénovací-sada/)
