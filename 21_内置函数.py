# 数学运算函数
# 基本教学函数
# 取绝对值
# print(f"abs()取绝对值")
# print(abs(-5))
# print(abs(3.14))
# 四舍五入
# print(f"round()四舍五入")
# print(round(3.1415, 2))
# print(round(3.58, 1))
# 幂运算
# print(f"pow()幂运算")
# print(pow(2, 3))
# print(pow(10, 3))
# divmod() 返回商和余数
# quotient, remainder = divmod(10, 3)
# print(f"{divmod(10, 3)}, type: {type(divmod(10, 3))}")
from codecs import namereplace_errors

# 最值函数
# numbers = [1, 5, 2, 8, 3]
# print(max(numbers))
# print(min(numbers))
#
# print(max(1, 5, 3))
# print(min(23, 54, 39))
# 支持字符串比较
# print(max("abcdef"))
# print(max("ax", "tw"))

# 类型转换函数
# 基本类型转换
# print(f"基本类型转换")
# print(int("123"))
# print(float("3.14"))
# print(str(345))
# print(bool(0))
# print(bool(1))
# print(bool(""))
# print(bool("Hello"))

# 集合类型转换
# print(f"集合类型转换")
# print(list("Hello"))
# print(tuple([1, 23, 45]))
# print(set([1, 2, 1, 34, 5, 5]))
# paris = [("a", 1), ("b", 2)]
# print(dict(paris))

# 特殊函数转换
# ASCII转成字符
# print(chr(65))
# 字符转ASCII码
# print(ord("A"))

# 进制转换
# print(bin(10))
# print(oct(10))
# print(hex(10))

# 序列操作函数

# 长度和统计
# print(f"长度和统计")
# print(len("abscde"))
# print(len([1, 23, 4, 5, 6]))
# print(len((1, 2, 3, 4, 5)))
# print(len({"a", "b", 1, 2, 3}))
# print(len({"a": 1, "b": 2}))

# 求和
# print(f"sum求和")
# scores = [80, 50, 45]
# print(sum(scores))
# 指定初始值
# print(sum(scores, 20))

# 排序和反转
# print(f"排序和反转")
# letters = ["b", "c", "a", "d"]
# print(sorted(letters))
# print(sorted(letters, reverse=True))
# 生成反向迭代器
# nums = [1, 2, 3]
# for n in reversed(nums):
#     print(n, end=" ")
# print(f"{reversed(nums)}, type:{type(reversed(nums))}")
# print(list(reversed(nums)))
# 枚举和打包
# foods = ["apple", "banana", "orange"]
# for idx, food in enumerate(foods):
#     print(f"{idx}: {food}")
# zip() 并行打包多个序列
# names = ["zhangsan", "lisi", "wanglei"]
# ages = [12, 34]
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")

# 逻辑判断
# flags = [True, False, True]
# print(any(flags))
# print(all(flags))
# scores = [80, 70, 65, 90]
# list_data = [x > 60 for x in scores]
# print(any(x > 60 for x in scores))
# print(all(x > 60 for x in scores))

# 迭代器和生成器相关
# range()函数
# for i in range(5):
#     print(f"i:{i}")
# print(f"\n指定开始和结束")
# for i in range(15, 10, -1):
#     print(i, end=" ")
# print(f"\n指定开始结束和步长")
#
# for i in range(10, 20, 2):
#     print(i, end=" ")

# enumerate()函数
# 返回枚举对象，包含索引和值

# fruits = ["apple", "banana", "cherry"]
# for i, fruit in enumerate(fruits):
#     print(f"{i}:{fruit}")
#
# for i, fruit in enumerate(fruits, start=1):
#     print(i, fruit)

# zip()函数
# names = ["Tom", "Jerry", "Spike"]
# scores = [95, 98, 88]
#
# for name, score in zip(names, scores):
#     print(f"{name} 的分数是：{score}")
#
# pairs = [("a", 1, 6), ("b", 2, 5), ("c", 3, 4)]
# letters, numbers, newnumbers = zip(*pairs)
# print(letters)
# print(numbers)
# print(newnumbers)


# map()和filter()函数
# words = ["hello", "world", "python"]
# upper_words = list(map(str.upper, words))
# print(upper_words)
# numbers = [1, 2, 3, 4]
# square = list(map(lambda x: x**2, numbers))
# print(square)

# filter()函数
# words = ["apple", "banana", "cat", "elephant"]
# new_words = list(filter(lambda str: len(str) > 5, words))
# print(new_words)
#
# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = list(filter(lambda n: n % 2 == 0, numbers))
# print(new_numbers)

# reversed()和sorted()函数

# for c in reversed("abcde"):
#     print(c, end=" ")
#
# fruits = ["apple", "banana", "cherry"]
# print(enumerate(fruits))
# print(list(enumerate(fruits)))
#
# numbers = [3, 1, 4, 4, 5]
# print(sorted(numbers))
#
# nums = [-3, 2, 1, -5]
# print(sorted(nums, key=abs))
# print(sorted(nums, key=abs, reverse=True))
#
# words = ["apple", "banana", "cherry", "date"]
# print(sorted(words, key=len))

# 对象操作和属性函数
# 类型检查函数
# 获取对象类型
# print(type("hello"))
# print(type([1, 2, 3]))
# 检查对象类型
# print(isinstance(5, int))
# print(isinstance(6, float))
# print(isinstance("abc", str))


# 属性操作函数
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#
# s = Student("Tom")
# # hasattr()检查对象是否有某个属性
# print(hasattr(s, "name"))
# print(hasattr(s, "age"))
# # getattr()获取对象的某个属性的值
# print(getattr(s, "name"))
# print(getattr(s, "age", None))

# setattr()给对象设置某个属性
# setattr(s, "age", 25)
# print(s.age)

# delattr()删除对象的某个属性值
# delattr(s, "age")
# print(s)

# 其他对象函数

# print(callable(print))
# print(callable(len))
# print(callable(list))

# dir()返回对象的所有属性列表
# print(dir(s))

# vars()返回对象的所有属性字典
# print(vars(s))

# id()返回对象的唯一标识
# print(id(s))

# 高级函数
# reduce()函数
# from functools import reduce
#
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)
#
# total = reduce(lambda x, y: x + y, numbers)
# print(total)
#
# result = reduce(lambda x, y: x + y, numbers, 10)
# print(result)
# 函数式变成
# numbers = [5, 2, 8, 1, 9, 3]
# result = sorted(filter(lambda x: x > 3, numbers))
# print(result)


def process_data(data):
    """数据处理函数"""
    # 数据过滤
    valid_data = list(filter(lambda x: x is not None and x > 0, data))
    # 数据转换
    processed_data = list(map(lambda x: x * 2, valid_data))
    # 排序
    sorted_data = sorted(processed_data)
    # 统计
    state = {
        "count": len(sorted_data),
        "max": max(sorted_data),
        "min": min(sorted_data),
        "sum": sum(sorted_data),
    }
    return sorted_data, state


raw_data = [1, 2, None, 3, -1, 4, 0, 5]
processed, stats = process_data(raw_data)
print(f"处理后的数据: {processed}")
print(f"统计信息: {stats}")

result = 0 and True
print(result)
print()
