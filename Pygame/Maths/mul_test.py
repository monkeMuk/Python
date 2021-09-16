import random

while True:
    x = random.randint(0,99)
    y = random.randint(0,99)
    z = x * y

    print(f"{x} x {y} == ?")
    a = int(input(""))

    if a == z:
        print(f"correct! {a} is the right aswer")
        play_again = input("do you want to continue?")
        if play_again != "yes":
            break
        else:
            continue
        
    else:
        print(f"Wrong! {a} is the wrong answer")
        continue

 
6