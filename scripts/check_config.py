#!/usr/bin/env python3
"""配置检查脚本。

检查所有环境变量、路径、依赖是否就绪。
"""
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config


def check_env_vars() -> bool:
    """检查环境变量。"""
    print("\n[1/5] 检查环境变量...")
    required = [
        ("AGNES_LLM_API_KEY", config.agnes.api_key),
        ("AGNES_LLM_BASE_URL", config.agnes.base_url),
        ("AGNES_LLM_MODEL", config.agnes.model),
    ]
    all_ok = True
    for name, value in required:
        if value:
            masked = value[:10] + "..." + value[-4:] if len(value) > 14 else "***"
            print(f"  ✓ {name} = {masked}")
        else:
            print(f"  ✗ {name} 未设置")
            all_ok = False
    return all_ok


def check_paths() -> bool:
    """检查路径。"""
    print("\n[2/5] 检查路径...")
    paths = [
        ("PROJECT_ROOT", config.paths.project_root),
        ("seeds_dir", config.paths.seeds_dir),
        ("queue_dir", config.paths.queue_dir),
        ("mock_dir", config.paths.mock_dir),
        ("golden_samples_dir", config.paths.golden_samples_dir),
        ("translations_dir", config.paths.translations_dir),
        ("progress_dir", config.paths.progress_dir),
        ("cache_dir", config.paths.cache_dir),
    ]
    all_ok = True
    for name, path in paths:
        exists = path.exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {name}: {path}")
        if not exists:
            all_ok = False
    return all_ok


def check_data_files() -> bool:
    """检查数据文件。"""
    print("\n[3/5] 检查数据文件...")
    files = [
        ("seed_file", config.paths.seed_file),
        ("pending_terms_file", config.paths.pending_terms_file),
    ]
    all_ok = True
    for name, path in files:
        exists = path.exists()
        status = "✓" if exists else "✗"
        size = path.stat().st_size if exists else 0
        print(f"  {status} {name}: {path} ({size} bytes)")
        if not exists:
            all_ok = False
    return all_ok


def check_hugo_config() -> bool:
    """检查Hugo配置。"""
    print("\n[4/5] 检查Hugo配置...")
    hugo_files = [
        config.hugo.config_dir / "_default" / "hugo.toml",
        config.hugo.config_dir / "_default" / "languages.toml",
        config.hugo.config_dir / "_default" / "params.toml",
    ]
    all_ok = True
    for path in hugo_files:
        exists = path.exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {path}")
        if not exists:
            all_ok = False
    return all_ok


def check_python_deps() -> bool:
    """检查Python依赖。"""
    print("\n[5/5] 检查Python依赖...")
    deps = ["openai", "requests", "dotenv", "yaml", "jsonschema"]
    all_ok = True
    for dep in deps:
        try:
            __import__(dep)
            print(f"  ✓ {dep}")
        except ImportError:
            print(f"  ✗ {dep} 未安装")
            all_ok = False
    return all_ok


def main():
    print("=" * 60)
    print("配置检查")
    print("=" * 60)
    config.print_summary()

    checks = [
        ("环境变量", check_env_vars()),
        ("路径", check_paths()),
        ("数据文件", check_data_files()),
        ("Hugo配置", check_hugo_config()),
        ("Python依赖", check_python_deps()),
    ]

    print("\n" + "=" * 60)
    print("检查结果汇总")
    print("=" * 60)
    all_pass = True
    for name, result in checks:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status} - {name}")
        if not result:
            all_pass = False

    if all_pass:
        print("\n✓ 所有检查通过")
        return 0
    else:
        print("\n✗ 存在检查失败项，请修复后再继续")
        return 1


if __name__ == "__main__":
    sys.exit(main())
