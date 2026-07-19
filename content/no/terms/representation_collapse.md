---
title: Representasjonskollaps
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
date: '2026-07-18T16:14:45.303044Z'
lastmod: '2026-07-18T16:38:07.042821Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En feiltilstand i selvtilsynslæring der modellen produserer identiske
  representasjoner for alle inndata, noe som fører til tap av diskriminerende evne.
---
## Definition

Representasjonskollaps oppstår når et neuronettverk, spesielt i selvtilsyns kontrastiv læring, lærer å kartlegge alle inndata til samme faste utvektorsvektor. Dette er en triviell løsning der modellen ikke lærer meningsfulle trekk.

### Summary

En feiltilstand i selvtilsynslæring der modellen produserer identiske representasjoner for alle inndata, noe som fører til tap av diskriminerende evne.

## Key Concepts

- Selvtilsynslæring
- Kontraktiv Tapsfunksjon
- Trivielle Løsninger
- Funktjonslæring

## Use Cases

- Feilsøking av SimCLR- eller MoCo-modeller
- Forbedring av Kontraktive Tapsfunksjoner
- Analyse av Modellkonvergens

## Related Terms

- [Kontraktiv Læring](/en/terms/kontraktiv-læring/)
- [Batch-normalisering](/en/terms/batch-normalisering/)
- [Momentum-koder](/en/terms/momentum-koder/)
- [Funksjonsekstraksjon](/en/terms/funksjonsekstraksjon/)
