"""mypackage包的初始文件"""

__version__ = "1.0.0"
__author__ = "王磊"

# 导入包中的模块 方便用户使用
from .module1 import function1
from .module2 import Class2

# 定义包级别的变量
package_variable = "这是包变量"

print("mypackage 包被导入")
print(__name__)
