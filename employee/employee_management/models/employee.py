from abc import ABC, abstractmethod

# Abstracción
class Employee(ABC):
    def __init__(self, name, salary):
        self._name = name              # Encapsulamiento
        self._salary = salary

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.get_role()} - {self._name}: ${self._salary}"

# Herencia y Polimorfismo
class Developer(Employee):
    def get_role(self):
        return "Developer"

class Designer(Employee):
    def get_role(self):
        return "Designer"
