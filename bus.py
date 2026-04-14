class Vehicle:
    def __init__(self,name,Top_speed,Milege):
        self.name=name
        self.Top_speed=Top_speed
        self.Milege=Milege

class Bus(Vehicle):
    pass

obj=Bus("Volvo",180,15)
print(f"Name:{obj.name}, Top Speed: {obj.Top_speed} km/h, Mileage: {obj.Milege} km/l")