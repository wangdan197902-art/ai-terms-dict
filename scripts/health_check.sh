#!/bin/bash
# 健康检查脚本
# 检查工具链、镜像源、Python环境、环境变量、内容数据、服务状态

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "=========================================="
echo "健康检查 - $(date)"
echo "=========================================="

# 1. 工具链检查
echo ""
echo "[1/6] 工具链检查..."
TOOLS=("hugo" "pagefind" "python3" "node" "npm" "git")
for tool in "${TOOLS[@]}"; do
    if command -v $tool >/dev/null 2>&1; then
        version=$($tool --version 2>&1 | head -1)
        echo "  ✓ $tool: $version"
    else
        echo "  ✗ $tool: 未安装"
    fi
done

# 2. Python环境检查
echo ""
echo "[2/6] Python环境检查..."
if [ -d ".venv" ]; then
    echo "  ✓ .venv 目录存在"
    if [ -f ".venv/bin/activate" ]; then
        echo "  ✓ activate 脚本存在"
    fi
else
    echo "  ✗ .venv 目录不存在，请运行 make init"
fi

# 3. 环境变量检查
echo ""
echo "[3/6] 环境变量检查..."
if [ -f ".env.local" ]; then
    echo "  ✓ .env.local 存在"
    if grep -q "AGNES_LLM_API_KEY" .env.local; then
        echo "  ✓ AGNES_LLM_API_KEY 已配置"
    else
        echo "  ✗ AGNES_LLM_API_KEY 未配置"
    fi
else
    echo "  ✗ .env.local 不存在"
fi

# 4. 内容数据检查
echo ""
echo "[4/6] 内容数据检查..."
if [ -f "data/seeds/seed_terms.json" ]; then
    count=$(python3 -c "import json; print(len(json.load(open('data/seeds/seed_terms.json'))))")
    echo "  ✓ 种子术语: $count 条"
else
    echo "  ✗ 种子术语文件不存在"
fi

if [ -f "data/queue/pending_terms.json" ]; then
    echo "  ✓ 队列文件存在"
else
    echo "  ⚠ 队列文件不存在，请运行 python3 scripts/fetch_terms_local.py"
fi

# 5. Hugo配置检查
echo ""
echo "[5/6] Hugo配置检查..."
for config_file in hugo.toml languages.toml params.toml; do
    if [ -f "config/_default/$config_file" ]; then
        echo "  ✓ config/_default/$config_file"
    else
        echo "  ✗ config/_default/$config_file 不存在"
    fi
done

# 6. 服务状态检查
echo ""
echo "[6/6] 服务状态检查..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost:1313/ | grep -q "200"; then
    echo "  ✓ Hugo服务运行中 (http://localhost:1313/)"
else
    echo "  ⚠ Hugo服务未运行 (运行 make serve 启动)"
fi

echo ""
echo "=========================================="
echo "健康检查完成"
echo "=========================================="
