---
title: Prompting Λιγών Παραδειγμάτων
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T15:40:44.253240Z'
lastmod: '2026-07-18T17:15:09.866371Z'
draft: false
source: agnes_llm
status: published
language: el
description: Το prompting λιγών παραδειγμάτων είναι μια τεχνική όπου στα μεγάλα γλωσσικά
  μοντέλα παρέχονται λίγα παραδείγματα εισόδου-εξόδου εντός της εντολής για τον καθορισμό
  της συμπεριφοράς τους.
---
## Definition

Αυτή η μέθοδος αξιοποιεί τις ικανότητες μάθησης εν περιεχομένων των μεγάλων γλωσσικών μοντέλων παρέχοντας λίγα παραστατικά παραδείγματα απευθείας στην εντολή. Σε αντίθεση με τη λεπτομερή ρύθμιση, η οποία απαιτεί την ενημέρωση των βαρών του μοντέλου, εδώ η γνώση ενσωματώνεται μέσω του context.

### Summary

Το prompting λιγών παραδειγμάτων είναι μια τεχνική όπου στα μεγάλα γλωσσικά μοντέλα παρέχονται λίγα παραδείγματα εισόδου-εξόδου εντός της εντολής για τον καθορισμό της συμπεριφοράς τους.

## Key Concepts

- Μάθηση εν περιεχομένων
- Μηχανική εντολών
- Οδηγία βασισμένη σε παραδείγματα
- Σύγκριση με μηδενικά παραδείγματα

## Use Cases

- Μορφοποίηση ανάλυσης συναισθήματος
- Προσαρμογή στυλ κώδικα
- Εξαγωγή δομημένων δεδομένων

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (μηδενικά παραδείγματα)](/en/terms/zero_shot-μηδενικά-παραδείγματα/)
- [prompt_engineering (μηχανική εντολών)](/en/terms/prompt_engineering-μηχανική-εντολών/)
- [in_context_learning (μάθηση εν περιεχομένων)](/en/terms/in_context_learning-μάθηση-εν-περιεχομένων/)
- [llm (μεγάλο γλωσσικό μοντέλο)](/en/terms/llm-μεγάλο-γλωσσικό-μοντέλο/)
