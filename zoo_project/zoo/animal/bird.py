# En el módulo ave.py

from .animal import Animal  # Importar la clase base Animal

class Bird(Animal):
    def __init__(self, name, age, species, plumage):
        super().init(name, age, species)
        self.plumage = plumage   # Atributo específico de las aves

    def make_sound(self):
        return f"{self.name} está cantando."

    def fly(self):
        return f"{self.name} está volando."

    def __str__(self):
        return f"{super().__str__()} - Plumaje: {self.plumage}"
