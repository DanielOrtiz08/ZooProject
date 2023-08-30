from zoo.zoo import Zoo
from zoo.exhibition import Exhibition
from zoo.animal import Animal
from zoo.animal.mammal import Mammal
from zoo.animal.bird import Bird
from zoo.animal.reptile import Reptile
from zoo.animal.fish import Fish
from zoo.staff import Staff
from zoo.visitor import Visitor

# Función para crear un zoológico de muestra con exhibiciones y animales
def crear_zoologico():
    # Crear exhibiciones
    jungle_exhibit = Exhibition("junglelandia", "Exhibición de Selva", "Ubicación 1")
    savannah_exhibit = Exhibition("Sabana Africana", "Exhibición de Sabana", "Ubicación 2")
    acoustic_exhition = Exhibition("the lake", "exhibición acuatica", "Ubicacion 3")

    # Crear animales
    tigre = Mammal("Tiger", 5, "Felino", "Rayado")
    leon = Mammal("Simba", 6, "Felino", "Amarillo")
    loro = Bird("Loro", 2, "pajaro", "Verde")
    serpiente = Reptile("Serpiente", 4, "serpiente", "Escamosa")
    pez_payaso = Fish("Nemo", 1, "Pez payaso", "Aleta Corta")

    # Agregar animales a exhibiciones
    jungle_exhibit.add_animal(tigre)
    jungle_exhibit.add_animal(loro)
    savannah_exhibit.agregar_animal(leon)
    savannah_exhibit.add_animal(serpiente)
    acoustic_exhition.agregar_animal(pez_payaso)

    # Crear personal
    tiger_keeper = Staff("Julano", 28, "Cuidador de tigres", 2500)
    vet = Staff("Pratishia", 35, "Veterinario", 3500)
    Biologist = Staff("Green", 39, "zoo keeper", 4300)

    # Crear visitantes
    visitante1 = Visitor("Daniel", 25, "Ticket001")
    visitante2 = Visitor("David", 22, "Ticket002")

    # Crear zoológico y agregar exhibiciones, personal y visitantes
    zoológico = Zoo("zoo animalista", "little city", 100)
    zoológico.add_exhibition(jungle_exhibit)
    zoológico.add_exhibition(savannah_exhibit)
    zoológico.add_exhibition(acoustic_exhition)
    
    zoológico.add_staff(tiger_keeper)
    zoológico.add_staff(vet)
    zoológico.add_staff(Biologist)
    
    zoológico.add_visitor(visitante1)
    zoológico.add_visitor(visitante2)

    return zoológico

# Función para mostrar el menú principal
def menu_principal():
    print("Bienvenido al Zoológico ", zoológico.name)
    while True:
        print("\nOpciones:")
        print("1. Agregar Exhibición")
        print("2. Listar Exhibiciones")
        print("3. Agregar Animal en una Exhibición")
        print("4. Listar Animales en una Exhibición")
        print("5. Agregar Empleado al Zoológico")
        print("6. Listar Personal del Zoológico")
        print("7. Agregar Visitante al Zoológico")
        print("8. Listar Visitantes del Zoológico")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            add_exhibition()
        elif opcion == "2":
            list_exhibitions()
        elif opcion == "3":
            add_animal()
        elif opcion == "4":
            list_animals_exhibition()
        elif opcion == "5":
            add_employee()
        elif opcion == "6":
            list_staff_zoo()
        elif opcion == "7":
            add_visitor()
        elif opcion == "8":
            list_visitor_zoo()
        elif opcion == "9":
            print("Gracias por visitar el Zoológico. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Function to add an exhibition
def add_exhibition(zoo):
    print("Agregando nueva exhibicion:")
    name = input("Enter the exhibition name: ")
    theme = input("Enter the exhibition theme: ")
    location = input("Enter the exhibition location: ")
    
    new_exhibition = Exhibition(name, theme, location)
    zoo.add_exhibition(new_exhibition)
    print(f"Exhibition '{name}' has been added to the zoo.")

# Function to list exhibitions
def list_exhibitions(zoo):
    print("Exhibitions in the zoo:")
    zoo.list_exhibitions()

# Function to add an animal to an exhibition
def add_animal(zoo):
    print("Adding an animal to an exhibition:")
    animal_name = input("Enter the animal name: ")
    animal_age = int(input("Enter the animal age: "))
    animal_species = input("Enter the animal species: ")

    print("Available exhibitions:")
    zoo.list_exhibitions()
    exhibition_name = input("Enter the name of the exhibition to add the animal: ")
    
    # Find the exhibition by name
    exhibition = zoo.find_exhibition_by_name(exhibition_name)

    if exhibition:
        new_animal = Animal(animal_name, animal_age, animal_species)
        exhibition.add_animal(new_animal)
        print(f"{animal_name} has been added to the exhibition '{exhibition_name}'.")
    else:
        print(f"No exhibition found with the name '{exhibition_name}'.")

# Function to list animals in an exhibition
def list_animals_exhibition(zoo):
    print("Available exhibitions:")
    zoo.list_exhibitions()
    exhibition_name = input("Enter the name of the exhibition: ")
    
    # Find the exhibition by name
    exhibition = zoo.find_exhibition_by_name(exhibition_name)

    if exhibition:
        print(f"Animals in the exhibition '{exhibition_name}':")
        exhibition.list_animals()
    else:
        print(f"No exhibition found with the name '{exhibition_name}'.")

# Function to add an employee
def add_employee(zoo):
    print("Adding a new employee:")
    employee_name = input("Enter the employee name: ")
    employee_age = int(input("Enter the employee age: "))
    employee_position = input("Enter the employee position: ")
    employee_salary = float(input("Enter the employee salary: "))
    
    new_employee = Staff(employee_name, employee_age, employee_position, employee_salary)
    zoo.add_personal(new_employee)
    print(f"Employee '{employee_name}' has been added to the zoo.")

# Function to list zoo staff
def list_staff_zoo(zoo):
    print("Zoo staff:")
    zoo.list_staff()

# Function to add a visitor
def add_visitor(zoo):
    print("Adding a new visitor:")
    visitor_name = input("Enter the visitor name: ")
    visitor_age = int(input("Enter the visitor age: "))
    visitor_ticket = input("Enter the visitor ticket number: ")
    
    new_visitor = Visitor(visitor_name, visitor_age, visitor_ticket)
    zoo.add_visitor(new_visitor)
    print(f"Visitor '{visitor_name}' has been added to the zoo.")

# Function to list zoo visitors
def list_visitor_zoo(zoo):
    print("Zoo visitors:")
    zoo.list_visitors()


# Función principal que llama al menú principal
if __name__ == "__main__":
    zoológico = crear_zoologico()
    menu_principal()
