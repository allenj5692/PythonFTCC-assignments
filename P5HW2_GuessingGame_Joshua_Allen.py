# Guessing Game
# 4/20/2018
# CTI-110 P5HW2 - Random Number Guessing Game
# Joshua Allen

#import random and import sys to start the random number generator and the ability to stop the program
import random
import sys
# start of the program
def guessNumber():
    number = random.randint(1, 100)
    guesses = 1
    guess = int(input("Can you guess the number I am thinking of? "))

    while (guess != number):
        if guess > number:
            print ("The number is lower than " + str(guess))
        else:
            print ("The number is higher than " + str(guess))
        guesses += 1
        guess = int(input("Try to guess the number again: "))
    print ("You are correct! The number was " + str(number))
    print ("You were able to guess the correct number in " + str(guesses) + " guess.")

    again = str(input("Do you want to play again (type yes or no): "))
    if again == "yes":
        guessNumber()
    else:
        
        sys.exit(0)
  
guessNumber()

