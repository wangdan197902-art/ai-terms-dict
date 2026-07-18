---
title: "on-policy"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
aliases:
  - /id/terms/on_policy/
date: "2026-07-18T15:32:19.697066Z"
lastmod: "2026-07-18T16:38:07.409527Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Pendekatan pembelajaran penguatan di mana kebijakan yang dievaluasi dan ditingkatkan adalah sama dengan kebijakan yang digunakan untuk menghasilkan data."
---

## Definition

Algoritma on-policy mengharuskan agen belajar secara langsung dari tindakan yang diambil oleh kebijakannya saat ini. Ini berarti data yang dikumpulkan selama eksplorasi digunakan segera untuk memperbarui kebijakan, memastikan konsistensi distribusi data.

### Summary

Pendekatan pembelajaran penguatan di mana kebijakan yang dievaluasi dan ditingkatkan adalah sama dengan kebijakan yang digunakan untuk menghasilkan data.

## Key Concepts

- pembelajaran penguatan
- gradien kebijakan
- konsistensi data
- efisiensi sampel

## Use Cases

- Kontrol robotika dengan batasan keamanan
- Agen permainan yang memerlukan pembaruan presisi
- Sistem adaptif waktu nyata

## Related Terms

- [off-policy (di luar kebijakan)](/en/terms/off-policy-di-luar-kebijakan/)
- [REINFORCE (algoritma gradien kebijakan)](/en/terms/reinforce-algoritma-gradien-kebijakan/)
- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [actor-critic (aktor-kritikus)](/en/terms/actor-critic-aktor-kritikus/)
