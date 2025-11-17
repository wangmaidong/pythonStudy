# import mymodule as test
import importlib

# from mymodule import add,Calculator
# mymodule.hello()
# result = mymodule.add(1,2)
# calc = mymodule.Calculator()
# print(calc.multiply(2,3))
# print(result)

# import myproject.mypackage as mypackage
#
# mypackage.function1()

# 导入子包
# from myproject.mypackage.subpackage import module3

# 导入子包模块的成员
# from myproject.mypackage.subpackage.module3 import function3

# function3()
# 相对导入和绝对导入

# 绝对导入
# from myproject.mypackage.module1 import function1
# from myproject.mypackage.subpackage.module3 import function3

# 高级导入技巧

# 动态导入
# module_name = "math"
# math_module = __import__(module_name)
# print(math_module.sqrt(9))

# 使用importlib
# import importlib
#
# module = importlib.import_module("json")
# data = module.loads('{"a": 1}')
# print(data)

# 导入包内部模块
module_name = "myproject.mypackage.module1"
mod = importlib.import_module(module_name)
result = mod.function1()
print(result)
