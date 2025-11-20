from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Employee(ABC):
    def __init__(self, name: str, employee_id: str, salary: float):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.hire_date = datetime.now()

    @abstractmethod
    def calculate_bonus(self) -> float:
        pass

    @abstractmethod
    def get_role(self) -> str:
        pass

    def get_info(self) -> str:
        return f"{self.name} ({self.employee_id}) - {self.get_role()}"


class Manager(Employee):
    def __init__(self, name: str, employee_id: str, salary: float, department: str):
       super().__init__(name,employee_id, salary)
       self.department = department
       self.team: List[Employee] = []
       
    def calculate_bonus(self) -> float:
        return self.salary * 0.3
    def get_role(self) -> str:
        return f"{self.department}经理"
    def add_team_member(self,employee:Employee):
        self.team.append(employee)
    def get_team_size(self) -> int:
        return len(self.team)
    
class Developer(Employee):
    def __init__(self,name:str, employee_id:str,salary:float, programming_language:str):
        super().__init__(name,employee_id,salary)
        self.programming_language = programming_language
    def calculate_bonus(self) -> float:
        return self.salary * 0.2
    def get_role(self) -> str:
        return f"{self.programming_language}开发工程师"

class Designer(Employee):
    def __init__(self,name:str,employee_id:str, salary:float,design_tool:str):
        super().__init__(name,employee_id,salary)
        self.design_tool = design_tool
    def calculate_bonus(self) -> float:
        return self.salary * 0.15
    def get_role(self) -> str:
        return f"{self.design_tool}设计师"

class Company:
    def __init__(self,name:str):
        self.name = name
        self.employees: List[Employee] = []
    def hire(self,employee:Employee):
        self.employees.append(employee)
        print(f"已雇佣：{employee.get_info()}")
    def calculate_total_payroll(self) -> float:
        total = sum(emp.salary for emp in self.employees)
        total_bonus = sum(emp.calculate_bonus() for emp in self.employees)
        return total + total_bonus
    def list_employees(self):
        print(f"\n{self.name}员工列表")
        for employee in self.employees:
            print(f" - {employee.get_info()}")
            print(f"   奖金： ￥{employee.calculate_bonus():.2f}")

# 创建公司对象
company = Company("科技公司")

# 创建经理对象
manager = Manager("王小明", "M001", 80000, "工程部")
# 创建开发工程师对象1
dev1 = Developer("李雷", "D001", 70000, "Python")
# 创建开发工程师对象2
dev2 = Developer("韩梅梅", "D002", 75000, "JavaScript")
# 创建设计师对象
designer = Designer("张伟", "DS001", 65000, "Figma")
        
# 构建经理的团队，添加开发与设计成员
manager.add_team_member(dev1)
manager.add_team_member(dev2)
manager.add_team_member(designer)

# 公司雇佣所有员工
company.hire(manager)
company.hire(dev1)
company.hire(dev2)
company.hire(designer)

# 输出公司员工信息
company.list_employees()
# 输出公司总薪酬
print(f"\n总薪酬: ￥{company.calculate_total_payroll():.2f}")
# 输出经理的团队人数
print(f"经理团队人数: {manager.get_team_size()}")
