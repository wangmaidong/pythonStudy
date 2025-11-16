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

# path = "/home/user/documents"
# print(os.path.exists(path))
# print(os.path.isfile("testfile/data.txt"))
# print(os.path.isdir("testfile"))
# print(os.path.islink(path))
#
# if os.path.isfile("testfile/data.txt"):
#     print(f"文件大小：{os.path.getsize("testfile/data.txt")}字节")
#     print(f"修改时间：{os.path.getatime("testfile/data.txt")}")
#
#
# # pathlib 模块 -现代路径操作
#
# # 创建路径对象
#
# path1 = Path("testfile/data.txt")
# path2 = Path("relative/path")
# path3 = Path.cwd()
# path4 = Path.home()
#
# print(f"绝对路径：{path1}")
# print(f"相对路径：{path2}")
# print(f"当前目录：{path3}")
# print(f"用户主目录：{path4}")

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
# new_folder = Path("new_directory")
# new_folder.mkdir(exist_ok=True)

# 创建多级目录
# deep_folder = Path("level1/level2/level3")
# deep_folder.mkdir(parents=True, exist_ok=True)

# 常用路径操作
# 获取当前目录信息

# current_dir = os.getcwd()
# print(f"当前工作目录：{current_dir}")
# 使用pathlib获取当前目录

# current_path = Path.cwd()
# print(f"当前路径：{current_path}")

# 获取用户主目录
# home_dir = Path.home()
# print(f"用户主目录：{home_dir}")


# 路径规范化
# 处理相对路径和符号链接
# path = Path("../../Documents/../file.txt")
# print(f"原始路径：{path}")
# print(f"解析后路径：{path.resolve()}")
#
# base_path = Path('/home/user/documents')
# target_path = Path("/home/user/documents/work/project/file.txt")
# resolve_path = target_path.relative_to(base_path)
# print(f"相对路径：{resolve_path}")

# paths = [
# '/home/user/documents/report.pdf',
#     'relative/path/file.txt',
#     '../parent/file.py',
#     'file_no_extension',
#     'archive.tar.gz'
# ]
# for path_str in paths:
#     path = Path(path_str)
#     print(f"\n分析路径：{path}")
#     print(f"文件名：{path.name}")
#     print(f"主干名：{path.stem}")
#     print(f"扩展名：{path.suffix}")
#     print(f"父目录：{path.parent}")
#     print(f"是否为绝对路径：{path.is_absolute()}")

# file_path = Path('test.txt')
# file_path.write_text("hello world", encoding="utf-8")
#
# content = file_path.read_text(encoding="utf-8")
# print(content)
#
# if file_path.exists():
#     stat = file_path.stat()
#     print(f"文件大小：{stat.st_size}")
#     print(f"最后修改时间：{stat.st_mtime}")
#
# new_path = file_path.rename("new_test.txt")
# import shutil
# Path("example_dir").mkdir(exist_ok=True)
# shutil.copytree("example_dir", "copy_dir", dirs_exist_ok=True)

# 操作系统检测
if os.name == "nt":
    path = Path("C:/Users/Name/Documents")
else:
    path = Path('/home/name/documents')

file_path = path / 'subfolder' / "file.txt"
print(f"文件路径：{file_path},类型：{type(file_path)}")

path_str = str(file_path)
print(f"字符串路径：{path_str}")
