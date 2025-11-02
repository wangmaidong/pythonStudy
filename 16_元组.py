# 空元组
# empty_tuple = ()
# print(f"空元组 empty_tuple: {empty_tuple} , 类型：{type(empty_tuple)}")
#
# numbers = (1, 2, 3, 4, 5, 6)
# fruits = ("apple", "orange", "banana")
# mixed = (1, "hello", 3.14, None)
#
# print(numbers)
# print(fruits)
# print(mixed)

# 使用tuple()函数

# list_data = [1, 2, 3]
# list_tuple = tuple(list_data)
# print(list_tuple)
#
# tuple_from_str = tuple("abc")
# print(tuple_from_str)
#
# another_empty_tuple = tuple()
# print(another_empty_tuple)

# 单个元素的元组

# not_a_tuple = 42
# print(f"{not_a_tuple}, {type(not_a_tuple)}")
#
# a_tuple = (42,)
# print(f"{a_tuple}, {type(a_tuple)}")
#
# another_a_tuple = (42,)
# print(f"{another_a_tuple}, {type(another_a_tuple)}")

# 访问元组的元素

# fruits = ("apple", "banana", "orange", "grape")
#
# for index, fruit in enumerate(fruits):
#     print(f"索引 {index} 对应的水果是：{fruits[index]}")
#
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(numbers[2:5])
# print(numbers[3:])
# print(numbers[2:4:2])
# print(numbers[::3])
# print(numbers[50::2])
# print(numbers[::-1])
#
# list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_numbers[50:])

# 如何"修改"元组

# fruits = ("apple", "orange", "banana")
# print(fruits)
#
# new_fruits = fruits[0:1] + ("blueberry",) + fruits[2:]
# print(new_fruits)

# 常用操作

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# combined = tuple1 + tuple2
#
# print(combined)
#
# repeated_tuple = tuple1 * 3
# print(repeated_tuple)
#
# fruits = ("apple", "banana")
# print(f"apple in fruits : {"apple" in fruits}")
# print(f"orange in fruits: { "orange" not in fruits}")
#
# print(len(fruits))

# 内置方法 count 和 index
# numbers = (1, 2, 3, 2, 4, 2, 5)
# numbers_list = [1, 2, 3, 2, 4, 2, 5]
# print(numbers.count(2))
# print(numbers.index(4))

# # 数据安全
#
# CONFIG = ("localhost", 8080, "/api/v1")
#
#
# def connect_to_server():
#     host, port, endpoint = CONFIG
#     print(f"连接到{host}:{port}{endpoint}")
#
#
# connect_to_server()
#
# # 作为字典的键
# coordinates_map = {(40.718, -74.0060): "NewYork", (34.0522, -118.2437): "Los Angeles"}
# print(coordinates_map[(40.718, -74.0060)])
#
#
# def get_user_info():
#     name = "wanglei"
#     age = 35
#     city = "hangzhou"
#     return name, age, city
#
#
# result_info = get_user_info()
# print(result_info)
# print(type(result_info))
# name, age, city = result_info
# print(f"{age}岁的{name}住在{city}")

# 元组的解包
person = ("Alice", 35, "杭州")
name, age, city = person

numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers
print(first)
print(second)
print(rest, type(rest))

a, b = 10, 20
a, b = b, a
print(a, b)
