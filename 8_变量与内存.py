# 多重赋值
# a = b = c = 100
# print(a, b, c)
#
# name, city, age = "wanglei", "hangzhou", 25
#
# print(name)
# print(city)
# print(age)

# 变量交换
# x, y = 10, 20
# x, y = y, x
# print(x)
# print(y)

# 一切皆是对象
# x = 42
# print(type(x))
# print(isinstance(x, object))
#
#
# def foo():
#     print(1)
#
#
# print(type(foo))
# print(isinstance(foo, object))
#
# # 动态类型
# var = 100
# print(type(var))
#
# var = "wanglei1"
# print(type(var))

# 对象的身份 id() 和 is()

# a = [1, 2, 3]
# print(id(a))
#
# b = a
# c = [1, 2, 3]
#
# print(a is b)
# print(a is c)
# print(a == c)
#
# print(id(a))
# print(id(b))
# print(id(c))

# a = 100
# b = a
# print(a is b)
# print(id(a))
# print(id(b))
#
# a = 200
# print(a is b)
# print(id(a))
# print(id(b))

# 整数缓存
# a = 100
# b = 100
# print(a is b)
# s1 = "hello"
# s2 = "hello"
# print(s1 is s2)
#
s3 = "hello" * 10
# s4 = "hello" * 10000
#
# print(s3)

# 元组示例
t = (1, 2, 3)
print(f"t的地址：{id(t)}")

t = (1, 2, 3, 4)
print(f"t的新地址：{id(t)}")
