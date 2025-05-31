class Database:
    __instance = None

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.employees = []
            Database.__instance = self

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return self.employees
