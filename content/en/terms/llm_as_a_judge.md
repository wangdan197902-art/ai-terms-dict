---
title: "LLM-as-a-Judge"
term_id: "llm_as_a_judge"
category: "application_paradigms"
subcategory: ""
tags: ["evaluation", "llm_application", "nlp"]
difficulty: 3
weight: 1
slug: "llm_as_a_judge"
aliases:
  - /en/terms/llm_as_a_judge/
date: "2026-07-18T10:04:10.298057Z"
lastmod: "2026-07-18T11:44:44.690421Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A method for evaluating Large Language Model outputs by using another LLM to score or rank responses against criteria."
---

## Definition

LLM-as-a-Judge is an evaluation paradigm where a Large Language Model serves as an automated evaluator for the quality of outputs from other models. Instead of relying solely on human annotators or rigid metrics like BLEU scores, a 'judge' LLM is prompted to assess responses based on specific criteria such as helpfulness, correctness, or safety. This approach scales evaluation efforts significantly and captures nuanced qualitative aspects of language generation, though it requires careful prompt engineering to mitigate biases inherent in the judge model itself.

### Summary

A method for evaluating Large Language Model outputs by using another LLM to score or rank responses against criteria.

## Key Concepts

- Automated Evaluation
- Prompt Engineering
- Model Alignment
- Quality Metrics

## Use Cases

- Benchmarking RLHF models
- Evaluating creative writing
- Safety and bias detection

## Related Terms

- [rlhf](/en/terms/rlhf/)
- [evaluation_metrics](/en/terms/evaluation_metrics/)
- [prompt_engineering](/en/terms/prompt_engineering/)
- [model_alignment](/en/terms/model_alignment/)
