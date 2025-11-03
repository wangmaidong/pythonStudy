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
def add(a, b):
    print(f"a={a}, b={b}")
    return a + b


result = add(23, 45)
print(result)


# 关键字参数
def student_info(name, age, city):
    print(f"姓名：{name}, 年龄：{age}, 城市：{city}")


student_info("wanglei", 24, "hangzhou")
student_info(city="beijing", name="lisi", age=16)


# 默认参数
def greet(name, msg="hello"):
    print(f"{msg}, {name}")


greet("Alice")
greet("Sam", "吃了吗？")
