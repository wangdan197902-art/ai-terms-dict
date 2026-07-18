---
title: "Webhook"
term_id: "webhook"
category: "engineering_practice"
subcategory: ""
tags: ["Integration", "APIs", "Automation"]
difficulty: 3
weight: 1
slug: "webhook"
aliases:
  - /en/terms/webhook/
date: "2026-07-18T10:19:55.510021Z"
lastmod: "2026-07-18T11:44:44.732883Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A user-defined HTTP callback triggered by specific events, allowing systems to push real-time notifications to other applications."
---

## Definition

A webhook is a mechanism for one service to provide real-time information to another service when an event occurs. Instead of polling for changes, the source system sends an HTTP POST request to a specified URL with payload data describing the event. This approach reduces server load and ensures immediate reaction to events, making it essential for integrating disparate software systems, automating workflows, and synchronizing data across platforms like GitHub, Stripe, or Slack.

### Summary

A user-defined HTTP callback triggered by specific events, allowing systems to push real-time notifications to other applications.

## Key Concepts

- Event-driven
- HTTP POST
- Callback URL
- Push notification

## Use Cases

- Automated CI/CD deployments
- Payment gateway notifications
- Slack bot integrations

## Related Terms

- [API](/en/terms/api/)
- [Event-driven architecture](/en/terms/event-driven-architecture/)
- [REST](/en/terms/rest/)
- [Integration](/en/terms/integration/)
