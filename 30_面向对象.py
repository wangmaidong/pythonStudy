# 定义类和创建对象
# __init__是构造方法，创建对象是自动调用，用于初始化对象属性
# self 代表当前对象本身，所有在类的方法中都必须写上（调用时不用传）


# class Student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def introduce(self):
#         print(f"我是{self.name},年龄是{self.age}岁,分数{self.score}")
#
#     def is_pass(self):
#         return self.score >= 60
#
#
# # 创建一个学生对象
# stu1 = Student("Alice", 20, 85)
# stu1.introduce()
# print(stu1.is_pass())
#
#
# # 实例属性 vs 类属性
# class Dog:
#     species = "狗"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# dog1 = Dog("Buddy", 2)
# dog2 = Dog("Lucy", 5)
# print(dog1.name, dog2.name)
# print(dog1.species, dog2.species)
#
# dog1.age = 4
# print(dog1.age, dog2.age)
#
# Dog.species = "Dog"
# print(dog1.species, dog2.species)
# # 如果通过实例修改类属性，只会为该实例新创建同名实例属性
# dog1.species = "wolf"
# print(dog1.species)
# print(dog2.species)
# print(Dog.species)


# 属性访问控制
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self._nickname = name
#         self.__realname = name
#
#
# stu = Student("小明")
# # 公开属性直接访问
# print(stu.name)
# stu.name = "小红"
# print(stu.name)
# # 受保护属性（实际能访问，约定不要在类外访问）
# print(stu._nickname)
# stu._nickname = "小亮"
# print(stu._nickname)


# print(stu.__realname)
# Python 内部会将 __age 自动改名为 _类名__age，所以stu._Student__age是可以访问的，但强烈不推荐这么做。
# print(stu._Student__realname)
# 使用属性装饰器
# class Demo:
#     def __init__(self, value):
#         self._value = value
#
#     # 定义value属性的getter方法
#     @property
#     def value(self):
#         return self._value
#
#     # 定义value属性的setter方法
#     @value.setter
#     def value(self, new_value):
#         if isinstance(new_value, int) and new_value >= 0:
#             self._value = new_value
#         else:
#             raise ValueError("value必须为负整数")
#
#
# demo = Demo(5)
# print(demo.value)
# demo.value = 12
# # demo.value = -3
#
#
# # 只读属性
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def area(self):
#         return 3.14 * self._radius**2
#
#
# c = Circle(2)
# print(c.area)
# c.area = 10


# 继承
# 基本继承
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         # 父类只定义接口/默认实现，一般由子类重写
#         raise NotImplementedError("子类必须实现speak方法")
#
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name}: 汪汪"
#
#
# class Cat(Animal):
#     def run(self):
#         print(f"{self.name}在跑")
#
#     def speak(self):
#         return f"{self.name}: 喵喵"
#
#
# dog = Dog("小黑")
# cat = Cat("小花")
#
# print(dog.speak())
# print(cat.speak())
# super 使用
# super().__init__()
# super().方法名

# class Animal:
#     def __init__(self,name):
#         self.name = name
#
# class Bird(Animal):
#     def __init__(self,name,can_fly=True):
#         super().__init__(name)
#         self.can_fly = can_fly


# 多重继承
# class A:
#     def foo(self):
#         print("A.foo")
#
#
# class B:
#     def bar(self):
#         print("B.bar")
#
#
# class C(A, B):
#     pass
#
#
# c = C()
# c.foo()
# c.bar()

# 多态
import math


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius**2
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
#
# def print_shape_info(shape):
#     print(f"面积：{shape.area():.2f}")
#     print(f"周长：{shape.perimeter():.2f}")
#
#
# shapes = [Rectangle(3, 4), Circle(5)]
#
# for s in shapes:
#     print_shape_info(s)


# class Demo:
#     def __new__(cls, *args, **kwargs):
#         print(f"__new__called: 分配对象空间， cls = {cls}")
#         instance = super().__new__(cls)
#         return instance
#
#     def __init__(self, value):
#         print(f"__init__called: 初始化对象，设置 value = {value}")
#         self.value = value
#
#
# print("创建 Demo 对象：")
# d = Demo(42)
# print(f"对象属性 value = {d.value}")


# 综合示例
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Vector({self.x},{self.y})"
#
#     def __repr__(self):
#         return f"Vector({self.x},{self.y})"
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar)
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def magnitude(self):
#         return (self.x**2 + self.y**2) ** 0.5
#
#     def __lt__(self, other):
#         return self.magnitude() < other.magnitude()
#
#     def __len__(self):
#         return 2
#
#     def __getitem__(self, index):
#         if index == 0:
#             return self.x
#         if index == 1:
#             return self.y
#         else:
#             raise IndexError("Vector index out of range")
#
#
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# print(v1)
# print(v1 + v2)
# print(v1 * 3)
# print(v1 == Vector(2, 3))
# print(v1[0])
# print(v1.magnitude())

# 抽象基类
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     """形状抽象基类"""
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#     # 具体方法
#     def description(self):
#         return f"This is a {self.__class__.__name__}"
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
#     def perimeter(self):
#         return 3.14 * 2 * self.radius
#
# class Square(Shape):
#     def __init__(self, x ,y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
#     def perimeter(self):
#         return (self.x + self.y) * 2
#
# circle = Circle(4)
# square = Square(3,7)
# print(circle.area())
# print(square.area())
# print(circle.description())

# 静态类和方法
# 类方法
# class MyClass:
#     count = 0
#     @classmethod
#     def increment_count(cls):
#         cls.count +=1
#
# print(MyClass.count)
# MyClass.increment_count()
# print(MyClass.count)
#
# class MathUtils:
#     @staticmethod
#     def add(a,b):
#         return a + b
#
# print(MathUtils.add(3,4))

# class Student:
#     school_name = "Python University"
#     students_count = 0
#
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#         Student.students_count += 1
#
#     def get_info(self):
#         return f"{self.name} - Grade {self.grade}"
#     @classmethod
#     def get_school_name(cls):
#         return f"School: {cls.school_name}, Students: {cls.students_count}"
#     @classmethod
#     def create_from_string(cls,student_str):
#         name,grade = student_str.split(',')
#         return cls(name.strip(), int(grade.strip()))
#     @staticmethod
#     def is_passing_garde(grade):
#         return grade >= 60
#     @staticmethod
#     def calculate_average(grades):
#         average =  sum(grades) / len(grades) if grades else 0
#         return round(average, 3)
#
#
# student1 = Student("Alice", 85)
# student2 = Student("Bob", 98)
# print(student1.get_info())
# print(student2.get_info())
# student3 = Student.create_from_string("Jerry,88")
# print(student3.get_info())
#
# print(Student.is_passing_garde(78))
# print(Student.calculate_average([78, 90, 86]))

# with 执行下上文
class FileOpen:
    def __init__(self, filepath, mode, encoding="utf-8"):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding
    def __enter__(self):
        print("打开文件")
        self.file = open(self.filepath, self.mode, encoding=self.encoding)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        if self.file:
            self.file.close()

with FileOpen("example.txt", "r") as f:
    f.read()



