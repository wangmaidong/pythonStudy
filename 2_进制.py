# 十进制
# dec_num = 100
# print("dec_num", dec_num)

# # 二进制
# bin_num = 0b1100100
# print("bin_num", bin_num)

# # 八进制
# oct_num = 0o144
# print("oct_num", oct_num)

# # 十六进制
# hex_num = 0x64
# print("hex_num", hex_num)


# 进制函数转换

# num = 255

# bin_str = bin(num)
# oct_str = oct(num)
# hex_str = hex(num)


# print(f"二进制：{bin_str}")
# print(f"八进制：{oct_str}")
# print(f"十六进制：{hex_str}")

# 将字符串转换为十进制整数

# binary_string = "0b11111111"

# print(f"二进制 {binary_string} 转换为十进制是 {int(binary_string, 2)}")

# octal_string = "377"
# print(f"八进制 {octal_string} 转换为十进制是{int(octal_string, 8)}")

# hex_string = "ff"
# print(f"十六进制 {hex_string} 转换为十进制是 {int(hex_string, 16)}")

# 进制转换函数

# num = 255
# bin_str = bin(num)
# oct_str = oct(num)
# hex_str = hex(num)

# print(f"十进制{num}")
# print(f"二进制{bin_str}")
# print(f"八进制{oct_str}")
# print(f"十六进制{hex_str}")

# 处理颜色值
# red_hex = "#FF0000"

# red_component = int(red_hex[1:3], 16)
# green_component = int(red_hex[3:5], 16)
# blue_component = int(red_hex[5:7], 16)

# print(f"颜色{red_hex}的RGB分量为：")
# print(f"R：{red_component}")
# print(f"G:{green_component}")
# print(f"B:{blue_component}")

# 格式化输出

num = 42

hex_with_prefix = hex(num)
print(hex_with_prefix)

hex_without_prefix = hex_with_prefix[2:4]
print(hex_without_prefix)

hex_without_prefix1 = f"{num:x}"
hex_without_prefix2 = f"{num:X}"
bin_without_prfix = f"{num:b}"

print(hex_without_prefix1)
print(hex_without_prefix2)
print(bin_without_prfix)
