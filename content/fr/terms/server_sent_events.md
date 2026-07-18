---
title: "Événements envoyés par le serveur"
term_id: "server_sent_events"
category: "engineering_practice"
subcategory: ""
tags: ["Web Development", "Real-time", "API Design"]
difficulty: 2
weight: 1
slug: "server_sent_events"
aliases:
  - /fr/terms/server_sent_events/
date: "2026-07-18T11:37:32.319181Z"
lastmod: "2026-07-18T11:44:45.326938Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un protocole standard permettant aux serveurs web de pousser des mises à jour en temps réel vers les clients via une seule connexion HTTP."
---

## Definition

Les événements envoyés par le serveur (SSE) permettent une communication unidirectionnelle du serveur vers le client, où le serveur peut diffuser des données en continu sans que le client ait besoin d'interroger régulièrement le serveur. Il utilise du HTTP standard, ce qui le rend simple à implémenter.

### Summary

Un protocole standard permettant aux serveurs web de pousser des mises à jour en temps réel vers les clients via une seule connexion HTTP.

## Key Concepts

- Flux d'événements
- Communication unidirectionnelle
- Reconnexion automatique
- Basé sur HTTP

## Use Cases

- Flux de cours boursiers en direct
- Notifications en temps réel
- Mises à jour de suivi de progression

## Related Terms

- [WebSockets (Communication bidirectionnelle)](/en/terms/websockets-communication-bidirectionnelle/)
- [Long Polling (Interrogation longue)](/en/terms/long-polling-interrogation-longue/)
- [Streaming API (API de streaming)](/en/terms/streaming-api-api-de-streaming/)
- [EventSource (Interface JavaScript SSE)](/en/terms/eventsource-interface-javascript-sse/)
