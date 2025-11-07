# 列表推导式
# 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"even_squares: {even_squares}")
# 多个条件
numbers = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(numbers)
# 条件表达式（三元运算符）
results = [x if x % 2 == 0 else "add" for x in range(10)]
print(results)
