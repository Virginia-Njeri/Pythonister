#1a) Create a class Vehicle with the following attributes:name, max_speed,mileage. Define attribute color to be “White” for all the vehicles.
 #Create two instances to confirm it works.
class Vehicle:
    color="white"
    def __init__ (self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def congratulation(self):
        return f"congratulation Virginia for buying {self.color} {self.name} {self.max_speed} {self.mileage}"    
#c)Create a method that returns the car name and its capacity.
    def carriage_capacity(self,capacity):
        return f"you bought {self.name} and can carry {capacity} babies"
        
