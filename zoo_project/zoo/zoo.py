# En el módulo zoo.py

class Zoo:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.exhibitions = []  # Lista para almacenar objetos de tipo Exhibicion
        self.staff = []    # Lista para almacenar objetos de tipo Personal
        self.visitors = []    # Lista para almacenar objetos de tipo Visitante

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)
        print(f"Se ha agregado la exhibición '{exhibition.name}' al zoológico.")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"{employee.name} ha sido agregado al personal del zoológico.")

    def add_visitor(self, visitor):
        self.visitors.append(visitor)
        print(f"{visitor.name} ha ingresado al zoológico.")

    def list_exhibitions(self):
        print("Exhibiciones en el zoológico:")
        for exhibition in self.exhibitions:
            print(f"- {exhibition.name} ({exhibition.theme})")

    def list_staff(self):
        print("Personal del zoológico:")
        for employee in self.staff:
            print(f"- {employee.name} ({employee.position})")

    def list_visitors(self):
        print("Visitantes en el zoológico:")
        for visitor in self.visitors:
            print(f"- {visitor.name}")

    def interact_with_animals(self):
        print("Los visitantes están interactuando con los animales:")
        for exhibition in self.exhibiciones:
            for animal in exhibition.anmals:
                print(f"- {animal.name} ({animal.species}) en la exhibición '{exhibition.name}'")
