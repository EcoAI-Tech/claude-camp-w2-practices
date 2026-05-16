"""
练习 1:学员花名册管理器
用字典存储学员信息(姓名、邮箱、加入日期),支持增、查、删。
"""
from datetime import datetime

# 用字典存储学员:key 是姓名,value 是 {邮箱, 加入日期}
roster = {}

def _split(text):
    """按中英文逗号拆分,去掉首尾空格和空项"""
    return [p.strip() for p in text.replace("，", ",").split(",") if p.strip()]


def add_student():
    """添加学员(支持用逗号一次添加多个)"""
    names = _split(input("请输入学员姓名(多个用逗号隔开):"))
    if not names:
        print("❌ 姓名不能为空")
        return

    emails = _split(input("请输入邮箱(多个用逗号隔开,与姓名一一对应):"))
    if len(names) != len(emails):
        print(f"❌ 姓名有 {len(names)} 个,邮箱有 {len(emails)} 个,数量不一致")
        return

    added = 0
    for name, email in zip(names, emails):
        if name in roster:
            print(f"❌ {name} 已存在,跳过")
            continue
        if "@" not in email or "." not in email:
            print(f"❌ {name} 的邮箱「{email}」格式不正确,跳过")
            continue
        roster[name] = {
            "email": email,
            "join_date": datetime.now().strftime("%Y-%m-%d"),
        }
        print(f"✅ 已添加:{name}")
        added += 1

    if added:
        print(f"📦 本次共添加 {added} 位学员")


def query_student():
    """查询学员(留空看全部)"""
    if not roster:
        print("📭 花名册为空")
        return

    name = input("请输入姓名(留空看全部):").strip()
    if not name:
        print(f"\n📋 共 {len(roster)} 位学员:")
        for n, info in roster.items():
            print(f"  • {n} | {info['email']} | 加入于 {info['join_date']}")
        return

    if name in roster:
        info = roster[name]
        print(f"✅ {name} | {info['email']} | 加入于 {info['join_date']}")
    else:
        print(f"❌ 未找到 {name}")


def delete_student():
    """删除学员"""
    name = input("请输入要删除的姓名:").strip()
    if name in roster:
        del roster[name]
        print(f"✅ 已删除 {name}")
    else:
        print(f"❌ {name} 不在花名册中")


def main():
    print("=" * 40)
    print("       学员花名册管理器")
    print("=" * 40)

    actions = {
        "1": ("添加学员", add_student),
        "2": ("查询学员", query_student),
        "3": ("删除学员", delete_student),
    }

    while True:
        print("\n请选择操作:")
        for k, (label, _) in actions.items():
            print(f"  {k}. {label}")
        print("  4. 退出")

        choice = input("输入选项(1-4):").strip()
        if choice == "4":
            print("👋 再见!")
            break
        if choice in actions:
            actions[choice][1]()
        else:
            print("❌ 无效选项,请输入 1-4")


if __name__ == "__main__":
    main()