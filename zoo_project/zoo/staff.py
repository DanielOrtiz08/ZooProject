
class Staff:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def work(self):
        return f"{self.name} is working on the position as a {self.position}."

    def rest(self):
        return f"{self.name} is resting ."

    def __str__(self):
        return f"Name: {self.name} Position: {self.position}"
