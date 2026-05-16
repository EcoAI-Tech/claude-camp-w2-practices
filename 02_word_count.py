"""
练习 2:词频统计器
读取一段文本,统计每个单词出现的次数,按次数从高到低排序输出。
大小写不敏感,标点不计入单词。
"""
import re
from collections import Counter


def count_words(text):
    """统计文本中各单词的词频,返回 Counter

    - 转小写实现大小写不敏感
    - 用正则提取「字母/数字」组成的词,自动忽略标点
    """
    words = re.findall(r"[a-z0-9]+", text.lower())
    return Counter(words)


def read_text():
    """读取多行文本输入,空行结束"""
    print("请输入文本(可多行,输入空行结束):")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:  # 支持管道输入 / Ctrl+D 结束
            break
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)


def print_report(counter):
    """按词频降序打印统计结果,次数相同按字母序"""
    if not counter:
        print("📭 没有统计到任何单词")
        return

    total = sum(counter.values())
    print(f"\n📊 共 {total} 个单词,{len(counter)} 个不同单词:")

    # 排序:次数降序,次数相同则单词升序
    ranked = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    width = max(len(word) for word, _ in ranked)
    for word, count in ranked:
        bar = "█" * count
        print(f"  {word:<{width}}  {count:>3}  {bar}")


def main():
    print("=" * 40)
    print("          词频统计器")
    print("=" * 40)

    text = read_text()
    counter = count_words(text)
    print_report(counter)


if __name__ == "__main__":
    main()
