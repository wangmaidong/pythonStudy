# 创建集合
# 使用{}创建
# fruits = {"apple", "orange", "lemon"}
# numbers = {1, 2, 3, 4, True}
# mixed = {1, "Hello"}
# print(numbers, type(numbers))
#
# empty_set = set()
# print(empty_set, type(empty_set))
# print({}, type({}))

# 使用set()创建
# list_data = [1, 2, 3, 4, 5, 3, 2]
# set_from_list = set(list_data)
# print(set_from_list)
#
# str = "anbbhhhdd"
# set_from_str = set(str)
# print(set_from_str)
#
# tuple_data = (1, 2, 3, 3, 5)
# set_from_tuple = set(tuple_data)
# print(set_from_tuple)

# 集合式推到

# squares = {x for x in range(5)}
# print(squares)
# squares_even = {x for x in range(10) if x % 2 == 0}
# print(squares_even)

# 集合的基本操作

# # 添加元素
# fruits = {"apple", "orange"}
# fruits.add("lemon")
# print(fruits)
# fruits.add("apple")
# print(fruits)
#
# fruits.update(["pina", "mango"])
# print(fruits)
# fruits.update("abc")
# print(fruits)

# 删除元素
# fruits = {"apple", "banana", "cherry", "date"}
# fruits.remove("banana")
# # fruits.remove("wanglei")
# print(fruits)
#
# fruits.discard("cherry")
# fruits.discard("zhangsan")
# print(fruits)

# pop_item = fruits.pop()
# print(pop_item)
# empty_set = set()
# empty_set.pop()

# fruits.clear()
# print(fruits)

# 集合查询操作
# fruits = {"apple", "banana", "orange"}
# print("apple" in fruits)
# print("lemon" in fruits)
# print("lemon" not in fruits)
# print(len(fruits))
# numbers = {10, 4, 7, 2, 15}
# print(f"最大值：{max(numbers)}")
# print(f"最小值：{min(numbers)}")
#
# for n in enumerate(numbers):
#     print(n)

# 集合的数学运算

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union1 = set1.union(set2)
union2 = set1 | set2
print(union1)
print(union2)

set3 = {4, 7, 8, 1}
big_union = set1.union(set2, set3)
print(big_union)

intersection1 = set1.intersection(set2)
print(intersection1)
intersection2 = set1 & set2
print(intersection2)
intersection3 = set1 & set3
print(intersection3)

difference1 = set1.difference(set2)
difference2 = set1 - set2
print(difference1)
print(difference2)

sym_diff1 = set1.symmetric_difference(set2)
sym_diff2 = set1 ^ set2
print(sym_diff1)
print(sym_diff2)
