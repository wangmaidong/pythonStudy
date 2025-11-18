import os
import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import random


def create_sample_data():
    """创建示例数据文件"""
    data = {
        "users": [
            {
                "id": i,
                "name": f"user_{i}",
                "age": random.randint(18, 60),
                "join_date": (
                    datetime.now() - timedelta(days=random.randint(0, 365))
                ).strftime("%Y-%m-%d"),
                "score": random.randint(50, 100),
            }
            for i in range(1, 11)
        ]
    }
    os.makedirs("data", exist_ok=True)

    with open("data/users.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    print(f"示例数据已创建：data/users.json")


def analyze_user_data():
    """分析用户数据"""
    try:
        with open("data/users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("数据文件不存在，请先运行 create_sample_data()")
    except json.JSONDecodeError:
        print("数据文件格式错误")
        return
    # 获取用户所有数据
    users = data["users"]
    age_distribution = Counter(user["age"] for user in users)
    print("\n年龄分布：")
    for age, count in sorted(age_distribution.items()):
        print(f"{age}岁：{count}人")

    score_groups = defaultdict(list)
    for user in users:
        # 计算分数区间（如70-79）
        score_range = f"{(user['score'] // 10) * 10} - {(user['score'] // 10) *10 + 9}"
        # 添加用户名到对应的分数区间
        score_groups[score_range].append(user["name"])
    # 输出分数分组信息
    print("\n分数分组：")
    for score_range, names in sorted(score_groups.items()):
        print(f"{score_range}分：{', '.join(names)}")

    # 统计用户总数
    total_users = len(users)
    # 计算平均年龄
    avg_age = sum(user["age"] for user in users) / total_users
    # 计算平均分数
    avg_score = sum(user["score"] for user in users) / total_users

    # 输出摘要统计
    print(f"\n统计摘要：")
    print(f"总用户数：{total_users}")
    print(f"平均年龄：{avg_age:.1f}岁")
    print(f"平均分数：{avg_score:.1f}分")


def get_user_by_id(user_id):
    """根据ID获取用户信息"""
    try:
        with open("data/users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        for user in data["users"]:
            if user["id"] == user_id:
                return user
        return None
    except FileNotFoundError:
        print("数据文件不存在")
        return None


def get_top_users(limit=5):
    try:
        with open("data/users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        users = data["users"]
        # 将用户按分数降序排列，取前limit个
        top_users = sorted(users, key=lambda x: x["score"], reverse=True)[:limit]
        # 打印前top N名用户信息
        print(f"\n前{limit}名用户:")
        for i, user in enumerate(top_users):
            print(f"{i}.{user['name']} - {user['score']} 分")
            # 返回最高分的用户列表
        return top_users
    except FileNotFoundError:
        print("数据文件不存在")
        return None


def search_users_by_age(min_age, max_age):
    """根据年龄范围搜索用户"""
    try:
        with open("data/users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        users = data["users"]
        filtered_users = [user for user in users if min_age <= user["age"] <= max_age]
        print(f"\n年龄在{min_age}--{max_age}岁的用户")
        if filtered_users:
            for user in filtered_users:
                print(f"{user['name']} - {user['age']}岁 - {user['score']}分")
        else:
            print("没有找到符合条件的用户")
        return filtered_users
    except FileNotFoundError:
        print("数据文件不存在")
        return None


# 只有在模块作为脚本直接运行时才执行以下代码
if __name__ == "__main__":
    # 打印分隔线
    print("=" * 50)
    # 输出系统标题
    print("用户数据分析系统")
    # 再打印分隔线
    print("=" * 50)

    # 创建样本数据
    create_sample_data()

    # 分析用户数据
    analyze_user_data()

    # 显示分数前5名用户
    get_top_users(5)

    # 按指定年龄段搜索用户
    search_users_by_age(25, 35)

    # 打印分析结束标志
    print("\n" + "=" * 50)
    print("分析完成！")
    print("=" * 50)
