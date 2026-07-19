---
title: "Model Embedding"
term_id: "embedding_model"
category: "application_paradigms"
subcategory: ""
tags: ["NLP", "Representation Learning", "Search"]
difficulty: 4
weight: 1
slug: "embedding_model"
date: "2026-07-18T15:34:15.539791Z"
lastmod: "2026-07-18T16:38:07.412907Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Model embedding mengubah data mentah seperti teks atau gambar menjadi vektor numerik padat yang mewakili makna semantik."
---
## Definition

Model-model ini memetakan data berdimensi tinggi ke dalam ruang vektor kontinu berdimensi lebih rendah di mana item serupa berada lebih dekat satu sama lain. Transformasi ini menangkap hubungan semantik, memungkinkan mesin memahami konteks dan makna.

### Summary

Model embedding mengubah data mentah seperti teks atau gambar menjadi vektor numerik padat yang mewakili makna semantik.

## Key Concepts

- Representasi Vektor
- Kesamaan Semantik
- Pengurangan Dimensi
- Ekstraksi Fitur

## Use Cases

- Membangun mesin pencari semantik
- Sistem rekomendasi untuk produk atau konten
- Mengelompokkan dokumen atau gambar yang serupa

## Code Example

```python
from transformers import AutoTokenizer, AutoModel
import torch

model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
inputs = tokenizer('Hello world', return_tensors='pt')
embeddings = model(**inputs).last_hidden_state.mean(dim=1)
```

## Related Terms

- [Word2Vec (Model representasi kata)](/en/terms/word2vec-model-representasi-kata/)
- [BERT (Model bahasa terenkripsi bidirectional)](/en/terms/bert-model-bahasa-terenkripsi-bidirectional/)
- [Vector Database (Basis data vektor)](/en/terms/vector-database-basis-data-vektor/)
- [Similarity Search (Pencarian kesamaan)](/en/terms/similarity-search-pencarian-kesamaan/)
