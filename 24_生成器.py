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


def simple_echo():
    """简单的回声生成器"""
    recived = yield "请给我一个值"
    yield f"你发来的消息是：{recived}"


gen = simple_echo()
print(next(gen))
print(gen.send("hello"))


# throw()向生成器抛出异常
def exception_generator():
    try:
        yield "开始"
        yield "继续"
        yield "结束"
    except ValueError as e:
        yield f"捕获异常：{e}"
        yield "恢复执行"


gen = exception_generator()
print(next(gen))
print(gen.throw(ValueError("测试异常")))
print(next(gen))


# print(next(gen))
#
# print(next(gen))
# close() 关闭生成器
def closeable_generator():
    try:
        yield "第一步"
        yield "第二步"
        yield "第三步"
    except GeneratorExit:
        print("生成器关闭，正在清理资源")
        raise


# 实际应用场景


# 处理大文件
def read_large_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def process_log_file(file_path):
    for line in read_large_file(file_path):
        if "ERROR" in line:
            yield line


for error_line in process_log_file("huge_log_file.log"):
    print(error_line)


gen = closeable_generator()
print(next(gen))
gen.close()
