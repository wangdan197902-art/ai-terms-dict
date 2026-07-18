---
title: "Ajan"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /tr/terms/agent/
date: "2026-07-18T15:22:18.226331Z"
lastmod: "2026-07-18T16:38:07.224179Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Çevresini algılayabilen, akıl yürütebilen ve belirli hedeflere ulaşmak için eylemler alabilen otonom bir yapay zeka sistemi."
---

## Definition

Yapay zekada bir ajan, kullanıcı veya sistem adına görevleri tamamlamak için hareket eden bir varlıktır. Sadece prompt'lara yanıt veren pasif modellerin aksine, ajanlar planlama yapabilir, araç kullanabilir ve eylemlerini tekrarlayabilir.

### Summary

Çevresini algılayabilen, akıl yürütebilen ve belirli hedeflere ulaşmak için eylemler alabilen otonom bir yapay zeka sistemi.

## Key Concepts

- Özerklik
- Araç kullanımı
- Planlama
- Reaktif döngü

## Use Cases

- Otomatik araştırma asistanları
- Kendiliğinden kod yazan botlar
- Akıllı ev kontrol sistemleri

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (Büyük Dil Modeli)](/en/terms/llm-büyük-dil-modeli/)
- [Orchestration (Orkestrasyon)](/en/terms/orchestration-orkestrasyon/)
- [Tool Calling (Araç Çağırma)](/en/terms/tool-calling-araç-çağırma/)
- [ReAct (Reasoning + Acting / Akıl Yürütme + Eylem)](/en/terms/react-reasoning-acting-akıl-yürütme-eylem/)
