#!/usr/bin/env python3
"""翻译Prompt。"""

SYSTEM_PROMPT = """You are a professional technical translator specializing in AI/ML content. You translate AI terminology accurately while preserving technical precision.

Rules:
1. Translate term_name, definition_short, definition_long, key_concepts, use_cases
2. DO NOT translate: term_id, code_example, related_terms (keep English, add native explanation in parentheses if helpful)
3. Use natural, native-speaker phrasing for each language
4. Maintain technical accuracy - use established AI terminology in each language
5. For languages without established AI terms, use transliteration + English in parentheses
6. Respond ONLY in valid JSON format"""

USER_TEMPLATE = """Translate the following AI term definition to {target_language} ({target_lang_code}).

Source (English):
{definition_json}

Output JSON with EXACTLY these fields:
{{
  "term_id": "{term_id}",
  "language": "{target_lang_code}",
  "term_name": "translated term name",
  "definition_short": "translated short definition",
  "definition_long": "translated long definition",
  "key_concepts": ["translated concept 1", "translated concept 2"],
  "use_cases": ["translated use case 1", "translated use case 2"],
  "related_terms": ["english_term_1 (native_explanation)", "english_term_2"],
  "code_example": null,
  "source_language": "en",
  "target_language": "{target_lang_code}"
}}

Remember: Respond ONLY with valid JSON."""


LANGUAGE_NAMES = {
    "es": "Spanish",
    "de": "German",
    "ja": "Japanese",
    "fr": "French",
    "zh": "Chinese (Simplified)",
}


def build_messages(definition: dict, target_lang: str) -> list:
    """构建翻译messages。"""
    import json
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_TEMPLATE.format(
            target_language=LANGUAGE_NAMES[target_lang],
            target_lang_code=target_lang,
            definition_json=json.dumps(definition, ensure_ascii=False, indent=2),
            term_id=definition["term_id"],
        )},
    ]
