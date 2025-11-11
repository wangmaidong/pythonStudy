# 生成器是一种特殊的迭代器
# 惰性计算：按需生成值，不立即计算所有结果
# 内存高效：一次只处理一个值，不存储整个序列
# 可迭代：可以用在for循环中
# 保持状态：记住上次执行的位置
# 携程特性：支持双向通信，可以接受外部数据


# 创建生成器
# 生成器函数
# def my_generator():
#     """简单的生成器函数示例"""
#     print("第一步")
#     yield "A"
#     print("第二步")
#     yield "B"
#     print("第三步")
#     yield "C"
#
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# for value in my_generator():
#     print(f"获取到：{value}")
#     break

# 生成器表达式

# gen = (x**2 for x in range(5))
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 列表推导式 vs 生成器表达式

# numbers = [1, 2, 3, 4, 5]
# squares_list = [x**2 for x in numbers]
# print(squares_list)
# print(type(squares_list))
#
# squares_gen = (x**2 for x in numbers)
# print(squares_gen)
# print(type(squares_gen))

# for square in squares_gen:
#     print(square, end=" ")

# 生成器的工作原理
# 生成器本质上是一个特殊的迭代器
# 创建阶段：调用生成器函数时，函数体不会立即执行，而是返回生成器对象
# 驱动阶段：通过next()或者for循环驱动执行
# 暂停恢复：遇到yield暂停并返回值，下次从暂停出继续
# 结束阶段：函数执行完毕时抛出Stopiteration异常


# 示例
# def exampple_gen():
#     print("Step 1")
#     yield "A"
#     print("Step 2")
#     yield "B"
#     print("Step 3")
#     yield "C"
#
#
# gen = exampple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# 状态保持示例
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# fib = fibonacci_generator()
# for i in range(10):
#     print(next(fib), end=" ")
#

# 生成器方法
# send()向生成器发送值


# def simple_echo():
#     """简单的回声生成器"""
#     recived = yield "请给我一个值"
#     yield f"你发来的消息是：{recived}"
#
#
# gen = simple_echo()
# print(next(gen))
# print(gen.send("hello"))
#
#
# # throw()向生成器抛出异常
# def exception_generator():
#     try:
#         yield "开始"
#         yield "继续"
#         yield "结束"
#     except ValueError as e:
#         yield f"捕获异常：{e}"
#         yield "恢复执行"
#
#
# gen = exception_generator()
# print(next(gen))
# print(gen.throw(ValueError("测试异常")))
# print(next(gen))
#
#
# # print(next(gen))
# #
# # print(next(gen))
# # close() 关闭生成器
# def closeable_generator():
#     try:
#         yield "第一步"
#         yield "第二步"
#         yield "第三步"
#     except GeneratorExit:
#         print("生成器关闭，正在清理资源")
#         raise


# 实际应用场景


# 处理大文件
# def read_large_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()
#
#
# def process_log_file(file_path):
#     for line in read_large_file(file_path):
#         if "ERROR" in line:
#             yield line
#
#
# for error_line in process_log_file("huge_log_file.log"):
#     print(error_line)
#
#
# gen = closeable_generator()
# print(next(gen))
# gen.close()


# 数据管道
# def data_processing_pipeline(data):
#     """数据处理管道"""
#     # 过滤有效数据
#     valid_data = (item for item in data if item is not None)
#     # 转换数据
#     transformed_data = (str(item).upper() for item in valid_data)
#     # 添加序号
#     number_data = (f"{i}:{item}" for i, item in enumerate(transformed_data))
#     return number_data
#
#
# raw_data = [None, "hello", None, "world", "python", None]
# result = data_processing_pipeline(raw_data)
# for item in result:
#     print(item)


# 无限序列
# def prime_generator():
#     """生成质数的无限序列"""
#     primes = []
#     num = 2
#     while True:
#         is_prime = True
#         for prime in primes:
#             if prime * prime > num:
#                 break
#             if num % prime == 0:
#                 is_prime = False
#         if is_prime:
#             primes.append(num)
#             yield num
#         num += 1
#
#
# prime_gen = prime_generator()
# first_20_prime = [next(prime_gen) for _ in range(20)]
# print(first_20_prime)


# 高级生成器模式
# 生成器委托
# 原始写法
# def chain_generators_old(*iterables):
#     for iterable in iterables:
#         for item in iterable:
#             yield item
#
#
# def chain_generators(*iterables):
#     for iterable in iterables:
#         yield from iterable
#
#
# gen1 = (x for x in range(3))
# gen2 = (x for x in range(3, 6))
# gen3 = (x for x in range(6, 9))
#
# chained = chain_generators(gen1, gen2, gen3)
# print(list(chained))


# 协程模式
# def average_coroutine():
#     """协程模式：实时计算平均值"""
#     total = 0
#     count = 0
#     average = 0
#     while True:
#         value = yield average
#         if value is None:
#             break
#         total += value
#         count += 1
#         average = total / count
#
#     return average
#
#
# coro = average_coroutine()
# next(coro)
# print(coro.send(10))
# print(coro.send(20))
# print(coro.send(30))


# 生成器与迭代器
# class SquareIterator:
#     def __init__(self, n):
#         self.n = n
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.n:
#             raise StopIteration
#         result = self.current**2
#         self.current += 1
#         return result
#
#
# def square_generator(n):
#     for i in range(n):
#         yield i**2
#
#
# print("迭代器")
# for x in SquareIterator(5):
#     print(x, end=" ")
# print("\n生成器函数")
# for x in square_generator(5):
#     print(x, end=" ")

# 性能比较
# 内存使用对比

# import sys
#
#
# def using_list(n):
#     result = [i**2 for i in range(n)]
#     return result
#
#
# def using_generator(n):
#     result = (i**2 for i in range(n))
#     return result
#
#
# n = 1000000
# list_result = using_list(n)
# gen_result = using_generator(n)
#
# print(f"列表内存使用： {sys.getsizeof(list_result)} 字节")
# print(f"生成器内存使用： {sys.getsizeof(gen_result)} 字节")

# 实用示例


# def chunk_reader(file_path, chunk_size=1024):
#     """分块读取文件"""
#     with open(file_path, "r", encoding="utf-8") as file:
#         while True:
#             chunk = file.read(chunk_size)
#             if not chunk:
#                 break
#             yield chunk
#
#
# def batch_processor(data, batch_size=100):
#     batch = []
#     for item in data:
#         batch.append(item)
#         if len(batch) >= batch_size:
#             yield batch
#             batch = []
#     if batch:
#         yield batch
#
#
# def process_large_dataset(data_generator):
#     for batch in batch_processor(data_generator, batch_size=50):
#         print(f"处理批次，大小： {len(batch)}")
#         processed_batch = [item * 2 for item in batch]
#         yield from processed_batch
#
#
# # 使用示例
# data_generator = chunk_reader("huge_log_file.log")
# for item in process_large_dataset(data_generator):
#     print(item)


# 状态生成机器
def state_machine():
    """使用生成器实现状态机"""
    state = "开始"
    while True:
        if state == "开始":
            command = yield "状态: 开始 - 输入 '运行' 或 '退出'"
            if command == "运行":
                state = "运行中"
            elif command == "退出":
                state = "结束"

        elif state == "运行中":
            command = yield "状态: 运行中 - 输入 '暂停' 或 '停止'"
            if command == "暂停":
                state = "暂停"
            elif command == "停止":
                state = "开始"

        elif state == "暂停":
            command = yield "状态: 暂停 - 输入 '继续' 或 '停止'"
            if command == "继续":
                state = "运行中"
            elif command == "停止":
                state = "开始"

        elif state == "结束":
            return "程序结束"


machine = state_machine()
print(next(machine))
print(machine.send("运行"))
print(machine.send("暂停"))
print(machine.send("继续"))
print(machine.send("停止"))
