from zoo.zoo import Zoo
from zoo.exhibition import Exhibition
from zoo.animal.mammal import Mammal
from zoo.animal.bird import Bird
from zoo.animal.reptile import Reptile
from zoo.animal.fish import Fish
from zoo.staff import Staff
from zoo.visitor import Visitor
import msvcrt
import zoo.animal.texting_animal as ta

# Función para crear un zoológico de muestra con exhibiciones y animales
def create_zoo():
    # Crear exhibiciones
    jungle_exhibit = Exhibition("junglelandia", "Exhibición de Selva", "Ubicación 1")
    savannah_exhibit = Exhibition("Sabana Africana", "Exhibición de Sabana", "Ubicación 2")
    acoustic_exhition = Exhibition("the lake", "exhibición acuatica", "Ubicacion 3")

    # Crear animales
    #self, name, age, species, exhibition, fur
    tigre = Mammal("Tiger", 5, "Felino", savannah_exhibit, "Rayado")
    leon = Mammal("Simba", 6, "Felino", savannah_exhibit, "Amarillo")
    loro = Bird("Loro", 2, "Pajaro", jungle_exhibit, "Verde")
    serpiente = Reptile("Snake", 4, "Serpiente", jungle_exhibit, "Escamosa")
    pez_payaso = Fish("Nemo", 1, "Fish", acoustic_exhition, "Aleta Corta")

    # Agregar animales a exhibiciones
    jungle_exhibit.add_animal(tigre)
    jungle_exhibit.add_animal(loro)
    savannah_exhibit.add_animal(leon)
    savannah_exhibit.add_animal(serpiente)
    acoustic_exhition.add_animal(pez_payaso)

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
def main_manu(zoológico):
    print("Welcome to the Zoo ", zoológico.name)
    while True:
        print("\nOptions:")
        print("1. Add Exhibition")
        print("2. List Exhibitions")
        print("3. Go to the animals")
        print("4. Add Employee to the Zoo")
        print("5. List Zoo Staff")
        print("6. Add Visitor to the Zoo")
        print("7. List Visitor in the Zoo")
        print("8. Exit")

        opcion = input("\nSelect an option: ")

        if opcion == "1":
            add_exhibition(zoológico)
        elif opcion == "2":
            list_exhibitions(zoológico)
        elif opcion == "3":
            texting_animal(zoológico)
        elif opcion == "4":
            add_employee(zoológico)
        elif opcion == "5":
            list_staff_zoo(zoológico)
        elif opcion == "6":
            add_visitor(zoológico)
        elif opcion == "7":
            list_visitor_zoo(zoológico)
        elif opcion == "8":
            print("Thanks for inspecting the Zoo. ¡See You Later!")
            break
        else:
            print("Invalid option. Please, selct a valid option.")
        
        msvcrt.getch()


# Function to add an exhibition
def add_exhibition(zoológico):
    print("\nAdding a new exhibition:")
    name = input("Enter the exhibition name: ")
    theme = input("Enter the exhibition theme: ")
    location = input("Enter the exhibition location: ")
    
    new_exhibition = Exhibition(name, theme, location)
    zoológico.add_exhibition(new_exhibition)
    return new_exhibition

# Function to list exhibitions
def list_exhibitions(zoológico):
    print("\nExhibitions in the zoo:")
    zoológico.list_exhibitions()

def texting_animal(zoológico):
    ta.menu_animal(zoológico)

# Function to add an employee
def add_employee(zoológico):
    print("\nAdding a new employee:")
    employee_name = input("Enter the employee name: ")
    employee_age = int(input("Enter the employee age: "))
    employee_position = input("Enter the employee position: ")
    employee_salary = float(input("Enter the employee salary: "))
    
    new_employee = Staff(employee_name, employee_age, employee_position, employee_salary)
    zoológico.add_staff(new_employee)

# Function to list zoo staff
def list_staff_zoo(zoológico):
    print("\nZoo staff:")
    zoológico.list_staff()

# Function to add a visitor
def add_visitor(zoológico):
    print("\nAdding a new visitor:")
    visitor_name = input("Enter the visitor name: ")
    visitor_age = int(input("Enter the visitor age: "))
    visitor_ticket = input("Enter the visitor ticket number: ")
    
    new_visitor = Visitor(visitor_name, visitor_age, visitor_ticket)
    zoológico.add_visitor(new_visitor)

# Function to list zoo visitors
def list_visitor_zoo(zoológico):
    print("\nZoo visitors:")
    zoológico.list_visitors()


if __name__ == "__main__":
    main_manu(create_zoo())
