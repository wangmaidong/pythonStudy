# print("A","B","C", sep="--")
# print( "年", '月', '日', sep="---")
# print("1", "2", "3", sep="*")
# print("Hello", "world", sep="")
# print("Python", 'Java', 'C++', sep='|')

# print('第一行')
# print('第二行')


# print("第一行", end="--")
# print('第二行', end="!")
# print()

# print('加载中', end="")
# print('....', end="")
# print('完成', end="!")
# print()

# print("苹果", "香蕉", "橘子", "梨", sep=",", end="都是水果\n")

# print('姓名', '年龄', '城市', sep=' | ', end="\n---\n")
# print('张三', '25', "杭州", sep=" | ", end='\n')

# with open("output.txt", "w", encoding="utf-8") as f:
#     print("这里是写入文件的内容", file=f)
#     print("这里是第二行的内容", file=f)

# import sys

# print("这是一个错误", file=sys.stderr)

# with open("log.txt", "w", encoding="utf-8") as log_file:
#     message = "我是信息"
#     print(message)
#     print(message, file=log_file)

# f-string
name = "Bob"
age = 20
score = 95.567

# print(f"姓名：{name}, age： {age}")

# print(f"明年年龄：{age + 1}")
# print(f"分数翻倍：{score * 2}")

# print(f"分数：{score:.1f}")
# print(f"分数：{score:.2f}")

# print(f"{name:>10}")
# print(f"{name:<10}")
# print(f"{name:^10}")

# print(f"十进制：{age}，十六进制：{age:x}，二进制：{age:b}")

# format()

# print("姓名：{}，年龄{}".format(name, age))
# print("{1}的年龄是{0}岁".format(age, name))

# print("姓名：{n}，年龄：{a}".format(n=name, a=age))


# print("分数：{:.2f}".format(score))
# print("十进制：{0}，十六进制：{0:x}，二进制：{0:b}".format(age))

# print("姓名：{:<2}，年龄：{:>10}".format(name, age))

# %格式化

# print("姓名：%s,年龄：%d,成绩：%.2f" % (name, age, score))
i = 20
print("王磊", "学习", "python")
print("222", end="")
print(f"\r进度：{i}%")
