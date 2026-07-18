#!/bin/bash
# 并行翻译20语种 - 每个语种1个进程
# 启动时间：2026-07-18

cd /Users/wangdan/Desktop/wangdan/想法/网站/01-小语种AI术语词典/aiterms-dictionary

# 20个语种
LANGS=(pt it nl ko sv he da no fi ru pl tr cs el ar id th vi ro hu)

# 创建日志目录
mkdir -p logs/parallel_translate

# 启动时间
echo "=== 并行翻译启动 ==="
echo "启动时间: $(date)"
echo "语种数量: ${#LANGS[@]}"
echo "并发数: ${#LANGS[@]}"
echo ""

# 启动20个并行进程
PIDS=()
for lang in "${LANGS[@]}"; do
    LOG_FILE="logs/parallel_translate/translate_${lang}_$(date +%Y%m%d_%H%M%S).log"
    echo "[$lang] 启动翻译... 日志: $LOG_FILE"

    python3 scripts/translate_batch.py --langs "$lang" --batch-size 5 > "$LOG_FILE" 2>&1 &
    PID=$!
    PIDS+=($PID)
    echo "[$lang] PID: $PID"

    # 每启动1个进程间隔1秒，避免同时启动压力
    sleep 1
done

echo ""
echo "=== 所有进程已启动 ==="
echo "进程数: ${#PIDS[@]}"
echo ""
echo "进程ID列表:"
for i in "${!LANGS[@]}"; do
    echo "  ${LANGS[$i]}: PID ${PIDS[$i]}"
done
echo ""

# 保存PID列表到文件
echo "# 并行翻译进程PID列表 - $(date)" > logs/parallel_translate/PIDS.txt
for i in "${!LANGS[@]}"; do
    echo "${LANGS[$i]} ${PIDS[$i]}" >> logs/parallel_translate/PIDS.txt
done

echo "PID列表已保存到: logs/parallel_translate/PIDS.txt"
echo ""
echo "=== 监控命令 ==="
echo "# 查看所有进程状态"
echo "ps aux | grep translate_batch | grep -v grep"
echo ""
echo "# 查看某语种日志"
echo "tail -f logs/parallel_translate/translate_<lang>_*.log"
echo ""
echo "# 统计已翻译条数"
echo "for f in data/queue/translated_terms_*.json; do lang=\$(basename \$f .json | sed 's/translated_terms_//'); count=\$(python3 -c \"import json; print(len(json.load(open('\$f'))))\" 2>/dev/null || echo 0); echo \"  \$lang: \$count 条\"; done"
