---
title: "API"
term_id: "api"
category: "engineering_practice"
subcategory: ""
tags: ["Development", "Integration", "Infrastructure"]
difficulty: 1
weight: 1
slug: "api"
date: "2026-07-18T15:22:09.621552Z"
lastmod: "2026-07-18T17:15:09.343226Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Ohjelmointirajapinta, jonka avulla eri ohjelmistojärjestelmät voivat kommunikoida ja vaihtaa dataa."
---
## Definition

API määrittelee joukon protokollia ja työkaluja ohjelmistojen ja sovellusten rakentamiseen. Tekoälyn alalla API:t mahdollistavat kehittäjille pääsyn tehokkaisiin malleihin, kuten suuriin kielimalleihin tai kuvageneraattoreihin, ilman paikallista isännöintiä.

### Summary

Ohjelmointirajapinta, jonka avulla eri ohjelmistojärjestelmät voivat kommunikoida ja vaihtaa dataa.

## Key Concepts

- Päätepisteet
- REST
- Todennus
- Payloadda

## Use Cases

- Chatbotien integrointi verkkosivustoille
- Pilvipohjaisten koneoppimismallien käyttö
- Datanhaku tekoälypalveluista

## Code Example

```python
import requests
response = requests.get('https://api.ai.com/v1/generate', headers={'Authorization': 'Bearer token'})
```

## Related Terms

- [REST](/en/terms/rest/)
- [SDK (Kehitysympäristöpaketti)](/en/terms/sdk-kehitysympäristöpaketti/)
- [Webhook](/en/terms/webhook/)
- [Integration (Integraatio)](/en/terms/integration-integraatio/)
