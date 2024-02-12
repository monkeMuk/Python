
# Optional Parameters

from typing import AsyncGenerator


def mul_Sev(x):
    return x*7

print(mul_Sev(4))

def repeat_five(x,y=5):
    return x * y
print(repeat_five("Mai ",2))

#Static Class and Methods

class Student:
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.weight = w

    #Class method
    def Class_population(cls):
        return cls.popu
    #Static method
    def isHeavy(w):
        return w >= 80
    def isMature(a):
        return a >= 15
    
    def display(self):
        print(f"{self.name} is {self.age} years old and is {self.weight} kg")

    
A = Student("Nik",14,94)
A.display()
    
# Static and Class methods still needs revision

#map() function takes 2 arguments; the function and the list

A = [1,2,3,4,5]

def sqr(x):
    return x**x

print(list(map(sqr,A)))
print([sqr(x) for x in A])

#Converts a lost from m to cm
height_meters = 1.76,1.89,1.56,1.56

def m_to_cm(x):
    return x*100

print([m_to_cm(i) for i in height_meters])
print(list(map(m_to_cm,height_meters)))

#Filter() function

Weight = 43,56,98,97,53,76

def Heavy(x):
    return x >= 60
def Light(x):
    return x <= 59

H_G = list(filter(Heavy,Weight))
L_G = list(filter(Light,Weight))
print(H_G)
print(L_G)

#lambdas/ they also mean anonymous function

def B(x):
    A = lambda x: x*2
    return A(x)*3
print(B(2))

foo = lambda x,y,z: x+y*z
print(foo(2,4,3))

A = 1,2,3,4,5,6,7,8,9,10
print(list(filter(lambda x: x%2 == 0, A)))
print(list(filter(lambda x: x%2 != 0,A)))

#Collections/Counter()
import collections
from collections import Counter

c = Counter(a=1,b=2,c=3,d=4)
d = ["a","b","b","c","c","c","d","d","d","d"]
c.subtract(d)
print(c)
#list c gets subtracted from list d

c.update(d)

print(c)
print(c.clear())
#list c gets + from list d


#or

print(c+d)
print(c-d)
print()




"""
print(list(c.elements()))
print(list(c.most_common(1)))
"""