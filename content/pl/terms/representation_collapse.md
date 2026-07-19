---
title: Zapadanie reprezentacji
term_id: representation_collapse
category: basic_concepts
subcategory: ''
tags:
- Self Supervised
- Training Dynamics
- Computer Vision
difficulty: 3
weight: 1
slug: representation_collapse
date: '2026-07-18T16:15:04.160011Z'
lastmod: '2026-07-18T17:15:08.913977Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Tryb awarii w uczeniu samonadzorowanym, w którym model generuje identyczne
  reprezentacje dla wszystkich danych wejściowych, tracąc zdolność dyskryminacyjną.
---
## Definition

Zapadanie reprezentacji występuje, gdy sieć neuronowa, szczególnie w ramach kontrastywnego uczenia samonadzorowanego, uczy się mapowania wszystkich punktów danych wejściowych na ten sam stały wektor wyjściowy. Jest to trywialne rozwiązanie, które uniemożliwia modelowi nauczenie się sensownych cech danych.

### Summary

Tryb awarii w uczeniu samonadzorowanym, w którym model generuje identyczne reprezentacje dla wszystkich danych wejściowych, tracąc zdolność dyskryminacyjną.

## Key Concepts

- Uczenie samonadzorowane
- Strata kontrastywna
- Rozwiązania trywialne
- Uczenie cech

## Use Cases

- Debugowanie modeli SimCLR lub MoCo
- Poprawa funkcji straty kontrastywnej
- Analiza zbieżności modelu

## Related Terms

- [Uczenie kontrastywne](/en/terms/uczenie-kontrastywne/)
- [Normalizacja wsadowa](/en/terms/normalizacja-wsadowa/)
- [Enkoder z pędem](/en/terms/enkoder-z-pędem/)
- [Ekstrakcja cech](/en/terms/ekstrakcja-cech/)
