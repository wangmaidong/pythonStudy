# 简单使用
# count = 1
# while count <= 10:
#     print(f"这是count的第{count}次循环")
#     count += 1

# 计算 1 到 100的和
# total = 0
# num = 1
# while num <= 100:
#     total += num
#     num += 1
# print(f"1到100的和是{total}")

# 用户输入验证
# while True:
#     user_input = input("请输入一个正整数：")
#     if user_input.isdigit() and int(user_input) > 0:
#         print(f"您输入的数字是：{user_input}")
#         break
#     else:
#         print("输入无效，请重新输入！")
# 处理列表数据
# 使用while循环遍历列表
# fruits = ["苹果", "香蕉", "橙子", "葡萄"]
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1

# num = 1
# while num <= 20:
#     if num == 5:
#         break
#     else:
#         print(num)
#         num += 1
# num = 0
# while num <= 5:
#     if num == 3:
#         num += 1
#         continue
#     else:
#         print(num)
#         num += 1

# while 循环后面可以跟一个else句子
# break 中断的循环体添加的 else 分支代码不会被执行， continue仍然可以执行
# count = 1
# while count <= 3:
#     print(f"循环第{count}次")
#     count += 1
# else:
#     print("不是break退出")

# 猜数字游戏
# import random
#
# secret_number = random.randint(1, 100)
# print(f"正确答案：{secret_number}")
# attempts = 0
# max_attempts = 7
# while attempts <= max_attempts:
#     user_input = input("请输入猜测的数字：")
#     if not user_input.isdigit():
#         print("请输入数字")
#         continue
#     user_input = int(user_input)
#     attempts += 1
#     if user_input == secret_number:
#         print(f"恭喜你在第{attempts}次猜中了答案")
#         break
#     elif user_input < secret_number:
#         print("太小了！")
#     elif user_input > secret_number:
#         print("太大了！")
# else:
#     print(f"游戏结束！正确答案是 {secret_number}")


# 菜单选择
# def show_menu():
#     print("\n===== 菜单系统 =====\n")
#     print("1. 查看信息")
#     print("2. 修改信息")
#     print("3. 退出系统")
#
#
# while True:
#     show_menu()
#     choice = input("请选择菜单")
#     if choice == "1":
#         print("显示信息.....")
#     elif choice == "2":
#         print("修改信息.....")
#     elif choice == "3":
#         print("退出系统")
#         break
#     else:
#         print("无效的输入，请重新输入！")

num = 0
while num < 5:
    num += 1
    if num == 3:
        break
    print(num)
else:
    print("我会被执行")
