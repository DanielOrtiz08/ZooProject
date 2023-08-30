# En el módulo reptil.py

from .animal import Animal  # Importar la clase base Animal

class Reptile(Animal):
    def __init__(self, name, age, species, scales):
        super().init(name, age, species)
        self.scales = scales  # Atributo específico de los reptiles

    def make_sound(self):
        return f"{self.name} está emitiendo un sonido de reptil."

    def shed_skin(self):
        return f"{self.name} está cambiando su piel."

    def __str__(self):
        return f"{super().__str__()} - Escamas: {self.scales}"
