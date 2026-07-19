---
title: Ko-træning
term_id: co_training
category: training_techniques
subcategory: ''
tags:
- Semi Supervised
- algorithm
- Data Efficiency
difficulty: 4
weight: 1
slug: co_training
date: '2026-07-18T15:45:27.845980Z'
lastmod: '2026-07-18T17:15:09.268386Z'
draft: false
source: agnes_llm
status: published
language: da
description: Ko-træning er en semi-overvåget læringsalgoritme, hvor to perspektiver
  på dataene bruges til at træne separate klassifikatorer, der iterativt mærker ulabelerede
  data for hinanden.
---
## Definition

Denne metode udnytter flere distinkte sæt af funktioner (perspektiver) fra de samme datapunkter. Indledningsvis trænes to klassifikatorer på små mærkede datasæt fra hvert perspektiv. De forudsiger derefter etiketter for ulabel

### Summary

Ko-træning er en semi-overvåget læringsalgoritme, hvor to perspektiver på dataene bruges til at træne separate klassifikatorer, der iterativt mærker ulabelerede data for hinanden.

## Key Concepts

- Semi-overvåget læring
- Flere perspektiver
- Iterativ mærkning
- Selektion baseret på høj konfidens

## Use Cases

- Tekstklassificering med flere funktioner
- Kategorisering af websider
- Dataaugmentation med begrænsede etiketter

## Related Terms

- [Semi-overvåget læring](/en/terms/semi-overvåget-læring/)
- [Selvtræning](/en/terms/selvtræning/)
- [Multi-perspektiv læring](/en/terms/multi-perspektiv-læring/)
- [Aktiv læring](/en/terms/aktiv-læring/)
