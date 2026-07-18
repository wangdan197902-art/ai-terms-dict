#!/usr/bin/env python3
"""定义生成Prompt。"""

SYSTEM_PROMPT = """You are an AI terminology expert specializing in Large Language Models, machine learning, and AI engineering. Your task is to generate comprehensive, accurate, and educational definitions for AI terms.

Requirements:
1. Definitions must be technically accurate and up-to-date
2. Target audience: developers, researchers, students learning AI
3. Provide both short (1 sentence) and long (100-200 words) definitions
4. Include 3-5 key concepts, 2-4 use cases, 3-5 related terms
5. Assign difficulty 1-5 (1=beginner, 5=expert)
6. Include relevant tags
7. If applicable, provide a code example
8. Respond ONLY in valid JSON format, no markdown, no explanation outside JSON"""

USER_TEMPLATE = """Generate a comprehensive definition for the AI term: "{term}"

Output JSON with EXACTLY these fields:
{{
  "term_id": "{term_id}",
  "english": "{term}",
  "category": "{category}",
  "subcategory": "",
  "definition_short": "one clear sentence summary (max 200 chars)",
  "definition_long": "detailed explanation 100-200 words covering what it is, why it matters, how it works",
  "key_concepts": ["concept1", "concept2", "concept3"],
  "use_cases": ["use case 1", "use case 2"],
  "related_terms": ["term1", "term2"],
  "code_example": "optional Python code example or null",
  "difficulty": 3,
  "tags": ["tag1", "tag2"]
}}

Remember: Respond ONLY with valid JSON, no markdown fences, no explanation."""


def build_messages(term_id: str, term: str, category: str) -> list:
    """构建定义生成的messages。"""
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_TEMPLATE.format(
            term=term, term_id=term_id, category=category
        )},
    ]
