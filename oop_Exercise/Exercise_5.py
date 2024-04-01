#Define a property that must have the same value for every class instance (object)

class Vehicle:
    
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color,School_bus.name,School_bus.max_speed,School_bus.mileage)
