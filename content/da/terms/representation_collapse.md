---
title: "Repræsentationskollaps"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /da/terms/representation_collapse/
date: "2026-07-18T16:15:02.198619Z"
lastmod: "2026-07-18T17:15:09.327794Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En fejlmåde inden for selvovervåget læring, hvor modellen udsender identiske repræsentationer for alle inputs, hvilket mister diskriminerende kraft."
---

## Definition

Repræsentationskollaps opstår, når et neuronnetværk, især i selvovervågede kontrastive læringsrammer, lærer at kortlægge alle datapunkter til den samme faste outputvektor. Dette trivielle resultat fjerner modellens evne til at differentiere mellem forskellige input.

### Summary

En fejlmåde inden for selvovervåget læring, hvor modellen udsender identiske repræsentationer for alle inputs, hvilket mister diskriminerende kraft.

## Key Concepts

- Selvovervåget Læring
- Kontraktiv Tab
- Trivielle Løsninger
- Funktionlæring

## Use Cases

- Fejlsøgning af SimCLR- eller MoCo-modeller
- Forbedring af Kontraktive Tab-funktioner
- Analyse af Modellens Konvergens

## Related Terms

- [Kontraktiv Læring](/en/terms/kontraktiv-læring/)
- [Batch-Normalisering](/en/terms/batch-normalisering/)
- [Momentum-Encoder](/en/terms/momentum-encoder/)
- [Funktionsekstraktion](/en/terms/funktionsekstraktion/)
