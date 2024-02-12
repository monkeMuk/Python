#   CLASS ATTRIBUTE

class Pets:
    len_of_names = 5
    #   class attributes 
    #   specific to the class


    def __init__(self,name):
        self.name = name
        #   Pets.len_of_names += 1 
        #   or
        Pets.add_len_of_names()

    #   CLASS METHOD

    @classmethod
    def return_len_of_names(cls):
        return cls.len_of_names

    @classmethod
    def add_len_of_names(cls):
        cls.len_of_names += 1
    #   only adds to the ones on line 3 and  4


P1 = Pets('A')
print(P1.len_of_names)
P2 = Pets('B')
print(P2.len_of_names)

print(Pets.return_len_of_names())


#   static method dont change anything// still not too sure

class Math:
    @staticmethod
    def mul10(x):
        return x*10

    @staticmethod
    def mul20(x):
        return x*20
    
    @staticmethod
    def pr():
        print("run")
    

print(Math.mul10(2))
Math.pr()