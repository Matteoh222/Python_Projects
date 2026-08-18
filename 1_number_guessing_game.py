'''Python Project #1: Number Guessing Game
The computer will randomly pick a number between one and 100.
The user picks their number of guesses and whether they want hints or not.'''

#setup introduction 
print("Welcome to Matteo's Number Guessing Game! \n I will pick a number from 1-100. \n Then, you will have a set number of guesses.")

import numpy as np 

solution = np.random.randint(1,101) #computer selects solution
#print(solution)


guesses = int(input("\nNumber of guesses:"))#user picks number of guesses


#function for game with no hints
def hintless(): 
    print('\nNow Guess!')
    for i in range(guesses):
        guess = int(input('\nGuess:')) #accept user's guess
        if guess == solution:
            if i == 0:
                print("Congratulations! You win! Only", i+1, "guess!")
            else:
                print("Congratulations! You win! Only", i+1, "guesses!")
            break
        elif i+1 == guesses:
            print("Oh no! Out of guesses. You lose. The answer was:", str(solution))
        else:
            print("Not quite. Try Again.")
            
#function for game with high/lower hints
def hintfull(): 
    print('\nNow Guess!')
    for i in range(guesses):
        guess = int(input('\nGuess:')) #accept user's guess
        if guess == solution:
            if i == 0:
                print("Congratulations! You win! Only", i+1, "guess!")
            else:
                print("Congratulations! You win! Only", i+1, "guesses!")
            break
        elif i+1 == guesses:
            print("Oh no! Out of guesses. You lose. The answer was:", str(solution))
        else:
            if guess > solution:
                print("Not quite. Try Again. Lower next time.")
            elif guess < solution: 
                print("Not quite. Try Again. Higher next time.")

#ask if user wants hints
hints = (input("\nWould you like hints (will tell you if you are higher or lower than the number?) y/n: "))
if hints == 'y':
    hintfull()
elif hints == 'n':
    hintless()