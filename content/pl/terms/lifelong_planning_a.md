---
title: Lifelong Planning A*
term_id: lifelong_planning_a
category: application_paradigms
subcategory: ''
tags:
- algorithms
- robotics
- Graph Theory
difficulty: 4
weight: 1
slug: lifelong_planning_a
date: '2026-07-18T16:03:57.818588Z'
lastmod: '2026-07-18T17:15:08.891967Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Algorytm wyszukiwania ścieżki inkrementalnej, który efektywnie aktualizuje
  najkrótsze ścieżki w dynamicznych grafach bez konieczności przeliczania ich od zera
  po zmianie wag krawędzi.
---
## Definition

Lifelong Planning A* (LPA*) jest rozszerzeniem algorytmu wyszukiwania A*, zaprojektowanym dla środowisk, w których koszty zmieniają się w czasie. Zamiast restartować wyszukiwanie, LPA* utrzymuje kolejkę priorytetową i aktualizuje tylko te części drzewa wyszukiwania, które zostały zmienione, co znacznie przyspiesza proces.

### Summary

Algorytm wyszukiwania ścieżki inkrementalnej, który efektywnie aktualizuje najkrótsze ścieżki w dynamicznych grafach bez konieczności przeliczania ich od zera po zmianie wag krawędzi.

## Key Concepts

- Wyszukiwanie inkrementalne
- Wyznaczanie ścieżki
- Grafy dynamiczne
- Nawigacja robotów

## Use Cases

- Trasy pojazdów autonomicznych w ruchu drogowym
- Nawigacja robotów w zmieniających się magazynach
- Ruch AI w grach strategicznych w czasie rzeczywistym

## Related Terms

- [a_star (algorytm A*)](/en/terms/a_star-algorytm-a/)
- [d_star (algorytm D*)](/en/terms/d_star-algorytm-d/)
- [incremental_search (wyszukiwanie inkrementalne)](/en/terms/incremental_search-wyszukiwanie-inkrementalne/)
- [path_planning (planowanie ścieżki)](/en/terms/path_planning-planowanie-ścieżki/)
