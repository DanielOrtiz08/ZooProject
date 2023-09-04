import zoo.animal.texting_animal as ta
from zoo.animal.mammal import Mammal
from zoo.animal.bird import Bird
from zoo.animal.reptile import Reptile
from zoo.animal.fish import Fish
import msvcrt

def interact_with_animals(zoo):
    animal = choose_animal(zoo)
    while True:
        print(f"\nInteracting with animal:")
        print("1. Feed")
        print("2. Sleep")
        print("3. Make Sound")
        print("4. Special Action (Specific to Animal Type)")
        print("5. Return to previous menu")
        choice = input("Select an action: ")

        if choice == '1':
            print(animal.eat())
        elif choice == '2':
            print(animal.sleep())
        elif choice == '3':
            print(animal.make_sound())
        elif choice == '4':
            if isinstance(animal, Mammal):
                # Interact with a Mammal-specific method
                print(animal.nurse())
            elif isinstance(animal, Reptile):
                # Interact with a Reptile-specific method
                print(animal.shed_skin())
            elif isinstance(animal, Fish):
                # Interact with a Fish-specific method
                print(animal.swim())
            elif isinstance(animal, Bird):
                # Interact with a Bird-specific method
                print(animal.fly())
        elif choice == '5':
            ta.menu_animal(zoo)
        else:
            print("Invalid option. Please select a valid option.")
        
        msvcrt.getch()

def choose_animal(zoo):
    zoo.list_all_animals()
    animal_name = input("write the name of an animal: ")
    return get_animal_by_name(zoo, animal_name)

def get_animal_by_name(zoo, animal_name):
    for exhibition in zoo.exhibitions:
        for animal in exhibition.animals:
            if animal.name == animal_name:
                print("animal found")
                return animal
    return None  # Retorna None si no se encuentra el animal
