'''Python Project #1: Number Guessing Game
The computer will randomly pick a number between one and 100
The user picks their number of guesses and difficulty level'''

#setup introduction 
print("Welcome to Matteo's Number Guessing Game! \n I will pick a number from 1-100. \n Then, you will have a set number of guesses.")

import numpy as np 

solution = np.random.randint(1,101) #computer selects solution

guess = int(input("Now Guess!:"))

print(guess == solution)