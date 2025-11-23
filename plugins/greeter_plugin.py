class GreeterPlugin:
    def __init__(self):
        self.name = "Greeter"
        self.version = "1.0"

    def execute(self, name, formal=False):
        if formal:
            return f"Good day, {name}. How may I assist you?"
        else:
            return f"Hello, {name}! Nice to see you!"


# 确保类名以Plugin结尾
GreeterPlugin = GreeterPlugin