class Automobile:
    def __init__(self,name,fare,prise_ticket):
        self.name=name
        self.fare=fare
        self.ticket=prise_ticket

class Bus(Automobile):
    pass
School_bus=Bus("School Volvo", 3.00,2)
print("Vechicle Name:", School_bus.name,"Total fare",School_bus.fare,"Price ticket",School_bus.ticket)




