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
with open("testfile/output.txt", "w", encoding="utf-8") as file:
    file.write("hello,world\n")
    file.write("This is a new line\n")


with open("testfile/output.txt", "a", encoding="utf-8") as file:
    file.write("This line is appended.\n")
