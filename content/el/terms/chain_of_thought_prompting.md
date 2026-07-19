---
title: "Prompting Σύνδεσης Σκέψης"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T15:39:30.151489Z"
lastmod: "2026-07-18T17:15:09.864209Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Το Prompting Σύνδεσης Σκέψης είναι μια τεχνική που ενθαρρύνει τα Μεγάλα Γλωσσικά Μοντέλα να παράγουν ενδιάμεσα βήματα λογικής πριν παράγουν μια τελική απάντηση."
---
## Definition

Το Prompting Σύνδεσης Σκέψης (Chain-of-Thought - CoT) βελτιώνει τις επιδόσεις των μεγάλων γλωσσικών μοντέλων σε σύνθετα καθήκοντα λογικής ζητώντας ρητά από το μοντέλο να διατυπώσει τη λογική του βήμα προς βήμα. Αντί να πηδάει απευθείας

### Summary

Το Prompting Σύνδεσης Σκέψης είναι μια τεχνική που ενθαρρύνει τα Μεγάλα Γλωσσικά Μοντέλα να παράγουν ενδιάμεσα βήματα λογικής πριν παράγουν μια τελική απάντηση.

## Key Concepts

- Λογική Βήμα προς Βήμα
- Μάθηση Few-Shot
- Λογική Συλλογιστική
- Ενδιάμεσα Βήματα

## Use Cases

- Επίλυση μαθηματικών προβλημάτων
- Σύνθετα καθήκοντα λογικής συλλογιστικής
- Αποσφαλμάτωση σφαλμάτων στη δημιουργία κώδικα

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (Prompting μηδενικών παραδειγμάτων)](/en/terms/zero-shot-prompting-prompting-μηδενικών-παραδειγμάτων/)
- [Few-Shot Prompting (Prompting λίγων παραδειγμάτων)](/en/terms/few-shot-prompting-prompting-λίγων-παραδειγμάτων/)
- [Self-Consistency (Αυτοσυνέπεια)](/en/terms/self-consistency-αυτοσυνέπεια/)
- [Reasoning (Λογική συλλογιστική)](/en/terms/reasoning-λογική-συλλογιστική/)
