---
title: "Размеченные данные"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /ru/terms/labeled_data/
date: "2026-07-18T16:00:49.264790Z"
lastmod: "2026-07-18T16:38:07.173448Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Данные, в которых правильные выходные значения или целевые значения предоставлены вместе с входными признаками."
---

## Definition

Размеченные данные состоят из входных образцов, сопоставленных с соответствующими эталонными метками, и служат основой для обучения с учителем. Они позволяют алгоритмам изучать отображение между входными данными и целевыми значениями.

### Summary

Данные, в которых правильные выходные значения или целевые значения предоставлены вместе с входными признаками.

## Key Concepts

- Обучение с учителем
- Эталонная истина
- Аннотирование
- Целевая переменная

## Use Cases

- Обучение классификаторов изображений
- Создание систем распознавания речи
- Прогнозное моделирование в финансах

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (неразмеченные данные)](/en/terms/unlabeled_data-неразмеченные-данные/)
- [supervised_learning (обучение с учителем)](/en/terms/supervised_learning-обучение-с-учителем/)
- [data_annotation (аннотирование данных)](/en/terms/data_annotation-аннотирование-данных/)
- [training_set (обучающая выборка)](/en/terms/training_set-обучающая-выборка/)
