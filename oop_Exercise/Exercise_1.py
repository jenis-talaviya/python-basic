#Create a Class with instance attributes

class Vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage = milage
        
modelx = Vehicle(210,15)
print(modelx.max_speed,modelx.milage)
