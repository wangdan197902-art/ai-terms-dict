---
title: "Közös tanulás"
term_id: "co_training"
category: "training_techniques"
subcategory: ""
tags: ["semi_supervised", "algorithm", "data_efficiency"]
difficulty: 4
weight: 1
slug: "co_training"
aliases:
  - /hu/terms/co_training/
date: "2026-07-18T15:49:31.008935Z"
lastmod: "2026-07-18T17:15:09.762502Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "A közös tanulás egy félig felügyelt tanuló algoritmus, ahol az adatok két nézetét használják fel különálló osztályozók tanításához, amelyek iteratívan címkézik egymás számára a címkézetlen adatokat."
---

## Definition

Ez a módszer kihasználja ugyanazon adathalmazok több különböző jellemzőkészletét (nézetet). Kezdetben két osztályozót tanítanak kis, címkézett adatokon minden nézetből. Ezek aztán címkéket jósolnak meg a címkézetlen

### Summary

A közös tanulás egy félig felügyelt tanuló algoritmus, ahol az adatok két nézetét használják fel különálló osztályozók tanításához, amelyek iteratívan címkézik egymás számára a címkézetlen adatokat.

## Key Concepts

- Fél felügyelt tanulás
- Több nézet
- Iteratív címkézés
- Magas bizalommal rendelkező kiválasztás

## Use Cases

- Szövegbesorolás több jellemzővel
- Weboldalkategorizálás
- Adataugmentáció korlátozott címkékkel

## Related Terms

- [Fél felügyelt tanulás](/en/terms/fél-felügyelt-tanulás/)
- [Ön-tanulás (Self-Training)](/en/terms/ön-tanulás-self-training/)
- [Többnézetes tanulás](/en/terms/többnézetes-tanulás/)
- [Aktív tanulás](/en/terms/aktív-tanulás/)
