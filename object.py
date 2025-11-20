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
    def calculate_bouns(self) -> float:
        pass

    @abstractmethod
    def get_role(self) -> str:
        pass

    def get_info(self) -> str:
        return f"{self.name} ({self.employee_id}) - {self.get_role()}"


class Manager(Employee):
    def __init__(self, name: str, employee_id: str, salary: float, department: str):
        # 调用父类构造器
        super().__init__(name, employee_id, salary)
        # 部门名称
        self.department = department
        # 团队成员列表
        self.team: List[Employee] = []
