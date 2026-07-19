---
title: Szkolenie współdziałające
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
date: '2026-07-18T15:45:43.110758Z'
lastmod: '2026-07-18T17:15:08.854275Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Szkolenie współdziałające to algorytm uczenia półnadzorowanego, w którym
  dwa widoki danych są wykorzystywane do trenowania oddzielnych klasyfikatorów, które
  iteracyjnie oznaczają nieoznaczone dane dla
---
## Definition

Ta metoda wykorzystuje wiele różnych zestawów cech (widoków) tych samych punktów danych. Początkowo dwa klasyfikatory są trenowane na małych zestawach danych oznaczonych z każdego widoku. Następnie przewidują etykiety dla nieozna

### Summary

Szkolenie współdziałające to algorytm uczenia półnadzorowanego, w którym dwa widoki danych są wykorzystywane do trenowania oddzielnych klasyfikatorów, które iteracyjnie oznaczają nieoznaczone dane dla siebie nawzajem.

## Key Concepts

- Uczenie półnadzorowane
- Wiele widoków
- Iteracyjne oznaczanie
- Wybór o wysokim poziomie pewności

## Use Cases

- Klasyfikacja tekstu z wieloma cechami
- Kategoryzacja stron internetowych
- Augmentacja danych przy ograniczonych etykietach

## Related Terms

- [Uczenie półnadzorowane](/en/terms/uczenie-półnadzorowane/)
- [Szkolenie własne (Self-Training)](/en/terms/szkolenie-własne-self-training/)
- [Uczenie wielowidokowe](/en/terms/uczenie-wielowidokowe/)
- [Uczenie aktywne](/en/terms/uczenie-aktywne/)
