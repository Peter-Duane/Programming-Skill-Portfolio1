# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:07:31 2024

@author: Peter Duane
"""

"""
Exercise 6 = Brute Force Attack
"""

password = ('Password') #using variable to store the correct password
count = 5 #the total number of attempts the user can do 

while count > 0:
    count -= 1 #subtracts the variable "count" every 1 time the user fails to input the correct password
    log_in = input("Enter the password: ") #interacts with the user to input the correct password 
    if log_in == password: #if the user inputs the correct password, the program will respond this way
        print("Welcome!")
        break #breaks the 'while' loop 
    else: #but if the user fails to input the correct password, it will trigger this command until the certain number of attempts is diminished
        print("Please try again.")
        print("You have",{count},"attempts left")
    if count == 0: #after the number of attempts is finished, the program will block the user from answering again.
        print("Page locked: Failed to input the correct password")
    
    
    
        