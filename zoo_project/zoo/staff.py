# En el módulo staff.py

class Staff:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def work(self):
        return f"{self.name} está trabajando en su puesto de {self.position}."

    def rest(self):
        return f"{self.name} está descansando."

    def __str__(self):
        return f"Nombre: {self.name} Puesto: {self.position}"
