---
title: Kolaps reprezentace
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
date: '2026-07-18T16:15:42.633808Z'
lastmod: '2026-07-18T17:15:09.196917Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Selhání v sebeučení, kdy model generuje pro všechny vstupy identické
  reprezentace, čímž ztrácí diskriminační schopnosti.
---
## Definition

Kolaps reprezentace nastává, když neuronová síť, zejména v rámci kontrastního sebeučení, naučí se mapovat všechny vstupní datové body na stejný pevný výstupní vektor. Jde o triviální řešení, které model ignoruje strukturu dat.

### Summary

Selhání v sebeučení, kdy model generuje pro všechny vstupy identické reprezentace, čímž ztrácí diskriminační schopnosti.

## Key Concepts

- Sebeučení
- Kontrastivní ztráta
- Triviální řešení
- Učení vlastností

## Use Cases

- Ladění modelů SimCLR nebo MoCo
- Vylepšování funkcí kontrastivní ztráty
- Analýza konvergence modelu

## Related Terms

- [Kontrastivní učení](/en/terms/kontrastivní-učení/)
- [Batch normalizace](/en/terms/batch-normalizace/)
- [Enkóder hybnosti](/en/terms/enkóder-hybnosti/)
- [Extrakce vlastností](/en/terms/extrakce-vlastností/)
