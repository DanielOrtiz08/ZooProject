
from .animal_group import AnimalGroup  # Importar la clase base Animal

class Bird(AnimalGroup):
    def __init__(self, name, age, type, exhibition, plumage):
        super().__init__(name, age, type, exhibition)
        self.plumage = plumage   # Atributo específico de las aves
        self.specie = "bird"
        
    def eat(self):
        return f"{self.name} is eating like a bird"

    def sleep(self):
        return f"{self.name} is sleeping in its nest"

    def make_sound(self):
        return f"{self.name} is singing."

    def fly(self):
        return f"{self.name} is flying."

    def __str__(self):
        return f"{super().__str__()} - Plumaje: {self.plumage}"
