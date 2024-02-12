import random

def guess(x):
    random_number=random.randint(1,5)
    if x < random_number:
        print("Too low")
    if x > random_number:
        print("Too high")
    if x == random_number:
        print("Correct")

guess(5)

