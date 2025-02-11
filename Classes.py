#A class is like a blueprint while an object is an instance of a class
#car:colour,horsepower,engine,brand
#colour=red
#horsepower=18999
#define a class called car
class car:
    def __init__(self,color,horsepower,brand):
        self.color=color
        self.horsepower=horsepower
        self.brand=brand
        self.speed=0
    def carinfo(self):
        #Prints car details
        return f"This car is a {self.brand} in {self.color} with a horsepower of {self.horsepower}"
    def accelerate(self,increment=5):
        self.speed+=increment
        print(f"The car has accelerated and the current speed is {self.speed}km/h")                               
#Creating an object
car1=car("yellow",4000,"Subaru")
car2=car("green",3500,"Toyota")
#Accessing attributes
print(car1.brand)
print(car2.horsepower)
#Calling a method
car1.accelerate()
car1.accelerate(10)
