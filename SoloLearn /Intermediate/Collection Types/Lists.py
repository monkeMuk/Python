#   Summary

#   List
a = ["b","c","d"]

#   Dictionary
a = {"b":1,"c":2,"d":3}

#   Tuples
a = ("a","b","c")
a = "b","c","d"
#   immutable

















names = ("Adli","nik","abdul")
print(names[2])



#   DICTIONARIES
"""
Allows to assign keys to values



Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be changed.

"""

ages = {
    "Adli":2,
    "nik":4,
    "abdul":5
    }

print(ages["nik"])
print("nik" in ages)

#   get is the same as indexing 

print(ages.get("nik"))
print(ages.get("5"))

#   the second value in .get(x,z) represents what it the value should be if the first value doesn't exist



fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4,0) + fib.get(7, 5))

'''
fib.get(4,0) + fib.get(7, 5) explanation

if 4 doesn't exist, replace it with 0
if 7 doesn't exist, replace it with 5

so 3 + 5 = 8

'''


a = {1:1,2:2,3:2}
print(a.get(1) + a.get(1))


#   Tuples
"""
They're like lists but cannot be changed
"""

cars = ("Myvi","Honda","Proton")
