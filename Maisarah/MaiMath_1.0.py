import random


response = input("Hiiiiiii Mooooooooodyyyy, the cutest girl in the world, are you ready  ")

MainLoop = False

if response == "yes":
    MainLoop = True
else:
    MainLoop = False

while MainLoop:

    score = 0

    mul_loop = False
    div_loop = False
    add_loop = False
    minus_loop = False

    #   Addition starts
    user_response = input("Are you ready for addition bambam? ")

    if user_response == "yes":
        add_loop = True
    else:
        print("Okayyyyyy, finnneeeee")

    while add_loop and score < 20:

        random_int_1 = random.randint(1,100)
        random_int_2 = random.randint(1,100)

        answer = random_int_1+random_int_2

        equation = (f"{random_int_1}+{random_int_2} = ? ")
        print(equation)

        while int(input()) != answer:
            print(f'Incorrect.\n{equation}')
        else:
            score += 1
            print(f"correct, score: {score}")
    else:
        print("Okay, time for subtraction, Mr Baby boss")
        add_loop = False
        minus_loop = True 

    while minus_loop and score < 40:

        random_int_1 = random.randint(50,100)
        random_int_2 = random.randint(1,49)

        answer = random_int_1-random_int_2

        equation = (f"{random_int_1}-{random_int_2} = ? ")
        print(equation)

        while int(input()) != answer:
            print(f'Incorrect.\n {equation}')
        else:
            score += 1
            print(f"correct, score: {score}")
    else:
        print("Time for multiplication cute little monkey")
        minus_loop = False
        mul_loop = True

    while mul_loop and score < 60:

        random_int_1 = random.randint(2,9)
        random_int_2 = random.randint(2,9)

        answer = random_int_1*random_int_2

        equation = (f"{random_int_1}x{random_int_2} = ? ")
        print(equation)

        while int(input()) != answer:
            print(f'Incorrect.\n{equation}')
        else:
            score += 1
            print("correct, score: {score}")
    else:
        print("Time for division big girl")
        mul_loop = False
        div_loop = True
    

    while div_loop:

        random_int_1 = random.randint(1,100)
        random_int_2 = random.randint(1,10)

        answer = random_int_1/random_int_2

        equation = (f"{random_int_1}/{random_int_2} = ? ")
        print(equation)

        while int(input()) != answer:
            print(f'Incorrect.\n{equation}')
        else:
            print("correct")

