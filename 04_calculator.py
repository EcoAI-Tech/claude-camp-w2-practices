"""
练习 4:安全计算器
支持四则运算(+ - × ÷),对除以零、非数字输入优雅处理,输入 quit 退出。
"""

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def read_number(prompt):
    """读取一个数字;输入 quit 返回 None 表示退出"""
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "quit":
            return None
        try:
            return float(raw)
        except ValueError:
            print(f"❌ 「{raw}」不是有效数字,请重新输入(或输入 quit 退出)")


def read_operator():
    """读取一个运算符;输入 quit 返回 None 表示退出"""
    while True:
        op = input("请输入运算符(+ - * /):").strip()
        if op.lower() == "quit":
            return None
        if op in OPERATORS:
            return op
        print("❌ 只支持 + - * /,请重新输入(或输入 quit 退出)")


def format_result(value):
    """整数值去掉多余的 .0,其余保留原样"""
    return int(value) if value == int(value) else value


def main():
    print("=" * 40)
    print("           安全计算器")
    print("=" * 40)
    print("支持 + - * /,任意输入 quit 退出\n")

    while True:
        a = read_number("请输入第一个数字:")
        if a is None:
            break

        op = read_operator()
        if op is None:
            break

        b = read_number("请输入第二个数字:")
        if b is None:
            break

        try:
            result = OPERATORS[op](a, b)
        except ZeroDivisionError:
            print("❌ 除数不能为零,请重新开始\n")
            continue

        x, y = format_result(a), format_result(b)
        print(f"✅ {x} {op} {y} = {format_result(result)}\n")

    print("👋 再见!")


if __name__ == "__main__":
    main()
