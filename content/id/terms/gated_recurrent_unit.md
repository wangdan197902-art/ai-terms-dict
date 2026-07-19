---
title: "Unit Rekuren Gerbang"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T15:51:39.525713Z"
lastmod: "2026-07-18T16:38:07.461363Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Jenis arsitektur jaringan saraf rekuren yang menggunakan mekanisme gerbang untuk mengontrol aliran informasi, berfungsi sebagai alternatif yang disederhanakan dari LSTM."
---
## Definition

Unit Rekuren Gerbang (GRU) adalah sel jaringan saraf rekuren (RNN) khusus yang dirancang untuk menangkap ketergantungan jangka panjang dalam data sekuensial. GRU menyederhanakan arsitektur Long Short-Term Memory (LSTM)

### Summary

Jenis arsitektur jaringan saraf rekuren yang menggunakan mekanisme gerbang untuk mengontrol aliran informasi, berfungsi sebagai alternatif yang disederhanakan dari LSTM.

## Key Concepts

- Jaringan Saraf Rekuren
- Gerbang Pembaruan
- Gerbang Reset
- Pemodelan Urutan

## Use Cases

- Pemrosesan bahasa alami
- Peramalan deret waktu
- Pengenalan suara

## Code Example

```python
import torch.nn as nn

# Define a simple GRU layer
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1)

# Example input: (seq_len, batch, input_size)
input_data = torch.randn(5, 3, 10)
hidden_state = None

output, hidden = gru(input_data, hidden_state)
```

## Related Terms

- [LSTM](/en/terms/lstm/)
- [RNN (Jaringan Saraf Rekuren)](/en/terms/rnn-jaringan-saraf-rekuren/)
- [Deep Learning (Pembelajaran Mendalam)](/en/terms/deep-learning-pembelajaran-mendalam/)
- [Sequence-to-Sequence (Urutan ke Urutan)](/en/terms/sequence-to-sequence-urutan-ke-urutan/)
