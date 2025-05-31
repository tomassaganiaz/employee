from models.employee import Developer, Designer
from models.manager import Manager 

class EmployeeBuilder:
    def __init__(self):
        self.name = ""
        self.salary = 0
        self.role = "Developer"

    def set_name(self, name):
        self.name = name
        return self

    def set_salary(self, salary):
        self.salary = salary
        return self

    def set_role(self, role):
        self.role = role
        return self

    def build(self):
        if self.role.lower() == "developer":
            return Developer(self.name, self.salary)
        elif self.role.lower() == "designer":
            return Designer(self.name, self.salary)
        elif self.role.lower() == "manager":
            from models.manager import Manager
            return Manager(self.name, self.salary)
        else:
            raise ValueError("Unknown role")
