# 导入包中的特定模块
from mypackage.module1 import function1

print(function1())

# 导入包中的特定函数/类

from mypackage.module2 import Class2

obj = Class2(34)
print(obj.display())

# 导入子包中的模块

from mypackage.subpackage import module3

print(module3.function3())

# 使用__init__.py 中导入的内容
from mypackage import function1

print(f"使用mypackage 的__init__.py 中导入的内容：{function1()} ")

# 导入包变量

import mypackage

print(mypackage.package_variable)
