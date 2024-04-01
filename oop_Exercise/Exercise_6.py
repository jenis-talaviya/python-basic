#Class Inheritance
class Vehicle:

    def __init__(self, name, mileage,capacity):
        self.name = name
        self.capacity = capacity
        self.mileage = mileage
        
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
