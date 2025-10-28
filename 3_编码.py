# ASCII码

# text = "Hello"
# encoded = text.encode("ascii")
# print(encoded)
# print(encoded.hex())
# print("".join(f"\\x{b:02x}" for b in encoded))
# print(encoded.decode("ascii"))


# 本地化编码

# 中文GB2312/GBK编码示例
# text = "中国"
# gbk_encoded = text.encode("gbk")
# print(gbk_encoded)  # b'\xd6\xd0\xb9\xfa'

# unicode

# Unicode 字符集包含全球所有字符
# characters = [
#     "A",  # 拉丁字母
#     "中",  # 中文
#     "🍕",  # Emoji
#     "α",  # 希腊字母
#     "あ",  # 日文
# ]

# for char in characters:
#     print(f"字符: {char}, Unicode码点：U+{ord(char):04x}")

# UTF-8

# text = "Hello 世界"

# utf8_encode = text.encode("utf-8")
# print(f"utf-8编码：{utf8_encode}")
# print(f"长度： {len(utf8_encode)}字节")

# for char in text:
#     encoded_char = char.encode("utf-8")
#     print(f" '{char}' ---> {encoded_char} ({list(encoded_char)})")

# utf-16
# text = "Hello 世界"
# utf16_encoded = text.encode("utf-16")
# print(f"UTF-16编码：{utf16_encoded}")
# print(f"长度：{len(utf16_encoded)} 字节")


# UTF-32
# text = "Hello 世界"
# utf32_encoded = text.encode("utf-32")
# print(f"UTF-32编码: {utf32_encoded}")
# print(f"长度: {len(utf32_encoded)} 字节")

text = "A"
ascii_str = text.encode("ascii")
utf8_str = text.encode("utf-8")

print(f"A 在ASCII编码中对应的编码是{ascii_str}")
print(f"A 在UTF-8中对应的编码是{utf8_str}")
