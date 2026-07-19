---
title: Algoritmo Attore-Critico
term_id: actor_critic_algorithm
category: basic_concepts
subcategory: ''
tags:
- Reinforcement Learning
- Neural Networks
- algorithms
difficulty: 4
weight: 1
slug: actor_critic_algorithm
date: '2026-07-18T15:44:17.069877Z'
lastmod: '2026-07-18T17:15:08.595674Z'
draft: false
source: agnes_llm
status: published
language: it
description: 'Un framework di apprendimento per rinforzo che combina metodi basati
  sul valore e sul policy utilizzando due reti neurali: un attore e un critico.'
---
## Definition

L'algoritmo attore-critico impiega due componenti: l'attore, che aggiorna la policy per selezionare le azioni, e il critico, che valuta la qualità di tali azioni stimando la funzione valore. Questa architettura ibrida permette di combinare i vantaggi dell'apprendimento per differenza temporale con l'ottimizzazione diretta della policy.

### Summary

Un framework di apprendimento per rinforzo che combina metodi basati sul valore e sul policy utilizzando due reti neurali: un attore e un critico.

## Key Concepts

- Gradiente della policy
- Funzione valore
- Errore di differenza temporale
- RL ibrido

## Use Cases

- Manipolazione di bracci robotici
- Agenti per giochi (es. AlphaStar)
- Sistemi di controllo continuo nei veicoli autonomi

## Related Terms

- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [A3C (Asynchronous Advantage Actor-Critic)](/en/terms/a3c-asynchronous-advantage-actor-critic/)
- [policy_gradient (gradiente della policy)](/en/terms/policy_gradient-gradiente-della-policy/)
- [value_function (funzione valore)](/en/terms/value_function-funzione-valore/)
