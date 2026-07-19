---
title: WordPiece
term_id: wordpiece
category: engineering_practice
subcategory: ''
tags:
- NLP
- tokenization
- BERT
difficulty: 3
weight: 1
slug: wordpiece
date: '2026-07-18T16:20:38.705932Z'
lastmod: '2026-07-18T16:38:07.214325Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Алгоритм токенизации подслов, который рекурсивно объединяет наиболее
  часто встречающиеся пары символов для обработки слов, отсутствующих в словаре.
---
## Definition

WordPiece — метод токенизации, широко используемый в моделях обработки естественного языка, таких как BERT и ALBERT. Он разбивает слова на более мелкие подсловные единицы для управления морфологическим богатством и сокращения...

### Summary

Алгоритм токенизации подслов, который рекурсивно объединяет наиболее часто встречающиеся пары символов для обработки слов, отсутствующих в словаре.

## Key Concepts

- Токенизация подслов
- Расширение словаря
- Обработка слов вне словаря
- Морфологический анализ

## Use Cases

- Предварительная обработка текста для моделей BERT
- Работа с языками с низким уровнем ресурсности
- Уменьшение размера матрицы эмбеддингов

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (Кодирование пар байт)](/en/terms/byte-pair-encoding-кодирование-пар-байт/)
- [SentencePiece (Инструмент SentencePiece)](/en/terms/sentencepiece-инструмент-sentencepiece/)
- [Tokenization (Токенизация)](/en/terms/tokenization-токенизация/)
- [NLP preprocessing (Предварительная обработка NLP)](/en/terms/nlp-preprocessing-предварительная-обработка-nlp/)
