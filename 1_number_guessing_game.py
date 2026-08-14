'''Python Project #1: Number Guessing Game
The computer will randomly pick a number between one and 100
The user picks their number of guesses and difficulty level'''

#setup introduction 
print("Welcome to Matteo's Number Guessing Game! \n I will pick a number from 1-100. \n Then, you will have a set number of guesses.")

import numpy as np 

solution = np.random.randint(1,101) #computer selects solution
print(solution)

guesses = int(input("Number of guesses:"))#user picks number of guesses


def hintless(): 
    print('Now Guess!')
    for i in range(guesses):
        guess = int(input('Guess:')) #accept user's guess
        if guess == solution:
            if i == 0:
                print("Congratulations! You win! Only", i+1, "guess!")
            else:
                print("Congratulations! You win! Only", i+1, "guesses!")
            break
        elif i+1 == guesses:
            print("Oh no! Out of guesses. You lose.")
        else:
            print("Not quite. Try Again.")

hintless()