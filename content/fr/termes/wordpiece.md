---
title: "WordPiece"
term_id: "wordpiece"
category: "engineering_practice"
subcategory: ""
tags: ["nlp", "tokenization", "bert"]
difficulty: 3
weight: 1
slug: "wordpiece"
aliases:
  - /fr/terms/wordpiece/
date: "2026-07-18T11:43:05.960152Z"
lastmod: "2026-07-18T11:44:45.359064Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un algorithme de tokenisation par sous-mots qui fusionne récursivement les paires de caractères les plus fréquentes pour gérer les mots hors vocabulaire."
---

## Definition

WordPiece est une méthode de tokenisation largement utilisée dans les modèles de traitement du langage naturel tels que BERT et ALBERT. Elle décompose les mots en unités de sous-mots plus petites afin de gérer la richesse morphologique et de réduire la taille du vocabulaire, permettant ainsi de mieux traiter les mots rares ou inconnus.

### Summary

Un algorithme de tokenisation par sous-mots qui fusionne récursivement les paires de caractères les plus fréquentes pour gérer les mots hors vocabulaire.

## Key Concepts

- Tokenisation par sous-mot
- Expansion du vocabulaire
- Gestion des mots hors vocabulaire
- Analyse morphologique

## Use Cases

- Prétraitement du texte pour les modèles BERT
- Traitement des langues à ressources limitées
- Réduction de la taille de la matrice d'embedding

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (autre algorithme de segmentation de sous-mots)](/en/terms/byte-pair-encoding-autre-algorithme-de-segmentation-de-sous-mots/)
- [SentencePiece (bibliothèque d'implémentation de tokenisation)](/en/terms/sentencepiece-bibliothèque-d-implémentation-de-tokenisation/)
- [Tokenisation (processus de division du texte en unités significatives)](/en/terms/tokenisation-processus-de-division-du-texte-en-unités-significatives/)
- [Prétraitement NLP (nettoyage et préparation des données textuelles)](/en/terms/prétraitement-nlp-nettoyage-et-préparation-des-données-textuelles/)
