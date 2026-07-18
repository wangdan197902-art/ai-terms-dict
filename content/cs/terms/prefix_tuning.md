---
title: "Prefix Tuning"
term_id: "prefix_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers"]
difficulty: 4
weight: 1
slug: "prefix_tuning"
aliases:
  - /cs/terms/prefix_tuning/
date: "2026-07-18T16:13:09.337296Z"
lastmod: "2026-07-18T17:15:09.190516Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Metoda efektivního doladění parametrů, která přidatelné spojité vektory na vstup vrstev transformátoru."
---

## Definition

Prefix Tuning je technika adaptace s nízkou spotřebou parametrů pro předtrénované transformátory. Místo aktualizace všech vah modelu se před vstup do každé vrstvy transformátoru přidává posloupnost trainovatelných spojitých vektorů (prefix). To umožňuje přizpůsobit model novým úkolům bez nutnosti přetrénovat celý model.

### Summary

Metoda efektivního doladění parametrů, která přidatelné spojité vektory na vstup vrstev transformátoru.

## Key Concepts

- Efektivní ladění parametrů
- Měkké podněty (Soft prompts)
- Vrstvy transformátoru
- Zmrazená kostra (Frozen backbone)

## Use Cases

- Adaptace pro učení s malým množstvím dat
- Vícenásobné učení s omezenými zdroji
- Přizpůsobování LLM pro specializované domény

## Related Terms

- [prompt_tuning (ladění podnětů)](/en/terms/prompt_tuning-ladění-podnětů/)
- [p_tuning (parametrické ladění)](/en/terms/p_tuning-parametrické-ladění/)
- [adapter_modules (adaptérní moduly)](/en/terms/adapter_modules-adaptérní-moduly/)
- [peft (techniky efektivního doladění)](/en/terms/peft-techniky-efektivního-doladění/)
