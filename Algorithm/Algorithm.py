x = [1,2,3,4,5,6,7,8,9,10]

target_number = 5

for target in x:
    if target == target_number:
        print(f"{target_number} is the target number")
        break
    else:
        print(f"{target}")

