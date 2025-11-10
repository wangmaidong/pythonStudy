# 迭代器是python中用于遍历数据集合的工具，它提供了一种统一、高效的方式来访问各种数据结构的元素
# 迭代器：实现了 迭代协议  的  对象
# 迭代协议：__iter__  __next__
# 迭代器 VS 可迭代对象
# 可迭代对象：可以被迭代的对象
# 迭代器：实际执行迭代的对象

# from collections.abc import Iterable, Iterator
#
# numbers = [1, 2, 3, 4]
# print(isinstance(numbers, Iterable))
# print(isinstance(numbers, Iterator))
#
# # 通过iter()获取迭代器
# numbers_iterator = iter(numbers)
# print(isinstance(numbers_iterator, Iterator))
# # 通过list转换为可迭代对象
# print(list(numbers_iterator))
# # 只能使用一次 再次使用只能得到一个空数组
# print(list(numbers_iterator))
#
#
# # 实现一个迭代器
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = self.data[self.index]
#         self.index += 1
#         return value
#
#
# my_iter = MyIterator([1, 2, 3])
# print(type(my_iter))
# print(isinstance(my_iter, Iterator))
# print(isinstance(my_iter, Iterable))
# for item in my_iter:
#     print(item)
# my_iter2 = MyIterator(["a", "b", "c"])
# print(next(my_iter2))
# print(next(my_iter2))
# print(next(my_iter2))

# 创建迭代器的方法

# 方法一：实现一个迭代器类


# class Countdown:
#     def __init__(self, start):
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration
#         value = self.current
#         self.current -= 1
#         return value
#
#
# countdown = Countdown(5)
# for num in countdown:
#     print(num, end=" ")
#
# # 方法二 使用yield()生成器函数
#
# print("\n")
#
#
# def simple_gen():
#     """简单的生成器函数"""
#     print("First yield")
#     yield 1
#     print("Second yield")
#     yield 2
#
#
# g = simple_gen()
# print(next(g))
# print(next(g))
#
# for value in simple_gen():
#     print(value)
#
# # 方法三 使用生成器表达式
#
# squares = (x**2 for x in range(5))
# print(list(squares))
#
# even_squares = (x**2 for x in range(20) if x % 2 == 0)
# print(list(even_squares))
#
# gen = (x**2 for x in range(5) if x % 2 != 0)
# print(next(gen))
# print(next(gen))

# 内置迭代器工具

# iter() 和 next()
# 创建一个迭代器
# numbers = [1, 2, 3, 4, 5]
# iterator = iter(numbers)
# 手动获取元素
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator, "已经结束"))

# enumerate()
# colors = ["red", "green", "yellow"]
# for index, color in enumerate(colors, start=1):
#     print(f"{index}:{color}")

# zip() 可以并行迭代执行多个可迭代对象
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# cities = ["北京", "上海", "广州"]
# for name, age, city in zip(names, ages, cities):
#     print(f"姓名：{name} 年龄：{age} 城市：{city}")

# 可迭代对象的长度不同以最小的为标准

# 高级用法
# scores = [
#     (85, 92, 78),  # 张三的成绩
#     (76, 88, 95),  # 李四的成绩
#     (90, 85, 92),  # 王五的成绩
# ]
# chinese, english, math = zip(*scores)
# print(f"语文成绩：{chinese}")
# print(f"英语成绩：{english}")
# print(f"数学成绩：{math}")

# 与推导式结合

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = [x + y for x, y in zip(list1, list2)]
# print(result)

# 处理长度不同的序列
# from itertools import zip_longest
#
# a = [1, 2, 3]
# b = [4, 5]
#
# for x, y in zip_longest(a, b, fillvalue=0):
#     print(f"{x} + {y} = {x+y}")

# map() 映射迭代
# 基本用法
# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)
# print(next(squared))
# print(next(squared))
# print(list(squared))

# 类型转换
# nums = [10, 20, 30]
# str_list = map(str, nums)
# print(list(str_list))
# 多序列处理
# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 7]
# result = map(lambda x, y: x + y, list1, list2)
# print(list(result))


# 自定义函数
# def double(x):
#     return x * 2
#
#
# numbers = [5, 6, 7]
# doubled = map(double, numbers)
# print(list(doubled))

# filter() 过滤迭代

# 基本用法
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))


# 过滤假值
# data = ["hello", "", "python", None, {}, [], "Ai"]
# valid_data = filter(None, data)
# print(list(valid_data))
# 自定义函数
# def is_positive(x):
#     return x > 0
#
#
# numbers = [0, -1, 2, -3, 4]
# positive = filter(is_positive, numbers)
# print(list(positive))


# 复杂函数
# def is_valid_email(email):
#     return email and "@" in email and "." in email
#
#
# emails = ["user@example.com", "invalid", "test@domain.org", ""]
# valid_email = filter(is_valid_email, emails)
# print(list(valid_email))

# 自定义迭代器
# 范围迭代器

# class RangeIterator:
#     def __init__(self, start, stop=None, step=1):
#         if stop is None:
#             self.start = 0
#             self.stop = start
#         else:
#             self.start = start
#             self.stop = stop
#         self.step = step
#         self.current = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if (self.step > 0 and self.current >= self.stop) or (
#             self.step < 0 and self.current <= self.stop
#         ):
#             raise StopIteration
#         value = self.current
#         self.current += self.step
#         return value
#
#
# print("正步长：")
# for i in RangeIterator(5):
#     print(i, end=" ")
# print("\n负步长")
# for i in RangeIterator(7, 2, -2):
#     print(i, end=" ")


# 文件行迭代器
# class FilelineIterator:
#     def __init__(self, filename):
#         print("执行初始化")
#         self.filename = filename
#         self.file = None
#
#     def __iter__(self):
#         print("iter调用")
#         self.file = open(self.filename, "r", encoding="utf-8")
#         return self
#
#     def __next__(self):
#         if self.file is None:
#             raise RuntimeError("必须先调用 __iter__方法")
#         line = self.file.readline()
#         if not line:
#             self.file.close()
#             raise StopIteration
#         # 移除空白，并返回内容
#         return line.strip()
#
#     def __del__(self):
#         if self.file and not self.file.closed:
#             self.file.close()
#
#
# def process_file(filename):
#     for line in FilelineIterator(filename):
#         if line:
#             print(f"处理：{line}")
# process_file("example.txt")


# 树状结构迭代器
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []
#
#     def add_child(self, child):
#         self.children.append(child)
#
#
# class TreeIterator:
#     def __init__(self, root):
#         self.stack = [root] if root else []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not self.stack:
#             raise StopIteration
#         # 弹出当前节点
#         node = self.stack.pop()
#         for child in reversed(node.children):
#             self.stack.append(child)
#         return node.value
#
#
# root = TreeNode("A")
# b = TreeNode("B")
# c = TreeNode("C")
# d = TreeNode("D")
# e = TreeNode("E")
#
# root.add_child(b)
# root.add_child(c)
# b.add_child(d)
# b.add_child(e)
#
# print(root.children)
#
# for value in TreeIterator(root):
#     print(value, end=" ")

# 无限迭代器
# itertools
# from itertools import count, cycle, repeat, islice
#
# # 无限计数器
# counter = count(10, 2)
# print("Count", [next(counter) for _ in range(5)])
# print("isLice count", list(islice(counter, 5)))
# # cycle 循环遍历
# cycler = cycle(["A", "B"])
# print("Cycler", [next(cycler) for _ in range(5)])
# print("islice", list(islice(cycler, 5)))
# # repeat 重复元素
# repeater = repeat("hello", 3)
# # print("Repeater", list(repeater))
# print("islice", list(islice(repeater, 5)))
# # infinite 无限重复
# infinite = repeat("world")
# print("Infinite", [next(infinite) for _ in range(6)])
#
#
# # 自定义无限迭代器
# class InfiniteNumbers:
#     def __init__(self, start=0):
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self.current
#         self.current += 1
#         return value
#
#
# numbers = InfiniteNumbers(5)
# print([next(numbers) for _ in range(7)])
# # 配合 islice使用
# limited = islice(InfiniteNumbers(1), 10)
# print(list(limited))

# 迭代器链式操作

# 链式操作示例
# import itertools
#
#
# def process_data_pipeline(data):
#     """数据处理流水线"""
#     # 1.过滤正数
#     filtered = filter(lambda x: x > 0, data)
#     # 2.计算平方
#     squared = map(lambda x: x**2, filtered)
#     # 3.取前五个
#     limited = itertools.islice(squared, 5)
#     return limited
#
#
# data = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
# result = list(process_data_pipeline(data))
# print(result)
# result2 = itertools.islice(map(lambda x: x**2, filter(lambda x: x > 0, data)), 5)
# print(list(result2))

# 迭代器工具函数
# itertools常用函数
# chain() compress()
# import itertools
# from typing import Iterator
#
# chain_iter = itertools.chain([1, 2], [3, 4], [5, 6], (7, 8))
# print("Chain_iter", list(chain_iter))
# # 条件过滤
# data = ["A", "B", "C", "D"]
# selectors = [1, 0, 1, 0]
# compress_iter = itertools.compress(data, selectors)
# print("Compress", list(compress_iter))
#
# # dropwhile 丢弃开头满足条件的元素
# drop_iter = itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 1, 2])
# print("Dropwhile", list(drop_iter))
#
# # takewhile 获取开头满足条件的元素
# take_iter = itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 1, 2])
# print("Takewhile", list(take_iter))
#
# # groupby - 分组
# data = ["apple", "animal", "banana", "bird", "cherry", "cat"]
# sorted_data = sorted(data, key=lambda x: x[0])
# grouped = itertools.groupby(sorted_data, key=lambda x: x[0])
# for key, group in grouped:
#     print(f"{key}: {list(group)}")


# 实际应用场景
# 数据库查询结果处理
# class DatabaseQueryIterator:
#     def __init__(self, query, chunk_size=1000):
#         self.query = query
#         self.chunk_size = chunk_size
#         self.current_chunk = []
#         self.current_index = 0
#         self.has_more = True
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index >= len(self.current_chunk):
#             if not self.has_more:
#                 raise StopIteration
#             self._fetch_next_chunk()
#         if not self.current_chunk:
#             raise StopIteration
#
#         value = self.current_chunk[self.current_index]
#         self.current_index += 1
#         return value
#
#     def _fetch_next_chunk(self):
#         import random
#
#         if random.random() < 0.2:
#             self.has_more = False
#             self.current_chunk = []
#         else:
#             self.current_chunk = [f"record_{i}" for i in range(self.chunk_size)]
#         self.current_index = 0
#
#
# query_iter = DatabaseQueryIterator("SELECT * FROM large_table")
# for i, record in enumerate(query_iter):
#     if i >= 5000:
#         break
#     if i % 1000 == 0:
#         print(f"处理第{i}条数据")


# 流式数据处理
class StreamProcessor:
    """流式数据处理"""

    def __init__(self, data_stream):
        self.data_stream = data_stream

    def __iter__(self):
        return self

    def filter_valid(self):
        # 过滤有效数据
        return filter(lambda x: x is not None and x != "", self.data_stream)

    def transform_data(self):
        # 转换数据
        return map(str.upper, self.filter_valid())

    def batch_process(self, batch_size=1000):
        batch = []
        transform_data = self.transform_data()
        for item in transform_data:
            batch.append(item)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    def process(self):
        # 处理流水线
        total_processed = 0
        for batch in self.batch_process(3):
            total_processed += len(batch)
            print(f"处理批次：{batch}")
        print(f"总共处理：{total_processed} 条记录")


def data_stream():
    data = ["hello", "", "world", None, "python", "stream", "", "processing"]
    for item in data:
        yield item


processor = StreamProcessor(data_stream())
processor.process()

# 最佳实践
# 使用迭代器处理大数据集
