import sys
sys.path.append("C:\\Users\\HP\\Desktop\\COMPILADORES\\POO_ConPolimorfismo\\zoo_project\\zoo\\exhibition")
from zoo.exhibition import Exhibition
from zoo.animal.mammal import Mammal
from zoo.animal.bird import Bird
from zoo.animal.reptile import Reptile
from zoo.animal.fish import Fish
import msvcrt
import event as ev
import main
import zoo.animal.polimorfismo_Animal as pa

def menu_animal(zoo):
    while(True):
        print("")
        print("1. Add animals")
        print("2. list animals exhibition")
        print("3. list all animals")
        print("4. interact with animals")
        print("5. return main menu")
        opction = input("\nselect an option: ")
        
        if opction == '1':
            add_animal(zoo)
        elif opction == '2':
            list_animals_exhibition(zoo)
        elif opction == '3':
            list_all_animals(zoo)
        elif opction == '4':
            pa.interact_with_animals(zoo)
        elif opction == '5':
            main.main_manu(zoo)
        else:
            print("Invalid option. Please, selct a valid option.")
        
        msvcrt.getch()
        

# Opction 1 ------------------------------------------------------------
# Function to add animal
def add_animal(zoo):
    print("\nAdding a new animal:")
    animal_name = input("Enter the animal name: ")
    animal_age = int(input("Enter the animal age: "))
    animal_type = input("Enter the animal type: ")
        
    band, Exhibition = available_exhibitions(zoo)
    
    if not band:
        print("animal no agree")
        return         
    
    while(True):
        animal_species = input("Enter the animal species: ")
        # Determine the appropriate animal subclass based on species
        if animal_species.lower() == "mammal":
            animal = create_mammal(animal_name, animal_age, animal_type, Exhibition)
            break
        elif animal_species.lower() == "reptile":
            animal = create_reptile(animal_name, animal_age, animal_type, Exhibition)
            break
        elif animal_species.lower() == "fish":
            animal = create_fish(animal_name, animal_age, animal_type, Exhibition)
            break
        elif animal_species.lower() == "bird":
            animal = create_bird(animal_name, animal_age, animal_type, Exhibition)
            break
        else:
            print(f"Invalid species: {animal_species}. Animal not added.")
        
        msvcrt.getch()

    print(f"Animal '{animal_name}' has been added to the zoo.")
    Exhibition.add_animal(animal)

# Check exhibitions
def available_exhibitions(zoológico):
    print("Available exhibitions:")
    zoológico.list_exhibitions()
    exhibition_name = input("Enter the name of the exhibition to add the animal: ")
    
    # Find the exhibition by name
    exhibition = zoológico.find_exhibition_by_name(exhibition_name)
    
    if not exhibition:
        desition = ev.alert_message(f"No exhibition found with the name {exhibition_name}.\nDo you want to add?")
        
        if desition:
            exhibition = main.add_exhibition(zoológico)
        else:
            return False, None
    return True, exhibition

# Function to create a mammal
def create_mammal(name, age, type, exhibition):
    fur_type = input("Enter the mammal's fur type: ")
    return Mammal(name, age, type, exhibition, fur_type)

# Function to create a reptile
def create_reptile(name, age, type, exhibition):
    scale = input("Enter the reptile's scale type: ")
    return Reptile(name, age, type, exhibition, scale)

# Function to create a fish
def create_fish(name, age, type, exhibition):
    fin_type = input("Enter the fish's fin type: ")
    return Fish(name, age, type, exhibition, fin_type)

# Function to create a bird
def create_bird(name, age, type, exhibition):
    plumage = input("Enter the bird's plumage color: ")
    return Bird(name, age, type, exhibition, plumage)

# Opction 2 ------------------------------------------------------------
# Function to list animals in an exhibition
def list_animals_exhibition(zoológico):
    print("Available exhibitions:")
    zoológico.list_exhibitions()
    exhibition_name = input("Enter the name of the exhibition: ")
    
    # Find the exhibition by name
    exhibition = zoológico.find_exhibition_by_name(exhibition_name)

    if exhibition:
        exhibition.list_animals()
    else:
        print(f"No exhibition found with the name '{exhibition_name}'.")

# Opction 3 ------------------------------------------------------------
# Function to list all animals in the zoo
def list_all_animals(zoo):
    print("Listing all", end=' ')
    zoo.list_all_animals()
     
