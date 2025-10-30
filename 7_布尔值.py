from pickle import FALSE

# is_sunny = True
# is_raining = False
#
# print(f"is_sunny: {is_sunny}, 类型：{type(is_sunny)}")
# print(f"is_raining: {is_raining},类型：{type(is_raining)}")
#
#
# print(f"True == 1 , {True == 1}")
# print(f"False == 0 , {False == 0}")
# print(f"True + True, {True + True}")
# print(f"False * 10 , {False * 10}")

# 布尔值的运算
# a, b = True, False
# print("布尔值运算：")
# print(f"与操作{a} and {b} = {a and b}")
# print(f"或操作{a} or {b} = {a or b}")
# print(f"非操作 not {a} = {not a}")
# print(f"非操作 not {b} = {not b}")
# 真值表

# print(f"AND运算")
# print(f"True and True = {True and True}")
# print(f"True and False = {True and False}")
# print(f"False and True = {False and True}")
# print(f"False and False = {False and False}")
#
# print(f"OR运算")
# print(f"True  or True = {True or True}")
# print(f"True or False = {True or False}")
# print(f"False or True = {False or True}")
# print(f"False or False = {False or False}")
#
# print(f"not运算")
# print(f"not True = {not True}")
# print(f"not False = {not False}")


# 短路特性
# def expensive_operation():
#     print("执行了耗时操作")
#     return True
#
#
# print("短路特性")
# result1 = False and expensive_operation()
# print(f"False and 耗时操作：{result1}")
#
# result2 = False or expensive_operation()
#
# print(f"False or 耗时操作：{result2}")
#
# result3 = True and expensive_operation()
# print(f"True and 耗时操作：{result3}")
# result4 = True or expensive_operation()
# print(f"True or 耗时操作：{result4}")

# 假值列表
# falsy_values = [False, None, 0, 0.0, 0j, "", [], (), {}, set()]
#
# print("假值测试")
# for value in falsy_values:
#     if value:
#         print(f"{value!r:10} --> True")
#     else:
#         print(f"{value!r:10} --> False")
# 真值列表
# truthy_values = [True, 1, 0.1, "hello", [1, 2, 3], (1, 2), {"key", "value"}, {1, 2, 3}]
# for value in truthy_values:
#     if value:
#         print(f"{value!r:10} ---> True")
#     else:
#         print(f"{value!r:10} ---> False")


# 条件语句

# age = 20
# has_license = True
# has_car = False
# if age >= 18:
#     print("已成年")
#
# if has_car and has_license:
#     print("可以开车")
# else:
#     print("不可以开车")
#
# score = 85
#
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# else:
#     grade = "D"
# print(f"分数：{score} --> 等级：{grade}")

# 循环控制
# count = 0
# while count < 5:
#     print(f"while循环：count = {count}")
#     count += 1
# print("\nbreak 和 continue 演示")
# for i in range(10):
#     if i == 2:
#         continue
#     if i == 7:
#         break
#     print(f"i == {i}")

# 布尔函数和操作


# bool()
# def bool_fun():
#     test_values = [0, 0.0, 0j, 1, -1, {}, (), [], None, [1]]
#     print("bool()函数测试：")
#     for value in test_values:
#         print(f"bool({value!r:10}) = {bool(value)}")
#
#
# bool_fun()


# class BanKAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def __bool__(self):
#         return self.balance > 0
#
#     def __str__(self):
#         return f"BankBalance(余额： ${self.balance})"
#
#
# print("\n自定义对象的布尔值")
# account1 = BanKAccount(100)
#
# account2 = BanKAccount(0)
# print(f"{account1}: bool() = {bool(account1)}")
# print(f"{account2}: bool() = {bool(account2)}")

# any() 和 all()函数
print("any()函数")
list1 = [True, True, True]
list2 = [False, True, False]
print(f"any([True, True, True]) = {any([True, True, True])}")
print(f"any([False, True, False]) = {any([False, True, False])}")
print(f"all([False, True, False]) = {all([False, True, False])}")
