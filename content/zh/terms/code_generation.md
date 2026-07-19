---
title: "代码生成"
term_id: "code_generation"
category: "application_paradigms"
subcategory: ""
tags: ["development", "automation", "programming"]
difficulty: 3
weight: 1
slug: "code_generation"
date: "2026-07-18T07:44:21.592227Z"
lastmod: "2026-07-18T11:44:44.591131Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "利用人工智能根据自然语言描述或现有代码片段自动创建源代码的过程。"
---
## Definition

代码生成利用在海量编程语言存储库上训练的大型语言模型，来生成可运行的软件工件。它解析人类可读的提示（如注释或自然语言指令），从而自动生成相应的功能代码。

### Summary

利用人工智能根据自然语言描述或现有代码片段自动创建源代码的过程。

## Key Concepts

- 自然语言处理
- 源代码合成
- 大型语言模型
- 自动化重构

## Use Cases

- 自动化样板代码的创建
- 将伪代码转换为可执行脚本
- 协助开发者进行调试和优化

## Code Example

```python
import openai
# Example prompt for generating a function
def generate_sort_function():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Write a Python function to sort a list of integers."}]
    )
    return response.choices[0].message.content
```

## Related Terms

- [LLM (大型语言模型)](/en/terms/llm-大型语言模型/)
- [IDE Integration (集成开发环境集成)](/en/terms/ide-integration-集成开发环境集成/)
- [Program Synthesis (程序综合)](/en/terms/program-synthesis-程序综合/)
- [Copilot (智能编码助手)](/en/terms/copilot-智能编码助手/)
