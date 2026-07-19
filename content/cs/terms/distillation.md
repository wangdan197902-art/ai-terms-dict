---
title: Destilace
term_id: distillation
category: training_techniques
subcategory: ''
tags:
- Optimization
- compression
- Model Efficiency
difficulty: 3
weight: 1
slug: distillation
date: '2026-07-18T15:24:25.501697Z'
lastmod: '2026-07-18T17:15:09.066423Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Destilace znalostí je technika komprese modelu, při které se menší model
  studenta učí napodobovat chování většího modelu učitele.
---
## Definition

Tento proces zahrnuje přenos znalostí ze složitého, vysoce výkonného neuronového sítě 'učitele' do jednodušší, efektivnější 'studentovy' sítě. Student se učí nejen z pevných štítků (hard labels), ale také z měkkých cílů (soft targets), které obsahují více informací o rozdělení pravděpodobnosti tříd.

### Summary

Destilace znalostí je technika komprese modelu, při které se menší model studenta učí napodobovat chování většího modelu učitele.

## Key Concepts

- Architektura Učitel-Student
- Měkké cíle (Soft Targets)
- Komprese modelu
- Efektivita inference

## Use Cases

- Nasazování velkých jazykových modelů na mobilní zařízení
- Snížení latence v aplikacích počítačového vidění v reálném čase
- Optimalizace hlubokých učebních modelů pro prostředí okrajových výpočtů (edge computing)

## Related Terms

- [Kvantizace (snížení přesnosti číselných reprezentací)](/en/terms/kvantizace-snížení-přesnosti-číselných-reprezentací/)
- [Pruning (odstraňování méně důležitých váh/neuronů)](/en/terms/pruning-odstraňování-méně-důležitých-váh-neuronů/)
- [Přenosové učení (použití znalostí z jedné domény v jiné)](/en/terms/přenosové-učení-použití-znalostí-z-jedné-domény-v-jiné/)
- [Vyhledávání neuronové architektury (automatický návrh struktur sítí)](/en/terms/vyhledávání-neuronové-architektury-automatický-návrh-struktur-sítí/)
