# En el módulo visitor.py

class Visitor:
    def __init__(self, name, age, ticket):
        self.name = name
        self.age = age
        self.ticket = ticket  # Número de boleto o identificación del visitante
        self.visited_exhibitions = []  # Lista para almacenar objetos de tipo Exhibicion visitados

    def enter(self, exhibition):
        self.visited_exhibitions.append(exhibition)
        print(f"{self.name} ha entrado a la exhibición '{exhibition.name}'.")

    def exit(self, exhibition):
        if exhibition in self.visited_exhibitions:
            self.visited_exhibitions.remove(exhibition)
            print(f"{self.name} ha salido de la exhibición '{exhibition.name}'.")
        else:
            print(f"{self.name} no estaba en la exhibición '{exhibition.name}'.")

    def observe_animals(self):
        print(f"{self.name} está observando los animales en las exhibiciones:")
        for exhibition in self.visited_exhibitions:
            print(f"- {exhibition.name} ({exhibition.theme})")

    def __str__(self):
        return f"Visitante: {self.name}, Edad: {self.age}, Boleto: {self.ticket}"
