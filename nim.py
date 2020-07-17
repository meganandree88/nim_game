'''
File name: nim.py 
Homework # 8
Part 1
This file contains the neccessary functions for a game named Nim played between a user and the computer.  The player and the computer take turns removing objects from a pile until there is a winner. 
'''

import sys
import random

def printScore(playerCount, computerCount):
    '''
    This function prints out the score of all of the games. This function prints
    out the number of times the player(user) has won and the number of times
    the computer has won.
    This function has two inputs: playerCount and computerCount
    '''
    print('**************')
    print('Player:', playerCount, '\tComputer:', computerCount)

def checkPlayer(newCurrent, playerCount, computerCount):
    '''
    This function checks the pile during the user's turn to see if the 
    user has won. If the user has won, this function calls the printScore
    function. 
    This function has three inputs: newCurrent, playerCount, and computerCount
    This function has one output: playerCount
    '''
    if newCurrent == 1:
        playerCount = playerCount + 1
        print('Yay! You won!')
        print('Current Score')
        printScore(playerCount, computerCount)
    return playerCount

def computerTurn(newCurrent):
    '''
    This function takes the turn of the computer.  It generates
    a random number between 1 and 3.  If the random number is 
    larger or equal to the current size of the pile, this function
    will generate a new random number until the random number is smaller 
    than the pile size.  The function will then calculate the new current 
    pile size. 
    This function has one input: newCurrent
    This function has one output: newCurrent
    '''
    if newCurrent <= 4:
        compChoice = newCurrent - 1

    else:
        compChoice = random.randint(1,3)
        while newCurrent - compChoice <= 0:
            compChoice = random.randint(1,3)
    newCurrent = newCurrent - compChoice
    print('Computer removed: ', compChoice)
    return newCurrent

def checkComputer(newCurrent, playerCount, computerCount):
    '''
    This function checks the pile during the computer's turn to see if the 
    computer has won.  If the computer won, this function will call the
    printScore function.
    This function has three inputs: newCurrent, playerCount, computerCount
    This function has one output: computerCount
    '''
    if newCurrent == 1:
        computerCount = computerCount + 1
        print('The computer won!')
        print('Current Score')
        printScore(playerCount, computerCount)
    return computerCount

def main():
    playAgain = 'y'

    #prints out a welcome statement
    print('Welcome to Nim!')
    print('***************')

    playerCount = 0
    computerCount = 0
    
    while playAgain == 'y':

        #generate a random number for the pile size between 9 and 21
        currentSize = random.randint(9,21)

        while currentSize != 0:

            #prints the current size of the pile
            print('Current pile size: ', currentSize)

            #prompts the user for an input and sets the input to a variable
            choice = input('Do you want to remove 1, 2, or 3 items? "q" to quit:')
            #if the user input is 'q', calls the printScore function
            if choice == 'q':
                print('Final Score')
                printScore(playerCount, computerCount)
                sys.exit(0)

            elif choice == '1' or choice == '2' or choice == '3':

                #if the user input is larger than the current pile size--> incorrect
                if int(choice) >= currentSize:
                    print('You did not enter a valid number.')
                
                else:
                    #calculates the new pile size
                    currentSize = currentSize - int(choice)

                    #checks to see if the user has won the game
                    if checkPlayer(currentSize, playerCount, computerCount) > playerCount:
                        playerCount = playerCount + 1
                        break 
                    else:

                        #takes the turn of the computer and checks to see if the computer has won
                        currentSize = computerTurn(currentSize)
                        if checkComputer(currentSize, playerCount, computerCount) > computerCount:
                            computerCount = computerCount + 1
                            break
                
            else: #if the user input is not a valid number or q, the user has entered an incorrect choice
                print('You did not enter a valid choice.')

        #prompts the user to play again
        playAgain = input('Would you like to play again? (y/n)')

        #stops the game if the user does not want to play again
        if playAgain == 'n':
            print('Final Score')
            printScore(playerCount, computerCount)
            break
        
main()
