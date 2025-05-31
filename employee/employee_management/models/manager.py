from models.employee import Employee

class Manager(Employee):
    def get_role(self):
        return "Manager"
