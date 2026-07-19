---
title: Representationskollaps
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
date: '2026-07-18T16:19:10.924099Z'
lastmod: '2026-07-18T17:15:09.043717Z'
draft: false
source: agnes_llm
status: published
language: sv
description: Ett misslyckandemönster inom självövervakat lärande där modellen产ar identiska
  representationer för alla indata, vilket förlorar diskrimineringsförmåga.
---
## Definition

Representationskollaps inträffar när ett neuralt nätverk, särskilt inom kontrastiva självövervakade ramverk, lär sig att mappa alla datapunkter till samma fasta utmatningsvektor. Detta triviala lösning ignorerar den underliggande strukturen i datan.

### Summary

Ett misslyckandemönster inom självövervakat lärande där modellen产ar identiska representationer för alla indata, vilket förlorar diskrimineringsförmåga.

## Key Concepts

- Självövervakat lärande
- Kontraktivt förlustmått
- Triviala lösningar
- Funktionlärande

## Use Cases

- Felsökning av SimCLR- eller MoCo-modeller
- Förbättring av Kontraktiva Förlustfunktioner
- Analys av Modellkonvergens

## Related Terms

- [Kontraktivt lärande](/en/terms/kontraktivt-lärande/)
- [Batchnormalisering](/en/terms/batchnormalisering/)
- [Momentumkodare](/en/terms/momentumkodare/)
- [Funktionsextrahering](/en/terms/funktionsextrahering/)
