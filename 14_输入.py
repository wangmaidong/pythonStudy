# 基本使用
# name = input()
# print(f"输入的name是： {name}")

# 带提示信息
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# print(f"你好! {name}, 你的年龄是：{age}")

# # 类型转换
# # 转换为整数
# age = int(input("请输入你的年龄："))
# print(f"年龄：{age}, 类型：{type(age)}")
# # 转换为浮点数
# height = float(input("请输入你的身高："))
# print(f"身高：{height}, 类型：{type(height)}")
# # 转换为布尔值
# is_student = input("你是学生吗？y/n").lower() == "y"
# print(f"类型：{type(is_student)}, 值：{is_student}")

# 基本的错误处理
# try:
#     age = int(input("请输入你的年龄："))
#     print(f"你的年龄是：{age}")
# except ValueError:
#     print("输入了错误的值！")

# 循环验证直到值正确
while True:
    try:
        age = int(input("请输入你的年龄："))
        if age < 0 or age > 150:
            print("输入的年龄范围不正确！")
            continue
        else:
            print(f"年龄是：{age}")
            break
    except ValueError:
        print("错误：请输入数字")
