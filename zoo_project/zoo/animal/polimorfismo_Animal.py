import zoo.animal.texting_animal as ta
from zoo.animal.mammal import Mammal
from zoo.animal.bird import Bird
from zoo.animal.reptile import Reptile
from zoo.animal.fish import Fish

def interact_with_animal(zoo):
    animal = choose_animal(zoo)
    while True:
        print(f"Interacting with animal:")
        print("1. Feed")
        print("2. Sleep")
        print("3. Make Sound")
        print("5. Return to previous menu")
        choice = input("Select an action: ")

        if choice == '1':
            animal.eat()
        elif choice == '2':
            animal.sleep()
        elif choice == '3':
            animal.make_sound()
        elif choice == '4':
            if isinstance(animal, Mammal):
                # Interact with a Mammal-specific method
                animal.nurse()
            elif isinstance(animal, Reptile):
                # Interact with a Reptile-specific method
                animal.shed_skin()
            elif isinstance(animal, Fish):
                # Interact with a Fish-specific method
                animal.swim()
            elif isinstance(animal, Bird):
                # Interact with a Bird-specific method
                animal.fly()
        elif choice == '5':
            ta.menu_animal(zoo)
        else:
            print("Invalid option. Please select a valid option.")

def choose_animal(zoo):
    zoo.list_all_animals()
    animal_name = input("write the name of an animal: ")
    return get_animal_by_name(zoo, animal_name)

def get_animal_by_name(zoo, animal_name):
    for exhibition in zoo.exhibiciones:
        for animal in exhibition.animales:
            if animal.name == animal_name:
                return animal
    return None  # Retorna None si no se encuentra el animal
