# 身份运算符
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
#
# print(f"a is b: {a is b}")
# print(f"b is c: {b is c}")
# print(f"b is not c: {b is not c}")

# 成员运算符
# 成员运算符示例
# fruits = ["苹果", "香蕉", "橙子"]
# print("苹果" in fruits)
# print("香蕉" in fruits)
# print("橙子" in fruits)
# print("榴莲" in fruits)
# print("芒果" not in fruits)
#
# text = "Hello World"
# print("Hello" in text)
# print("python" in text)

# 优先级
# result1 = 2 + 3 * 4
# result2 = (2 + 3) * 4
# result3 = 10 - 4 + 2
# result4 = 2**3 * 4
# result5 = 15 / 3 * 2
# print(f"result1: {result1}")
# print(f"result2: {result2}")
# print(f"result3: {result3}")
# print(f"result4: {result4}")
# print(f"result5: {result5}")
#
# a, b, c = 5, 3, 2
# result6 = a + b * c**2
# print(result6)
# result_clear = a + (b * (c**2))
# print(result_clear)

# 结合性规则
# 从左到右：大多数运算符：+ - / // %
# 从右到左：**  = +=
# result7 = 10 - 3 - 2
# result8 = 2**2**3
# print(result7)
# print(result8)

# a = b = c = d = e = f = g = 1
# result = (a + b) * (c - d) / (e**f) % g
# print(result)

# 浮点数
# print(f" 5 / 2 = { 5/ 2} , 类型是：{ type (5/2)}")
# print(f" 5 // 2 = { 5 // 2}, 类型是：{type(5 // 2)}")

# 逻辑运算符的短路特性和返回值

# v1 = "zhangsan" and "wanglei"
#
# print(v1)
#
# v2 = "" and "lisi"
# print(v2)

# 设置默认值
# username = input("请输入用户名") or "匿名用户"
# print(f"欢迎：{username}!")
#
# name = "" or "Guset"
# print(name)
# config = {}
# port = config.get("port") or 8080
# print(port)

# 条件赋值
# is_vip = True
# discount = is_vip and 0.8 or 0.6
# print(f"折扣: {discount}")
#
# if is_vip:
#     discount = 0.8
# else:
#     discount = 0.6

# 链式判断
# import os
#
# config = {}
# result = None or "" or 0 or "找到了" or "backup"
# print(result)
#
# db_host = os.getenv("DB_HOST") or config.get("db_host") or "localhost"
# print(db_host)
# 条件执行

# debug_mode = True
# debug_mode and print("调试信息：正在运行....")
# if debug_mode:
#     print("调试信息：正在运行...")

# 复杂示例

# result1 = "a" and "b" and "c"
# print(result1)
# result2 = "" and "b" or "c"
# print(result2)
# result3 = 0 or [] or {} or "default"
# print(result3)
# result4 = [1] or [2] or [3]
# print(result4)

# 以下值都会被视为假值

print(bool(None))
print(bool(""))
print(bool({}))
print(bool([]))
print(bool(0))
print(bool(0.00))
print(bool(0j))
