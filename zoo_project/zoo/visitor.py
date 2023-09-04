# En el módulo visitor.py

class Visitor:
    def __init__(self, name, age, ticket):
        self.name = name
        self.age = age
        self.ticket = ticket  # Número de boleto o identificación del visitante
        self.visited_exhibitions = []  # Lista para almacenar objetos de tipo Exhibicion visitados
        self.location = False

    def enter_exhibiton(self, exhibition):
        self.visited_exhibitions.append(exhibition)
        print(f"{self.name} has entered the exhibition '{exhibition.name}'.")
        self.location = True

    def exit_exhibition(self, exhibition):
        self.location = False
        if exhibition in self.visited_exhibitions:
            self.visited_exhibitions.remove(exhibition)
            print(f"{self.name} has exited the exhibición '{exhibition.name}'.")
        else:
            print(f"{self.name} was not in the exhibición '{exhibition.name}'.")

    def observe_animals(self):
        if not self.visited_exhibitions:
            print("the visitor has not entered any exhibition")
        else:
            if self.location:
                print(f"{self.name} is looking the animal in the exhibition: {self.visited_exhibitions[-1]}")
            else:
                print(f"The visitor is in the zoo but is outside the exhibitions")
                
    
    def visited_exhibitions(self):
        print("visited exhibitions")
        for exhibition in self.visited_exhibitions:
                    print(f"- {exhibition.name} ({exhibition.theme})")

    def __str__(self):
        return f"Visitor: {self.name}, Age: {self.age}, Ticket: {self.ticket}"
