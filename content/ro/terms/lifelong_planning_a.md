---
title: "Planificare pe viață A*"
term_id: "lifelong_planning_a"
category: "application_paradigms"
subcategory: ""
tags: ["algorithms", "robotics", "graph_theory"]
difficulty: 4
weight: 1
slug: "lifelong_planning_a"
aliases:
  - /ro/terms/lifelong_planning_a/
date: "2026-07-18T16:08:34.181746Z"
lastmod: "2026-07-18T17:15:09.675031Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Un algoritm incrementali de găsire a drumului care actualizează eficient cele mai scurte căi în grafuri dinamice fără a recalculea de la zero după modificările greutăților muchiilor."
---

## Definition

Lifelong Planning A* (LPA*) este o extensie a algoritmului de căutare A* concepută pentru medii în care costurile se schimbă în timp. În loc să repornească căutarea, LPA* menține o coadă de priorități și actualizează doar nodurile afectate de modificări, asigurând o eficiență superioară în scenarii dinamice.

### Summary

Un algoritm incrementali de găsire a drumului care actualizează eficient cele mai scurte căi în grafuri dinamice fără a recalculea de la zero după modificările greutăților muchiilor.

## Key Concepts

- Căutare incrementală
- Găsirea traseului
- Grafuri dinamice
- Navigație robotică

## Use Cases

- Rutarea vehiculelor autonome în trafic
- Navigația roboților în depozite care se schimbă
- Mișcarea IA în jocurile de strategie în timp real

## Related Terms

- [a_star (algoritmul A*)](/en/terms/a_star-algoritmul-a/)
- [d_star (algoritmul D*)](/en/terms/d_star-algoritmul-d/)
- [incremental_search (căutare incrementală)](/en/terms/incremental_search-căutare-incrementală/)
- [path_planning (planificarea traseului)](/en/terms/path_planning-planificarea-traseului/)
