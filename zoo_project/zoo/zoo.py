
import event as ev

class Zoo:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.exhibitions = []  # Lista para almacenar objetos de tipo Exhibicion
        self.staff = []    # Lista para almacenar objetos de tipo Personal
        self.visitors = []    # Lista para almacenar objetos de tipo Visitante

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)
        print(f"Exhibition '{exhibition}' has been added to the zoo.")
        
    def delete_exhibition(self, exhibition):
        respuesta = ev.alert_message("If you remove an exhibit\nthe animals will also be removed\nare you sure about this action?")
        if respuesta:
            self.exhibitions.remove(exhibition)
    
    def list_all_animals(self):
        print("Animals in the zoo:")
        i = 1
        for exhibition in self.exhibitions:
            print(f"{i}). Animals in the '{exhibition.name}' exhibition:")
            exhibition.list_animals()
            i = i+1        

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"Employee '{employee}' has been added to the zoo.")

    def add_visitor(self, visitor):
        self.visitors.append(visitor)
        print("Visitor ", visitor, " has been added to the zoo.")

    def list_exhibitions(self):
        print("Exhibitions in the zoo:")
        for exhibition in self.exhibitions:
            print(f"- {exhibition.name} ({exhibition.theme})")

    def list_staff(self):
        print("Zoo staff:")
        for employee in self.staff:
            print(f"- {employee.name} ({employee.position})")

    def list_visitors(self):
        print("Visitors in the zoo:")
        for visitor in self.visitors:
            print(f"- {visitor.name}")
      
    def find_exhibition_by_name(self, name):
        for exhibition in self.exhibitions:
            if exhibition.compareTo(name):
                return exhibition
        return None
        

