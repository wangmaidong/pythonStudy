# 函数的定义
# 文档字符串
# def greet(name):
#     """向指定的人打招呼"""
#     print(f"你好！{name}")
#
#
# print(greet.__doc__)
# greet("王磊")
from idlelib.pyshell import restart_line
from logging import setLogRecordFactory


# 参数类型详解
# 位置参数
# def add(a, b):
#     print(f"a={a}, b={b}")
#     return a + b
#
#
# result = add(23, 45)
# print(result)


# 关键字参数
# def student_info(name, age, city):
#     print(f"姓名：{name}, 年龄：{age}, 城市：{city}")
#
#
# student_info("wanglei", 24, "hangzhou")
# student_info(city="beijing", name="lisi", age=16)


# 默认参数
# def greet(name, msg="hello"):
#     print(f"{msg}, {name}")
#
#
# greet("Alice")
# greet("Sam", "吃了吗？")


# 默认参数需要出现在非默认参数之后
# def foo(b, a=1):
#     pass


# 可变参数 *args
# args 是一个元组
# def show_args(*args):
#     print(f"参数类型：{type(args)}")
#     print(f"参数内容：{args}")
#
#
# show_args(1, 2, 3)
# show_args("wanglei", 23)


# def make_pizza(*toppings):
#     print("制作一个披萨，添加以下配料：")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza("意大利香肠")
# make_pizza("蘑菇", "青椒", "芝士")

# 关键字可变参数
# kwargs 是一个字典类型
# def show_kwargs(**kwargs):
#     print(f"参数类型：{type(kwargs)}")
#     print(f"参数内容：{kwargs}")
#
#
# show_kwargs(a=1, b=2, c=4)


# def demo(a, b=1, *args, **kwargs):
#     print(f"a: {a}")
#     print(f"args: {args}")
#     print(f"b: {b}")
#     print(f"kwargs: {kwargs}")
#
#
# demo(1, 2, 3, 3, c=23)

# 参数的解包


# *用于解包序列类型
# def greet(name, age, city):
#     print(f"姓名：{name}, 年龄：{age}, 城市：{city}")
#
#
# person_info = ["Alice", 25, "杭州"]
# greet(*person_info)
#
# data = ("Bob", 25, "北京")
# greet(*data)

# **用于解包字典类型


# def greet(name, age, city):
#     print(f"姓名：{name}, 年龄：{age}, 城市：{city}")
#
#
# info_dict = {"name": "王磊", "age": 24, "city": "杭州"}
#
# greet(**info_dict)


# 混合使用 * 和 ** 进行参数的解包
# def complex_fun(a, b, d, e, c=3):
#     print(f"a={a}, b={b}, c={c},d={d},e={e}")
#
#
# position_args = [1, 2]
# keyword_args = {"d": 3, "e": 4}
# complex_fun(*position_args, **keyword_args)


# 返回值
# 返回单个值
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + last_name
#     return full_name
#
#
# print(get_formatted_name("wang", "lei"))
#
#
# def oprate_numbers(a, b):
#     sum_result = a + b
#     diff_result = a - b
#     product_result = a * b
#     return sum_result, diff_result, product_result
#
#
# result = oprate_numbers(2, 4)
# print(f"result: {result}, 类型： {type(result)}")
#
#
# # 返回复杂数据结构
# def create_student_report(name, **scores):
#     report = {"name": name, "total_score": 0, "subjects": scores}
#     for score in scores.values():
#         report["total_score"] += score
#
#     report["average"] = report["total_score"] / len(scores)
#     return report
#
#
# student = create_student_report("wanglei", math=86, english=80, science=97)
# print(f"student : {student}, type: {type(student)}")


# 文档字符串
# def calculate_circle_area(radius):
#     """
#     计算圆的面积
#
#     参数:
#     radius (float): 圆的半径
#
#     返回:
#     float: 圆的面积
#     """
#     import math
#
#     return math.pi * radius**2
#
#
# # 查看文档字符串
# print(calculate_circle_area.__doc__)
# # 查看函数帮助
# help(calculate_circle_area)

# 变量作用域
# LEGB 原则  本地作用域  嵌套函数作用域  全局作用域  内置作用域
# name = "全局变量"
#
#
# def outer():
#     name = "外部函数变量"
#
#     def inner():
#         name = "内部函数变量"
#         print(name)
#
#     inner()
#     print(name)
#
#
# outer()
# print(name)
#
# # global 关键字
# counter = 0
#
#
# def increment():
#     global counter
#     counter += 1
#
#
# increment()
# increment()
# print(counter)
#
# # nonlocal关键字
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner", x)
#
#     inner()
#     print("outer", x)
#
#
# outer()


# 函数的高级特性
# 函数作为参数
# def apply_operation(numbers, operation):
#     """对数字列表应用操作"""
#     return [operation(n) for n in numbers]
#
#
# def square(x):
#     return x**2
#
#
# def double(x):
#     return x * 2
#
#
# numbers = [1, 2, 3, 4, 5]
# res1 = apply_operation(numbers, square)
# res2 = apply_operation(numbers, double)
# print(f"res1:{res1}")
# print(f"res2:{res2}")


# 嵌套函数
# def greet(name):
#     def format_message():
#         return f"hello {name}"
#
#     return format_message()
#
#
# print(greet("王磊"))


# 闭包
# def make_multiplier(factor):
#     def multiplier(x):
#         return x * factor
#
#     return multiplier
#
#
# double = make_multiplier(2)
# triple = make_multiplier(3)
#
# print(double(5))
# print(triple(5))


# 装饰器
# def my_decorator(func):
#     def wrapper():
#         print("函数执行前")
#         func()
#         print("函数执行后")
#
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print("Hello")
#
#
# say_hello()


# 带参数的装饰器
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"调用函数 {func.__name__}, 参数： {args} {kwargs}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @logger
# def add(x, y, **kwargs):
#     return x + y
#
#
# print(add(3, 5, a=1, b=2))

# 匿名函数

# square = lambda x: x**2
# print(square(5))
#
# students = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Bob", "grade": 92},
#     {"name": "Charlie", "grade": 78},
# ]
#
# sorted_students = sorted(students, key=lambda x: x["grade"])
# print(sorted_students)

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)
#
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))
#
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# for i in range(10):
#     print(fibonacci(i), end=" ")


# def safe_divide(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         return "错误：除数不能为零"
#     except TypeError:
#         return "错误：参数类型不正确"
#     else:
#         return result
#
#
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# print(safe_divide(10, "sd"))


# 实际函数示例
# 数据处理
# def analyze_numbers(numbers):
#     if not numbers:
#         return None
#     analysis = {
#         "count": len(numbers),
#         "sum": sum(numbers),
#         "mean": sum(numbers) / len(numbers),
#         "max": max(numbers),
#         "min": min(numbers),
#     }
#     return analysis
#
#
# data = [10, 20, 30, 40, 50]
# result = analyze_numbers(data)
# print(result)


def read_file_safely(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileExistsError:
        return f"错误：文件{filename} 不存在"
    except Exception as e:
        return f"读取文件时出错：{str(e)}"
