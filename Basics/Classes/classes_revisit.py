class Food:
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
    
    def draw(self): #   this is a class method
        pass

chicken = Food("chicken",5)
sushi = Food("sushi",7)

print(sushi.quantity)
print(chicken.name)