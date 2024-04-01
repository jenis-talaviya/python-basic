#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
        
detailx = vehicle("school volvo",180,12)
print(f"vehicle name:{detailx.name} speed:{detailx.max_speed} mileage:{detailx.milage}")