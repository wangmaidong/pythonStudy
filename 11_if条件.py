# 判断是不是闰年
def is_r_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return f"{year}是闰年"
    else:
        return f"{year}不是闰年"


print(is_r_year(2025))
print(is_r_year(2000))
