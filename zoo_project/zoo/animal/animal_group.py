
from abc import ABC, abstractmethod

class AnimalGroup(ABC):
    
    def __init__(self, name, age, type, exhibition):
        self.name = name
        self.age = age
        self.type = type
        self.exhibition = exhibition
        
    def eat(self):
        pass

    def sleep(self):
        pass

    def make_sound(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.type}, Exhibition: {self.exhibition} "
