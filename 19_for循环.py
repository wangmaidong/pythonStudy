# 遍历各种元素
# # 遍历列表
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"fruit: {fruit}")
# # 遍历元组
# numbers = (1, 2, 3)
# for num in numbers:
#     print(f"num : {num}")
#
# # 遍历字符串
#
# text = "hello"
# for t in text:
#     print(f"遍历字符串：{t}")
#
# # 遍历集合
# unique_numbers = set([1, 2, 3, 4, 5])
# for num in unique_numbers:
#     print(f"遍历集合：{num}")
# # 遍历字典
# person = {"name": "Alice", "age": 30, "city": "Beijing"}
#
# for key in person:
#     print(f"key: {key}")
#
# for value in person.values():
#     print(f"value: {value}")
#
# for item in person.items():
#     print(f"item: {item}")
import math

# range()函数
# for i in range(6):
#     print(i)
# print("------------------")
# for i in range(1, 6):
#     print(i)
# print("------------------")
# for i in range(0, 10, 3):
#     print(i)
# print("------------------")
# for i in range(5, 0, -1):
#     print(i)

# enumerate()函数

# fruits = ["apple", "orange", "lemon"]
#
# for index, fruit in enumerate(fruits):
#     print(f"{index}:{fruit}")
#
# for index, fruit in enumerate(fruits, 1):
#     print(f"{index}:{fruit}")

# 循环控制语句

# # break
# numbers = [2, 5, 8, 12, 7, 15, 3]
# for num in numbers:
#     if num > 10:
#         print(num)
#         break
#     print(f"检查数字：{num}")
#
# #  continue
#
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# else 循环结束后的语句（没有break中断）
# target = 88
# numbers = [1, 2, 4, 56, 78]
# for num in numbers:
#     if num == target:
#         print(f"找到了目标：{target}")
#         break
# else:
#     print(f"没有找到目标：{target}")

# 嵌套循环 打印 9 * 9 乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")
#     print("------------")

# 实际应用案例
# scores = [85, 92, 78, 96, 88]
# total = 0
#
# for score in scores:
#     total += score
#
# average_score = math.floor(total / len(scores))
# print(f"平均分是：{average_score}")

numbers = [2, 4, 6, 8]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # 危险！会跳过元素
