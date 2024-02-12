import random

Mais_response = input("Are you ready little monkey?\n")

MainLoop = False

if Mais_response == "yes":
    MainLoop = True
else:
    MainLoop = False

while MainLoop:

    score = 0

    one_digit_addition_loop = False
    two_digit_addition_loop = False
    one_digit_multiplication_loop = False
    two_digit_multiplication_loop = False
    EndMessage = False

    response = input("Press 'S' to start\n")

    if response == "S":
        one_digit_addition_loop = True
        print("\nLet's start\n")
    else:
        print("okay")


        

    while one_digit_addition_loop and score <= 50:

        random_int_1 = random.randint(0,9)
        random_int_2 = random.randint(0,9)
        random_int_answer = random_int_1 + random_int_2

        equation = (f"{random_int_1} + {random_int_2}?")
        print(equation)
        
        while int(input()) != random_int_answer:
            print(f"Wrong, {equation}")
        else:
            score += 1
            print(f"Correct, score: {score}")
    else:
        one_digit_addition_loop = False
        two_digit_addition_loop = True

    while two_digit_addition_loop and score <= 100:

        random_int_1 = random.randint(9,99)
        random_int_2 = random.randint(9,99)
        random_int_answer = random_int_1 + random_int_2

        equation = (f"{random_int_1} + {random_int_2}?")
        print(equation)
        
        while int(input()) != random_int_answer:
            print(f"Wrong, {equation}")
        else:
            score += 1
            print(f"Correct, score: {score}")
    else:
        two_digit_addition_loop = False
        one_digit_multiplication_loop = True

    while one_digit_multiplication_loop and score <= 150:

        random_int_1 = random.randint(1,9)
        random_int_2 = random.randint(1,9)
        random_int_answer = random_int_1 * random_int_2

        equation = (f"{random_int_1} * {random_int_2}?")
        print(equation)
        
        while int(input()) != random_int_answer:
            print(f"Wrong, {equation}")
        else:
            score += 1
            print(f"Correct, score: {score}")
    else:
        one_digit_multiplication_loop = False
        two_digit_multiplication_loop = True

    while two_digit_multiplication_loop and score <= 200:

        random_int_1 = random.randint(9,99)
        random_int_2 = random.randint(9,99)
        random_int_answer = random_int_1 * random_int_2

        equation = (f"{random_int_1} * {random_int_2}?")
        print(equation)
        
        while int(input()) != random_int_answer:
            print(f"Wrong, {equation}")
        else:
            score += 1
            print(f"Correct, score: {score}")
    else:
        two_digit_multiplication_loop = False
        EndMessage = True

    if EndMessage == True:
        print("Congrats, you've finished your daily Math Exercise")