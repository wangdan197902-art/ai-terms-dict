---
title: "Lánc-gondolkodásos promptolás"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /hu/terms/chain_of_thought_prompting/
date: "2026-07-18T15:37:16.238032Z"
lastmod: "2026-07-18T17:15:09.739005Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "A Lánc-gondolkodásos promptolás egy technika, amely ösztönzi a nagy nyelvi modelleket (LLM), hogy a végső válasz előtt generáljanak köztes érvelési lépéseket."
---

## Definition

A Lánc-gondolkodásos (CoT) promptolás javítja a nagy nyelvi modellek teljesítményét a komplex érvelési feladatokon azzal, hogy kifejezetten kéri a modellt, hogy taglalja lépésről lépésre a logikáját. Ehelyett, hogy közvetlenül ugrana a válaszra, a modell először levezeti az eredményt.

### Summary

A Lánc-gondolkodásos promptolás egy technika, amely ösztönzi a nagy nyelvi modelleket (LLM), hogy a végső válasz előtt generáljanak köztes érvelési lépéseket.

## Key Concepts

- Lépésről lépésre történő érvelés
- Kevés mintás tanulás
- Logikai következtetés
- Köztes lépések

## Use Cases

- Matematikai szöveges feladatok megoldása
- Komplex logikai érvelési feladatok
- Kódgenerálási hibák hibakeresése

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Nulladik mintás promptolás (prompt példa nélkül)](/en/terms/nulladik-mintás-promptolás-prompt-példa-nélkül/)
- [Kevés mintás promptolás (néhány példával)](/en/terms/kevés-mintás-promptolás-néhány-példával/)
- [Ön-konzisztencia (több válasz összehasonlítása)](/en/terms/ön-konzisztencia-több-válasz-összehasonlítása/)
- [Érvelés (logikai gondolkodás)](/en/terms/érvelés-logikai-gondolkodás/)
