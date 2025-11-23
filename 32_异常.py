# 基本示例
# while True:
#     try:
#         x = int(input("请输入一个整数："))
#         y = 10 / x
#         print(f"结果：{y}")
#         break
#     except ValueError:
#         print("输入的不是有效整数")
#     except ZeroDivisionError:
#         print("不能除以0")

# exceptions = [
#     ("10 / 0", ZeroDivisionError),
#     ("int('abc')", ValueError),
#     ("'2' + 2", TypeError),
#     ("[1, 2, 3][10]", IndexError),
#     ("{'a': 1}['b']", KeyError),
#     ("'hello'.nonexistent_method()", AttributeError),
#     ("print(undefined_variable)", NameError),
#     ("open('nonexistent_file.txt')", FileNotFoundError)
# ]
#
# for code, expected_exception in exceptions:
#     try:
#         exec(code)
#     except expected_exception as e:
#         print(f"{code:30} -> {type(e).__name__}: {e}")

# 手动抛出异常
# def divide(a,b):
#     if b == 0:
#         raise ZeroDivisionError("除数不能为零")
#     return a / b
#
# try:
#     divide(10, 0)
# except ZeroDivisionError as e:
#     print(f"发生异常：{e}")

# 重新抛出异常：
# def process_data(data):
#     try:
#         number = int(data)
#         result = 100 / number
#         return result
#     except ValueError:
#         print("数据格式错误，记录日志...")
#         raise
#     except ZeroDivisionError:
#         print("除零错误，记录日志...")
#         raise
#
# try:
#     process_data('abc')
# except BaseException as e:
#     print(f"外层捕获错误：{e}")

# 异常链
# def process_file(filename):
#     try:
#         with open(filename) as f:
#             return f.read()
#     except FileNotFoundError as e:
#         raise RuntimeError("文件处理失败") from e
#
# try:
#     data = process_file('not_exist.txt')
# except RuntimeError as e:
#     print("捕获到业务异常：", e)
#     print(f"原始异常为：{e.__cause__}")

# # 自定义异常类
# class MyCustomError(Exception):
#     pass
#
# # 带参数的异常
# class DataFormatError(Exception):
#     def __init__(self, field,message):
#         self.field = field
#         self.message = message
#         super().__init__(f"{field} 格式错误：{message}")
# try:
#     raise DataFormatError("email", "缺少@符号")
# except DataFormatError as e:
#     print(f"字段：{e.field}, 错误：{e.message}")
#
# try:
#     # 某些操作，可能抛出自定义异常
#     raise MyCustomError("Something went wrong!")
# except MyCustomError as e:
#     print("捕获到自定义异常:", e)

# with处理异常
# class FileOpener:
#     def __init__(self,filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#     def __enter__(self):
#         try:
#             self.file = open(self.filename, self.mode)
#             print(f"文件已打开")
#             return self.file
#         except FileNotFoundError:
#             print(FileNotFoundError)
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#             print(f"文件已关闭")
#         if exc_type:
#             print(f"发生异常：{exc_type.__name__}:{exc_val}")
#             return False
# try:
#     with FileOpener("example1.txt", "r") as f:
#         # f.write("hello world\n")
#         # raise ValueError("人为制造的错误测试异常处理")
#         # f.write("这句话不会执行")
#         print(111)
# except Exception as e:
#     print(f"外部捕获的异常{e}")

# 异常日志记录
# import logging
# logging.basicConfig(level=logging.ERROR)
#
# class DatabaseError(Exception):
#     pass
#
# class ValidationError(Exception):
#     pass
#
# def get_user_from_db(user_id):
#     """根据用户ID从数据库获取用户信息"""
#     if user_id == 0:
#         raise DatabaseError("数据库连接失败")
#     return {"user_id": user_id, "name": "Test User", "age": 25}
# def validate_and_process(user_data):
#     if not user_data.get('name') or user_data.get('age') < 0:
#         raise ValidationError("用户信息无效")
#     user_data['processed'] = True
#     return user_data
# def process_user_data(user_id):
#     try:
#         user_data = get_user_from_db(user_id)
#         result = validate_and_process(user_data)
#         return result
#     except DatabaseError as e:
#         logging.error(f"数据库错误 - 用户ID: {user_id}, 错误: {e}")
#         raise
#     except ValidationError as e:
#         logging.warning(f"数据验证失败 - 用户ID: {user_id}, 错误: {e}")
#         return None
#     except Exception as e:
#         logging.critical(f"未知错误 - 用户ID: {user_id}, 错误: {e}")
#         raise
#
# process_user_data(0)

# 异常组
# def multiple_operations():
#     errors = []
#     try:
#         int('abc')
#     except ValueError as e:
#         errors.append(e)
#     try:
#         int('def')
#     except ValueError as e:
#         errors.append(e)
#     try:
#         1 / 0
#     except ZeroDivisionError as e:
#         errors.append(e)
#     if errors:
#         raise ExceptionGroup('多个操作失败', errors)
#
# try:
#     multiple_operations()
# except* ValueError as eg:
#     print("处理ValueError:")
#     for e in eg.exceptions:
#         print(f"  - {e}")
# except* ZeroDivisionError as eg:
#     print("处理ZeroDivisionError:")
#     for e in eg.exceptions:
#         print(f"  - {e}")

# import traceback
#
# try:
#     data = {"key": "value"}
#     print(data["noneexistent_key"])
# except Exception as e:
#     print(f"错误信息：{str(e)}")
#     print(f"错误类型：{type(e).__name__}")
#     print("追踪信息：")
#     print(traceback.print_exc())
#     tb_info = traceback.format_exc()
#     print("格式化堆栈：")
#     print(tb_info)
import time

# 方法1: 使用异常处理流程控制（不推荐）
def with_exceptions(n):
    results = []
    for i in range(n):
        try:
            if i % 2 == 0:
                raise ValueError("测试异常")
            results.append(i)
        except ValueError:
            pass
    return results

# 方法2: 使用条件判断（推荐）
def without_exceptions(n):
    results = []
    for i in range(n):
        if i % 2 != 0:
            results.append(i)
    return results

n = 10000

start = time.time()
with_exceptions(n)
exception_time = time.time() - start

start = time.time()
without_exceptions(n)
normal_time = time.time() - start

print(f"使用异常: {exception_time:.6f}秒")
print(f"使用条件: {normal_time:.6f}秒")
print(f"性能差异: {exception_time/normal_time:.2f}倍")