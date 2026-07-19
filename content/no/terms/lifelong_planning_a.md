---
title: Livslang planlegging A*
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
date: '2026-07-18T16:02:37.288933Z'
lastmod: '2026-07-18T16:38:07.019047Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En inkrementell sti-finningsalgoritme som effektivt oppdaterer korteste
  veier i dynamiske grafer uten å beregne på nytt fra bunnen av etter endringer i
  kantvekt.
---
## Definition

Livslang planlegging A* (LPA*) er en utvidelse av A*-søkealgoritmen designet for miljøer der kostnader endrer seg over tid. I stedet for å starte søket på nytt, vedlikeholder LPA* en prioritetskø og oppdaterer kun de nodene som påvirkes av endringene, noe som gjør den mye raskere enn å kjøre A* på nytt i dynamiske miljøer.

### Summary

En inkrementell sti-finningsalgoritme som effektivt oppdaterer korteste veier i dynamiske grafer uten å beregne på nytt fra bunnen av etter endringer i kantvekt.

## Key Concepts

- Inkrementell søking
- Sti-finding
- Dynamiske grafer
- Robotikk-navigasjon

## Use Cases

- Ruting for autonome kjøretøy i trafikk
- Robots navigasjon i endrende lagermiljøer
- AI-bevegelse i sanntids strategispill

## Related Terms

- [a_star (A*-algoritmen)](/en/terms/a_star-a-algoritmen/)
- [d_star (D*-algoritmen)](/en/terms/d_star-d-algoritmen/)
- [incremental_search (inkrementell søking)](/en/terms/incremental_search-inkrementell-søking/)
- [path_planning (sti-planlegging)](/en/terms/path_planning-sti-planlegging/)
