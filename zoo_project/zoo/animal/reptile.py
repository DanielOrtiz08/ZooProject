
from .animal_group import AnimalGroup  # Importar la clase base Animal

class Reptile(AnimalGroup):
    def __init__(self, name, age, type, exhibition, scales):
        super().__init__(name, age, type, exhibition)
        self.scales = scales  # Atributo específico de los reptiles
        self.specie = "reptile"
    
    def eat(self):
        return f"{self.name} eats like a reptile"

    def sleep(self):
        return f"{self.name} is sleeping like a reptile"

    def make_sound(self):
        return f"{self.name} is making a reptilian sound."

    def shed_skin(self):
        return f"{self.name} is shedding its skin."

    def __str__(self):
        return f"{super().__str__()} - scales: {self.scales}"
