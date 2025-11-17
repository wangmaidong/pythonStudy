# os - 操作系统接口
# 目录操作
import json
import os

# print("当前目录", os.getcwd())
# os.chdir("testfile")
# print("切换后", os.getcwd())
#
# # 目录管理
# os.makedirs("test_dir/sub_dir", exist_ok=True)
# os.rmdir("test_dir/sub_dir")
# print("目录内容", os.listdir("."))

# 路径操作
# file_path = "home/user/document.txt"
# print(f"目录名：{os.path.dirname(file_path)}")
# print(f"文件名：{os.path.basename(file_path)}")
# print(f"路径分割：{os.path.split(file_path)}")
# print(f"扩展名：{os.path.splitext(file_path)}")

# 环境变量
# print("PATH", os.getenv("PATH"))
# print("所有环境变量：", dict(os.environ))

# result = os.system("ls -l")
# print("命令结果：", result)

# sys 系统相关功能
import sys

#
# print(f"python版本：{sys.version}")
# print(f"平台信息：{sys.platform}")
# print(f"可执行文件路径：{sys.executable}")

# 命令行参数
# print(f"命令参数：{sys.argv}")
# if len(sys.argv) < 2:
#     print("缺少参数")
#     sys.exit(1)

# 查看模块搜索路径
# print("模块搜索路径：")
# for path in sys.path:
#     print(" ", path)

# sys.path.append("/custom/module/path")

# sys.stdout.write("标准输出\n")

# x = [1, 2, 3]
# print("引用计数：", sys.getrefcount(x))

# datetime 日期时间处理
# 获取当前时间
from datetime import datetime, date, time, timedelta

# now = datetime.now()
# print("当前时间：", now)
# print(f"格式化时间：{now.strftime("%Y-%m-%d %H-%M-%S")}")

# # 创建特定时间
# dt = datetime(2024, 1, 15, 14, 30, 0)
# print(f"特定时间：{dt}")
# # 时间运算
# tomorrow = now + timedelta(days=1)
# last_week = now - timedelta(weeks=1)
# print(f"明天：{tomorrow}")
# print(f"上周：{last_week}")
#
# time_diff = tomorrow - now
# print(f"时间差：{time_diff}")
# print(f"相差天数：{time_diff.days}")
# print(f"相差秒数：{time_diff.total_seconds()}")
# # 时间组件
# print(f"年：{now.year}")
# print(f"月：{now.month}")
# print(f"日：{now.day}")
# print(f"时：{now.hour}")
# print(f"分：{now.minute}")
# print(f"秒：{now.second}")
# # 字符串解析
# date_str = "2025-11-17 18-39-19"
# parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H-%M-%S")
# print(f"解析后的时间：{parsed_date}")

# JSON数据处理

# 基本用法
# data = {
#     "name": "张三",
#     "age": 25,
#     "is_student": False,
#     "hobbies": ["读书", "编程", "音乐"],
#     "address": {"city": "北京", "street": "朝阳区"},
# }
# json_str = json.dumps(data, ensure_ascii=False, indent=2)
# print(f"JSON字符串：{json_str}")
#
# parsed_data = json.loads(json_str)
# print(f"解析后的数据：{parsed_data}")
# print(f"姓名：{parsed_data['name']}")
#
#
# # 自定义编码器
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class PersonEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "age": obj.age}
#         return super().default(obj)


# person = Person("李四", 30)
# person_json = json.dumps(person, cls=PersonEncoder, ensure_ascii=False)
# print("自定义对象JSON:", person_json)

# collections 高级数据结构
# counter 计数器
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(f"词频统计：{word_count}")
print(f"出现最多的两个：{word_count.most_common(2)}")

# 更新计数器
word_count.update(["apple", "orange"])
print(f"更新后的计数器：{word_count}")


# defaultdict 默认字典

from collections import defaultdict

dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["vegetables"].append("carrot")
print(f"默认字典：{dict(dd)}")


# 自定义默认值函数
def default_value():
    return "未知"


dd2 = defaultdict(default_value)
print(f"键值不存在时的值：{dd2['nonexistent']}")
# 有序字典
from collections import OrderedDict

od = OrderedDict()
od["z"] = 1
od["a"] = 2
od["c"] = 3
print(f"有序字典:{od}")
