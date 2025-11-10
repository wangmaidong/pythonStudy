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

numbers = [1, 2, 3, 4, 5]
squares_list = [x**2 for x in numbers]
print(squares_list)
print(type(squares_list))

squares_gen = (x**2 for x in numbers)
print(squares_gen)
print(type(squares_gen))

for square in squares_gen:
    print(square, end=" ")
