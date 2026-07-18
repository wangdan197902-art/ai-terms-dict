#!/usr/bin/env python3
"""24语种LLM翻译能力深度测试 v2.0

测试方法：
- 5个代表性术语样本（覆盖5个category）
- 24个目标语种（除英文外的所有扩展语种）
- 每术语每语种单独调用API（共5×24=120次）
- 串行执行+间隔2秒（避免429）
- 检查字段完整性、字段长度、响应时间、翻译质量

输出：
- data/quality_tests/24lang_test_v2_{timestamp}.json
- 控制台进度
"""
import sys
import json
import time
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.utils.agnes_client import get_client
from scripts.translate_batch import build_batch_translate_messages


# 测试样本：5个代表性术语（覆盖5个category）
SAMPLE_TERM_IDS = [
    "few_shot_prompting",   # application_paradigms
    "governance",           # ethics_safety
    "stit_logic",           # engineering_practice
    "few_shot",             # basic_concepts
    "robot_learning",       # training_techniques
]

# 24个扩展语种（不含6个核心语种en/zh/es/de/ja/fr）
TEST_LANGS = [
    "pt", "ru", "ko", "ar", "hi", "it", "nl", "pl", "tr", "vi",
    "th", "id", "uk", "sv", "cs", "da", "fi", "no", "he",
    "ro", "hu", "el", "bg", "hr",
]

REQUIRED_FIELDS = [
    "term_name", "definition_short", "definition_long",
    "key_concepts", "use_cases", "related_terms",
]

OUTPUT_DIR = config.paths.progress_dir.parent.parent / "quality_tests"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_sample_terms() -> list:
    """加载测试样本术语。"""
    with open(config.paths.generated_definitions_file, "r", encoding="utf-8") as f:
        all_defs = json.load(f)
    samples = [d for d in all_defs if d["term_id"] in SAMPLE_TERM_IDS]
    # 按SAMPLE_TERM_IDS顺序排序
    samples.sort(key=lambda x: SAMPLE_TERM_IDS.index(x["term_id"]))
    print(f"已加载 {len(samples)}/{len(SAMPLE_TERM_IDS)} 个样本术语")
    for s in samples:
        print(f"  - {s['term_id']}: {s.get('english', '')} ({s.get('category', '')})")
    return samples


def evaluate_translation(trans: dict, source_def: dict) -> dict:
    """评估单次翻译质量。"""
    evaluation = {
        "field_complete": True,
        "missing_fields": [],
        "field_lengths": {},
        "quality_issues": [],
    }

    # 1. 字段完整性检查
    for field in REQUIRED_FIELDS:
        val = trans.get(field)
        if not val or (isinstance(val, list) and len(val) == 0):
            evaluation["field_complete"] = False
            evaluation["missing_fields"].append(field)
        else:
            if isinstance(val, str):
                evaluation["field_lengths"][field] = len(val)
            elif isinstance(val, list):
                evaluation["field_lengths"][field] = sum(len(str(x)) for x in val)

    # 2. 字段长度合理性（与原文对比）
    src_short = source_def.get("definition_short", "")
    src_long = source_def.get("definition_long", "")
    if trans.get("definition_short"):
        ratio = len(trans["definition_short"]) / max(len(src_short), 1)
        if ratio < 0.3:
            evaluation["quality_issues"].append(f"def_short过短 ratio={ratio:.2f}")
        elif ratio > 3.0:
            evaluation["quality_issues"].append(f"def_short过长 ratio={ratio:.2f}")
    if trans.get("definition_long"):
        ratio = len(trans["definition_long"]) / max(len(src_long), 1)
        if ratio < 0.3:
            evaluation["quality_issues"].append(f"def_long过短 ratio={ratio:.2f}")
        elif ratio > 3.0:
            evaluation["quality_issues"].append(f"def_long过长 ratio={ratio:.2f}")

    # 3. term_name是否本地化（不应等于英文）
    en_name = source_def.get("english", "")
    trans_name = trans.get("term_name", "")
    if trans_name == en_name and en_name:
        # 某些技术术语保留英文是合理的（如LLM），但多数应本地化
        if not any(x in en_name.lower() for x in ["llm", "rag", "gpt", "ai", "ml"]):
            evaluation["quality_issues"].append("term_name未本地化")

    # 4. related_terms应保留英文缩写（如果有）
    if trans.get("related_terms") and isinstance(trans["related_terms"], list):
        for rt in trans["related_terms"]:
            if isinstance(rt, str) and len(rt) > 100:
                evaluation["quality_issues"].append(f"related_term过长: {rt[:50]}...")

    return evaluation


def grade_result(evaluation: dict, response_time: float) -> str:
    """根据评估结果打分。"""
    if not evaluation["field_complete"]:
        return "C-不完整"
    if evaluation["quality_issues"]:
        if len(evaluation["quality_issues"]) >= 2:
            return "B-合格"
        return "B-合格"
    if response_time > 30:
        return "A-优秀(慢)"
    return "A-优秀"


def main():
    print("=" * 70)
    print("24语种LLM翻译能力深度测试 v2.0")
    print(f"  测试样本: {len(SAMPLE_TERM_IDS)} 个术语")
    print(f"  测试语种: {len(TEST_LANGS)} 个")
    print(f"  预计调用: {len(SAMPLE_TERM_IDS) * len(TEST_LANGS)} 次")
    print(f"  模型: {config.agnes.model}")
    print("=" * 70)

    samples = load_sample_terms()
    if len(samples) != len(SAMPLE_TERM_IDS):
        print("⚠ 样本加载不完整，终止测试")
        return 1

    client = get_client()
    results = {
        "test_info": {
            "test_time": datetime.utcnow().isoformat() + "Z",
            "model": config.agnes.model,
            "sample_term_ids": SAMPLE_TERM_IDS,
            "test_langs": TEST_LANGS,
            "total_calls": len(SAMPLE_TERM_IDS) * len(TEST_LANGS),
        },
        "summary": {},
        "lang_results": {},
        "raw_results": [],
    }

    total_calls = 0
    successful_calls = 0
    complete_field_calls = 0
    grade_a = 0
    grade_b = 0
    grade_c = 0
    total_response_time = 0
    start_time = time.time()

    # 串行：每术语 × 每语种
    for sample in samples:
        term_id = sample["term_id"]
        print(f"\n{'='*70}")
        print(f"测试术语: {term_id} ({sample.get('english', '')})")
        print(f"{'='*70}")

        for lang in TEST_LANGS:
            total_calls += 1
            print(f"  [{total_calls}/{results['test_info']['total_calls']}] {term_id} → {lang} ...", end="", flush=True)

            attempt_result = {
                "term_id": term_id,
                "lang": lang,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "api_success": False,
                "field_complete": False,
                "grade": "F-失败",
                "response_time": 0,
                "missing_fields": [],
                "quality_issues": [],
                "field_lengths": {},
                "translation": None,
            }

            try:
                t0 = time.time()
                messages = build_batch_translate_messages([sample], lang)
                result = client.chat_json(messages, temperature=0.3)
                elapsed = time.time() - t0

                attempt_result["response_time"] = round(elapsed, 2)
                total_response_time += elapsed

                if "translations" in result and len(result["translations"]) > 0:
                    trans = result["translations"][0]
                    trans["term_id"] = term_id
                    attempt_result["api_success"] = True
                    attempt_result["translation"] = {
                        "term_name": trans.get("term_name", ""),
                        "definition_short": trans.get("definition_short", "")[:200],
                        "definition_long": trans.get("definition_long", "")[:300],
                        "key_concepts": trans.get("key_concepts", []),
                        "use_cases": trans.get("use_cases", []),
                        "related_terms": trans.get("related_terms", []),
                    }

                    evaluation = evaluate_translation(trans, sample)
                    attempt_result["field_complete"] = evaluation["field_complete"]
                    attempt_result["missing_fields"] = evaluation["missing_fields"]
                    attempt_result["quality_issues"] = evaluation["quality_issues"]
                    attempt_result["field_lengths"] = evaluation["field_lengths"]
                    attempt_result["grade"] = grade_result(evaluation, elapsed)

                    successful_calls += 1
                    if evaluation["field_complete"]:
                        complete_field_calls += 1
                    if attempt_result["grade"].startswith("A"):
                        grade_a += 1
                    elif attempt_result["grade"].startswith("B"):
                        grade_b += 1
                    elif attempt_result["grade"].startswith("C"):
                        grade_c += 1

                    print(f" {attempt_result['grade']} ({elapsed:.1f}s)")
                else:
                    print(f" ✗ 响应格式异常 ({elapsed:.1f}s)")
                    attempt_result["quality_issues"] = ["响应格式异常：缺少translations字段"]

            except Exception as e:
                elapsed = time.time() - t0
                attempt_result["response_time"] = round(elapsed, 2)
                attempt_result["quality_issues"] = [f"API异常: {str(e)[:200]}"]
                print(f" ✗ 异常: {str(e)[:80]}")

            results["raw_results"].append(attempt_result)

            # 按语种聚合
            if lang not in results["lang_results"]:
                results["lang_results"][lang] = {
                    "total": 0, "success": 0, "complete": 0,
                    "grades": {"A": 0, "B": 0, "C": 0, "F": 0},
                    "total_time": 0, "issues": [],
                }
            lr = results["lang_results"][lang]
            lr["total"] += 1
            lr["total_time"] += attempt_result["response_time"]
            if attempt_result["api_success"]:
                lr["success"] += 1
            if attempt_result["field_complete"]:
                lr["complete"] += 1
            if attempt_result["grade"]:
                grade_key = attempt_result["grade"][0]
                if grade_key in lr["grades"]:
                    lr["grades"][grade_key] += 1
            if attempt_result["quality_issues"]:
                lr["issues"].extend(attempt_result["quality_issues"])

            # 间隔2秒避免触发429
            time.sleep(2)

    total_elapsed = time.time() - start_time

    # 汇总
    results["summary"] = {
        "total_calls": total_calls,
        "successful_calls": successful_calls,
        "complete_field_calls": complete_field_calls,
        "grade_a": grade_a,
        "grade_b": grade_b,
        "grade_c": grade_c,
        "grade_f": total_calls - successful_calls,
        "success_rate": round(successful_calls / total_calls * 100, 1),
        "complete_rate": round(complete_field_calls / total_calls * 100, 1),
        "total_elapsed_sec": round(total_elapsed, 1),
        "avg_response_sec": round(total_response_time / max(successful_calls, 1), 2),
    }

    # 输出
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"24lang_test_v2_{timestamp}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # 打印汇总
    print("\n" + "=" * 70)
    print("测试汇总")
    print("=" * 70)
    print(f"  总调用数: {total_calls}")
    print(f"  API成功: {successful_calls}/{total_calls} ({results['summary']['success_rate']}%)")
    print(f"  字段完整: {complete_field_calls}/{total_calls} ({results['summary']['complete_rate']}%)")
    print(f"  A-优秀: {grade_a}")
    print(f"  B-合格: {grade_b}")
    print(f"  C-不完整: {grade_c}")
    print(f"  F-失败: {total_calls - successful_calls}")
    print(f"  总耗时: {total_elapsed:.1f}s ({total_elapsed/60:.1f}分钟)")
    print(f"  平均响应: {results['summary']['avg_response_sec']}s")
    print(f"\n按语种汇总:")
    print(f"  {'lang':4s} | {'success':8s} | {'complete':8s} | {'A':3s} {'B':3s} {'C':3s} {'F':3s} | {'avg_time':8s} | issues")
    for lang in TEST_LANGS:
        lr = results["lang_results"].get(lang, {})
        avg_t = lr.get("total_time", 0) / max(lr.get("total", 1), 1)
        print(f"  {lang:4s} | {lr.get('success',0):3d}/{lr.get('total',0):3d}   | {lr.get('complete',0):3d}/{lr.get('total',0):3d}   | "
              f"{lr.get('grades',{}).get('A',0):3d} {lr.get('grades',{}).get('B',0):3d} {lr.get('grades',{}).get('C',0):3d} {lr.get('grades',{}).get('F',0):3d} | "
              f"{avg_t:6.2f}s  | {len(lr.get('issues',[]))}条")

    print(f"\n✓ 结果保存: {output_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
