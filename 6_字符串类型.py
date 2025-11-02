# 字符串的基本概念
# str1 = "单引号字符串"
# str2 = "双引号" "字符串"
# str3 = """三引号
# 可以创建
# 多行文本"""
# str4 = """同样支持
# 多行文本"""

# print(str1)
# print(str2)
# print(str3)
# print(str4)
# print(type(str1))


# 字符串的转义字符
# print("转义字符演示：")
# print("换行：hello\nworld")
# print("制表符：Name\twanglei")
# print("反斜杠：路径：\\\\Users")
# print("单引号：I 'm wanglei")
# print('双引号："')

# raw_str = r"原始字符串: \n\t不会转义"
# print(raw_str)

# text = "Hello World"
# print("索引操作:")
# print(f"字符串: '{text}'")
# print(f"长度: {len(text)}")
# print(f"正索引 - text[0]: '{text[0]}'")  # H
# print(f"正索引 - text[6]: '{text[6]}'")  # P
# print(f"负索引 - text[-1]: '{text[-1]}'")  # n
# print(f"负索引 - text[-6]: '{text[-6]}'")  # P

# 索引越界会报错
# try:
#     print(text[20])
# except IndexError as e:
#     print(f"索引错误: {e}")

# text = "Hello Python Programming"
#       0123456789
# print("切片操作:")
# print(f"原始字符串：{text}")
# print(f"text[0:5]: '{text[0:5]}'")
# print(f"text[6:12]: '{text[6:12]}'")
# print(f"text[:5]: '{text[:5]}'")
# print(f"text[2:]: '{text[2:]}'")
# print(f"text[0:6:2]: '{text[0:6:2]}'")
# print(f"text[-11:]: '{text[-11:]}'")
# print(f"text[::2]: '{text[::2]}'")
# print(f"text[1::2]: '{text[1::2]}'")
# print(f"text[::-1]: '{text[-2::-1]}'")


# 字符串操作与方法
# text1 = "H-e-l-l-o-W-o-r-l-d"
# print(text1.split("-"))
# print(text1.rsplit("-"))

# text2 = " Hello World "
# print(f"去除空白：{text2.strip()}")
# print(f"去除左侧空白：{text2.lstrip()}")
# print(f"去除右侧空白：{text2.rstrip()}")

# text3 = "123456"
# text4 = "123456wl"
# text5 = "abcDER123@"

# text6 = "RRRAAKD"
# text7 = "abcg"

# text8 = "wl123"

# print(f"{text3}是否全是数字：{text3.isdigit()}")
# print(f"{text4}是否全部为字母：{text4.isalpha()}")
# print(f"{text5}是否全部为字母或数字：{text5.isalnum()}")
# print(f"{text6}是否全部为大写：{text6.isupper()}")
# print(f"{text7}是否全部为小写：{text7.islower()}")

# print(f"{text8}是否以wl开头：{text8.startswith('wl')}")

# 大小写转换

# text = "hello World of Python"
# print("大小写转换")
# print(f"原始：'{text}'")
# print(f"大写：'{text.upper()}'")
# print(f"小写：'{text.lower()}'")
# print(f"首字母大写：'{text.capitalize()}'")
# print(f"每个单词首字母大写：'{text.title()}'")
# print(f"大小写交换：'{text.swapcase()}'")

# print(f"是否全部大写：{text.isupper()}")
# print(f"是否全部小写：{text.islower()}")
# print(f"HELLO是否全部大写：{'HELLO'.isupper()}")

# 查找和替换

# text = "Hello World, Welcome To Python World"
# text1 = "Hello World, Welcome To Python World"
# text2 = "Hello World, Welcome To Python World"
# print("查找和替换")
# print(f"原始：'{text}'")
# print(f"查找 Python: {text.find('Python')}")
# print(f"从右侧查找 Python: {text.rfind('Python')}")
# print(f"统计World的出现次数：{text.count('World')}")
# print(f"全部替换World：{text1.replace('World', "Earth")}, 新的text1: {text1}")
# print(f"只替换第一个World：{text2.replace('World', "Earth", 1)} , 新的text2: {text2}")

# 去除空格和填充
# text = "   Hello World   "
# print("去除空格：")
# print(f"原始：|{text}|")
# print(f"去除两端空格：|{text.strip()}|")
# print(f"去除左端空格：|{text.lstrip()}|")
# print(f"去除右端空格：|{text.rstrip()}|")

# 定义一个包含特定字符（*）的字符串
# text2 = "***Hello World***"
#
# print(f"去除特定字符：|{text2.strip('*')}|")
#
# text3 = "Hello"
# print(f"居中：|{text3.center(20)}|")
# print(f"左对齐：|{text3.ljust(20)}|")
# print(f"右对齐：|{text3.rjust(20)}|")
# print(f"零填充：|{text3.zfill(20)}|")
# print(f"居中：|{text3.zfill(10)}|")

# 分割和连接

# csv_data = "apple,banana,orange,grape"
# sentence = "Hello World of Python"
# lines = "第一行\n第二行\n第三行"
#
# print("分割操作")
# print(f"CVS分割：{csv_data.split(',')}")
# print(f"句子分割：{sentence.split()}")
# print(f"限制分割：{sentence.split(' ', 2)}")
# print(f"从右限制分割：{sentence.rsplit(' ', 2)}")

# print(f"行分割：{lines.splitlines()}")
# 连接字符串
# fruits = ["apple", "banana", "orange"]
# print(f"连接：{'--'.join(fruits)}")
# print(f"连接：{','.join(fruits)}")

# 字符串编码
text = "Hello 世界 🐍"

print(f"原始字符串：{text}")

# 编码为字节
utf8_bytes = text.encode("utf-8")
gbk_bytes = text.encode("gbk", errors="ignore")

print(f"UTF-8字节：{utf8_bytes}")
print(f"GBk字节： {gbk_bytes}")

decode_utf8 = utf8_bytes.decode("utf-8")
decode_gbk = gbk_bytes.decode("gbk")

print(f"UTF8解码：{decode_utf8}")
print(f"GBK解码：{decode_gbk}")
