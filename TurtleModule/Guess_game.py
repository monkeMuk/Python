import random

start = int(input("start | "))
if start <= -1:
    print("Start must be larger than -1")
    quit()
end = int(input("end   | "))

r = random.randint(start,end)
guesses = 0

while True:
    user_guess = int(input("Make a guess  | "))
    guesses += 1

    if user_guess == r:
        print("✅")
        print("You had "+ str(guesses) + " guesses")
        break
    elif user_guess > r: 
        print("Your answer too high!")
        continue
    elif user_guess < r:
        print("Your answer is too low!")
        continue




#random.randint(10)   /includes 10
#random.randrange(10) /does not include 10