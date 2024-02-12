#Dictionaries

names = {"Alex":2,"ADA":3,"ARMAN":5,"AVA":7}
print(names["Alex"])
names["Arman"] = 3
print(names["Arman"])
print("Jack" in names)
print("Alex" in names)
print("AVA" not in names)
print(names.get("ADA"))
print(names.get("Alisa"))

#Tuples

food = ("chicken","fried","rice","egg")
print(food[1])
"""
food["chicken"] = "Oil"
print(food)

#Error
"""

#list slices

name = "Barack Obama"
print(name[::-1])

name = "Alice","Elbert","Bob","efram"
print(name[1:3])

sq = [i**2 for i in range(5)]
print(sq)

#string formatting

print("{0}{1}{0}{1}{0}{1}{2}".format("H","A","k"))

a = "{x}, {y}".format(x=5, y=12)
print(a)

str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)

