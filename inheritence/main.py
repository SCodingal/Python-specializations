class Vechicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vechicle):
    pass
School_bus=Bus("School Volvo", 180,12)
print("Vechicle Name:", School_bus.name,"Speed:",School_bus.max_speed,"Mileage:",School_bus.mileage)

class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

peggy=Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
