# 基本用法
class Example:
    def __init__(self):
        self.value = 42


example = Example()

print(hasattr(example, "value"))

# 获取属性值
print(getattr(example, "value"))

# 设置属性值
setattr(example, "new_attr", "hello")
print(example.new_attr)
# 删除属性
delattr(example, "new_attr")
print("new_attr" in dir(example))


# 安全的属性访问
class Config:
    def __init__(self):
        self.host = "localhost"
        self.port = 8080


config = Config()
timeout = getattr(config, "timeout", 30)
print(f"Timeout:{timeout}")

debug = getattr(config, "debug", False)
print(f"Debug:{debug}")
