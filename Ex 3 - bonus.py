# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:27:26 2024

@author: Peter Duane
"""

"""
Exercise 3 = Biography
"""

name=(input("Enter your name: ")) #interacts with the user to enter their name here.
hometown=(input("Enter your hometown: ")) #interacts with the user to enter their hometown here.


while True: #"while" creates a loop that ensures that the user inputs the correct alpha-numerical character.
    age=(input("Enter your age: ")) #interacts with the user to enter their age here.
    try: #"try" defines the "number=int(age)" and test for errors as it is being executed.
        number=int(age) #this command makes the "age" variable be answerable by numbers/integers only, transforming a string to an integer.
        break #breaks the while loop
    except: #handles the error and responds to it accordingly without troubling the program.
        print("Please enter a digit") #the response of "except" command.
    
biography = ['Name:', name, 'Hometown:', hometown, 'Age:', number] #compiled information that the user typed in every input command.
print(biography) #translates the whole list to the program and showcases the compilation of information.