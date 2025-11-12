# 可迭代对象
# 可迭代对象是实现了 __iter__()方法的对象，可以被用于 for 循环等迭代操作
# 核心特征：
# 实现了__iter__()方法
# 可以被用于for循环
# 不是迭代器，但可以生成迭代器
# 每次迭代都会创建一个新的迭代器

# 常见可迭代对象
# 内置可迭代对象
# string = "hello"
# lst = [1, 2, 3]
# tup = (1, 2, 3)
# dct = {"a": 1, "b": 2}
# st = {1, 2, 3}
#
# # 验证是否为可迭代对象
# from collections.abc import Iterable, Iterator
#
# print(isinstance(string, Iterable))
# print(isinstance(lst, Iterable))
# print(isinstance(string, Iterator))
#
#
# # 自定义可迭代对象
# class MyRangeIterator:
#     """实现一个自定义迭代器类"""
#
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.end:
#             val = self.current
#             self.current += 1
#             return val
#         else:
#             raise StopIteration
#
#
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return MyRangeIterator(self.start, self.end)
#
#
# # 使用示例
# my_range = MyRange(1, 5)
# for num in my_range:
#     print(num)
# for num in my_range:
#     print(num)
#
# list_data = [x for x in my_range]
# print(list_data)

# 迭代协议详解
# 协议定义
# 迭代协议是Python中支持迭代操作的核心机制，包含两个核心方法
# __iter__()返回迭代器对象
# __next__()返回下一个元素，没有时抛出StopIteration

# 迭代器执行流程
# 1.调用iter()获取迭代器
iterator = iter([1, 2, 3])
# 2.循环调用next()获取元素
# while True:
#     try:
#         item = next(iterator) # 相当于 iterator.__next__()
#         print(f"获取到元素：{item}")
#     except StopIteration:
#         print("迭代结束")
#         break

# 迭代器
# 定义和特点

# 迭代器是实现了 __iter__() 和 __next__()方法的的对象， 是迭代协议的核心实现

# 自定义迭代器


# class MyRangeIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.end:
#             val = self.current
#             self.current += 1
#             return val
#         else:
#             raise StopIteration
#
#
# iterator1 = MyRangeIterator(1, 4)
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))

# 迭代器 vs  可迭代对象

# lst 是一个可迭代对象，但不是迭代器，有__iter__ 没有 __next__
lst = [1, 2, 3]
print(hasattr(lst, "__iter__"))
print(hasattr(lst, "__next__"))

lst_iterator = iter(lst)
print(hasattr(lst_iterator, "__iter__"))
print(hasattr(lst_iterator, "__next__"))

# 验证类型
from collections.abc import Iterator

print(isinstance(lst_iterator, Iterator))
print(isinstance(lst, Iterator))
