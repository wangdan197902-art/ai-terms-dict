---
title: Коэффициент фи
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T16:10:15.198505Z'
lastmod: '2026-07-18T16:38:07.191724Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Статистическая мера связи между двумя бинарными переменными.
---
## Definition

Коэффициент фи (φ) — это мера ассоциации для двух бинарных переменных, служащая коэффициентом корреляции Пирсона для дихотомических переменных. Он принимает значения от -1 до +1, где 0 указывает на отсутствие связи.

### Summary

Статистическая мера связи между двумя бинарными переменными.

## Key Concepts

- Бинарные переменные
- Корреляция
- Таблица сопряженности
- Сила ассоциации

## Use Cases

- Оценка производительности бинарного классификатора с учетом метрик, помимо точности
- Анализ взаимосвязей в данных опросов с ответами «да/нет»
- Отбор признаков в наборах данных с категориальными входными данными

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [V Крамера (Обобщение коэффициента фи для таблиц большего размера)](/en/terms/v-крамера-обобщение-коэффициента-фи-для-таблиц-большего-размера/)
- [Корреляция Пирсона (Мера линейной зависимости)](/en/terms/корреляция-пирсона-мера-линейной-зависимости/)
- [Матрица ошибок (Таблица результатов классификации)](/en/terms/матрица-ошибок-таблица-результатов-классификации/)
- [Взаимная информация (Мера статистической зависимости)](/en/terms/взаимная-информация-мера-статистической-зависимости/)
