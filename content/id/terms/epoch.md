---
title: Epoch
term_id: epoch
category: training_techniques
subcategory: ''
tags:
- training
- Neural Networks
- basics
difficulty: 2
weight: 1
slug: epoch
date: '2026-07-18T15:49:34.400551Z'
lastmod: '2026-07-18T16:38:07.455552Z'
draft: false
source: agnes_llm
status: published
language: id
description: Satu putaran lengkap dataset pelatihan melalui algoritme pembelajaran
  mesin selama pelatihan model.
---
## Definition

Dalam pembelajaran mesin, epoch mewakili satu iterasi tunggal atas seluruh dataset pelatihan. Selama setiap epoch, model memproses semua contoh pelatihan, memperbarui bobotnya melalui backpropagation, dan mengevaluasi kinerja terhadap data validasi.

### Summary

Satu putaran lengkap dataset pelatihan melalui algoritme pembelajaran mesin selama pelatihan model.

## Key Concepts

- Iterasi Pelatihan
- Backpropagation
- Konvergensi
- Penyetelan Hyperparameter

## Use Cases

- Mengonfigurasi loop pelatihan jaringan saraf
- Memantau kerugian validasi per siklus
- Mengimplementasikan strategi penghentian dini

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch Size (Ukuran Batch)](/en/terms/batch-size-ukuran-batch/)
- [Iteration (Iterasi)](/en/terms/iteration-iterasi/)
- [Learning Rate (Laju Pembelajaran)](/en/terms/learning-rate-laju-pembelajaran/)
- [Overfitting (Kelebihan Cocok)](/en/terms/overfitting-kelebihan-cocok/)
