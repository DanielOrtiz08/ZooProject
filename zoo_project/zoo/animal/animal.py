# En el módulo animal.py

class Animal:
    def __init__(self, name, age, species, exhibition=None):
        self.name = name
        self.age = age
        self.species = species
        self.exhibition = exhibition

    def eat(self):
        return f"{self.name} está comiendo."

    def sleep(self):
        return f"{self.name} está durmiendo."

    def make_sound(self):
        return f"{self.name} está haciendo un sonido."

    def __str__(self):
        return f"Nombre: {self.name} Especie: {self.species} "
