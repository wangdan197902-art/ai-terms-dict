---
title: "Agen"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /id/terms/agent/
date: "2026-07-18T15:22:20.474460Z"
lastmod: "2026-07-18T16:38:07.386230Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Sistem AI yang mampu memahami lingkungannya, bernalar, dan mengambil tindakan untuk mencapai tujuan tertentu secara otonom."
---

## Definition

Dalam AI, agen adalah entitas yang bertindak atas nama pengguna atau sistem untuk menyelesaikan tugas. Berbeda dengan model pasif yang hanya merespons prompt, agen dapat merencanakan, menggunakan alat, dan melakukan iterasi pada tindakannya.

### Summary

Sistem AI yang mampu memahami lingkungannya, bernalar, dan mengambil tindakan untuk mencapai tujuan tertentu secara otonom.

## Key Concepts

- Otonomi
- Penggunaan alat
- Perencanaan
- Loop reaktif

## Use Cases

- Asisten riset otomatis
- Bot pemrograman mandiri
- Pengontrol rumah pintar

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Large Language Model / Model Bahasa Besar)](/en/terms/llm-large-language-model-model-bahasa-besar/)
- [Orchestration (Orkestrasi)](/en/terms/orchestration-orkestrasi/)
- [Tool Calling (Pemanggilan Alat)](/en/terms/tool-calling-pemanggilan-alat/)
- [ReAct (Reasoning and Acting / Bernalar dan Bertindak)](/en/terms/react-reasoning-and-acting-bernalar-dan-bertindak/)
