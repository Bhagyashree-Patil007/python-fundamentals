#Guess The Number:mini project

import random

number=random.randint(1,100)

while True:
    userchoice=input("guess the number or quit")
    if (userchoice=="quit"):
        break

    userchoice=int(userchoice)
    if(userchoice==number):
        print("Guess Succesfull!...")
        break
    elif(userchoice<number):
        print("guess the bigger number")
    else:
        print("guess the smaller number")

print("Game Over!...")


