#Working with a while loop

#Printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Importing random and writing a while loop

import random

#enter a statement that will generate a random number between 1 and 10 by 
#using the randint() function of the random module.

number = random.randint(1,10)

isGuessRight = False

#handle the game logic, create a while loop:
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        
        
        #Writing the for loop
        
for x in range (0, 11):
    print(x)