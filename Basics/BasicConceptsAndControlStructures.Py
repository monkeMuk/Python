print (2 == 3)

print (2 != 2)

if 10 >= 5:
    print("yes")
else:
    print("no")

if 10 >= 7:
    print("10 is bigger than 7")
elif 10 == 4:
    print("10 is equal to 4")

a = 2
b = 2

if a == 5 and b == 4:
    print("both right")
elif a == 5 or b == 3:
    print("One of em is right")
elif not a == 5 and not b == 6:
    print("both wrong")

age = 25
money = 1000

if age >= 18 and age <= 30:
    print("come in")
elif age >= 18 and money >= 1000:
    print("come in")
elif age <= 18 or money <= 500:
    print("cannot come in")

n = [ "James", "Jani", "Albert", "Nik"]
print(n[1])

str = "Hi my name is Zuzie"
print(str[0])

letters = ["A","B","C","D","E"]
letters[0] = "F"
print("A" in letters)
print("G" in letters)
print(not "C" in letters)
letters.append("H")
print(letters)
print(len(letters))

nums = [ 1, 2, 3 ]
nums.append( 4 )
print( nums )
print(len(nums))

s = [ "My", " name ", " nik " ]
s.insert(2, " is ")
print(s)
print(s.index("My"))

a = 1 
while a <= 5:
    print(a)
    a = a + 1
print("Finished")

x = 1
while x <= 10:
    print(x)
    x = x + 1
    if x == 4:
        print("It's four")
        continue
    if x == 8:
        print("It's 8")
        break
    

q = ["A","b","c","d","e"]
print(q[::-1])

p = ["a","b","c","d"]
for i in p:
    print( i + "A" )

a = "MaisarahMaisarah"
letters = 0

for x in a:
    if( x == "a" or "a"):
        letters += 1
print(letters)
    
n = list(range(5))
print(n)

x = "Mukhriz"
print(x[::-1])

p = ["a","b","c","d"]
for i in p:
    print( i + "A" )

a = "MaisarahMaisarah"
letters = 0

for x in a:
    if( x == "a" and "a"):
        letters += 1
print(letters)

n = list(range(5))
print(n)
print(n[2])
    
m = list(range(5,10))
print(m)
print(m[3])

a = list(range(0,20,2))
print(a)

for i in range(3):
    print("Maisarah")

# Celcius to Fahrenheit calculator
C = 20
F = (C*2)+30
print(F)

