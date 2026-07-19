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
date: '2026-07-18T15:27:25.926996Z'
lastmod: '2026-07-18T15:51:59.542685Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um algoritmo de tokenização de subpalavras que mescla recursivamente
  os pares de caracteres mais frequentes para lidar com palavras fora do vocabulário.
---
## Definition

O WordPiece é um método de tokenização amplamente utilizado em modelos de processamento de linguagem natural, como BERT e ALBERT. Ele divide palavras em unidades menores de subpalavras para gerenciar a riqueza morfológica e reduzir o tamanho do vocabulário, permitindo que o modelo lide eficazmente com palavras raras ou não vistas anteriormente.

### Summary

Um algoritmo de tokenização de subpalavras que mescla recursivamente os pares de caracteres mais frequentes para lidar com palavras fora do vocabulário.

## Key Concepts

- Tokenização de subpalavras
- Expansão de vocabulário
- Tratamento de palavras fora do vocabulário
- Análise morfológica

## Use Cases

- Pré-processamento de texto para modelos BERT
- Manipulação de idiomas com poucos recursos
- Redução do tamanho da matriz de embeddings

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (codificação por par de bytes)](/en/terms/byte-pair-encoding-codificação-por-par-de-bytes/)
- [SentencePiece (biblioteca de tokenização independente de idioma)](/en/terms/sentencepiece-biblioteca-de-tokenização-independente-de-idioma/)
- [Tokenização (processo de dividir texto em unidades)](/en/terms/tokenização-processo-de-dividir-texto-em-unidades/)
- [Pré-processamento de PLN (tratamento inicial de dados textuais)](/en/terms/pré-processamento-de-pln-tratamento-inicial-de-dados-textuais/)
