# 创建字典
# 使用花括号
# empty_dict = {}
# print(empty_dict)
#
# person = {"name": "Alice", "age": 30, "city": "杭州"}
# scores = {"math": 95, "English": 89}
#
#
# print(person)
# print(scores)

# 使用 dict

# dict1 = dict([("name", "BOb"), ("age", 18), ("city", "hangzhou")])
# print(dict1)
# dict2 = dict(name="charlie", age=18, city="杭州")
# print(dict2)
# dict3 = dict([["a", 1], ["b", 2]])
# print(dict3)
# keys = ["math", "english", "science"]
# default_score = 60
# score_dict = dict.fromkeys(keys, default_score)
# print(score_dict)
# empty_dict = dict.fromkeys(keys)
# print(empty_dict)

# 字典推导式
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)
#
# even_squares = {x: x**2 for x in range(1, 8) if x % 2 == 0}
# print(even_squares)
#
# original = {"a": 1, "b": 2, "c": 3}
# double = {k: v * 2 for k, v in original.items()}
# print(double)

# 访问字典元素
# person = {"name": "Alice", "age": 30, "city": "Beijing"}
# print(person["name"])
# print(person["age"])
#
# print(f"\n使用get()方法访问属性")
# print(person.get("name"))
# print(person.get("city"))
# print(person.get("country", "unknown"))
# # 使用setdefault()
# name = person.setdefault("name", "wangei")
# print(name)
# print(person)
#
# country = person.setdefault("country", "China")
# print(country)
# print(person)

# # 修改字典
#
# # 添加/删除字典
# person = {"name": "wanglei", "age": 18, "city": "杭州"}
# person["age"] = 30
# print(person)
#
# # 使用update进行更新
# person.update({"name": "lisi", "age": 20, "country": "China"})
# print(person)
#
# person.update([("job", "IT"), ("department", "wangxin")])
# print(person)
#
# person.update(salary=50000, tel=1589999)
# print(person)

# 删除元素
# person = {"name": "Alice", "age": 30, "city": "Beijing", "job": "Engineer"}
#
# del person["age"]
# print(f"删除 age : {person}")
#
# city = person.pop("city")
# print(f"pop删除city , {city}")
# print(person)
#
# last_item = person.popitem()
# print(f"popitem 删除：{last_item}")
# print(person)
#
#
# person.clear()
# print(person)

# 字典遍历

# person = {"name": "Alice", "age": 30, "city": "Beijing"}

# for key in person:
#     print(key)
#
# for key in person.keys():
#     print(f"Key: {key}")

# 遍历所有的值
# for value in person.values():
#     print(f"Value: {value}")

# for key, value in person.items():
#     print(f"{key} ---> {value}")
# 字典视图对象

# person = {"name": "Alice", "age": 30}
#
# keys_view = person.keys()
# values_view = person.values()
# items_view = person.items()
# print("修改前：")
# print(keys_view)
# print(values_view)
# print(items_view)
#
# person["city"] = "Beijing"
# person.update(name="wanglei")
# print("修改后")
#
# print(keys_view, type(keys_view))
# print(values_view)
# print(items_view)

# 字典的常用方法

# person = {"name": "Alice", "age": 30, "city": "Beijing"}
# print("name" in person)
# print("country" not in person)
#
# print(len(person))
#
# person_copy = person.copy()
# print(person_copy)
#
# new_dict = dict.fromkeys(["a", "b", "c"], 0)
# print(new_dict)
