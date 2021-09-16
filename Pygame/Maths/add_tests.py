import random


x = random.randint(0,99)
y = random.randint(0,99)
z = x + y


while True:
    print(f"{x} + {y} == ?")
    a = int(input(""))

    if a == z:
        print(f"correct! {a} is the right aswer")
        break
    else:
        print(f"Wrong! {a} is the wrong answer")
        continue
