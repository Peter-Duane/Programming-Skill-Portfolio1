# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:44:39 2024

@author: Peter Duane
"""

"""
Exercise 8 = Simple Search
"""

names=["Jake","Zac","Ian","Ron","Sam","Dave"] # A variable of list of all the names that are meant to be searched by the user.
print("These are list of names: ", (names)) # This will print the names so that the system can show the list.

question = (input("Whose name do you want to find? ")) # This will interact with the users and where they can type the name they want to find.
found = False # this variable will support the if-else statement later.
                # this variable is false because as long as the user types a name that is not on the list, the system will recognize and act accordingly instead of malfunctioning.
Names = [] # this variable helps separate a name in the set of variables.
for name in names: # name is the variable, and names is the dictionary, this command separates the specific string from the set of strings.
    if question.title() in name.title(): # if the question connects with a name on the list, it will be recognized by the program, then separate in from within the list.
                                        # .title helps the users type their input in any capitalization which prevents the system from not recognizing the user's input.
        Names.append(name) # Adds an element by the end of the list in which the 'Names' is the primary variable that puts the 'name' (secondary variable) into that primary variable.
        found = True # this variable is changed from 'False' to 'True' if the question recognizes the name that is typed in by the user.
        
if found: # As we see here, if the user inputs a name that is recognized by the program, the 'found' variable is changed to 'True'.
    print("Name found! The name you are searching for is...", Names) # Which then prints the name that the user is finding.
else: # if the user inputs a name that is not on the list, the 'found' variable will remain 'False' which then prints that there is no such name in the dictionary.
    print("Name not found, Please try again.")



