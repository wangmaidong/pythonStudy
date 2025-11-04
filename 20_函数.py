# 函数的定义
# 文档字符串
# def greet(name):
#     """向指定的人打招呼"""
#     print(f"你好！{name}")
#
#
# print(greet.__doc__)
# greet("王磊")


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
name = "全局变量"


def outer():
    name = "外部函数变量"

    def inner():
        name = "内部函数变量"
        print(name)

    inner()
    print(name)


outer()
print(name)

# global 关键字
counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()
print(counter)

# nonlocal关键字


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner", x)

    inner()
    print("outer", x)


outer()
