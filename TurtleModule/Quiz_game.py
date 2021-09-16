print("Welcome to my history quiz")

playing = input("Are you Maisarah? ")

if playing.lower() != "yes":
    print("❌")
    quit()

print("Okay, mai, let's play now :) ")
score = 0

#Question 1
answer = int(input("What year was Maisarah born in?"))                
if answer == 2012:
    print("✅")
    score += 1
else:
    print("❌")

#Question 2
answer = input("Where did Maisarah study before coming to BrainyBunch? ")
if answer.lower() == "kinderfun":
    print("✅")
    score += 1
else:
    print("❌")

#Question 3
answer = int(input("How old would grandmaisarah be in 2050? "))
if answer == 38:
    print("✅")
    score += 1
else:
    print("❌")

print("Congratulations Maisarah my little monkey <3 ")
print("You have achieved " + str(score) + " marks")
print("You have achieved " + str((score/3)*100) + "%")

