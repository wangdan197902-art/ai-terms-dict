---
title: "Hierarchická navigovatelná malá světová síť"
term_id: "hierarchical_navigable_small_world"
category: "basic_concepts"
subcategory: ""
tags: ["algorithms", "search", "data_structures"]
difficulty: 4
weight: 1
slug: "hierarchical_navigable_small_world"
aliases:
  - /cs/terms/hierarchical_navigable_small_world/
date: "2026-07-18T16:01:17.680438Z"
lastmod: "2026-07-18T17:15:09.138660Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Datová struktura založená na grafech umožňující efektivní aproximované hledání nejbližších sousedů ve vysoce dimenzionálních prostorech."
---

## Definition

Algoritmus Hierarchická navigovatelná malá světová síť (HNSW) konstruuje vícevrstvý graf, kde každá vrstva obsahuje podmnožinu uzlů z vrstvy pod ní. Navigace začíná v horní vrstvě, která slouží jako expresní dálnice pro rychlý přesun blízko cíle, a postupně sestupuje do spodních vrstev pro přesné hledání. Tento přístup kombinuje výhody malých světových sítí s hierarchickou strukturou pro dosažení vysoké rychlosti a přesnosti při aproximovaném hledání nejbližších sousedů.

### Summary

Datová struktura založená na grafech umožňující efektivní aproximované hledání nejbližších sousedů ve vysoce dimenzionálních prostorech.

## Key Concepts

- Prohledávání grafu
- Aproximovaný nejbližší soused
- Vícevrstvý graf
- Logaritmická složitost

## Use Cases

- Vektorové vyhledávání
- Doporučovací systémy
- Vyhledávání obrázků

## Related Terms

- [K nejbližších sousedů (K-Nearest Neighbors)](/en/terms/k-nejbližších-sousedů-k-nearest-neighbors/)
- [Faiss (knihovna pro vektorové vyhledávání)](/en/terms/faiss-knihovna-pro-vektorové-vyhledávání/)
- [Annoy (knihovna pro aproximované nejbližší sousedy)](/en/terms/annoy-knihovna-pro-aproximované-nejbližší-sousedy/)
