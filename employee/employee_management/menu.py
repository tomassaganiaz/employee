from database import Database
from builder import EmployeeBuilder

def show_menu():
    db = Database.get_instance()
    while True:
        print("\n1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Salir")
        choice = input("Opción: ")

        if choice == '1':
            name = input("Nombre: ")
            salary = float(input("Salario: "))
            role = input("Rol (Developer/Designer/Manager): ")

            builder = EmployeeBuilder()
            employee = builder.set_name(name).set_salary(salary).set_role(role).build()
            db.add_employee(employee)
            print("Empleado agregado.")

        elif choice == '2':
            print("\n--- Lista de empleados ---")
            for emp in db.list_employees():
                print(emp)

        elif choice == '3':
            break
        else:
            print("Opción inválida")
