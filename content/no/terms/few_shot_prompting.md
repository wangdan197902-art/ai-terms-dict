---
title: "Few-shot prompting"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /no/terms/few_shot_prompting/
date: "2026-07-18T15:36:58.944953Z"
lastmod: "2026-07-18T16:38:06.958432Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Few-shot prompting er en teknikk der store språkmodeller (LLMer) gis et lite antall input-output-eksempler i prompten for å veilede atferden deres."
---

## Definition

Denne metoden utnytter evnen til kontekstuell læring hos store språkmodeller ved å gi noen illustrative eksempler direkte i prompten. I motsetning til finjustering, som krever oppdatering av modellvektene, fungerer dette ved å gi modellen eksempler på hva som forventes av responsen.

### Summary

Few-shot prompting er en teknikk der store språkmodeller (LLMer) gis et lite antall input-output-eksempler i prompten for å veilede atferden deres.

## Key Concepts

- Kontekstuell læring
- Promptingeniørfag
- Eksempelbasert veiledning
- Sammenligning med null-skudd

## Use Cases

- Formatering av sentimentanalyse
- Tilpasning av kodestil
- Uttak av strukturerte data

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

- [zero_shot (null-skudd)](/en/terms/zero_shot-null-skudd/)
- [prompt_engineering (promptingeniørfag)](/en/terms/prompt_engineering-promptingeniørfag/)
- [in_context_learning (kontekstuell læring)](/en/terms/in_context_learning-kontekstuell-læring/)
- [llm (stor språkmodell)](/en/terms/llm-stor-språkmodell/)
