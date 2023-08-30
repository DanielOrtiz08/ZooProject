# En el módulo pez.py

from .animal import Animal  # Importar la clase base Animal

class Fish(Animal):
    def init(self, name, age, species, fin_type):
        super().init(name, age, species)
        self.fin_type = fin_type  # Atributo específico de los peces

    def make_sound(self):
        return f"{self.name} está nadando en silencio."

    def swim(self):
        return f"{self.name} está nadando con sus aletas {self.fin_type}."

    def __str__(self):
        return f"{super().__str__()} - Tipo de Aleta: {self.fin_type}"
