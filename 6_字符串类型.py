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
text1 = "H-e-l-l-o-W-o-r-l-d"
print(text1.split("-"))
print(text1.rsplit("-"))

text2 = " Hello World "
print(f"去除空白：{text2.strip()}")
print(f"去除左侧空白：{text2.lstrip()}")
print(f"去除右侧空白：{text2.rstrip()}")

text3 = "123456"
text4 = "123456wl"
text5 = "abcDER123@"

text6 = "RRRAAKD"
text7 = "abcg"

text8 = "wl123"

print(f"{text3}是否全是数字：{text3.isdigit()}")
print(f"{text4}是否全部为字母：{text4.isalpha()}")
print(f"{text5}是否全部为字母或数字：{text5.isalnum()}")
print(f"{text6}是否全部为大写：{text6.isupper()}")
print(f"{text7}是否全部为小写：{text7.islower()}")

print(f"{text8}是否以wl开头：{text8.startswith('wl')}")
