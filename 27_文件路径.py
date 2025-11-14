# 主要使用os.path模块和 pathlib模块
# 导入必要模块
import os  # 操作系统接口
import os.path  # 传统路径操作
from pathlib import Path  # 文件通配符搜索
import shutil  # 高级文件操作

# 传统路径操作
# 路径拼接

# path_list = ["父文件夹", "子文件夹", "文件.txt"]
# full_path = os.path.join(*path_list)
# print(full_path)

# 获取文件名和目录名
# path = "/home/user/documents/file.txt"
# print(os.path.basename(path))
# print(os.path.dirname(path))
# print(os.path.split(path))

# 分离扩展名
# name, ext = os.path.splitext("example.tar.gz")
# print(name)
# print(ext)
# 获取文件的绝对路径
# print(os.path.abspath("testfile/data.txt"))
# print(os.path.realpath("testfile/data.txt"))
# 检查路径和属性

path = "/home/user/documents"
print(os.path.exists(path))
print(os.path.isfile("testfile/data.txt"))
print(os.path.isdir("testfile"))
print(os.path.islink(path))

if os.path.isfile("testfile/data.txt"):
    print(f"文件大小：{os.path.getsize("testfile/data.txt")}字节")
    print(f"修改时间：{os.path.getatime("testfile/data.txt")}")


# pathlib 模块 -现代路径操作

# 创建路径对象

path1 = Path("testfile/data.txt")
path2 = Path("relative/path")
path3 = Path.cwd()
path4 = Path.home()

print(f"绝对路径：{path1}")
print(f"相对路径：{path2}")
print(f"当前目录：{path3}")
print(f"用户主目录：{path4}")

# 路径属性和方法
# 基本属性
# p = Path("E:\study\Ai\pythonStudy\\testfile\data.txt")
# print(f"完整路径：{p}")
# print(f"文件名：{p.name}")
# print(f"文件名（无后缀）：{p.stem}")
# print(f"扩展名：{p.suffix}")
# print(f"父路径：{p.parent}")
# print(f"磁盘/锚：{p.anchor}")
#
# p1 = Path("testfile/output.txt")
# print(f"替换文件名：{p.with_name('output1.txt')}")
# print(f"替换扩展名：{p.with_suffix('.md')}")
#
# # 路经检查
# print(f"是否存在：{p.exists()}")
# print(f"是否为文件：{p.is_file()}")
# print(f"是否为目录：{p.is_dir()}")
# print(f"是否位绝对路径：{p.is_absolute()}")
# print(f"绝对路径：{p1.resolve()}")
#
# # 安全获取文件信息
# if p.is_file():
#     stat = p.stat()
#     print(f"文件大小：{stat.st_size}")
#     print(f"最后修改：{stat.st_mtime}")
# else:
#     print("不是文件，无法获取大小和时间")

# 路径遍历和文件操作

# folder = Path("testfile")
# for item in folder.iterdir():
#     print(item)
# folder1 = Path("../pythonStudy")
# for py_file in folder1.rglob("*.py"):
#     print(py_file)

# 目录创建
