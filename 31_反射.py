# 基本用法
# class Example:
#     def __init__(self):
#         self.value = 42
#
#
# example = Example()
#
# print(hasattr(example, "value"))
#
# # 获取属性值
# print(getattr(example, "value"))
#
# # 设置属性值
# setattr(example, "new_attr", "hello")
# print(example.new_attr)
# # 删除属性
# delattr(example, "new_attr")
# print("new_attr" in dir(example))
#
#
# # 安全的属性访问
# class Config:
#     def __init__(self):
#         self.host = "localhost"
#         self.port = 8080
#
#
# config = Config()
# timeout = getattr(config, "timeout", 30)
# print(f"Timeout:{timeout}")
#
# debug = getattr(config, "debug", False)
# print(f"Debug:{debug}")

# class Foo:
#     def __init__(self):
#         self.attr1 = "hello"
# class Bar(Foo):
#     def method1(self):
#         return "world"
#
# foo = Foo()
# bar = Bar()
#
# # 类型检查
# print(type(foo))
# print(isinstance(foo, Foo))
# print(isinstance(bar, Bar))
# print(isinstance(bar, Foo))
# print(issubclass(Bar, Foo))
#
# # 对象信息
# print(hasattr(foo,"attr1"))
# print(getattr(foo,"attr1"))
# print(vars(foo))
# print(dir(foo))

# def show_object_members(obj):
#     print(f"对象类型：{type(obj)}")
#     for attr in dir(obj):
#         if attr.startswith("__"):
#             continue
#         value = getattr(obj, attr)
#         if callable(value):
#             print(f"[方法]{attr}()")
#         else:
#             print(f"[属性]{attr} = {value}")
#
# show_object_members(123)

# 动态方法调用
# class ExampleObj:
#     def calculate(self, x,y):
#         return x + y
#
# obj = ExampleObj()
# method_name = "calculate"
# args = (3,5)
# if hasattr(obj, method_name):
#     method = getattr(obj, method_name)
#     if callable(method):
#         try:
#             result = method(*args)
#             print(f"Result: {result}")
#         except Exception as e:
#             print(f"调用方法{method_name}时发生异常：{e}")
#     else:
#         print(f"{method_name}不是可调用对象")
# else:
#     print(f"对象没有方法{method_name}")

# 带参数处理的方法调用
# class APIHandler:
#     def get_user(self,user_id,include_profile=False):
#         user = {"id": user_id, "name": f"User{user_id}"}
#         if include_profile:
#             user['profile'] = {"email": f"User{user_id}@qq.com"}
#         return user
#     def create_post(self,title,content, tags = None, published = True):
#         post = {
#             "title": title,
#             "content": content,
#             "tags": tags or [],
#             "published": published
#         }
#         return post
#
# def call_method_dynamically(obj, method_name,**kwargs):
#     if not hasattr(obj, method_name):
#         raise AttributeError(f"对象没有方法'{method_name}''")
#     method = getattr(obj, method_name)
#     if not callable(method):
#         raise TypeError(f"'{method_name}' 不是可调用的方法")
#     return method(**kwargs)
#
# handler = APIHandler()
# user_data = call_method_dynamically(handler, 'get_user', user_id = 123, include_profile=True)
# print(f"用户数据：{user_data}")
#
# post_data = call_method_dynamically(
#     handler,
#     'create_post',
#     title = "Python反射机制",
#     content = "反射机制详解",
#     tags = ["Python", "reflection"],
#     published = False
# )
# print("文章数据：", post_data )

# 类级别的反射
# class DatabaseModel:
#     table_name = "users"
#     connection_string = "sqlite:///database.db"
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     @classmethod
#     def get_table_info(cls):
#         return f"表名：{cls.table_name},链接：{cls.connection_string}"
#     @staticmethod
#     def validate_data(data):
#         return isinstance(data,dict)
#     def save(self):
#         return f"保存{self.name}到数据库"
#
# print("类属性：")
# print(f"table_name:{getattr(DatabaseModel,'table_name')}")
# print(f"connection_string:{getattr(DatabaseModel,'connection_string')}")
#
# # 动态修改类属性
# setattr(DatabaseModel, 'table_name', 'customers')
# print(f"修改后的表名：{DatabaseModel.table_name}")
# # 调用类方法
# class_method = getattr(DatabaseModel,'get_table_info')
# print(class_method())
# # 调用静态方法
# static_method = getattr(DatabaseModel, 'validate_data')
# print(static_method([12]))
# # 检查类成员
# print("\n检查类成员")
# print(f"有table_name:{hasattr(DatabaseModel,'table_name')}")
# print(f"有get_table_info:{hasattr(DatabaseModel, 'get_table_info')}")
# print(f"有save:{hasattr(DatabaseModel, 'save')}")

# 模块级别的反射
# import importlib
# module_name = "math"
# math_mod = importlib.import_module(module_name)
#
# print(math_mod)
# print(getattr(math_mod, "sqrt")(16))
#
# if hasattr(math_mod, "pow"):
#     pow_func = getattr(math_mod, "pow")
#     print(pow_func(2,8))

# 插件系统实现
# import os
# import importlib
#
#
# class PluginManager:
#     def __init__(self):
#         self.plugins = {}
#         self.load_plugins()
#
#     def load_plugins(self):
#         """动态加载所有插件"""
#         plugins_dir = "plugins"
#         for filename in os.listdir(plugins_dir):
#             if filename.endswith('.py') and not filename.startswith('_'):
#                 module_name = filename[:-3]  # 移除 .py
#                 try:
#                     # 动态导入模块
#                     module = importlib.import_module(f"{plugins_dir}.{module_name}")
#
#                     # 查找插件类（约定：以Plugin结尾的类）
#                     for attr_name in dir(module):
#                         attr = getattr(module, attr_name)
#                         if (isinstance(attr, type) and
#                                 attr_name.endswith('Plugin') and
#                                 attr_name != 'PluginManager'):
#                             plugin_instance = attr()
#                             self.plugins[plugin_instance.name] = plugin_instance
#                             print(f"加载插件: {plugin_instance.name} v{plugin_instance.version}")
#
#                 except Exception as e:
#                     print(f"加载插件 {module_name} 失败: {e}")
#
#     def execute_plugin(self, plugin_name, *args, **kwargs):
#         """执行插件"""
#         if plugin_name in self.plugins:
#             plugin = self.plugins[plugin_name]
#             return plugin.execute(*args, **kwargs)
#         else:
#             return f"Error: Plugin '{plugin_name}' not found"
#
#     def list_plugins(self):
#         """列出所有可用插件"""
#         return list(self.plugins.keys())


# 使用插件系统
# manager = PluginManager()
# print("可用插件:", manager.list_plugins())
#
# # 动态调用插件
# result1 = manager.execute_plugin("Basic Calculator", "add", 10, 5)
# result2 = manager.execute_plugin("Greeter", "Alice", formal=True)
#
# print("计算结果:", result1)  # 15
# print("问候结果:", result2)  # Good day, Alice. How may I assist you?

# 魔术方法和反射

# class DynamicAttributes:
#     """动态属性管理类"""
#     def __init__(self):
#         self._data = {}
#         self._access_count = {}
#
#     def __getattr__(self,name):
#         if name in self._data:
#             self._access_count[name] = self._access_count.get(name, 0) + 1
#             return self._data[name]
#         else:
#             raise AttributeError(f" '{type(self).__name__}' object has no attribute")
#     def __setattr__(self, name, value):
#         if name.startswith("_"):
#             super().__setattr__(name, value)
#         else:
#             if "_data" in self.__dict__:
#                 self._data[name] = value
#                 self._access_count[name] = 0
#             else:
#                 super().__setattr__(name,value)
#
#     def __delattr__(self, name):
#         if name in self._data:
#             del self._data[name]
#             del self._access_count[name]
#         else:
#             super().__delattr__(name)
#     def __dir__(self):
#         """自定义dir()输出"""
#         base_attrs = super().__dir__()
#         dynamic_attrs = list(self._data.keys())
#         return base_attrs + dynamic_attrs
#     def get_access_stats(self):
#         """返回访问字数统计表"""
#         return self._access_count.copy()
#
# obj = DynamicAttributes()
# obj.foo = 123
# obj.bar = 'hello'
#
# print(obj.foo)
# print(obj.bar)
# print(obj.foo)
# del obj.bar
# print(f"所有属性：{dir(obj)}")
# print(f"访问次数统计：{obj.get_access_stats()}")

# 配置管理系统
# class ConfigManager:
#     def __init__(self,config_dict=None):
#         self._config = config_dict or {}
#         self._defaults = {
#             "debug": False,
#             "host": "loaclhost",
#             "port": "8080",
#             "timeout": 30
#         }
#     def __getattr__(self, name):
#         if name in self._config:
#             return self._config[name]
#         elif name in self._defaults:
#             return self._defaults[name]
#         else:
#             raise AttributeError(f"配置项 '{name}' 不存在")
#     def set_config(self,**kwargs):
#         for key, value in kwargs.items():
#             self._config[key] = value
#     def show_config(self):
#         all_config = {**self._defaults, **self._config}
#         for key,value in sorted(all_config.items()):
#             source = "自定义" if key in self._config else "默认"
#             print(f"{key:20} = {value:15} [{source}]")
# config = ConfigManager()
# print(f"Host: {config.host}")
# print(f"Port: {config.port}")
# print(f"Debug: {config.debug}")
#
# config.set_config(host = "127.12.23.2", port = "8080", new_setting = 'custom')
# print("\n所有配置")
# config.show_config()

# API路由映射

# class APIController:
#     def get_user(self, user_id = None):
#         if user_id:
#             return f"获取用户 {user_id}"
#         return "获取所有用户"
#     def create_user(self, name, email):
#         return f"创建用户：{name} ({email})"
#     def update_user(self,user_id,**data):
#         return f"更新用户：{user_id}: {data}"
#     def delete_user(self, user_id):
#         return f"删除用户：{user_id}"
#
# class Router:
#     def __init__(self):
#         self.controller = APIController()
#     def route(self,method,path,**params):
#         path_parts = path.strip('/').split('/')
#         if path_parts[0] == 'users':
#             if method.upper() == "GET":
#                 action = 'get_user'
#                 if len(path_parts) > 1:
#                     params["user_id"] = path_parts[1]
#             elif method.upper() == "POST":
#                 action = "create_user"
#             elif method.upper() == "PUT" and len(path_parts) > 1:
#                 action = "update_user"
#                 params["user_id"] = path_parts[1]
#             elif method.upper() == "DELETE" and len(path_parts) > 1:
#                 action = "delete_user"
#                 params["user_id"] = path_parts[1]
#             else:
#                 return "Error: 无效的请求"
#
#             if hasattr(self.controller, action):
#                 method_to_call = getattr(self.controller, action)
#                 return method_to_call(**params)
#             else:
#                 return f"Error: 操作{action}不存在"
#         return "Error: 路径不存在"
#
# router = Router()
# requests = [
#     ('GET', '/users'),
#     ('GET', '/users/123'),
#     ('POST', '/users', {'name': 'Alice', 'email': 'alice@example.com'}),
#     ('PUT', '/users/123', {'name': 'Alice Smith'}),
#     ('DELETE', '/users/123')
# ]
# for method, path, *args in requests:
#     params = args[0] if args else {}
#     result = router.route(method, path, **params)
#     print(f"{method} {path} -> {result}")

import time

class Performance:
    def method(self):
        return "result"

obj = Performance()

# 测试直接方法调用与反射方法调用的性能差异
start = time.time()
for _ in range(100000):
    obj.method()
direct_time = time.time() - start

start = time.time()
for _ in range(100000):
    getattr(obj, 'method')()
reflect_time = time.time() - start

print(f"直接调用: {direct_time:.6f}s")
print(f"反射调用: {reflect_time:.6f}s")
print(f"性能差异: {reflect_time/direct_time:.2f}x")




