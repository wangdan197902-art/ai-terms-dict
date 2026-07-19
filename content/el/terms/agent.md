---
title: "Πράκτορας"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T15:22:22.602242Z"
lastmod: "2026-07-18T17:15:09.837541Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Ένα σύστημα τεχνητής νοημοσύνης ικανό να αντιλαμβάνεται το περιβάλλον του, να σκέφτεται και να αναλαμβάνει δράσεις για την επίτευξη συγκεκριμένων στόχων αυτόνομα."
---
## Definition

Στην τεχνητή νοημοσύνη, ένας πράκτορας είναι μια οντότητα που ενεργεί εκ μέρους ενός χρήστη ή συστήματος για την ολοκλήρωση εργασιών. Σε αντίθεση με παθητικά μοντέλα που απαντούν μόνο σε prompts, οι πράκτορες μπορούν να σχεδιάσουν, να χρησιμοποιήσουν εργαλεία και να επαναλάβουν τις ενέργειές τους.

### Summary

Ένα σύστημα τεχνητής νοημοσύνης ικανό να αντιλαμβάνεται το περιβάλλον του, να σκέφτεται και να αναλαμβάνει δράσεις για την επίτευξη συγκεκριμένων στόχων αυτόνομα.

## Key Concepts

- Αυτονομία
- Χρήση εργαλείων
- Σχεδιασμός
- Αντανακλαστικός βρόχος

## Use Cases

- Αυτόματοι βοηθοί έρευνας
- Bots αυτοματισμένης κωδικοποίησης
- Έλεγχοι έξυπνων σπιτιών

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Μοντέλο Γλώσσας Μεγάλης Κλίμακας)](/en/terms/llm-μοντέλο-γλώσσας-μεγάλης-κλίμακας/)
- [Orchestration (Ορχήστρωση)](/en/terms/orchestration-ορχήστρωση/)
- [Tool Calling (Κλήση Εργαλείου)](/en/terms/tool-calling-κλήση-εργαλείου/)
- [ReAct (Αντίδραση & Δράση)](/en/terms/react-αντίδραση-δράση/)
