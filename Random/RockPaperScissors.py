import random
def play():
    user = input("insert rock, paper, or scissors: ").lower
    comp_choice = random.choice(["rock","paper","scissors"])

    if user == comp_choice:
        print("Tie")

    if user == "rock" and comp_choice == "scissors":
        print("Player wins | computer picked " + comp_choice)
    if user == "paper" and comp_choice == "rock":
        print("Player wins | computer picked " + comp_choice)
    if user == "scissors" and comp_choice == "rock ":
        print("Player wins | computer picked " + comp_choice)
    else:
        print("Player loses | computer picked " + comp_choice)


play()