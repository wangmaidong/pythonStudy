# 整数的基本概念
# positive = 42
# negative = -16
# zero = 0
# print(f"positive: {positive}, 类型是：{type(positive)}")
# print(f"nagative: {negative}, 类型是：{type(negative)}")
# print(f"zero: {zero}, 类型是：{type(zero)}")

# 不同进制的整数表示
# 最后都会以十进制在控制台打印
# decimal = 10
# print(f"十进制10： {decimal}")

# binary = 0b1010
# print(f"二进制 0B1010: {binary}")

# octal = 0o12
# print(f"八进制 0O12: {octal}")

# hexadecimal = 0xA
# print(f"十六进制 0Xa: {hexadecimal}")

# large_number = 1_000_000
# print(f"大数字： {large_number}")

# credit_card = 1234_5678_9012
# print(f"信用卡号：{credit_card}")

# bytes_value = 0b1100_1010_0101
# print(f"字节值：{bytes_value}")

# 整型转换函数

# print("类型转换：")
# print(f"int(3.14) = {int(3.14)}")
# print(f"int(-2.99) = {int(-2.99)}")
# print(f"int('100') = {int('100')}")
# print(f"int('1010', 2) = {int('1010',2)}")
# print(f"int('FF', 16) = {int('ff', 16)}")
# print(f"int(True) = {int(True)}")
# print(f"int(False) = {int(False)}")

# 进制转换函数
# number = 10
# print(f"\n数字 {number} 的不同进制")
# print(f"二进制：{bin(number)}")
# print(f"八进制：{oct(number)}")
# print(f"十六进制：{hex(number)}")

# 整型运算
# a, b = 10, 3

# 基本算数运算
# print("基本算数运算")
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")
# print(f"{a} // {b} = {a//b}")
# print(f"{a} % {b} = {a%b}")
# print(f"{a} ** {b} = {a**b}")
# print(f"-{a} = {-a}")
# print(f"+{a} = {+a}")

# 位运算
# x, y = 5, 3
# print(f"x的二进制：{bin(x)}")  # 0b101
# print(f"y的二进制：{bin(y)}")  # 0b011

# print(f"{x} & {y} = {x&y} , 二进制：{bin(x&y)}")
# print(f"{x} | {y} = {x|y}, 二进制：{bin(x|y)}")
# print(f"{x} ^ {y} = {x^y}, 二进制：{bin(x^y)}")
# print(f"~{x} = {~x}, 二进制：{bin(~x)}")
# print(f"{x} << 1 = {x<<1}, 二进制：{bin(x<<1)}")
# print(f"{x} >> 1 = {x>>1}, 二进制：{bin(x>>1)}")

# READ_PERMISSION = 0b001

# WRITE_PERMISSION = 0b010

# EXECUTE_PERMISSION = 0b100

# user_permissions = READ_PERMISSION | WRITE_PERMISSION  # 0b011

# print(f"\n权限控制")
# print(f"用户权限：{type(bin(user_permissions)) }")

# print(f"可读权限：{(user_permissions & READ_PERMISSION) != 0}")

# print(f"可写权限：{(user_permissions & WRITE_PERMISSION) != 0}")

# print(f"可执行权限：{(user_permissions & EXECUTE_PERMISSION) != 0}")

# # 添加执行权限

# user_permissions |= EXECUTE_PERMISSION

# print(f"添加执行权限后：{(user_permissions & EXECUTE_PERMISSION) != 0}")

# 比较运算
# a, b = 10, 5
# print("比较运算")
# print(f"{a} == {b}: {a == b}")
# print(f"{a} != {b}: {a != b}")

# print(f"{a} > {b}: {a > b}")

# print(f"{a} < {b}: {a < b}")

# print(f"{a} >= {b}: {a >= b}")
# print(f"{a} <= {b}: {a <= b}")

# 链式比较

# c = 7

# print(f"\n链式比较：")
# print(f"{b} < {c} < {a} : { b < c < a}")
# print(f"{a} > {c} > {b} : {a > c >b}")

# 整型的特性

# very_large = 10**100
# very_small = -(10**100)

# print(f"非常大的数：{very_large}")
# print(f"非常小的数：{very_small}")
# print(f"类型依然是：{type(very_large)}")


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# print(f"\n演示阶乘")

# print(f" 10 != {factorial(10)}")
# print(f"50 != {factorial(50)}")

# 内存占用
# import sys

# numbers = [0, 1, 10, 100, 1000, 10**10, 10**100]

# print(f"\n内存占用")

# for num in numbers:
#     size = sys.getsizeof(num)
#     print(f"数字{num}: {size}字节")

# 内置数学函数

import math

numbers = [-5, 0, 5, 10, 15]

print("内置数学函数")

for num in numbers:
    print(f"abs({num}) = {abs(num)}")

print(f"\n最大值：{max(1,5,9,3,4)}")
print(f"最小值：{min(1,52,47,2,6)}")
print(f"求和：{sum([1,5,3])}")

print(f"2的3次方：{pow(2,3)}")
print(f"四舍五入：{round(3.1415926, 3)}")
print(f"向上取整：{math.ceil(3.14)}")
print(f"向下取整：{math.floor(3.14)}")

print(int(3.1415926))
