class Plane:
    def __init__(self,ModelName,brand,capacity):
        self.ModelName = ModelName
        self.brand = brand
        self.capacity = capacity
    
    def intro_plane(self):
        print(
            "The name of the plane is " + self.ModelName + 
            ". It was released by " + self.brand +
            ". It has a capacity of " + str(self.capacity)
            )
            

P1 = Plane("B737", " Boeing", 155)
P2 = Plane("A350","Airbus", 250)

P1.intro_plane()
P2.intro_plane()

name = "nik"
age = 24
print(f"{name} is {age} years old")


class Cow:
    def __init__(self,w,c):
        self.weight = w
        self.colour = c
    
    def CowDes(self):
        print(f"The cow's weight is {self.weight} kg and its colour is {self.colour} ")

C1 = Cow(50,"blue" )
C2 = Cow(58,"green")

class Farmer:
    def __init__(self,n,a):
        self.name = n
        self.age = a

F1 = Farmer("Jerome",25)
F2 = Farmer("Justin",47)
F1.own_cow = C1
F2.own_cow = C2

F1.own_cow.CowDes()
F2.own_cow.CowDes()


    
