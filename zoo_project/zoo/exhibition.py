# En el módulo exhibition.py

class Exhibition:
    def __init__(self, name, theme, location):
        self.name = name
        self.theme = theme
        self.location = location
        self.animals = []  # Lista para almacenar objetos de tipo Animal en esta exhibición

    def add_animal(self, animal):
        self.animals.append(animal)
        animal.exhibition = self  # Establecer la referencia a esta exhibición en el animal
        print(f"{animal.name} ha sido agregado a la exhibición '{self.name}'.")

    def list_animals(self):
        print(f"Animales en la exhibición '{self.name}':")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.species})")

    def __str__(self):
        return f"Exhibición '{self.name}' - Tema: {self.theme}, Ubicación: {self.location}"
