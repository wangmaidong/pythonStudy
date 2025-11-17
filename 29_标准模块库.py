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
# from collections import Counter
#
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# word_count = Counter(words)
# print(f"词频统计：{word_count}")
# print(f"出现最多的两个：{word_count.most_common(2)}")
#
# # 更新计数器
# word_count.update(["apple", "orange"])
# print(f"更新后的计数器：{word_count}")
#
#
# # defaultdict 默认字典
#
# from collections import defaultdict
#
# dd = defaultdict(list)
# dd["fruits"].append("apple")
# dd["fruits"].append("banana")
# dd["vegetables"].append("carrot")
# print(f"默认字典：{dict(dd)}")
#
#
# # 自定义默认值函数
# def default_value():
#     return "未知"
#
#
# dd2 = defaultdict(default_value)
# print(f"键值不存在时的值：{dd2['nonexistent']}")
# # 有序字典
# from collections import OrderedDict
#
# od = OrderedDict()
# od["z"] = 1
# od["a"] = 2
# od["c"] = 3
# print(f"有序字典:{od}")
#
# # namedtuple 命名元组
# from collections import namedtuple
# Point = namedtuple("Point", ["x", "y"])
# p = Point(10, 20)
# print("点坐标",p)
# print(f"x坐标：{p.x}")
# print(f"y坐标：{p.y}")
# # 双端队列
# from collections import deque
# dq = deque([1,2,3])
# dq.append(4)
# dq.appendleft(0)
# print(f"双端队列：{dq}")
# print(f"右端弹出：{dq.pop()}")
# print(f"左端弹出：{dq.popleft()}")

# 正则表达式
# import re
#
# text = "小王的邮箱是: kwang@mail.com, 电话: 188-1234-5678。还有一个邮箱：abc_xyz@company.org, 另外电话: 139-8765-4321。"
#
# # 1. match：只检查是否从开头匹配
# result = re.match(r'小王的邮箱是', text)
# if result:
#     print("match - 匹配到字符串开头:", result.group())
#
# # 2. search：查找第一个邮箱
# email = re.search(r'\w+@\w+\.\w+', text)
# if email:
#     print("search - 第一个邮箱:", email.group())
#
# # 3. findall：查找所有电话号码
# phones = re.findall(r'\d{3}-\d{4}-\d{4}', text)
# print("findall - 所有电话:", phones)
#
# # 4. finditer：遍历所有邮箱并打印位置信息
# print("finditer - 所有邮箱位置和内容:")
# for match in re.finditer(r'\w+@\w+\.\w+', text):
#     print(f"邮箱: {match.group()}，起始: {match.start()}，结束: {match.end()}")
#
# # 5. split：按中文全角逗号和冒号分割
# fragments = re.split(r'[：:，,]', text)
# print("split - 分割结果:", fragments)
#
# # 6. compile：预编译正则以提高多次匹配效率
# pattern = re.compile(r'\w+@\w+\.\w+')
# emails = pattern.findall(text)
# print("compile - 所有邮箱:", emails)
#
# # 7. 分组匹配
# m = re.match(r'(\w+)的邮箱是: (\w+@\w+\.\w+)', text)
# if m:
#     print("match.group(0):", m.group(0))  # 整体
#     print("match.group(1):", m.group(1))  # "小王"
#     print("match.group(2):", m.group(2))  # 邮箱
#
# # 8. sub：替换所有数字为*
# anonymized = re.sub(r'\d', '*', text)
# print("sub - 隐私处理后:", anonymized)

# random 随机数生成
import random
print(f"0-1随机浮点数：{random.random()}")
print(f"1-10随机整数：{random.randint(1,10)}")
print(f"1-100随机偶数：{random.randrange(0,101,2)}")
print(f"5.0-10.0随机浮点数：{random.uniform(5.0, 10.0)}")

# 序列操作
items = ['apple', 'banana', 'cherry', 'date']
print(f"随机选择：{random.choice(items)}")
print(f"随机选择多个：{random.choices(items, k=3)}")
print(f"随机抽样：{random.sample(items,2)}")

# 打乱顺序
random.shuffle(items)
print(f"打乱顺序：{items}")
