# En el módulo mamifero.py

from .animal import Animal  # Importar la clase base Animal

class Mammal(Animal):
    def __init__(self, name, age, species, fur):
        super().init(name, age, species)
        self.fur = fur # pelaje Atributo específico de los mamíferos

    def make_sound(self):
        return f"{self.name} está emitiendo un sonido de mamífero."

    def nurse(self):
        return f"{self.name} está amamantando a sus crías."

    def __str__(self):
        return f"{super().__str__()} - Pelaje: {self.fur}"
