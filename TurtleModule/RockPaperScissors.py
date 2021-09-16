import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Type in Rock/ Paper/ Scissors or  Q tp quit. | " ).lower()
    if user_input == "q":
        break
    if user_input not in options:
        print('Answer invalid, try again')
        continue
    random_number = random.randint(0,2)
    #rock = 0, paper = 1, scissor = 2
    computer_pick = options[random_number]
    print("Computer picks " + computer_pick + ".")

    #winning conditions below

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")

    else:
        print("Computer wins!")
        computer_wins += 1

print("You have "+ str(user_wins) + " points" ) 
print("The computer has " + str(computer_wins) + " points")   
print("thank you for playing <3")           
    
