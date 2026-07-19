---
title: Penyetelan Halus Supervisi
term_id: supervised_fine_tuning
category: training_techniques
subcategory: ''
tags:
- training
- LLM
- Fine-Tuning
difficulty: 4
weight: 1
slug: supervised_fine_tuning
date: '2026-07-18T15:36:17.841134Z'
lastmod: '2026-07-18T16:38:07.419800Z'
draft: false
source: agnes_llm
status: published
language: id
description: Proses melatih ulang model pra-latih pada dataset spesifik untuk menyesuaikannya
  dengan tugas atau domain tertentu.
---
## Definition

Penyetelan Halus Supervisi (SFT) melibatkan pengambilan model pra-latih berskala besar, seperti model bahasa, dan melanjutkan pelatihannya pada dataset kecil berkualitas tinggi yang berlabel untuk tugas turunan tertentu.

### Summary

Proses melatih ulang model pra-latih pada dataset spesifik untuk menyesuaikannya dengan tugas atau domain tertentu.

## Key Concepts

- Model Pra-Latih
- Pembelajaran Transfer
- Penyetelan Instruksi
- Adaptasi Domain

## Use Cases

- Pengembangan chatbot kustom
- Sistem tanya-jawab medis khusus
- Asisten generasi kode

## Code Example

```python
model.train()
for batch in dataloader:
    inputs, labels = batch
    outputs = model(inputs, labels=labels)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
```

## Related Terms

- [Pra-pelatihan (Pre-training)](/en/terms/pra-pelatihan-pre-training/)
- [Reinforcement Learning from Human Feedback (RLHF)](/en/terms/reinforcement-learning-from-human-feedback-rlhf/)
- [Rekayasa Prompt (Prompt Engineering)](/en/terms/rekayasa-prompt-prompt-engineering/)
- [LLM (Large Language Model)](/en/terms/llm-large-language-model/)
