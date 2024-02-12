a = ["b","c","d"]


#   prints the last element in the list 
print(a[-1])

#   prints how many elements  are in the list
print(len(a))

#   printing a specfici element usign index
print(a[0])

"""
a = ["b","c","d"]

first element is always 0
so,

b = 0 
c = 1
d = 1

"""


# prints elements that inhibit index 0 till but not 2 ( so 0 - 1)
print(a[0:2])

#   adds "e" into the list 
a.append("e")
print(a)

#   insert takes the index u want the element to inhibit and the actual element- does not replace original element but instead just +1 it 
a.insert(0,"f")
print(a)


#   removes the last element in the list
a.pop()
print(a)

#   prints the list but in reversed order
a.reverse()
print(a)

#   sorts it in alphabetical order
a.sort()
print(a)


#   finds the index of a specific value
print(a.index("c"))


#   finding out if a specific element is in a course or not 
print("g" in a)
print("g" not in a)




#   find value and index of all the elements , start = 1 makes sure the indexs start at 1   
for index,course in enumerate(a, start=1):
    print(index,course)

#   s

""" 
------------------------
"""



num = [1,2,3,4]

print(min(num))
print(max(num))
print(sum(num))