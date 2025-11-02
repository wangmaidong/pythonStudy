# 创建列表
# empty_list = []
# print(f"empty_list: {empty_list}")
#
# numbers = [1, 2, 3]
# fruits = ["apple", "orange", "banana"]
# mixed = [1, "Hello", True, {}]
# print(f"numbers: {numbers}")
# print(f"fruits: {fruits}")
# print(f"mixed: {mixed}")
# 使用 list()创建列表
# list_from_str = list("abc")
# print(f"list_from_str: {list_from_str}")
# list_from_tuple = list((1, 2, 3))
# print(f"list_from_tuple: {list_from_tuple}")
# another_empty_list = list()
# print(f"another_empty_list: {another_empty_list}")
from traceback import print_tb

# 访问列表元素
# 索引访问
# fruits = ["apple", "banana", "orange", "grape"]
# print(f"第一个元素：{fruits[0]}")
# print(f"第二个元素：{fruits[1]}")
# print(f"第三个元素：{fruits[2]}")
# try:
#     print(fruits[10])
# except IndexError:
#     print(f"访问超出元素出错： {IndexError}")

# # 切片访问
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # 开始索引，结束索引，步长默认为1
# print(numbers[2:5])
# # 只有开始，默认结束到列表末尾
# print(numbers[2])
# # 开始为负数，表示从右边倒数第几个开始
# print(numbers[-4:8])
# # 指定步长
# print(numbers[::2])
# # 从右到左打印
# print(numbers[::-1])
# # 创建的切片是新的
# sub_list = numbers[2:6]
# print(f"sub_list: {sub_list}")

# # 修改列表
# # 修改元素
# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "orange"
# print(f"修改后：{fruits}")
# # 添加元素
# fruits.append("lemon")
# print(fruits)
# fruits.insert(2, "grape")
# print(fruits)
# fruits.extend(["mango", "pineapple"])
# print(fruits)

# 删除元素
# remove
# people1 = ["张三", "李四", "王五", "赵六", "周七", "李四"]
# try:
#     print(people1.remove("李四"))
#     print(people1)
# except ValueError:
#     print(ValueError)
# # pop
# people2 = ["张三", "李四", "王五", "赵六", "周七", "李四"]
# try:
#     print(people2.pop(10))
#     print(people2)
# except IndexError:
#     print(IndexError)
# # del 索引不存在不会报错
# people3 = ["张三", "李四", "王五", "赵六", "周七", "李四"]
# try:
#     del people3[8:10]
#     print(people3)
# except IndexError:
#     print(IndexError)
#
# people4 = ["张三", "李四", "王五", "赵六", "周七", "李四"]
# people4.clear()
# print(people4)

# 列表操作与方法

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = list1 + list2
# print(f"列表合并：{combined}")
#
# repeated_list = list1 * 3
# print(f"重复列表：{repeated_list}")
#
# print(f" 1 in list1 : { 1 in list1}")
# print(f"4 in list1 : { 4 in list1}")
# print(f"combined的长度是：{len(combined)}")

# people = ["张三", "李四", "王五", "赵六", "周七", "李四"]
# print(f"index, 查找")
# print(people.index("李四", 4))
# print(f"统计 李四出现了： {people.count('李四1')} 次")
# people.sort()
# print(people)
# people.reverse()
# print(people)

# # 遍历列表
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"我是：{fruit}")
#
# for index, fruit in enumerate(fruits):
#     print(f"索引 {index} 对应的水果是：{fruit}")

# 列表推导式

nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]
print(f"squares: {squares}")
squares_even = [x**2 for x in nums if (x % 2 == 0)]
print(f"squares_even: {squares_even}")

fruits = ["Apple", "Banana", "cherry"]
fruits_lower = [fruit.lower() for fruit in fruits]
print(f"fruits_lower: {fruits_lower}")
