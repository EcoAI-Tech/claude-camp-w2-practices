"""
练习 3:待办清单
支持添加任务、标记完成、查看列表。
数据持久化到 todos.json,重启后自动加载;文件缺失或损坏时优雅降级。
"""
import json
import os

DATA_FILE = "todos.json"


def load_todos():
    """从 todos.json 加载任务;文件缺失或损坏时返回空列表"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️  读取 {DATA_FILE} 失败({e}),将以空清单开始")
        return []
    if not isinstance(data, list):
        print(f"⚠️  {DATA_FILE} 内容格式不对,将以空清单开始")
        return []
    return data


def save_todos(todos):
    """把任务列表写回 todos.json"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"❌ 保存失败:{e}")


def add_task(todos):
    """添加一个待办任务"""
    title = input("请输入任务内容:").strip()
    if not title:
        print("❌ 任务内容不能为空")
        return
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"✅ 已添加:{title}")


def complete_task(todos):
    """按编号把任务标记为完成"""
    if not todos:
        print("📭 清单为空")
        return
    show_tasks(todos)
    raw = input("请输入要完成的任务编号:").strip()
    if not raw.isdigit():
        print("❌ 请输入数字编号")
        return
    idx = int(raw) - 1
    if not 0 <= idx < len(todos):
        print(f"❌ 编号 {raw} 超出范围")
        return
    if todos[idx]["done"]:
        print(f"ℹ️  「{todos[idx]['title']}」已经是完成状态")
        return
    todos[idx]["done"] = True
    save_todos(todos)
    print(f"✅ 已完成:{todos[idx]['title']}")


def show_tasks(todos):
    """查看所有任务"""
    if not todos:
        print("📭 清单为空")
        return
    done = sum(1 for t in todos if t["done"])
    print(f"\n📋 共 {len(todos)} 个任务,已完成 {done} 个:")
    for i, task in enumerate(todos, 1):
        mark = "✔" if task["done"] else " "
        print(f"  {i}. [{mark}] {task['title']}")


def main():
    print("=" * 40)
    print("           待办清单")
    print("=" * 40)

    todos = load_todos()
    if todos:
        print(f"📂 已加载 {len(todos)} 个历史任务")

    actions = {
        "1": ("添加任务", add_task),
        "2": ("标记完成", complete_task),
        "3": ("查看列表", show_tasks),
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
            actions[choice][1](todos)
        else:
            print("❌ 无效选项,请输入 1-4")


if __name__ == "__main__":
    main()
