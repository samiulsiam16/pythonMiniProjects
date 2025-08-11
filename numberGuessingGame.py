# Make a game to guess the number

import random       # random module helps us to create random numbers or characters.

target=random.randint(1,100)

while True:
    userGuess = input("Guess the target or Quit(Q) :")
    if(userGuess == "Q"):
        break
    
    userGuess = int(userGuess)
    if(userGuess == target):
        print("Success : Correct Guess!")
        break
    elif(userGuess>target):
        print("Your guess is too big. Take a small guess.")
    else:
        print("your guess is too small. Take a big guess.")

print("-----GAME OVER-----")
