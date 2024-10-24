# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:39:31 2024

@author: Peter Duane
"""

"""
Exercise 4 = Primitive Quiz
"""
print("Guess the Capital Quiz")
print("Europe Edition")
print("**********************")

import random # import helps the programmer to use outdated or new commands from other updates of python if it isn't recognized by the current version.

countries={
    'France': 'Paris',
    'Greece': 'Athens',
    'Portugal': 'Lisbon',
    'Russia': 'Moscow',
    'Sweden': 'Stockholm',
    'United Kingdom': 'London',
    'Spain': 'Madrid',
    'Italy': 'Rome',
    'Denmark': 'Copenhagen',
    'Austria': 'Vienna'
} # dictionary of every country in Europe and their respective capitals.
States=list(countries.keys()) # variable makes the program recognize every key in the dictionary as a separate group.
point=0 # current score of the player at the start of the quiz.
for state in random.sample(States, 10): # for state in random.sample helps to execute an instruction for a specific number of iterations.
                                        # this means that the commands below will trigger until the corresponding number(10x) has been reached.
                                        # random.sample also helps to separate each key into each question without repeating any key value.
    capital = countries[state] # this variable is recognized as the capitals in the key-value dictionary, which are also the answer to every question.
    question = input('What is the capital of %s? ' %state ) # this variable interacts with the user and enables them to answer the question provided.
                    # %s acts as an anchor for the %state which enables to convert it to the corresponding string variable.
                    # %s only works for string variables (words/letters)
    if question.title() == capital: # this if statement triggers if the user made the correct answer.
                                    # (question).title() helps the program recognize the input of the user regardless of the capitalization.
        point+=1 # every time that the user types in the correct answer, the system will add one point to the current score.
        print('Correct! Your score is %d/10' %point) # %d acts as an anchor for integers instead of string values
                                                     # which enables the program to input the corresponding variable without having to change it manually periodically.
    else: # this else statement will trigger if the user made an incorrect answer.
        print('Incorrect. Your score is %d/10' %point)
print('You made it till the end, Congratulations! Your score is %d/10' %point)
# ^ this print should trigger in the end after the user has completed the quiz and should show the user their last recorded score (%point).