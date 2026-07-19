---
title: Nadzorowane dostrajanie
term_id: supervised_fine_tuning
category: training_techniques
subcategory: ''
tags:
- training
- LLM
- Fine-Tuning
difficulty: 4
weight: 1
slug: supervised_fine_tuning
date: '2026-07-18T15:37:11.704016Z'
lastmod: '2026-07-18T17:15:08.837419Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Proces dalszego trenowania modelu wstępnie wytrenowanego na konkretnym
  zbiorze danych w celu dostosowania go do określonego zadania lub domeny.
---
## Definition

Nadzorowane dostrajanie (SFT) polega na przyjęciu dużego modelu wstępnie wytrenowanego, takiego jak model językowy, i kontynuowaniu jego treningu na mniejszym, wysokiej jakości zbiorze danych oznaczonym etykietami dla konkretnego zadania podrzędnego.

### Summary

Proces dalszego trenowania modelu wstępnie wytrenowanego na konkretnym zbiorze danych w celu dostosowania go do określonego zadania lub domeny.

## Key Concepts

- Modele wstępnie wytrenowane
- Uczenie transferowe
- Dostrajanie instrukcji
- Adaptacja domeny

## Use Cases

- Tworzenie niestandardowych chatbotów
- Specjalistyczne systemy pytań i odpowiedzi medycznych
- Asystenci generowania kodu

## Code Example

```python
model.train()
for batch in dataloader:
    inputs, labels = batch
    outputs = model(inputs, labels=labels)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
```

## Related Terms

- [Pre-training (trening wstępny)](/en/terms/pre-training-trening-wstępny/)
- [Reinforcement Learning from Human Feedback (uczenie przez wzmacnianie z ludzką informacją zwrotną)](/en/terms/reinforcement-learning-from-human-feedback-uczenie-przez-wzmacnianie-z-ludzką-informacją-zwrotną/)
- [Prompt Engineering (inżynieria promptów)](/en/terms/prompt-engineering-inżynieria-promptów/)
- [LLM (duży model językowy)](/en/terms/llm-duży-model-językowy/)
