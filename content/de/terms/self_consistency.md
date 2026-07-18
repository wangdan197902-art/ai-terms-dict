---
title: "Selbstkonsistenz"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
aliases:
  - /de/terms/self_consistency/
date: "2026-07-18T11:32:49.644516Z"
lastmod: "2026-07-18T11:44:44.983822Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Selbstkonsistenz ist eine Dekodierungsstrategie, bei der mehrere Denkpfade abgetastet und die am häufigsten vorkommende Antwort als endgültige Ausgabe ausgewählt wird."
---

## Definition

Diese Technik wird hauptsächlich bei Large Language Models (LLMs) eingesetzt und verbessert die Genauigkeit, indem sie durch Abtasten mehrere diverse Antworten auf einen Prompt generiert. Anstatt sich auf gierisches Dekodieren (greedy decoding) zu verlassen, aggregiert sie die Ergebnisse, um konsistente und korrektere Ausgaben zu erzielen.

### Summary

Selbstkonsistenz ist eine Dekodierungsstrategie, bei der mehrere Denkpfade abgetastet und die am häufigsten vorkommende Antwort als endgültige Ausgabe ausgewählt wird.

## Key Concepts

- Mehrheitsentscheidung
- Dekodierungsstrategie
- LLM-Reasoning
- Reduzierung von Halluzinationen

## Use Cases

- Mathematische Textaufgaben
- Komplexe logische Deduktion
- Aufgaben zur Code-Synthese

## Related Terms

- [Chain-of-Thought](/en/terms/chain-of-thought/)
- [Temperaturabtastung](/en/terms/temperaturabtastung/)
- [Ensemble-Methoden](/en/terms/ensemble-methoden/)
- [Prompt Engineering](/en/terms/prompt-engineering/)
