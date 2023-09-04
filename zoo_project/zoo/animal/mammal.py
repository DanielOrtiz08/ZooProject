
from .animal_group import AnimalGroup  # Importar la clase base Animal

class Mammal(AnimalGroup):
    def __init__(self, name, age, type, exhibition, fur):
        super().__init__(name, age, type, exhibition)
        self.fur = fur # pelaje Atributo específico de los mamíferos
        self.specie = "mammal"
        
    def eat(self):
        return f"{self.name} is eating like a mammal."

    def sleep(self):
        return f"{self.name} sleeps like a mammal."

    def make_sound(self):
        return f"{self.name} is making a mammal sound."

    def nurse(self):
        return f"{self.name} is nursing its calves."

    def __str__(self):
        return f"{super().__str__()} - Fur: {self.fur}"
