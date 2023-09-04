
class Exhibition:
    def __init__(self, name, theme, location):
        self.name = name
        self.theme = theme
        self.location = location
        self.animals = []  # Lista para almacenar objetos de tipo Animal en esta exhibición

    def add_animal(self, animal):
        self.animals.append(animal)
        animal.exhibition = self  # Establecer la referencia a esta exhibición en el animal
        print(f"{animal.name} has been added to the exhibition '{self.name}'.")

    def list_animals(self):
        print(f"Animals in the exhibition '{self.name}':")
        for animal in self.animals:
            print(f"{animal.str}")
            
    def compareTo(self, name):
        return self.name == name

    def __str__(self):
        return f"Exhibition '{self.name}' - Theme: {self.theme}, location: {self.location}"
