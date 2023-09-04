
from .animal_group import AnimalGroup  # Importar la clase base Animal

class Fish(AnimalGroup):
    def __init__(self, name, age, type, exhibition, fin_type):
        super().__init__(name, age, type, exhibition)
        self.fin_type = fin_type  # Atributo específico de los peces
        self.specie = "fish"
        
    def eat(self):
        return f"{self.name} eats in the water"

    def sleep(self):
        return f"the fish {self.name} is not sleeping"

    def make_sound(self):
        return f"{self.name} is swimming silently."

    def swim(self):
        return f"{self.name} is swimming with its {self.fin_type} fins."

    def __str__(self):
        return f"{super().__str__()}, Fin type: {self.fin_type}"
    