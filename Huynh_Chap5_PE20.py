#=======================================================================================
#Author:        Tracy Huynh
#Program ID:    Huynh_Chap5_PE20.py
#Due Date:      04/29/2019
#Description:   This program generates a random number from 1 to 100
#               and prompts the user to guess it. Tracks the number of tries
#               and gives the user an option of quitting or playing again. 
#=======================================================================================

# Import random module from libaray
import random

def main():
    # Initialize the main loop variable
    keep_going = 'y'

    # main loop iterates as long as the user wants to play
    while keep_going == 'y' or keep_going == 'Y':
        number = random.randint(1,100)

        # Get the user's guess
        print("Enter an integer number between 1 and 100, or 0 to quit", end='')
        guess = int(input(": "))

        # Call the guessTheNumber function and pass two variables as arguments

        guessTheNumber(number, guess)

        # Check to see if the user wants to play again
        # if user does not want to play, display message
        keep_going = input("Keep going (y to continue)?: ")
        if keep_going != 'y' and keep_going != 'Y':
            print("Thanks for playing!")
        
def guessTheNumber(number, guess):
    # Inner loop iterates as long as the user wants to guess the number
    # Set tries to 0 to accumulate number of tries
    tries = 0
    while guess != 0:
        if guess > number:
            print("Too high, try again")
            tries += 1
            print("Enter an integer number between 1 and 100, or 0 to quit", end='')
            guess = int(input(": "))
            
        elif guess < number:
            print("Too low, try again")
            tries += 1
            print("Enter an integer number between 1 and 100, or 0 to quit", end='')
            guess = int(input(": "))

        else:
            print()
            tries += 1
            print("Congratulations! You guessed the right number!",
                  "\nYou guessed the number in", tries, "tries!")
            return
        
    # User entered 0 to quit                   
    print()                             # Print a statement without argument         
    print("You quit to early.",         # Print total attempts and correct number
          "\nTotal attempts: ", tries,
          "\nThe number was: ", number)
        


# Call the main function
main()
            
    
    
        
    
