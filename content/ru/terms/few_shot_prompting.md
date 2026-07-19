---
title: Few-shot промптинг
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T15:34:00.526390Z'
lastmod: '2026-07-18T16:38:07.105747Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Few-shot промптинг — это техника, при которой большим языковым моделям
  предоставляется небольшое количество примеров ввода и вывода непосредственно в запросе
  для направления их поведения.
---
## Definition

Этот метод использует возможности контекстного обучения больших языковых моделей, предоставляя несколько иллюстративных примеров прямо в промпте. В отличие от дообучения (fine-tuning), которое требует обновления весов модели, few-shot промптинг позволяет адаптировать поведение модели «на лету» без дополнительных затрат на тренировку, просто демонстрируя желаемый формат ответа или логику рассуждений.

### Summary

Few-shot промптинг — это техника, при которой большим языковым моделям предоставляется небольшое количество примеров ввода и вывода непосредственно в запросе для направления их поведения.

## Key Concepts

- Контекстное обучение
- Инженерия промптов
- Руководство на основе примеров
- Сравнение с zero-shot

## Use Cases

- Форматирование анализа тональности
- Адаптация стиля кода
- Извлечение структурированных данных

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (обучение без примеров)](/en/terms/zero_shot-обучение-без-примеров/)
- [prompt_engineering (инженерия промптов)](/en/terms/prompt_engineering-инженерия-промптов/)
- [in_context_learning (контекстное обучение)](/en/terms/in_context_learning-контекстное-обучение/)
- [llm (большие языковые модели)](/en/terms/llm-большие-языковые-модели/)
