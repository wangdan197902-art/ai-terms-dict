---
title: "Keruntuhan Representasi"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /id/terms/representation_collapse/
date: "2026-07-18T16:07:27.548808Z"
lastmod: "2026-07-18T16:38:07.500972Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Modus kegagalan dalam pembelajaran mandiri di mana model menghasilkan representasi identik untuk semua masukan, sehingga kehilangan daya diskriminatifnya."
---

## Definition

Keruntuhan representasi terjadi ketika jaringan saraf, khususnya dalam kerangka kerja pembelajaran kontrasitif mandiri, belajar memetakan semua titik data masukan ke vektor keluaran tetap yang sama. Ini merupakan solusi sepele yang harus dihindari agar model dapat mempelajari fitur yang bermakna.

### Summary

Modus kegagalan dalam pembelajaran mandiri di mana model menghasilkan representasi identik untuk semua masukan, sehingga kehilangan daya diskriminatifnya.

## Key Concepts

- Pembelajaran Mandiri
- Fungsi Kerugian Kontrasitif
- Solusi Sepele
- Pembelajaran Fitur

## Use Cases

- Debugging Model SimCLR atau MoCo
- Meningkatkan Fungsi Kerugian Kontrasitif
- Menganalisis Konvergensi Model

## Related Terms

- [Pembelajaran Kontrasitif](/en/terms/pembelajaran-kontrasitif/)
- [Normalisasi Batch](/en/terms/normalisasi-batch/)
- [Encoder Momentum](/en/terms/encoder-momentum/)
- [Ekstraksi Fitur](/en/terms/ekstraksi-fitur/)
