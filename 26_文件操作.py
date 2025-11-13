# 文件操作
# 只读模式打开文本文件
# file = open("testfile/data.txt", "r", encoding="utf-8")
# 写入模式打开文件
# file_w = open("testfile/output.txt", "w", encoding="utf-8")
# 二级制模式打开文件
# file_rb = open("testfile/flower.png", "rb")
# print(file)
# print(file_w)
# print(file_rb)
import json

# 读取文件的方法
# with open("testfile/data.txt", "r", encoding="utf-8") as file:
#     # content = file.read()
#     # print(content)
#     print(file.readline())
#     print(file.readline())

# 逐行读取
# with open("testfile/data.txt", "r", encoding="utf-8") as file:
#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()

# with open("testfile/data.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print(lines)
#     for line in lines:
#         print(line.strip())
#
# with open("testfile/data.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# 读取指定字节数
# with open("testfile/data.txt", "r", encoding="utf-8") as file:
#     for i in range(8):
#         chunk = file.read(5)
#         print(chunk.strip())
# 分块读取大文件
# with open("testfile/data.txt", "r", encoding="utf-8") as file:
#     while True:
#         chunk = file.read(20)
#         if not chunk:
#             break
#         print(chunk)

# 分块读取二进制文件
# with open("testfile/flower.png", "rb") as file:
#     chunk = file.read(1024)
#     print(chunk)

# 写入文件
# with open("testfile/output.txt", "w", encoding="utf-8") as file:
#     file.write("hello,world\n")
#     file.write("This is a new line\n")
#
#
# with open("testfile/output.txt", "a", encoding="utf-8") as file:
#     file.write("This line is appended.\n")
# # 批量写入字符串
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
#
# with open("testfile/output.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)
#
# with open("testfile/output.txt", "w", encoding="utf-8") as file:
#     for line in lines:
#         file.write(line)

# 文件位置操作
# tell()是返回的是字节的位置
# with open("testfile/data.txt", "r", encoding="utf-8") as file:
#     print(f"初始位置：{file.tell()}")
#     content = file.read(5)
#     print(f"读取后位置：{file.tell()}")

# 移动文件指针
# with open("testfile/data.txt", "rb") as file:
#     file.seek(0)
#     print(f"位置：{file.tell()}")
#
#     file.seek(10)
#     print(f"位置：{file.tell()}")
#
#     file.seek(5, 1)
#     print(f"位置：{file.tell()}")
#     file.seek(-10, 2)
#     print(f"位置：{file.tell()}")

# 文件属性检查

# 基本属性检查
import os
from base64 import encode

if os.path.exists("demo.txt"):
    print("文件存在")
else:
    print("文件不存在")

if os.path.isfile("testfile/data.txt"):
    print("是文件")
if os.path.isdir("testfile"):
    print("是目录")

size = os.path.getsize("testfile/flower.png")
print(f"文件大小是：{size}")

# 详细属性信息
from datetime import datetime

info = os.stat("testfile/data.txt")
print(f"文件大小：{info.st_size}")
print(f"创建时间：{datetime.fromtimestamp(info.st_ctime)}")
print(f"最后访问：{datetime.fromtimestamp(info.st_atime)}")
print(f"最后修改：{datetime.fromtimestamp(info.st_mtime)}")
print(f"文件权限：{oct(info.st_mode)}")

# 处理不同类型的文件
# csv文件
import csv

with open("testfile/test.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["姓名", "年龄", "城市"])  # 写入表头
    writer.writerow(["张三", "25", "北京"])  # 写入数据
    writer.writerow(["李四", "30", "上海"])
# 读取csv文件

with open("testfile/test.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# 读写JSON文件
data = {"name": "张三", "age": 25, "cities": ["北京", "上海", "广州"]}
with open("testfile/test.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

with open("testfile/test.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print(loaded_data)
