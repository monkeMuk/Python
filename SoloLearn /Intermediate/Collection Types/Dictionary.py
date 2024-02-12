a = {"b":1,"c":2,"d":3}

#   prints the value of key "b"
print(a["b"])

#   finds the first value and if it doesn't exist, uses the 2nd value 
print(a.get("e","Doesn't exist "))

#   prints the keys
print(a.keys())
#   prinths the values
print(a.values())
#   prints both keys and values
print(a.items())

#    Loops through the dict and prints the values
for key, value in a.items():
    print(value)

print()