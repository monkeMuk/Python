class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Man(Human):
    def __init__(self,name,age,colour):
        super().__init__(name,age)   # runs self.name = name self.age = age
        self.colour = colour

    def speak(self):
        print("Hi")
    
    def say(self):
        print(f"I am {self.name} and I am {self.age} years old and I like {self.colour}")

class Woman(Human):
    def __init__(self,name,age,food):
        super().__init__(name,age)   # runs self.name = name self.age = age
        self.food = food

    def speak(self):
        print("Bye")

    def say(self):
        print(f"I am {self.name} and I am {self.age} years old and I like {self.food}")


h = Human("nik",43)

alfred = Man("alfred",24,"red")
alfred.say()

Allie = Woman("Allie",25,"peas")
Allie.say()