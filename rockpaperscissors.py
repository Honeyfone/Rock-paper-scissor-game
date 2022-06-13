# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:15:30 2022

@author: OLADELE KAYODE
"""

import random

# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

while True:
    print('Player pick your choice: rock, paper or scissors')
    choice = str(input())
    choice = choice.lower()

    print("My choice is", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)

    print("Computer choice is", computer_choice)
    if choice in choices:
        if choice == computer_choice:
            print('it is a tie')
        if choice == 'rock':
            if computer_choice == 'paper':
                print('you lose, sorry try again')
            elif computer_choice == 'scissors':
                print('You win!!! Good guess')
        if choice == 'paper':
            if computer_choice =='scissors':
                print('you lose, sorry try again')
            elif computer_choice == 'rock':
                print('You win!!! Good guess')
        if choice == 'scissors':
            if computer_choice == 'rock':
                print('you lose, sorry try again')
            elif computer_choice == 'paper':
                print('You win!!! Good game :)')
    else:
        print('invalid choice, try again')
        
    print()
    
    