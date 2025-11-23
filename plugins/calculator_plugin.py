class BasicCalculatorPlugin:
    def __init__(self):
        self.name = "Basic Calculator"
        self.version = "1.0"

    def execute(self, operation, *args):
        if operation == "add":
            return sum(args)
        elif operation == "multiply":
            result = 1
            for num in args:
                result *= num
            return result
        else:
            return f"Unknown operation: {operation}"


# 确保类名以Plugin结尾
CalculatorPlugin = BasicCalculatorPlugin