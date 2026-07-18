#!/usr/bin/env python3
"""数据Schema校验与质量检测。

校验 generated_definitions.json 和 translated_terms.json 是否符合Schema。
"""
import sys
import json
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False
    print("⚠ jsonschema未安装，跳过Schema校验，仅做基础检查")


def load_schema() -> dict:
    """加载JSON Schema。"""
    schema_file = Path(__file__).parent.parent / "schemas" / "term_schema.json"
    with open(schema_file, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_definition(defn: dict, schema: dict) -> list:
    """校验单个定义，返回错误列表。"""
    errors = []
    if HAS_JSONSCHEMA:
        try:
            jsonschema.validate(defn, schema)
        except jsonschema.ValidationError as e:
            errors.append(f"Schema: {e.message} at {list(e.path)}")

    # 基础校验
    required = ["term_id", "english", "category", "definition_short", "definition_long"]
    for field in required:
        if field not in defn or not defn[field]:
            errors.append(f"Missing required field: {field}")

    # 长度校验
    if len(defn.get("definition_short", "")) > 300:
        errors.append("definition_short exceeds 300 chars")
    if len(defn.get("definition_long", "")) < 50:
        errors.append("definition_long less than 50 chars")

    # 分类校验
    valid_categories = ["basic_concepts", "training_techniques", "application_paradigms", "engineering_practice", "ethics_safety"]
    if defn.get("category") not in valid_categories:
        errors.append(f"Invalid category: {defn.get('category')}")

    # 难度校验
    diff = defn.get("difficulty")
    if not isinstance(diff, int) or diff < 1 or diff > 5:
        errors.append(f"Invalid difficulty: {diff}")

    return errors


def validate_translations(translations: list) -> dict:
    """校验翻译数据。"""
    report = {
        "total": len(translations),
        "valid": 0,
        "errors": [],
        "by_language": defaultdict(int),
        "by_source": defaultdict(int),
        "completeness": {},
    }

    # 按term_id分组
    by_term = defaultdict(list)
    for t in translations:
        by_term[t["term_id"]].append(t["language"])
        report["by_language"][t["language"]] += 1
        report["by_source"][t.get("source", "unknown")] += 1

    # 完整性校验：每个术语应有6个语种
    expected_langs = {"en", "es", "de", "ja", "fr", "zh"}
    incomplete = []
    for term_id, langs in by_term.items():
        actual_langs = set(langs)
        if actual_langs != expected_langs:
            missing = expected_langs - actual_langs
            incomplete.append({"term_id": term_id, "missing": list(missing)})

    report["completeness"] = {
        "expected_langs": list(expected_langs),
        "total_terms": len(by_term),
        "complete_terms": len(by_term) - len(incomplete),
        "incomplete": incomplete[:10],  # 只显示前10个
    }

    # 逐条校验
    schema = load_schema() if HAS_JSONSCHEMA else {}
    for i, t in enumerate(translations):
        errors = validate_definition(t, schema)
        if errors:
            report["errors"].append({
                "index": i,
                "term_id": t.get("term_id", "unknown"),
                "language": t.get("language", "unknown"),
                "errors": errors,
            })
        else:
            report["valid"] += 1

    return report


def check_quality(definitions: list) -> dict:
    """质量检测：同质化、翻译一致性、术语覆盖度。"""
    quality = {
        "total_definitions": len(definitions),
        "category_distribution": Counter(d.get("category", "unknown") for d in definitions),
        "difficulty_distribution": Counter(d.get("difficulty", 0) for d in definitions),
        "avg_key_concepts": 0,
        "avg_use_cases": 0,
        "with_code_example": 0,
        "potential_duplicates": [],
    }

    total_kc = sum(len(d.get("key_concepts", [])) for d in definitions)
    total_uc = sum(len(d.get("use_cases", [])) for d in definitions)
    quality["avg_key_concepts"] = round(total_kc / len(definitions), 1) if definitions else 0
    quality["avg_use_cases"] = round(total_uc / len(definitions), 1) if definitions else 0
    quality["with_code_example"] = sum(1 for d in definitions if d.get("code_example"))

    # 检测同质化（短定义高度相似）
    short_defs = [(d["term_id"], d.get("definition_short", "")) for d in definitions]
    for i, (id1, s1) in enumerate(short_defs):
        for id2, s2 in short_defs[i+1:]:
            if s1 and s2:
                # 简单Jaccard相似度
                words1 = set(s1.lower().split())
                words2 = set(s2.lower().split())
                if words1 and words2:
                    sim = len(words1 & words2) / len(words1 | words2)
                    if sim > 0.7:
                        quality["potential_duplicates"].append({
                            "term1": id1, "term2": id2, "similarity": round(sim, 2)
                        })

    return quality


def main():
    print("=" * 60)
    print("Step 02-02: 数据Schema校验与质量检测")
    print("=" * 60)

    # 加载数据
    defs_file = config.paths.generated_definitions_file
    trans_file = config.paths.translated_terms_file

    print(f"\n[1] 校验定义文件: {defs_file}")
    with open(defs_file, "r", encoding="utf-8") as f:
        definitions = json.load(f)
    print(f"  定义数: {len(definitions)}")

    print(f"\n[2] 校验翻译文件: {trans_file}")
    with open(trans_file, "r", encoding="utf-8") as f:
        translations = json.load(f)
    print(f"  翻译数: {len(translations)}")

    # 校验定义
    print(f"\n[3] 定义Schema校验:")
    schema = load_schema() if HAS_JSONSCHEMA else {}
    def_errors = []
    for d in definitions:
        errors = validate_definition(d, schema)
        if errors:
            def_errors.append({"term_id": d.get("term_id"), "errors": errors})

    if def_errors:
        print(f"  ✗ {len(def_errors)} 条定义有错误:")
        for e in def_errors[:5]:
            print(f"    {e['term_id']}: {e['errors'][:2]}")
    else:
        print(f"  ✓ 全部 {len(definitions)} 条定义通过Schema校验")

    # 校验翻译
    print(f"\n[4] 翻译完整性校验:")
    trans_report = validate_translations(translations)
    print(f"  总数: {trans_report['total']}")
    print(f"  有效: {trans_report['valid']}")
    print(f"  语种分布: {dict(trans_report['by_language'])}")
    print(f"  来源分布: {dict(trans_report['by_source'])}")
    print(f"  完整性: {trans_report['completeness']['complete_terms']}/{trans_report['completeness']['total_terms']} 术语有完整6语种")

    if trans_report["errors"]:
        print(f"  ⚠ {len(trans_report['errors'])} 条翻译有错误")

    # 质量检测
    print(f"\n[5] 质量检测:")
    quality = check_quality(definitions)
    print(f"  分类分布: {dict(quality['category_distribution'])}")
    print(f"  难度分布: {dict(quality['difficulty_distribution'])}")
    print(f"  平均key_concepts: {quality['avg_key_concepts']}")
    print(f"  平均use_cases: {quality['avg_use_cases']}")
    print(f"  含代码示例: {quality['with_code_example']}/{quality['total_definitions']}")
    if quality["potential_duplicates"]:
        print(f"  ⚠ 潜在重复: {len(quality['potential_duplicates'])} 对")
        for dup in quality["potential_duplicates"][:3]:
            print(f"    {dup['term1']} vs {dup['term2']}: {dup['similarity']}")
    else:
        print(f"  ✓ 无高度同质化定义")

    # 生成报告
    report = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "definitions": {
            "total": len(definitions),
            "errors": len(def_errors),
            "error_details": def_errors[:10],
        },
        "translations": trans_report,
        "quality": quality,
    }

    report_file = config.paths.reports_dir / f"validation_report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    config.paths.reports_dir.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)
    print(f"\n✓ 校验报告: {report_file}")

    # 退出码
    has_p0 = len(def_errors) > 0 or len(trans_report["errors"]) > 0
    return 1 if has_p0 else 0


if __name__ == "__main__":
    sys.exit(main())
