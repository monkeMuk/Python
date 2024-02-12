#   methods = functions within classes
#   assingning attributes to instances


class Car():
    age = 12    
    all = []

    def __init__(self, name: str, price: int, quantity ):

        #   makes sure price and quantity is above than 0 // assert = make sure
        assert price >= 0, f"{price} is lower than 0" 
        assert quantity >= 0, f"{quantity} is lower than 0"

        #   Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        #   Actions to execute
        Car.all.append(self)
        #   This adds all the instances into a list

    def cal_total_price(self):
        return self.price * self.quantity

    def add(self,x,y):
        return x + y

    def __repr__(self):
        return f"Car('{self.name}')"
        """
        Makes the contents within all = [] list more presetable by assingining them with names
        """ 

car1 = Car("Myvi",100,3 ) 
car2 = Car("Honda",300,8)
car3 = Car("Waja",590,6)
car4 = Car("Nissan",330,7)


"""
print(car1.cal_total_price())
print(car2.cal_total_price())

print(car1.age)
print(car2.age)

print(Car.__dict__) #    prints all the attributes for the class level
print(car1.__dict__) #  prints all the  attributes for the instance level
"""
print(Car.all)


for instance in Car.all:
    print(instance.name)

for instances in Car.all:
    instances.price = 1000
    print(instances.price)