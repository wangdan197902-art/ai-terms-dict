---
title: "TensorFlow Hub"
term_id: "tensorflow_hub"
category: "basic_concepts"
subcategory: ""
tags: ["tensorflow", "libraries", "transfer-learning"]
difficulty: 3
weight: 1
slug: "tensorflow_hub"
aliases:
  - /id/terms/tensorflow_hub/
date: "2026-07-18T16:10:44.135717Z"
lastmod: "2026-07-18T16:38:07.513371Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Repositori untuk modul pembelajaran mesin yang dapat digunakan kembali, memungkinkan pembelajaran transfer dengan model yang telah dilatih sebelumnya."
---

## Definition

TensorFlow Hub adalah platform untuk mempublikasikan dan menggunakan kembali komponen pembelajaran mesin. Platform ini memungkinkan pengembang mengakses model yang telah dilatih sebelumnya untuk berbagai tugas seperti klasifikasi gambar, embedding teks, dan lainnya.

### Summary

Repositori untuk modul pembelajaran mesin yang dapat digunakan kembali, memungkinkan pembelajaran transfer dengan model yang telah dilatih sebelumnya.

## Key Concepts

- Pembelihan transfer
- Penggunaan ulang modul
- Model terlatih sebelumnya
- Efisiensi

## Use Cases

- Prototipe model cepat
- Mengurangi biaya pelatihan
- Mengimplementasikan NLP/CV terkini

## Code Example

```python
import tensorflow_hub as hub
module = hub.load('https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5')
```

## Related Terms

- [Hugging Face](/en/terms/hugging-face/)
- [Keras Applications (Aplikasi Keras)](/en/terms/keras-applications-aplikasi-keras/)
- [Transfer Learning (Pembelihan Transfer)](/en/terms/transfer-learning-pembelihan-transfer/)
- [Model Zoo (Zoo Model)](/en/terms/model-zoo-zoo-model/)
